# Change History for nasa.json (Part 17)

### Changes from 31606f9 to dd2190f (Part 6/162)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
                     "@type": "dcat:Distribution",
+                    "description": "Web Map Service Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/lecz-urban-rural-population-land-area-estimates-v2/maps/services",
+                    "mediaType": "text/html",
                     "title": "Use Web Map Service (WMS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/lecz-urban-rural-population-land-area-estimates-v2",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/lecz-urban-rural-population-land-area-estimates-v2",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Maps Download Page",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/lecz-urban-rural-population-land-area-estimates-v2/maps",
+            "identifier": "C1000000400-SEDAC",
+            "issued": "2013-12-31",
+            "keyword": [
+                "population",
+                "earth science",
+                "human dimensions"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4MW2F2J",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2013-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/H4TM782G",
+                "https://doi.org/10.7927/H4CC0XMD"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 -58.0 180.0 85.0",
+            "temporal": "1990-01-01T00:00:00Z/2100-01-01T00:00:00Z",
             "theme": [
                 "LECZ",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Low Elevation Coastal Zone (LECZ) Urban-Rural Population and Land Area Estimates, Version 2"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ULY-J-SCE-3-RDR-DOPPLER-HIRES-V1.0",
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
-                "jupiter",
-                "ulysses"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Ulysses spacecraft was occulted by the Io Plasma Torus (IPT) during its Jupiter encounter on 8 February 1992. The Ulysses dual-frequency radio subsystem used by the Ulysses Solar Corona Experiment (SCE) was utilized to measure the electron content (column density) of the IPT [BIRDETAL1992B]. In the nominal mode for radio-sounding observations [BIRDETAL1992A], both downlinks (S-band: f_s = 2.3 GHz X-band: f_x = 8.4 GHz) are phase coherent with the uplink (S-band: f_u = 2.1 GHz). The dual-frequency radio-sounding technique exploits the dispersive nature of ionized media on the propagation of the two downlinks. The tiny Doppler shift due to plasma moving in and out of the ray path is greater at S-band than at the higher frequency X-band.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.uly-j-sce-3-rdr-doppler-hires-v1.0_2w4c-84xj",
+            "issued": "2018-06-26",
+            "keyword": [
+                "jupiter",
+                "ulysses"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ULY-J-SCE-3-RDR-DOPPLER-HIRES-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.uly-j-sce-3-rdr-doppler-hires-v1.0_2w4c-84xj",
-            "description": "The Ulysses spacecraft was occulted by the Io Plasma Torus (IPT) during its Jupiter encounter on 8 February 1992. The Ulysses dual-frequency radio subsystem used by the Ulysses Solar Corona Experiment (SCE) was utilized to measure the electron content (column density) of the IPT [BIRDETAL1992B]. In the nominal mode for radio-sounding observations [BIRDETAL1992A], both downlinks (S-band: f_s = 2.3 GHz X-band: f_x = 8.4 GHz) are phase coherent with the uplink (S-band: f_u = 2.1 GHz). The dual-frequency radio-sounding technique exploits the dispersive nature of ionized media on the propagation of the two downlinks. The tiny Doppler shift due to plasma moving in and out of the ray path is greater at S-band than at the higher frequency X-band.",
-            "title": "ULY JUP SCE DOPPLER HI-RES DATA",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ULY JUP SCE DOPPLER HI-RES DATA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCMIP-3-PRL1-V3.0",
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
+            "description": "This archive contains data from the RPC-MIP instrument onboard ROSETTA Orbiter acquired during the PRELANDING mission phase between 2014/01/21 and 2014/07/22. The primary target was comet 67P/C-G. It also contains documentation which describes the RPC-MIP experiment. The data archived in this data set conform to the Planetary Data System Standards, Version 3.6. This is V3.0 updated after Science Review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcmip-3-prl1-v3.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCMIP-3-PRL1-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcmip-3-prl1-v3.0",
-            "description": "This archive contains data from the RPC-MIP instrument onboard ROSETTA Orbiter acquired during the PRELANDING mission phase between 2014/01/21 and 2014/07/22. The primary target was comet 67P/C-G. It also contains documentation which describes the RPC-MIP experiment. The data archived in this data set conform to the Planetary Data System Standards, Version 3.6. This is V3.0 updated after Science Review.",
-            "title": "ROSETTA-ORBITER 67P RPCMIP 3 PRL1 V3.0",
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
+            "title": "ROSETTA-ORBITER 67P RPCMIP 3 PRL1 V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/ORACLES_Model_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2021-04-12. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/ORACLES_Model_Data_1.",
-            "issued": "2021-03-01",
-            "temporal": "2016-08-27T00:00:00Z/2018-10-27T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-19",
-            "keyword": [
-                "aerosols",
-                "atmospheric temperature",
-                "atmosphere",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Paquita Zuidema",
                 "hasEmail": "mailto:pzuidema@miami.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2040492215-LARC_ASDC",
             "description": "ORACLES_Model_Data consists of model-derived estimates for aerosol time since emissions (days), calculated with the Weather Research and Aerosol Aware Microphysics (WRF-AAM) Model collected for the ObseRvations of Aerosols above CLouds and their intEractions sub-orbital (ORACLES) campaign. Data collection is complete, and data is available for all three deployments (August 19, 2016 \u2013 October 27, 2016; August 1, 2017 \u2013 September 4, 2017; September 21, 2018 \u2013 October 27, 2018).\r\n\r\nSouthern Africa produces almost one-third of the Earth\u2019s biomass burning aerosol particles. The ORACLES (ObseRvations of Aerosols above CLouds and their intEractionS) experiment was a five year investigation with three intensive observation periods (August 19, 2016 \u2013 October 27, 2016; August 1, 2017 \u2013 September 4, 2017; September 21, 2018 \u2013 October 27, 2018) and was designed to study key processes that determine the climate impacts of African biomass burning aerosols. ORACLES provided multi-year airborne observations over the complete vertical column of the key parameters that drive aerosol-cloud interactions in the southeast Atlantic, an area with some of the largest inter-model differences in aerosol forcing assessments. These inter-model differences in aerosol and cloud distributions, as well as their combined climatic effects in the SE Atlantic are partly due to the persistence of aerosols above clouds. The varying separation of cloud and aerosol layers sampled during ORACLES allow for a process-oriented understanding of how variations in radiative heating profiles impact cloud properties, which is expected to improve model simulations for other remote regions experience long-range aerosol transport above clouds. ORACLES uses two NASA aircraft, the P-3 and ER-2. The P-3 was used as a low-flying platform for simultaneous in situ and remote sensing measurements of aerosols and clouds in all three campaigns, supplemented by ER-2 remote sensing in 2016. ER-2 observations will be used to enhance satellite-based remote sensing by resolving variability within a particular scene, and by guiding the development of new and improved remote sensing techniques.",
-            "graphic-preview-description": "ORACLES Enhanced Modis Airborne Simulator (eMAS) Data",
-            "title": "ORACLES Model Derived Measurements",
-            "graphic-preview-file": "https://mas.arc.nasa.gov/data/deploy_html/oracles_home.html",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FORACLES_Model_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FORACLES_Model_Data_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espo.nasa.gov/oracles",
-                    "description": "ESPO home page for ORACLES",
                     "@type": "dcat:Distribution",
+                    "description": "ESPO home page for ORACLES",
+                    "downloadURL": "https://espo.nasa.gov/oracles",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
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
-                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/ORACLES_Model_Data_1",
-                    "description": "DOI data set landing page for ORACLES_Model_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for ORACLES_Model_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/ORACLES_Model_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://mas.arc.nasa.gov/data/deploy_html/oracles_home.html",
-                    "description": "ORACLES Enhanced Modis Airborne Simulator (eMAS) Data",
                     "@type": "dcat:Distribution",
+                    "description": "ORACLES Enhanced Modis Airborne Simulator (eMAS) Data",
+                    "downloadURL": "https://mas.arc.nasa.gov/data/deploy_html/oracles_home.html",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://airbornescience.nasa.gov/content/An_overview_of_the_ORACLES_ObseRvations_of_Aerosols_above_CLouds_and_their_intEractionS_0",
-                    "description": "ORACLES Mission Overview",
                     "@type": "dcat:Distribution",
+                    "description": "ORACLES Mission Overview",
+                    "downloadURL": "https://airbornescience.nasa.gov/content/An_overview_of_the_ORACLES_ObseRvations_of_Aerosols_above_CLouds_and_their_intEractionS_0",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://airbornescience.nasa.gov/category/Mission/ORACLES",
-                    "description": "NASA Airborne Science ORACLES Posts",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Airborne Science ORACLES Posts",
+                    "downloadURL": "https://airbornescience.nasa.gov/category/Mission/ORACLES",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/centers/ames/earthscience/news/Making-It-Work-In-The-Field-With-Oracles",
-                    "description": "NASA.gov Article \u201cMaking It Work in the Field with ORACLES\u201d",
                     "@type": "dcat:Distribution",
+                    "description": "NASA.gov Article \u201cMaking It Work in the Field with ORACLES\u201d",
+                    "downloadURL": "https://www.nasa.gov/centers/ames/earthscience/news/Making-It-Work-In-The-Field-With-Oracles",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://blogs.nasa.gov/earthexpeditions/tag/oracles/",
-                    "description": "NASA Earth Expeditions ORACLES Posts",
                     "@type": "dcat:Distribution",
+                    "description": "NASA Earth Expeditions ORACLES Posts",
+                    "downloadURL": "https://blogs.nasa.gov/earthexpeditions/tag/oracles/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/image-feature/looking-back-at-the-science-and-lessons-learned-from-oracles",
-                    "description": "NASA.gov Article \u201cLooking back at the science and lessons learned from ORACLES\u201d",
                     "@type": "dcat:Distribution",
+                    "description": "NASA.gov Article \u201cLooking back at the science and lessons learned from ORACLES\u201d",
+                    "downloadURL": "https://www.nasa.gov/image-feature/looking-back-at-the-science-and-lessons-learned-from-oracles",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/soot/power-user/ORACLES/2016",
-                    "description": "ORACLES Data on the Sub-Orbital Order Tool (SOOT) Power User Interface (UI)",
                     "@type": "dcat:Distribution",
+                    "description": "ORACLES Data on the Sub-Orbital Order Tool (SOOT) Power User Interface (UI)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/soot/power-user/ORACLES/2016",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2040492215-LARC_ASDC",
-                    "description": "ORACLES_Model_Data_1 on Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "ORACLES_Model_Data_1 on Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2040492215-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/ORACLES/Model_Data_1/",
-                    "description": "ASDC Direct Data Download for ORACLES_Model_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for ORACLES_Model_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/ORACLES/Model_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "graphic-preview-description": "ORACLES Enhanced Modis Airborne Simulator (eMAS) Data",
+            "graphic-preview-file": "https://mas.arc.nasa.gov/data/deploy_html/oracles_home.html",
+            "identifier": "C2040492215-LARC_ASDC",
+            "issued": "2021-03-01",
+            "keyword": [
+                "aerosols",
+                "atmospheric temperature",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/ORACLES_Model_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-04-19",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>-77.0 -77.0 -77.0 39.0 39.0 39.0 39.0 -77.0 -77.0 -77.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2016-08-27T00:00:00Z/2018-10-27T23:59:59.999Z",
             "theme": [
                 "ORACLES",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ORACLES Model Derived Measurements"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://techport.nasa.gov/view/10852",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2011-12-01",
-            "temporal": "2011-12-01T00:00:00Z/2014-11-01T00:00:00Z",
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
-                "project",
-                "active",
-                "wallops flight facility"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Donald Hassler",
                 "hasEmail": "mailto:hassler@boulder.swri.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Science Mission Directorate"
-            },
-            "identifier": "TECHPORT_10852",
             "description": "&lt;p&gt;\r\n\tThe optical design of RAISE is based on a new class of UV/EUV imaging spectrometers that use&amp;nbsp; only two reflections to provide quasi-stigmatic performance simultaneously over multiple wavelengths&amp;nbsp; and spatial fields. Figure 5 summarizes the RAISE instrument design, showing photographs of each of&amp;nbsp; the components or subsystems. The design uses an off-axis parabolic telescope mirror to form a real&amp;nbsp; image of the sun on the spectrometer entrance aperture. A slit then selects a portion of the solar image,&amp;nbsp; passing its light onto a near-normal incidence toroidal grating, which re-images the spectrally dispersed&amp;nbsp; radiation onto two array detectors. Two full spectral passbands over the same one-dimensional spatial&amp;nbsp; field are recorded simultaneously with no scanning of the detectors or grating. The two different spectral&amp;nbsp; bands (1st-order 1205-1243&amp;Aring; and 1526-1564&amp;Aring;) are imaged onto two intensified Active Pixel Sensor&amp;nbsp; (APS) detectors whose focal planes are individually adjusted for optimized performance. The telescope&amp;nbsp; and grating are coated with B4C to enhance short wavelength (2nd order) reflectance (Fig. 6), enabling the&amp;nbsp; instrument to record the brightest lines between 602-622&amp;Aring; and 761-780&amp;Aring; at the same time. Table 1&amp;nbsp; summarizes the main optical parameters for RAISE. &amp;nbsp;&amp;nbsp;&lt;/p&gt;\r\n&lt;p&gt;\r\n\t&lt;strong&gt;TVLS Grating. &lt;/strong&gt;The single toroidal variable line space (TVLS) grating has a toroidal surface&amp;nbsp; (Sagittal Radius = 640.5 mm, Tangential Radius = 635.3 mm), with varied line space (VLS) rulings of the&amp;nbsp; type developed originally for spherical substrates by Kita, Harada, and collaborators (1983, 1995). By&amp;nbsp; combining this VLS concept with toroidal surfaces, RAISE is the first to exploit this new class of&amp;nbsp; spectrometers, as described by Thomas (2003). For RAISE, the grating is placed 400 mm behind the slit,&amp;nbsp; with focus at a distance of approximately 1700 mm, for a spectrometer magnification of 4.25. By&amp;nbsp; operating at high magnification, the RAISE spectrometer most effectively utilizes the full length and&amp;nbsp; width available in the sounding rocket payload. The first RAISE grating, mechanically ruled by Bach&amp;nbsp; Research, Inc., was delivered in August 2007 and tested for figure, ruling density and total grating&amp;nbsp; efficiency.&amp;nbsp;&lt;/p&gt;\r\n&lt;p&gt;\r\n\t&lt;strong&gt;Intensified APS Cameras&lt;/strong&gt;. The RAISE Intensified APS camera systems are 1k x 1k CMOS Active&amp;nbsp; Pixel Sensors using miniature digital camera electronics and fed by an MCP intensifier. APS cameras&amp;nbsp; were chosen for RAISE (rather than CCDs) because of their extremely fast readout, direct digital output,&amp;nbsp; low mass, low power, deep full well and high radiation tolerance. The RAISE cameras were developed at&amp;nbsp; DLR (Germany) using a Cypress/Filfactory Star 1000 APS and include a 12-bit external ADC and USB&amp;nbsp; 2.0 interface. We will operate the cameras at 5-10 frames/sec readout, making dark current negligible&amp;nbsp; compared to the incoming signal. The complete camera electronics including its controller is integrated&amp;nbsp; on only one printed circuit board, and uses a rigid-flex 3D-interconnection between the boards to form a&amp;nbsp; lightweight, compact sensor head. Flight detectors were delivered by DLR in August 2008.&amp;nbsp;&lt;/p&gt;\r\n&lt;p&gt;\r\n\t&lt;strong&gt;&lt;em&gt;RAISE Chromospheric Slit Jaw Camera (SJC)&amp;nbsp; &lt;/em&gt;&lt;/strong&gt;To co-align the RAISE spectra with observations from SDO, HINODE, and IRIS, and to collect&amp;nbsp; chromospheric disk images in C IV and the continuum between 1500-1700 &amp;Aring;, the solar image at the&amp;nbsp; telescope focal plane (spectrograph entrance slit plane) is re-imaged onto a SJC mounted on the bo",
-            "title": "Rapid Acquisition Imaging Spectrograph (RAISE) Renewal Proposal Project",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "http://techport.nasa.gov/xml-api/10852",
                     "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "TECHPORT_10852",
+            "issued": "2011-12-01",
+            "keyword": [
+                "project",
+                "active",
+                "wallops flight facility"
+            ],
+            "landingPage": "http://techport.nasa.gov/view/10852",
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
+            "temporal": "2011-12-01T00:00:00Z/2014-11-01T00:00:00Z",
+            "title": "Rapid Acquisition Imaging Spectrograph (RAISE) Renewal Proposal Project"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MARSIS-2-EDR-EXT2-V1.0",
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
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains the scientific telemetry produced by the MARSIS instrument after editing for duplicated and corrupted packets, together with geometric information computed on ground to locate observations in space and time. Both subsurface and ionosphere sounding data are included in the dataset.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-marsis-2-edr-ext2-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars express",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MARSIS-2-EDR-EXT2-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-marsis-2-edr-ext2-v1.0",
-            "description": "This dataset contains the scientific telemetry produced by the MARSIS instrument after editing for duplicated and corrupted packets, together with geometric information computed on ground to locate observations in space and time. Both subsurface and ionosphere sounding data are included in the dataset.",
-            "title": "MARS EXPRESS MARS MARSIS EXPERIMENT DATA RECORD EXT 2 V1.0",
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
+            "title": "MARS EXPRESS MARS MARSIS EXPERIMENT DATA RECORD EXT 2 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-J%2FS%2FSS-PWS-1-EDR-WFRM-60MS-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "The Voyager 1 Plasma Wave Spectrometer (PWS) raw full resolution data set consists of electric field waveform samples from the Voyager 1 Plasma Wave Subsystem waveform receiver obtained during the entire mission. Data will continue to be added to the archive on subsequent volumes. The data set encompasses all waveform observations obtained in the cruise mission phases before, between, and after the Jupiter and Saturn encounter phases as well as those obtained during the two encounter phases. Data for this data set are acquired from the PWS waveform receiver. Data are presented as time series of 4-bit voltage measurements acquired at the rate of 28,800 samples per second through a 40 Hz to 12 kHz bandpass filter. An automatic gain control is used to keep the signal within the usable range of the 4-bit digitization, however, the gain information is not returned to the ground, hence, there is no direct, absolute calibration. However, a power spectrum analysis returns a spectrum that has accurate relative amplitudes between spectral elements. This data set provides the highest temporal resolution data from the Voyager mission. A browse data set is included with these data which provides for a graphical search of the data using a series of thumbnail and full-sized spectrograms which lead the user to the particular data file(s) of interest.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-j-s-ss-pws-1-edr-wfrm-60ms-v1.0_2wbb-urqa",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "saturn",
                 "jupiter",
                 "solar system",
                 "voyager"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-J%2FS%2FSS-PWS-1-EDR-WFRM-60MS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-j-s-ss-pws-1-edr-wfrm-60ms-v1.0_2wbb-urqa",
-            "description": "The Voyager 1 Plasma Wave Spectrometer (PWS) raw full resolution data set consists of electric field waveform samples from the Voyager 1 Plasma Wave Subsystem waveform receiver obtained during the entire mission. Data will continue to be added to the archive on subsequent volumes. The data set encompasses all waveform observations obtained in the cruise mission phases before, between, and after the Jupiter and Saturn encounter phases as well as those obtained during the two encounter phases. Data for this data set are acquired from the PWS waveform receiver. Data are presented as time series of 4-bit voltage measurements acquired at the rate of 28,800 samples per second through a 40 Hz to 12 kHz bandpass filter. An automatic gain control is used to keep the signal within the usable range of the 4-bit digitization, however, the gain information is not returned to the ground, hence, there is no direct, absolute calibration. However, a power spectrum analysis returns a spectrum that has accurate relative amplitudes between spectral elements. This data set provides the highest temporal resolution data from the Voyager mission. A browse data set is included with these data which provides for a graphical search of the data using a series of thumbnail and full-sized spectrograms which lead the user to the particular data file(s) of interest.",
-            "title": "VG1 J/S/SS PLASMA WAVE SPECTROMETER RAW WAVEFORM 60MS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VG1 J/S/SS PLASMA WAVE SPECTROMETER RAW WAVEFORM 60MS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Agbo.ast.2mass.phot&version=1.0",
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
-                "multiple asteroids",
-                "none"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set includes J, H, and Ks      magnitudes from the Two Micron All-Sky Survey (2MASS) for sources      which were positionally associated with asteroids, comets, planets,    and planetary satellites.  This version includes the 2MASS Extended    Mission.",
+            "identifier": "urn:nasa:pds:gbo.ast.2mass.phot",
+            "issued": "2021-05-21",
+            "keyword": [
+                "multiple asteroids",
+                "none"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Agbo.ast.2mass.phot&version=1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:gbo.ast.2mass.phot",
-            "description": "This data set includes J, H, and Ks      magnitudes from the Two Micron All-Sky Survey (2MASS) for sources      which were positionally associated with asteroids, comets, planets,    and planetary satellites.  This version includes the 2MASS Extended    Mission.",
-            "title": "2MASS ASTEROID AND COMET SURVEY",
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
+            "title": "2MASS ASTEROID AND COMET SURVEY"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1196",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Nepstad, D.C., and P.R. Moutinho. 2013. LBA-ECO LC-14 Biophysical Measurements, Rainfall Exclusion, Tapajos National Forest. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1196",
-            "issued": "2023-10-03",
-            "temporal": "1998-09-28T00:00:00Z/2006-11-10T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-12",
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
-            "identifier": "C2781593560-ORNL_CLOUD",
             "description": "This data set reports forest biophysical measurements from a rainfall exclusion experiment conducted at the km 67 Seca Floresta site, Tapajos National Forest, Brazil from 1998 to 2006. The purpose was to observe the potential effects of severe water stress on a humid Amazonian forest (Nepstad 2002). Data are reported for stem inventory, tree diameter at breast height (DBH) and height, dendrometer measurements of tree diameter growth increments, canopy density, leaf area index (LAI), and coarse and fine litter mass.The measurements were made monthly from September 28, 1998 through November 10, 2006. There are six comma-delimited data files (.csv), one text file (.txt), and two companion files with this data set.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO LC-14 Biophysical Measurements, Rainfall Exclusion, Tapajos National Forest",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/lba_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1196",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1196",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/land_use_land_cover_change/LC14_Aboveground_Prod/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/land_use_land_cover_change/LC14_Aboveground_Prod/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/LC14_Aboveground_Prod.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/LC14_Aboveground_Prod.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1196",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1196",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC14_Aboveground_Prod/comp/LC14_Aboveground_Prod.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC14_Aboveground_Prod/comp/LC14_Aboveground_Prod.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/csv",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC14_Aboveground_Prod/comp/LC14_Canopy_Density_summary_1999_2005.csv",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC14_Aboveground_Prod/comp/LC14_Canopy_Density_summary_1999_2005.csv",
+                    "mediaType": "text/csv",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC14_Aboveground_Prod/comp/LC14_sample_grids.jpg",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/LC14_Aboveground_Prod/comp/LC14_sample_grids.jpg",
+                    "mediaType": "image/jpeg",
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
+            "identifier": "C2781593560-ORNL_CLOUD",
+            "issued": "2023-10-03",
+            "keyword": [
+                "vegetation",
+                "ecological dynamics",
+                "earth science",
+                "biosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1196",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-10-12",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-2.86 -54.96",
+            "temporal": "1998-09-28T00:00:00Z/2006-11-10T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO LC-14 Biophysical Measurements, Rainfall Exclusion, Tapajos National Forest"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ECG5D-ICO44",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.. 2021-04-19. ECCO Sea-Ice and Snow Concentration and Thickness - Daily Mean 0.5 Degree (Version 4 Release 4). Version V4r4. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/ECG5D-ICO44. ECCO; ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.; 2020; ECCO Sea-Ice and Snow Concentration and Thickness - Daily Mean 0.5 Degree (Version 4 Release 4); 10.5067/ECG5D-ICO44; https://podaac.jpl.nasa.gov/ECCO.",
-            "issued": "2021-01-01",
-            "temporal": "1992-01-01T00:00:00Z/2018-01-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-12-31",
-            "references": [
-                "https://doi.org/10.5281/zenodo.3765928"
-            ],
-            "keyword": [
-                "sea ice",
-                "models",
-                "earth science services",
-                "earth science reanalyses/assimilation models",
-                "earth science",
-                "cryosphere"
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
-            "identifier": "C1990404815-POCLOUD",
-            "description": "This dataset contains daily-averaged sea-ice and snow concentration and thickness interpolated to a regular 0.5-degree grid from the ECCO Version 4 revision 4 (V4r4) ocean and sea-ice state estimate. Estimating the Circulation and Climate of the Ocean (ECCO) ocean and sea-ice state estimates are dynamically and kinematically-consistent reconstructions of the three-dimensional, time-evolving ocean, sea-ice, and surface atmospheric states. ECCO V4r4 is a free-running solution of the 1-degree global configuration of the MIT general circulation model (MITgcm) that has been fit to observations in a least-squares sense. Observational data constraints used in V4r4 include sea surface height (SSH) from satellite altimeters [ERS-1/2, TOPEX/Poseidon, GFO, ENVISAT, Jason-1,2,3, CryoSat-2, and SARAL/AltiKa]; sea surface temperature (SST) from satellite radiometers [AVHRR], sea surface salinity (SSS) from the Aquarius satellite radiometer/scatterometer, ocean bottom pressure (OBP) from the GRACE satellite gravimeter; sea ice concentration from satellite radiometers [SSM/I and SSMIS], and in-situ ocean temperature and salinity measured with conductivity-temperature-depth (CTD) sensors and expendable bathythermographs (XBTs) from several programs [e.g., WOCE, GO-SHIP, Argo, and others] and platforms [e.g.,research vessels, gliders, moorings, ice-tethered profilers, and instrumented pinnipeds]. V4r4 covers the period 1992-01-01T12:00:00 to 2018-01-01T00:00:00.",
-            "release-place": "PO.DAAC",
-            "graphic-preview-description": "Thumbnail image for Website",
             "creator": "ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.",
-            "title": "ECCO Sea-Ice and Snow Concentration and Thickness - Daily Mean 0.5 Degree (Version 4 Release 4)",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_SEA_ICE_CONC_THICKNESS_05DEG_DAILY_V4R4.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset contains daily-averaged sea-ice and snow concentration and thickness interpolated to a regular 0.5-degree grid from the ECCO Version 4 revision 4 (V4r4) ocean and sea-ice state estimate. Estimating the Circulation and Climate of the Ocean (ECCO) ocean and sea-ice state estimates are dynamically and kinematically-consistent reconstructions of the three-dimensional, time-evolving ocean, sea-ice, and surface atmospheric states. ECCO V4r4 is a free-running solution of the 1-degree global configuration of the MIT general circulation model (MITgcm) that has been fit to observations in a least-squares sense. Observational data constraints used in V4r4 include sea surface height (SSH) from satellite altimeters [ERS-1/2, TOPEX/Poseidon, GFO, ENVISAT, Jason-1,2,3, CryoSat-2, and SARAL/AltiKa]; sea surface temperature (SST) from satellite radiometers [AVHRR], sea surface salinity (SSS) from the Aquarius satellite radiometer/scatterometer, ocean bottom pressure (OBP) from the GRACE satellite gravimeter; sea ice concentration from satellite radiometers [SSM/I and SSMIS], and in-situ ocean temperature and salinity measured with conductivity-temperature-depth (CTD) sensors and expendable bathythermographs (XBTs) from several programs [e.g., WOCE, GO-SHIP, Argo, and others] and platforms [e.g.,research vessels, gliders, moorings, ice-tethered profilers, and instrumented pinnipeds]. V4r4 covers the period 1992-01-01T12:00:00 to 2018-01-01T00:00:00.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECG5D-ICO44",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECG5D-ICO44",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/ecco",
-                    "description": "Mission and Instrument Overview",
                     "@type": "dcat:Distribution",
+                    "description": "Mission and Instrument Overview",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/ecco",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ecco-group.org",
-                    "description": "The project website for the ECCO Consortium.",
                     "@type": "dcat:Distribution",
+                    "description": "The project website for the ECCO Consortium.",
+                    "downloadURL": "https://www.ecco-group.org",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://github.com/ECCO-GROUP/",
-                    "description": "Software maintained by ECCO Consortium on GitHub.",
                     "@type": "dcat:Distribution",
+                    "description": "Software maintained by ECCO Consortium on GitHub.",
+                    "downloadURL": "https://github.com/ECCO-GROUP/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://github.com/ECCO-GROUP/ECCO-v4-Configurations/tree/master/ECCOv4%20Release%204",
-                    "description": "ECCO Version 4 Release 4 model configuration maintained by the ECCO Consortium on GitHub",
                     "@type": "dcat:Distribution",
+                    "description": "ECCO Version 4 Release 4 model configuration maintained by the ECCO Consortium on GitHub",
+                    "downloadURL": "https://github.com/ECCO-GROUP/ECCO-v4-Configurations/tree/master/ECCOv4%20Release%204",
+                    "mediaType": "text/html",
                     "title": "View the documentation for this dataset's algorithms"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/misc/web/misc/ecco/docs/v4r4_reproduction_howto.pdf",
-                    "description": "Instructions for reproducing ECCO Version 4 Release 4",
                     "@type": "dcat:Distribution",
+                    "description": "Instructions for reproducing ECCO Version 4 Release 4",
+                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/misc/web/misc/ecco/docs/v4r4_reproduction_howto.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ecco-v4-python-tutorial.readthedocs.io/",
-                    "description": "Python Tutorials for ECCO Central Production Version 4 (ECCO V4)",
                     "@type": "dcat:Distribution",
+                    "description": "Python Tutorials for ECCO Central Production Version 4 (ECCO V4)",
+                    "downloadURL": "https://ecco-v4-python-tutorial.readthedocs.io/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/misc/web/misc/ecco/docs/v4r4_user_guide.pdf",
-                    "description": "ECCO Version 4 Release 4 User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "ECCO Version 4 Release 4 User Guide",
+                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/misc/web/misc/ecco/docs/v4r4_user_guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/misc/web/misc/ecco/docs/v4r4_synopsis.pdf",
-                    "description": "Synopsis of ECCO Version 4 Release 4",
                     "@type": "dcat:Distribution",
+                    "description": "Synopsis of ECCO Version 4 Release 4",
+                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/misc/web/misc/ecco/docs/v4r4_synopsis.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the documentation for this dataset's algorithms"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://dspace.mit.edu/handle/1721.1/110380",
-                    "description": "Synopsis of ECCO 'Central Estimate' global ocean and sea-ice state estimate, Version 4 Release 3",
                     "@type": "dcat:Distribution",
+                    "description": "Synopsis of ECCO 'Central Estimate' global ocean and sea-ice state estimate, Version 4 Release 3",
+                    "downloadURL": "https://dspace.mit.edu/handle/1721.1/110380",
+                    "mediaType": "text/html",
                     "title": "View the documentation for this dataset's algorithms"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/misc/web/misc/ecco/docs/v4r4_overview_plots.pdf",
-                    "description": "Sample Plots -- gcmfaces analysis of ECCO V4, Release 4 (1992-2017)",
                     "@type": "dcat:Distribution",
+                    "description": "Sample Plots -- gcmfaces analysis of ECCO V4, Release 4 (1992-2017)",
+                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/misc/web/misc/ecco/docs/v4r4_overview_plots.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_SEA_ICE_CONC_THICKNESS_05DEG_DAILY_V4R4.jpg",
-                    "description": "Thumbnail image for Website",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail image for Website",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_SEA_ICE_CONC_THICKNESS_05DEG_DAILY_V4R4.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ECG5D-ICO44",
-                    "description": "Access the data set landing page for the collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data set landing page for the collection.",
+                    "downloadURL": "https://doi.org/10.5067/ECG5D-ICO44",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1990404815-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1990404815-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C1990404815-POCLOUD/temporal",
-                    "description": "Browse and download granules over HTTPS using the virtual directories service",
                     "@type": "dcat:Distribution",
+                    "description": "Browse and download granules over HTTPS using the virtual directories service",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C1990404815-POCLOUD/temporal",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 }
             ],
+            "graphic-preview-description": "Thumbnail image for Website",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_SEA_ICE_CONC_THICKNESS_05DEG_DAILY_V4R4.jpg",
+            "identifier": "C1990404815-POCLOUD",
+            "issued": "2021-01-01",
+            "keyword": [
+                "sea ice",
+                "models",
+                "earth science services",
+                "earth science reanalyses/assimilation models",
+                "earth science",
+                "cryosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/ECG5D-ICO44",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "references": [
+                "https://doi.org/10.5281/zenodo.3765928"
+            ],
+            "release-place": "PO.DAAC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1992-01-01T00:00:00Z/2018-01-01T00:00:00Z",
             "theme": [
                 "ECCO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ECCO Sea-Ice and Snow Concentration and Thickness - Daily Mean 0.5 Degree (Version 4 Release 4)"
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
-                "knowledge",
-                "ask the academy",
-                "appel",
-                "sharing"
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
-            "identifier": "NASA-862__51",
             "description": "Academy of Program/Project & Engineering Leadership's Ask the Academy magazine past issues.",
-            "title": "Academy of Program/Project & Engineering Leadership ASK the Academy Past Issues",
-            "programCode": [
-                "026:045"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -52752,23 +52731,46 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
+            "identifier": "NASA-862__51",
+            "issued": "2018-06-25",
+            "keyword": [
+                "knowledge",
+                "ask the academy",
+                "appel",
+                "sharing"
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
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-LORRI-3-JUPITER-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains Calibrated data taken by the New Horizons Long Range Reconnaissance Imager instrument during the Jupiter encounter mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-lorri-3-jupiter-v1.0_2wgn-79ip",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "callisto",
                 "j2 europa",
@@ -52782,38 +52784,38 @@
                 "j6 himalia",
                 "new horizons"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-LORRI-3-JUPITER-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-lorri-3-jupiter-v1.0_2wgn-79ip",
-            "description": "This data set contains Calibrated data taken by the New Horizons Long Range Reconnaissance Imager instrument during the Jupiter encounter mission phase.",
-            "title": "NEW HORIZONS LORRI JUPITER ENCOUNTER V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEW HORIZONS LORRI JUPITER ENCOUNTER V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-ALICE-2-JUPITER-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains Raw data taken by the New Horizons Alice UV Spectrograph instrument during the Jupiter encounter mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-alice-2-jupiter-v2.0_2wgy-87b4",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "j2 europa",
                 "new horizons",
@@ -52824,707 +52826,707 @@
                 "ganymede",
                 "jupiter"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-ALICE-2-JUPITER-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-alice-2-jupiter-v2.0_2wgy-87b4",
-            "description": "This data set contains Raw data taken by the New Horizons Alice UV Spectrograph instrument during the Jupiter encounter mission phase.",
-            "title": "NEW HORIZONS ALICE JUPITER ENCOUNTER V2.0",
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
+            "title": "NEW HORIZONS ALICE JUPITER ENCOUNTER V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/KORUSAQ_Miscellaneous_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/KORUSAQ_Miscellaneous_Data_1.",
-            "issued": "2021-12-16",
-            "temporal": "2016-04-30T00:00:00Z/2016-06-13T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-01-27",
-            "keyword": [
-                "aerosols",
-                "earth science",
-                "air quality",
-                "atmospheric chemistry",
-                "atmospheric water vapor",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Xinrong Ren",
                 "hasEmail": "mailto:xinrong.ren@noaa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2210941542-LARC_ASDC",
             "description": "KORUSAQ_Miscellaneous_Data are miscellaneous ancillary files collected during the KORUS-AQ field campaign. This product includes data collected onboard the UMD Cessna Aircraft. Data collection for this product is complete.\r\n\r\nThe KORUS-AQ field study was conducted in South Korea during May-June, 2016. The study was jointly sponsored by NASA and Korea\u2019s National Institute of Environmental Research (NIER). The primary objectives were to investigate the factors controlling air quality in Korea (e.g., local emissions, chemical processes, and transboundary transport) and to assess future air quality observing strategies incorporating geostationary satellite observations. To achieve these science objectives, KORUS-AQ adopted a highly coordinated sampling strategy involved surface and airborne measurements including both in-situ and remote sensing instruments.\r\n\r\nSurface observations provided details on ground-level air quality conditions while airborne sampling provided an assessment of conditions aloft relevant to satellite observations and necessary to understand the role of emissions, chemistry, and dynamics in determining air quality outcomes. The sampling region covers the South Korean peninsula and surrounding waters with a primary focus on the Seoul Metropolitan Area. Airborne sampling was primarily conducted from near surface to about 8 km with extensive profiling to characterize the vertical distribution of pollutants and their precursors. The airborne observational data were collected from three aircraft platforms: the NASA DC-8, NASA B-200, and Hanseo King Air. Surface measurements were conducted from 16 ground sites and 2 ships: R/V Onnuri and R/V Jang Mok.\r\n\r\nThe major data products collected from both the ground and air include in-situ measurements of trace gases (e.g., ozone, reactive nitrogen species, carbon monoxide and dioxide, methane, non-methane and oxygenated hydrocarbon species), aerosols (e.g., microphysical and optical properties and chemical composition), active remote sensing of ozone and aerosols, and passive remote sensing of NO2, CH2O, and O3 column densities. These data products support research focused on examining the impact of photochemistry and transport on ozone and aerosols, evaluating emissions inventories, and assessing the potential use of satellite observations in air quality studies.",
-            "title": "KORUS-AQ Miscellaneous Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FKORUSAQ_Miscellaneous_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FKORUSAQ_Miscellaneous_Data_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espo.nasa.gov/korus-aq",
-                    "description": "KORUS-AQ Earth Science Project Office (ESPO) home page",
                     "@type": "dcat:Distribution",
+                    "description": "KORUS-AQ Earth Science Project Office (ESPO) home page",
+                    "downloadURL": "https://espo.nasa.gov/korus-aq",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nier.go.kr/NIER/eng/index.do",
-                    "description": "National Institute of Environmental Research home page",
                     "@type": "dcat:Distribution",
+                    "description": "National Institute of Environmental Research home page",
+                    "downloadURL": "https://www.nier.go.kr/NIER/eng/index.do",
+                    "mediaType": "text/html",
                     "title": "The dataset's home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/feature/langley/the-future-of-monitoring-air-quality-from-space",
-                    "description": "Article, The Future of Monitoring Air Quality from Space",
                     "@type": "dcat:Distribution",
+                    "description": "Article, The Future of Monitoring Air Quality from Space",
+                    "downloadURL": "https://www.nasa.gov/feature/langley/the-future-of-monitoring-air-quality-from-space",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/feature/airborne-expedition-tackles-global-air-quality-problem",
-                    "description": "Article, Airborne Expedition Tackles Global Air Quality Problem",
                     "@type": "dcat:Distribution",
+                    "description": "Article, Airborne Expedition Tackles Global Air Quality Problem",
+                    "downloadURL": "https://www.nasa.gov/feature/airborne-expedition-tackles-global-air-quality-problem",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www-air.larc.nasa.gov/missions/korus-aq/docs/White_paper_NASA_KORUS-AQ.pdf",
-                    "description": "KORUS-AQ White Paper Outlining NASA\u2019s contribution",
                     "@type": "dcat:Distribution",
+                    "description": "KORUS-AQ White Paper Outlining NASA\u2019s contribution",
+                    "downloadURL": "https://www-air.larc.nasa.gov/missions/korus-aq/docs/White_paper_NASA_KORUS-AQ.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://espo.nasa.gov/sites/default/files/documents/MAPS-Seoul_White%20Paper_26%20Feb%202015_Final.pdf",
-                    "description": "KORUS-AQ White Paper outlining Korea\u2019s contribution (the Megacity Air Pollution Study [MAPS] - Seoul)",
                     "@type": "dcat:Distribution",
+                    "description": "KORUS-AQ White Paper outlining Korea\u2019s contribution (the Megacity Air Pollution Study [MAPS] - Seoul)",
+                    "downloadURL": "https://espo.nasa.gov/sites/default/files/documents/MAPS-Seoul_White%20Paper_26%20Feb%202015_Final.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
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
-                    "downloadURL": "https://www.nasa.gov/content/earth-expeditions-korus-aq",
-                    "description": "Earth Expeditions Tagged Posts",
                     "@type": "dcat:Distribution",
+                    "description": "Earth Expeditions Tagged Posts",
+                    "downloadURL": "https://www.nasa.gov/content/earth-expeditions-korus-aq",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://espo.nasa.gov/sites/default/files/documents/KORUS-AQ-ENG.pdf",
-                    "description": "KORUS-AQ Rapid Science Synthesis Report",
                     "@type": "dcat:Distribution",
+                    "description": "KORUS-AQ Rapid Science Synthesis Report",
+                    "downloadURL": "https://espo.nasa.gov/sites/default/files/documents/KORUS-AQ-ENG.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://edition.cnn.com/2016/06/02/asia/nasa-air-pollution-south-korea-photos/",
-                    "description": "KORUS-AQ CNN Photo Release",
                     "@type": "dcat:Distribution",
+                    "description": "KORUS-AQ CNN Photo Release",
+                    "downloadURL": "https://edition.cnn.com/2016/06/02/asia/nasa-air-pollution-south-korea-photos/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.cnn.com/2016/06/02/asia/nasa-south-korea-dc-8-pollution/index.html",
-                    "description": "KORUS-AQ CNN Article",
                     "@type": "dcat:Distribution",
+                    "description": "KORUS-AQ CNN Article",
+                    "downloadURL": "https://www.cnn.com/2016/06/02/asia/nasa-south-korea-dc-8-pollution/index.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/KORUSAQ_Miscellaneous_Data_1",
-                    "description": "DOI Data Set Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "DOI Data Set Landing Page",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/KORUSAQ_Miscellaneous_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2210941542-LARC_ASDC",
-                    "description": "Earthdata Search Client for KORUSAQ_Miscellaneous_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search Client for KORUSAQ_Miscellaneous_Data_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2210941542-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/KORUS-AQ/Miscellaneous_Data_1/",
-                    "description": "ASDC Direct Data Download for KORUSAQ_Miscellaneous_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for KORUSAQ_Miscellaneous_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/KORUS-AQ/Miscellaneous_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2210941542-LARC_ASDC",
+            "issued": "2021-12-16",
+            "keyword": [
+                "aerosols",
+                "earth science",
+                "air quality",
+                "atmospheric chemistry",
+                "atmospheric water vapor",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/KORUSAQ_Miscellaneous_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-01-27",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>25.0 -180.0 25.0 180.0 67.0 180.0 67.0 -180.0 25.0 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2016-04-30T00:00:00Z/2016-06-13T23:59:59.999Z",
             "theme": [
                 "KORUS-AQ",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "KORUS-AQ Miscellaneous Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Lidar/Ozone/TOLNet/NASA-GSFC",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/Lidar/Ozone/TOLNet/NASA-GSFC.",
-            "issued": "2022-09-21",
-            "temporal": "2013-09-19T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-10-04",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric water vapor",
-                "atmospheric temperature",
-                "atmospheric pressure",
-                "atmospheric chemistry",
-                "atmospheric winds"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Sullivan",
                 "hasEmail": "mailto:john.t.sullivan@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2566314972-LARC_ASDC",
             "description": "TOLNet_GSFC_Data is the lidar data collected by the Tropospheric Ozone (TROPOZ) lidar at the Goddard Space Flight Center (GSFC) as part of the Tropospheric Ozone Lidar Network (TOLNet). Data collection for this product is ongoing.\r\n\r\nIn the troposphere, ozone is considered a pollutant and is important to understand due to its harmful effects on human health and vegetation. Tropospheric ozone is also significant for its impact on climate as a greenhouse gas. Operating since 2011, TOLNet is an interagency collaboration between NASA, NOAA, and the EPA designed to perform studies of air quality and atmospheric modeling as well as validation and interpretation of satellite observations. TOLNet is currently comprised of six Differential Absorption Lidars (DIAL). Each of the lidars are unique, and some have had a long history of ozone observations prior to joining the network. Five lidars are mobile systems that can be deployed at remote locations to support field campaigns. This includes the Langley Mobile Ozone Lidar (LMOL) at NASA Langley Research Center (LaRC), the Tropospheric Ozone (TROPOZ) lidar at the Goddard Space Flight Center (GSFC), the Tunable Optical Profile for Aerosol and oZone (TOPAZ) lidar at the NOAA Chemical Sciences Laboratory (CSL) in Boulder, Colorado, the Autonomous Mobile Ozone LIDAR instrument for Tropospheric Experiments (AMOLITE) lidar at Environment and Climate Change Canada (ECCC) in Toronto, Canada, and the Rocket-city O3 Quality Evaluation in the Troposphere (RO3QET) lidar at the University of Alabama in Huntsville, Alabama. The remaining lidar, the Table Mountain Facility (TMF) tropospheric ozone lidar system located at the NASA Jet Propulsion Laboratory (JPL), is a fixed system.\r\n\r\nTOLNet seeks to address three science objectives. The primary objective of the network is to provide high spatio-temporal measurements of ozone from near the surface to the top of the troposphere. Detailed observations of ozone structure allow science teams and the modeling community to better understand ozone in the lower-atmosphere and to assess the accuracy and vertical resolution with which geosynchronous instruments could retrieve the observed laminar ozone structures. Another objective of TOLNet is to identify an ozone lidar instrument design that would be suitable to address the needs of NASA, NOAA, and EPA air quality scientists who express a desire for these ozone profiles. The third objective of TOLNET is to perform basic scientific research into the processes create and destroy the ubiquitously observed ozone laminae and other ozone features in the troposphere. To help fulfill these objectives, lidars that are a part of TOLNet have been deployed to support nearly ten campaigns thus far. This includes campaigns such as the Deriving Information on Surface conditions from Column and Vertically Resolved Observations Relevant to Air Quality (DISCOVER-AQ) mission, the Korea United States Air Quality Study (KORUS-AQ), the Tracking Aerosol Convection ExpeRiment \u2013 Air Quality (TRACER-AQ) campaign, the Front Range Air Pollution and Photochemistry \u00c9xperiment (FRAPP\u00c9), the Long Island Sound Tropospheric Ozone Study (LISTOS), and the Ozone Water\u2013Land Environmental Transition Study (OWLETS).",
-            "title": "TOLNet NASA Goddard Space Flight Center Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FLidar%2FOzone%2FTOLNet%2FNASA-GSFC",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FLidar%2FOzone%2FTOLNet%2FNASA-GSFC",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www-air.larc.nasa.gov/missions/TOLNet/",
-                    "description": "TOLNet Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "TOLNet Project Home Page",
+                    "downloadURL": "https://www-air.larc.nasa.gov/missions/TOLNet/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
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
-                    "downloadURL": "http://dx.doi.org/10.1364/AO.52.003557",
-                    "description": "Ground-based lidar for atmospheric boundary layer ozone measurements",
                     "@type": "dcat:Distribution",
+                    "description": "Ground-based lidar for atmospheric boundary layer ozone measurements",
+                    "downloadURL": "http://dx.doi.org/10.1364/AO.52.003557",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www-air.larc.nasa.gov/missions/TOLNet/docs/meeting/June2016/Wednesday/Berkoff_TolnetSTMmeetingV3_Final.pdf",
-                    "description": "Capabilities & example data from the Langley Mobile Ozone Lidar (LMOL)",
                     "@type": "dcat:Distribution",
+                    "description": "Capabilities & example data from the Langley Mobile Ozone Lidar (LMOL)",
+                    "downloadURL": "https://www-air.larc.nasa.gov/missions/TOLNet/docs/meeting/June2016/Wednesday/Berkoff_TolnetSTMmeetingV3_Final.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5194/amt-7-3529-2014",
-                    "description": "A mobile differential absorption lidar to measure sub-hourly fluctuation of tropospheric ozone profiles in the Baltimore\u2013Washington, D.C. region",
                     "@type": "dcat:Distribution",
+                    "description": "A mobile differential absorption lidar to measure sub-hourly fluctuation of tropospheric ozone profiles in the Baltimore\u2013Washington, D.C. region",
+                    "downloadURL": "https://doi.org/10.5194/amt-7-3529-2014",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1364/AO.41.007550",
-                    "description": "Redesign and improved performance of the tropospheric ozone lidar at the Jet Propulsion Laboratory Table Mountain Facility",
                     "@type": "dcat:Distribution",
+                    "description": "Redesign and improved performance of the tropospheric ozone lidar at the Jet Propulsion Laboratory Table Mountain Facility",
+                    "downloadURL": "https://doi.org/10.1364/AO.41.007550",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/JTECH-D-10-05044.1",
-                    "description": "Development and Application of a Compact, Tunable, Solid-State Airborne Ozone Lidar System for Boundary Layer Profiling",
                     "@type": "dcat:Distribution",
+                    "description": "Development and Application of a Compact, Tunable, Solid-State Airborne Ozone Lidar System for Boundary Layer Profiling",
+                    "downloadURL": "https://doi.org/10.1175/JTECH-D-10-05044.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://doi.org/10.1175/JTECH-D-10-05043.1",
-                    "description": "Comparison between the TOPAZ Airborne Ozone Lidar and In Situ Measurements during TexAQS 2006",
                     "@type": "dcat:Distribution",
+                    "description": "Comparison between the TOPAZ Airborne Ozone Lidar and In Situ Measurements during TexAQS 2006",
+                    "downloadURL": "http://doi.org/10.1175/JTECH-D-10-05043.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5194/amt-6-801-2013",
-                    "description": "Developing a portable, autonomous aerosol backscatter lidar for network or remote operations",
                     "@type": "dcat:Distribution",
+                    "description": "Developing a portable, autonomous aerosol backscatter lidar for network or remote operations",
+                    "downloadURL": "https://doi.org/10.5194/amt-6-801-2013",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5194/amt-10-3865-2017",
-                    "description": "Quantifying TOLNet ozone lidar accuracy during the 2014 DISCOVER-AQ and FRAPP\u00c9 campaigns",
                     "@type": "dcat:Distribution",
+                    "description": "Quantifying TOLNet ozone lidar accuracy during the 2014 DISCOVER-AQ and FRAPP\u00c9 campaigns",
+                    "downloadURL": "https://doi.org/10.5194/amt-10-3865-2017",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2566314972-LARC_ASDC",
-                    "description": "Earthdata Search for TOLNet_GSFC_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for TOLNet_GSFC_Data_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2566314972-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/Lidar/Ozone/TOLNet/NASA-GSFC",
-                    "description": "DOI for TOLNet_GSFC_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI for TOLNet_GSFC_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/Lidar/Ozone/TOLNet/NASA-GSFC",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/TOLNet/GSFC_Data_1/",
-                    "description": "ASDC Direct Data Download for TOLNet_GSFC_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for TOLNet_GSFC_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/TOLNet/GSFC_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TOLNet/GSFC_Data_1/contents.html",
-                    "description": "OPeNDAP data access for TOLNet_GSFC_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for TOLNet_GSFC_Data_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/TOLNet/GSFC_Data_1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2566314972-LARC_ASDC",
+            "issued": "2022-09-21",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "atmospheric pressure",
+                "atmospheric chemistry",
+                "atmospheric winds"
+            ],
+            "landingPage": "https://doi.org/10.5067/Lidar/Ozone/TOLNet/NASA-GSFC",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-10-04",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>29.65 -180.0 29.65 180.0 52.0 180.0 52.0 -180.0 29.65 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2013-09-19T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "TOLNet",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TOLNet NASA Goddard Space Flight Center Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/GHN21-3U280",
             "citation": "NOAA Satellite Applications and Research (STAR). 2023-11-09. GHRSST Level 3U NOAA/ACSPO SST from VIIRS. Version 2.80. GHRSST Level 3U NOAA ACSPO SST v2.80 from VIIRS on NOAA-21 Satellite. Suitland, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/GHN21-3U280. https://www.star.nesdis.noaa.gov/star/index.php.",
-            "issued": "2023-11-09",
-            "temporal": "2023-03-19T00:00:00Z/2023-11-13T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-11-09",
-            "references": [
-                "https://doi.org/10.3390/rs14143476",
-                "https://doi.org/10.1117/1.JRS.11.032405"
-            ],
-            "keyword": [
-                "earth science",
-                "oceans",
-                "ocean temperature"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:podaac@podaac.jpl.nasa.gov"
             },
-            "identifier": "C2754899545-POCLOUD",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "description": "The N21-VIIRS-L3U-ACSPO-v2.80 dataset produced by the NOAA ACSPO system derives the Subskin Sea Surface Temperature (SST) from the Visible Infrared Imaging Radiometer Suite (VIIRS) onboard the Joint Polar Satellite System (JPSS)-2 satellite, renamed as NOAA-21 (N21). N21 was launched on Nov. 10, 2022, the 3rd satellite in the US NOAA latest JPSS series.  <br><br>\r\n\r\nThe ACSPO N21 VIIRS L3U (Level 3 Uncollated) product is a gridded version of the ACSPO N21 VIIRS L2P product, also available at PO.DAAC (10.5067/GHV21-2P290). The L3U output files are 10-minute granules in netCDF4 format, compliant with the Group for High Resolution Sea Surface Temperature (GHRSST) Data Specification version 2 (GDS2). The  ACSPO N21 VIIRS SST record is available back to 19 Mar 2023. There are 144 granules per 24hr interval, with a total data volume of 0.5GB/day. Fill values are reported at all invalid pixels, including pixels with >5 km inland. For each valid water pixel (defined as ocean, sea, lake or river, and up to 5 km inland), the following layers are reported: SSTs, a subset of l2p_flags (including day/night, land, ice, twilight, and glint flags), wind speed, and ACSPO SST minus reference (Canadian Met Centre 0.1deg L4 SST, 10.5067/GHCMC-4FM03). Only L2P SSTs with QL=5 were gridded, so all valid SSTs are recommended for the users. Per GDS2 specifications, two additional Sensor-Specific Error Statistics layers (SSES bias and standard deviation) are reported in each pixel with valid SST. <br><br>\r\n\r\nThe ACSPO VIIRS L3U product is monitored and validated against quality controlled in situ data provided by NOAA in situ SST Quality Monitor system (iQuam) using another NOAA system, SST Quality Monitor (SQUAM).",
-            "release-place": "Suitland, MD, USA",
-            "series-name": "GHRSST Level 3U NOAA/ACSPO SST from VIIRS",
             "creator": "NOAA Satellite Applications and Research (STAR)",
-            "title": "GHRSST Level 3U NOAA ACSPO SST v2.80 from VIIRS on NOAA-21 Satellite",
-            "graphic-preview-description": "Thumbnail",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/VIIRS_N20-STAR-L3U-v2.80.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The N21-VIIRS-L3U-ACSPO-v2.80 dataset produced by the NOAA ACSPO system derives the Subskin Sea Surface Temperature (SST) from the Visible Infrared Imaging Radiometer Suite (VIIRS) onboard the Joint Polar Satellite System (JPSS)-2 satellite, renamed as NOAA-21 (N21). N21 was launched on Nov. 10, 2022, the 3rd satellite in the US NOAA latest JPSS series.  <br><br>\r\n\r\nThe ACSPO N21 VIIRS L3U (Level 3 Uncollated) product is a gridded version of the ACSPO N21 VIIRS L2P product, also available at PO.DAAC (10.5067/GHV21-2P290). The L3U output files are 10-minute granules in netCDF4 format, compliant with the Group for High Resolution Sea Surface Temperature (GHRSST) Data Specification version 2 (GDS2). The  ACSPO N21 VIIRS SST record is available back to 19 Mar 2023. There are 144 granules per 24hr interval, with a total data volume of 0.5GB/day. Fill values are reported at all invalid pixels, including pixels with >5 km inland. For each valid water pixel (defined as ocean, sea, lake or river, and up to 5 km inland), the following layers are reported: SSTs, a subset of l2p_flags (including day/night, land, ice, twilight, and glint flags), wind speed, and ACSPO SST minus reference (Canadian Met Centre 0.1deg L4 SST, 10.5067/GHCMC-4FM03). Only L2P SSTs with QL=5 were gridded, so all valid SSTs are recommended for the users. Per GDS2 specifications, two additional Sensor-Specific Error Statistics layers (SSES bias and standard deviation) are reported in each pixel with valid SST. <br><br>\r\n\r\nThe ACSPO VIIRS L3U product is monitored and validated against quality controlled in situ data provided by NOAA in situ SST Quality Monitor system (iQuam) using another NOAA system, SST Quality Monitor (SQUAM).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHN21-3U280",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGHN21-3U280",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/VIIRS_N20-STAR-L3U-v2.80.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/VIIRS_N20-STAR-L3U-v2.80.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/ghrsst/open/docs/GDS20r5.pdf",
-                    "description": "Documentation on the GDS version 2 format specification",
                     "@type": "dcat:Distribution",
+                    "description": "Documentation on the GDS version 2 format specification",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/ghrsst/open/docs/GDS20r5.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.star.nesdis.noaa.gov/sod/sst/iquam/",
-                    "description": "In situ SST Quality Monitor (iQUAM)",
                     "@type": "dcat:Distribution",
+                    "description": "In situ SST Quality Monitor (iQUAM)",
+                    "downloadURL": "https://www.star.nesdis.noaa.gov/sod/sst/iquam/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrsst.jpl.nasa.gov",
-                    "description": "GHRSST Global Data Assembly Center and data access",
                     "@type": "dcat:Distribution",
+                    "description": "GHRSST Global Data Assembly Center and data access",
+                    "downloadURL": "https://ghrsst.jpl.nasa.gov",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/forum/viewtopic.php?f=7&t=298",
-                    "description": "Sea Surface Temperature measurement description.",
                     "@type": "dcat:Distribution",
+                    "description": "Sea Surface Temperature measurement description.",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/forum/viewtopic.php?f=7&t=298",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.star.nesdis.noaa.gov/sod/sst/micros/",
-                    "description": "Monitoring of IR Clear-sky Radiances over Oceans for SST",
                     "@type": "dcat:Distribution",
+                    "description": "Monitoring of IR Clear-sky Radiances over Oceans for SST",
+                    "downloadURL": "https://www.star.nesdis.noaa.gov/sod/sst/micros/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
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
-                    "downloadURL": "https://www.star.nesdis.noaa.gov/sod/sst/squam/",
-                    "description": "SST Quality Monitor (SQUAM)",
                     "@type": "dcat:Distribution",
+                    "description": "SST Quality Monitor (SQUAM)",
+                    "downloadURL": "https://www.star.nesdis.noaa.gov/sod/sst/squam/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2147488020-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2147488020-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2147488020-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2147488020-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ghrsst.org/",
-                    "description": "GHRSST Project",
                     "@type": "dcat:Distribution",
+                    "description": "GHRSST Project",
+                    "downloadURL": "https://www.ghrsst.org/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/VIIRS_N20-STAR-L3U-v2.80.jpg",
+            "identifier": "C2754899545-POCLOUD",
+            "issued": "2023-11-09",
+            "keyword": [
+                "earth science",
+                "oceans",
+                "ocean temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/GHN21-3U280",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-11-09",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "references": [
+                "https://doi.org/10.3390/rs14143476",
+                "https://doi.org/10.1117/1.JRS.11.032405"
+            ],
+            "release-place": "Suitland, MD, USA",
+            "series-name": "GHRSST Level 3U NOAA/ACSPO SST from VIIRS",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2023-03-19T00:00:00Z/2023-11-13T00:00:00Z",
             "theme": [
                 "GHRSST",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GHRSST Level 3U NOAA ACSPO SST v2.80 from VIIRS on NOAA-21 Satellite"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/TRMMLBA/AMPR/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Petersen, Walter A and Timothy  Lang.1999. TRMM LBA (LARGE SCALE BIOSPHERE-ATMOSPHERE) EXPERIMENT (AMPR) [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/TRMMLBA/AMPR/DATA101",
-            "issued": "1999-06-25",
-            "temporal": "1999-01-24T17:41:10Z/1999-02-23T22:33:19Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
-            "keyword": [
-                "spectral/engineering",
-                "earth science",
-                "microwave"
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
-            "identifier": "C1979080166-GHRC_DAAC",
             "description": "The Advanced Microwave Precipitation Radiometer (AMPR) was deployed during the Tropical Rainfall Measuring Mission - Large Scale Biosphere-Atmosphere Experiment (TRMM-LBA); the second of three TRMM ground validation missions.  AMPR data were collected at four distinct microwave frequencies (10.7, 19.35, 37.1 and 85.5 GHz) for the time period of January 23 through February 26, 1999.  The geographic domain of the TRMM-LBA region was wholly within Brazilian Amazon Basin between 16 S to 6N latitude and 76W to 49 W longitude.  The TRMM-LBA mission was to study convection over humid tropical land regions within the range of research-quality radar, lightning, radiosonde and raingage sites located in the Amazon Basin (Rondonia, Brazil).",
-            "graphic-preview-description": "N/A",
-            "title": "TRMM LBA (LARGE SCALE BIOSPHERE-ATMOSPHERE) EXPERIMENT (AMPR) V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/ampr/trmmlba/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTRMMLBA%2FAMPR%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTRMMLBA%2FAMPR%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=amprtblba",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=amprtblba",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/ampr/trmmlba/browse/lba_ampr_19990207_173646-220744.gif",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/ampr/trmmlba/browse/lba_ampr_19990207_173646-220744.gif",
+                    "mediaType": "image/gif",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/ampr/trmmlba/browse/lba_ampr_19990210_173949-211801.gif",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/ampr/trmmlba/browse/lba_ampr_19990210_173949-211801.gif",
+                    "mediaType": "image/gif",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/ampr/trmmlba/doc/amprtblba_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/ampr/trmmlba/doc/amprtblba_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/ampr/ampr.pdf",
-                    "description": "Brief Instrument Description of the Advanced Microwave Precipitation Radiometer (AMPR)",
                     "@type": "dcat:Distribution",
+                    "description": "Brief Instrument Description of the Advanced Microwave Precipitation Radiometer (AMPR)",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/ampr/ampr.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/ampr/example_ampr_read_program.f",
-                    "description": "Example program to read AMPR data from a text file into arrays",
                     "@type": "dcat:Distribution",
+                    "description": "Example program to read AMPR data from a text file into arrays",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/ampr/example_ampr_read_program.f",
+                    "mediaType": "text/html",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://weather.msfc.nasa.gov/ampr/",
-                    "description": "The home page for the project or program which sponsored the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The home page for the project or program which sponsored the dataset",
+                    "downloadURL": "https://weather.msfc.nasa.gov/ampr/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/ampr/trmmlba/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/ampr/trmmlba/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/ampr/trmmlba/browse/",
+            "identifier": "C1979080166-GHRC_DAAC",
+            "issued": "1999-06-25",
+            "keyword": [
+                "spectral/engineering",
+                "earth science",
+                "microwave"
+            ],
+            "landingPage": "https://doi.org/10.5067/TRMMLBA/AMPR/DATA101",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-04-28",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/MSFC/GHRC"
+            },
             "spatial": "-62.9596 -12.4343 -56.5415 -9.5957",
+            "temporal": "1999-01-24T17:41:10Z/1999-02-23T22:33:19Z",
             "theme": [
                 "TRMM-LBA",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TRMM LBA (LARGE SCALE BIOSPHERE-ATMOSPHERE) EXPERIMENT (AMPR) V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GIO-C-OPE-3-RDR-GRIGG-SKJELL-V1.0",
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
-                "giotto extended mission",
-                "26p/grigg-skjellerup 1 (1922 k1)"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset includes raw and calibrated results from the Optical Probe Experiment (OPE) aboard the Giotto spacecraft during its extended mission to comet 26P/Grigg-Skjellerup, as well as the data used in the calibration.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.gio-c-ope-3-rdr-grigg-skjell-v1.0_2wqy-c27z",
+            "issued": "2018-06-26",
+            "keyword": [
+                "giotto extended mission",
+                "26p/grigg-skjellerup 1 (1922 k1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GIO-C-OPE-3-RDR-GRIGG-SKJELL-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.gio-c-ope-3-rdr-grigg-skjell-v1.0_2wqy-c27z",
-            "description": "This dataset includes raw and calibrated results from the Optical Probe Experiment (OPE) aboard the Giotto spacecraft during its extended mission to comet 26P/Grigg-Skjellerup, as well as the data used in the calibration.",
-            "title": "GIOTTO EXTENDED MISSION, OPE, V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "GIOTTO EXTENDED MISSION, OPE, V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-D-GDDS-5-DUST-V4.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains the data from the Galileo dust detector system (GDDS) from start of mission through the end of mission. Included are the dust impact data, noise data, laboratory calibration data, and location and orientation of the spacecraft and instrument.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-d-gdds-5-dust-v4.0_2wsf-9khh",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "dust",
                 "galileo",
                 "calibration"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-D-GDDS-5-DUST-V4.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-d-gdds-5-dust-v4.0_2wsf-9khh",
-            "description": "This data set contains the data from the Galileo dust detector system (GDDS) from start of mission through the end of mission. Included are the dust impact data, noise data, laboratory calibration data, and location and orientation of the spacecraft and instrument.",
-            "title": "GALILEO DUST DETECTION SYSTEM V4.0",
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
+            "title": "GALILEO DUST DETECTION SYSTEM V4.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1189-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-11-17T09:35:55.000 to 2015-11-17T16:50:08.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1189-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1189-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1189-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-11-17T09:35:55.000 to 2015-11-17T16:50:08.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1189 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1189 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-CAL%2FJ%2FM-ALICE-3-MARS-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains CODMAC level 3 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the Mars swing-by phase of the Rosetta mission, which occurred 2006-07-29 to 2007-05-28. Data include the calibration observations of payload checkout (PC) 4, observations of Mars, and observations of Jupiter and the Io plasma torus.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-cal-j-m-alice-3-mars-v1.0_2wt6-inw7",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "mars",
                 "international rosetta mission",
@@ -53532,546 +53534,546 @@
                 "saturn",
                 "calibration"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-CAL%2FJ%2FM-ALICE-3-MARS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-cal-j-m-alice-3-mars-v1.0_2wt6-inw7",
-            "description": "This data set contains CODMAC level 3 data acquired by the Rosetta Orbiter ALICE UV Spectrometer during the Mars swing-by phase of the Rosetta mission, which occurred 2006-07-29 to 2007-05-28. Data include the calibration observations of payload checkout (PC) 4, observations of Mars, and observations of Jupiter and the Io plasma torus.",
-            "title": "ROSETTA-ORBITER CAL/JUPITER/MARS ALICE 3 MARS V1.0",
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
+            "title": "ROSETTA-ORBITER CAL/JUPITER/MARS ALICE 3 MARS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/SOLVE2_Miscellaneous_DC8_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2023-07-18. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/SOLVE2_Miscellaneous_DC8_Data_1.",
-            "issued": "2022-09-13",
-            "temporal": "2002-12-13T00:00:00Z/2003-02-06T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-12-13",
-            "keyword": [
-                "spectral/engineering",
-                "earth science",
-                "platform characteristics"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John McGrath",
                 "hasEmail": "mailto:john.t.mcgrath@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2569836961-LARC_ASDC",
             "description": "SOLVE2_Miscellaneous_DC8_Data is the supplementary miscellaneous data for the DC-8 aircraft collected during the SAGE III Ozone Loss and Validation Experiment II (SOLVE II). Data collection for this product is complete.\r\n\r\nThe SOLVE campaign was a NASA multi-program effort of the Upper Atmosphere Research Program (UARP), Atmospheric Effects of Aviation Project (AEAP), Atmospheric Chemistry Modeling and Analysis Program (ACMAP) and Earth Observing System (EOS) of NASA\u2019s Earth Science Enterprise (ESE). SOLVE\u2019s primary objective was for calibrating and validating the Stratospheric Aerosol and Gas Experiment (SAGE) III satellite measurements, while examining the processes that controlled ozone levels at a mid- to high-latitude range. The major goal of SAGE III was to quantitatively assess ozone loss at high latitudes. SOLVE was a two-phase experiment, the first phase, SOLVE, occurred during the fall of 1999 through the spring of 2000. The second phase, SOLVE II, occurred during the winter of 2003.\r\n\r\nSOLVE took place in the Arctic high-latitude region during the winter. The polar ozone depletion processes cause by human-produced chlorine and bromine are most active in mid-to-late winter and early spring in the high Arctic. In order to conduct this validation experiment, NASA deployed the NASA ER-2 aircraft and NASA DC-8 aircraft. The ER-2 measured a variety of atmospheric data, including ozone (O3), H2O, CO2, ClONO2, HCl, ClO/BrO, and Cl2O2. The DC-8 aircraft measured ozone, ClO/BrO, and aerosol, among other atmospheric data. SOLVE also utilized balloon platforms, ground-based instruments, and collaborations with the German Aerospace Center\u2019s (DLR) FALCON aircraft equipped with the OLEX Lidar to achieve the mission objectives. Overall, the campaign had 28 flights, with SOLVE featuring 17 total flights among the different aircrafts and SOLVE II featuring 11 flights.",
-            "title": "SOLVE II Miscellaneous DC-8 Aircraft Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSOLVE2_Miscellaneous_DC8_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSOLVE2_Miscellaneous_DC8_Data_1",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cloud1.arc.nasa.gov/solve/index.html",
-                    "description": "SOLVE Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "SOLVE Project Home Page",
+                    "downloadURL": "https://cloud1.arc.nasa.gov/solve/index.html",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espo.nasa.gov/solve",
-                    "description": "ESPO Home Page for SOLVE",
                     "@type": "dcat:Distribution",
+                    "description": "ESPO Home Page for SOLVE",
+                    "downloadURL": "https://espo.nasa.gov/solve",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
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
-                    "downloadURL": "https://espo.nasa.gov/solve/content/SOLVE_Science_Overview",
-                    "description": "SOLVE I Science Overview",
                     "@type": "dcat:Distribution",
+                    "description": "SOLVE I Science Overview",
+                    "downloadURL": "https://espo.nasa.gov/solve/content/SOLVE_Science_Overview",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://cloud1.arc.nasa.gov/solveII/presentation_files/Newman_021218.pdf",
-                    "description": "SOLVE II Science Overview",
                     "@type": "dcat:Distribution",
+                    "description": "SOLVE II Science Overview",
+                    "downloadURL": "https://cloud1.arc.nasa.gov/solveII/presentation_files/Newman_021218.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://cloud1.arc.nasa.gov/solveII/presentation_files/Margitan_021218.pdf",
-                    "description": "SOLVE II Balloon Campaign Overview",
                     "@type": "dcat:Distribution",
+                    "description": "SOLVE II Balloon Campaign Overview",
+                    "downloadURL": "https://cloud1.arc.nasa.gov/solveII/presentation_files/Margitan_021218.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/2003JD004348",
-                    "description": "Measurements of ice water content in tropopause region Arctic cirrus during the SAGE III Ozone Loss and Validation Experiment (SOLVE)",
                     "@type": "dcat:Distribution",
+                    "description": "Measurements of ice water content in tropopause region Arctic cirrus during the SAGE III Ozone Loss and Validation Experiment (SOLVE)",
+                    "downloadURL": "https://doi.org/10.1029/2003JD004348",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1029/2001JD002040",
-                    "description": "Chlorine budget and partitioning during the Stratospheric Aerosol and Gas Experiment (SAGE) III Ozone Loss and Validation Experiment (SOLVE)",
                     "@type": "dcat:Distribution",
+                    "description": "Chlorine budget and partitioning during the Stratospheric Aerosol and Gas Experiment (SAGE) III Ozone Loss and Validation Experiment (SOLVE)",
+                    "downloadURL": "https://doi.org/10.1029/2001JD002040",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5194/acp-5-1311-2005",
-                    "description": "Aerosol optical depth measurements by airborne sun photometer in SOLVE II: Comparisons to SAGE III, POAM III and airborne spectrometer measurements",
                     "@type": "dcat:Distribution",
+                    "description": "Aerosol optical depth measurements by airborne sun photometer in SOLVE II: Comparisons to SAGE III, POAM III and airborne spectrometer measurements",
+                    "downloadURL": "https://doi.org/10.5194/acp-5-1311-2005",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2569836961-LARC_ASDC",
-                    "description": "Earthdata Search client for SOLVE2_Miscellaneous_DC8_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search client for SOLVE2_Miscellaneous_DC8_Data_1",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2569836961-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/SOLVE2_Miscellaneous_DC8_Data_1",
-                    "description": "DOI for SOLVE2_Miscellaneous_DC8_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI for SOLVE2_Miscellaneous_DC8_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/SOLVE2_Miscellaneous_DC8_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/SOLVE_II/Miscellaneous_DC8_Data_1/",
-                    "description": "ASDC Direct Data Download for SOLVE2_Miscellaneous_DC8_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for SOLVE2_Miscellaneous_DC8_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/SOLVE_II/Miscellaneous_DC8_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2569836961-LARC_ASDC",
+            "issued": "2022-09-13",
+            "keyword": [
+                "spectral/engineering",
+                "earth science",
+                "platform characteristics"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/SOLVE2_Miscellaneous_DC8_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-12-13",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>13.1 -180.0 13.1 180.0 90.0 180.0 90.0 -180.0 13.1 -180.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2002-12-13T00:00:00Z/2003-02-06T23:59:59.999Z",
             "theme": [
                 "SOLVE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SOLVE II Miscellaneous DC-8 Aircraft Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-PRL-67P-M07-INF-REFL-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in reflectance units (normalized  and thus without unit),  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the PRELANDING mission phase, covering the period  from 2014-09-02T10:00:00.000 to 2014-09-23T09:59:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-prl-67p-m07-inf-refl-v1.0_2wuy-9ubf",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-PRL-67P-M07-INF-REFL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-prl-67p-m07-inf-refl-v1.0_2wuy-9ubf",
-            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in reflectance units (normalized  and thus without unit),  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the PRELANDING mission phase, covering the period  from 2014-09-02T10:00:00.000 to 2014-09-23T09:59:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 PRL-MTP007 RDR-INF-REFL V1.0",
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
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 PRL-MTP007 RDR-INF-REFL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/602",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Hall, F.G., G. Rapalee, and D.E. Knapp. 2001. BOREAS Follow-On DSP-10 Regridded TM Mosaic Land Cover Maps for 1994. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/602",
-            "issued": "2024-04-27",
-            "temporal": "1994-01-01T00:00:00Z/1995-01-01T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-29",
-            "keyword": [
-                "earth science",
-                "land surface",
-                "land use/land cover"
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
-            "identifier": "C2956562366-ORNL_CLOUD",
             "description": "Existing 30-m land cover Thematic Mapper classification by CCRS was aggregated and reprocessed and are now available at multiple resolutions (10x5 minutes and 30 minutes).",
-            "graphic-preview-description": "Browse Image",
-            "title": "BOREAS Follow-On DSP-10 Regridded TM Mosaic Land Cover Maps for 1994",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/boreas_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F602",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F602",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/DSP/BFO_dsp10_landcover_tm_mosaic/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/boreas/DSP/BFO_dsp10_landcover_tm_mosaic/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/BOREAS/FollowOn/guides/dsp10_landcov_tm_mos_maps.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/BOREAS/FollowOn/guides/dsp10_landcov_tm_mos_maps.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/602",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/602",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/DSP/BFO_dsp10_landcover_tm_mosaic/comp/0_landcover_tm_mos_30min.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/DSP/BFO_dsp10_landcover_tm_mosaic/comp/0_landcover_tm_mos_30min.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/DSP/BFO_dsp10_landcover_tm_mosaic/comp/0_landcov_tm_mos_10by5min.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/DSP/BFO_dsp10_landcover_tm_mosaic/comp/0_landcov_tm_mos_10by5min.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/DSP/BFO_dsp10_landcover_tm_mosaic/comp/dsp10_landcov_tm_mos_maps.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/boreas/DSP/BFO_dsp10_landcover_tm_mosaic/comp/dsp10_landcov_tm_mos_maps.pdf",
+                    "mediaType": "application/pdf",
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
+            "identifier": "C2956562366-ORNL_CLOUD",
+            "issued": "2024-04-27",
+            "keyword": [
+                "earth science",
+                "land surface",
+                "land use/land cover"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/602",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-04-29",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-111.0 48.0 -90.0 60.0",
+            "temporal": "1994-01-01T00:00:00Z/1995-01-01T23:59:59Z",
             "theme": [
                 "BOREAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "BOREAS Follow-On DSP-10 Regridded TM Mosaic Land Cover Maps for 1994"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/FIRMS/MODIS/MCD14DL.NRT.0061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "LANCEMODIS. 2021-03-15. MODIS/Aqua Terra Thermal Anomalies/Fire locations 1km FIRMS NRT (Vector data). Version 6.1NRT. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, The Land, Atmosphere Near real-time Capability for EOS (LANCE). https://doi.org/10.5067/FIRMS/MODIS/MCD14DL.NRT.0061. https://earthdata.nasa.gov/earth-observation-data/near-real-time/firms/active-fire-data.",
-            "issued": "2021-03-01",
-            "temporal": "2019-12-15T00:00:00Z/2025-01-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-28",
-            "references": [
-                "https://doi.org/10.1007/978-1-4419-6749-7_29",
-                "https://doi.org/10.1016/S0034-4257(02)00076-7"
-            ],
-            "keyword": [
-                "land surface",
-                "surface radiative properties",
-                "biosphere",
-                "earth science",
-                "ecological dynamics",
-                "national geospatial data asset",
-                "ngda",
-                "surface thermal properties"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:support@earthdata.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
-            "identifier": "C2105705664-LANCEMODIS",
-            "description": "The MODIS/Aqua Terra Thermal Anomalies/Fire locations 1km FIRMS Near Real-Time (NRT) - Collection 61 processed by NASA's Land, Atmosphere Near real-time Capability for EOS (LANCE) Fire Information for Resource Management System (FIRMS), using swath products (MOD14/MYD14) rather than the tiled MOD14A1 and MYD14A1 products. The thermal anomalies / active fire represent the center of a 1km pixel that is flagged by the MODIS MOD14/MYD14 Fire and Thermal Anomalies algorithm (Giglio 2003) as containing one or more fires within the pixel. This is the most basic fire product in which active fires and other thermal anomalies, such as volcanoes, are identified.\r\n\r\nMCD14DL are available in the following formats: TXT, SHP, KML, WMS. These data are also provided through the LANCE FIRMS Fire Email Alerts. Please note only the TXT and SHP files contain all the attributes.\r\n\r\nCollection 61 data replaced Collection 6 (DOI:10.5067/FIRMS/MODIS/MCD14DL.NRT.006) in April 2021.  The C61 processing does not contain any updates to the science algorithm; changes were made to improve the calibration approach in the generation of the Terra and Aqua MODIS Level 1B products.",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "LANCEMODIS",
-            "title": "MODIS/Aqua Terra Thermal Anomalies/Fire locations 1km FIRMS NRT (Vector data)",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MODIS/Aqua Terra Thermal Anomalies/Fire locations 1km FIRMS Near Real-Time (NRT) - Collection 61 processed by NASA's Land, Atmosphere Near real-time Capability for EOS (LANCE) Fire Information for Resource Management System (FIRMS), using swath products (MOD14/MYD14) rather than the tiled MOD14A1 and MYD14A1 products. The thermal anomalies / active fire represent the center of a 1km pixel that is flagged by the MODIS MOD14/MYD14 Fire and Thermal Anomalies algorithm (Giglio 2003) as containing one or more fires within the pixel. This is the most basic fire product in which active fires and other thermal anomalies, such as volcanoes, are identified.\r\n\r\nMCD14DL are available in the following formats: TXT, SHP, KML, WMS. These data are also provided through the LANCE FIRMS Fire Email Alerts. Please note only the TXT and SHP files contain all the attributes.\r\n\r\nCollection 61 data replaced Collection 6 (DOI:10.5067/FIRMS/MODIS/MCD14DL.NRT.006) in April 2021.  The C61 processing does not contain any updates to the science algorithm; changes were made to improve the calibration approach in the generation of the Terra and Aqua MODIS Level 1B products.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FFIRMS%2FMODIS%2FMCD14DL.NRT.0061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FFIRMS%2FMODIS%2FMCD14DL.NRT.0061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://firms.modaps.eosdis.nasa.gov/",
-                    "description": "VECTOR DATA - available FIRMS (Global)",
                     "@type": "dcat:Distribution",
+                    "description": "VECTOR DATA - available FIRMS (Global)",
+                    "downloadURL": "https://firms.modaps.eosdis.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://firms.modaps.nasa.gov/usfs/",
-                    "description": "VECTOR DATA - available FIRMS US/Canada",
                     "@type": "dcat:Distribution",
+                    "description": "VECTOR DATA - available FIRMS US/Canada",
+                    "downloadURL": "https://firms.modaps.nasa.gov/usfs/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nrt4.modaps.eosdis.nasa.gov/archive/FIRMS/modis-c6.1/",
-                    "description": "Access Collection 6.1 data from NASA LANCE FIRMS for the last 2 months in TXT (CSV) format",
                     "@type": "dcat:Distribution",
+                    "description": "Access Collection 6.1 data from NASA LANCE FIRMS for the last 2 months in TXT (CSV) format",
+                    "downloadURL": "https://nrt4.modaps.eosdis.nasa.gov/archive/FIRMS/modis-c6.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www.earthdata.nasa.gov/sites/default/files/imported/MODIS_C6_Fire_User_Guide_B.pdf",
-                    "description": "MODIS Active Fire Data User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "MODIS Active Fire Data User Guide",
+                    "downloadURL": "https://www.earthdata.nasa.gov/sites/default/files/imported/MODIS_C6_Fire_User_Guide_B.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 }
             ],
+            "identifier": "C2105705664-LANCEMODIS",
+            "issued": "2021-03-01",
+            "keyword": [
+                "land surface",
+                "surface radiative properties",
+                "biosphere",
+                "earth science",
+                "ecological dynamics",
+                "national geospatial data asset",
+                "ngda",
+                "surface thermal properties"
+            ],
+            "landingPage": "https://doi.org/10.5067/FIRMS/MODIS/MCD14DL.NRT.0061",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-28",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "references": [
+                "https://doi.org/10.1007/978-1-4419-6749-7_29",
+                "https://doi.org/10.1016/S0034-4257(02)00076-7"
+            ],
+            "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -80.0 180.0 80.0",
+            "temporal": "2019-12-15T00:00:00Z/2025-01-27T00:00:00Z",
             "theme": [
                 "Terra",
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Aqua Terra Thermal Anomalies/Fire locations 1km FIRMS NRT (Vector data)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/9NR0M4ILQEZN",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SMEX03 Site Photographs, Oklahoma, Version 1. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/9NR0M4ILQEZN.",
-            "issued": "2003-07-02",
-            "temporal": "2003-07-02T00:00:00Z/2003-07-17T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2003-07-17",
-            "keyword": [
-                "earth science",
-                "land use/land cover",
-                "land surface"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Michael Cosh",
                 "hasEmail": "mailto:mcosh@hydrolab.arsusda.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1386205626-NSIDCV0",
             "description": "The <em>SMEX03 Site Photographs</em> data set includes photographs of the regional study areas of Alabama, Georgia, and Oklahoma, USA as part of the 2003 Soil Moisture Experiment (SMEX03).",
-            "title": "SMEX03 Site Photographs, Oklahoma, Version 1",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F9NR0M4ILQEZN",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F9NR0M4ILQEZN",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Oklahoma/ancillary_data/photographs/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Oklahoma/ancillary_data/photographs/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Oklahoma/ancillary_data/photographs/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://daacdata.apps.nsidc.org/pub/DATASETS/AVDM/data/soil_moisture/SMEX03/Oklahoma/ancillary_data/photographs/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/9NR0M4ILQEZN",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/9NR0M4ILQEZN",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/9NR0M4ILQEZN",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/9NR0M4ILQEZN",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1386205626-NSIDCV0",
+            "issued": "2003-07-02",
+            "keyword": [
+                "earth science",
+                "land use/land cover",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.5067/9NR0M4ILQEZN",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2003-07-17",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-98.33 34.44 -97.42 36.87",
+            "temporal": "2003-07-02T00:00:00Z/2003-07-17T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SMEX03 Site Photographs, Oklahoma, Version 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GNSS/GNSS_IGSCLK5_001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GGL/CDDIS. https://doi.org/10.5067/GNSS/GNSS_IGSCLK5_001.",
-            "issued": "1992-01-01",
-            "temporal": "1992-01-01T00:00:00Z/2023-02-28T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-09-17",
-            "keyword": [
-                "gravity/gravitational field",
-                "solid earth",
-                "tectonics",
-                "earth science",
-                "geodetics"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:support-cddis@earthdata.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GGL/CDDIS"
-            },
-            "identifier": "C1426334262-CDDIS",
             "description": "This derived product set consists of Global Navigation Satellite System Final Satellite and Receiver Clock Product (5-minute granularity, daily files, generated weekly) from the NASA Crustal Dynamics Data Information System (CDDIS). GNSS provide autonomous geo-spatial positioning with global coverage. GNSS data sets from ground receivers at the CDDIS consist primarily of the data from the U.S. Global Positioning System (GPS) and the Russian GLObal NAvigation Satellite System (GLONASS). Since 2011, the CDDIS GNSS archive includes data from other GNSS (Europe\u2019s Galileo, China\u2019s Beidou, Japan\u2019s Quasi-Zenith Satellite System/QZSS, the Indian Regional Navigation Satellite System/IRNSS, and worldwide Satellite Based Augmentation Systems/SBASs), which are similar to the U.S. GPS in terms of the satellite constellation, orbits, and signal structure.  Analysis Centers (ACs) of the International GNSS Service (IGS) retrieve GNSS data on regular schedules to produce GNSS satellite and ground receiver clock values. The IGS Analysis Center Coordinator (ACC) uses these individual AC solutions to generate the official IGS final combined satellite and receiver clock products. The final products are considered the most consistent and highest quality IGS solutions; they consist of daily orbit files, generated on a weekly basis with a delay up to 13 (for the last day of the week) to 20 (for the first day of the week) days. All satellite and receiver clock solution files utilize the clock RINEX format and span 24 hours from 00:00 to 23:45 UTC.",
-            "title": "Global Navigation Satellite System (GNSS) Final Clock Product (5 minute resolution, daily files, generated weekly) from NASA CDDIS",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGNSS_IGSCLK5_001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGNSS%2FGNSS_IGSCLK5_001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "ftp://cddis.nasa.gov/gnss/products",
-                    "description": "URL for retrieval of GNSS derived products through ftp",
                     "@type": "dcat:Distribution",
+                    "description": "URL for retrieval of GNSS derived products through ftp",
+                    "downloadURL": "ftp://cddis.nasa.gov/gnss/products",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/GNSS_product_holdings.html",
-                    "description": "URL for more information about GNSS derived products",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about GNSS derived products",
+                    "downloadURL": "https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/GNSS_product_holdings.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.5067/GNSS/GNSS_IGSCLK5_001",
-                    "description": "URL for more information about GNSS derived products",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about GNSS derived products",
+                    "downloadURL": "http://dx.doi.org/10.5067/GNSS/GNSS_IGSCLK5_001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1426334262-CDDIS",
+            "issued": "1992-01-01",
+            "keyword": [
+                "gravity/gravitational field",
+                "solid earth",
+                "tectonics",
+                "earth science",
+                "geodetics"
+            ],
+            "landingPage": "https://doi.org/10.5067/GNSS/GNSS_IGSCLK5_001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-09-17",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GGL/CDDIS"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1992-01-01T00:00:00Z/2023-02-28T00:00:00Z",
             "theme": [
                 "IGS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global Navigation Satellite System (GNSS) Final Clock Product (5 minute resolution, daily files, generated weekly) from NASA CDDIS"
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
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-alice-2-jupiter-v1.0_2wz3-4jjy",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "j1 io",
                 "jupiter",
@@ -54082,386 +54084,362 @@
                 "calibration",
                 "callisto"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-ALICE-2-JUPITER-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-alice-2-jupiter-v1.0_2wz3-4jjy",
-            "description": "This data set contains Raw data taken by the New Horizons Alice UV Imager instrument during the Jupiter encounter mission phase.",
-            "title": "NEW HORIZONS ALICE JUPITER ENCOUNTER V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "NEW HORIZONS ALICE JUPITER ENCOUNTER V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-ESC3-67PCHURYUMOV-M20-V3.0",
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
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-esc3-67pchuryumov-m20-v3.0",
             "description": "This CODMAC level 3 data set contains radiometric calibrated image data in W/m^2/sr/nm, acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft during the COMET ESCORT 3 mission phase, covering the period from 2015-08-25T23:25:00.000 to 2015-09-22T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V3.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after the July and October 2018 PSA/PDS external peer reviews. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets. Included FITs files. Browse products changed to the same size as the original image.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 3 ESC3-MTP020 RDR V3.0",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-3-esc3-67pchuryumov-m20-v3.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-3-ESC3-67PCHURYUMOV-M20-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
             "programCode": [
                 "026:005"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
+            "references": [
+                "https://pds.nasa.gov"
+            ],
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "ROSETTA-ORBITER 67P OSIWAC 3 ESC3-MTP020 RDR V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=P11-J-POS-6-LIGHT-TIME-V1.0",
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
-                "pioneer 11",
-                "jupiter"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Pioneer 11 one-way light travel time data.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.p11-j-pos-6-light-time-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "pioneer 11",
+                "jupiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=P11-J-POS-6-LIGHT-TIME-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.p11-j-pos-6-light-time-v1.0",
-            "description": "Pioneer 11 one-way light travel time data.",
-            "title": "P11 JUPITER POSITION LIGHT TIME",
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
+            "title": "P11 JUPITER POSITION LIGHT TIME"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.7927/H4R49NQV",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Center for Hazards and Risk Research - CHRR - Columbia University, Center for International Earth Science Information Network - CIESIN - Columbia University, and International Bank for Reconstruction and Development - The World Bank. 2005-12-31. Global Drought Mortality Risks and Distribution. Version 1.00. Palisades, NY. Archived by National Aeronautics and Space Administration, U.S. Government, Center for Hazards and Risk Research (CHRR)/Columbia University. https://doi.org/10.7927/H4R49NQV. https://doi.org/10.7927/H4R49NQV.",
-            "issued": "2005-12-31",
-            "temporal": "2000-01-01T00:00:00Z/2000-12-31T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2005-12-31",
-            "references": [
-                "https://doi.org/10.7927/H4VX0DFT",
-                "https://doi.org/10.7927/H4GQ6VP4",
-                "https://doi.org/10.7927/H4MG7MDV"
-            ],
-            "keyword": [
-                "population",
-                "earth science",
-                "natural hazards",
-                "human dimensions"
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
-            "identifier": "C179001771-SEDAC",
-            "description": "The Global Drought Mortality Risks and Distribution is a 2.5 minute grid of global drought mortality risks. Gridded Population of the World, Version 3 (GPWv3) data provide a baseline estimation of population per grid cell from which to estimate potential mortality risks due to drought hazard. Mortality loss estimates per hazard event are calculated using regional, hazard-specific mortality records of the Emergency Events Database (EM-DAT) that span the 20 years between 1981 and 2000. Data regarding the frequency and distribution of drought hazard are obtained from the Global Drought Hazard Frequency and Distribution data set. In order to more accurately reflect the confidence associated with the data and procedures, the potential mortality estimate range is classified into deciles, 10 classes of increasing risk with an approximately equal number of grid cells per class, producing a relative estimate of drought-based mortality risks. This data set is the result of collaboration among the Columbia University Center for Hazards and Risk Research (CHRR), International Bank for Reconstruction and Development/The World Bank, and Columbia University Center for International Earth Science Information Network (CIESIN).",
-            "release-place": "Palisades, NY",
-            "graphic-preview-description": "Maps Download Page",
             "creator": "Center for Hazards and Risk Research - CHRR - Columbia University, Center for International Earth Science Information Network - CIESIN - Columbia University, and International Bank for Reconstruction and Development - The World Bank",
-            "title": "Global Drought Mortality Risks and Distribution",
-            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/ndh-drought-mortality-risks-distribution/maps",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Global Drought Mortality Risks and Distribution is a 2.5 minute grid of global drought mortality risks. Gridded Population of the World, Version 3 (GPWv3) data provide a baseline estimation of population per grid cell from which to estimate potential mortality risks due to drought hazard. Mortality loss estimates per hazard event are calculated using regional, hazard-specific mortality records of the Emergency Events Database (EM-DAT) that span the 20 years between 1981 and 2000. Data regarding the frequency and distribution of drought hazard are obtained from the Global Drought Hazard Frequency and Distribution data set. In order to more accurately reflect the confidence associated with the data and procedures, the potential mortality estimate range is classified into deciles, 10 classes of increasing risk with an approximately equal number of grid cells per class, producing a relative estimate of drought-based mortality risks. This data set is the result of collaboration among the Columbia University Center for Hazards and Risk Research (CHRR), International Bank for Reconstruction and Development/The World Bank, and Columbia University Center for International Earth Science Information Network (CIESIN).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4R49NQV",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.7927%2FH4R49NQV",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/ndh/ndh-drought-mortality-risks-distribution/drought-mortality-thumbnail.jpg",
-                    "description": "Sample browse graphic of the data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse graphic of the data set.",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/downloads/maps/ndh/ndh-drought-mortality-risks-distribution/drought-mortality-thumbnail.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-drought-mortality-risks-distribution/data-download",
-                    "description": "Data Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-drought-mortality-risks-distribution/data-download",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-drought-mortality-risks-distribution/maps",
-                    "description": "Maps Download Page",
                     "@type": "dcat:Distribution",
+                    "description": "Maps Download Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-drought-mortality-risks-distribution/maps",
+                    "mediaType": "text/html",
                     "title": "Get a related map visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-drought-mortality-risks-distribution/maps/services",
-                    "description": "Web Map Service Page",
                     "@type": "dcat:Distribution",
+                    "description": "Web Map Service Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-drought-mortality-risks-distribution/maps/services",
+                    "mediaType": "text/html",
                     "title": "Use Web Map Service (WMS) to download the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-drought-mortality-risks-distribution",
-                    "description": "Data Set\u00a0Overview Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set\u00a0Overview Page",
+                    "downloadURL": "https://sedac.ciesin.columbia.edu/data/set/ndh-drought-mortality-risks-distribution",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Maps Download Page",
+            "graphic-preview-file": "https://sedac.ciesin.columbia.edu/data/set/ndh-drought-mortality-risks-distribution/maps",
+            "identifier": "C179001771-SEDAC",
+            "issued": "2005-12-31",
+            "keyword": [
+                "population",
+                "earth science",
+                "natural hazards",
+                "human dimensions"
+            ],
+            "landingPage": "https://doi.org/10.7927/H4R49NQV",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2005-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "SEDAC"
+            },
+            "references": [
+                "https://doi.org/10.7927/H4VX0DFT",
+                "https://doi.org/10.7927/H4GQ6VP4",
+                "https://doi.org/10.7927/H4MG7MDV"
+            ],
+            "release-place": "Palisades, NY",
             "spatial": "-180.0 -58.0 180.0 85.0",
+            "temporal": "2000-01-01T00:00:00Z/2000-12-31T00:00:00Z",
             "theme": [
                 "NDH",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Global Drought Mortality Risks and Distribution"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-CAL-ROMAP-3-CR4A-SPM-V1.0",
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
-                "calibration",
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This archive contains level 3 data from the ROMAP SPM instrument onboard ROSETTA Lander, acquired during the CR4A (cruise 4A) phase. It also contains documentation which describes the ROMAP experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-cal-romap-3-cr4a-spm-v1.0_2x66-pxea",
+            "issued": "2021-05-21",
+            "keyword": [
+                "calibration",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-CAL-ROMAP-3-CR4A-SPM-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-cal-romap-3-cr4a-spm-v1.0_2x66-pxea",
-            "description": "This archive contains level 3 data from the ROMAP SPM instrument onboard ROSETTA Lander, acquired during the CR4A (cruise 4A) phase. It also contains documentation which describes the ROMAP experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-LANDER CAL ROMAP 3 CR4A SPM V1.0",
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
+            "title": "ROSETTA-LANDER CAL ROMAP 3 CR4A SPM V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/768/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2013-06-19",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "nasa",
-                "dashlink",
-                "ames"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Miryam Strautkalns",
                 "hasEmail": "mailto:miryam.strautkalns@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_768",
             "description": "Understanding aging mechanisms of electronic components is of extreme importance in the aerospace domain where they are part of numerous critical subsystems including avionics. In particular, power MOSFETs are of special interest as they are involved in high voltage switching circuits such as drivers for electrical motors. With increased use of electronics in aircraft control, it becomes more important to understand the degradation of these components in aircraft specific environments. In this paper, we present an accelerated aging methodology for power MOSFETs that subject the devices to indirect thermal overstress during high voltage switching. During this accelerated aging process, two major modes of failure were observed \u2013 latch-up and die attach degradation. In this paper we present the details of our aging methodology along with details of experiments and analysis of the results.",
-            "title": "Towards Accelerated Aging Methodologies and Health Management of Power MOSFETs",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2009_PHM_MOSFETAging.pdf",
-                    "description": "2009_PHM_MOSFETAging.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "2009_PHM_MOSFETAging.pdf",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/publication/2009_PHM_MOSFETAging.pdf",
+                    "mediaType": "application/pdf",
                     "title": "2009_PHM_MOSFETAging.pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_768",
+            "issued": "2013-06-19",
+            "keyword": [
+                "nasa",
+                "dashlink",
+                "ames"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/768/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Towards Accelerated Aging Methodologies and Health Management of Power MOSFETs"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-A-MAG-3-RDR-IDA-HIGH-RES-V1.0",
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
-                "ida",
-                "galileo"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Galileo Orbiter Magnetometer (MAG) calibrated high-resolution data from the Ida flyby in spacecraft, EME-50, RTN and Ida Solar Ecliptic (IaSE) coordinates. These data cover the interval 1993-08-28 15:56 to 1993-08-28 17:50.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-a-mag-3-rdr-ida-high-res-v1.0_2x8t-tmi3",
+            "issued": "2018-06-26",
+            "keyword": [
+                "ida",
+                "galileo"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-A-MAG-3-RDR-IDA-HIGH-RES-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-a-mag-3-rdr-ida-high-res-v1.0_2x8t-tmi3",
-            "description": "Galileo Orbiter Magnetometer (MAG) calibrated high-resolution data from the Ida flyby in spacecraft, EME-50, RTN and Ida Solar Ecliptic (IaSE) coordinates. These data cover the interval 1993-08-28 15:56 to 1993-08-28 17:50.",
-            "title": "GALILEO ORBITER A MAG RDR IDA HIGH RES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "GALILEO ORBITER A MAG RDR IDA HIGH RES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1%2FVG2-SR%2FUR-RSS-4-OCC-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "not applicable",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-vg2-sr-ur-rss-4-occ-v1.0_2xd8-4atc",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "voyager",
                 "u rings",
                 "s rings"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1%2FVG2-SR%2FUR-RSS-4-OCC-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-vg2-sr-ur-rss-4-occ-v1.0_2xd8-4atc",
-            "description": "not applicable",
-            "title": "VG1/VG2 SR/UR RSS RESAMPLED RING OCCULTATION V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VG1/VG2 SR/UR RSS RESAMPLED RING OCCULTATION V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/EQMKOJJ9L16B",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Andrews, Arlyn; Trudeau, Michael; Mountain, Marikate. 2022-09-15. CMS_CTL_NA_TCCON_FOOTPRINTS. Version 1. CarbonTracker-Lagrange North America TCCON Vertical Profile of Footprints. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/EQMKOJJ9L16B. https://disc.gsfc.nasa.gov/datacollection/CMS_CTL_NA_TCCON_FOOTPRINTS_1.html. Digital Science Data.",
-            "issued": "2006-12-22",
-            "temporal": "2006-12-11T19:00:00Z/2016-08-31T22:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-08-31",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric chemistry"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "THOMAS HEARTY",
                 "hasEmail": "mailto:Thomas.J.Hearty@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C2467917764-GES_DISC",
-            "description": "This data set provides Weather Research and Forecasting (WRF) Stochastic Time-Inverted Lagrangian Transport (STILT) particle trajectory data products for particle receptors co-located with atmospheric column observations from the TCCON ground network. Meteorological fields from the WRF model are used to drive STILT. STILT applies a Lagrangian particle dispersion model backwards in time from a measurement location (the \"receptor\" location), to create the adjoint of the transport model in the form of a \"footprint\" field. The footprint, with units of mixing ratio  per surface flux, quantifies the influence of upwind surface fluxes on greenhouse gas concentrations measured at the receptor and is computed by counting the number of particles in a surface-influenced volume and the time spent in that volume. For each column observation location, the receptors are located at 23 discrete vertical levels throughout the atmospheric column.  The CMS program is designed to make significant contributions in characterizing, quantifying, understanding, and predicting the evolution of global carbon sources and sinks through improved monitoring of carbon stocks and fluxes. The System uses NASA observations and modeling/analysis capabilities to establish the accuracy, quantitative uncertainties, and utility of products for supporting national and international policy, regulatory, and management activities. CMS data products are designed to inform near-term policy development and planning.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "CMS_CTL_NA_TCCON_FOOTPRINTS",
             "creator": "Andrews, Arlyn; Trudeau, Michael; Mountain, Marikate",
-            "title": "CarbonTracker-Lagrange North America TCCON Vertical Profile of Footprints V1 (CMS_CTL_NA_TCCON_FOOTPRINTS)",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/CMS/CMS_CTL_NA_TCCON_FOOTPRINTS_1.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "This data set provides Weather Research and Forecasting (WRF) Stochastic Time-Inverted Lagrangian Transport (STILT) particle trajectory data products for particle receptors co-located with atmospheric column observations from the TCCON ground network. Meteorological fields from the WRF model are used to drive STILT. STILT applies a Lagrangian particle dispersion model backwards in time from a measurement location (the \"receptor\" location), to create the adjoint of the transport model in the form of a \"footprint\" field. The footprint, with units of mixing ratio  per surface flux, quantifies the influence of upwind surface fluxes on greenhouse gas concentrations measured at the receptor and is computed by counting the number of particles in a surface-influenced volume and the time spent in that volume. For each column observation location, the receptors are located at 23 discrete vertical levels throughout the atmospheric column.  The CMS program is designed to make significant contributions in characterizing, quantifying, understanding, and predicting the evolution of global carbon sources and sinks through improved monitoring of carbon stocks and fluxes. The System uses NASA observations and modeling/analysis capabilities to establish the accuracy, quantitative uncertainties, and utility of products for supporting national and international policy, regulatory, and management activities. CMS data products are designed to inform near-term policy development and planning.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FEQMKOJJ9L16B",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FEQMKOJJ9L16B",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -54471,99 +54449,99 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/CMS_CTL_NA_TCCON_FOOTPRINTS_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/CMS_CTL_NA_TCCON_FOOTPRINTS_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/CMS/CMS_CTL_NA_TCCON_FOOTPRINTS.1/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/CMS/CMS_CTL_NA_TCCON_FOOTPRINTS.1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/CMS/CMS_CTL_NA_TCCON_FOOTPRINTS.1/doc/README.UserGuide_CMS_CTL_FOOTPRINTS.1.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/CMS/CMS_CTL_NA_TCCON_FOOTPRINTS.1/doc/README.UserGuide_CMS_CTL_FOOTPRINTS.1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/CMS/CMS_CTL_NA_TCCON_FOOTPRINTS.1/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/CMS/CMS_CTL_NA_TCCON_FOOTPRINTS.1/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://carbon.nasa.gov/",
-                    "description": "The NASA Carbon Monitoring System (CMS) page.",
                     "@type": "dcat:Distribution",
+                    "description": "The NASA Carbon Monitoring System (CMS) page.",
+                    "downloadURL": "https://carbon.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=CMS_CTL_NA_TCCON_FOOTPRINTS",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=CMS_CTL_NA_TCCON_FOOTPRINTS",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/CMS/CMS_CTL_NA_TCCON_FOOTPRINTS_1.png",
+            "identifier": "C2467917764-GES_DISC",
+            "issued": "2006-12-22",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/EQMKOJJ9L16B",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2016-08-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "CMS_CTL_NA_TCCON_FOOTPRINTS",
             "spatial": "-169.5 10.5 -50.5 79.5",
+            "temporal": "2006-12-11T19:00:00Z/2016-08-31T22:00:00Z",
             "theme": [
                 "CMS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CarbonTracker-Lagrange North America TCCON Vertical Profile of Footprints V1 (CMS_CTL_NA_TCCON_FOOTPRINTS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA2522",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Livesey, N. and Read, W.. 2020-06-11. ML2DGM. Version 005. MLS/Aura Level 2 Diagnostics, Miscellaneous Grid V005. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/MLS/DATA2522. https://disc.gsfc.nasa.gov/datacollection/ML2DGM_005.html. Digital Science Data.",
-            "issued": "2020-02-04",
-            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-02-04",
-            "keyword": [
-                "earth science",
-                "spectral/engineering",
-                "microwave"
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
-            "identifier": "C1729925150-GES_DISC",
-            "description": "ML2DGM is the EOS Aura Microwave Limb Sounder (MLS) product containing the minor frame diagnostic quantities on a miscellaneous grid. These include items such as tangent pressure, chi-square describing various fits to the measured radiances, number of radiances used in various retrieval phases, etc. This product contains a second auxiliary file which includes cloud-induced radiances inferred for selected spectral channels. The data version is 5.0. Data coverage is from August 8, 2004 to current. Spatial coverage is near-global (-82 degrees to +82 degrees latitude), with each profile spaced 1.5 degrees or ~165 km along the orbit track (roughly 15 orbits per day). Vertical resolution varies between species and typically ranges from 3 - 6 km. Users of the ML2DGM data product should read the EOS MLS Level 2 Version 5 Quality Document for more information.\n\nThe data are stored in the version 5 Hierarchical Data Format, or HDF5. Each file contains sets of HDF5 dataset objects (n-dimensional arrays) for each diagnostics measurement. The dataset objects represent data and geolocation fields; included in the file are file attributes and metadata. There are two files per day (MLS-Aura_L2AUX-DGM* and MLS-Aura_L2AUX-Cloud*).",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "ML2DGM",
             "creator": "Livesey, N. and Read, W.",
-            "title": "MLS/Aura Level 2 Diagnostics, Miscellaneous Grid V005 (ML2DGM) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML2DGM_005.jpeg",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "ML2DGM is the EOS Aura Microwave Limb Sounder (MLS) product containing the minor frame diagnostic quantities on a miscellaneous grid. These include items such as tangent pressure, chi-square describing various fits to the measured radiances, number of radiances used in various retrieval phases, etc. This product contains a second auxiliary file which includes cloud-induced radiances inferred for selected spectral channels. The data version is 5.0. Data coverage is from August 8, 2004 to current. Spatial coverage is near-global (-82 degrees to +82 degrees latitude), with each profile spaced 1.5 degrees or ~165 km along the orbit track (roughly 15 orbits per day). Vertical resolution varies between species and typically ranges from 3 - 6 km. Users of the ML2DGM data product should read the EOS MLS Level 2 Version 5 Quality Document for more information.\n\nThe data are stored in the version 5 Hierarchical Data Format, or HDF5. Each file contains sets of HDF5 dataset objects (n-dimensional arrays) for each diagnostics measurement. The dataset objects represent data and geolocation fields; included in the file are file attributes and metadata. There are two files per day (MLS-Aura_L2AUX-DGM* and MLS-Aura_L2AUX-Cloud*).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA2522",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FMLS%2FDATA2522",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -54573,157 +54551,181 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML2DGM_005.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/ML2DGM_005.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level2/ML2DGM.005/",
-                    "description": "Access the data via HTTP.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aura_MLS_Level2/ML2DGM.005/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML2DGM_005",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=ML2DGM_005",
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
-                    "description": "MLS Science Team home page.",
                     "@type": "dcat:Distribution",
+                    "description": "MLS Science Team home page.",
+                    "downloadURL": "https://mls.jpl.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/ML2DGM_005.jpeg",
+            "identifier": "C1729925150-GES_DISC",
+            "issued": "2020-02-04",
+            "keyword": [
+                "earth science",
+                "spectral/engineering",
+                "microwave"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/MLS/DATA2522",
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
+            "series-name": "ML2DGM",
             "spatial": "-180.0 -82.0 180.0 82.0",
+            "temporal": "2004-08-02T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MLS/Aura Level 2 Diagnostics, Miscellaneous Grid V005 (ML2DGM) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-U-PWS-1-EDR-WFRM-60MS-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set consists of electric field waveform samples from the Voyager 2 Plasma Wave Receiver waveform receiver obtained during the Uranus encounter. The waveforms are collections of 4-bit samples of the electric field measured by the dipole electric antenna at a rate of 28,800 samples per second. 1600 samples are collected in 55.56 msec followed by a 4.44-msec gap. Each 60-msec interval constitutes a line of waveform samples. The data set includes about 271 frames of waveform samples consisting of up to 800 lines, each. The telemetry format for the waveform data is identical to that for images, hence the use of line and frame as constructs in describing the form of the data. The waveform is sampled through a bandpass filter with a passband of 40 Hz to 12 kHz. The 4-bit samples provide sixteen digital values of the electric field with a linear amplitude scale, but the amplitude scale is arbitrary because of the automatic gain control used in the waveform receiver. The instantaneous dynamic range afforded by the 4 bit samples is about 23 db, but the automatic gain control allows the dominant signal in the passband to be set at the optimum level to fit within the instantaneous dynamic range. With the gain control, the overall dynamic range of the waveform receiver is about 100 db. The automatic gain control gain setting is not returned to the ground, hence, there is no absolute calibration for the data. However, by comparing the waveform spectrum derived by Fourier transforming the waveform to the spectrum provided by the spectrum analyzer data, an absolute calibration may be obtained in most cases. The data may be plotted in raw form to show the actual waveform useful for studying events such as dust impacts on the spacecraft. But the normal method of analyzing the waveform data is by Fourier transforming the samples from each line to arrive at an amplitude versus frequency spectrum. By stacking the spectra side-by-side in time order, a frequency- time spectrogram can be produced. Additional information about this dataset and the instrument which produced it can be found elsewhere in this catalog. An overview of the data in this data set can be found in Gurnett et al. [1986] and a complete instrument description can be found in Scarf and Gurnett [1977].",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-u-pws-1-edr-wfrm-60ms-v1.0_2xeh-8tfi",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "voyager",
                 "uranus",
                 "comet sl9/jupiter collision"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-U-PWS-1-EDR-WFRM-60MS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-u-pws-1-edr-wfrm-60ms-v1.0_2xeh-8tfi",
-            "description": "This data set consists of electric field waveform samples from the Voyager 2 Plasma Wave Receiver waveform receiver obtained during the Uranus encounter. The waveforms are collections of 4-bit samples of the electric field measured by the dipole electric antenna at a rate of 28,800 samples per second. 1600 samples are collected in 55.56 msec followed by a 4.44-msec gap. Each 60-msec interval constitutes a line of waveform samples. The data set includes about 271 frames of waveform samples consisting of up to 800 lines, each. The telemetry format for the waveform data is identical to that for images, hence the use of line and frame as constructs in describing the form of the data. The waveform is sampled through a bandpass filter with a passband of 40 Hz to 12 kHz. The 4-bit samples provide sixteen digital values of the electric field with a linear amplitude scale, but the amplitude scale is arbitrary because of the automatic gain control used in the waveform receiver. The instantaneous dynamic range afforded by the 4 bit samples is about 23 db, but the automatic gain control allows the dominant signal in the passband to be set at the optimum level to fit within the instantaneous dynamic range. With the gain control, the overall dynamic range of the waveform receiver is about 100 db. The automatic gain control gain setting is not returned to the ground, hence, there is no absolute calibration for the data. However, by comparing the waveform spectrum derived by Fourier transforming the waveform to the spectrum provided by the spectrum analyzer data, an absolute calibration may be obtained in most cases. The data may be plotted in raw form to show the actual waveform useful for studying events such as dust impacts on the spacecraft. But the normal method of analyzing the waveform data is by Fourier transforming the samples from each line to arrive at an amplitude versus frequency spectrum. By stacking the spectra side-by-side in time order, a frequency- time spectrogram can be produced. Additional information about this dataset and the instrument which produced it can be found elsewhere in this catalog. An overview of the data in this data set can be found in Gurnett et al. [1986] and a complete instrument description can be found in Scarf and Gurnett [1977].",
-            "title": "VG2 URA PWS RAW EXPERIMENT WAVEFORM 60MS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VG2 URA PWS RAW EXPERIMENT WAVEFORM 60MS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-EXT2-67P-M28-INF-REFL-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in reflectance units (normalized  and thus without unit),  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the ROSETTA EXTENSION 2 mission phase, covering the period  from 2016-04-05T23:25:00.000 to 2016-05-03T23:25:00.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-ext2-67p-m28-inf-refl-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-EXT2-67P-M28-INF-REFL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-ext2-67p-m28-inf-refl-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in reflectance units (normalized  and thus without unit),  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the ROSETTA EXTENSION 2 mission phase, covering the period  from 2016-04-05T23:25:00.000 to 2016-05-03T23:25:00.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 EXT2-MTP028 RDR-INF-REFL V1.0",
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
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 EXT2-MTP028 RDR-INF-REFL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-M-OSIWAC-2-MARS-MARSSWINGBY-V1.4",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera\nduring the MARS SWING-BY mission phase",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-m-osiwac-2-mars-marsswingby-v1.4_2xgc-wt3v",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "mars",
                 "phobos",
@@ -54735,38 +54737,48 @@
                 "international rosetta mission",
                 "jupiter"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-M-OSIWAC-2-MARS-MARSSWINGBY-V1.4",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-m-osiwac-2-mars-marsswingby-v1.4_2xgc-wt3v",
-            "description": "This data set contains images acquired by the OSIRIS Wide Angle Camera\nduring the MARS SWING-BY mission phase",
-            "title": "ROSETTA-ORBITER MARS SWING-BY OSIWAC 2\n                                      EDR V1.4",
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
+            "title": "ROSETTA-ORBITER MARS SWING-BY OSIWAC 2\n                                      EDR V1.4"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1214471197-ASF.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, ASF.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "undefined",
+                "hasEmail": "mailto:uso@asf.alaska.edu"
+            },
+            "description": "Sentinel-1A Dual-pol ground range detected full resolution images",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Vertex, the ASF search and download interface",
+                    "downloadURL": "https://vertex.daac.asf.alaska.edu/",
+                    "mediaType": "text/html",
+                    "title": "Download this dataset"
+                }
+            ],
+            "identifier": "C1214471197-ASF",
             "issued": "2014-06-15",
-            "temporal": "2014-04-03T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-11-17",
             "keyword": [
                 "coastal processes",
                 "cryosphere",
@@ -54793,957 +54805,923 @@
                 "biosphere",
                 "earth science"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "undefined",
-                "hasEmail": "mailto:uso@asf.alaska.edu"
-            },
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1214471197-ASF.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-11-17",
+            "programCode": [
+                "026:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "ASF"
             },
-            "identifier": "C1214471197-ASF",
-            "description": "Sentinel-1A Dual-pol ground range detected full resolution images",
-            "title": "SENTINEL-1A_DUAL_POL_GRD_FULL_RES",
-            "programCode": [
-                "026:001"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://vertex.daac.asf.alaska.edu/",
-                    "description": "Vertex, the ASF search and download interface",
-                    "@type": "dcat:Distribution",
-                    "title": "Download this dataset"
-                }
-            ],
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2014-04-03T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SENTINEL-1A_DUAL_POL_GRD_FULL_RES"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCMAG-2-ESC2-RAW-V6.0",
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
-                "international rosetta mission",
-                "67p/churyumov-gerasimenko 1 (1969 r1)"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains EDITED RAW DATA (CODMAC LEVEL 2) of the\nCOMET ESCORT 2 Phase from March 11 until June 30, 2015 of the\nROSETTA orbiter magnetometer RPCMAG. Observations are done in\nthe vicinity of comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1).\nThe current version of the dataset is V6.0",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcmag-2-esc2-raw-v6.0_2xiu-kiit",
+            "issued": "2018-06-26",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCMAG-2-ESC2-RAW-V6.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpcmag-2-esc2-raw-v6.0_2xiu-kiit",
-            "description": "This dataset contains EDITED RAW DATA (CODMAC LEVEL 2) of the\nCOMET ESCORT 2 Phase from March 11 until June 30, 2015 of the\nROSETTA orbiter magnetometer RPCMAG. Observations are done in\nthe vicinity of comet 67P/CHURYUMOV-GERASIMENKO 1 (1969 R1).\nThe current version of the dataset is V6.0",
-            "title": "ROSETTA-ORBITER 67P RPCMAG 2 ESC2 RAW V6.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER 67P RPCMAG 2 ESC2 RAW V6.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/SEA_OF_JAPAN/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/SEA_OF_JAPAN/DATA001.",
-            "issued": "1999-06-22",
-            "temporal": "1999-06-22T01:25:00Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "salinity/density",
-                "ocean chemistry",
-                "ocean temperature",
-                "oceans",
-                "earth science",
-                "ocean optics"
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
-            "identifier": "C1633360655-OB_DAAC",
             "description": "Measurements from the Sea of Japan made between 1999 and 2000.",
-            "title": "Measurements from the Sea of Japan between 1999 and 2000",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FSEA_OF_JAPAN%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FSEA_OF_JAPAN%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/Sea_of_Japan/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/Sea_of_Japan/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360655-OB_DAAC",
+            "issued": "1999-06-22",
+            "keyword": [
+                "salinity/density",
+                "ocean chemistry",
+                "ocean temperature",
+                "oceans",
+                "earth science",
+                "ocean optics"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/SEA_OF_JAPAN/DATA001",
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
+            "temporal": "1999-06-22T01:25:00Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Measurements from the Sea of Japan between 1999 and 2000"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1061-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-09-27T06:38:10.000 to 2015-09-27T09:07:07.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1061-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1061-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1061-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-09-27T06:38:10.000 to 2015-09-27T09:07:07.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1061 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1061 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/D7GK8F5J8M8R",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MEaSUREs InSAR-Based Antarctica Ice Velocity Map V002. Version 2. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/D7GK8F5J8M8R.",
-            "issued": "1996-01-01",
-            "temporal": "1996-01-01T00:00:00Z/2016-12-31T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2016-12-31",
-            "keyword": [
-                "cryosphere",
-                "snow/ice",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Eric Rignot",
                 "hasEmail": "mailto:erignot@uci.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA NSIDC DAAC"
-            },
-            "identifier": "C1414573008-NSIDC_ECS",
             "description": "This data set, part of the NASA Making Earth System Data Records for Use in Research Environments (MEaSUREs) Program, provides the first comprehensive, high-resolution, digital mosaics of ice motion in Antarctica assembled from multiple satellite interferometric, synthetic-aperture radar systems. Data were largely acquired during the International Polar Years 2007 to 2009, as well as between 2013 and 2016. Additional data acquired between 1996 and 2016 were used as needed to maximize coverage.\n\nSee <a href=\"https://nsidc.org/data/measures/aiv\">Antarctic Ice Sheet Velocity and Mapping Data</a> for related data.",
-            "title": "MEaSUREs InSAR-Based Antarctica Ice Velocity Map V002",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FD7GK8F5J8M8R",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FD7GK8F5J8M8R",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/MEASURES/NSIDC-0484.002/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/MEASURES/NSIDC-0484.002/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1414573008-NSIDC_ECS&q=nsidc-0484&m=-67.1%21-95.78%210%212%210%210%2C2&tl=1576701501%214%21%21",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1414573008-NSIDC_ECS&q=nsidc-0484&m=-67.1%21-95.78%210%212%210%210%2C2&tl=1576701501%214%21%21",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/NSIDC-0484/versions/2/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/NSIDC-0484/versions/2/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/D7GK8F5J8M8R",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/D7GK8F5J8M8R",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/D7GK8F5J8M8R",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/D7GK8F5J8M8R",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1414573008-NSIDC_ECS",
+            "issued": "1996-01-01",
+            "keyword": [
+                "cryosphere",
+                "snow/ice",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/D7GK8F5J8M8R",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2016-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 -60.0",
+            "temporal": "1996-01-01T00:00:00Z/2016-12-31T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MEaSUREs InSAR-Based Antarctica Ice Velocity Map V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-SS-RPCMAG-4-CR2-RESAMPLED-V9.0",
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
-                "checkout",
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains RESAMPLED DATA (CODMAC LEVEL 4) of the CRUISE 2 (CR2)\nphase of the ROSETTA orbiter magnetometer RPCMAG.\nIncluded are data from the time interval June 1, 2005 until July 8, 2006.\nThe current version of the dataset is V9.0.\nThe difference to the datasets of earlier versions is mainly a significantly\nimproved sensor temperature model, more detailed documentation about magnetic\ndisturbance sources, more data handling information for the user and\nalso an improved quality flagging system.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-ss-rpcmag-4-cr2-resampled-v9.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "checkout",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-SS-RPCMAG-4-CR2-RESAMPLED-V9.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-ss-rpcmag-4-cr2-resampled-v9.0",
-            "description": "This dataset contains RESAMPLED DATA (CODMAC LEVEL 4) of the CRUISE 2 (CR2)\nphase of the ROSETTA orbiter magnetometer RPCMAG.\nIncluded are data from the time interval June 1, 2005 until July 8, 2006.\nThe current version of the dataset is V9.0.\nThe difference to the datasets of earlier versions is mainly a significantly\nimproved sensor temperature model, more detailed documentation about magnetic\ndisturbance sources, more data handling information for the user and\nalso an improved quality flagging system.",
-            "title": "ROSETTA-ORBITER SW RPCMAG 4 CR2 RESAMPLED V9.0",
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
+            "title": "ROSETTA-ORBITER SW RPCMAG 4 CR2 RESAMPLED V9.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-EXT2-67P-M30-STRLIGHT-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 2 mission phase, covering the period from 2016-05-31T23:25:00.000 to 2016-06-28T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-ext2-67p-m30-strlight-v1.0_2xvb-njnw",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "international rosetta mission",
                 "vega",
                 "zeta cas"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-EXT2-67P-M30-STRLIGHT-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-ext2-67p-m30-strlight-v1.0_2xvb-njnw",
-            "description": "This CODMAC level 4 data set contains solar stray light corrected, radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 2 mission phase, covering the period from 2016-05-31T23:25:00.000 to 2016-06-28T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 EXT2-MTP030 RDR-STRLIGHT V1.0",
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
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 EXT2-MTP030 RDR-STRLIGHT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MCD06COSP_D3_MODIS.062",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "MODIS Atmosphere Science Team. 2022-05-10. MODIS (Aqua/Terra) Cloud Properties Level 3 daily, 1x1 degree grid. Version 6.2. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, L1 and Atmosphere Archive and Distribution System (LAADS). https://doi.org/10.5067/MODIS/MCD06COSP_D3_MODIS.062. https://doi.org/10.5067/MODIS/MCD06COSP_D3_MODIS.062.",
-            "issued": "2022-05-05",
-            "temporal": "2002-07-04T00:00:00Z/2025-01-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-20",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric radiation",
-                "clouds",
-                "ngda",
-                "national geospatial data asset"
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
-            "identifier": "C2263893831-LAADS",
-            "description": "The combined MODIS (Aqua/Terra) Cloud Properties Level 3 daily, 1x1 degree grid product represents a new addition that is especially geared to facilitate climate scientists who deal with both models and observations. MCD06COSP_D3_MODIS represents the daily product\u2019s short-name.  The \u201cCOSP\u201d acronym in its short-name stands for  Cloud Feedback Model Intercomparison Project (CFMIP) Observation Simulator Package. This product is an aggregation of combined MODIS Level-2 inputs from both the Terra and Aqua incarnations (MOD35/MOD06 and MYD35/MYD06, respectively), and employs an aggregation methodology consistent with the MOD08 and MYD08 products.  Provided in netCDF4 format, it contains 23 aggregated science data sets (SDS/parameters).\r\n\r\nThe Collection 6.2 (C6.2) is an improved version from the previous version (C6.1) because a number of bugs detected in Collection 6.1 are fixed.",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "MODIS Atmosphere Science Team",
-            "title": "MODIS (Aqua/Terra) Cloud Properties Level 3 daily, 1x1 degree grid",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The combined MODIS (Aqua/Terra) Cloud Properties Level 3 daily, 1x1 degree grid product represents a new addition that is especially geared to facilitate climate scientists who deal with both models and observations. MCD06COSP_D3_MODIS represents the daily product\u2019s short-name.  The \u201cCOSP\u201d acronym in its short-name stands for  Cloud Feedback Model Intercomparison Project (CFMIP) Observation Simulator Package. This product is an aggregation of combined MODIS Level-2 inputs from both the Terra and Aqua incarnations (MOD35/MOD06 and MYD35/MYD06, respectively), and employs an aggregation methodology consistent with the MOD08 and MYD08 products.  Provided in netCDF4 format, it contains 23 aggregated science data sets (SDS/parameters).\r\n\r\nThe Collection 6.2 (C6.2) is an improved version from the previous version (C6.1) because a number of bugs detected in Collection 6.1 are fixed.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD06COSP_D3_MODIS.062",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD06COSP_D3_MODIS.062",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD06COSP_D3_MODIS.062",
-                    "description": "The product landing page",
                     "@type": "dcat:Distribution",
+                    "description": "The product landing page",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD06COSP_D3_MODIS.062",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://atmosphere-imager.gsfc.nasa.gov/sites/default/files/ModAtmo/documents/L3_MCD06COSP_UserGuide_v1.5.pdf",
-                    "description": "Daily MCD06COSP product User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Daily MCD06COSP product User Guide",
+                    "downloadURL": "https://atmosphere-imager.gsfc.nasa.gov/sites/default/files/ModAtmo/documents/L3_MCD06COSP_UserGuide_v1.5.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/MCD06COSP_D3_MODIS--62",
-                    "description": "Search and order products from LAADS website.",
                     "@type": "dcat:Distribution",
+                    "description": "Search and order products from LAADS website.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/MCD06COSP_D3_MODIS--62",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LAADS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/62/MCD06COSP_D3_MODIS/",
-                    "description": "Direct access to MCD06COSP_D3_MODIS C6.2 data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to MCD06COSP_D3_MODIS C6.2 data set.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/62/MCD06COSP_D3_MODIS/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/62/MCD06COSP_D3_MODIS/contents.html",
-                    "description": "Direct access to product's OPeNDAP directory",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to product's OPeNDAP directory",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/62/MCD06COSP_D3_MODIS/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2263893831-LAADS",
+            "issued": "2022-05-05",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric radiation",
+                "clouds",
+                "ngda",
+                "national geospatial data asset"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MCD06COSP_D3_MODIS.062",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-20",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-07-04T00:00:00Z/2025-01-27T00:00:00Z",
             "theme": [
                 "Terra",
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS (Aqua/Terra) Cloud Properties Level 3 daily, 1x1 degree grid"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-2-ESC1-EDITED-V1.0",
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
-                "67p/churyumov-gerasimenko 1 (1969 r1)",
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This dataset contains EDITED raw data from the\nRosetta RPC-LAP instrument, acquired during the 1st part of the escort\nphase (ESC1) at comet 67P/Churyomov-Gerasimenko.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-2-esc1-edited-v1.0_2xyi-tp2h",
+            "issued": "2018-06-26",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RPCLAP-2-ESC1-EDITED-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rpclap-2-esc1-edited-v1.0_2xyi-tp2h",
-            "description": "This dataset contains EDITED raw data from the\nRosetta RPC-LAP instrument, acquired during the 1st part of the escort\nphase (ESC1) at comet 67P/Churyomov-Gerasimenko.",
-            "title": "ROSETTA-ORBITER 67P RPCLAP 2 ESC1 EDITED V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER 67P RPCLAP 2 ESC1 EDITED V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1049-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-09-22T09:49:10.000 to 2015-09-22T17:32:50.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1049-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-1049-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-1049-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-09-22T09:49:10.000 to 2015-09-22T17:32:50.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1049 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 1049 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DI-C-SPICE-6-V1.0",
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
-                "deep impact",
-                "9p/tempel 1 (1867 g1)"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set includes the complete set of Deep Impact SPICE data files (``kernel files''), which can be accessed using SPICE software. The SPICE data contains geometric and other ancillary information needed to recover the full value of the science instrument data. In particular SPICE kernels provide spacecraft and planetary ephemerides, instrument mounting alignments, spacecraft orientation, spacecraft sequences of events, and data needed for relevant time conversions.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.di-c-spice-6-v1.0_2y52-kdhm",
+            "issued": "2018-06-26",
+            "keyword": [
+                "deep impact",
+                "9p/tempel 1 (1867 g1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DI-C-SPICE-6-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.di-c-spice-6-v1.0_2y52-kdhm",
-            "description": "This data set includes the complete set of Deep Impact SPICE data files (``kernel files''), which can be accessed using SPICE software. The SPICE data contains geometric and other ancillary information needed to recover the full value of the science instrument data. In particular SPICE kernels provide spacecraft and planetary ephemerides, instrument mounting alignments, spacecraft orientation, spacecraft sequences of events, and data needed for relevant time conversions.",
-            "title": "DEEP IMPACT SPICE KERNELS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "DEEP IMPACT SPICE KERNELS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/N09_AVH02C1.006",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "The Long-Term Data Record (LTDR) project. 2023-07-25. NOAA-09 AVHRR Top-of-Atmosphere Reflectance Daily L3 Global 0.05 Deg. CMG. Version 6. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, L1 and Atmosphere Archive and Distribution System (LAADS). https://doi.org/10.5067/MODIS/N09_AVH02C1.006.",
-            "issued": "2022-08-04",
-            "temporal": "1985-01-04T00:00:00Z/1988-11-30T23:59:59.900Z",
-            "@type": "dcat:Dataset",
-            "modified": "1988-11-08",
-            "keyword": [
-                "atmospheric radiation",
-                "surface radiative properties",
-                "spectral/engineering",
-                "land surface",
-                "infrared wavelengths",
-                "earth science",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:MODAPSUSO@lists.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
-            "identifier": "C2738349954-LAADS",
-            "description": "The Long-Term Data Record (LTDR) produces, validates, and distributes a global land surface climate data record (CDR) that uses both mature and well-tested algorithms in concert with the best-available polar-orbiting satellite data from past to the present.   The CDR is critically important to studying global climate change.  The LTDR project is unique in that it serves as a bridge that connects data derived from the NOAA Advanced Very High Resolution Radiometer (AVHRR), the EOS Moderate resolution Imaging Spectroradiometer (MODIS), the Suomi National Polar-orbiting Partnership (SNPP) Visible Infrared Imaging Radiometer Suite (VIIRS), and Joint Polar Satellite System (JPSS) VIIRS missions.  The LTDR draws from the following eight AVHRR missions: \r\nNOAA-7, NOAA-9, NOAA-11, NOAA-14, NOAA-16, NOAA-18, NOAA-19, and MetOp-B.\r\nCurrently, the project generates a daily surface reflectance product as the fundamental climate data record (FCDR) and derives daily Normalized Differential Vegetation Index (NDVI) and Leaf-Area Index/fraction of absorbed Photosynthetically Active Radiation (LAI/fPAR) as two thematic CDRs (TCDR).  LAI/fPAR was developed as an experimental product.\r\n\r\nThe  NOAA-09 AVHRR Top-of-Atmosphere Reflectance Daily L3 Global 0.05 Deg. CMG, short-name N09_AVH02C1 is generated from GIMMS Advanced Processing System (GAPS) BRDF-corrected Surface Reflectance product (AVH01C1). The N09_AVH02C1 consist of Top-of-atmosphere reflectance for bands 1 and 2, data Quality flags, angles (solar zenith, view zenith, and relative azimuth), thermal data (thermal bands 3, 4 and 5), and additional data (scan time).",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "The Long-Term Data Record (LTDR) project",
-            "title": "NOAA-09 AVHRR Top-of-Atmosphere Reflectance Daily L3 Global 0.05 Deg. CMG",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Long-Term Data Record (LTDR) produces, validates, and distributes a global land surface climate data record (CDR) that uses both mature and well-tested algorithms in concert with the best-available polar-orbiting satellite data from past to the present.   The CDR is critically important to studying global climate change.  The LTDR project is unique in that it serves as a bridge that connects data derived from the NOAA Advanced Very High Resolution Radiometer (AVHRR), the EOS Moderate resolution Imaging Spectroradiometer (MODIS), the Suomi National Polar-orbiting Partnership (SNPP) Visible Infrared Imaging Radiometer Suite (VIIRS), and Joint Polar Satellite System (JPSS) VIIRS missions.  The LTDR draws from the following eight AVHRR missions: \r\nNOAA-7, NOAA-9, NOAA-11, NOAA-14, NOAA-16, NOAA-18, NOAA-19, and MetOp-B.\r\nCurrently, the project generates a daily surface reflectance product as the fundamental climate data record (FCDR) and derives daily Normalized Differential Vegetation Index (NDVI) and Leaf-Area Index/fraction of absorbed Photosynthetically Active Radiation (LAI/fPAR) as two thematic CDRs (TCDR).  LAI/fPAR was developed as an experimental product.\r\n\r\nThe  NOAA-09 AVHRR Top-of-Atmosphere Reflectance Daily L3 Global 0.05 Deg. CMG, short-name N09_AVH02C1 is generated from GIMMS Advanced Processing System (GAPS) BRDF-corrected Surface Reflectance product (AVH01C1). The N09_AVH02C1 consist of Top-of-atmosphere reflectance for bands 1 and 2, data Quality flags, angles (solar zenith, view zenith, and relative azimuth), thermal data (thermal bands 3, 4 and 5), and additional data (scan time).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FN09_AVH02C1.006",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FN09_AVH02C1.006",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ltdr.modaps.eosdis.nasa.gov/cgi-bin/ltdr/ltdrPage.cgi?fileName=docs",
-                    "description": "Overview of LTDR Products documents",
                     "@type": "dcat:Distribution",
+                    "description": "Overview of LTDR Products documents",
+                    "downloadURL": "https://ltdr.modaps.eosdis.nasa.gov/cgi-bin/ltdr/ltdrPage.cgi?fileName=docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/1/N09_AVH02C1--466",
-                    "description": "Search and order products from LAADS website.",
                     "@type": "dcat:Distribution",
+                    "description": "Search and order products from LAADS website.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/1/N09_AVH02C1--466",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LAADS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/466/N09_AVH02C1/",
-                    "description": "Direct access to C6 N09_AVH02C1 data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to C6 N09_AVH02C1 data set.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/466/N09_AVH02C1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://landweb.modaps.eosdis.nasa.gov/QA_WWW/forPage/user_guide/avhrr/LTDR_Ver5_Products_UserGuide_v1.0.pdf",
-                    "description": "A combined User's Guides for all L3 LTDR products",
                     "@type": "dcat:Distribution",
+                    "description": "A combined User's Guides for all L3 LTDR products",
+                    "downloadURL": "https://landweb.modaps.eosdis.nasa.gov/QA_WWW/forPage/user_guide/avhrr/LTDR_Ver5_Products_UserGuide_v1.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 }
             ],
+            "identifier": "C2738349954-LAADS",
+            "issued": "2022-08-04",
+            "keyword": [
+                "atmospheric radiation",
+                "surface radiative properties",
+                "spectral/engineering",
+                "land surface",
+                "infrared wavelengths",
+                "earth science",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/N09_AVH02C1.006",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1988-11-08",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1985-01-04T00:00:00Z/1988-11-30T23:59:59.900Z",
             "theme": [
                 "NOAA - SPACE WEATHER PROGRAM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NOAA-09 AVHRR Top-of-Atmosphere Reflectance Daily L3 Global 0.05 Deg. CMG"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-MI-5-ANAGLYPH-OPS-V1.0",
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
-                "mars exploration rover"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "NULL",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-mi-5-anaglyph-ops-v1.0_2y6f-a44d",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars exploration rover"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MER1-M-MI-5-ANAGLYPH-OPS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mer1-m-mi-5-anaglyph-ops-v1.0_2y6f-a44d",
-            "description": "NULL",
-            "title": "MER 1 MARS MICROSCOPIC IMAGER\n                                      ANAGLYPH RDR OPS V1.0",
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
+            "title": "MER 1 MARS MICROSCOPIC IMAGER\n                                      ANAGLYPH RDR OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MESS-H-XRS-5-RDR-FOOTPRINTS-V1.0",
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
-                "messenger",
-                "mercury"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Abstract ======== This data set consists of the MESSENGER XRS reduced data record (RDR) footprints which are derived from the navigational meta-data for each calibrated data record (CDR) whose FOV_STATUS is 1 or 3; that is, when the field of view intersects the planet and is either partially or entirely sunlit. Each XRS observation results in four X-ray spectra. When an X-ray interacts with one of the four detectors, a charge or voltage pulse is generated. This signal is converted into one of 2^8 (256) channels, which are correlated to energy. Over a commanded integration time period a histogram of counts as a function of energy (channel number) is recorded. The EDRs are the number of events in each channel of the four detectors accumulated over the integration period. Channels above or below the useful energy range of the detectors are not transmitted. The result is three 244-channel GPC histograms and one 231-channel solar monitor histogram, each of which is designated as a single X-ray spectrum. Each observation is calibrated and processed into the CDR data set. For each CDR whose field of view is contained or partially contained on the planetary surface, a footprint is computed that corresponds to the perimeter of the planetary region within the instrument field of view during the integration time of the observation.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mess-h-xrs-5-rdr-footprints-v1.0_2ycb-fdvi",
+            "issued": "2018-06-26",
+            "keyword": [
+                "messenger",
+                "mercury"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MESS-H-XRS-5-RDR-FOOTPRINTS-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mess-h-xrs-5-rdr-footprints-v1.0_2ycb-fdvi",
-            "description": "Abstract ======== This data set consists of the MESSENGER XRS reduced data record (RDR) footprints which are derived from the navigational meta-data for each calibrated data record (CDR) whose FOV_STATUS is 1 or 3; that is, when the field of view intersects the planet and is either partially or entirely sunlit. Each XRS observation results in four X-ray spectra. When an X-ray interacts with one of the four detectors, a charge or voltage pulse is generated. This signal is converted into one of 2^8 (256) channels, which are correlated to energy. Over a commanded integration time period a histogram of counts as a function of energy (channel number) is recorded. The EDRs are the number of events in each channel of the four detectors accumulated over the integration period. Channels above or below the useful energy range of the detectors are not transmitted. The result is three 244-channel GPC histograms and one 231-channel solar monitor histogram, each of which is designated as a single X-ray spectrum. Each observation is calibrated and processed into the CDR data set. For each CDR whose field of view is contained or partially contained on the planetary surface, a footprint is computed that corresponds to the perimeter of the planetary region within the instrument field of view during the integration time of the observation.",
-            "title": "MESSENGER H XRS 5 REDUCED DATA RECORD\n                                      (RDR) FOOTPRINTS V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MESSENGER H XRS 5 REDUCED DATA RECORD\n                                      (RDR) FOOTPRINTS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1266-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-18T17:53:45.000 to 2015-12-19T00:16:28.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1266-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1266-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1266-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-18T17:53:45.000 to 2015-12-19T00:16:28.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1266 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1266 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/NIMBUS/NmHRIR3H",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Nimbus High Resolution Infrared Radiometer Remapped Digital Data Daily L3, HDF5 V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/NIMBUS/NmHRIR3H.",
-            "issued": "1964-08-29",
-            "temporal": "1964-08-29T00:00:00Z/1969-11-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1969-11-30",
-            "keyword": [
-                "earth science",
-                "infrared wavelengths",
-                "spectral/engineering"
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
-            "identifier": "C1690336970-NSIDC_ECS",
             "description": "This data set (NmHRIR3H) consists of daily, global composites of High Resolution Infrared Radiometer (HRIR) data obtained by the Nimbus 1, Nimbus 2, and Nimbus 3 satellites during 1964, 1966, and 1969. Each composite is provided as a set of three HDF5-formatted files: separate North and South Polar projections in the 10 km Equal-Area Scalable Earth Grid (EASE-Grid) and an equatorial projection in a 20 km equidistant grid for the region between 60 N and 60 S. Browse images are also available.",
-            "title": "Nimbus High Resolution Infrared Radiometer Remapped Digital Data Daily L3, HDF5 V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNIMBUS%2FNmHRIR3H",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FNIMBUS%2FNmHRIR3H",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/NIMBUS/NmHRIR3H.001",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/NIMBUS/NmHRIR3H.001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000000-NSIDC_ECS&m=-32.484375%210.5625%211%211%210%210%2C2&q=NmHRIR3H",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000000-NSIDC_ECS&m=-32.484375%210.5625%211%211%210%210%2C2&q=NmHRIR3H",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/NmHRIR3H/versions/1/",
-                    "description": "Data Access link for ITSD project",
                     "@type": "dcat:Distribution",
+                    "description": "Data Access link for ITSD project",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/NmHRIR3H/versions/1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/NIMBUS/NmHRIR3H",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/NIMBUS/NmHRIR3H",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/NIMBUS/NmHRIR3H",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/NIMBUS/NmHRIR3H",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C1690336970-NSIDC_ECS",
+            "issued": "1964-08-29",
+            "keyword": [
+                "earth science",
+                "infrared wavelengths",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/NIMBUS/NmHRIR3H",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1969-11-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1964-08-29T00:00:00Z/1969-11-30T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Nimbus High Resolution Infrared Radiometer Remapped Digital Data Daily L3, HDF5 V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-EXT3-67P-M33-INF-REFL-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in reflectance units (normalized  and thus without unit),  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the ROSETTA EXTENSION 3 mission phase, covering the period  from 2016-08-09T23:25:00.000 to 2016-09-02T06:39:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-ext3-67p-m33-inf-refl-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-EXT3-67P-M33-INF-REFL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-ext3-67p-m33-inf-refl-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in reflectance units (normalized  and thus without unit),  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the ROSETTA EXTENSION 3 mission phase, covering the period  from 2016-08-09T23:25:00.000 to 2016-09-02T06:39:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 EXT3-MTP033 RDR-INF-REFL V1.0",
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
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 EXT3-MTP033 RDR-INF-REFL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-J-MAG-4-1.92SEC",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set includes Voyager 2 Jupiter encounter magnetometer data that have been resampled at a 1.92 second sample rate. The data set is composed of 6 columns: 1) ctime - this column contains the data acquisition time. The time is always output in the ISO standard spacecraft event time format (yyyy-mm-dd-Thh:mm:ss.sss) but is stored internally in Cline time which is measured in seconds after 00:00:00.000 Jan 01, 1966, 2) br - this column contains the radial component of the magnetic field, 3) bphi - this column contains the phi component of the magnetic field, 4) btheta - this column contains the theta component of the magnetic field, 5) bmag - this column contains the magnitude of the magnetic field, 6) flag - a flag value that indicates either software error or spacecraft hardware interference reduced confidence in this record (flag value of 1 is bad , 0 is good or unchecked). All magnetic field observations are measured in nanoTeslas. The coordinate system for this dataset is Minus System III. All of the magnetic field data are calibrated (see the instrument calibration description for more details). The Jupiter System III coordinate system is defined in Dessler 1983 and the reference documents for this dataset are: Ness et al, 1979A Lepping et al, 1981 Connerney,Acuna,Ness, 1981 Behannon,Burlaga,Ness, 1981",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-j-mag-4-1.92sec_2yf7-7jvy",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "voyager",
                 "jupiter",
                 "comet sl9/jupiter collision"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-J-MAG-4-1.92SEC",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-j-mag-4-1.92sec_2yf7-7jvy",
-            "description": "This data set includes Voyager 2 Jupiter encounter magnetometer data that have been resampled at a 1.92 second sample rate. The data set is composed of 6 columns: 1) ctime - this column contains the data acquisition time. The time is always output in the ISO standard spacecraft event time format (yyyy-mm-dd-Thh:mm:ss.sss) but is stored internally in Cline time which is measured in seconds after 00:00:00.000 Jan 01, 1966, 2) br - this column contains the radial component of the magnetic field, 3) bphi - this column contains the phi component of the magnetic field, 4) btheta - this column contains the theta component of the magnetic field, 5) bmag - this column contains the magnitude of the magnetic field, 6) flag - a flag value that indicates either software error or spacecraft hardware interference reduced confidence in this record (flag value of 1 is bad , 0 is good or unchecked). All magnetic field observations are measured in nanoTeslas. The coordinate system for this dataset is Minus System III. All of the magnetic field data are calibrated (see the instrument calibration description for more details). The Jupiter System III coordinate system is defined in Dessler 1983 and the reference documents for this dataset are: Ness et al, 1979A Lepping et al, 1981 Connerney,Acuna,Ness, 1981 Behannon,Burlaga,Ness, 1981",
-            "title": "VOYAGER 2 JUPITER MAGNETOMETER RESAMPLED DATA 1.92 SEC",
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
+            "title": "VOYAGER 2 JUPITER MAGNETOMETER RESAMPLED DATA 1.92 SEC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-OSINAC-3-EAR1-EARTHSWINGBY1-V1.4",
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
-                "international rosetta mission",
-                "calibration"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains images acquired by the OSIRIS Narrow Angle Camera\nduring the EARTH SWING-BY 1 mission phase",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-osinac-3-ear1-earthswingby1-v1.4_2yfb-egnh",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "calibration"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-OSINAC-3-EAR1-EARTHSWINGBY1-V1.4",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-osinac-3-ear1-earthswingby1-v1.4_2yfb-egnh",
-            "description": "This data set contains images acquired by the OSIRIS Narrow Angle Camera\nduring the EARTH SWING-BY 1 mission phase",
-            "title": "ROSETTA-ORBITER EARTH SWING-BY 1 OSINAC\n                                      3 RDR V1.4",
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
+            "title": "ROSETTA-ORBITER EARTH SWING-BY 1 OSINAC\n                                      3 RDR V1.4"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5270/S5P-3p6lnwd",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Copernicus Sentinel data processed by ESA, Koninklijk Nederlands Meteorologisch Instituut (KNMI)/Netherlands Institute for Space Research (SRON). 2019-03-28. S5P_L2__CH4___. Version 1. Sentinel-5P TROPOMI Methane CH4 1-Orbit L2 7km x 7km. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5270/S5P-3p6lnwd. https://disc.gsfc.nasa.gov/datacollection/S5P_L2__CH4____1.html. Digital Science Data.",
-            "issued": "2017-05-05",
-            "temporal": "2018-04-30T00:41:24Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-05-05",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "atmospheric chemistry"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jochen Landgraf",
                 "hasEmail": "mailto:j.landgraf@sron.nl"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C1442068505-GES_DISC",
-            "description": "Starting from August 6th in 2019, Sentinel-5P TROPOMI along-track high spatial resolution (~5.5km at nadir) has been implemented.\nFor data after August 6th of 2019, please check S5P_L2__CH4___ data collection.\n\nThe Copernicus Sentinel-5 Precursor (Sentinel-5P or S5P) satellite mission is one of the European Space Agency's (ESA) new mission family - Sentinels, and it is a joint initiative between the Kingdom of the Netherlands and the ESA. The sole payload on Sentinel-5P is the TROPOspheric Monitoring Instrument (TROPOMI), which is a nadir-viewing 108 degree Field-of-View push-broom grating hyperspectral spectrometer, covering the wavelength of ultraviolet-visible (UV-VIS, 270nm to 495nm), near infrared (NIR, 675nm to 775nm), and shortwave infrared (SWIR, 2305nm-2385nm). Sentinel-5P is the first of the Atmospheric Composition Sentinels and is expected to provide measurements of ozone, NO2, SO2, CH4, CO, formaldehyde, aerosols and cloud at high spatial, temporal and spectral resolutions.\n\nThe retrieval algorithm for Sentinel-5P TROPOMI methane product is a physics based method that uses the Oxygen-A band (760 nm) and absorption bands in shortwave infrared spectrum. In Sentinel-5P/TROPOMI methane algorithm, the atmosphere forward model simulates the absorbing gas (oxygen, methane, water vapor, and carbon monoxide) optical properties, as well as aerosol optical properties with size distribution, refractive index, and number concentration. The inversion is performed based on the forward calculation, the measurement, and the prior information. Cloud filtering is critical in methane retrieval, S5P methane algorithm applies re-gridded Visible Infrared Imaging Radiometer Suite (VIIRS) cloud mask data. Additional cloud filters based on S5P/TROPOMI measurements and the FRESCO apparent surface pressure will be applied when VIIRS cloud data are not available. Other current data filters in the retrieval algorithm include land-only pixels (excluding mountainous areas), spectrum intensity, solar zenith angle and instrument zenith angle. \n\nThe S5P/TROPOMI methane retrieval is for non-time-critical (NTC) data stream only, and its main outputs include the column averaged dry air mixing ratio of methane, the random error, and the biased corrected dry air methane fraction data based on the retrieved surface albedo. \n\nThe data are stored in an enhanced netCDF-4 format.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "S5P_L2__CH4___",
             "creator": "Copernicus Sentinel data processed by ESA, Koninklijk Nederlands Meteorologisch Instituut (KNMI)/Netherlands Institute for Space Research (SRON)",
-            "title": "Sentinel-5P TROPOMI Methane CH4 1-Orbit L2 7km x 7km V1 (S5P_L2__CH4___) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/S5P_OFFL_L2__CH4____1.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Starting from August 6th in 2019, Sentinel-5P TROPOMI along-track high spatial resolution (~5.5km at nadir) has been implemented.\nFor data after August 6th of 2019, please check S5P_L2__CH4___ data collection.\n\nThe Copernicus Sentinel-5 Precursor (Sentinel-5P or S5P) satellite mission is one of the European Space Agency's (ESA) new mission family - Sentinels, and it is a joint initiative between the Kingdom of the Netherlands and the ESA. The sole payload on Sentinel-5P is the TROPOspheric Monitoring Instrument (TROPOMI), which is a nadir-viewing 108 degree Field-of-View push-broom grating hyperspectral spectrometer, covering the wavelength of ultraviolet-visible (UV-VIS, 270nm to 495nm), near infrared (NIR, 675nm to 775nm), and shortwave infrared (SWIR, 2305nm-2385nm). Sentinel-5P is the first of the Atmospheric Composition Sentinels and is expected to provide measurements of ozone, NO2, SO2, CH4, CO, formaldehyde, aerosols and cloud at high spatial, temporal and spectral resolutions.\n\nThe retrieval algorithm for Sentinel-5P TROPOMI methane product is a physics based method that uses the Oxygen-A band (760 nm) and absorption bands in shortwave infrared spectrum. In Sentinel-5P/TROPOMI methane algorithm, the atmosphere forward model simulates the absorbing gas (oxygen, methane, water vapor, and carbon monoxide) optical properties, as well as aerosol optical properties with size distribution, refractive index, and number concentration. The inversion is performed based on the forward calculation, the measurement, and the prior information. Cloud filtering is critical in methane retrieval, S5P methane algorithm applies re-gridded Visible Infrared Imaging Radiometer Suite (VIIRS) cloud mask data. Additional cloud filters based on S5P/TROPOMI measurements and the FRESCO apparent surface pressure will be applied when VIIRS cloud data are not available. Other current data filters in the retrieval algorithm include land-only pixels (excluding mountainous areas), spectrum intensity, solar zenith angle and instrument zenith angle. \n\nThe S5P/TROPOMI methane retrieval is for non-time-critical (NTC) data stream only, and its main outputs include the column averaged dry air mixing ratio of methane, the random error, and the biased corrected dry air methane fraction data based on the retrieved surface albedo. \n\nThe data are stored in an enhanced netCDF-4 format.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5270%2FS5P-3p6lnwd",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5270%2FS5P-3p6lnwd",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -55753,151 +55731,152 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/S5P_L2__CH4____1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/S5P_L2__CH4____1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/opendap/S5P_TROPOMI_Level2/S5P_L2__CH4___.1/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/opendap/S5P_TROPOMI_Level2/S5P_L2__CH4___.1/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/data/S5P_TROPOMI_Level2/S5P_L2__CH4___.1",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://tropomi.gesdisc.eosdis.nasa.gov/data/S5P_TROPOMI_Level2/S5P_L2__CH4___.1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sentinel.esa.int/documents/247904/3541451/Sentinel-5P-Methane-Product-Readme-File",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://sentinel.esa.int/documents/247904/3541451/Sentinel-5P-Methane-Product-Readme-File",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=S5P_L2__CH4____1",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=S5P_L2__CH4____1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sentinel.esa.int/documents/247904/2476257/Sentinel-5P-TROPOMI-ATBD-Methane-retrieval",
-                    "description": "Algorithm Theoretical Basis Document",
                     "@type": "dcat:Distribution",
+                    "description": "Algorithm Theoretical Basis Document",
+                    "downloadURL": "https://sentinel.esa.int/documents/247904/2476257/Sentinel-5P-TROPOMI-ATBD-Methane-retrieval",
+                    "mediaType": "text/html",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sentinel.esa.int/documents/247904/2474726/Sentinel-5P-Level-2-Product-User-Manual-Methane",
-                    "description": "Product User Manual Document",
                     "@type": "dcat:Distribution",
+                    "description": "Product User Manual Document",
+                    "downloadURL": "https://sentinel.esa.int/documents/247904/2474726/Sentinel-5P-Level-2-Product-User-Manual-Methane",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://sentinel.esa.int/web/sentinel/missions/sentinel-5p",
-                    "description": "ESA Copernicus Sentinel 5P Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "ESA Copernicus Sentinel 5P Home Page",
+                    "downloadURL": "https://sentinel.esa.int/web/sentinel/missions/sentinel-5p",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/information/glossary?title=Sentinel-5P",
-                    "description": "S5P TROPOMI Data Collection Summary",
                     "@type": "dcat:Distribution",
+                    "description": "S5P TROPOMI Data Collection Summary",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/information/glossary?title=Sentinel-5P",
+                    "mediaType": "text/html",
                     "title": "View this dataset's product history"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/S5P_OFFL_L2__CH4____1.png",
+            "identifier": "C1442068505-GES_DISC",
+            "issued": "2017-05-05",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5270/S5P-3p6lnwd",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-05-05",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "S5P_L2__CH4___",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2018-04-30T00:41:24Z/2022-01-17T00:00:00Z",
             "theme": [
                 "Sentinel-5P",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Sentinel-5P TROPOMI Methane CH4 1-Orbit L2 7km x 7km V1 (S5P_L2__CH4___) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://c3.nasa.gov/dashlink/resources/93/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2010-09-10",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "dashlink",
-                "ames",
-                "nasa"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Nisheeth Srivastava",
                 "hasEmail": "mailto:nisheeths@gmail.com"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Dashlink"
-            },
-            "identifier": "DASHLINK_93",
             "description": "Anomaly detection has recently become an important problem in many industrial and financial applications. In several instances, the data to be analyzed for possible anomalies is located at multiple sites and cannot be merged due to practical constraints such as bandwidth limitations and proprietary concerns. At the same time, the size of data sets affects prediction quality in almost all data mining applications. In such circumstances, distributed data mining algorithms may be used to extract information from multiple data sites in order to make better predictions. In the absence of theoretical guarantees, however, the degree to which data decentralization affects the performance of these algorithms is not known, which reduces the data providing participants' incentive to cooperate.This creates a metaphorical 'prisoners' dilemma' in the context of data mining.\r\n\r\n \r\n\r\nIn this work, we propose a novel general framework for distributed anomaly detection with theoretical performance guarantees. Our algorithmic approach combines existing anomaly detection procedures with a novel method for computing global statistics using local sufficient statistics. We show that the performance of such a distributed approach is indistinguishable from that of a centralized instantiation of the same anomaly detection algorithm, a condition that we call zero information loss. We further report experimental results on synthetic as well as real-world data to demonstrate the viability of our approach.\r\n\r\n The remaining content of this presentation is presented in Fig. 1.",
-            "title": "Solving a prisoner's dilemma in distributed anomaly detection",
-            "programCode": [
-                "026:029"
-            ],
             "distribution": [
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/CIDU09_distributed_AD.jpg",
-                    "description": ": CIDU09 poster",
                     "@type": "dcat:Distribution",
+                    "description": ": CIDU09 poster",
+                    "downloadURL": "https://c3.nasa.gov/dashlink/static/media/other/CIDU09_distributed_AD.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "CIDU09_distributed_AD.jpg"
                 }
             ],
-            "accrualPeriodicity": "irregular"
+            "identifier": "DASHLINK_93",
+            "issued": "2010-09-10",
+            "keyword": [
+                "dashlink",
+                "ames",
+                "nasa"
+            ],
+            "landingPage": "https://c3.nasa.gov/dashlink/resources/93/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:029"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Dashlink"
+            },
+            "title": "Solving a prisoner's dilemma in distributed anomaly detection"
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
-                "sharing",
-                "appel",
-                "knowledge",
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
-            "identifier": "NASA-862__50",
             "description": "Academy of Program/Project & Engineering Leadership's Ask the Academy magazine past issues.",
-            "title": "Academy of Program/Project & Engineering Leadership ASK the Academy Past Issues",
-            "programCode": [
-                "026:045"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -55905,81 +55884,80 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
+            "identifier": "NASA-862__50",
+            "issued": "2018-06-25",
+            "keyword": [
+                "sharing",
+                "appel",
+                "knowledge",
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
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-CAL-MIDAS-3-CVP-FULL-V1.0",
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
-                "calibration",
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Micro-Imaging Dust Analysis System (MIDAS) is an instrument on the ROSETTA Orbiter that will provide 3D images and statistical parameters of pristine cometary particles hitting the detector. This data set includes all data from the COMMISSIONING mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-cal-midas-3-cvp-full-v1.0_2yj5-gint",
+            "issued": "2018-06-26",
+            "keyword": [
+                "calibration",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-CAL-MIDAS-3-CVP-FULL-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-cal-midas-3-cvp-full-v1.0_2yj5-gint",
-            "description": "The Micro-Imaging Dust Analysis System (MIDAS) is an instrument on the ROSETTA Orbiter that will provide 3D images and statistical parameters of pristine cometary particles hitting the detector. This data set includes all data from the COMMISSIONING mission phase.",
-            "title": "ROSETTA-ORBITER CAL MIDAS 3 CVP FULL V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER CAL MIDAS 3 CVP FULL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://nasa3d.arc.nasa.gov/detail/crawler",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://www.nasa.gov/mission_pages/shuttle/main/index.html"
-            ],
-            "keyword": [
-                "transport",
-                "3d model",
-                "crawler",
-                "shuttle"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Beth Beck",
                 "hasEmail": "mailto:beth.beck@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "NASA-330__1",
             "description": "Originally designed to carry the towering Saturn V moon rocket from the Vehicle Assembly Building to the seaside launch site, the enormous transporters now carry the space shuttles to the launch pads for liftoff. Polygons: 146050 Vertices: 141658",
-            "title": "NASA 3D Models: Crawler",
-            "programCode": [
-                "026:045",
-                "026:046"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -55987,220 +55965,244 @@
                     "mediaType": "application/octet-stream"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-330__1",
+            "issued": "2018-06-25",
+            "keyword": [
+                "transport",
+                "3d model",
+                "crawler",
+                "shuttle"
+            ],
+            "landingPage": "http://nasa3d.arc.nasa.gov/detail/crawler",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:045",
+                "026:046"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
+            "references": [
+                "http://www.nasa.gov/mission_pages/shuttle/main/index.html"
+            ],
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "NASA 3D Models: Crawler"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-PRL-67P-M04-INF-REFL-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in reflectance units (normalized  and thus without unit),  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the PRELANDING mission phase, covering the period  from 2014-06-04T10:50:00.000 to 2014-07-02T08:34:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-prl-67p-m04-inf-refl-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-PRL-67P-M04-INF-REFL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-prl-67p-m04-inf-refl-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in reflectance units (normalized  and thus without unit),  acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft  during the PRELANDING mission phase, covering the period  from 2014-06-04T10:50:00.000 to 2014-07-02T08:34:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 PRL-MTP004 RDR-INF-REFL V1.0",
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
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 PRL-MTP004 RDR-INF-REFL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-RPCMAG-2-EAR3-RAW-V3.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This dataset contains EDITED RAW DATA of the third  Earth Swingby\n(EAR3). The closest approach (CA) took place on November 13, 2009\nat 07:45. Additionally data from the Payload Checkout PC10 are added.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-rpcmag-2-ear3-raw-v3.0_2ynh-bzwf",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "international rosetta mission",
                 "earth",
                 "checkout"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-E-RPCMAG-2-EAR3-RAW-V3.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-e-rpcmag-2-ear3-raw-v3.0_2ynh-bzwf",
-            "description": "This dataset contains EDITED RAW DATA of the third  Earth Swingby\n(EAR3). The closest approach (CA) took place on November 13, 2009\nat 07:45. Additionally data from the Payload Checkout PC10 are added.",
-            "title": "ROSETTA-ORBITER EARTH RPCMAG 2 EAR3 RAW V3.0",
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
+            "title": "ROSETTA-ORBITER EARTH RPCMAG 2 EAR3 RAW V3.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-N-MAG-4-SUMM-NLSCOORDS-12SEC-V1.0",
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
-                "voyager",
-                "neptune"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Voyager magnetometer investigation (P.I.- Norman F. Ness) makes available archival data through the National Space Science Data Center (NSSDC) located at NASA/GSFC as well as through the Planetary Data System (PDS) and other channels. The primary archive format, referred to as a 'summary tape' or 'conjoint summary tape' has been used consistently since the beginning of the Voyager mission to the outer planets (1977). This format makes available magnetometer observations, supplementary engineering and ephemeris data in one data file, and it is one product of Voyager magnetometer routine data processing. Users are referred to the summary format data for all data requirements with one exception: Neptune encounter high field observations. Neptune close approach observations are archived separately and in a different format from that with which many are familiar. This high-field archive is described here.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-n-mag-4-summ-nlscoords-12sec-v1.0_2yrc-x26u",
+            "issued": "2021-05-21",
+            "keyword": [
+                "voyager",
+                "neptune"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG2-N-MAG-4-SUMM-NLSCOORDS-12SEC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg2-n-mag-4-summ-nlscoords-12sec-v1.0_2yrc-x26u",
-            "description": "The Voyager magnetometer investigation (P.I.- Norman F. Ness) makes available archival data through the National Space Science Data Center (NSSDC) located at NASA/GSFC as well as through the Planetary Data System (PDS) and other channels. The primary archive format, referred to as a 'summary tape' or 'conjoint summary tape' has been used consistently since the beginning of the Voyager mission to the outer planets (1977). This format makes available magnetometer observations, supplementary engineering and ephemeris data in one data file, and it is one product of Voyager magnetometer routine data processing. Users are referred to the summary format data for all data requirements with one exception: Neptune encounter high field observations. Neptune close approach observations are archived separately and in a different format from that with which many are familiar. This high-field archive is described here.",
-            "title": "VG2 NEP MAG RESAMPLED SUMMARY NLS COORDINATES 12SEC V1.0",
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
+            "title": "VG2 NEP MAG RESAMPLED SUMMARY NLS COORDINATES 12SEC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://techport.nasa.gov/view/14682",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2014-04-01",
-            "temporal": "2014-04-01T00:00:00Z/2014-09-01T00:00:00Z",
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
-                "completed",
-                "project",
-                "glenn research center"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Michael Kulis",
                 "hasEmail": "mailto:michael.j.kulis@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Space Technology Mission Directorate"
-            },
-            "identifier": "TECHPORT_14682",
             "description": "&lt;p&gt;The objective of the proposed work is to develop a rapid time response diagnostic using a suite of instruments for the detection of heated&amp;nbsp;polytetrafluoroethylene (PTFE) insulated wires based on chemicals and particles generated at relatively low temperatures. &amp;nbsp;The anticipated result of the proposed effort is the development of a conceptual design for an early warning system that can specifically detect the overheating of&amp;nbsp;polytetrafluoroethylene (PTFE) insulated wires. This design can be utilized as a subsystem integrated into a fully capable fire detection system.&lt;/p&gt;",
-            "title": "Early Detection of Overheating Polytetrafluoroethylene Insulated Wires Project",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "http://techport.nasa.gov/xml-api/14682",
                     "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "TECHPORT_14682",
+            "issued": "2014-04-01",
+            "keyword": [
+                "completed",
+                "project",
+                "glenn research center"
+            ],
+            "landingPage": "http://techport.nasa.gov/view/14682",
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
+            "temporal": "2014-04-01T00:00:00Z/2014-09-01T00:00:00Z",
+            "title": "Early Detection of Overheating Polytetrafluoroethylene Insulated Wires Project"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3337-V1.0",
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
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-07-05T07:14:24.000 to 2012-07-05T09:03:36.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3337-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars express"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3337-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3337-v1.0",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-07-05T07:14:24.000 to 2012-07-05T09:03:36.500.",
-            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3337 V1.0",
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
+            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3337 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-ROSINA-2-CR4B-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set present engineering data of the COPS and DFMS ROSINA sensors during the S/C Themal Characterization test- Cruise 4-2 phase. Version 2.0 contains significant corrections to the V1.0 data set.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rosina-2-cr4b-v2.0_2yvk-jdua",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "2867 steins",
                 "international rosetta mission",
@@ -56209,1179 +56211,1155 @@
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "21 lutetia"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-ROSINA-2-CR4B-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-rosina-2-cr4b-v2.0_2yvk-jdua",
-            "description": "This data set present engineering data of the COPS and DFMS ROSINA sensors during the S/C Themal Characterization test- Cruise 4-2 phase. Version 2.0 contains significant corrections to the V1.0 data set.",
-            "title": "ROSETTA-ORBITER CHECK ROSINA 2 CR4B V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ROSETTA-ORBITER CHECK ROSINA 2 CR4B V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/GPMGV/OLYMPEX/MULTIPLE/DATA401",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Stocker, Erich .2018. GPM Ground Validation Composite Satellite Overpasses OLYMPEX [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/GPMGV/OLYMPEX/MULTIPLE/DATA401",
-            "issued": "2018-07-23",
-            "temporal": "2015-11-01T01:26:15Z/2016-05-01T21:36:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
-            "keyword": [
-                "atmospheric water vapor",
-                "precipitation",
-                "microwave",
-                "atmosphere",
-                "spectral/engineering",
-                "earth science"
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
-            "identifier": "C1979643229-GHRC_DAAC",
             "description": "The GPM Ground Validation Composite Satellite Overpasses OLYMPEX dataset provides brightness temperature, precipitation, and total column water vapor estimates from multiple satellite overpasses including DMSP F16-19, GCOM-W1, GPM, MetOp, NOAA, and NPP for the OLYMPEX field campaign. The OLYMPEX field campaign took place between November, 2015, and January, 2016, with additional ground sampling continuing through February, on the Olympic Peninsula in the Pacific Northwest of the United States. This field campaign provides ground-based validation support of the findings resulting from the Global Precipitation Measurement (GPM) Core Observatory satellite. Data files are available from November 1, 2015 thru May 1, 2016 in HDF-5 format.",
-            "title": "GPM Ground Validation Composite Satellite Overpasses OLYMPEX V4",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FOLYMPEX%2FMULTIPLE%2FDATA401",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FGPMGV%2FOLYMPEX%2FMULTIPLE%2FDATA401",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmopassolyx",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=gpmopassolyx",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://dx.doi.org/10.5067/GPMGV/OLYMPEX/DATA101",
-                    "description": "OLYMPEX Field Campaign Collection DOI",
                     "@type": "dcat:Distribution",
+                    "description": "OLYMPEX Field Campaign Collection DOI",
+                    "downloadURL": "http://dx.doi.org/10.5067/GPMGV/OLYMPEX/DATA101",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://olympex.atmos.washington.edu/",
-                    "description": "University of Washington OLYMPEX project web site",
                     "@type": "dcat:Distribution",
+                    "description": "University of Washington OLYMPEX project web site",
+                    "downloadURL": "http://olympex.atmos.washington.edu/",
+                    "mediaType": "text/html",
                     "title": "View information related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/overpasses/doc/gpmopassolyx_dataset.pdf",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/gpmValidation/olympex/overpasses/doc/gpmopassolyx_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://doi.org/10.1175/JTECH-D-16-0100.1",
-                    "description": "Intercalibration of the GPM Microwave Radiometer Constellation",
                     "@type": "dcat:Distribution",
+                    "description": "Intercalibration of the GPM Microwave Radiometer Constellation",
+                    "downloadURL": "http://doi.org/10.1175/JTECH-D-16-0100.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/JTECH-D-16-0019.1",
-                    "description": "The GPM combined algorithm",
                     "@type": "dcat:Distribution",
+                    "description": "The GPM combined algorithm",
+                    "downloadURL": "https://doi.org/10.1175/JTECH-D-16-0019.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.1175/JTECH-D-15-0039.1",
-                    "description": "The evolution of the Goddard profiling algorithm to a fully parametric scheme",
                     "@type": "dcat:Distribution",
+                    "description": "The evolution of the Goddard profiling algorithm to a fully parametric scheme",
+                    "downloadURL": "https://doi.org/10.1175/JTECH-D-15-0039.1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://journals.ametsoc.org/topic/gpm",
-                    "description": "Precipitation Retrieval Algorithms for GPM",
                     "@type": "dcat:Distribution",
+                    "description": "Precipitation Retrieval Algorithms for GPM",
+                    "downloadURL": "https://journals.ametsoc.org/topic/gpm",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/olympex",
-                    "description": "GHRC OLYMPEX project web page",
                     "@type": "dcat:Distribution",
+                    "description": "GHRC OLYMPEX project web page",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/olympex",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
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
-            "spatial": "-157.22 37.3591 -88.4232 57.4634",
-            "theme": [
-                "OLYMPEX",
-                "geospatial"
-            ],
+            "identifier": "C1979643229-GHRC_DAAC",
+            "issued": "2018-07-23",
+            "keyword": [
+                "atmospheric water vapor",
+                "precipitation",
+                "microwave",
+                "atmosphere",
+                "spectral/engineering",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/GPMGV/OLYMPEX/MULTIPLE/DATA401",
             "language": [
                 "en-US"
-            ]
+            ],
+            "modified": "2022-04-28",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/MSFC/GHRC"
+            },
+            "spatial": "-157.22 37.3591 -88.4232 57.4634",
+            "temporal": "2015-11-01T01:26:15Z/2016-05-01T21:36:00Z",
+            "theme": [
+                "OLYMPEX",
+                "geospatial"
+            ],
+            "title": "GPM Ground Validation Composite Satellite Overpasses OLYMPEX V4"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/WB224IA3PVOJ",
             "citation": "NLDAS project. David M. Mocko,  NASA/GSFC/HSL. 2022-01-08. NLDAS_NOAH0125_M. Version 2.0. NLDAS Noah Land Surface Model L4 Monthly 0.125 x 0.125 degree V2.0. Greenbelt, Maryland, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/WB224IA3PVOJ. https://disc.gsfc.nasa.gov/datacollection/NLDAS_NOAH0125_M_2.0.html. Digital Science Data.",
-            "issued": "2020-06-18",
-            "temporal": "1979-01-01T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-06-18",
-            "references": [
-                "https://doi.org/10.1029/2011JD016048",
-                "https://doi.org/10.1029/2011JD016051",
-                "https://doi.org/10.1175/1520-0493(1997)125%3C2896%3AAOTLSA%3E2.0.CO%3B2",
-                "https://doi.org/10.1023/A%3A1000531001463",
-                "https://doi.org/10.1029/2002JD003296",
-                "https://doi.org/10.1029/1999JD900232",
-                "https://doi.org/10.1175/2009JHM1174.1",
-                "https://doi.org/10.1002/hyp.9214"
-            ],
-            "keyword": [
-                "precipitation",
-                "vegetation",
-                "terrestrial hydrosphere",
-                "surface water",
-                "surface thermal properties",
-                "surface radiative properties",
-                "soils",
-                "snow/ice",
-                "land surface",
-                "earth science",
-                "biosphere",
-                "atmospheric water vapor",
-                "atmospheric temperature",
-                "atmospheric radiation",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Hualan Rui",
                 "hasEmail": "mailto:Hualan.Rui@nasa.gov"
             },
+            "creator": "NLDAS project",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1887990023-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "This data set contains fifty-two fields simulated from the Noah land-surface model (LSM) for Phase 2 of the North American Land Data Assimilation System (NLDAS-2). The data are in 1/8th degree grid spacing and range from Jan 1979 to the present. The temporal resolution is monthly. The file format is netCDF (converted from the GRIB format). \n\nThe NLDAS-2 monthly Noah model data, containing fifty-two fields, were generated from the NLDAS-2 hourly Noah model data, as monthly accumulation for rainfall, snowfall, subsurface runoff, surface runoff, total evapotranspiration, snow melt, and monthly averages for other variables. The monthly period of each month is from 00Z at start of the month to 23:59Z at end of the month, with the exception of the very first month in the data set (Jan 1979) which starts at 00Z 02 Jan 1979. Also for the first month (Jan 1979), because the variables listed as instantaneous in the README file do not have valid data exactly on 00Z 02 Jan 1979, and this one hour is not included in the average for this month only. \n\nDetails about the NLDAS-2 configuration of the Noah LSM can be found in Xia et al. (2012).",
-            "editor": "David M. Mocko,  NASA/GSFC/HSL",
-            "release-place": "Greenbelt, Maryland, USA",
-            "series-name": "NLDAS_NOAH0125_M",
-            "creator": "NLDAS project",
-            "graphic-preview-description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
-            "title": "NLDAS Noah Land Surface Model L4 Monthly 0.125 x 0.125 degree V2.0 (NLDAS_NOAH0125_M) at GES DISC",
-            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=NLDAS_NOAH0125_M_2.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FWB224IA3PVOJ",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FWB224IA3PVOJ",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/NLDAS_NOAH0125_M_2.0.png",
-                    "description": "NLDAS-2 Noah Monthly 0.125 degree Soil moisture content (0-10cm) [kg m-2] January 1979.",
                     "@type": "dcat:Distribution",
+                    "description": "NLDAS-2 Noah Monthly 0.125 degree Soil moisture content (0-10cm) [kg m-2] January 1979.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/NLDAS_NOAH0125_M_2.0.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/NLDAS_NOAH0125_M_2.0.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/NLDAS_NOAH0125_M_2.0.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/NLDAS/NLDAS_NOAH0125_M.2.0/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/NLDAS/NLDAS_NOAH0125_M.2.0/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=NLDAS_NOAH0125_M",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=NLDAS_NOAH0125_M",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=NLDAS_NOAH0125_M_2.0",
-                    "description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
                     "@type": "dcat:Distribution",
+                    "description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
+                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=NLDAS_NOAH0125_M_2.0",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through GIOVANNI"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/dods/NLDAS_NOAH0125_M.2.0",
-                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
                     "@type": "dcat:Distribution",
+                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/dods/NLDAS_NOAH0125_M.2.0",
+                    "mediaType": "text/html",
                     "title": "Use GRADS DATA SERVER (GDS) to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/NLDAS/NLDAS2_README.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/NLDAS/NLDAS2_README.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ldas.gsfc.nasa.gov/nldas/",
-                    "description": "NLDAS Project Web Site",
                     "@type": "dcat:Distribution",
+                    "description": "NLDAS Project Web Site",
+                    "downloadURL": "https://ldas.gsfc.nasa.gov/nldas/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/information/howto?tags=hydrology",
-                    "description": "How to read and plot the data.",
                     "@type": "dcat:Distribution",
+                    "description": "How to read and plot the data.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/information/howto?tags=hydrology",
+                    "mediaType": "text/html",
                     "title": "View this dataset's how-to documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/information/documents?title=Hydrology+Documentation",
-                    "description": "GES DISC Hydrology Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "GES DISC Hydrology Documentation",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/information/documents?title=Hydrology+Documentation",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/opendap/NLDAS/NLDAS_NOAH0125_M.2.0/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/opendap/NLDAS/NLDAS_NOAH0125_M.2.0/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/thredds/catalog/NLDAS_aggregation/NLDAS_NOAH0125_M.2.0/catalog.html",
-                    "description": "Time aggregated THREDDS Data Server (TDS)",
                     "@type": "dcat:Distribution",
+                    "description": "Time aggregated THREDDS Data Server (TDS)",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/thredds/catalog/NLDAS_aggregation/NLDAS_NOAH0125_M.2.0/catalog.html",
+                    "mediaType": "text/html",
                     "title": "Use THREDDS DATA to download the dataset's data"
                 }
             ],
+            "editor": "David M. Mocko,  NASA/GSFC/HSL",
+            "graphic-preview-description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
+            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=NLDAS_NOAH0125_M_2.0",
+            "identifier": "C1887990023-GES_DISC",
+            "issued": "2020-06-18",
+            "keyword": [
+                "precipitation",
+                "vegetation",
+                "terrestrial hydrosphere",
+                "surface water",
+                "surface thermal properties",
+                "surface radiative properties",
+                "soils",
+                "snow/ice",
+                "land surface",
+                "earth science",
+                "biosphere",
+                "atmospheric water vapor",
+                "atmospheric temperature",
+                "atmospheric radiation",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/WB224IA3PVOJ",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-06-18",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.1029/2011JD016048",
+                "https://doi.org/10.1029/2011JD016051",
+                "https://doi.org/10.1175/1520-0493(1997)125%3C2896%3AAOTLSA%3E2.0.CO%3B2",
+                "https://doi.org/10.1023/A%3A1000531001463",
+                "https://doi.org/10.1029/2002JD003296",
+                "https://doi.org/10.1029/1999JD900232",
+                "https://doi.org/10.1175/2009JHM1174.1",
+                "https://doi.org/10.1002/hyp.9214"
+            ],
+            "release-place": "Greenbelt, Maryland, USA",
+            "series-name": "NLDAS_NOAH0125_M",
             "spatial": "-125.0 25.0 -67.0 53.0",
+            "temporal": "1979-01-01T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "NLDAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NLDAS Noah Land Surface Model L4 Monthly 0.125 x 0.125 degree V2.0 (NLDAS_NOAH0125_M) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/SEAC4RS_TraceGas_AircraftInSitu_ER2_Data_1",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2021-09-07. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC/SUBORBITAL/SEAC4RS_TraceGas_AircraftInSitu_ER2_Data_1.",
-            "issued": "2021-03-19",
-            "temporal": "2013-08-01T00:00:00Z/2013-09-23T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-20",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "atmospheric chemistry"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Gao Chen",
                 "hasEmail": "mailto:gao.chen@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C2119341690-LARC_ASDC",
             "description": "SEAC4RS_TraceGas_AircraftInSitu_ER2_Data are in-situ trace gas data collected onboard the ER-2 aircraft during the Studies of Emissions and Atmospheric Composition, Clouds and Climate Coupling by Regional Surveys (SEA4CRS) airborne field study. Data collection for this product is complete.\r\n\r\nStudies of Emissions and Atmospheric Composition, Clouds and Climate Coupling by Regional Surveys (SEAC4RS) airborne field study was conducted in August and September of 2013. The field operation was based in Houston, Texas. The primary SEAC4RS science objectives are: to determine how pollutant emissions are redistributed via deep convection throughout the troposphere; to determine the evolution of gases and aerosols in deep convective outflow and the implications for UT/LS chemistry; to identify the influences and feedbacks of aerosol particles from anthropogenic pollution and biomass burning on meteorology and climate through changes in the atmospheric heat budget (i.e., semi-direct effect) or through microphysical changes in clouds (i.e., indirect effects); and lastly, to serve as a calibration and validation test bed for future satellite instruments and missions.\r\n\r\nThe airborne observational data were collected from three aircraft platforms: the NASA DC-8, ER-2, and SPEC LearJet. Both the NASA DC-8 and ER-2 aircraft were instrumented for comprehensive in-situ and remote sensing measurements of the trace gas, aerosol properties, and cloud properties. In addition, radiative fluxes and meteorological parameters were also recorded. The NASA DC-8 was mostly responsible for tropospheric sampling, while the NASA ER-2 was operating in the lower stratospheric regime. The SPEC LearJet was dedicated to in-situ cloud characterizations. To accomplish the science objectives, the flight plans were designed to investigate the influence of biomass burning and pollution, their temporal evolution, and ultimately, impacts on meteorological processes which can, in turn, feedback on regional air quality. With respect to meteorological feedbacks, the opportunity to examine the impact of polluting aerosols on cloud properties and dynamics was of particular interest.",
-            "title": "SEAC4RS ER-2 Aircraft In-Situ Trace Gas Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSEAC4RS_TraceGas_AircraftInSitu_ER2_Data_1",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC%2FSUBORBITAL%2FSEAC4RS_TraceGas_AircraftInSitu_ER2_Data_1",
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://espo.nasa.gov/sites/default/files/documents/SEAC4RS_DraftPlan_20130409b_USA.pdf",
-                    "description": "SEAC4RS Draft Plan",
                     "@type": "dcat:Distribution",
+                    "description": "SEAC4RS Draft Plan",
+                    "downloadURL": "https://espo.nasa.gov/sites/default/files/documents/SEAC4RS_DraftPlan_20130409b_USA.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://www-air.larc.nasa.gov/missions/dc3-seac4rs/docs/SEAC4RS_Data_Management_Plan.pdf",
-                    "description": "SEAC4RS/DC3 Data Management Plan",
                     "@type": "dcat:Distribution",
+                    "description": "SEAC4RS/DC3 Data Management Plan",
+                    "downloadURL": "https://www-air.larc.nasa.gov/missions/dc3-seac4rs/docs/SEAC4RS_Data_Management_Plan.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://espo.nasa.gov/seac4rs",
-                    "description": "SEAC4RS Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "SEAC4RS Project Home Page",
+                    "downloadURL": "https://espo.nasa.gov/seac4rs",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.nasa.gov/topics/earth/features/seac4rs_2013.html",
-                    "description": "SEAC4RS nasa.gov feature article",
                     "@type": "dcat:Distribution",
+                    "description": "SEAC4RS nasa.gov feature article",
+                    "downloadURL": "https://www.nasa.gov/topics/earth/features/seac4rs_2013.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2015JD024297",
-                    "description": "SEAC4RS Overview Paper",
                     "@type": "dcat:Distribution",
+                    "description": "SEAC4RS Overview Paper",
+                    "downloadURL": "https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2015JD024297",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2119341690-LARC_ASDC",
-                    "description": "Earthdata Search for SEAC4RS_TraceGas_AircraftInSitu_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for SEAC4RS_TraceGas_AircraftInSitu_Data_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2119341690-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/SEAC4RS_TraceGas_AircraftInSitu_ER2_Data_1",
-                    "description": "DOI data set landing page for SEAC4RS_TraceGas_AircraftInSitu_ER2_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for SEAC4RS_TraceGas_AircraftInSitu_ER2_Data_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC/SUBORBITAL/SEAC4RS_TraceGas_AircraftInSitu_ER2_Data_1",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/SEAC4RS/TraceGas_AircraftInSitu_ER2_Data_1/",
-                    "description": "ASDC Direct Data Download for SEAC4RS_TraceGas_AircraftInSitu_ER2_Data_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for SEAC4RS_TraceGas_AircraftInSitu_ER2_Data_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/SEAC4RS/TraceGas_AircraftInSitu_ER2_Data_1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 }
             ],
+            "identifier": "C2119341690-LARC_ASDC",
+            "issued": "2021-03-19",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "atmospheric chemistry"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC/SUBORBITAL/SEAC4RS_TraceGas_AircraftInSitu_ER2_Data_1",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-04-20",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:9825\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>15.0 -128.0 15.0 -82.0 53.0 -82.0 53.0 -128.0 15.0 -128.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "2013-08-01T00:00:00Z/2013-09-23T23:59:59.999Z",
             "theme": [
                 "SEAC4RS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SEAC4RS ER-2 Aircraft In-Situ Trace Gas Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/TEMSC-AT634",
             "citation": "D. N. Wiese, D.-N. Yuan, C. Boening, F. W. Landerer, M. M. Watkins. 2023-01-25. Tellus Level-4 ANTARCTICA Mass Anomaly Time Series. Version RL06.3Mv04. Tellus Level-4 Ocean Mass Anomaly Time Series from JPL GRACE/GRACE-FO Mascon CRI Filtered Release 06.3 version 04. JPL/PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, JPL/Tellus. https://doi.org/10.5067/TEMSC-AT634. http://grace.jpl.nasa.gov/data/get-data/jpl_global_mascons/.",
-            "issued": "2020-02-14",
-            "temporal": "2002-04-01T00:00:00Z/2024-11-11T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-02-14",
-            "references": [
-                "https://doi.org/10.1002/2014JB011547"
-            ],
-            "keyword": [
-                "earth science",
-                "glaciers/ice sheets",
-                "climate indicators",
-                "cryospheric indicators",
-                "cryosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:podaac@podaac.jpl.nasa.gov"
             },
-            "identifier": "C3206284786-POCLOUD",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/JPL/PODAAC"
-            },
-            "description": "This dataset is a time series of mass variability averaged over all of the global ocean. It provides the non-steric or mass only sea level changes over time. The mass variability are derived from JPL GRACE Mascon Ocean, Ice, and Hydrology Equivalent Water Height CRI Filtered RL063Mv04 dataset, which can be found at https://podaac.jpl.nasa.gov/dataset/TELLUS_GRAC-GRFO_MASCON_CRI_GRID_RL06.3_V4. A more detailed description on the Mascon solution, including the mathematical derivation, implementation of geophysical constraints, and solution validation, please see Watkins et al., 2015, doi: 10.1002/2014JB011547. The mass variability are provided as an ASCII table.",
-            "release-place": "JPL/PO.DAAC",
-            "series-name": "Tellus Level-4 ANTARCTICA Mass Anomaly Time Series",
             "creator": "D. N. Wiese, D.-N. Yuan, C. Boening, F. W. Landerer, M. M. Watkins",
-            "title": "Tellus Level-4 Antarctica Mass Anomaly Time Series from JPL GRACE/GRACE-FO Mascon CRI Filtered Release 06.3 version 04",
-            "graphic-preview-description": "Thumbnail",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ANTARCTICA_MASS_TELLUS_MASCON_CRI_TIME_SERIES_RL06.3_V4.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset is a time series of mass variability averaged over all of the global ocean. It provides the non-steric or mass only sea level changes over time. The mass variability are derived from JPL GRACE Mascon Ocean, Ice, and Hydrology Equivalent Water Height CRI Filtered RL063Mv04 dataset, which can be found at https://podaac.jpl.nasa.gov/dataset/TELLUS_GRAC-GRFO_MASCON_CRI_GRID_RL06.3_V4. A more detailed description on the Mascon solution, including the mathematical derivation, implementation of geophysical constraints, and solution validation, please see Watkins et al., 2015, doi: 10.1002/2014JB011547. The mass variability are provided as an ASCII table.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTEMSC-AT634",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTEMSC-AT634",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://grace.jpl.nasa.gov/data/get-data/jpl_global_mascons/",
-                    "description": "Additional resource and information site for the Global Mascon datasets. This includes update announcements, user feedback page, and FAQ's.",
                     "@type": "dcat:Distribution",
+                    "description": "Additional resource and information site for the Global Mascon datasets. This includes update announcements, user feedback page, and FAQ's.",
+                    "downloadURL": "http://grace.jpl.nasa.gov/data/get-data/jpl_global_mascons/",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/GRACE-FO",
-                    "description": "PODAAC's GRACE-FO Project-Page",
                     "@type": "dcat:Distribution",
+                    "description": "PODAAC's GRACE-FO Project-Page",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/GRACE-FO",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/GRACE",
-                    "description": "PODAAC's GRACE Project-Page",
                     "@type": "dcat:Distribution",
+                    "description": "PODAAC's GRACE Project-Page",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/GRACE",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ANTARCTICA_MASS_TELLUS_MASCON_CRI_TIME_SERIES_RL06.3_V4.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ANTARCTICA_MASS_TELLUS_MASCON_CRI_TIME_SERIES_RL06.3_V4.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C3206284786-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C3206284786-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C3206284786-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C3206284786-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/gravity/gracefo-documentation",
-                    "description": "Page with GRACE-FO documentation and technical notes for many of the project's data products",
                     "@type": "dcat:Distribution",
+                    "description": "Page with GRACE-FO documentation and technical notes for many of the project's data products",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/gravity/gracefo-documentation",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/gracefo/open/docs/GRACE_GRACE-FO_ReleaseNotes_JPL_MASCON.txt",
-                    "description": "RL0.63 Version 4 Release Note",
                     "@type": "dcat:Distribution",
+                    "description": "RL0.63 Version 4 Release Note",
+                    "downloadURL": "https://archive.podaac.earthdata.nasa.gov/podaac-ops-cumulus-docs/gracefo/open/docs/GRACE_GRACE-FO_ReleaseNotes_JPL_MASCON.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Thumbnail",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ANTARCTICA_MASS_TELLUS_MASCON_CRI_TIME_SERIES_RL06.3_V4.jpg",
+            "identifier": "C3206284786-POCLOUD",
+            "issued": "2020-02-14",
+            "keyword": [
+                "earth science",
+                "glaciers/ice sheets",
+                "climate indicators",
+                "cryospheric indicators",
+                "cryosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/TEMSC-AT634",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2020-02-14",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "references": [
+                "https://doi.org/10.1002/2014JB011547"
+            ],
+            "release-place": "JPL/PO.DAAC",
+            "series-name": "Tellus Level-4 ANTARCTICA Mass Anomaly Time Series",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-04-01T00:00:00Z/2024-11-11T00:00:00Z",
             "theme": [
                 "GRACE",
                 "GRACE-FO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Tellus Level-4 Antarctica Mass Anomaly Time Series from JPL GRACE/GRACE-FO Mascon CRI Filtered Release 06.3 version 04"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-CAL-ROMAP-2-CR5-SPM-V1.0",
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
-                "calibration"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This archive contains level 2 data from the ROMAP SPM instrument onboard ROSETTA Lander, acquired during the CR5 (cruise 5) phase. It also contains documentation which describes the ROMAP experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-cal-romap-2-cr5-spm-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "calibration"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-CAL-ROMAP-2-CR5-SPM-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-cal-romap-2-cr5-spm-v1.0",
-            "description": "This archive contains level 2 data from the ROMAP SPM instrument onboard ROSETTA Lander, acquired during the CR5 (cruise 5) phase. It also contains documentation which describes the ROMAP experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-LANDER CAL ROMAP 2 CR5 SPM V1.0",
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
+            "title": "ROSETTA-LANDER CAL ROMAP 2 CR5 SPM V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/684",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Ramankutty, N., and J.A. Foley. 2002. LBA Regional Potential Vegetation, 5-min (Ramankutty and Foley). ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/684",
-            "issued": "2023-10-03",
-            "temporal": "1900-01-01T00:00:00Z/1992-01-01T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-04",
-            "keyword": [
-                "biosphere",
-                "vegetation",
-                "earth science"
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
-            "identifier": "C2777327573-ORNL_CLOUD",
             "description": "The data set consists of a subset for the study area of the Large Scale Biosphere-Atmosphere Experiment in Amazonia (LBA) in South America (i.e., longitude 85 deg to 30 deg W, latitude 25 deg S to 10 deg N) of the 5-min resolution Global Potential Vegetation data set developed by Navin Ramankutty and Jon Foley at the University of Wisconsin. Data are available in both ASCII GRID and binary image file formats.The original map was derived at a 5-min resolution and contains natural vegetation classified into 15 types.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA Regional Potential Vegetation, 5-min (Ramankutty and Foley)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/684_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F684",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F684",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/land_use_land_cover_change/potential_vegetation/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/land_use_land_cover_change/potential_vegetation/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/lba_uwveg.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/lba_uwveg.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/684",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/684",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/potential_vegetation/comp//uwveg_readme.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/land_use_land_cover_change/potential_vegetation/comp//uwveg_readme.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/684_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/684_1_fit.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=684",
-                    "description": "Web Coverage Service for this collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Web Coverage Service for this collection.",
+                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=684",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/684_1_fit.png",
+            "identifier": "C2777327573-ORNL_CLOUD",
+            "issued": "2023-10-03",
+            "keyword": [
+                "biosphere",
+                "vegetation",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/684",
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
             "spatial": "-85.0 -25.0 -30.0 10.0",
+            "temporal": "1900-01-01T00:00:00Z/1992-01-01T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA Regional Potential Vegetation, 5-min (Ramankutty and Foley)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/Aqua/AIRS/DATA311",
             "citation": "AIRS Science Team/Joao Teixeira. 2013-03-12. AIRH3ST8. Version 006. AIRS/Aqua L3 8-day Standard Physical Retrieval (AIRS+AMSU+HSB) 1 degree x 1 degree V006. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aqua/AIRS/DATA311. https://disc.gsfc.nasa.gov/datacollection/AIRH3ST8_006.html. Digital Science Data.",
-            "issued": "2002-09-01",
-            "temporal": "2002-09-01T00:00:00Z/2003-02-08T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2003-02-08",
-            "keyword": [
-                "atmospheric water vapor",
-                "clouds",
-                "atmospheric radiation",
-                "earth science",
-                "land surface",
-                "atmospheric pressure",
-                "oceans",
-                "ocean temperature",
-                "surface radiative properties",
-                "atmospheric chemistry",
-                "atmosphere",
-                "altitude",
-                "surface thermal properties",
-                "air quality",
-                "atmospheric temperature"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ED ESFANDIARI",
                 "hasEmail": "mailto:asghar.e.esfandiari@nasa.gov"
             },
+            "creator": "AIRS Science Team/Joao Teixeira",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1238517250-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "The Atmospheric Infrared Sounder (AIRS) is a grating spectrometer (R = 1200) aboard the second Earth Observing System (EOS) polar-orbiting platform, EOS Aqua. In combination with the Advanced Microwave Sounding Unit (AMSU) and the Humidity Sounder for Brazil (HSB), AIRS constitutes an innovative atmospheric sounding group of visible, infrared, and microwave sensors. This product is similar to AIRX3ST8. However, it contains science retrievals that use the Humidity Sounder for Brazil (HSB). Because the HSB instrument lived only from September 2002 through January 2003 when it terminally failed, the data set covers these five months only. The AIRS Level 3 8-Day Gridded Retrieval Product contains standard retrieval means, standard deviations and input counts. Each file covers an 8-day period, or one-half of the Aqua orbit repeat cycle. The mean values are simply the arithmetic means of the daily products, weighted by the number of input counts for each day in that grid box. The geophysical parameters have been averaged and binned into 1 x 1 deg grid cells, from -180.0 to +180.0 deg longitude and from -90.0 to +90.0 deg latitude. For each grid map of 4-byte floating-point mean values there is a corresponding 4-byte floating-point map of standard deviation and a 2-byte integer grid map of counts. The counts map provides the user with the number of points per bin that were included in the mean and can be used to generate custom multi-day maps from the daily gridded products. The thermodynamic parameters are: Skin Temperature (land and sea surface), Air Temperature at the surface, Profiles of Air Temperature and Water Vapor, Tropopause Characteristics, Column Precipitable Water, Cloud Amount/Frequency, Cloud Height, Cloud Top Pressure, Cloud Top Temperature, Reflectance, Emissivity, Surface Pressure, Cloud Vertical Distribution. The trace gases parameters are: Total Amounts and Vertical Profiles of Carbon Monoxide, Methane, and Ozone. The actual names of the variables in the data files should be inferred from the Processing File Description document.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "AIRH3ST8",
-            "creator": "AIRS Science Team/Joao Teixeira",
-            "title": "AIRS/Aqua L3 8-day Standard Physical Retrieval (AIRS+AMSU+HSB) 1 degree x 1 degree V006 (AIRH3ST8) at GES DISC",
-            "graphic-preview-description": "Sample data of the \"AIRS/Aqua Level 3 multiday standard physical retrieval\".",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRH3ST8_006.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAqua%2FAIRS%2FDATA311",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAqua%2FAIRS%2FDATA311",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRH3ST8_006.png",
-                    "description": "Sample data of the \"AIRS/Aqua Level 3 multiday standard physical retrieval\".",
                     "@type": "dcat:Distribution",
+                    "description": "Sample data of the \"AIRS/Aqua Level 3 multiday standard physical retrieval\".",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRH3ST8_006.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRH3ST8_006.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/AIRH3ST8_006.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_Level3/AIRH3ST8.006/",
-                    "description": "Access the data via HTTP.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Aqua_AIRS_Level3/AIRH3ST8.006/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_Level3/AIRH3ST8.006/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/opendap/Aqua_AIRS_Level3/AIRH3ST8.006/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRH3ST8+006",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=AIRH3ST8+006",
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
+            "graphic-preview-description": "Sample data of the \"AIRS/Aqua Level 3 multiday standard physical retrieval\".",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/AIRH3ST8_006.png",
+            "identifier": "C1238517250-GES_DISC",
+            "issued": "2002-09-01",
+            "keyword": [
+                "atmospheric water vapor",
+                "clouds",
+                "atmospheric radiation",
+                "earth science",
+                "land surface",
+                "atmospheric pressure",
+                "oceans",
+                "ocean temperature",
+                "surface radiative properties",
+                "atmospheric chemistry",
+                "atmosphere",
+                "altitude",
+                "surface thermal properties",
+                "air quality",
+                "atmospheric temperature"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aqua/AIRS/DATA311",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2003-02-08",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "AIRH3ST8",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-09-01T00:00:00Z/2003-02-08T23:59:59.999Z",
             "theme": [
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "AIRS/Aqua L3 8-day Standard Physical Retrieval (AIRS+AMSU+HSB) 1 degree x 1 degree V006 (AIRH3ST8) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/AQR50-3W3DS",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA Aquarius project. 2017-12-07. Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Descending Seasonal Data. Version 5.0. Aquarius Sea Surface Salinity Products. Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC OBPG. https://doi.org/10.5067/AQR50-3W3DS. http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius. NASA Aquarius project, NASA/GSFC OBPG, 2017-12-07, Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Descending Seasonal Data V5.0, http://podaac.jpl.nasa.gov/SeaSurfaceSalinity/Aquarius.",
-            "issued": "2017-10-21",
-            "temporal": "2011-08-25T02:41:02Z/2015-06-07T12:45:21Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-12-07",
-            "keyword": [
-                "oceans",
-                "ocean winds",
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
-            "identifier": "C2491757202-POCLOUD",
-            "description": "Aquarius Level 3 ocean surface wind speed standard mapped image data contains gridded 1 degree spatial resolution wind speed data averaged over daily, 7 day, monthly, and seasonal time scales. This particular data set is the\nSeasonal, Descending wind speed product for version 5.0 of the Aquarius data set, which is the official end of mission public data release from the AQUARIUS/SAC-D mission. Only retrieved values for Descending passes have been used to create this product.  The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
-            "release-place": "Goddard Space Flight Center, 8800 Greenbelt Rd.; Greeenbelt, MD., 20771, USA",
-            "series-name": "Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Descending Seasonal Data",
-            "graphic-preview-description": "Thumbnail",
             "creator": "NASA Aquarius project",
-            "title": "Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Descending Seasonal Data V5.0",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_WIND_SPEED_SMID_3MONTH_V5.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Aquarius Level 3 ocean surface wind speed standard mapped image data contains gridded 1 degree spatial resolution wind speed data averaged over daily, 7 day, monthly, and seasonal time scales. This particular data set is the\nSeasonal, Descending wind speed product for version 5.0 of the Aquarius data set, which is the official end of mission public data release from the AQUARIUS/SAC-D mission. Only retrieved values for Descending passes have been used to create this product.  The Aquarius instrument is onboard the AQUARIUS/SAC-D satellite, a collaborative effort between NASA and the Argentinian Space Agency Comision Nacional de Actividades Espaciales (CONAE). The instrument consists of three radiometers in push broom alignment at incidence angles of 29, 38, and 46 degrees incidence angles relative to the shadow side of the orbit.  Footprints for the beams are: 76 km (along-track) x 94 km (cross-track), 84 km x 120 km and 96km x 156 km, yielding a total cross-track swath of 370 km. The radiometers measure brightness temperature at 1.413 GHz in their respective horizontal and vertical polarizations (TH and TV). A scatterometer operating at 1.26 GHz measures ocean backscatter in each footprint that is used for surface roughness corrections in the estimation of salinity. The scatterometer has an approximate 390km swath.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3W3DS",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAQR50-3W3DS",
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_WIND_SPEED_SMID_3MONTH_V5.jpg",
-                    "description": "Thumbnail",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_WIND_SPEED_SMID_3MONTH_V5.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491757202-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C2491757202-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491757202-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C2491757202-POCLOUD",
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
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/AQUARIUS_L3_WIND_SPEED_SMID_3MONTH_V5.jpg",
+            "identifier": "C2491757202-POCLOUD",
+            "issued": "2017-10-21",
+            "keyword": [
+                "oceans",
+                "ocean winds",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/AQR50-3W3DS",
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
+            "series-name": "Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Descending Seasonal Data",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2011-08-25T02:41:02Z/2015-06-07T12:45:21Z",
             "theme": [
                 "AQUARIUS SAC-D",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aquarius Official Release Level 3 Wind Speed Standard Mapped Image Descending Seasonal Data V5.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LCROSS-E%2FL-NSP1-FL-3-CAL-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "Calibrated flash mode spectra from the Near Infrared Spectrometer 1 (NSP1) aboard the Lunar Crater Observation and Sensing Satellite (LCROSS).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lcross-e-l-nsp1-fl-3-cal-v1.0_2z8r-9zbd",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "lunar crater observation and sensing satellite",
                 "calibration",
                 "moon",
                 "earth"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=LCROSS-E%2FL-NSP1-FL-3-CAL-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.lcross-e-l-nsp1-fl-3-cal-v1.0_2z8r-9zbd",
-            "description": "Calibrated flash mode spectra from the Near Infrared Spectrometer 1 (NSP1) aboard the Lunar Crater Observation and Sensing Satellite (LCROSS).",
-            "title": "LCROSS EARTH/MOON 1ST NEAR IR SPECTROMETER FLASH 3 CAL V1.0",
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
+            "title": "LCROSS EARTH/MOON 1ST NEAR IR SPECTROMETER FLASH 3 CAL V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-ROSINA-4-PRL-V2.0",
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
+            "description": "This data set contains CODMAC level 4 science data acquired by the ROSINA COPS sensor between 2014-03-29 and 2014-11-18 during the Prelanding phase of the Rosetta mission to comet 67P/CG. V2.0: Minor species (CH4, NH3, HCN, H2CO, C2H6, CH3OH, H2S, C2H5OH, OCS, CS2) detected by DFMS were added.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rosina-4-prl-v2.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-ROSINA-4-PRL-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rosina-4-prl-v2.0",
-            "description": "This data set contains CODMAC level 4 science data acquired by the ROSINA COPS sensor between 2014-03-29 and 2014-11-18 during the Prelanding phase of the Rosetta mission to comet 67P/CG. V2.0: Minor species (CH4, NH3, HCN, H2CO, C2H6, CH3OH, H2S, C2H5OH, OCS, CS2) detected by DFMS were added.",
-            "title": "ROSETTA-ORBITER 67P ROSINA 4\n                                      PRL V2.0",
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
+            "title": "ROSETTA-ORBITER 67P ROSINA 4\n                                      PRL V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://turbmodels.larc.nasa.gov/rsm-stressomega.html",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://turbmodels.larc.nasa.gov/index.html"
-            ],
-            "keyword": [
-                "stress",
-                "wilcox",
-                "turbulence",
-                "models",
-                "reynolds"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Christopher Rumsey",
                 "hasEmail": "mailto:c.l.rumsey@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "NASA-839",
             "description": "This web page gives detailed information on the equations for various forms of the Stress-omega Full Reynolds Stress model.",
-            "title": "Stress-omega Full Reynolds Stress Model",
-            "programCode": [
-                "026:023"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -57389,58 +57367,91 @@
                     "mediaType": "application/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-839",
+            "issued": "2018-06-25",
+            "keyword": [
+                "stress",
+                "wilcox",
+                "turbulence",
+                "models",
+                "reynolds"
+            ],
+            "landingPage": "http://turbmodels.larc.nasa.gov/rsm-stressomega.html",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:023"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
+            "references": [
+                "http://turbmodels.larc.nasa.gov/index.html"
+            ],
             "theme": [
                 "Aerospace"
-            ]
+            ],
+            "title": "Stress-omega Full Reynolds Stress Model"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-CAL-ROMAP-2-CR4A-MAG-V1.0",
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
-                "calibration",
-                "international rosetta mission"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This archive contains level 2 data from the ROMAP-MAG instrument onboard ROSETTA Lander, acquired during the CR4A (cruise 4A) phase. It also contains documentation which describes the ROMAP experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-cal-romap-2-cr4a-mag-v1.0_2zdh-xqwm",
+            "issued": "2021-05-21",
+            "keyword": [
+                "calibration",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RL-CAL-ROMAP-2-CR4A-MAG-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.rl-cal-romap-2-cr4a-mag-v1.0_2zdh-xqwm",
-            "description": "This archive contains level 2 data from the ROMAP-MAG instrument onboard ROSETTA Lander, acquired during the CR4A (cruise 4A) phase. It also contains documentation which describes the ROMAP experiment. The data archived in this data set conform to the Planetary Data System (PDS) Standards, Version 3.6.",
-            "title": "ROSETTA-LANDER CAL ROMAP 2 CR4A MAG\n                            V1.0",
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
+            "title": "ROSETTA-LANDER CAL ROMAP 2 CR4A MAG\n                            V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/2zey-awys",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Kim Tolbert",
+                "hasEmail": "mailto:kim.tolbert@nasa.gov"
+            },
+            "description": "Time histories of NaI, GBO, and GOES data, with flare and day/night markers. Orbital plots are on RHESSI orbit times.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://hesperia.gsfc.nasa.gov/fermi/gbm/qlook/orbit_plots/",
+                    "mediaType": "image/png"
+                }
+            ],
+            "identifier": "NASA-0000245__2",
             "issued": "2018-06-25",
-            "temporal": "2008-08-12/2014-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "gbm",
                 "goes",
@@ -57450,151 +57461,115 @@
                 "gbo",
                 "telescope"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Kim Tolbert",
-                "hasEmail": "mailto:kim.tolbert@nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/2zey-awys",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:020"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000245__2",
-            "description": "Time histories of NaI, GBO, and GOES data, with flare and day/night markers. Orbital plots are on RHESSI orbit times.",
-            "title": "GBM Quicklook Daily and Orbital Plots",
-            "programCode": [
-                "026:020"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://hesperia.gsfc.nasa.gov/fermi/gbm/qlook/orbit_plots/",
-                    "mediaType": "image/png"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
+            "temporal": "2008-08-12/2014-01-01",
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "GBM Quicklook Daily and Orbital Plots"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-EXT3-67PCHURYUMOV-M33-V1.0",
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
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm acquired by the OSIRIS Wide Angle Camera during the ROSETTA EXTENSION 3 phase of the Rosetta mission, covering the period from 2016-08-09T23:25:00.000 to 2016-09-02T06:39:59.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-ext3-67pchuryumov-m33-v1.0_2zfe-srqf",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-EXT3-67PCHURYUMOV-M33-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-ext3-67pchuryumov-m33-v1.0_2zfe-srqf",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm acquired by the OSIRIS Wide Angle Camera during the ROSETTA EXTENSION 3 phase of the Rosetta mission, covering the period from 2016-08-09T23:25:00.000 to 2016-09-02T06:39:59.000.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 EXT3-MTP033 RDR V1.0",
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
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 EXT3-MTP033 RDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC3-67P-M19-INFLDSTR-V1.0",
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
+            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the COMET ESCORT 3 mission phase, covering the period  from 2015-07-28T23:25:00.000 to 2015-08-25T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc3-67p-m19-infldstr-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSIWAC-4-ESC3-67P-M19-INFLDSTR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osiwac-4-esc3-67p-m19-infldstr-v1.0",
-            "description": "This CODMAC level 4 data set contains solar stray-light corrected, in-field stray-light corrected,  radiometric calibrated and geometric distortion corrected  (resampled) image data in W/m^2/sr/nm,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the COMET ESCORT 3 mission phase, covering the period  from 2015-07-28T23:25:00.000 to 2015-08-25T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V1.0 is the first version of this dataset: Lien corrected dataset after September 2019 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC3-MTP019 RDR-INFLDSTR V1.0",
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
+            "title": "ROSETTA-ORBITER 67P OSIWAC 4 ESC3-MTP019 RDR-INFLDSTR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/RF3R3G9I3UVX",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Alex Turner & Daniel Jacob. 2016-09-30. CMS_CH4_FLX_NA. Version 1. CMS (Carbon Monitoring System) Methane (CH4) Flux for North America 0.5 degree x 0.667 degree V1. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/RF3R3G9I3UVX. https://disc.gsfc.nasa.gov/datacollection/CMS_CH4_FLX_NA_1.html.",
-            "issued": "2010-01-01",
-            "temporal": "2010-01-01T00:00:00Z/2012-01-01T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2012-01-01",
-            "references": [
-                "https://doi.org/10.5194/acp-15-7049-2015"
-            ],
-            "keyword": [
-                "atmospheric chemistry",
-                "atmosphere",
-                "earth science"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "THOMAS HEARTY",
                 "hasEmail": "mailto:Thomas.J.Hearty@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C1332706746-GES_DISC",
-            "description": "An error was found in this product; therefore, it has been deleted.  Please use the CMS Methane (CH4) Flux for North America Daily product (CMS_CH4_FLX_NAD) in its place.\n\nThe CMS Methane (CH4) Flux for North America data set contains estimates of methane emission in North America based on an inversion of the GEOS-Chem chemical  transport model constrained by Greenhouse Gases Observing SATellite (GOSAT) observations .  The nested approach of the inversion enables large point sources to be resolved while aggregating regions with weak emissions and minimizing aggregation errors.  The emission sources are separated into 9 different sectors as follows: Total, Wetlands, Livestock, Oil/Gas, Waste (Landfills wastewater), Coal, Rice, Open Fires, and Other.  More details about the algorithm and error characterization can be found in (Turner, Jacob, Wecht, et al. 2015).\n\nThe NASA Carbon Monitoring System (CMS) is designed to make significant contributions in characterizing, quantifying, understanding, and predicting the evolution of global carbon sources and sinks through improved monitoring of carbon stocks and fluxes. The System will use the full range of NASA satellite observations and modeling/analysis capabilities to establish the accuracy, quantitative uncertainties, and utility of products for supporting national and international policy, regulatory, and management activities. CMS will maintain a global emphasis while providing finer scale regional information, utilizing space-based and surface-based data and will rapidly initiate generation and distribution of products both for user evaluation and to inform near-term policy development and planning.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "CMS_CH4_FLX_NA",
             "creator": "Alex Turner & Daniel Jacob",
-            "title": "CMS (Carbon Monitoring System) Methane (CH4) Flux for North America 0.5 degree x 0.667 degree V1 (CMS_CH4_FLX_NA) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/CMS_CH4_FLX_NA_1.png",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "An error was found in this product; therefore, it has been deleted.  Please use the CMS Methane (CH4) Flux for North America Daily product (CMS_CH4_FLX_NAD) in its place.\n\nThe CMS Methane (CH4) Flux for North America data set contains estimates of methane emission in North America based on an inversion of the GEOS-Chem chemical  transport model constrained by Greenhouse Gases Observing SATellite (GOSAT) observations .  The nested approach of the inversion enables large point sources to be resolved while aggregating regions with weak emissions and minimizing aggregation errors.  The emission sources are separated into 9 different sectors as follows: Total, Wetlands, Livestock, Oil/Gas, Waste (Landfills wastewater), Coal, Rice, Open Fires, and Other.  More details about the algorithm and error characterization can be found in (Turner, Jacob, Wecht, et al. 2015).\n\nThe NASA Carbon Monitoring System (CMS) is designed to make significant contributions in characterizing, quantifying, understanding, and predicting the evolution of global carbon sources and sinks through improved monitoring of carbon stocks and fluxes. The System will use the full range of NASA satellite observations and modeling/analysis capabilities to establish the accuracy, quantitative uncertainties, and utility of products for supporting national and international policy, regulatory, and management activities. CMS will maintain a global emphasis while providing finer scale regional information, utilizing space-based and surface-based data and will rapidly initiate generation and distribution of products both for user evaluation and to inform near-term policy development and planning.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FRF3R3G9I3UVX",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FRF3R3G9I3UVX",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -57604,78 +57579,81 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/CMS_CH4_FLX_NA_1.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/CMS_CH4_FLX_NA_1.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/CMS/CMS_CH4_FLX_NA.1/doc/README.CMS_CH4_FLX_NA_V1.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gsfc.nasa.gov/data/CMS/CMS_CH4_FLX_NA.1/doc/README.CMS_CH4_FLX_NA_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://carbon.nasa.gov/",
-                    "description": "The NASA Carbon Monitoring System (CMS) page.",
                     "@type": "dcat:Distribution",
+                    "description": "The NASA Carbon Monitoring System (CMS) page.",
+                    "downloadURL": "https://carbon.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/CMS_CH4_FLX_NA_1.png",
+            "identifier": "C1332706746-GES_DISC",
+            "issued": "2010-01-01",
+            "keyword": [
+                "atmospheric chemistry",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/RF3R3G9I3UVX",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2012-01-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.5194/acp-15-7049-2015"
+            ],
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "CMS_CH4_FLX_NA",
             "spatial": "-140.0 10.0 -40.0 70.0",
+            "temporal": "2010-01-01T00:00:00Z/2012-01-01T23:59:59.999Z",
             "theme": [
                 "CMS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "CMS (Carbon Monitoring System) Methane (CH4) Flux for North America 0.5 degree x 0.667 degree V1 (CMS_CH4_FLX_NA) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/46J4Z696YA09",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "OCO-2 Science Team/Michael Gunson, AnnmarieEldering. 2019-10-31. OCO2_L2_CO2Prior. Version 10r. OCO-2 Level 2 CO2 prior based on CO2 monthly flask record, global meteorology, and age of air, Retrospective Processing V10r. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/46J4Z696YA09. https://disc.gsfc.nasa.gov/datacollection/OCO2_L2_CO2Prior_10r.html. Digital Science Data.",
-            "issued": "2019-10-20",
-            "temporal": "2014-09-06T00:00:00Z/2022-01-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-10-20",
-            "keyword": [
-                "atmospheric chemistry",
-                "atmosphere",
-                "earth science"
-            ],
-            "data-presentation-form": "Digital Science Data",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "THOMAS HEARTY",
                 "hasEmail": "mailto:Thomas.J.Hearty@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
-            "identifier": "C1685783897-GES_DISC",
-            "description": "Version 10r is the current version of the data set. Older versions will no longer be available and are superseded by Version 10r.\n\nIn early 2021, the OCO Team identified an issue with OCO-2 level 2 products processed since January 28, 2020. The Ancillary Geometric Product (AGAP) file, a static file used in OCO-2 Geolocation processing, was inadvertently replaced with an obsolete version. This AGAP file included a ~300 m pointing error. As a result, all OCO-2 Level 2, version 10r, data files for the period January 28 - December 31, 2020, were corrected and replaced. The replacement process was completed by the end of June, 2021. The significance of this error has been described in Kiel et al. (2019; doi:10.5194/amt-12-2241-2019).\n\nThe Orbiting Carbon Observatory is the first NASA mission designed to collect space-based measurements of atmospheric carbon dioxide with the precision, resolution, and coverage needed to characterize the processes controlling its buildup in the atmosphere. The OCO-2 project uses the LEOStar-2 spacecraft that carries a single instrument. It incorporates three high-resolution spectrometers that make coincident measurements of reflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and in molecular oxygen (O2) A-Band at 0.76 micrometers.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "OCO2_L2_CO2Prior",
             "creator": "OCO-2 Science Team/Michael Gunson, AnnmarieEldering",
-            "title": "OCO-2 Level 2 CO2 prior based on CO2 monthly flask record, global meteorology, and age of air, Retrospective Processing V10r (OCO2_L2_CO2Prior) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/OCO2_logo.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "Version 10r is the current version of the data set. Older versions will no longer be available and are superseded by Version 10r.\n\nIn early 2021, the OCO Team identified an issue with OCO-2 level 2 products processed since January 28, 2020. The Ancillary Geometric Product (AGAP) file, a static file used in OCO-2 Geolocation processing, was inadvertently replaced with an obsolete version. This AGAP file included a ~300 m pointing error. As a result, all OCO-2 Level 2, version 10r, data files for the period January 28 - December 31, 2020, were corrected and replaced. The replacement process was completed by the end of June, 2021. The significance of this error has been described in Kiel et al. (2019; doi:10.5194/amt-12-2241-2019).\n\nThe Orbiting Carbon Observatory is the first NASA mission designed to collect space-based measurements of atmospheric carbon dioxide with the precision, resolution, and coverage needed to characterize the processes controlling its buildup in the atmosphere. The OCO-2 project uses the LEOStar-2 spacecraft that carries a single instrument. It incorporates three high-resolution spectrometers that make coincident measurements of reflected sunlight in the near-infrared CO2 near 1.61 and 2.06 micrometers and in molecular oxygen (O2) A-Band at 0.76 micrometers.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F46J4Z696YA09",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F46J4Z696YA09",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -57685,59 +57663,59 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO2_L2_CO2Prior_10r.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OCO2_L2_CO2Prior_10r.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L2_CO2Prior.10r/",
-                    "description": "Access the data via HTTP",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTP",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/data/OCO2_DATA/OCO2_L2_CO2Prior.10r/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OCO2_L2_CO2Prior",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OCO2_L2_CO2Prior",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_L2_CO2Prior.10r/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://oco2.gesdisc.eosdis.nasa.gov/opendap/OCO2_L2_CO2Prior.10r/contents.html",
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/README.OCO2.pdf",
-                    "description": "README document",
                     "@type": "dcat:Distribution",
+                    "description": "README document",
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
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/SDOS_SIS_L2Fluorescence.V6.pdf",
-                    "description": "Software Interface Specification",
                     "@type": "dcat:Distribution",
+                    "description": "Software Interface Specification",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OCO/SDOS_SIS_L2Fluorescence.V6.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
@@ -57747,377 +57725,377 @@
                     "title": "View this dataset's algorithm theoretical basis document"
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
+            "identifier": "C1685783897-GES_DISC",
+            "issued": "2019-10-20",
+            "keyword": [
+                "atmospheric chemistry",
+                "atmosphere",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/46J4Z696YA09",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-10-20",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "OCO2_L2_CO2Prior",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2014-09-06T00:00:00Z/2022-01-17T00:00:00Z",
             "theme": [
                 "OCO-2",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OCO-2 Level 2 CO2 prior based on CO2 monthly flask record, global meteorology, and age of air, Retrospective Processing V10r (OCO2_L2_CO2Prior) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-LEISA-3-LAUNCH-V1.0",
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
-                "new horizons",
-                "calibration"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains Calibrated data taken by the New Horizons Linear Etalon Imaging Spectral Array instrument during the post-launch checkout mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-leisa-3-launch-v1.0_2zkt-9nyc",
+            "issued": "2021-05-21",
+            "keyword": [
+                "new horizons",
+                "calibration"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-X-LEISA-3-LAUNCH-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-x-leisa-3-launch-v1.0_2zkt-9nyc",
-            "description": "This data set contains Calibrated data taken by the New Horizons Linear Etalon Imaging Spectral Array instrument during the post-launch checkout mission phase.",
-            "title": "NEW HORIZONS LEISA POST-LAUNCH CHECKOUT V1.0",
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
+            "title": "NEW HORIZONS LEISA POST-LAUNCH CHECKOUT V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ESO1M-SR-APPH-4-OCC-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "TBD",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.eso1m-sr-apph-4-occ-v1.0_2znf-jvu2",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "saturn",
                 "s rings",
                 "saturn occultation of 28 sagittarius 1989"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ESO1M-SR-APPH-4-OCC-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.eso1m-sr-apph-4-occ-v1.0_2znf-jvu2",
-            "description": "TBD",
-            "title": "ESO1M SR AP-PHOTOMETER RESAMPLED RING OCCULTATION V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "ESO1M SR AP-PHOTOMETER RESAMPLED RING OCCULTATION V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-J-LECP-4-15MIN",
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
-                "voyager"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "THIS DATA SET CONSISTS OF RESAMPLED DATA FROM THE LOW ENERGY CHARGED PARTICLE (LECP) EXPERIMENT ON VOYAGER 1 WHILE THE SPACECRAFT WAS IN THE VICINITY OF JUPITER. THIS INSTRUMENT MEASURES THE INTENSITIES OF IN-SITU CHARGED PARTICLES (>26 KEV ELECTRONS AND >30 KEV IONS) WITH VARIOUS LEVELS OF DISCRIMINATION BASED ON ENERGY, MASS SPECIES, AND ANGULAR ARRIVAL DIRECTION. A SUBSET OF ALMOST 100 LECP CHANNELS ARE INCLUDED WITH THIS DATA SET. THE LECP DATA ARE GLOBALLY CALIBRATED TO THE EXTENT POSSIBLE (SEE BELOW) AND THEY ARE TIME AVERAGED TO ABOUT 15 MINUTE TIME INTERVALS WITH THE EXACT BEGINNING AND ENDING TIMES FOR THOSE INTERVALS MATCHING THE LECP INSTRUMENTAL CYCLE PERIODS (THE ANGULAR SCANNING PERIODS). THE LECP INSTUMENT HAS A ROTATING HEAD FOR OBTAINING ANGULAR ANISOTROPY MEASUREMENTS OF THE MEDIUM ENERGY CHARGED PARTICLES THAT IT MEASURES. THE CYCLE TIME FOR THE ROTATION IF VARIABLE, BUT DURING ENCOUNTERS IT IS ALWAYS FASTER THAN 15 MINUTES. THUS, THE FULL ANGULAR ANISOTROPY INFORMATION IS PRESERVED WITH THIS DATA. THE DATA IS IN THE FORM OF 'RATE' DATA WHICH HAS NOT BEEN CONVERTED TO THE USUAL PHYSICAL UNITS. THE REASON IS THAT SUCH A CONVERSION WOULD DEPEND ON UNCERTAIN DETERMINATIONS SUCH AS THE MASS SPECIES OF THE PARTICLES AND THE LEVEL OF BACKGROUND. BOTH MASS SPECIES AND BACKGROUND ARE GENERALLY DETERMINED FROM CONTEXT DURING THE STUDY OF PARTICULAR REGIONS. TO CONVERT 'RATE' TO 'INTENSITY' FOR A PARTICULAR CHANNEL ONE PERFORMS THE FOLLOWING TASKS: 1) DECIDE ON THE LEVEL OF BACKGROUND CONTAMINATION AND SUBTRACT THAT OFF THE GIVEN RATE LEVEL. BACKGROUND IS TO BE DETERMINED FROM CONTEXT AND FROM MAKING USE OF SECTOR 8 RATES (SECTOR 8 HAS A 2 mm AL SHIELD COVERING IT). 2) DIVIDE THE BACKGROUND CORRECTED RATE BY THE CHANNEL GEOMETRIC FACTOR AND BY THE ENERGY BANDPASS OF THE CHANNEL. THE GEOMETRIC FACTOR IS FOUND IN ENTRY 'channel_geometric_ factor' AS ASSOCIATED WITH EACH CHANNEL 'channel_id'. TO DETERMINE THE ENERGY BANDPASS, ONE MUST JUDGE THE MASS SPECIES OF THE OF THE DETECTED PARTICLES (FOR IONS BUT NOT FOR ELECTRONS). THE ENERGY BAND PASSES ARE GIVEN IN ENTRIES 'minimum_instrument_parameter' and 'maximum_instrument_ parameter' IN TABLE 'FPLECPENERGY', AND ARE GIVEN IN THE FORM 'ENERGY/NUCLEON'. FOR CHANNELS THAT BEGIN THEIR NAMES WITH THE DESIGNATIONS 'CH' THESE BANDPASSES CAN BE USED ON MASS SPECIES THAT ARE ACCEPTED INTO THAT CHANNEL (SEE ENTRIES 'minimum_instrument_parameter' and 'maximum_instrument_ parameter' IN TABLE 'FPLECPCHANZ', WHICH GIVE THE MINIMUM AND MAXIMUM 'Z' VALUE ACCEPTED -- THESE ENTRIES ARE BLANK FOR ELECTRON CHANNELS). FOR OTHER CHANNELS THE GIVEN BANDPASS REFERS ONLY TO THE LOWEST 'Z' VALUE ACCEPTED. THE BANDPASSES FOR OTHER 'Z' VALUES ARE NOT ALL KNOWN, BUT SOME ARE GIVEN IN THE LITERATURE (E.G. KRIMIGIS ET AL., 1979). THE FINAL PRODUCT OF THESE INSTRUCTIONS WILL BE THE PARTICLE INTENSITY WITH THE UNITS: COUNTS/(CM**2.STR.SEC.KEV). SOME CHANNELS ARE SUBJECT TO SERIOUS CONTAMINATIONS, AND MANY OF THESE CONTAMINATIONS CANNOT BE REMOVED EXCEPT WITH A REGION-BY-REGION ANALYSIS, WHICH HAS NOT BEEN DONE FOR THIS DATA. THUS, TO USE THIS DATA IT IS ABSOLUTELY VITAL THAT THE CONTAMINATION TYPES ('contamination_id' , 'contamination_desc') AND THE LEVELS OF CONTAMINATION ('data_quality_id' CORRESPONDING TO THE DEFINITIONS 'data_quality_desc') BE CAREFULLY EXAMINED FOR ALL REGIONS OF STUDY. A DEAD TIME CORRECTION PROCEDURE HAS BEEN APPLIED IN AN ATTEMPT TO CORRECT THE LINEAR EFFECTS OF DETECTOR OVERDRIVE (PULSE-PILEUP). THIS PROCEDURE DOES NOT FIX SEVERELY OVERDRIVEN DETECTORS. A PROCEDURE IS AVAILABLE FOR CORRECTING VOYAGER 2 LECP ELECTRON CONTAMINATION OF LOW ENERGY ION CHANNELS, BUT ITS EFFECTIVENESS HAS BEEN EVALUATED ONLY FOR THE URANUS DATA SET. THUS, CORRECTIONS HAVE BEEN APPLIED ONLY TO THE URANUS DATA SET. Also included with this data are one standard deviation statistical uncertainties for the directional data (sectors 1 through 8) expressed as a percent. Unknown values are generally coded as s",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-j-lecp-4-15min_2zni-v6sa",
+            "issued": "2021-05-21",
+            "keyword": [
+                "jupiter",
+                "voyager"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-J-LECP-4-15MIN",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-j-lecp-4-15min_2zni-v6sa",
-            "description": "THIS DATA SET CONSISTS OF RESAMPLED DATA FROM THE LOW ENERGY CHARGED PARTICLE (LECP) EXPERIMENT ON VOYAGER 1 WHILE THE SPACECRAFT WAS IN THE VICINITY OF JUPITER. THIS INSTRUMENT MEASURES THE INTENSITIES OF IN-SITU CHARGED PARTICLES (>26 KEV ELECTRONS AND >30 KEV IONS) WITH VARIOUS LEVELS OF DISCRIMINATION BASED ON ENERGY, MASS SPECIES, AND ANGULAR ARRIVAL DIRECTION. A SUBSET OF ALMOST 100 LECP CHANNELS ARE INCLUDED WITH THIS DATA SET. THE LECP DATA ARE GLOBALLY CALIBRATED TO THE EXTENT POSSIBLE (SEE BELOW) AND THEY ARE TIME AVERAGED TO ABOUT 15 MINUTE TIME INTERVALS WITH THE EXACT BEGINNING AND ENDING TIMES FOR THOSE INTERVALS MATCHING THE LECP INSTRUMENTAL CYCLE PERIODS (THE ANGULAR SCANNING PERIODS). THE LECP INSTUMENT HAS A ROTATING HEAD FOR OBTAINING ANGULAR ANISOTROPY MEASUREMENTS OF THE MEDIUM ENERGY CHARGED PARTICLES THAT IT MEASURES. THE CYCLE TIME FOR THE ROTATION IF VARIABLE, BUT DURING ENCOUNTERS IT IS ALWAYS FASTER THAN 15 MINUTES. THUS, THE FULL ANGULAR ANISOTROPY INFORMATION IS PRESERVED WITH THIS DATA. THE DATA IS IN THE FORM OF 'RATE' DATA WHICH HAS NOT BEEN CONVERTED TO THE USUAL PHYSICAL UNITS. THE REASON IS THAT SUCH A CONVERSION WOULD DEPEND ON UNCERTAIN DETERMINATIONS SUCH AS THE MASS SPECIES OF THE PARTICLES AND THE LEVEL OF BACKGROUND. BOTH MASS SPECIES AND BACKGROUND ARE GENERALLY DETERMINED FROM CONTEXT DURING THE STUDY OF PARTICULAR REGIONS. TO CONVERT 'RATE' TO 'INTENSITY' FOR A PARTICULAR CHANNEL ONE PERFORMS THE FOLLOWING TASKS: 1) DECIDE ON THE LEVEL OF BACKGROUND CONTAMINATION AND SUBTRACT THAT OFF THE GIVEN RATE LEVEL. BACKGROUND IS TO BE DETERMINED FROM CONTEXT AND FROM MAKING USE OF SECTOR 8 RATES (SECTOR 8 HAS A 2 mm AL SHIELD COVERING IT). 2) DIVIDE THE BACKGROUND CORRECTED RATE BY THE CHANNEL GEOMETRIC FACTOR AND BY THE ENERGY BANDPASS OF THE CHANNEL. THE GEOMETRIC FACTOR IS FOUND IN ENTRY 'channel_geometric_ factor' AS ASSOCIATED WITH EACH CHANNEL 'channel_id'. TO DETERMINE THE ENERGY BANDPASS, ONE MUST JUDGE THE MASS SPECIES OF THE OF THE DETECTED PARTICLES (FOR IONS BUT NOT FOR ELECTRONS). THE ENERGY BAND PASSES ARE GIVEN IN ENTRIES 'minimum_instrument_parameter' and 'maximum_instrument_ parameter' IN TABLE 'FPLECPENERGY', AND ARE GIVEN IN THE FORM 'ENERGY/NUCLEON'. FOR CHANNELS THAT BEGIN THEIR NAMES WITH THE DESIGNATIONS 'CH' THESE BANDPASSES CAN BE USED ON MASS SPECIES THAT ARE ACCEPTED INTO THAT CHANNEL (SEE ENTRIES 'minimum_instrument_parameter' and 'maximum_instrument_ parameter' IN TABLE 'FPLECPCHANZ', WHICH GIVE THE MINIMUM AND MAXIMUM 'Z' VALUE ACCEPTED -- THESE ENTRIES ARE BLANK FOR ELECTRON CHANNELS). FOR OTHER CHANNELS THE GIVEN BANDPASS REFERS ONLY TO THE LOWEST 'Z' VALUE ACCEPTED. THE BANDPASSES FOR OTHER 'Z' VALUES ARE NOT ALL KNOWN, BUT SOME ARE GIVEN IN THE LITERATURE (E.G. KRIMIGIS ET AL., 1979). THE FINAL PRODUCT OF THESE INSTRUCTIONS WILL BE THE PARTICLE INTENSITY WITH THE UNITS: COUNTS/(CM**2.STR.SEC.KEV). SOME CHANNELS ARE SUBJECT TO SERIOUS CONTAMINATIONS, AND MANY OF THESE CONTAMINATIONS CANNOT BE REMOVED EXCEPT WITH A REGION-BY-REGION ANALYSIS, WHICH HAS NOT BEEN DONE FOR THIS DATA. THUS, TO USE THIS DATA IT IS ABSOLUTELY VITAL THAT THE CONTAMINATION TYPES ('contamination_id' , 'contamination_desc') AND THE LEVELS OF CONTAMINATION ('data_quality_id' CORRESPONDING TO THE DEFINITIONS 'data_quality_desc') BE CAREFULLY EXAMINED FOR ALL REGIONS OF STUDY. A DEAD TIME CORRECTION PROCEDURE HAS BEEN APPLIED IN AN ATTEMPT TO CORRECT THE LINEAR EFFECTS OF DETECTOR OVERDRIVE (PULSE-PILEUP). THIS PROCEDURE DOES NOT FIX SEVERELY OVERDRIVEN DETECTORS. A PROCEDURE IS AVAILABLE FOR CORRECTING VOYAGER 2 LECP ELECTRON CONTAMINATION OF LOW ENERGY ION CHANNELS, BUT ITS EFFECTIVENESS HAS BEEN EVALUATED ONLY FOR THE URANUS DATA SET. THUS, CORRECTIONS HAVE BEEN APPLIED ONLY TO THE URANUS DATA SET. Also included with this data are one standard deviation statistical uncertainties for the directional data (sectors 1 through 8) expressed as a percent. Unknown values are generally coded as s",
-            "title": "VOYAGER 1 JUP LOW ENERGY CHARGED PARTICLE CALIB. 15MIN",
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
+            "title": "VOYAGER 1 JUP LOW ENERGY CHARGED PARTICLE CALIB. 15MIN"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VL1%2FVL2-M-MET-4-BINNED-P-T-V-V1.0",
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
-                "mars",
-                "viking"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains binned and splined data obtained from the Viking Meteorology Instrument System (VMIS) through most of the Viking Lander 2 mission and the early days of the Lander 1 mission. The data set consists of mean values of pressure, temperature, and wind speed (zonal, meridional, and combined) and relevant statistics and warning flags calculated for 25 bins of equal duration per day. The effect of Lander interference on the temperature measurements is also estimated. The data are presented on a bin by bin basis for Lander 1 sol (Mars solar day after landing) 1-45 and for Lander 2 sol 1-1050 (with the only major gap occurring between sol 561 and 625). Failure of the quadrant sensor on Lander 1 sol 45 (see HESS_ETAL_1977) precludes unambiguous determination of wind direction without modification to the analysis techniques and software used to generate this data set (see HESS_ETAL_1977) therefore, this data set does not include Lander 1 measurements made after sol 45. A data set which has recovered a period of measurements made between Lander 1 sol 1 and 350 is available refer to PDS data set id VL1-M-MET-4-BINNED-P-T-V-CORR-V1.0.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vl1-vl2-m-met-4-binned-p-t-v-v1.0_2zpx-ehu7",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars",
+                "viking"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VL1%2FVL2-M-MET-4-BINNED-P-T-V-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vl1-vl2-m-met-4-binned-p-t-v-v1.0_2zpx-ehu7",
-            "description": "This data set contains binned and splined data obtained from the Viking Meteorology Instrument System (VMIS) through most of the Viking Lander 2 mission and the early days of the Lander 1 mission. The data set consists of mean values of pressure, temperature, and wind speed (zonal, meridional, and combined) and relevant statistics and warning flags calculated for 25 bins of equal duration per day. The effect of Lander interference on the temperature measurements is also estimated. The data are presented on a bin by bin basis for Lander 1 sol (Mars solar day after landing) 1-45 and for Lander 2 sol 1-1050 (with the only major gap occurring between sol 561 and 625). Failure of the quadrant sensor on Lander 1 sol 45 (see HESS_ETAL_1977) precludes unambiguous determination of wind direction without modification to the analysis techniques and software used to generate this data set (see HESS_ETAL_1977) therefore, this data set does not include Lander 1 measurements made after sol 45. A data set which has recovered a period of measurements made between Lander 1 sol 1 and 350 is available refer to PDS data set id VL1-M-MET-4-BINNED-P-T-V-CORR-V1.0.",
-            "title": "VL1/VL2 MARS METEOROLOGY RESAMPLED DATA BINNED-P-T-V V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VL1/VL2 MARS METEOROLOGY RESAMPLED DATA BINNED-P-T-V V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://doi.org/10.5067/LYHA9088MFWQ",
             "citation": "Li, B., H. Beaudoing, and M. Rodell,  NASA/GSFC/HSL. 2018-02-01. GLDAS_CLSM025_D. Version 2.0. GLDAS Catchment Land Surface Model L4 daily 0.25 x 0.25 degree V2.0. Greenbelt, Maryland, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/LYHA9088MFWQ. https://disc.gsfc.nasa.gov/datacollection/GLDAS_CLSM025_D_2.0.html. Digital Science Data.",
-            "issued": "2017-12-01",
-            "temporal": "1948-01-01T00:00:00Z/2014-12-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-12-01",
-            "references": [
-                "https://doi.org/10.1038/s41598-019-47219-z"
-            ],
-            "keyword": [
-                "atmospheric water vapor",
-                "atmospheric winds",
-                "earth science",
-                "land surface",
-                "precipitation",
-                "snow/ice",
-                "soils",
-                "terrestrial hydrosphere",
-                "atmosphere",
-                "surface water",
-                "atmospheric pressure",
-                "atmospheric radiation",
-                "atmospheric temperature",
-                "surface thermal properties"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "HUALAN RUI",
                 "hasEmail": "mailto:Hualan.Rui@nasa.gov"
             },
+            "creator": "Li, B., H. Beaudoing, and M. Rodell,  NASA/GSFC/HSL",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1453188197-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "NASA Global Land Data Assimilation System Version 2 (GLDAS-2) has three components: GLDAS-2.0, GLDAS-2.1, and GLDAS-2.2. GLDAS-2.0 is forced entirely with the Princeton meteorological forcing input data and provides a temporally consistent series from 1948 through 2014. GLDAS-2.1 is forced with a combination of model and observation data from 2000 to present. GLDAS-2.2 product suites use data assimilation (DA), whereas the GLDAS-2.0 and GLDAS-2.1 products are \"open-loop\" (i.e., no data assimilation). The choice of forcing data, as well as DA observation source, variable, and scheme, vary for different GLDAS-2.2 products.\n\nThis data set, GLDAS-2.0 0.25 degree daily, contains a series of land surface parameters simulated from the Catchment Land Surface Model 3.6, and currently covers from January 1948 to December 2014.\n\nThe GLDAS-2.0 model simulations were initialized on January 1, 1948, using soil moisture and other state fields from the LSM climatology for that day of the year. The simulations were forced by the global meteorological forcing data set from Princeton University (Sheffield et al., 2006). Each simulation uses the common GLDAS data sets for land water mask (MOD44W: Carroll et al., 2009) and elevation (GTOPO30) along with the model default land cover and soils datasets. Catchment model uses the Mosaic land cover classification and soils, topographic, and other model-specific parameters were derived in a consistent manner as in the NASA/GMAO&#8217;s GEOS-5 climate modeling system. The MODIS based land surface parameters are used in the current GLDAS-2.0 and GLDAS-2.1 products. \n\nThe GLDAS-2.0 data are archived and distributed in netCDF format.",
-            "release-place": "Greenbelt, Maryland, USA",
-            "series-name": "GLDAS_CLSM025_D",
-            "creator": "Li, B., H. Beaudoing, and M. Rodell,  NASA/GSFC/HSL",
-            "graphic-preview-description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
-            "title": "GLDAS Catchment Land Surface Model L4 daily 0.25 x 0.25 degree V2.0 (GLDAS_CLSM025_D) at GES DISC",
-            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=GLDAS_CLSM025_D_2_0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FLYHA9088MFWQ",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FLYHA9088MFWQ",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GLDAS_CLSM025_D_2.0.png",
-                    "description": "GLDAS-2.0 Catchment daily 0.25 degree root zone soil moisture content [kg m-2] for Jan. 01, 1948.",
                     "@type": "dcat:Distribution",
+                    "description": "GLDAS-2.0 Catchment daily 0.25 degree root zone soil moisture content [kg m-2] for Jan. 01, 1948.",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/GLDAS_CLSM025_D_2.0.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GLDAS_CLSM025_D_2.0.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/GLDAS_CLSM025_D_2.0.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/GLDAS/GLDAS_CLSM025_D.2.0/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/GLDAS/GLDAS_CLSM025_D.2.0/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GLDAS_CLSM025_D_2.0",
-                    "description": "Use the Earthdata Search Client (EDSC) to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client (EDSC) to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=GLDAS_CLSM025_D_2.0",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=GLDAS_CLSM025_D_2_0",
-                    "description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
                     "@type": "dcat:Distribution",
+                    "description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
+                    "downloadURL": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=GLDAS_CLSM025_D_2_0",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization through GIOVANNI"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/opendap/hyrax/GLDAS/GLDAS_CLSM025_D.2.0/",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/opendap/hyrax/GLDAS/GLDAS_CLSM025_D.2.0/",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/dods/GLDAS_CLSM025_D.2.0/",
-                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
                     "@type": "dcat:Distribution",
+                    "description": "The GrADS Data Server (GDS) is another form of OPeNDAP that provides subsetting and some analysis services across the Internet.",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/dods/GLDAS_CLSM025_D.2.0/",
+                    "mediaType": "text/html",
                     "title": "Use GRADS DATA SERVER (GDS) to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/GLDAS/GLDAS_CLSM025_D.2.0/doc/README_GLDAS2.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/data/GLDAS/GLDAS_CLSM025_D.2.0/doc/README_GLDAS2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ldas.gsfc.nasa.gov/gldas/",
-                    "description": "GLDAS Project Web Site",
                     "@type": "dcat:Distribution",
+                    "description": "GLDAS Project Web Site",
+                    "downloadURL": "https://ldas.gsfc.nasa.gov/gldas/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/information/howto?tags=hydrology",
-                    "description": "How to read and plot the data.",
                     "@type": "dcat:Distribution",
+                    "description": "How to read and plot the data.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/information/howto?tags=hydrology",
+                    "mediaType": "text/html",
                     "title": "View this dataset's how-to documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/information/documents?title=Hydrology+Documentation",
-                    "description": "GES DISC Hydrology Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "GES DISC Hydrology Documentation",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/information/documents?title=Hydrology+Documentation",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/thredds/catalog/GLDAS_aggregation/GLDAS_CLSM025_D.2.0/catalog.html",
-                    "description": "Time aggregated THREDDS Data Server (TDS)",
                     "@type": "dcat:Distribution",
+                    "description": "Time aggregated THREDDS Data Server (TDS)",
+                    "downloadURL": "https://hydro1.gesdisc.eosdis.nasa.gov/thredds/catalog/GLDAS_aggregation/GLDAS_CLSM025_D.2.0/catalog.html",
+                    "mediaType": "text/html",
                     "title": "Use THREDDS DATA to download the dataset's data"
                 }
             ],
+            "graphic-preview-description": "The GES-DISC Interactive Online Visualization ANd aNalysis Interface (Giovanni) is a web-based tool that allows users to interactively visualize and analyze data.",
+            "graphic-preview-file": "https://giovanni.gsfc.nasa.gov/giovanni/#dataKeyword=GLDAS_CLSM025_D_2_0",
+            "identifier": "C1453188197-GES_DISC",
+            "issued": "2017-12-01",
+            "keyword": [
+                "atmospheric water vapor",
+                "atmospheric winds",
+                "earth science",
+                "land surface",
+                "precipitation",
+                "snow/ice",
+                "soils",
+                "terrestrial hydrosphere",
+                "atmosphere",
+                "surface water",
+                "atmospheric pressure",
+                "atmospheric radiation",
+                "atmospheric temperature",
+                "surface thermal properties"
+            ],
+            "landingPage": "https://doi.org/10.5067/LYHA9088MFWQ",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-12-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "references": [
+                "https://doi.org/10.1038/s41598-019-47219-z"
+            ],
+            "release-place": "Greenbelt, Maryland, USA",
+            "series-name": "GLDAS_CLSM025_D",
             "spatial": "-180.0 -60.0 180.0 90.0",
+            "temporal": "1948-01-01T00:00:00Z/2014-12-30T23:59:59.999Z",
             "theme": [
                 "GLDAS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GLDAS Catchment Land Surface Model L4 daily 0.25 x 0.25 degree V2.0 (GLDAS_CLSM025_D) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://nasa3d.arc.nasa.gov/detail/eoss-aquarius",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://www.nasa.gov/mission_pages/aquarius/main/index.html"
-            ],
-            "keyword": [
-                "aquarius",
-                "eyes on the solar system",
-                "satellite",
-                "spacecraft",
-                "3d model"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Brian Kumanchik",
                 "hasEmail": "mailto:brian.kumanchik@jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "NASA-312",
             "description": "Polygons: 6012 Vertices: 8418",
-            "title": "NASA 3D Models: Aquarius",
-            "programCode": [
-                "026:007"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -58125,91 +58103,90 @@
                     "mediaType": "application/blender"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-312",
+            "issued": "2018-06-25",
+            "keyword": [
+                "aquarius",
+                "eyes on the solar system",
+                "satellite",
+                "spacecraft",
+                "3d model"
+            ],
+            "landingPage": "http://nasa3d.arc.nasa.gov/detail/eoss-aquarius",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:007"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
+            "references": [
+                "http://www.nasa.gov/mission_pages/aquarius/main/index.html"
+            ],
             "theme": [
                 "Space Science"
-            ]
+            ],
+            "title": "NASA 3D Models: Aquarius"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-SWAP-3-JUPITER-V2.0",
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
-                "solar wind",
-                "new horizons"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains Calibrated data taken by the New Horizons Solar Wind Around Pluto instrument during the Jupiter encounter mission phase.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-swap-3-jupiter-v2.0_2zre-zuwu",
+            "issued": "2021-05-21",
+            "keyword": [
+                "solar wind",
+                "new horizons"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=NH-J-SWAP-3-JUPITER-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.nh-j-swap-3-jupiter-v2.0_2zre-zuwu",
-            "description": "This data set contains Calibrated data taken by the New Horizons Solar Wind Around Pluto instrument during the Jupiter encounter mission phase.",
-            "title": "NEW HORIZONS SWAP JUPITER ENCOUNTER V2.0",
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
+            "title": "NEW HORIZONS SWAP JUPITER ENCOUNTER V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/Aura/OMI/DATA2434",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Joanna Joiner. 2023-06-01. OMUFPMET. Version 004. GEOS-5 FP-IT 3D Time-Averaged Model-Layer Assimilated Data Geo-Colocated to OMI/Aura UV2 1-Orbit L2 Swath 13x24km V4. NASA Goddard Space Flight Center. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://doi.org/10.5067/Aura/OMI/DATA2434. https://disc.gsfc.nasa.gov/datacollection/OMUFPMET_004.html. Digital Science Data. https://aura.gsfc.nasa.gov/.",
-            "issued": "2023-03-31",
-            "temporal": "2004-10-01T00:00:00Z/2023-06-12T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-03-31",
-            "keyword": [
-                "atmospheric temperature",
-                "earth science",
-                "atmosphere",
-                "atmospheric pressure"
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
-            "identifier": "C2556146042-GES_DISC",
-            "description": "The GEOS-5 FP-IT 3D Time-Averaged Model-Layer Assimilated Data Geo-Colocated to OMI/Aura UV2 1-Orbit L2 Swath 13x24km (OMUFPMET) product provides selected meteorlogical fields from the GEOS-5 Forward Processing for Instrument Teams (FP-IT) assimilated product produced by the Global Modeling and Assimilation Office (GMAO) co-located in space and time with the OMI UV-2 swath.\n\nThe fields in this product include layer pressure thickness, surface pressure, vertical temperature profiles, surface potential, and mid-layer pressure along with geolocation info. The OMI team also provides a corresponding product for the OMI VIS swath, OMVFPMET. The OMI ancillary products were developed to provide supplementary information for use with the OMI collection 4 L1B data sets. The original GEOS-5 FP-IT data are reported on a 0.625 deg longitude by 0.5 deg latitude grid, whereas the OMI UV-2 spatial resolution is 13km x 24km at nadir.\n\nThe OMUFPMET files are in netCDF4 format which is compatible with most netCDF and HDF5 readers and tools.  Each file is approximately 45mb in size. The lead for this product is Zachary Fasnacht of SSAI. Joanna Joiner is the responsible NASA official.",
-            "release-place": "NASA Goddard Space Flight Center",
-            "series-name": "OMUFPMET",
             "creator": "Joanna Joiner",
-            "title": "GEOS-5 FP-IT 3D Time-Averaged Model-Layer Assimilated Data Geo-Colocated to OMI/Aura UV2 1-Orbit L2 Swath 13x24km V4 (OMUFPMET) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMUFPMET_004.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The GEOS-5 FP-IT 3D Time-Averaged Model-Layer Assimilated Data Geo-Colocated to OMI/Aura UV2 1-Orbit L2 Swath 13x24km (OMUFPMET) product provides selected meteorlogical fields from the GEOS-5 Forward Processing for Instrument Teams (FP-IT) assimilated product produced by the Global Modeling and Assimilation Office (GMAO) co-located in space and time with the OMI UV-2 swath.\n\nThe fields in this product include layer pressure thickness, surface pressure, vertical temperature profiles, surface potential, and mid-layer pressure along with geolocation info. The OMI team also provides a corresponding product for the OMI VIS swath, OMVFPMET. The OMI ancillary products were developed to provide supplementary information for use with the OMI collection 4 L1B data sets. The original GEOS-5 FP-IT data are reported on a 0.625 deg longitude by 0.5 deg latitude grid, whereas the OMI UV-2 spatial resolution is 13km x 24km at nadir.\n\nThe OMUFPMET files are in netCDF4 format which is compatible with most netCDF and HDF5 readers and tools.  Each file is approximately 45mb in size. The lead for this product is Zachary Fasnacht of SSAI. Joanna Joiner is the responsible NASA official.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FOMI%2FDATA2434",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FAura%2FOMI%2FDATA2434",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
@@ -58219,118 +58196,120 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OMUFPMET_004.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/OMUFPMET_004.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Ancillary/OMUFPMET.004/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Ancillary/OMUFPMET.004/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OMUFPMET_004",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=OMUFPMET_004",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/opendap/Aura_OMI_Ancillary/OMUFPMET.004/contents.html",
-                    "description": "Access the data via the OPeNDAP protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via the OPeNDAP protocol.",
+                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/opendap/Aura_OMI_Ancillary/OMUFPMET.004/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OMI/AURA-OMI-KNMI-L01B-0005-SD-iods-v024148-20210702.pdf",
-                    "description": "OMI v4 L01B Algorithm Theoretical Basis Documents",
                     "@type": "dcat:Distribution",
+                    "description": "OMI v4 L01B Algorithm Theoretical Basis Documents",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OMI/AURA-OMI-KNMI-L01B-0005-SD-iods-v024148-20210702.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level2/OMUFPMET.004/doc/OMxFPMET_README.pdf",
-                    "description": "Product README",
                     "@type": "dcat:Distribution",
+                    "description": "Product README",
+                    "downloadURL": "https://aura.gesdisc.eosdis.nasa.gov/data/Aura_OMI_Level2/OMUFPMET.004/doc/OMxFPMET_README.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OMI/OMUFPMET.fs",
-                    "description": "File Specification Document",
                     "@type": "dcat:Distribution",
+                    "description": "File Specification Document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/OMI/OMUFPMET.fs",
+                    "mediaType": "text/html",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://aura.gsfc.nasa.gov/",
-                    "description": "Aura Project Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "Aura Project Home Page",
+                    "downloadURL": "https://aura.gsfc.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.knmiprojects.nl/projects/ozone-monitoring-instrument",
-                    "description": "OMI KNMI Home Page",
                     "@type": "dcat:Distribution",
+                    "description": "OMI KNMI Home Page",
+                    "downloadURL": "https://www.knmiprojects.nl/projects/ozone-monitoring-instrument",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://projects.knmi.nl/omi/research/documents/",
-                    "description": "List of Publications",
                     "@type": "dcat:Distribution",
+                    "description": "List of Publications",
+                    "downloadURL": "http://projects.knmi.nl/omi/research/documents/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's publications"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/OMUFPMET_004.png",
+            "identifier": "C2556146042-GES_DISC",
+            "issued": "2023-03-31",
+            "keyword": [
+                "atmospheric temperature",
+                "earth science",
+                "atmosphere",
+                "atmospheric pressure"
+            ],
+            "landingPage": "https://doi.org/10.5067/Aura/OMI/DATA2434",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-03-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "NASA Goddard Space Flight Center",
+            "series-name": "OMUFPMET",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2004-10-01T00:00:00Z/2023-06-12T00:00:00Z",
             "theme": [
                 "Aura",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "GEOS-5 FP-IT 3D Time-Averaged Model-Layer Assimilated Data Geo-Colocated to OMI/Aura UV2 1-Orbit L2 Swath 13x24km V4 (OMUFPMET) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://appel.nasa.gov/archives/past-issues/",
+            "accrualPeriodicity": "R/P3M",
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
-                "sharing",
-                "appel",
-                "ask magazine",
-                "knowledge"
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
-            "identifier": "NASA-860__6",
             "description": "Academy of Program/Project & Engineering Leadership's ASK Magazine archive.",
-            "title": "Academy of Program/Project & Engineering Leadership ASK Magazine Past Issues",
-            "programCode": [
-                "026:045"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -58338,885 +58317,915 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/P3M",
+            "identifier": "NASA-860__6",
+            "issued": "2018-06-25",
+            "keyword": [
+                "sharing",
+                "appel",
+                "ask magazine",
+                "knowledge"
+            ],
+            "landingPage": "http://appel.nasa.gov/archives/past-issues/",
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
+            "title": "Academy of Program/Project & Engineering Leadership ASK Magazine Past Issues"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VEGA1-C-MISCHA-3-RDR-HALLEY-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "On MARCH 6, 1986, AT 7:20:06 UT, the Vega spacecraft passed the nucleus of comet Halley at a distance of 8,890 km with a relative velocity of 78 km/s. The magnetic field experiments MISCHA carried four fluxgate sensors, with three sensors mounted on a boom at the end of the solar panels and the fourth sensor mounted one meter closer. During the cruise phase, the TRASSA-1 mode of the instrument (1 vector/2.5 min) was used. The sensors were switched to the TRASSA-2 mode (1 vector/min) during the flyby which started roughly two days before the encounter. From 3 h before closest approach (CA) until 1 hour after CA, the HS-mode (1 vector/6s) and the DT-mode (1 vector/100ms) was used [DELVAETAL1991].",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vega1-c-mischa-3-rdr-halley-v1.0_2ztj-z4jt",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "1p/halley 1 (1682 q1)",
                 "halley",
                 "vega 1"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VEGA1-C-MISCHA-3-RDR-HALLEY-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vega1-c-mischa-3-rdr-halley-v1.0_2ztj-z4jt",
-            "description": "On MARCH 6, 1986, AT 7:20:06 UT, the Vega spacecraft passed the nucleus of comet Halley at a distance of 8,890 km with a relative velocity of 78 km/s. The magnetic field experiments MISCHA carried four fluxgate sensors, with three sensors mounted on a boom at the end of the solar panels and the fourth sensor mounted one meter closer. During the cruise phase, the TRASSA-1 mode of the instrument (1 vector/2.5 min) was used. The sensors were switched to the TRASSA-2 mode (1 vector/min) during the flyby which started roughly two days before the encounter. From 3 h before closest approach (CA) until 1 hour after CA, the HS-mode (1 vector/6s) and the DT-mode (1 vector/100ms) was used [DELVAETAL1991].",
-            "title": "VEGA1 HALLEY FLYBY MAGNETOMETER DATA",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "VEGA1 HALLEY FLYBY MAGNETOMETER DATA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1759",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Bakian-Dogaheh, K., R.H. Chen, M. Moghaddam, Y. Yi, and A. Tabatabaeenejad. 2020. ABoVE: Active Layer Soil Characterization of Permafrost Sites, Northern Alaska, 2018. ORNL DAAC, Oak Ridge, Tennessee, USA. https://doi.org/10.3334/ORNLDAAC/1759",
-            "issued": "2024-05-01",
-            "temporal": "2018-08-22T00:00:00Z/2018-08-26T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-02",
-            "keyword": [
-                "earth science",
-                "frozen ground",
-                "soils",
-                "land surface"
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
-            "identifier": "C2143402217-ORNL_CLOUD",
             "description": "This dataset provides in situ soil measurements including soil dielectric properties, temperature, and moisture profiles, active layer thickness (ALT), and measurements of soil organic matter, bulk density, porosity, texture, and coarse root biomass. Samples were collected from the surface to permafrost table in soil pits at selected sites along the Dalton Highway in Northern Alaska. From North to South, the study sites include Franklin Bluffs, Sagwon, Happy Valley, Ice Cut, and Imnavait Creek. Measurements were made from August 22 to August 26, 2018. The purpose of the field campaign was to characterize the dielectric properties of permafrost active layer soils in support of the NASA Arctic and Boreal Vulnerability Experiment (ABoVE) Airborne Campaign.",
-            "graphic-preview-description": "Site sampling plan used for characterizing active layer soils (left). Axes are in meters. At Imnavait Creek, active layer thickness (ALT) was measured on transects intersecting a central soil pit. Soil dielectric properties, in situ moisture and temperature profiles were measured, and soil samples were collected for analyses from the soil pit (right).",
-            "title": "ABoVE: Active Layer Soil Characterization of Permafrost Sites, Northern Alaska, 2018",
-            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Permafrost_ActiveLayer_NSlope_Fig1.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1759",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1759",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/above/Permafrost_ActiveLayer_NSlope/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/above/Permafrost_ActiveLayer_NSlope/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Permafrost_ActiveLayer_NSlope.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Permafrost_ActiveLayer_NSlope.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1759",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1759",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Permafrost_ActiveLayer_NSlope/comp/20425_PROCHECK_Manual_Web.pdf",
-                    "description": "ABoVE: Active Layer Soil Characterization of Permafrost Sites, Northern Alaska, 2018: 20425_PROCHECK_Manual_Web.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Active Layer Soil Characterization of Permafrost Sites, Northern Alaska, 2018: 20425_PROCHECK_Manual_Web.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Permafrost_ActiveLayer_NSlope/comp/20425_PROCHECK_Manual_Web.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Permafrost_ActiveLayer_NSlope/comp/20587_TEROS11-12_Manual_Web.pdf",
-                    "description": "ABoVE: Active Layer Soil Characterization of Permafrost Sites, Northern Alaska, 2018: 20587_TEROS11-12_Manual_Web.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Active Layer Soil Characterization of Permafrost Sites, Northern Alaska, 2018: 20587_TEROS11-12_Manual_Web.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Permafrost_ActiveLayer_NSlope/comp/20587_TEROS11-12_Manual_Web.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Permafrost_ActiveLayer_NSlope/comp/Data_Descriptions_with_Equations.pdf",
-                    "description": "ABoVE: Active Layer Soil Characterization of Permafrost Sites, Northern Alaska, 2018: Data_Descriptions_with_Equations.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Active Layer Soil Characterization of Permafrost Sites, Northern Alaska, 2018: Data_Descriptions_with_Equations.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Permafrost_ActiveLayer_NSlope/comp/Data_Descriptions_with_Equations.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Permafrost_ActiveLayer_NSlope/comp/Permafrost_ActiveLayer_NSlope.pdf",
-                    "description": "ABoVE: Active Layer Soil Characterization of Permafrost Sites, Northern Alaska, 2018: Permafrost_ActiveLayer_NSlope.pdf",
                     "@type": "dcat:Distribution",
+                    "description": "ABoVE: Active Layer Soil Characterization of Permafrost Sites, Northern Alaska, 2018: Permafrost_ActiveLayer_NSlope.pdf",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/above/Permafrost_ActiveLayer_NSlope/comp/Permafrost_ActiveLayer_NSlope.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Permafrost_ActiveLayer_NSlope_Fig1.png",
-                    "description": "Site sampling plan used for characterizing active layer soils (left). Axes are in meters. At Imnavait Creek, active layer thickness (ALT) was measured on transects intersecting a central soil pit. Soil dielectric properties, in situ moisture and temperature profiles were measured, and soil samples were collected for analyses from the soil pit (right).",
                     "@type": "dcat:Distribution",
+                    "description": "Site sampling plan used for characterizing active layer soils (left). Axes are in meters. At Imnavait Creek, active layer thickness (ALT) was measured on transects intersecting a central soil pit. Soil dielectric properties, in situ moisture and temperature profiles were measured, and soil samples were collected for analyses from the soil pit (right).",
+                    "downloadURL": "https://daac.ornl.gov/ABOVE/guides/Permafrost_ActiveLayer_NSlope_Fig1.png",
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
-            "spatial": "-149.31 68.61 -148.56 69.81",
-            "theme": [
-                "ABoVE",
-                "geospatial"
-            ],
-            "language": [
-                "en-US"
-            ]
-        },
+            "graphic-preview-description": "Site sampling plan used for characterizing active layer soils (left). Axes are in meters. At Imnavait Creek, active layer thickness (ALT) was measured on transects intersecting a central soil pit. Soil dielectric properties, in situ moisture and temperature profiles were measured, and soil samples were collected for analyses from the soil pit (right).",
+            "graphic-preview-file": "https://daac.ornl.gov/ABOVE/guides/Permafrost_ActiveLayer_NSlope_Fig1.png",
+            "identifier": "C2143402217-ORNL_CLOUD",
+            "issued": "2024-05-01",
+            "keyword": [
+                "earth science",
+                "frozen ground",
+                "soils",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1759",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-05-02",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
+            "spatial": "-149.31 68.61 -148.56 69.81",
+            "temporal": "2018-08-22T00:00:00Z/2018-08-26T23:59:59Z",
+            "theme": [
+                "ABoVE",
+                "geospatial"
+            ],
+            "title": "ABoVE: Active Layer Soil Characterization of Permafrost Sites, Northern Alaska, 2018"
+        },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-MASTCAM-4-RDR-VID-V1.0",
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
-                "mars science laboratory",
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "NULL",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-mastcam-4-rdr-vid-v1.0_327b-huj8",
+            "issued": "2018-06-26",
+            "keyword": [
+                "mars science laboratory",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-MASTCAM-4-RDR-VID-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-mastcam-4-rdr-vid-v1.0_327b-huj8",
-            "description": "NULL",
-            "title": "MSL MARS MAST CAMERA 4 RDR\n                                      VIDEO V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "MSL MARS MAST CAMERA 4 RDR\n                                      VIDEO V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0120",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2000-04-07. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/FIRE/0120.",
-            "issued": "2000-03-17",
-            "temporal": "1991-11-17T00:00:00Z/1991-12-06T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-11",
-            "keyword": [
-                "atmosphere",
-                "clouds",
-                "earth science",
-                "infrared wavelengths",
-                "spectral/engineering",
-                "visible wavelengths",
-                "altitude"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "PAIVI PIIRONEN",
                 "hasEmail": "mailto:paivi.piironen@research.nokia.com"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1000001173-LARC_ASDC",
             "description": "The First ISCCP Regional Experiments have been designed to improve data products and cloud/radiation parameterizations used in general circulation models (GCMs). Specifically, the goals of FIRE are (1) to seek the basic understanding of the interaction of physical processes in determining life cycles of cirrus and marine stratocumulus systems and the radiative properties of these clouds during their life cycles and (2) to investigate the interrelationships between ISCCP data, GCM parameterizations, and higher space and time resolution cloud data. To-date, four intensive field-observation periods were planned and executed: a cirrus IFO (October 13 - November 2, 1986); a marine stratocumulus IFO off the southwestern coast of California (June 29 - July 20, 1987); a second cirrus IFO in southeastern Kansas (November 13 - December 7, 1991); and a second marine stratocumulus IFO in the eastern North Atlantic Ocean (June 1 - June 28, 1992). Each mission combined coordinated satellite, airborne, and surface observations with modeling studies to investigate the cloud properties and physical processes of the cloud systems.This data set contains altitude vs. time images (RTIs) of cirrus clouds collected during FIRE Cirrus 2 at Coffeyville, Kansas. The images were sampled at 5 km intervals in the cross wind scans.",
-            "title": "First ISCCP Regional Experiment (FIRE) Cirrus 2 Volume Imaging Lidar (VIL) Altitude vs. Time (RTI) Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0120",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0120",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001173-LARC_ASDC",
-                    "description": "Earthdata Search for FIRE_CI2_VIL_RTI_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for FIRE_CI2_VIL_RTI_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000001173-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_ci2_hsrl_vil_dataset.pdf",
-                    "description": "FIRE Cirrus 2 High Spectral Resolution Lidar (HSRL)/Volume Imaging Lidar (VIL) Langley DAAC Data Set Document",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE Cirrus 2 High Spectral Resolution Lidar (HSRL)/Volume Imaging Lidar (VIL) Langley DAAC Data Set Document",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_ci2_hsrl_vil_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ci2_vil_rti.txt",
-                    "description": "FIRE II experiment data with Altitude vs. Time (RTI) and Cirrus Scan gif pictures Readme",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE II experiment data with Altitude vs. Time (RTI) and Cirrus Scan gif pictures Readme",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ci2_vil_rti.txt",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0120",
-                    "description": "DOI data set landing page for FIRE_CI2_VIL_RTI_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for FIRE_CI2_VIL_RTI_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0120",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_CI2_VIL_RTI/",
-                    "description": "ASDC Direct Data Download for FIRE_CI2_VIL_RTI_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for FIRE_CI2_VIL_RTI_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_CI2_VIL_RTI/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_CI2_VIL_RTI/contents.html",
-                    "description": "OPeNDAP data access for FIRE_CI2_VIL_RTI_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for FIRE_CI2_VIL_RTI_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_CI2_VIL_RTI/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1000001173-LARC_ASDC",
+            "issued": "2000-03-17",
+            "keyword": [
+                "atmosphere",
+                "clouds",
+                "earth science",
+                "infrared wavelengths",
+                "spectral/engineering",
+                "visible wavelengths",
+                "altitude"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0120",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-07-11",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:LineString xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:4326\">36.93 -95.6 36.93 -95.7</gml:LineString>",
+            "temporal": "1991-11-17T00:00:00Z/1991-12-06T23:59:59.999Z",
             "theme": [
                 "FIRE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "First ISCCP Regional Experiment (FIRE) Cirrus 2 Volume Imaging Lidar (VIL) Altitude vs. Time (RTI) Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ECL5M-ICO44",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.. 2021-04-19. ECCO Sea-Ice and Snow Concentration and Thickness - Monthly Mean llc90 Grid (Version 4 Release 4). Version V4r4. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/ECL5M-ICO44. ECCO; ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.; 2020; ECCO Sea-Ice and Snow Concentration and Thickness - Monthly Mean llc90 Grid (Version 4 Release 4); 10.5067/ECL5M-ICO44; https://podaac.jpl.nasa.gov/ECCO.",
-            "issued": "2021-01-01",
-            "temporal": "1992-01-01T00:00:00Z/2018-01-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-12-31",
-            "references": [
-                "https://doi.org/10.5281/zenodo.3765928"
-            ],
-            "keyword": [
-                "earth science services",
-                "earth science",
-                "earth science reanalyses/assimilation models",
-                "sea ice",
-                "cryosphere",
-                "models"
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
-            "identifier": "C1991543764-POCLOUD",
-            "description": "This dataset provides monthly-averaged sea-ice and snow concentration, thickness, and pressure loading on the native Lat-Lon-Cap 90 (LLC90) model grid from the ECCO Version 4 Release 4 (V4r4) ocean and sea-ice state estimate. Estimating the Circulation and Climate of the Ocean (ECCO) ocean and sea-ice state estimates are dynamically and kinematically-consistent reconstructions of the three-dimensional time-evolving ocean, sea-ice, and surface atmospheric states. ECCO V4r4 is a free-running solution of the 1-degree global configuration of the MIT general circulation model (MITgcm) that has been fit to observations in a least-squares sense. Observational data constraints used in V4r4 include sea surface height (SSH) from satellite altimeters [ERS-1/2, TOPEX/Poseidon, GFO, ENVISAT, Jason-1,2,3, CryoSat-2, and SARAL/AltiKa]; sea surface temperature (SST) from satellite radiometers [AVHRR], sea surface salinity (SSS) from the Aquarius satellite radiometer/scatterometer, ocean bottom pressure (OBP) from the GRACE satellite gravimeter; sea ice concentration from satellite radiometers [SSM/I and SSMIS], and in-situ ocean temperature and salinity measured with conductivity-temperature-depth (CTD) sensors and expendable bathythermographs (XBTs) from several programs [e.g., WOCE, GO-SHIP, Argo, and others] and platforms [e.g., research vessels, gliders, moorings, ice-tethered profilers, and instrumented pinnipeds]. V4r4 covers the period 1992-01-01T12:00:00 to 2018-01-01T00:00:00.",
-            "release-place": "PO.DAAC",
-            "graphic-preview-description": "Thumbnail image for Website",
             "creator": "ECCO Consortium, Fukumori, I., Wang, O., Fenty, I., Forget, G., Heimbach, P., & Ponte, R. M.",
-            "title": "ECCO Sea-Ice and Snow Concentration and Thickness - Monthly Mean llc90 Grid (Version 4 Release 4)",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_SEA_ICE_CONC_THICKNESS_LLC0090GRID_MONTHLY_V4R4.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "This dataset provides monthly-averaged sea-ice and snow concentration, thickness, and pressure loading on the native Lat-Lon-Cap 90 (LLC90) model grid from the ECCO Version 4 Release 4 (V4r4) ocean and sea-ice state estimate. Estimating the Circulation and Climate of the Ocean (ECCO) ocean and sea-ice state estimates are dynamically and kinematically-consistent reconstructions of the three-dimensional time-evolving ocean, sea-ice, and surface atmospheric states. ECCO V4r4 is a free-running solution of the 1-degree global configuration of the MIT general circulation model (MITgcm) that has been fit to observations in a least-squares sense. Observational data constraints used in V4r4 include sea surface height (SSH) from satellite altimeters [ERS-1/2, TOPEX/Poseidon, GFO, ENVISAT, Jason-1,2,3, CryoSat-2, and SARAL/AltiKa]; sea surface temperature (SST) from satellite radiometers [AVHRR], sea surface salinity (SSS) from the Aquarius satellite radiometer/scatterometer, ocean bottom pressure (OBP) from the GRACE satellite gravimeter; sea ice concentration from satellite radiometers [SSM/I and SSMIS], and in-situ ocean temperature and salinity measured with conductivity-temperature-depth (CTD) sensors and expendable bathythermographs (XBTs) from several programs [e.g., WOCE, GO-SHIP, Argo, and others] and platforms [e.g., research vessels, gliders, moorings, ice-tethered profilers, and instrumented pinnipeds]. V4r4 covers the period 1992-01-01T12:00:00 to 2018-01-01T00:00:00.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECL5M-ICO44",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECL5M-ICO44",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/ecco",
-                    "description": "Mission and Instrument Overview",
                     "@type": "dcat:Distribution",
+                    "description": "Mission and Instrument Overview",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/ecco",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.ecco-group.org",
-                    "description": "The project website for the ECCO Consortium.",
                     "@type": "dcat:Distribution",
+                    "description": "The project website for the ECCO Consortium.",
+                    "downloadURL": "https://www.ecco-group.org",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://github.com/ECCO-GROUP/",
-                    "description": "Software maintained by ECCO Consortium on GitHub.",
                     "@type": "dcat:Distribution",
+                    "description": "Software maintained by ECCO Consortium on GitHub.",
+                    "downloadURL": "https://github.com/ECCO-GROUP/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://github.com/ECCO-GROUP/ECCO-v4-Configurations/tree/master/ECCOv4%20Release%204",
-                    "description": "ECCO Version 4 Release 4 model configuration maintained by the ECCO Consortium on GitHub",
                     "@type": "dcat:Distribution",
+                    "description": "ECCO Version 4 Release 4 model configuration maintained by the ECCO Consortium on GitHub",
+                    "downloadURL": "https://github.com/ECCO-GROUP/ECCO-v4-Configurations/tree/master/ECCOv4%20Release%204",
+                    "mediaType": "text/html",
                     "title": "View the documentation for this dataset's algorithms"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/misc/web/misc/ecco/docs/v4r4_reproduction_howto.pdf",
-                    "description": "Instructions for reproducing ECCO Version 4 Release 4",
                     "@type": "dcat:Distribution",
+                    "description": "Instructions for reproducing ECCO Version 4 Release 4",
+                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/misc/web/misc/ecco/docs/v4r4_reproduction_howto.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ecco-v4-python-tutorial.readthedocs.io/",
-                    "description": "Python Tutorials for ECCO Central Production Version 4 (ECCO V4)",
                     "@type": "dcat:Distribution",
+                    "description": "Python Tutorials for ECCO Central Production Version 4 (ECCO V4)",
+                    "downloadURL": "https://ecco-v4-python-tutorial.readthedocs.io/",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/misc/web/misc/ecco/docs/v4r4_user_guide.pdf",
-                    "description": "ECCO Version 4 Release 4 User Guide",
                     "@type": "dcat:Distribution",
+                    "description": "ECCO Version 4 Release 4 User Guide",
+                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/misc/web/misc/ecco/docs/v4r4_user_guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/misc/web/misc/ecco/docs/v4r4_synopsis.pdf",
-                    "description": "Synopsis of ECCO Version 4 Release 4",
                     "@type": "dcat:Distribution",
+                    "description": "Synopsis of ECCO Version 4 Release 4",
+                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/misc/web/misc/ecco/docs/v4r4_synopsis.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the documentation for this dataset's algorithms"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://dspace.mit.edu/handle/1721.1/110380",
-                    "description": "Synopsis of ECCO 'Central Estimate' global ocean and sea-ice state estimate, Version 4 Release 3",
                     "@type": "dcat:Distribution",
+                    "description": "Synopsis of ECCO 'Central Estimate' global ocean and sea-ice state estimate, Version 4 Release 3",
+                    "downloadURL": "https://dspace.mit.edu/handle/1721.1/110380",
+                    "mediaType": "text/html",
                     "title": "View the documentation for this dataset's algorithms"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/misc/web/misc/ecco/docs/v4r4_overview_plots.pdf",
-                    "description": "Sample Plots -- gcmfaces analysis of ECCO V4, Release 4 (1992-2017)",
                     "@type": "dcat:Distribution",
+                    "description": "Sample Plots -- gcmfaces analysis of ECCO V4, Release 4 (1992-2017)",
+                    "downloadURL": "https://podaac-tools.jpl.nasa.gov/drive/files/misc/web/misc/ecco/docs/v4r4_overview_plots.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's product usage"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_SEA_ICE_CONC_THICKNESS_LLC0090GRID_MONTHLY_V4R4.jpg",
-                    "description": "Thumbnail image for Website",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail image for Website",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_SEA_ICE_CONC_THICKNESS_LLC0090GRID_MONTHLY_V4R4.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ECL5M-ICO44",
-                    "description": "Access the data set landing page for the collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data set landing page for the collection.",
+                    "downloadURL": "https://doi.org/10.5067/ECL5M-ICO44",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1991543764-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1991543764-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C1991543764-POCLOUD/temporal",
-                    "description": "Browse and download granules over HTTPS using the virtual directories service",
                     "@type": "dcat:Distribution",
+                    "description": "Browse and download granules over HTTPS using the virtual directories service",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C1991543764-POCLOUD/temporal",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 }
             ],
+            "graphic-preview-description": "Thumbnail image for Website",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/ECCO_L4_SEA_ICE_CONC_THICKNESS_LLC0090GRID_MONTHLY_V4R4.jpg",
+            "identifier": "C1991543764-POCLOUD",
+            "issued": "2021-01-01",
+            "keyword": [
+                "earth science services",
+                "earth science",
+                "earth science reanalyses/assimilation models",
+                "sea ice",
+                "cryosphere",
+                "models"
+            ],
+            "landingPage": "https://doi.org/10.5067/ECL5M-ICO44",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-12-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/JPL/PODAAC"
+            },
+            "references": [
+                "https://doi.org/10.5281/zenodo.3765928"
+            ],
+            "release-place": "PO.DAAC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1992-01-01T00:00:00Z/2018-01-01T00:00:00Z",
             "theme": [
                 "ECCO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ECCO Sea-Ice and Snow Concentration and Thickness - Monthly Mean llc90 Grid (Version 4 Release 4)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aorex.spice&version=8.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This bundle contains OSIRIS-REx SPICE kernels and related documentation.",
+            "identifier": "urn:nasa:pds:orex.spice",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "osiris-rex",
                 "observation geometry",
                 "(101955) bennu"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aorex.spice&version=8.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:orex.spice",
-            "description": "This bundle contains OSIRIS-REx SPICE kernels and related documentation.",
-            "title": "OSIRIS-REx SPICE Kernel Archive Bundle",
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
+            "title": "OSIRIS-REx SPICE Kernel Archive Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSIWAC-3-CR2-CHECKOUT-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 3 data set contains radiometric calibrated image data in W/m^2/sr/nm,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the CRUISE 2 mission phase, covering the period  from 2005-04-05T00:00:00.000 to 2006-07-28T23:59:59.000. The prime objective was commissioning / calibration. Several targets of opportunity were observed, but none of them is identifiable as prime target. This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Reprocessed dataset after October 2018 PSA/PDS external peer review.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osiwac-3-cr2-checkout-v2.0_32cs-q4vm",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "starfield",
                 "international rosetta mission",
                 "9p/tempel 1 (1867 g1)",
                 "16 cyg b"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-X-OSIWAC-3-CR2-CHECKOUT-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-x-osiwac-3-cr2-checkout-v2.0_32cs-q4vm",
-            "description": "This CODMAC level 3 data set contains radiometric calibrated image data in W/m^2/sr/nm,  acquired by the OSIRIS Wide Angle Camera on the Rosetta spacecraft  during the CRUISE 2 mission phase, covering the period  from 2005-04-05T00:00:00.000 to 2006-07-28T23:59:59.000. The prime objective was commissioning / calibration. Several targets of opportunity were observed, but none of them is identifiable as prime target. This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Reprocessed dataset after October 2018 PSA/PDS external peer review.",
-            "title": "ROSETTA-ORBITER CHECKOUT OSIWAC 3 CR2 RDR V2.0",
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
+            "title": "ROSETTA-ORBITER CHECKOUT OSIWAC 3 CR2 RDR V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ECOSTRESS/ECO1BGEO.001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Simon Hook, Mike Smyth, Tom Logan, William Johnson. 2019-03-27. ECO1BGEO.001. ECOSTRESS Geolocation Daily L1B Global 70 m V001. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/ECOSTRESS/ECO1BGEO.001. https://doi.org/10.5067/ECOSTRESS/ECO1BGEO.001. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2019-03-27",
-            "temporal": "2018-07-09T00:00:00Z/2024-09-09T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-04",
-            "keyword": [
-                "sensor characteristics",
-                "earth science",
-                "spectral/engineering"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Simon Hook",
                 "hasEmail": "mailto:simon.j.hook@jpl.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LP DAAC"
-            },
-            "identifier": "C1534584923-LPDAAC_ECS",
-            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52\u00b0 N and 52\u00b0 S latitudes. A map of the acquisition coverage can be found in figure 2 on the ECOSTRESS website(https://ecostress.jpl.nasa.gov/science).\r\n\r\nThe ECO1BGEO Version 1 data product provides the geolocation information for the radiance values retrieved in the ECO1BRAD Version 1 data product (https://doi.org/10.5067/ECOSTRESS/ECO1BRAD.001). The ECO1BGEO data product should be used to georeference the ECO1BRAD, ECO2CLD, ECO2LSTE, ECO3ANCQA, ECO3ETPTJPL, ECO4ESIPTJPL, ECO4WUE data products. The geolocation processing corrects the ISS-reported ephemeris and attitude data by image matching with a global ortho-base derived from Landsat data, and then assigns latitude and longitude values to each of the Level 1 radiance pixels. When image matching is successful, the data are geolocated to better than 50 meter (m) accuracy. The ECO1BGEO data product is provided as swath data.\r\n\r\nThe ECO1BGEO data product contains data layers for latitude and longitude values, solar and view geometry information, surface height, and the fraction of pixel on land versus water.\r\n\r\nKnown Issues: *Geolocation accuracy: In cases where scenes were not successfully matched with the ortho-base, the geolocation error is significantly larger, with the worst-case geolocation error for uncorrected data being at 7 kilometers (km). Within the metadata of the ECO1BGEO file, if the field \"L1GEOMetadata/OrbitCorrectionPerformed\" is \"True,\" the data was corrected, and geolocation accuracy should be better than 50 m. If this is \"False,\" then the data was processed without correcting the geolocation and will have up to 7 km geolocation error.\r\n*Data acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented and science acquisitions resumed. To optimize the new acquisition approach TIR bands 2, 4 and 5 are being downloaded. The data products are as previously, except the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023.\r\n*Data acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\r\n*Data acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing Unit firmware update (version 4.1) to the payload on April 28, 2023. To better balance contiguous science data scene variables, 3-band collection is currently being interleaved with 5-band acquisitions over the orbital day/night periods.",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "series-name": "ECO1BGEO.001",
             "creator": "Simon Hook, Mike Smyth, Tom Logan, William Johnson",
-            "title": "ECOSTRESS Geolocation Daily L1B Global 70m V001",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The ECOsystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) mission measures the temperature of plants to better understand how much water plants need and how they respond to stress. ECOSTRESS is attached to the International Space Station (ISS) and collects data globally between 52\u00b0 N and 52\u00b0 S latitudes. A map of the acquisition coverage can be found in figure 2 on the ECOSTRESS website(https://ecostress.jpl.nasa.gov/science).\r\n\r\nThe ECO1BGEO Version 1 data product provides the geolocation information for the radiance values retrieved in the ECO1BRAD Version 1 data product (https://doi.org/10.5067/ECOSTRESS/ECO1BRAD.001). The ECO1BGEO data product should be used to georeference the ECO1BRAD, ECO2CLD, ECO2LSTE, ECO3ANCQA, ECO3ETPTJPL, ECO4ESIPTJPL, ECO4WUE data products. The geolocation processing corrects the ISS-reported ephemeris and attitude data by image matching with a global ortho-base derived from Landsat data, and then assigns latitude and longitude values to each of the Level 1 radiance pixels. When image matching is successful, the data are geolocated to better than 50 meter (m) accuracy. The ECO1BGEO data product is provided as swath data.\r\n\r\nThe ECO1BGEO data product contains data layers for latitude and longitude values, solar and view geometry information, surface height, and the fraction of pixel on land versus water.\r\n\r\nKnown Issues: *Geolocation accuracy: In cases where scenes were not successfully matched with the ortho-base, the geolocation error is significantly larger, with the worst-case geolocation error for uncorrected data being at 7 kilometers (km). Within the metadata of the ECO1BGEO file, if the field \"L1GEOMetadata/OrbitCorrectionPerformed\" is \"True,\" the data was corrected, and geolocation accuracy should be better than 50 m. If this is \"False,\" then the data was processed without correcting the geolocation and will have up to 7 km geolocation error.\r\n*Data acquisition gap: ECOSTRESS was launched on June 29, 2018, and moved to autonomous science operations on August 20, 2018, following a successful in-orbit checkout period. On September 29, 2018, ECOSTRESS experienced an anomaly with its primary mass storage unit (MSU). ECOSTRESS has a primary and secondary MSU (A and B). On December 5, 2018, the instrument was switched to the secondary MSU and science operations resumed. On March 14, 2019, the secondary MSU experienced a similar anomaly temporarily halting science acquisitions. On May 15, 2019, a new data acquisition approach was implemented and science acquisitions resumed. To optimize the new acquisition approach TIR bands 2, 4 and 5 are being downloaded. The data products are as previously, except the bands not downloaded contain fill values (L1 radiance and L2 emissivity). This approach was implemented from May 15, 2019, through April 28, 2023.\r\n*Data acquisition gap: From February 8 to February 16, 2020, an ECOSTRESS instrument issue resulted in a data anomaly that created striping in band 4 (10.5 micron). These data products have been reprocessed and are available for download. No ECOSTRESS data were acquired on February 17, 2020, due to the instrument being in SAFEHOLD. Data acquired following the anomaly have not been affected.\r\n*Data acquisition: ECOSTRESS has now successfully returned to 5-band mode after being in 3-band mode since 2019. This feature was successfully enabled following a Data Processing Unit firmware update (version 4.1) to the payload on April 28, 2023. To better balance contiguous science data scene variables, 3-band collection is currently being interleaved with 5-band acquisitions over the orbital day/night periods.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECOSTRESS%2FECO1BGEO.001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FECOSTRESS%2FECO1BGEO.001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/xhdf5",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1534584923-LPDAAC_ECS",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C1534584923-LPDAAC_ECS",
+                    "mediaType": "application/xhdf5",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/xhdf5",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/ECOSTRESS/ECO1BGEO.001/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/ECOSTRESS/ECO1BGEO.001/",
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
-                    "downloadURL": "https://doi.org/10.5067/ECOSTRESS/ECO1BGEO.001",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/ECOSTRESS/ECO1BGEO.001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1323/ECO1B_User_Guide_V1.pdf",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1323/ECO1B_User_Guide_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ecostress.jpl.nasa.gov/science",
-                    "description": "The ECOSTRESS website provides detailed information on the mission, instrument, products, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The ECOSTRESS website provides detailed information on the mission, instrument, products, etc.",
+                    "downloadURL": "https://ecostress.jpl.nasa.gov/science",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/222/ECO1B_Calibration_ATBD_V1.pdf",
-                    "description": "The Calibration ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The Calibration ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/222/ECO1B_Calibration_ATBD_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/223/ECO1B_Geolocation_ATBD_V1.pdf",
-                    "description": "The Geolocation ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The Geolocation ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/223/ECO1B_Geolocation_ATBD_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1321/ECO1B_PSD_V1.pdf",
-                    "description": "The Product Specification Document (PSD) describes the format and contents of the ECOSTRESS product.",
                     "@type": "dcat:Distribution",
+                    "description": "The Product Specification Document (PSD) describes the format and contents of the ECOSTRESS product.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1321/ECO1B_PSD_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/225/ECO1B_Rad_ASD_V1.pdf",
-                    "description": "The Radiance Algorithm Specification Document (ASD) describes the computer processing used to generate the ECOSTRESS products.",
                     "@type": "dcat:Distribution",
+                    "description": "The Radiance Algorithm Specification Document (ASD) describes the computer processing used to generate the ECOSTRESS products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/225/ECO1B_Rad_ASD_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/226/ECO1B_Geo_ASD_V1.pdf",
-                    "description": "The Geolocation Algorithm Specification Document (ASD) describes the computer processing used to generate the ECOSTRESS geolocation product.",
                     "@type": "dcat:Distribution",
+                    "description": "The Geolocation Algorithm Specification Document (ASD) describes the computer processing used to generate the ECOSTRESS geolocation product.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/226/ECO1B_Geo_ASD_V1.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1573/Quick_Guide_for_Accessing_ECOSTRESS_Swath_Data_in_NASA_Earthdata_Search.pdf",
-                    "description": "The Earthdata Search Quick Guide explains how to search ECOSTRESS data in NASA Earthdata Search.",
                     "@type": "dcat:Distribution",
+                    "description": "The Earthdata Search Quick Guide explains how to search ECOSTRESS data in NASA Earthdata Search.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1573/Quick_Guide_for_Accessing_ECOSTRESS_Swath_Data_in_NASA_Earthdata_Search.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's how-to documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://appeears.earthdatacloud.nasa.gov/",
-                    "description": "The Application for Extracting and Exploring Analysis Ready Samples (A\u03c1\u03c1EEARS) offers a simple and efficient way to perform data access and transformation processes.",
                     "@type": "dcat:Distribution",
+                    "description": "The Application for Extracting and Exploring Analysis Ready Samples (A\u03c1\u03c1EEARS) offers a simple and efficient way to perform data access and transformation processes.",
+                    "downloadURL": "https://appeears.earthdatacloud.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through APPEEARS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/ECOA/ECOSTRESS/ECO1BGEO.001/contents.html",
-                    "description": "OPeNDAP provides direct access to data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP provides direct access to data via HTTPS.",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/ECOA/ECOSTRESS/ECO1BGEO.001/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1534584923-LPDAAC_ECS",
+            "issued": "2019-03-27",
+            "keyword": [
+                "sensor characteristics",
+                "earth science",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://doi.org/10.5067/ECOSTRESS/ECO1BGEO.001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-09-04",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, South Dakota, USA",
+            "series-name": "ECO1BGEO.001",
             "spatial": "-180.0 -54.0 180.0 54.0",
+            "temporal": "2018-07-09T00:00:00Z/2024-09-09T00:00:00Z",
             "theme": [
                 "ECOSTRESS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "ECOSTRESS Geolocation Daily L1B Global 70m V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0895-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-07-13T21:14:45.000 to 2015-07-14T04:39:07.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0895-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC3-0895-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc3-0895-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 3 phase 2015-07-01 to 2015-10-21. It is a Global Gravity measurement at the comet 67P and covers the time 2015-07-13T21:14:45.000 to 2015-07-14T04:39:07.500.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0895 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 3 0895 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/698",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Stone, T.A., and P. Schlesinger. 2003. RLC Selected Infrastructure Data for the Former Soviet Union, 1993. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/698",
-            "issued": "2023-11-21",
-            "temporal": "1993-01-01T00:00:00Z/1993-12-31T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-12-02",
-            "keyword": [
-                "human dimensions",
-                "earth science",
-                "infrastructure",
-                "surface water",
-                "terrestrial hydrosphere"
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
-            "identifier": "C2810672079-ORNL_CLOUD",
             "description": "This data set consists of roads, drainage, railroads, utilities, and population center information in readily usable vector format for the land area of the Former Soviet Union. The purpose of this dataset was to create a completely intact vector layer which could be readily used to aid in mapping efforts for the area of the FSU. These five vector data layers were assembled from the Digital Chart of the World (DCW), 1993. Individual record attributes were stored for population centers only. Vector maps for the FSU are in ArcView shapefile format.",
-            "graphic-preview-description": "Browse Image",
-            "title": "RLC Selected Infrastructure Data for the Former Soviet Union, 1993",
-            "graphic-preview-file": "https://daac.ornl.gov/RLC/guides/fsudcw.jpg",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F698",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F698",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/global_vegetation/rlc_vector_data/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/global_vegetation/rlc_vector_data/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/RLC/guides/RLC_vector_data.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/RLC/guides/RLC_vector_data.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/698",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/698",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/rlc_vector_data/comp/fsudcw_readme.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/rlc_vector_data/comp/fsudcw_readme.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/rlc_vector_data/comp/RLC_vector_data.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/global_vegetation/rlc_vector_data/comp/RLC_vector_data.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://daac.ornl.gov/RLC/guides/fsudcw.jpg",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/RLC/guides/fsudcw.jpg",
+                    "mediaType": "image/jpeg",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/RLC/guides/fsudcw.jpg",
+            "identifier": "C2810672079-ORNL_CLOUD",
+            "issued": "2023-11-21",
+            "keyword": [
+                "human dimensions",
+                "earth science",
+                "infrastructure",
+                "surface water",
+                "terrestrial hydrosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/698",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-12-02",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "25.0 23.21 180.0 71.0",
+            "temporal": "1993-01-01T00:00:00Z/1993-12-31T23:59:59Z",
             "theme": [
                 "Vegetation",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "RLC Selected Infrastructure Data for the Former Soviet Union, 1993"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://appel.nasa.gov/knowledge-sharing/publications/appel-releases-ibook-html/",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "references": [
-                "http://km.nasa.gov/knowledge-map/"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Ed Hoffman",
+                "hasEmail": "mailto:ehoffman@nasa.gov"
+            },
+            "description": "The NASA Academy of Program/Project & Engineering Leadership (APPEL) is excited to announce the public release of Orbital Debris Management and Risk Mitigation, its first publication of NASA training materials using the iBook format.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://appel.nasa.gov/wp-content/themes/bold-2.0/ibooks/Orbital_Debris_Management_and_Risk_Mitigation.ibooks",
+                    "mediaType": "application/ibooks"
+                }
             ],
+            "identifier": "NASA-863",
+            "issued": "2018-06-25",
             "keyword": [
                 "orbital",
                 "training",
@@ -59227,266 +59236,271 @@
                 "sharing",
                 "management"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Ed Hoffman",
-                "hasEmail": "mailto:ehoffman@nasa.gov"
-            },
+            "landingPage": "http://appel.nasa.gov/knowledge-sharing/publications/appel-releases-ibook-html/",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:045"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-863",
-            "description": "The NASA Academy of Program/Project & Engineering Leadership (APPEL) is excited to announce the public release of Orbital Debris Management and Risk Mitigation, its first publication of NASA training materials using the iBook format.",
-            "title": "Academy of Program/Project & Engineering Leadership Orbital Debris Management and Risk Mitigation",
-            "programCode": [
-                "026:045"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://appel.nasa.gov/wp-content/themes/bold-2.0/ibooks/Orbital_Debris_Management_and_Risk_Mitigation.ibooks",
-                    "mediaType": "application/ibooks"
-                }
+            "references": [
+                "http://km.nasa.gov/knowledge-map/"
             ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "Academy of Program/Project & Engineering Leadership Orbital Debris Management and Risk Mitigation"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/N14_AVH02C1.006",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "The Long-Term Data Record (LTDR) project. 2023-07-25. NOAA-14 AVHRR Top-of-Atmosphere Reflectance Daily L3 Global 0.05 Deg. CMG. Version 6. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, L1 and Atmosphere Archive and Distribution System (LAADS). https://doi.org/10.5067/MODIS/N14_AVH02C1.006.",
-            "issued": "2022-07-21",
-            "temporal": "1995-01-01T00:00:00Z/2023-09-04T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-24",
-            "keyword": [
-                "land surface",
-                "surface radiative properties",
-                "atmosphere",
-                "earth science",
-                "infrared wavelengths",
-                "spectral/engineering",
-                "atmospheric radiation"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:MODAPSUSO@lists.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
-            "identifier": "C2737882843-LAADS",
-            "description": "The Long-Term Data Record (LTDR) produces, validates, and distributes a global land surface climate data record (CDR) that uses both mature and well-tested algorithms in concert with the best-available polar-orbiting satellite data from past to the present.   The CDR is critically important to studying global climate change.  The LTDR project is unique in that it serves as a bridge that connects data derived from the NOAA Advanced Very High Resolution Radiometer (AVHRR), the EOS Moderate resolution Imaging Spectroradiometer (MODIS), the Suomi National Polar-orbiting Partnership (SNPP) Visible Infrared Imaging Radiometer Suite (VIIRS), and Joint Polar Satellite System (JPSS) VIIRS missions.  The LTDR draws from the following eight AVHRR missions: \r\nNOAA-7, NOAA-9, NOAA-11, NOAA-14, NOAA-16, NOAA-18, NOAA-19, and MetOp-B.\r\nCurrently, the project generates a daily surface reflectance product as the fundamental climate data record (FCDR) and derives daily Normalized Differential Vegetation Index (NDVI) and Leaf-Area Index/fraction of absorbed Photosynthetically Active Radiation (LAI/fPAR) as two thematic CDRs (TCDR).  LAI/fPAR was developed as an experimental product.\r\n\r\nThe  NOAA-14 AVHRR Top-of-Atmosphere Reflectance Daily L3 Global 0.05Deg CMG, short-name N14_AVH02C1 is generated from GIMMS Advanced Processing System (GAPS) BRDF-corrected Surface Reflectance product (AVH01C1). The N14_AVH02C1 consist of Top-of-atmosphere reflectance for bands 1 and 2, data Quality flags, angles (solar zenith, view zenith, and relative azimuth), thermal data (thermal bands 3, 4 and 5), and additional data (scan time).",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "The Long-Term Data Record (LTDR) project",
-            "title": "NOAA-14 AVHRR Top-of-Atmosphere Reflectance Daily L3 Global 0.05 Deg. CMG",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Long-Term Data Record (LTDR) produces, validates, and distributes a global land surface climate data record (CDR) that uses both mature and well-tested algorithms in concert with the best-available polar-orbiting satellite data from past to the present.   The CDR is critically important to studying global climate change.  The LTDR project is unique in that it serves as a bridge that connects data derived from the NOAA Advanced Very High Resolution Radiometer (AVHRR), the EOS Moderate resolution Imaging Spectroradiometer (MODIS), the Suomi National Polar-orbiting Partnership (SNPP) Visible Infrared Imaging Radiometer Suite (VIIRS), and Joint Polar Satellite System (JPSS) VIIRS missions.  The LTDR draws from the following eight AVHRR missions: \r\nNOAA-7, NOAA-9, NOAA-11, NOAA-14, NOAA-16, NOAA-18, NOAA-19, and MetOp-B.\r\nCurrently, the project generates a daily surface reflectance product as the fundamental climate data record (FCDR) and derives daily Normalized Differential Vegetation Index (NDVI) and Leaf-Area Index/fraction of absorbed Photosynthetically Active Radiation (LAI/fPAR) as two thematic CDRs (TCDR).  LAI/fPAR was developed as an experimental product.\r\n\r\nThe  NOAA-14 AVHRR Top-of-Atmosphere Reflectance Daily L3 Global 0.05Deg CMG, short-name N14_AVH02C1 is generated from GIMMS Advanced Processing System (GAPS) BRDF-corrected Surface Reflectance product (AVH01C1). The N14_AVH02C1 consist of Top-of-atmosphere reflectance for bands 1 and 2, data Quality flags, angles (solar zenith, view zenith, and relative azimuth), thermal data (thermal bands 3, 4 and 5), and additional data (scan time).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FN14_AVH02C1.006",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FN14_AVH02C1.006",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ltdr.modaps.eosdis.nasa.gov/cgi-bin/ltdr/ltdrPage.cgi?fileName=docs",
-                    "description": "Overview of LTDR Products documents",
                     "@type": "dcat:Distribution",
+                    "description": "Overview of LTDR Products documents",
+                    "downloadURL": "https://ltdr.modaps.eosdis.nasa.gov/cgi-bin/ltdr/ltdrPage.cgi?fileName=docs",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/1/N14_AVH02C1--466",
-                    "description": "Search and order products from LAADS website.",
                     "@type": "dcat:Distribution",
+                    "description": "Search and order products from LAADS website.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/1/N14_AVH02C1--466",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LAADS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/466/N14_AVH02C1/",
-                    "description": "Direct access to C6 N14_AVH02C1 data set.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to C6 N14_AVH02C1 data set.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/466/N14_AVH02C1/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://landweb.modaps.eosdis.nasa.gov/QA_WWW/forPage/user_guide/avhrr/LTDR_Ver5_Products_UserGuide_v1.0.pdf",
-                    "description": "A combined User's Guides for all L3 LTDR products",
                     "@type": "dcat:Distribution",
+                    "description": "A combined User's Guides for all L3 LTDR products",
+                    "downloadURL": "https://landweb.modaps.eosdis.nasa.gov/QA_WWW/forPage/user_guide/avhrr/LTDR_Ver5_Products_UserGuide_v1.0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 }
             ],
+            "identifier": "C2737882843-LAADS",
+            "issued": "2022-07-21",
+            "keyword": [
+                "land surface",
+                "surface radiative properties",
+                "atmosphere",
+                "earth science",
+                "infrared wavelengths",
+                "spectral/engineering",
+                "atmospheric radiation"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/N14_AVH02C1.006",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-07-24",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1995-01-01T00:00:00Z/2023-09-04T00:00:00Z",
             "theme": [
                 "NOAA - SPACE WEATHER PROGRAM",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NOAA-14 AVHRR Top-of-Atmosphere Reflectance Daily L3 Global 0.05 Deg. CMG"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MOD14A2.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Louis Giglio, Christopher Justice. 2021-02-11. MODIS/Terra Thermal Anomalies/Fire 8-Day L3 Global 1km SIN Grid V061. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MOD14A2.061. https://doi.org/10.5067/MODIS/MOD14A1.061. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2021-02-11",
-            "temporal": "2000-02-18T00:00:00Z/2024-05-27T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-11",
-            "keyword": [
-                "biosphere",
-                "national geospatial data asset",
-                "surface thermal properties",
-                "earth science",
-                "ecological dynamics",
-                "ngda",
-                "land surface"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Louis Giglio",
                 "hasEmail": "mailto:lgiglio@umd.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LP DAAC"
-            },
-            "identifier": "C2565791018-LPCLOUD",
-            "description": "The Terra Moderate Resolution Imaging Spectroradiometer (MODIS) Thermal Anomalies and Fire 8-Day (MOD14A2) Version 6.1 data are generated at 1 kilometer (km) spatial resolution as a Level 3 product. The MOD14A2 gridded composite contains the maximum value of the individual fire pixel classes detected during the eight days of acquisition.\n\nThe Science Dataset (SDS) layers include the fire mask and pixel quality indicators.\n\nValidation at stage 3 (https://modis-land.gsfc.nasa.gov/MODLAND_val.html) has been achieved for all MODIS Thermal Anomalies and Fire products. Further details regarding MODIS land product validation for the MOD14 data product is available from the MODIS land team validation site (https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD14).\n\nImprovements/Changes from Previous Versions\n\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
-            "release-place": "Sioux Falls, South Dakota, USA",
-            "graphic-preview-description": "Browse image for Earthdata Search",
             "creator": "Louis Giglio, Christopher Justice",
-            "title": "MODIS/Terra Thermal Anomalies/Fire 8-Day L3 Global 1km SIN Grid V061",
-            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2622741318-LPCLOUD?h=85&w=85",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The Terra Moderate Resolution Imaging Spectroradiometer (MODIS) Thermal Anomalies and Fire 8-Day (MOD14A2) Version 6.1 data are generated at 1 kilometer (km) spatial resolution as a Level 3 product. The MOD14A2 gridded composite contains the maximum value of the individual fire pixel classes detected during the eight days of acquisition.\n\nThe Science Dataset (SDS) layers include the fire mask and pixel quality indicators.\n\nValidation at stage 3 (https://modis-land.gsfc.nasa.gov/MODLAND_val.html) has been achieved for all MODIS Thermal Anomalies and Fire products. Further details regarding MODIS land product validation for the MOD14 data product is available from the MODIS land team validation site (https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD14).\n\nImprovements/Changes from Previous Versions\n\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD14A2.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMOD14A2.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOLT/MOD14A2.061/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOLT/MOD14A2.061/",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2565791018-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2565791018-LPCLOUD",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://appeears.earthdatacloud.nasa.gov/",
-                    "description": "The Application for Extracting and Exploring Analysis Ready Samples (A\u03c1\u03c1EEARS) offers a simple and efficient way to perform data access and transformation processes.",
                     "@type": "dcat:Distribution",
+                    "description": "The Application for Extracting and Exploring Analysis Ready Samples (A\u03c1\u03c1EEARS) offers a simple and efficient way to perform data access and transformation processes.",
+                    "downloadURL": "https://appeears.earthdatacloud.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MOD14A2.061",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MOD14A2.061",
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
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/1005/MOD14_User_Guide_V61.pdf",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/1005/MOD14_User_Guide_V61.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/87/MOD14_ATBD.pdf",
-                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/87/MOD14_ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MOD14A2",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/61/MOD14A2",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis-land.gsfc.nasa.gov/MODLAND_val.html",
-                    "description": "Validation at stage 3 has been achieved for the MODIS Thermal Anomalies and Fire products.",
                     "@type": "dcat:Distribution",
+                    "description": "Validation at stage 3 has been achieved for the MODIS Thermal Anomalies and Fire products.",
+                    "downloadURL": "https://modis-land.gsfc.nasa.gov/MODLAND_val.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD14",
-                    "description": "Further details regarding MODIS land product validation for the MOD14 data product is available from the MODIS Land Team Validation site.",
                     "@type": "dcat:Distribution",
+                    "description": "Further details regarding MODIS land product validation for the MOD14 data product is available from the MODIS Land Team Validation site.",
+                    "downloadURL": "https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MOD14",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP131/MOLT/MOD14A2.061/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP131/MOLT/MOD14A2.061/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2622741318-LPCLOUD?h=85&w=85",
-                    "description": "Browse image for Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse image for Earthdata Search",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2622741318-LPCLOUD?h=85&w=85",
+                    "mediaType": "text/html",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse image for Earthdata Search",
+            "graphic-preview-file": "https://cmr.earthdata.nasa.gov/browse-scaler/browse_images/granules/G2622741318-LPCLOUD?h=85&w=85",
+            "identifier": "C2565791018-LPCLOUD",
+            "issued": "2021-02-11",
+            "keyword": [
+                "biosphere",
+                "national geospatial data asset",
+                "surface thermal properties",
+                "earth science",
+                "ecological dynamics",
+                "ngda",
+                "land surface"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MOD14A2.061",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-02-11",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, South Dakota, USA",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2000-02-18T00:00:00Z/2024-05-27T00:00:00Z",
             "theme": [
                 "Terra",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Terra Thermal Anomalies/Fire 8-Day L3 Global 1km SIN Grid V061"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/32nk-tfsz",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Larvae-Pupae transition flies (Drosophila) were recovered and transport for 3 days at 12-14C to arrest development until the launch site then exposed to RT (18-20C) for some hours including the launch and trip to the International Space Station then pupae were exposed to microgravity in the ISS for 4 days and a half at 22C. Finally pupae were fixed on acetone and frozen until recovery on Earth. Four groups of samples: 1 ISS (+ground control) as described 2 RPM (microgravity simulator on Earth) as described 3 RPM without constrains (No MAMBA container and only 5 days exposure without cold transport) and 4 centrifuge 10g without constrains control.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-36",
+                    "mediaType": "text/html",
+                    "title": "Transcription profiling of Drosophila after exposure to microgravity in the International Space Station and in a microgravity simulator"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-36_32nk-tfsz",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "labeling",
                 "affymetrix:protocol:hybridization-unknown",
@@ -59501,74 +59515,35 @@
                 "p-mtab-3322",
                 "treatment"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/32nk-tfsz",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-36_32nk-tfsz",
-            "description": "Larvae-Pupae transition flies (Drosophila) were recovered and transport for 3 days at 12-14C to arrest development until the launch site then exposed to RT (18-20C) for some hours including the launch and trip to the International Space Station then pupae were exposed to microgravity in the ISS for 4 days and a half at 22C. Finally pupae were fixed on acetone and frozen until recovery on Earth. Four groups of samples: 1 ISS (+ground control) as described 2 RPM (microgravity simulator on Earth) as described 3 RPM without constrains (No MAMBA container and only 5 days exposure without cold transport) and 4 centrifuge 10g without constrains control.",
-            "title": "Transcription profiling of Drosophila after exposure to microgravity in the International Space Station and in a microgravity simulator",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-36",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Transcription profiling of Drosophila after exposure to microgravity in the International Space Station and in a microgravity simulator"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Transcription profiling of Drosophila after exposure to microgravity in the International Space Station and in a microgravity simulator"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1273348496-GES_DISC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Miller, Alvin Jim, et al.. 1994-10-24. UARZCNMC. Version 001. UARS Correlative NMC Daily Gridded Stratospheric Assimilated Data V001. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/UARZCNMC_001.html. Digital Science Data.",
-            "issued": "1991-09-12",
-            "temporal": "1991-09-12T00:00:00Z/2001-09-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "1991-09-12",
-            "keyword": [
-                "atmospheric winds",
-                "altitude",
-                "earth science",
-                "atmosphere",
-                "atmospheric water vapor",
-                "atmospheric temperature"
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
-            "identifier": "C1273348496-GES_DISC",
-            "description": "The UARS Correlative assimilation data from NOAA's National Meteorological Center (NMC) consists of daily model runs at 12 GMT as a means of providing an independent analysis for comparison with data from the UARS instruments. The NMC data product includes temperature (Kelvin), humidity (%), geopotential height (m), and zonal and meridional wind components (m/s).\n\nGeopotential height and atmospheric temperature data are derived from two analysis systems: 1) tropospheric fields from 1000 to 100 mb, and 2) stratospheric analyses from 70 to 0.4 mb. The tropospheric fields are the 12 GMT gridded fields which are part of the Global Daily Assimilation System (GDAS), where data from radiosondes, aircraft, satellites, ships, bouys, or any other conventional means are assimilated and merged into meteorological fields (heights, temperature, winds). The stratospheric analyses are 12 GMT operational analyses at the 70 - 0.4 mb pressure levels produced from satellite temperature retrievals and RAOBS via a modified Cressman analysis. Tropospheric temperature analyses use combined NOAA-10 and NOAA-11 data. Moisture (northern hemisphere only) and Winds data are obtained from the NMC GDAS.\n\nThe gridded fields are on the standard 65 x 65 NMC polar stereographic grid oriented 80W (grid increment 381 km at 60N), and 100E (grid increment 381 km at 60S); Pole at (33,33). The NMC uses 18 standard pressure levels for data at 1000, 850, 700, 500, 400, 300, 250, 200, 150, 100, 70, 50, 30, 10, 5, 2, 1, 0.4 millibars. Height and temperature data are produced at all 18 pressure levels from 1000 mb to 0.4 mb. Moisture data are only produced in the northern hemisphere for the 6 lowest altitude pressure levels. Wind data are produced for the 12 lowest altitude levels in the northern hemisphere, and at the 4 levels 1000, 500, 300, and 250 mb in the southern hemisphere.\n\nThere are four data files representing each subtype per day. Included in the NMC correlative data set will be a geographical data richness file. This file is used by the NMC access routines, and indicates the radiosonde coverage for each point on the NMC grid. The data files are available in a binary record oriented format.",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "UARZCNMC",
             "creator": "Miller, Alvin Jim, et al.",
-            "title": "UARS Correlative NMC Daily Gridded Stratospheric Assimilated Data V001 (UARZCNMC) at GES DISC",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/UARZCNMC_001.png",
-            "programCode": [
-                "026:001"
-            ],
+            "data-presentation-form": "Digital Science Data",
+            "description": "The UARS Correlative assimilation data from NOAA's National Meteorological Center (NMC) consists of daily model runs at 12 GMT as a means of providing an independent analysis for comparison with data from the UARS instruments. The NMC data product includes temperature (Kelvin), humidity (%), geopotential height (m), and zonal and meridional wind components (m/s).\n\nGeopotential height and atmospheric temperature data are derived from two analysis systems: 1) tropospheric fields from 1000 to 100 mb, and 2) stratospheric analyses from 70 to 0.4 mb. The tropospheric fields are the 12 GMT gridded fields which are part of the Global Daily Assimilation System (GDAS), where data from radiosondes, aircraft, satellites, ships, bouys, or any other conventional means are assimilated and merged into meteorological fields (heights, temperature, winds). The stratospheric analyses are 12 GMT operational analyses at the 70 - 0.4 mb pressure levels produced from satellite temperature retrievals and RAOBS via a modified Cressman analysis. Tropospheric temperature analyses use combined NOAA-10 and NOAA-11 data. Moisture (northern hemisphere only) and Winds data are obtained from the NMC GDAS.\n\nThe gridded fields are on the standard 65 x 65 NMC polar stereographic grid oriented 80W (grid increment 381 km at 60N), and 100E (grid increment 381 km at 60S); Pole at (33,33). The NMC uses 18 standard pressure levels for data at 1000, 850, 700, 500, 400, 300, 250, 200, 150, 100, 70, 50, 30, 10, 5, 2, 1, 0.4 millibars. Height and temperature data are produced at all 18 pressure levels from 1000 mb to 0.4 mb. Moisture data are only produced in the northern hemisphere for the 6 lowest altitude pressure levels. Wind data are produced for the 12 lowest altitude levels in the northern hemisphere, and at the 4 levels 1000, 500, 300, and 250 mb in the southern hemisphere.\n\nThere are four data files representing each subtype per day. Included in the NMC correlative data set will be a geographical data richness file. This file is used by the NMC access routines, and indicates the radiosonde coverage for each point on the NMC grid. The data files are available in a binary record oriented format.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -59577,99 +59552,126 @@
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/UARZCNMC_001.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/UARZCNMC_001.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/UARS_Correlative_Level4/UARZCNMC/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/UARS_Correlative_Level4/UARZCNMC/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=UARZCNMC",
-                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=UARZCNMC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://uars.gsfc.nasa.gov/",
-                    "description": "The UARS Project Homepage.",
                     "@type": "dcat:Distribution",
+                    "description": "The UARS Project Homepage.",
+                    "downloadURL": "https://uars.gsfc.nasa.gov/",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/UARS_Correlative_Level4/UARZCNMC/doc/README.UARCorr.doc",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/UARS_Correlative_Level4/UARZCNMC/doc/README.UARCorr.doc",
+                    "mediaType": "application/msword",
                     "title": "View this dataset's read me document"
                 }
             ],
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Images/UARZCNMC_001.png",
+            "identifier": "C1273348496-GES_DISC",
+            "issued": "1991-09-12",
+            "keyword": [
+                "atmospheric winds",
+                "altitude",
+                "earth science",
+                "atmosphere",
+                "atmospheric water vapor",
+                "atmospheric temperature"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1273348496-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "1991-09-12",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "UARZCNMC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1991-09-12T00:00:00Z/2001-09-30T23:59:59.999Z",
             "theme": [
                 "UARS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "UARS Correlative NMC Daily Gridded Stratospheric Assimilated Data V001 (UARZCNMC) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-ROSINA-5-ESC1-V1.0",
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
+            "description": "This data set contains CODMAC\nlevel 5 science data acquired by the DFMS and RTOF ROSINA sensors\nbetween 2014-11-19 and 2015-03-10 during the Escort phase 1 of\nthe Rosetta mission at the comet 67P/CG.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rosina-5-esc1-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-ROSINA-5-ESC1-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rosina-5-esc1-v1.0",
-            "description": "This data set contains CODMAC\nlevel 5 science data acquired by the DFMS and RTOF ROSINA sensors\nbetween 2014-11-19 and 2015-03-10 during the Escort phase 1 of\nthe Rosetta mission at the comet 67P/CG.",
-            "title": "ROSETTA-ORBITER 67P ROSINA 5 ESC1 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P ROSINA 5 ESC1 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-EXT1-67PCHURYUMOV-M25-V2.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 1 mission phase, covering the period from 2016-01-12T23:25:00.000 to 2016-02-09T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after October 2018 PSA/PDS external peer review. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-ext1-67pchuryumov-m25-v2.0",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2021-05-21",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "67p/churyumov-gerasimenko 1 (1969 r1)",
                 "earth",
@@ -59677,655 +59679,667 @@
                 "vega",
                 "zeta cas"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-OSINAC-4-EXT1-67PCHURYUMOV-M25-V2.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-osinac-4-ext1-67pchuryumov-m25-v2.0",
-            "description": "This CODMAC level 4 data set contains radiometric calibrated and geometric distortion corrected (resampled) image data in W/m^2/sr/nm, acquired by the OSIRIS Narrow Angle Camera on the Rosetta spacecraft during the ROSETTA EXTENSION 1 mission phase, covering the period from 2016-01-12T23:25:00.000 to 2016-02-09T23:24:59.000. The prime target is comet 67P/Churyumov-Gerasimenko 1 (1969 R1). This version V2.0 supersedes previous deliveries of the same dataset with the following changes since the last version: Lien corrected dataset after October 2018 PSA/PDS external peer review. Updated documentation and ancillary files, added document on bandpass filter. Updated SCIENCE_USER_GUIDE_V03.PDF to include one section about FAQ and one section about image data quality. Added shutter backtravel and readout issues to image quality map. Updated DATA_QUALITY_ID keyword in image header. Improved handling of images with missing packets.",
-            "title": "ROSETTA-ORBITER 67P OSINAC 4 EXT1-MTP025 RDR V2.0",
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
+            "title": "ROSETTA-ORBITER 67P OSINAC 4 EXT1-MTP025 RDR V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1000000283-LARC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "The data used in this study were produced by the MISR Science Team;processed/stored at the Langley DAAC;Product is the MISR Level 2 TOA/Cloud Stereo parameters for the INTEX-B region;See ProductionDateTime for published Date.",
-            "issued": "2015-05-27",
-            "temporal": "2006-02-28T00:00:00Z/2006-04-03T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2015-05-27",
-            "keyword": [
-                "earth science",
-                "atmosphere",
-                "clouds"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "User Representative",
                 "hasEmail": "mailto:support-asdc@earthdata.nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "LaRC"
-            },
-            "identifier": "C1000000283-LARC",
             "description": "MISR Level 2 TOA/Cloud Stereo Product containing the Stereoscopically Derived Cloud Mask (SDCM), cloud winds, Reflecting Level Reference Altitude (RLRA), with associated data for the INTEXB_2006 theme.",
-            "title": "MISR L2 TOA/Cloud Stereo Product subset for the INTEX-B region V002",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C1000000283-LARC.html",
-                    "description": "View this dataset on the CMR (Common Metadata Repository)",
                     "@type": "dcat:Distribution",
+                    "description": "View this dataset on the CMR (Common Metadata Repository)",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/search/concepts/C1000000283-LARC.html",
+                    "mediaType": "text/html",
                     "title": "CMR"
                 }
             ],
+            "identifier": "C1000000283-LARC",
+            "issued": "2015-05-27",
+            "keyword": [
+                "earth science",
+                "atmosphere",
+                "clouds"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1000000283-LARC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2015-05-27",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LaRC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2006-02-28T00:00:00Z/2006-04-03T23:59:59Z",
             "theme": [
                 "INTEXB_2006",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MISR L2 TOA/Cloud Stereo Product subset for the INTEX-B region V002"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "026:00"
             ],
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1415263464-GES_DISC.html",
             "citation": "NASA Goddard Space Flight Center (GSFC). 2017-07-31. THIRN7L1BCLT. Version 001. THIR/Nimbus-7 Level 1 Cloud Data for SBUV/TOMS V001. Greenbelt, MD, USA. Archived by National Aeronautics and Space Administration, U.S. Government, Goddard Earth Sciences Data and Information Services Center (GES DISC). https://disc.gsfc.nasa.gov/datacollection/THIRN7L1BCLT_001.html. Digital Science Data.",
-            "issued": "2017-07-31",
-            "temporal": "1978-10-31T00:00:00Z/1984-10-28T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2017-07-31",
-            "keyword": [
-                "earth science",
-                "infrared wavelengths",
-                "spectral/engineering"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "JAMES JOHNSON",
                 "hasEmail": "mailto:James.Johnson@nasa.gov"
             },
+            "creator": "NASA Goddard Space Flight Center (GSFC)",
             "data-presentation-form": "Digital Science Data",
-            "identifier": "C1415263464-GES_DISC",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
-            },
             "description": "THIRN7L1BCLT is the Nimbus-7 Temperature-Humidity Infrared Radiometer (THIR) Level 1 Cloud Data for SBUV/TOMS (BCLT) product and contains total cloud amounts; radiances at three cloud altitudes: low (below 2km), middle (2 to 7 km depending on latitude), and height (above the middle cloud layer); cirrus and deep convective clouds; and mean and RMS deviations of cloud and surface radiances. Data are averaged orbit by orbit onto each of the Nimbus 7 TOMS IFOV, which vary from 50 km to 50 km at nadir to 200 km x 200 km at the edges, as well as SBUV 180 km x 180 km IFOVs. The BCLT product includes improved cloud estimation compared to the earlier CLT product.\n\nEach file contains one day of data (~14 orbits per day). Spatial coverage is global. The data are available from October 31, 1978 (day of year 304) through October 27, 1984 (day of year 301).\n\nThis product was previously available from the NSSDC with the identifier ESAD-00196 (old ID 78-098A-10E)",
-            "release-place": "Greenbelt, MD, USA",
-            "series-name": "THIRN7L1BCLT",
-            "creator": "NASA Goddard Space Flight Center (GSFC)",
-            "title": "THIR/Nimbus-7 Level 1 Cloud Data for SBUV/TOMS V001 (THIRN7L1BCLT) at GES DISC",
-            "graphic-preview-description": "Montage of mean radiance at mid-level (2-7 km) on 1 November 1978 for orbits 107 to 120",
-            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Nimbus/images/THIRN7_BCLT_Sample.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Nimbus/images/THIRN7_BCLT_Sample.png",
-                    "description": "Montage of mean radiance at mid-level (2-7 km) on 1 November 1978 for orbits 107 to 120",
                     "@type": "dcat:Distribution",
+                    "description": "Montage of mean radiance at mid-level (2-7 km) on 1 November 1978 for orbits 107 to 120",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Nimbus/images/THIRN7_BCLT_Sample.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/THIRN7L1BCLT_001.html",
-                    "description": "Access the dataset landing page from the GES DISC website.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the dataset landing page from the GES DISC website.",
+                    "downloadURL": "https://disc.gsfc.nasa.gov/datacollection/THIRN7L1BCLT_001.html",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus7_THIR_Level1/THIRN7L1BCLT.001/",
-                    "description": "Access the data via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "Access the data via HTTPS.",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus7_THIR_Level1/THIRN7L1BCLT.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=THIRN7L1BCLT",
-                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
                     "@type": "dcat:Distribution",
+                    "description": "Use the Earthdata Search Client to find and retrieve data sets across multiple data centers.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=THIRN7L1BCLT",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus7_THIR_Level1/THIRN7L1BCLT.001/doc/README.THIRN7L1BCLT.001.pdf",
-                    "description": "README Document",
                     "@type": "dcat:Distribution",
+                    "description": "README Document",
+                    "downloadURL": "https://acdisc.gesdisc.eosdis.nasa.gov/data/Nimbus7_THIR_Level1/THIRN7L1BCLT.001/doc/README.THIRN7L1BCLT.001.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's read me document"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/N7_Users_Guide.pdf",
-                    "description": "Nimbus 7 User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Nimbus 7 User's Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/N7_Users_Guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/N7THIRDataUserGuide_0582.pdf",
-                    "description": "Nimbus 7 THIR Data User's Guide",
                     "@type": "dcat:Distribution",
+                    "description": "Nimbus 7 THIR Data User's Guide",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.5_Product_Quality/N7THIRDataUserGuide_0582.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.2_Product_Rqmts_Design/THIR_TST343041_CLT.pdf",
-                    "description": "Nimbus 7 THIR (B)CLT Tape Specification Document",
                     "@type": "dcat:Distribution",
+                    "description": "Nimbus 7 THIR (B)CLT Tape Specification Document",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/repository/Mission/Nimbus/3.3_Product_Documentation/3.3.2_Product_Rqmts_Design/THIR_TST343041_CLT.pdf",
+                    "mediaType": "application/pdf",
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
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Nimbus/N7_THIR_Inventory.xlsx",
-                    "description": "N7 THIR Inventory",
                     "@type": "dcat:Distribution",
+                    "description": "N7 THIR Inventory",
+                    "downloadURL": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Nimbus/N7_THIR_Inventory.xlsx",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "graphic-preview-description": "Montage of mean radiance at mid-level (2-7 km) on 1 November 1978 for orbits 107 to 120",
+            "graphic-preview-file": "https://docserver.gesdisc.eosdis.nasa.gov/public/project/Nimbus/images/THIRN7_BCLT_Sample.png",
+            "identifier": "C1415263464-GES_DISC",
+            "issued": "2017-07-31",
+            "keyword": [
+                "earth science",
+                "infrared wavelengths",
+                "spectral/engineering"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C1415263464-GES_DISC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2017-07-31",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/GESDISC"
+            },
+            "release-place": "Greenbelt, MD, USA",
+            "series-name": "THIRN7L1BCLT",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "1978-10-31T00:00:00Z/1984-10-28T23:59:59.999Z",
             "theme": [
                 "Nimbus",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "THIR/Nimbus-7 Level 1 Cloud Data for SBUV/TOMS V001 (THIRN7L1BCLT) at GES DISC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1258-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-14T18:05:55.000 to 2015-12-14T20:01:38.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1258-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1258-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1258-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-12-14T18:05:55.000 to 2015-12-14T20:01:38.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1258 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1258 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1184",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Roberts, D.A., I. Numata, K.W. Holmes, G.T. Batista, T. Krug, A.L. Monteiro, R.L. Powell, and O.A. Chadwick. 2013. LBA-ECO ND-01 Primary Forests Land Cover Transition Maps, Rondonia, Brazil: 1975-1999. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/1184",
-            "issued": "2023-10-03",
-            "temporal": "1975-06-19T00:00:00Z/1999-10-16T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-12",
-            "keyword": [
-                "earth science",
-                "land surface",
-                "land use/land cover"
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
-            "identifier": "C2781575223-ORNL_CLOUD",
             "description": "This data set provides classified land cover transition images (maps) derived from Landsat Thematic Mapper (TM) and Multispectral Scanner (MSS) imagery for Ariquemes, Luiza, and Ji-Paranao areas in Rondonia, Brazil, at 30-m resolution. Images depict the age relative to the year 2000, of cleared land from the date the land was cut, to the date when primary forests transitioned into nonforest class (for example,  25 = cut by 1975, or 25 years before the year 2000). Temporal changes in three regions are represented by 31 TM scenes acquired between 1984 and 1999, and a pair of MSS scenes from 1975 and 1978. Data are provided as three GeoTiff (*.tif) images, one for each of the three areas.",
-            "graphic-preview-description": "Browse Image",
-            "title": "LBA-ECO ND-01 Primary Forests Land Cover Transition Maps, Rondonia, Brazil: 1975-1999",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1184_1_fit.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1184",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F1184",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/nutrient_dynamics/ND01_Age_Maps/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/lba/nutrient_dynamics/ND01_Age_Maps/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/LBA/guides/ND01_Age_Maps.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/LBA/guides/ND01_Age_Maps.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1184",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/1184",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/nutrient_dynamics/ND01_Age_Maps/comp/ND01_Age_Maps.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/lba/nutrient_dynamics/ND01_Age_Maps/comp/ND01_Age_Maps.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1184_1_fit.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/sdat-tds/1184_1_fit.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1184",
-                    "description": "Web Coverage Service for this collection.",
                     "@type": "dcat:Distribution",
+                    "description": "Web Coverage Service for this collection.",
+                    "downloadURL": "https://webmap.ornl.gov/wcsdown/dataset.jsp?ds_id=1184",
+                    "mediaType": "text/html",
                     "title": "Use Web Coverage Service (WCS) to download the dataset's data"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/sdat-tds/1184_1_fit.png",
+            "identifier": "C2781575223-ORNL_CLOUD",
+            "issued": "2023-10-03",
+            "keyword": [
+                "earth science",
+                "land surface",
+                "land use/land cover"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/1184",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-10-12",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-64.64 -12.43 -61.18 -9.18",
+            "temporal": "1975-06-19T00:00:00Z/1999-10-16T23:59:59Z",
             "theme": [
                 "LBA-ECO",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "LBA-ECO ND-01 Primary Forests Land Cover Transition Maps, Rondonia, Brazil: 1975-1999"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/TCSP/CRS/DATA101",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Heymsfield, Gerald M and Lin  Tian.2006. TCSP CLOUD RADAR SYSTEM (CRS) [indicate subset used]. Dataset available online from the NASA Global Hydrometeorology Resource Center DAAC, Huntsville, Alabama, U.S.A. DOI: http://dx.doi.org/10.5067/TCSP/CRS/DATA101",
-            "issued": "2006-04-07",
-            "temporal": "2005-07-05T18:27:59Z/2005-07-27T10:49:32Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-04-28",
-            "keyword": [
-                "radar",
-                "spectral/engineering",
-                "earth science"
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
-            "identifier": "C1979948526-GHRC_DAAC",
             "description": "The TCSP Cloud Radar System (CRS) datasets consists of vertically profiled reflectivity and Doppler velocity at aircraft nadir along the flight track. The CRS is a 94 GHz (W-band; 3 mm wavelength) Doppler radar developed for autonomous operation in the NASA ER-2 high-altitude aircraft and for ground-based operation. It provided high-resolution profiles of reflectivity and Doppler velocity in clouds and it has important applications to atmospheric remote sensing studies. The CRS was designed to fly with the Cloud Lidar System (CLS), in the tail cone of an ER-2 superpod. There are two basic modes of operation of the CRS: 1) ER-2 with reflectivity, Doppler, and linear-depolarization measurements, and 2) ground-based with full polarimetric capability. The Tropical Cloud Systems and Processes (TCSP) mission used the ER-2 mode. The TCSP mission collected data for research and documentation of cyclogenesis, the interaction of temperature, humidity, precipitation, wind and air pressure that creates ideal birthing conditions for tropical storms, hurricanes and related phenomena. The goal of this mission was to help us better understand how hurricanes and other tropical storms are formed and intensify.",
-            "graphic-preview-description": "N/A",
-            "title": "TCSP CLOUD RADAR SYSTEM (CRS) V1",
-            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/tcsp/crs/browse/",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTCSP%2FCRS%2FDATA101",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FTCSP%2FCRS%2FDATA101",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=tcspcrs",
-                    "description": "Files may be downloaded directly to your workstation from this link",
                     "@type": "dcat:Distribution",
+                    "description": "Files may be downloaded directly to your workstation from this link",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=tcspcrs",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/tcsp/crs/browse/crs_050715_1005-1041_v1_merge.gif",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/tcsp/crs/browse/crs_050715_1005-1041_v1_merge.gif",
+                    "mediaType": "image/gif",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "image/gif",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/tcsp/crs/browse/crs_050715_0859-0923_v1.gif",
-                    "description": "Sample browse image",
                     "@type": "dcat:Distribution",
+                    "description": "Sample browse image",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/tcsp/crs/browse/crs_050715_0859-0923_v1.gif",
+                    "mediaType": "image/gif",
                     "title": "Get a related visualization"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/tcsp/tcspcrs/tcspcrs_dataset.html",
-                    "description": "The guide document contains detailed information about the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The guide document contains detailed information about the dataset",
+                    "downloadURL": "http://ghrc.nsstc.nasa.gov/uso/ds_docs/tcsp/tcspcrs/tcspcrs_dataset.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/tcsp/tcspcrs/UF-IDL.guide.txt",
-                    "description": "UF-IDL guide",
                     "@type": "dcat:Distribution",
+                    "description": "UF-IDL guide",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/tcsp/tcspcrs/UF-IDL.guide.txt",
+                    "mediaType": "text/html",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/tcsp/tcspcrs/ASCII-README.txt",
-                    "description": "Preliminary radar reflectivity dataset measured by NASA Goddard Space Flight Center ER-2 Doppler Radar and Cloud Radar System",
                     "@type": "dcat:Distribution",
+                    "description": "Preliminary radar reflectivity dataset measured by NASA Goddard Space Flight Center ER-2 Doppler Radar and Cloud Radar System",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/tcsp/tcspcrs/ASCII-README.txt",
+                    "mediaType": "text/html",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/tcsp/tcspcrs/formatspec_2_0.pdf",
-                    "description": "ASCII File Format Specification for Data Exchange",
                     "@type": "dcat:Distribution",
+                    "description": "ASCII File Format Specification for Data Exchange",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/tcsp/tcspcrs/formatspec_2_0.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/tcsp/tcspcrs/CRS-UF.txt",
-                    "description": "UNIVERSAL FORMAT FOR EDOP DATA",
                     "@type": "dcat:Distribution",
+                    "description": "UNIVERSAL FORMAT FOR EDOP DATA",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/tcsp/tcspcrs/CRS-UF.txt",
+                    "mediaType": "text/html",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "application/x-tar",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/tcsp/tcspcrs/software.tar",
-                    "description": "tcspcrs software (TAR)",
                     "@type": "dcat:Distribution",
+                    "description": "tcspcrs software (TAR)",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/doc/tcsp/tcspcrs/software.tar",
+                    "mediaType": "application/x-tar",
                     "title": "Downloadable software applications"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/TCSP",
-                    "description": "The home page for the project or program which sponsored the dataset",
                     "@type": "dcat:Distribution",
+                    "description": "The home page for the project or program which sponsored the dataset",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/home/field-campaigns/TCSP",
+                    "mediaType": "text/html",
                     "title": "The dataset's project home page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/tcsp/crs/browse/",
-                    "description": "N/A",
                     "@type": "dcat:Distribution",
+                    "description": "N/A",
+                    "downloadURL": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/tcsp/crs/browse/",
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
+            "graphic-preview-file": "https://ghrc.nsstc.nasa.gov/pub/fieldCampaigns/tcsp/crs/browse/",
+            "identifier": "C1979948526-GHRC_DAAC",
+            "issued": "2006-04-07",
+            "keyword": [
+                "radar",
+                "spectral/engineering",
+                "earth science"
+            ],
+            "landingPage": "https://doi.org/10.5067/TCSP/CRS/DATA101",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-04-28",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/MSFC/GHRC"
+            },
             "spatial": "-97.247 4.697 -66.343 21.939",
+            "temporal": "2005-07-05T18:27:59Z/2005-07-27T10:49:32Z",
             "theme": [
                 "TCSP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "TCSP CLOUD RADAR SYSTEM (CRS) V1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/14",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Lutz, R. J. 1994. Atmos[pheric]. Profile: St[andar]d. Press[ure]. Level (FIFE). Data set. Available on-line [http://www.daac.ornl.gov] from Oak Ridge National Laboratory Distributed Active Archive Center, Oak Ridge, Tennessee, U.S.A. Also published in D. E. Strebel, D. R. Landis, K. F. Huemmrich, and B. W. Meeson (eds.), Collected Data of the First ISLSCP Field Experiment, Vol. 1: Surface Observations and Non-Image Data Sets. CD-ROM. National Aeronautics and Space Administration, Goddard Space Flight Center, Greenbelt, Maryland, U.S.A. (available from http://www.daac.ornl.gov). doi:10.3334/ORNLDAAC/14",
-            "issued": "2024-05-03",
-            "temporal": "1987-05-26T00:00:00Z/1989-08-12T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-06",
-            "keyword": [
-                "earth science",
-                "atmospheric pressure",
-                "atmosphere",
-                "atmospheric temperature",
-                "atmospheric winds"
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
-            "identifier": "C2978502225-ORNL_CLOUD",
             "description": "Derived (5mb interval) radiosonde observations from Wilf Brutsaert's data",
-            "graphic-preview-description": "Browse Image",
-            "title": "Atmos. Profile: Std. Press. Level (FIFE)",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/fife_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F14",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F14",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/fife_atmos_brut_drv/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/fife/fife_atmos_brut_drv/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/FIFE/guides/brut_sonde_atm_derived.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/FIFE/guides/brut_sonde_atm_derived.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/14",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/14",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/msword",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_atmos_brut_drv/comp/brut_drv.doc",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_atmos_brut_drv/comp/brut_drv.doc",
+                    "mediaType": "application/msword",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_atmos_brut_drv/comp/brut_drv.tdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_atmos_brut_drv/comp/brut_drv.tdf",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_atmos_brut_drv/comp/brut_sonde_atm_derived.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fife/fife_atmos_brut_drv/comp/brut_sonde_atm_derived.pdf",
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
+            "identifier": "C2978502225-ORNL_CLOUD",
+            "issued": "2024-05-03",
+            "keyword": [
+                "earth science",
+                "atmospheric pressure",
+                "atmosphere",
+                "atmospheric temperature",
+                "atmospheric winds"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/14",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-05-06",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "39.12 -96.56",
+            "temporal": "1987-05-26T00:00:00Z/1989-08-12T23:59:59Z",
             "theme": [
                 "FIFE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Atmos. Profile: Std. Press. Level (FIFE)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://techport.nasa.gov/view/10986",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2014-06-01",
-            "temporal": "2014-06-01T00:00:00Z/2017-05-01T00:00:00Z",
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
                 "fn": "George Komar",
                 "hasEmail": "mailto:george.komar@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Science Mission Directorate"
-            },
-            "identifier": "TECHPORT_10986",
             "description": "&lt;p&gt;\r\n\tN/A&lt;/p&gt;",
-            "title": "Enhancement, Demonstration, and Validation of the Wideband Instrument for Snow Measurements (WISM) Project",
-            "programCode": [
-                "026:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "http://techport.nasa.gov/xml-api/10986",
                     "mediaType": "application/xml"
                 }
-            ]
+            ],
+            "identifier": "TECHPORT_10986",
+            "issued": "2014-06-01",
+            "keyword": [
+                "nasa headquarters",
+                "project",
+                "active"
+            ],
+            "landingPage": "http://techport.nasa.gov/view/10986",
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
+            "temporal": "2014-06-01T00:00:00Z/2017-05-01T00:00:00Z",
+            "title": "Enhancement, Demonstration, and Validation of the Wideband Instrument for Snow Measurements (WISM) Project"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-J-MAG-4-1.92SEC",
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
-                "voyager",
-                "jupiter"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set includes Voyager 1 Jupiter encounter magnetometer data that have been resampled at a 1.92 second sample rate. The data set is composed of 6 columns: 1) ctime - this column contains the data acquisition time. The time is always output in the ISO standard spacecraft event time format (yyyy-mm-dd-Thh:mm:ss.sss) but is stored internally in Cline time which is measured in seconds after 00:00:00.000 Jan 01, 1966, 2) br - this column contains the radial component of the magnetic field, 3) bphi - this column contains the phi component of the magnetic field, 4) btheta - this column contains the theta component of the magnetic field, 5) bmag - this column contains the magnitude of the magnetic field, 6) flag - a flag value that indicates either software error or spacecraft hardware interference reduced confidence in this record (flag value of 1 is bad , 0 is good or unchecked). All magnetic field observations are measured in nanoTeslas. The coordinate system for this dataset is Minus System III. All of the magnetic field data are calibrated (see the instrument calibration description for more details). The Jupiter System III coordinate system is defined in Dessler 1983 and the reference documents for this dataset are: Ness et al, 1979 Lepping et al, 1981 Connerney,Acuna,Ness, 1981 Behannon,Burlaga,Ness, 1981",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-j-mag-4-1.92sec_32yv-nakb",
+            "issued": "2021-05-21",
+            "keyword": [
+                "voyager",
+                "jupiter"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=VG1-J-MAG-4-1.92SEC",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.vg1-j-mag-4-1.92sec_32yv-nakb",
-            "description": "This data set includes Voyager 1 Jupiter encounter magnetometer data that have been resampled at a 1.92 second sample rate. The data set is composed of 6 columns: 1) ctime - this column contains the data acquisition time. The time is always output in the ISO standard spacecraft event time format (yyyy-mm-dd-Thh:mm:ss.sss) but is stored internally in Cline time which is measured in seconds after 00:00:00.000 Jan 01, 1966, 2) br - this column contains the radial component of the magnetic field, 3) bphi - this column contains the phi component of the magnetic field, 4) btheta - this column contains the theta component of the magnetic field, 5) bmag - this column contains the magnitude of the magnetic field, 6) flag - a flag value that indicates either software error or spacecraft hardware interference reduced confidence in this record (flag value of 1 is bad , 0 is good or unchecked). All magnetic field observations are measured in nanoTeslas. The coordinate system for this dataset is Minus System III. All of the magnetic field data are calibrated (see the instrument calibration description for more details). The Jupiter System III coordinate system is defined in Dessler 1983 and the reference documents for this dataset are: Ness et al, 1979 Lepping et al, 1981 Connerney,Acuna,Ness, 1981 Behannon,Burlaga,Ness, 1981",
-            "title": "VOYAGER 1 JUPITER MAGNETOMETER RESAMPLED DATA 1.92 SEC",
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
+            "title": "VOYAGER 1 JUPITER MAGNETOMETER RESAMPLED DATA 1.92 SEC"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.nasa.gov/mission_pages/station/expeditions/expedition30/index.html",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brian Dunbar",
+                "hasEmail": "mailto:brian.dunbar@nasa.gov"
+            },
+            "description": "Press kit for ISS mission Expedition 30 from 11/2011-07/2012. Press kits contain information about each mission overview, crew, mission timeline, benefits, and media contact information.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "Press Kit PDF",
+                    "downloadURL": "http://www.nasa.gov/pdf/605284main_Expedition_30_31_Press_Kit.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "ISS 30 Press Kit"
+                }
+            ],
+            "identifier": "OCIO-Fitara-40",
             "issued": "2012-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "crew",
                 "launch",
@@ -60338,139 +60352,104 @@
                 "schedule",
                 "30"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Brian Dunbar",
-                "hasEmail": "mailto:brian.dunbar@nasa.gov"
-            },
+            "landingPage": "http://www.nasa.gov/mission_pages/station/expeditions/expedition30/index.html",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:037"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "JSC"
             },
-            "identifier": "OCIO-Fitara-40",
-            "description": "Press kit for ISS mission Expedition 30 from 11/2011-07/2012. Press kits contain information about each mission overview, crew, mission timeline, benefits, and media contact information.",
-            "title": "ISS Expedition 30 Press Kit",
-            "programCode": [
-                "026:037"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "http://www.nasa.gov/pdf/605284main_Expedition_30_31_Press_Kit.pdf",
-                    "description": "Press Kit PDF",
-                    "@type": "dcat:Distribution",
-                    "title": "ISS 30 Press Kit"
-                }
-            ],
-            "accrualPeriodicity": "irregular"
+            "title": "ISS Expedition 30 Press Kit"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ODY-M-GRS-5-SGS-V1.0",
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
+            "description": "The ODY MARS GAMMA RAY SPECTROMETER 5 SGS (SGS) data set is a collection of data tables that contain a gamma spectrum and the associated engineering data that has been summed over 5-degree by 5-degree latitude longitude cells on the surface of Mars and over a time period of 15 degrees of solar longitude (Ls). The SGS are produced because the individual gamma spectra collected during an approximately 19.7 second collection interval do not contain enough counts to be statistically significant. The SGS are summed over large enough and long enough spatial and temporal intervals to provide a statistically meaningful spectrum that can be used for scientific data analysis.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ody-m-grs-5-sgs-v1.0_332w-d3m7",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "2001 mars odyssey"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=ODY-M-GRS-5-SGS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ody-m-grs-5-sgs-v1.0_332w-d3m7",
-            "description": "The ODY MARS GAMMA RAY SPECTROMETER 5 SGS (SGS) data set is a collection of data tables that contain a gamma spectrum and the associated engineering data that has been summed over 5-degree by 5-degree latitude longitude cells on the surface of Mars and over a time period of 15 degrees of solar longitude (Ls). The SGS are produced because the individual gamma spectra collected during an approximately 19.7 second collection interval do not contain enough counts to be statistically significant. The SGS are summed over large enough and long enough spatial and temporal intervals to provide a statistically meaningful spectrum that can be used for scientific data analysis.",
-            "title": "ODY MARS GAMMA RAY SPECTROMETER 5 SGS V1.0",
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
+            "title": "ODY MARS GAMMA RAY SPECTROMETER 5 SGS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aorex.ovirs&version=9.0",
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
-                "origins spectral interpretation resource identification security regolith explorer (osiris-rex)",
-                "(101955) bennu"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This bundle collects all the operational data products produced by the OSIRIS-REx Visible and InfraRed Spectrometer (OVIRS). OVIRS is used for the spectral characterization of the surface of (101955) Bennu.",
+            "identifier": "urn:nasa:pds:orex.ovirs",
+            "issued": "2021-05-21",
+            "keyword": [
+                "origins spectral interpretation resource identification security regolith explorer (osiris-rex)",
+                "(101955) bennu"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewBundle.jsp?identifier=urn%3Anasa%3Apds%3Aorex.ovirs&version=9.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:orex.ovirs",
-            "description": "This bundle collects all the operational data products produced by the OSIRIS-REx Visible and InfraRed Spectrometer (OVIRS). OVIRS is used for the spectral characterization of the surface of (101955) Bennu.",
-            "title": "Origins, Spectral Interpretation, Resource Identification, Security, Regolith Explorer (OSIRIS-REx): Visible and InfraRed Spectrometer (OVIRS) Bundle",
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
+            "title": "Origins, Spectral Interpretation, Resource Identification, Security, Regolith Explorer (OSIRIS-REx): Visible and InfraRed Spectrometer (OVIRS) Bundle"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/338d-fuyt",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "temporal": "1973-01-01/1974-01-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "planetary science",
-                "space science",
-                "geography",
-                "saturn",
-                "imagery",
-                "planetary missions"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Site Admin",
                 "hasEmail": "mailto:seseinfo@asu.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "NASA-0000075",
             "description": "The Mariner 10 Image Archive includes tools to view shaded relief maps of the surface of Mercury, a 3D globe, and all images acquired by NASA's Mariner 10 mission.",
-            "title": "Mariner 10 Image Archive",
-            "programCode": [
-                "026:046"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -60478,174 +60457,175 @@
                     "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-0000075",
+            "issued": "2018-06-25",
+            "keyword": [
+                "planetary science",
+                "space science",
+                "geography",
+                "saturn",
+                "imagery",
+                "planetary missions"
+            ],
+            "landingPage": "https://data.nasa.gov/d/338d-fuyt",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:046"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
+            "temporal": "1973-01-01/1974-01-01",
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "Mariner 10 Image Archive"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SeaBASS/PAC_DFO_PAR_BUOY/DATA001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC. https://doi.org/10.5067/SeaBASS/PAC_DFO_PAR_BUOY/DATA001.",
-            "issued": "1998-05-23",
-            "temporal": "1998-05-05T00:00:00Z/2023-04-17T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-06",
-            "keyword": [
-                "salinity/density",
-                "earth science",
-                "ocean chemistry",
-                "ocean temperature",
-                "ocean optics",
-                "oceans"
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
-            "identifier": "C1633360580-OB_DAAC",
             "description": "Optical sensors were added to some of the 17 meteorological ODAS (Ocean Data Acquisition System) buoys which provide weather and ocean data along and off the west coast of Canada for the Environment (EC) and the Fisheries and Ocean departments (DFO) of the Canadian federal government. This dataset includes Photosynthetically Active Radiation (PAR) data from two locations: Halibut Bank (buoy code 46146) and Saanich Inlet near the Institute of Ocean Sciences (buoy code 46134). For additional information please refer to Gower et al., 1999 (DOI:10.1109/OCEANS.1999.800169)",
-            "title": "PAR data from buoys along the west coast of Canada",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FPAC_DFO_PAR_BUOY%2FDATA001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSeaBASS%2FPAC_DFO_PAR_BUOY%2FDATA001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/PAC_DFO_PAR_BUOY/",
-                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
                     "@type": "dcat:Distribution",
+                    "description": "Detailed information about the SeaBASS Experiment such as cruises, funding, and investigators",
+                    "downloadURL": "https://seabass.gsfc.nasa.gov/experiment/PAC_DFO_PAR_BUOY/",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1633360580-OB_DAAC",
+            "issued": "1998-05-23",
+            "keyword": [
+                "salinity/density",
+                "earth science",
+                "ocean chemistry",
+                "ocean temperature",
+                "ocean optics",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/SeaBASS/PAC_DFO_PAR_BUOY/DATA001",
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
+            "temporal": "1998-05-05T00:00:00Z/2023-04-17T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "PAR data from buoys along the west coast of Canada"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=A12A-L-SWS-4-SOLAR-WIND-1HR-AVG-V1.0",
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
-                "apollo 12",
-                "moon"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains tables of time ordered, hourly-averaged plasma parameters, mainly of the solar wind, as observed on the Moon at the Apollo 12 ALSEP site by the Apollo 12 Solar Wind Spectrometer from 19 November 1969 through 25 March 1976.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.a12a-l-sws-4-solar-wind-1hr-avg-v1.0_33cq-kgdz",
+            "issued": "2018-06-26",
+            "keyword": [
+                "apollo 12",
+                "moon"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=A12A-L-SWS-4-SOLAR-WIND-1HR-AVG-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.a12a-l-sws-4-solar-wind-1hr-avg-v1.0_33cq-kgdz",
-            "description": "This data set contains tables of time ordered, hourly-averaged plasma parameters, mainly of the solar wind, as observed on the Moon at the Apollo 12 ALSEP site by the Apollo 12 Solar Wind Spectrometer from 19 November 1969 through 25 March 1976.",
-            "title": "APOLLO 12 ALSEP/SWS SOLAR WIND 1-HR AVG TABLES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "APOLLO 12 ALSEP/SWS SOLAR WIND 1-HR AVG TABLES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-CAL-MRI-2-NAV-9P-CRUISE-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains raw calibration and test images acquired by the Deep Impact Medium Resolution Instrument Visible CCD during the cruise phase of the mission. These observations were used for optical and autonomous navigation (NAV) of the flyby spacecraft. These data were collected from 14 January to 25 April 2005. Test images of comet 9P/Tempel 1 were acquired on 25 April.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-cal-mri-2-nav-9p-cruise-v1.0_33d3-uvs8",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "9p/tempel 1 (1867 g1)",
                 "calibration",
                 "deep impact"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=DIF-CAL-MRI-2-NAV-9P-CRUISE-V1.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.dif-cal-mri-2-nav-9p-cruise-v1.0_33d3-uvs8",
-            "description": "This data set contains raw calibration and test images acquired by the Deep Impact Medium Resolution Instrument Visible CCD during the cruise phase of the mission. These observations were used for optical and autonomous navigation (NAV) of the flyby spacecraft. These data were collected from 14 January to 25 April 2005. Test images of comet 9P/Tempel 1 were acquired on 25 April.",
-            "title": "DEEP IMPACT 9P/TEMPEL CRUISE - RAW MRI NAV IMAGES V1.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "DEEP IMPACT 9P/TEMPEL CRUISE - RAW MRI NAV IMAGES V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/33d4-txfa",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
-            "issued": "2018-06-25",
-            "temporal": "1970-01-01/1970-12-31",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
-            "keyword": [
-                "planetary science",
-                "earth",
-                "geography",
-                "space science",
-                "orbital mechanics"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Site Admin",
                 "hasEmail": "mailto:rpif@lpi.usra.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Aeronautics and Space Administration"
-            },
-            "identifier": "NASA-0000076",
             "description": "The Mars Maps Catalog includes various mappings of the surface of Mars.",
-            "title": "Mars Map Catalog",
-            "programCode": [
-                "026:046"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -60653,317 +60633,351 @@
                     "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
+            "identifier": "NASA-0000076",
+            "issued": "2018-06-25",
+            "keyword": [
+                "planetary science",
+                "earth",
+                "geography",
+                "space science",
+                "orbital mechanics"
+            ],
+            "landingPage": "https://data.nasa.gov/d/33d4-txfa",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:046"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Aeronautics and Space Administration"
+            },
+            "temporal": "1970-01-01/1970-12-31",
             "theme": [
                 "Management/Operations"
-            ]
+            ],
+            "title": "Mars Map Catalog"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/VIIRS/AERDB_L2_VIIRS_SNPP.002",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "NASA VIIRS Atmosphere SIPS. 2023-01-16. VIIRS Deep Blue Level-3 Daily Aerosol Data 1x1 degree grid . Version 2.0. MODAPS at NASA/GSFC. Archived by National Aeronautics and Space Administration, U.S. Government, L1 and Atmosphere Archive and Distribution System (LAADS). https://doi.org/10.5067/VIIRS/AERDB_L2_VIIRS_SNPP.002. https://doi.org/10.5067/VIIRS/AERDB_L2_VIIRS_SNPP.002.",
-            "issued": "2023-01-01",
-            "temporal": "2012-03-01T00:00:00Z/2024-09-30T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-25",
-            "keyword": [
-                "atmosphere",
-                "earth science",
-                "aerosols"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:sips.support@ssec.wisc.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Not provided"
-            },
-            "identifier": "C2600303218-LAADS",
-            "description": "The VIIRS/SNPP Deep Blue Aerosol L2 6-Min Swath 6 km product from the Visible Infrared Imaging Radiometer Suite (VIIRS) determines atmospheric aerosol loading for daytime cloud-free snow-free scenes. This orbit-level product (Short-name: AERDB_L2_VIIRS_SNPP) has an at-nadir resolution of 6 km x 6 km, and progressively increases away from nadir given the sensor\u2019s scanning geometry and Earth\u2019s curvature.  Viewed differently, this product\u2019s resolution accommodates 8 x 8 native VIIRS moderate-resolution (M-band) pixels that nominally have ~750 m horizontal pixel size.  The L2 Deep Blue AOT data products, at 550 nanometers reference wavelengths, are derived from particular VIIRS bands using two primary AOT retrieval algorithms: Deep Blue algorithm over land, and the Satellite Ocean Aerosol Retrieval (SOAR) algorithm over ocean.  Although this product is called Deep Blue based on retrievals for the land algorithm, the data includes over-water retrievals as well.\r\n\r\nThis L2 description pertains to the VIIRS Deep Blue Aerosol collection version 2.0 (C2) product. Significant changes have been made to the V2.0 Deep Blue/SOAR algorithms to further improve the data quality. For C2.0, the aerosol products are available for NOAA20 VIIRS in addition to SNPP. Some  of changes in the retrieval algorithms and data products include, new SDS suite for prognostic uncertainties of 550 nm AOT over both land and ocean is added, surface pressure is better accounted for for both over-land and over-ocean retrievals by adding surface pressure nodes in the aerosol lookup table, and a number of other improvements which can be found from Product page at:\r\nhttps://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/products/AERDB_L2_VIIRS_SNPP\r\n\r\nFor more information consult Deep Blue aerosol team Page at: \r\nhttps://deepblue.gsfc.nasa.gov",
-            "release-place": "MODAPS at NASA/GSFC",
             "creator": "NASA VIIRS Atmosphere SIPS",
-            "title": "VIIRS/SNPP Deep Blue Aerosol L2 6 Min Swath 6km",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The VIIRS/SNPP Deep Blue Aerosol L2 6-Min Swath 6 km product from the Visible Infrared Imaging Radiometer Suite (VIIRS) determines atmospheric aerosol loading for daytime cloud-free snow-free scenes. This orbit-level product (Short-name: AERDB_L2_VIIRS_SNPP) has an at-nadir resolution of 6 km x 6 km, and progressively increases away from nadir given the sensor\u2019s scanning geometry and Earth\u2019s curvature.  Viewed differently, this product\u2019s resolution accommodates 8 x 8 native VIIRS moderate-resolution (M-band) pixels that nominally have ~750 m horizontal pixel size.  The L2 Deep Blue AOT data products, at 550 nanometers reference wavelengths, are derived from particular VIIRS bands using two primary AOT retrieval algorithms: Deep Blue algorithm over land, and the Satellite Ocean Aerosol Retrieval (SOAR) algorithm over ocean.  Although this product is called Deep Blue based on retrievals for the land algorithm, the data includes over-water retrievals as well.\r\n\r\nThis L2 description pertains to the VIIRS Deep Blue Aerosol collection version 2.0 (C2) product. Significant changes have been made to the V2.0 Deep Blue/SOAR algorithms to further improve the data quality. For C2.0, the aerosol products are available for NOAA20 VIIRS in addition to SNPP. Some  of changes in the retrieval algorithms and data products include, new SDS suite for prognostic uncertainties of 550 nm AOT over both land and ocean is added, surface pressure is better accounted for for both over-land and over-ocean retrievals by adding surface pressure nodes in the aerosol lookup table, and a number of other improvements which can be found from Product page at:\r\nhttps://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/products/AERDB_L2_VIIRS_SNPP\r\n\r\nFor more information consult Deep Blue aerosol team Page at: \r\nhttps://deepblue.gsfc.nasa.gov",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FAERDB_L2_VIIRS_SNPP.002",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FVIIRS%2FAERDB_L2_VIIRS_SNPP.002",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://deepblue.gsfc.nasa.gov/science",
-                    "description": "The Deep Blue algorithm",
                     "@type": "dcat:Distribution",
+                    "description": "The Deep Blue algorithm",
+                    "downloadURL": "https://deepblue.gsfc.nasa.gov/science",
+                    "mediaType": "text/html",
                     "title": "View the primary investigator's documentation for this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/AERDB_L2_VIIRS_SNPP--5200",
-                    "description": "Search and order VIIRS Level 2 Aerosol product from LAADS website.",
                     "@type": "dcat:Distribution",
+                    "description": "Search and order VIIRS Level 2 Aerosol product from LAADS website.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/search/order/2/AERDB_L2_VIIRS_SNPP--5200",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through LAADS"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/5200/AERDB_L2_VIIRS_SNPP/",
-                    "description": "Direct access to LAADS archive for AERDB_L2_VIIRS_SNPP data.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct access to LAADS archive for AERDB_L2_VIIRS_SNPP data.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/5200/AERDB_L2_VIIRS_SNPP/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/VIIRS/AERDB_L2_VIIRS_SNPP.002",
-                    "description": "Product DOI landing page",
                     "@type": "dcat:Distribution",
+                    "description": "Product DOI landing page",
+                    "downloadURL": "https://doi.org/10.5067/VIIRS/AERDB_L2_VIIRS_SNPP.002",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/api/v2/content/archives/Document%20Archive/Science%20Data%20Product%20Documentation/VIIRS_Deep_Blue_Aerosol_User_Guide_v2.pdf",
-                    "description": "VIIRS Aerosol User\u2019s Guide",
                     "@type": "dcat:Distribution",
+                    "description": "VIIRS Aerosol User\u2019s Guide",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/api/v2/content/archives/Document%20Archive/Science%20Data%20Product%20Documentation/VIIRS_Deep_Blue_Aerosol_User_Guide_v2.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/5111/AERDB_L2_VIIRS_SNPP/contents.html",
-                    "description": "Access to OPeNDAP archive",
                     "@type": "dcat:Distribution",
+                    "description": "Access to OPeNDAP archive",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/opendap/RemoteResources/laads/allData/5111/AERDB_L2_VIIRS_SNPP/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/viirs/SNPP-VIIRS_DB_Aerosol_ATBD.pdf",
-                    "description": "A link to product ATBD",
                     "@type": "dcat:Distribution",
+                    "description": "A link to product ATBD",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/missions-and-measurements/viirs/SNPP-VIIRS_DB_Aerosol_ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 }
             ],
+            "identifier": "C2600303218-LAADS",
+            "issued": "2023-01-01",
+            "keyword": [
+                "atmosphere",
+                "earth science",
+                "aerosols"
+            ],
+            "landingPage": "https://doi.org/10.5067/VIIRS/AERDB_L2_VIIRS_SNPP.002",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2024-09-25",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Not provided"
+            },
+            "release-place": "MODAPS at NASA/GSFC",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2012-03-01T00:00:00Z/2024-09-30T00:00:00Z",
             "theme": [
                 "Suomi-NPP",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VIIRS/SNPP Deep Blue Aerosol L2 6 Min Swath 6km"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0034",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "2000-04-07. Archived by National Aeronautics and Space Administration, U.S. Government, NASA/LARC/SD/ASDC. https://doi.org/10.5067/ASDC_DAAC/FIRE/0034.",
-            "issued": "2000-03-17",
-            "temporal": "1992-06-01T00:00:00Z/1992-06-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2018-07-10",
-            "keyword": [
-                "atmospheric temperature",
-                "visible wavelengths",
-                "spectral/engineering",
-                "infrared wavelengths",
-                "earth science",
-                "clouds",
-                "atmospheric radiation",
-                "atmospheric pressure",
-                "atmosphere"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "WILLIAM ROSSOW",
                 "hasEmail": "mailto:wbrossow@ccny.cuny.edu"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "NASA/LARC/SD/ASDC"
-            },
-            "identifier": "C1000000999-LARC_ASDC",
             "description": "The First ISCCP Regional Experiments have been designed to improve data products and cloud/radiation parameterizations used in general circulation models (GCMs). Specifically, the goals of FIRE are (1) to improve the basic understanding of the interaction of physical processes in determining life cycles of cirrus and marine stratocumulus systems and the radiative properties of these clouds during their life cycles and (2) to investigate the interrelationships between the ISCCP data, GCM parameterizations, and higher space and time resolution cloud data. To-date, four intensive field-observation periods were planned and executed: a cirrus IFO (October 13 - November 2, 1986); a marine stratocumulus IFO off the southwestern coast of California (June 29 - July 20, 1987); a second cirrus IFO in southeastern Kansas (November 13 - December 7, 1991); and a second marine stratocumulus IFO in the eastern North Atlantic Ocean (June 1 - June 28, 1992). Each mission combined coordinated satellite, airborne, and surface observations with modeling studies to investigate the cloud properties and physical processes of the cloud systems.A subset of the ISCCP Stage DX Cloud Product (Revised Algorithm) are included for the FIRE ASTEX region.",
-            "title": "First ISCCP Regional Experiment (FIRE) Atlantic Stratocumulus Transition Experiment (ASTEX) ISCCP DX Cloud Product - Revised Algorithm Data",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0034",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FASDC_DAAC%2FFIRE%2F0034",
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
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000999-LARC_ASDC",
-                    "description": "Earthdata Search for FIRE_AX_ISCCP_DX_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search for FIRE_AX_ISCCP_DX_1 (NASA Application to search, discover, visualize, refine, and access NASA Earth Observation data)",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1000000999-LARC_ASDC",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fire_isccp_dx_read.f",
-                    "description": "Subroutines to read DX data from a DX file - Direct File Download (.f)",
                     "@type": "dcat:Distribution",
+                    "description": "Subroutines to read DX data from a DX file - Direct File Download (.f)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/read_software/fire_isccp_dx_read.f",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_isccp_dx_dataset.pdf",
-                    "description": "FIRE International Satellite Cloud Climatology Project (ISCCP) DX Cloud Product - Revised Algorithm",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE International Satellite Cloud Climatology Project (ISCCP) DX Cloud Product - Revised Algorithm",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/guide/base_fire_isccp_dx_dataset.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/postscript",
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ax_isccp_dx_part2.ps",
-                    "description": "FIRE ASTEX sample read software and data files - Direct File Download (.ps)",
                     "@type": "dcat:Distribution",
+                    "description": "FIRE ASTEX sample read software and data files - Direct File Download (.ps)",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ax_isccp_dx_part2.ps",
+                    "mediaType": "application/postscript",
                     "title": "View this dataset's science data product software documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0034",
-                    "description": "DOI data set landing page for FIRE_AX_ISCCP_DX_1",
                     "@type": "dcat:Distribution",
+                    "description": "DOI data set landing page for FIRE_AX_ISCCP_DX_1",
+                    "downloadURL": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0034",
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ax_isccp_dx_part1",
-                    "description": "Description of Tapes Created for the ASTEX Project Readme",
                     "@type": "dcat:Distribution",
+                    "description": "Description of Tapes Created for the ASTEX Project Readme",
+                    "downloadURL": "https://asdc.larc.nasa.gov/documents/fire/readme/readme_fire_ax_isccp_dx_part1",
+                    "mediaType": "text/html",
                     "title": "View this dataset's read me document"
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
-                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_AX_ISCCP_DX/",
-                    "description": "ASDC Direct Data Download for FIRE_AX_ISCCP_DX_1",
                     "@type": "dcat:Distribution",
+                    "description": "ASDC Direct Data Download for FIRE_AX_ISCCP_DX_1",
+                    "downloadURL": "https://asdc.larc.nasa.gov/data/FIRE/FIRE_AX_ISCCP_DX/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_AX_ISCCP_DX/contents.html",
-                    "description": "OPeNDAP data access for FIRE_AX_ISCCP_DX_1",
                     "@type": "dcat:Distribution",
+                    "description": "OPeNDAP data access for FIRE_AX_ISCCP_DX_1",
+                    "downloadURL": "https://opendap.larc.nasa.gov/opendap/FIRE/FIRE_AX_ISCCP_DX/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C1000000999-LARC_ASDC",
+            "issued": "2000-03-17",
+            "keyword": [
+                "atmospheric temperature",
+                "visible wavelengths",
+                "spectral/engineering",
+                "infrared wavelengths",
+                "earth science",
+                "clouds",
+                "atmospheric radiation",
+                "atmospheric pressure",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.5067/ASDC_DAAC/FIRE/0034",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2018-07-10",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/LARC/SD/ASDC"
+            },
             "spatial": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><gml:Polygon xmlns:gml=\"http://www.opengis.net/gml/3.2\" srsName=\"EPSG:4326\"><gml:outerBoundaryIs><gml:LinearRing><gml:posList>10.0 -40.0 10.0 -5.0 40.0 -5.0 40.0 -40.0 10.0 -40.0</gml:posList></gml:LinearRing></gml:outerBoundaryIs><gml:innerBoundaryIs></gml:innerBoundaryIs></gml:Polygon>",
+            "temporal": "1992-06-01T00:00:00Z/1992-06-30T23:59:59.999Z",
             "theme": [
                 "FIRE",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "First ISCCP Regional Experiment (FIRE) Atlantic Stratocumulus Transition Experiment (ASTEX) ISCCP DX Cloud Product - Revised Algorithm Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3292-V1.0",
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
-                "mars"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-05-20T06:51:42.000 to 2012-05-20T09:03:21.500.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3292-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars express",
+                "mars"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MEX-M-MRS-1%2F2%2F3-EXT3-3292-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mex-m-mrs-1-2-3-ext3-3292-v1.0",
-            "description": "This is a Mars Express Radio Science data set, collected during the extended mission phase 2010-01-01 to 2012-12-31. It is a Global Gravity measurement and covers the time 2012-05-20T06:51:42.000 to 2012-05-20T09:03:21.500.",
-            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3292 V1.0",
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
+            "title": "MARS EXPRESS MARS MRS 1/2/3\n                                     EXTENDED MISSION 3 3292 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/33fi-nj84",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Presented here is the environmental microbiome study of the International Space Station surfaces. The environmental samples were collected with the polyester wipes from eight different locations in the ISS during two consecutive sampling sessions (three months apart). The specific objective was to unveil the pool of genes for each location during two separate sessions to learn of functional and metabolic diversity of microorganisms in the ISS. The International Space Station (ISS) as a closed built environment has its own environmental microbiome which is shaped by microgravity, radiation, and limited human presence. The microbial diversity associated with ISS environmental surfaces was investigated during this study. Polyester wipes and contact slides were used for sampling of eight various surface locations on the ISS at different time periods. The samples were retrieved and analyzed immediately upon the return to the Earth (via Soyuz TMA-14M or Dragon capsule from SpaceX). After surface sample collection, contact slides containing nutrient media for the growth of bacteria and fungi were incubated at 25C. The polyester wipes were processed to measure microbial burden (R2A, Blood Agar, and Potato Dextrose Agar) and recover cultivable bacteria as well as fungi. Subsequently, viable microbial burden was assessed using Adenosine Triphosphate (ATP) assay, and quantitative polymerase chain reaction (PCR) methods after propidium monoazide (PMA) treatment. The 16S-tag and metagenome analyses were used to elucidate viable microbial diversity. The cultivable bacterial population yield from the polyester wipes was very high (5 to 7-logs) when compared with the contact slides (10^2 to 10^3 CFU/m2). The PMA-qPCR analysis showed considerable variation of viable bacterial population (10^5 to 10^9 16S rDNA gene copies/m2) among locations sampled. Unlike contact slides, polyester wipes cover much larger sample surface (~1 m2) and produce much more reliable results of the microbial diversity of the ISS covering both cultivable and non-cultivable species. The cultivable, total, and viable microbial diversity was determined utilizing state-of-the art molecular techniques. The implementation of the PMA assay before DNA extraction allowed distinguishing viable microorganisms, which is crucial for determining their role to the crew health, the ISS maintenance and the general knowledge of the closed environmentally controlled built systems.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-69",
+                    "mediaType": "text/html",
+                    "title": "Microbial Observatory (ISS-MO): Indoor microbiome study of the International Space Station surfaces"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-69_33fi-nj84",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "genelab metagenomic data processing protocol",
                 "spaceflight",
@@ -60975,247 +60989,247 @@
                 "qc and data transformation",
                 "sample collection"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/33fi-nj84",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-69_33fi-nj84",
-            "description": "Presented here is the environmental microbiome study of the International Space Station surfaces. The environmental samples were collected with the polyester wipes from eight different locations in the ISS during two consecutive sampling sessions (three months apart). The specific objective was to unveil the pool of genes for each location during two separate sessions to learn of functional and metabolic diversity of microorganisms in the ISS. The International Space Station (ISS) as a closed built environment has its own environmental microbiome which is shaped by microgravity, radiation, and limited human presence. The microbial diversity associated with ISS environmental surfaces was investigated during this study. Polyester wipes and contact slides were used for sampling of eight various surface locations on the ISS at different time periods. The samples were retrieved and analyzed immediately upon the return to the Earth (via Soyuz TMA-14M or Dragon capsule from SpaceX). After surface sample collection, contact slides containing nutrient media for the growth of bacteria and fungi were incubated at 25C. The polyester wipes were processed to measure microbial burden (R2A, Blood Agar, and Potato Dextrose Agar) and recover cultivable bacteria as well as fungi. Subsequently, viable microbial burden was assessed using Adenosine Triphosphate (ATP) assay, and quantitative polymerase chain reaction (PCR) methods after propidium monoazide (PMA) treatment. The 16S-tag and metagenome analyses were used to elucidate viable microbial diversity. The cultivable bacterial population yield from the polyester wipes was very high (5 to 7-logs) when compared with the contact slides (10^2 to 10^3 CFU/m2). The PMA-qPCR analysis showed considerable variation of viable bacterial population (10^5 to 10^9 16S rDNA gene copies/m2) among locations sampled. Unlike contact slides, polyester wipes cover much larger sample surface (~1 m2) and produce much more reliable results of the microbial diversity of the ISS covering both cultivable and non-cultivable species. The cultivable, total, and viable microbial diversity was determined utilizing state-of-the art molecular techniques. The implementation of the PMA assay before DNA extraction allowed distinguishing viable microorganisms, which is crucial for determining their role to the crew health, the ISS maintenance and the general knowledge of the closed environmentally controlled built systems.",
-            "title": "Microbial Observatory (ISS-MO): Indoor microbiome study of the International Space Station surfaces",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-69",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Microbial Observatory (ISS-MO): Indoor microbiome study of the International Space Station surfaces"
-                }
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Microbial Observatory (ISS-MO): Indoor microbiome study of the International Space Station surfaces"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2331332266-OB_DAAC.html",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Archived by National Aeronautics and Space Administration, U.S. Government, NASA/GSFC/SED/ESD/GCDC/OB.DAAC.",
-            "issued": "2019-06-23",
-            "temporal": "2002-07-04T00:00:00Z/2023-03-01T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2019-10-01",
-            "keyword": [
-                "national geospatial data asset",
-                "oceans",
-                "ocean chemistry",
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
-                "name": "NASA/GSFC/SED/ESD/GCDC/OB.DAAC"
-            },
-            "identifier": "C2331332266-OB_DAAC",
             "description": "The Ocean Biology DAAC produces near real-time (quicklook) products using the best-available combination of ancillary data from meteorological and ozone data. As such, the inputs and the calibration used are less than optimal. Quicklook products provide a snapshot of the data during a short time period within a single orbit.",
-            "title": "Aqua MODIS Global Mapped Particulate Inorganic Carbon (PIC) - Near Real Time (NRT) Data, version R2022.0",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
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
-                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/AQUA/MODIS/L3M/PIC/2022",
-                    "description": "MODIS-Aqua L3M Particulate Inorganic Carbon (PIC) - Near Real Time (NRT) Dataset Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "MODIS-Aqua L3M Particulate Inorganic Carbon (PIC) - Near Real Time (NRT) Dataset Landing Page",
+                    "downloadURL": "https://oceancolor.gsfc.nasa.gov/data/10.5067/AQUA/MODIS/L3M/PIC/2022",
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
+            "identifier": "C2331332266-OB_DAAC",
+            "issued": "2019-06-23",
+            "keyword": [
+                "national geospatial data asset",
+                "oceans",
+                "ocean chemistry",
+                "ngda",
+                "earth science"
+            ],
+            "landingPage": "https://cmr.earthdata.nasa.gov:443/search/concepts/C2331332266-OB_DAAC.html",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2019-10-01",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA/GSFC/SED/ESD/GCDC/OB.DAAC"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2002-07-04T00:00:00Z/2023-03-01T00:00:00Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Aqua MODIS Global Mapped Particulate Inorganic Carbon (PIC) - Near Real Time (NRT) Data, version R2022.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/MODIS/MCD43D53.061",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Crystal Schaaf, Zhuosen Wang. 2021-02-22. MODIS/Terra+Aqua BRDF/Albedo White Sky Albedo Band2 Daily L3 Global 30ArcSec CMG V061. Sioux Falls, South Dakota, USA. Archived by National Aeronautics and Space Administration, U.S. Government, NASA EOSDIS Land Processes Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MCD43D53.061. https://doi.org/10.5067/MODIS/MCD43D53.061. The DOI landing page provides citations in APA and Chicago styles..",
-            "issued": "2021-02-22",
-            "temporal": "2000-02-16T00:00:00Z/2024-05-20T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-22",
-            "keyword": [
-                "ngda",
-                "land surface",
-                "earth science",
-                "national geospatial data asset",
-                "surface radiative properties"
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
-            "identifier": "C2540273066-LPCLOUD",
-            "description": "The MCD43D53 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) White-Sky Albedo dataset is produced daily using 16 days of Terra and Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) data at 30 arc second (1,000 meter (m)) resolution. Data are temporally weighted to the ninth day which is reflected in the Julian date in the file name. This Climate Modeling Grid (CMG) product covers the entire globe for use in climate simulation models. Due to the large file size, each MCD43D product contains just one data layer. \r\n\r\nMCD43D42 through MCD43D61 are the albedo products of the MCD43D BRDF/Albedo product suite. There are 10 black-sky albedo and 10 white-sky albedo layers representing MODIS bands 1 through 7 and the visible, near infrared (NIR), and shortwave bands. The black-sky albedo (directional hemispherical reflectance) is defined as albedo in the absence of a diffuse component and is a function of solar zenith angle. White-sky albedo (bihemispherical reflectance) is defined as albedo in the absence of a direct component when the diffuse component is isotropic. \r\n\r\nMCD43D53 is the white-sky albedo for MODIS band 2. \r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
-            "release-place": "Sioux Falls, South Dakota, USA",
             "creator": "Crystal Schaaf, Zhuosen Wang",
-            "title": "MODIS/Terra+Aqua BRDF/Albedo White Sky Albedo Band2 Daily L3 Global 30ArcSec CMG V061",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "The MCD43D53 Version 6.1 Bidirectional Reflectance Distribution Function and Albedo (BRDF/Albedo) White-Sky Albedo dataset is produced daily using 16 days of Terra and Aqua Moderate Resolution Imaging Spectroradiometer (MODIS) data at 30 arc second (1,000 meter (m)) resolution. Data are temporally weighted to the ninth day which is reflected in the Julian date in the file name. This Climate Modeling Grid (CMG) product covers the entire globe for use in climate simulation models. Due to the large file size, each MCD43D product contains just one data layer. \r\n\r\nMCD43D42 through MCD43D61 are the albedo products of the MCD43D BRDF/Albedo product suite. There are 10 black-sky albedo and 10 white-sky albedo layers representing MODIS bands 1 through 7 and the visible, near infrared (NIR), and shortwave bands. The black-sky albedo (directional hemispherical reflectance) is defined as albedo in the absence of a diffuse component and is a function of solar zenith angle. White-sky albedo (bihemispherical reflectance) is defined as albedo in the absence of a direct component when the diffuse component is isotropic. \r\n\r\nMCD43D53 is the white-sky albedo for MODIS band 2. \r\n\r\nImprovements/Changes from Previous Versions\r\n\r\n* The Version 6.1 Level-1B (L1B) products have been improved by undergoing various calibration changes that include: changes to the response-versus-scan angle (RVS) approach that affects reflectance bands for Aqua and Terra MODIS, corrections to adjust for the optical crosstalk in Terra MODIS infrared (IR) bands, and corrections to the Terra MODIS forward look-up table (LUT) update for the period 2012 - 2017.\r\n* A polarization correction has been applied to the L1B Reflective Solar Bands (RSB).",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43D53.061",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FMODIS%2FMCD43D53.061",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43D53.061/",
-                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
                     "@type": "dcat:Distribution",
+                    "description": "LP DAAC Data Pool provides direct access to available products via HTTPS.",
+                    "downloadURL": "https://e4ftl01.cr.usgs.gov/MOTA/MCD43D53.061/",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "application/x-hdf",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2540273066-LPCLOUD",
-                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
                     "@type": "dcat:Distribution",
+                    "description": "Earthdata Search allows users to search, discover, visualize, refine, and access NASA Earth Observation data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=C2540273066-LPCLOUD",
+                    "mediaType": "application/x-hdf",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43D53.061",
-                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "The LP DAAC product page provides information on Science Data Set layers and links for user guides, ATBDs, data access, tools, customer support, etc.",
+                    "downloadURL": "https://doi.org/10.5067/MODIS/MCD43D53.061",
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
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.umb.edu/spectralmass/terra_aqua_modis/v006",
-                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The technical information in the User's Guide enables users to interpret and use the data products.",
+                    "downloadURL": "https://www.umb.edu/spectralmass/terra_aqua_modis/v006",
+                    "mediaType": "text/html",
                     "title": "View this dataset's user's guide"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://lpdaac.usgs.gov/documents/97/MCD43_ATBD.pdf",
-                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
                     "@type": "dcat:Distribution",
+                    "description": "The ATBD provides physical theory and mathematical procedures for the calculations used to produce the data products.",
+                    "downloadURL": "https://lpdaac.usgs.gov/documents/97/MCD43_ATBD.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View this dataset's algorithm theoretical basis document"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/6/MCD43D53",
-                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
                     "@type": "dcat:Distribution",
+                    "description": "The File Specification provides a description of the product file including Scientific Data Sets and their attributes.",
+                    "downloadURL": "https://ladsweb.modaps.eosdis.nasa.gov/filespec/MODIS/6/MCD43D53",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis-land.gsfc.nasa.gov/MODLAND_val.html",
-                    "description": "Validation at stage 4 has been achieved for all MODIS BRDF/Albedo products.",
                     "@type": "dcat:Distribution",
+                    "description": "Validation at stage 4 has been achieved for all MODIS BRDF/Albedo products.",
+                    "downloadURL": "https://modis-land.gsfc.nasa.gov/MODLAND_val.html",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MCD43",
-                    "description": "Further details regarding MODIS land product validation for the MCD43 data products are available from the MODIS Land Team Validation site.",
                     "@type": "dcat:Distribution",
+                    "description": "Further details regarding MODIS land product validation for the MCD43 data products are available from the MODIS Land Team Validation site.",
+                    "downloadURL": "https://modis-land.gsfc.nasa.gov/ValStatus.php?ProductID=MCD43",
+                    "mediaType": "text/html",
                     "title": "View this dataset's science data product validation documentation"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP137/MOTA/MCD43D53.061/contents.html",
-                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
                     "@type": "dcat:Distribution",
+                    "description": "Access data via Open-source Project for a Network Data Access Protocol",
+                    "downloadURL": "https://opendap.cr.usgs.gov/opendap/hyrax/DP137/MOTA/MCD43D53.061/contents.html",
+                    "mediaType": "text/html",
                     "title": "Use OPeNDAP to access the dataset's data"
                 }
             ],
+            "identifier": "C2540273066-LPCLOUD",
+            "issued": "2021-02-22",
+            "keyword": [
+                "ngda",
+                "land surface",
+                "earth science",
+                "national geospatial data asset",
+                "surface radiative properties"
+            ],
+            "landingPage": "https://doi.org/10.5067/MODIS/MCD43D53.061",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2021-02-22",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "LP DAAC"
+            },
+            "release-place": "Sioux Falls, South Dakota, USA",
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2000-02-16T00:00:00Z/2024-05-20T00:00:00Z",
             "theme": [
                 "Terra",
                 "Aqua",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "MODIS/Terra+Aqua BRDF/Albedo White Sky Albedo Band2 Daily L3 Global 30ArcSec CMG V061"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/33mv-scxd",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GeneLab Outreach",
+                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
+            },
+            "description": "Microgravity leads to a 10-15% loss of bone mass in astronauts during space flight. Osteoclast is the multinucleated bone resorbing cell. In this study we used NASA developed ground based Rotary Wall Vessel Bioreactor (RWV) Rotary Cell Culture System (RCCS) to simulate microgravity (uXg) conditions and demonstrated a significant increase (2-fold) in osteoclastogenesis compared to ground based control (Xg) mouse bone marrow cultures. We further determined the gene expression profiling of RAW 264.7 osteoclast progenitor cells in microgravity by agilent microarray analysis. Gene expression pattern was functional group clustered by transcriptome analysis using gene ontology tree machine (GOTM) for cell proliferation/survival differentiation and function. We confirm the microgravity modulated gene expression critical for osteoclast differentiation by real-time RT-PCR and Western blot analysis in murine bone marrow cultures. We identify transcription factors such as c-Jun c-Fos PU-1 critical for osteoclast differentiation is up-regulated in microgravity conditions. In addition microgravity resulted in 2.3 and 2.0-fold increase in the level of cathepsin K and MMP-9 matrix metalloproteinase expression in preosteoclast cells involved in the bone resorption process respectively. We also demonstrate a significant increase in the expression levels of M-CSF receptor c-Fms and PLCy2 and S100A8 molecules that play an important role in Ca2+ signaling essential for osteoclast function. Further microgravity stimulated preosteoclast cells showed elevated cytosolic Ca2+ levels compared to ground based control cells. Thus microgravity regulated gene expression profiling in preosteoclast cells provide new insights in to molecular mechanisms and therapeutic targets of osteoclast differentiation/activation responsible for bone loss and fracture risk in astronauts during space flight mission. Microgravity associated with space flight is a challenge for normal bone homeostasis. Astronauts experience 10-15% bone loss during a space flight mission. We aimed to determine the effect of simulated microgravity on osteoclast preosteoclasts cells. RAW264.7 cells (1.5 x 106 /ml) were loaded in RCCS with DMEM containing 10% FBS for 24 h. The cells were stimulated with RANKL (80ng/ml) for 24 h to obtain preosteoclasts in parallel with ground based control cells. Total RNA was isolated using RNAzol reagent (Biotecx Labs Houston TX) from control (Xg) and microgravity (uXg) subjected cells and hybridized with Agilent whole mouse genome 4x44K array system. Slides were washed and scanned on an Agilent G2565 microarray scanner. Data obtained were analyzed with Agilent feature extraction and GeneSpring GX v7.3.1 software packages (Genus biosystem Inc. Northbrook IL USA).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "description": "GeneLab Study Page",
+                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-18",
+                    "mediaType": "text/html",
+                    "title": "Microarray Profile of Gene Expression during Osteoclast Differentiation in Modeled Microgravity"
+                }
+            ],
+            "identifier": "nasa_genelab_GLDS-18_33mv-scxd",
             "issued": "2018-06-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
             "keyword": [
                 "image_aquisition",
                 "labeling",
@@ -61235,474 +61249,462 @@
                 "bioassay_data_transformation",
                 "treatment group"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "GeneLab Outreach",
-                "hasEmail": "mailto:genelab-outreach@lists.nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/33mv-scxd",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "nasa_genelab_GLDS-18_33mv-scxd",
-            "description": "Microgravity leads to a 10-15% loss of bone mass in astronauts during space flight. Osteoclast is the multinucleated bone resorbing cell. In this study we used NASA developed ground based Rotary Wall Vessel Bioreactor (RWV) Rotary Cell Culture System (RCCS) to simulate microgravity (uXg) conditions and demonstrated a significant increase (2-fold) in osteoclastogenesis compared to ground based control (Xg) mouse bone marrow cultures. We further determined the gene expression profiling of RAW 264.7 osteoclast progenitor cells in microgravity by agilent microarray analysis. Gene expression pattern was functional group clustered by transcriptome analysis using gene ontology tree machine (GOTM) for cell proliferation/survival differentiation and function. We confirm the microgravity modulated gene expression critical for osteoclast differentiation by real-time RT-PCR and Western blot analysis in murine bone marrow cultures. We identify transcription factors such as c-Jun c-Fos PU-1 critical for osteoclast differentiation is up-regulated in microgravity conditions. In addition microgravity resulted in 2.3 and 2.0-fold increase in the level of cathepsin K and MMP-9 matrix metalloproteinase expression in preosteoclast cells involved in the bone resorption process respectively. We also demonstrate a significant increase in the expression levels of M-CSF receptor c-Fms and PLCy2 and S100A8 molecules that play an important role in Ca2+ signaling essential for osteoclast function. Further microgravity stimulated preosteoclast cells showed elevated cytosolic Ca2+ levels compared to ground based control cells. Thus microgravity regulated gene expression profiling in preosteoclast cells provide new insights in to molecular mechanisms and therapeutic targets of osteoclast differentiation/activation responsible for bone loss and fracture risk in astronauts during space flight mission. Microgravity associated with space flight is a challenge for normal bone homeostasis. Astronauts experience 10-15% bone loss during a space flight mission. We aimed to determine the effect of simulated microgravity on osteoclast preosteoclasts cells. RAW264.7 cells (1.5 x 106 /ml) were loaded in RCCS with DMEM containing 10% FBS for 24 h. The cells were stimulated with RANKL (80ng/ml) for 24 h to obtain preosteoclasts in parallel with ground based control cells. Total RNA was isolated using RNAzol reagent (Biotecx Labs Houston TX) from control (Xg) and microgravity (uXg) subjected cells and hybridized with Agilent whole mouse genome 4x44K array system. Slides were washed and scanned on an Agilent G2565 microarray scanner. Data obtained were analyzed with Agilent feature extraction and GeneSpring GX v7.3.1 software packages (Genus biosystem Inc. Northbrook IL USA).",
-            "title": "Microarray Profile of Gene Expression during Osteoclast Differentiation in Modeled Microgravity",
-            "programCode": [
-                "026:005"
-            ],
-            "distribution": [
-                {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://genelab-data.ndc.nasa.gov/genelab/accession/GLDS-18",
-                    "description": "GeneLab Study Page",
-                    "@type": "dcat:Distribution",
-                    "title": "Microarray Profile of Gene Expression during Osteoclast Differentiation in Modeled Microgravity"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "Microarray Profile of Gene Expression during Osteoclast Differentiation in Modeled Microgravity"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-IRIMAG-N-NDR-GZ-V1.0",
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
-                "international halley watch",
-                "halley"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "In preparation for the concerted international study of Comet Halley, the IHW conducted a trial run with observations of Comet Crommelin, largely during February and March of 1984.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-irimag-n-ndr-gz-v1.0_33pm-b4bf",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international halley watch",
+                "halley"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=IHW-C-IRIMAG-N-NDR-GZ-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ihw-c-irimag-n-ndr-gz-v1.0_33pm-b4bf",
-            "description": "In preparation for the concerted international study of Comet Halley, the IHW conducted a trial run with observations of Comet Crommelin, largely during February and March of 1984.",
-            "title": "IHW COMET IRIMAG NO-DATA DATA RECORD GZ V1.O",
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
+            "title": "IHW COMET IRIMAG NO-DATA DATA RECORD GZ V1.O"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-TBOC8-V1.0",
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
-                "cassini-huygens",
-                "saturn"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Cassini Radio Science Titan Bistatic and Occultation experiments (TBOC8) Raw Data Archive is a time-ordered collection of radio science raw data acquired on May 6, 2016, during the Cassini Extended Extended Mission.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-tboc8-v1.0_33qh-wbhq",
+            "issued": "2021-05-21",
+            "keyword": [
+                "cassini-huygens",
+                "saturn"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=CO-SSA-RSS-1-TBOC8-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.co-ssa-rss-1-tboc8-v1.0_33qh-wbhq",
-            "description": "The Cassini Radio Science Titan Bistatic and Occultation experiments (TBOC8) Raw Data Archive is a time-ordered collection of radio science raw data acquired on May 6, 2016, during the Cassini Extended Extended Mission.",
-            "title": "CASSINI RSS RAW DATA SET - TBOC8 V1.0",
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
+            "title": "CASSINI RSS RAW DATA SET - TBOC8 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-DAN-2-EDR-V1.0",
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
-                "mars science laboratory"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "Raw, uncalibrated housekeeping and scientific data collected from the Dynamic Albedo of Neutron Detector (DAN) aboard the Mars Science Laboratory.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-dan-2-edr-v1.0_33qk-iddj",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "mars science laboratory"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MSL-M-DAN-2-EDR-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.msl-m-dan-2-edr-v1.0_33qk-iddj",
-            "description": "Raw, uncalibrated housekeeping and scientific data collected from the Dynamic Albedo of Neutron Detector (DAN) aboard the Mars Science Laboratory.",
-            "title": "MSL MARS DYNAMIC ALBEDO OF NEUTRONS 2 EDR V1.0",
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
+            "title": "MSL MARS DYNAMIC ALBEDO OF NEUTRONS 2 EDR V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0339-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-10-06T05:02:05.000 to 2014-10-06T15:38:31.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0339-v1.0_33ss-5r9u",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-PRL-0339-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-prl-0339-v1.0_33ss-5r9u",
-            "description": "This is a Rosetta Radio Science data set, collected during the PRELANDING phase 2014-01-21 to 2014-11-18. It is a Global Gravity measurement at the comet 67P and covers the time 2014-10-06T05:02:05.000 to 2014-10-06T15:38:31.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0339 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     PRELANDING 0339 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-RAC-5-XYZ-OPS-V1.0",
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
-                "phoenix"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The Robotic Arm Camera (RAC)  experiment on the Mars Phoenix Lander consists of one instrument  component plus command electronics. This RAC Imaging Operations RDR  data set contains xyz data from the Robotic Arm Camera (RAC).",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-rac-5-xyz-ops-v1.0_33v2-i4r8",
+            "issued": "2021-05-21",
+            "keyword": [
+                "mars",
+                "phoenix"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=PHX-M-RAC-5-XYZ-OPS-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.phx-m-rac-5-xyz-ops-v1.0_33v2-i4r8",
-            "description": "The Robotic Arm Camera (RAC)  experiment on the Mars Phoenix Lander consists of one instrument  component plus command electronics. This RAC Imaging Operations RDR  data set contains xyz data from the Robotic Arm Camera (RAC).",
-            "title": "PHOENIX MARS ROBOTIC ARM CAMERA 5 \n                                      XYZ OPS V1.0",
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
+            "title": "PHOENIX MARS ROBOTIC ARM CAMERA 5 \n                                      XYZ OPS V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/497NQVJ0CBEX",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "SnowEx Meteorological Station Measurements from Grand Mesa, CO V001. Version 1. Archived by National Aeronautics and Space Administration, U.S. Government, NASA National Snow and Ice Data Center Distributed Active Archive Center. https://doi.org/10.5067/497NQVJ0CBEX.",
-            "issued": "2016-10-09",
-            "temporal": "2016-10-09T00:00:00Z/2022-08-30T23:59:59.999Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-08-30",
-            "keyword": [
-                "atmospheric pressure",
-                "atmosphere",
-                "atmospheric radiation",
-                "atmospheric temperature",
-                "atmospheric water vapor",
-                "atmospheric winds",
-                "cryosphere",
-                "earth science",
-                "land surface",
-                "snow/ice",
-                "soils"
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
-            "identifier": "C2555433963-NSIDC_ECS",
             "description": "This dataset contains meteorological data collected as part of the ongoing the NASA SnowEx mission, from five meteorological stations installed between 2016-2017 in Grand Mesa, Colorado, to provide supporting data for SnowEx field campaigns and forcing data for modeling. Each station collects a suite of meteorological data at a fixed geographic point, from varying heights above and below the surface elevation. Measured data include: air temperature, relative humidity, long and shortwave solar radiation, barometric pressure, soil moisture and temperature, and derived snow depth. The temporal data coverage varies between each station, but spans October 2016 to August 2022.   \n\n\nThe dataset(s) contain air temperature and relative humidity (10ft and 20ft levels),  4-component radiation (shortwave, longwave), barometric pressure, soil-moisture and temperature (three depths), and a snow-depth product. Data coverage varies for each met station, but spans the time period of October 2016 \u2013 August, 2022. The data frequency is hourly and times are in UTC. The data is monotonic (no duplicate or mis-orderd timestamps) and steps have been taken to remove erroneous data. Periods of missing data are filled with NaN values. The scripts used to process raw data into the current format  are available on the github page (https://github.com/wrudisill/GrandMesaMetData/blob/main/process_data_initial.py).",
-            "title": "SnowEx Meteorological Station Measurements from Grand Mesa, CO V001",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F497NQVJ0CBEX",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2F497NQVJ0CBEX",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX_Met.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX_Met.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX_Met/versions/1",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX_Met/versions/1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX_Met+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX_Met+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX_Met.001/",
-                    "description": "Direct download via HTTPS protocol.",
                     "@type": "dcat:Distribution",
+                    "description": "Direct download via HTTPS protocol.",
+                    "downloadURL": "https://n5eil01u.ecs.nsidc.org/SNOWEX/SNEX_Met.001/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX_Met/versions/1",
-                    "description": "Search and filter data files using a map-based interface",
                     "@type": "dcat:Distribution",
+                    "description": "Search and filter data files using a map-based interface",
+                    "downloadURL": "https://nsidc.org/data/data-access-tool/SNEX_Met/versions/1",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX_Met+V001",
-                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
                     "@type": "dcat:Distribution",
+                    "description": "NASA's newest search and order tool for subsetting, reprojecting, and reformatting data.",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search?q=SNEX_Met+V001",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/497NQVJ0CBEX",
-                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
                     "@type": "dcat:Distribution",
+                    "description": "Provides access to data, documentation, tools, citation information, support, and other resources.",
+                    "downloadURL": "https://doi.org/10.5067/497NQVJ0CBEX",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.5067/497NQVJ0CBEX",
-                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
                     "@type": "dcat:Distribution",
+                    "description": "Includes a user's guide, supplemental documents like ATBDs and academic papers, How Tos, FAQs, etc.",
+                    "downloadURL": "https://doi.org/10.5067/497NQVJ0CBEX",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 }
             ],
+            "identifier": "C2555433963-NSIDC_ECS",
+            "issued": "2016-10-09",
+            "keyword": [
+                "atmospheric pressure",
+                "atmosphere",
+                "atmospheric radiation",
+                "atmospheric temperature",
+                "atmospheric water vapor",
+                "atmospheric winds",
+                "cryosphere",
+                "earth science",
+                "land surface",
+                "snow/ice",
+                "soils"
+            ],
+            "landingPage": "https://doi.org/10.5067/497NQVJ0CBEX",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2022-08-30",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "NASA NSIDC DAAC"
+            },
             "spatial": "-108.21399 39.03388 -108.21399 39.03388",
+            "temporal": "2016-10-09T00:00:00Z/2022-08-30T23:59:59.999Z",
             "theme": [
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SnowEx Meteorological Station Measurements from Grand Mesa, CO V001"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.3334/ORNLDAAC/629",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Chapin, F.S.III, W. Eugster, and J.P. McFadden. 2002. Arctic Tundra Flux Study in the Kuparuk River Basin (Alaska), 1994-1996. ORNL DAAC, Oak Ridge, Tennessee, USA. http://dx.doi.org/10.3334/ORNLDAAC/629",
-            "issued": "2023-10-02",
-            "temporal": "1994-01-01T00:00:00Z/1997-01-01T23:59:59Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-10",
-            "keyword": [
-                "atmospheric chemistry",
-                "earth science",
-                "land surface",
-                "atmospheric pressure",
-                "atmospheric radiation",
-                "atmospheric temperature",
-                "atmospheric water vapor",
-                "atmospheric winds",
-                "vegetation",
-                "biosphere",
-                "soils",
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
-            "identifier": "C2776912302-ORNL_CLOUD",
             "description": "CO2 and water vapor fluxes and ecosystem characteristics were measured at 24 sites along a 317-km transect from the Arctic coast to the latitudinal treeline in Alaska during the growing seasons of 1994-1996.",
-            "graphic-preview-description": "Browse Image",
-            "title": "Arctic Tundra Flux Study in the Kuparuk River Basin (Alaska), 1994-1996",
-            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/fluxnet_logo_square.png",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F629",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.3334%2FORNLDAAC%2F629",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/daacdata/fluxnet/Arctic_Flux/",
-                    "description": "This link allows direct data access via Earthdata login",
                     "@type": "dcat:Distribution",
+                    "description": "This link allows direct data access via Earthdata login",
+                    "downloadURL": "https://daac.ornl.gov/daacdata/fluxnet/Arctic_Flux/",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://daac.ornl.gov/FLUXNET/guides/mcfadden_flux_guide.html",
-                    "description": "ORNL DAAC Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "ORNL DAAC Data Set Documentation",
+                    "downloadURL": "https://daac.ornl.gov/FLUXNET/guides/mcfadden_flux_guide.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/629",
-                    "description": "Data set Landing Page DOI URL",
                     "@type": "dcat:Distribution",
+                    "description": "Data set Landing Page DOI URL",
+                    "downloadURL": "https://doi.org/10.3334/ORNLDAAC/629",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fluxnet/Arctic_Flux/comp/0_DataPolicy.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fluxnet/Arctic_Flux/comp/0_DataPolicy.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fluxnet/Arctic_Flux/comp/Alaska_Kuparuk_flux_format.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fluxnet/Arctic_Flux/comp/Alaska_Kuparuk_flux_format.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fluxnet/Arctic_Flux/comp/Alaska_Kuparuk_sites.dat",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fluxnet/Arctic_Flux/comp/Alaska_Kuparuk_sites.dat",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fluxnet/Arctic_Flux/comp/Alaska_Kuparuk_sites.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fluxnet/Arctic_Flux/comp/Alaska_Kuparuk_sites.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fluxnet/Arctic_Flux/comp/Alaska_Kuparuk_sites_format.txt",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fluxnet/Arctic_Flux/comp/Alaska_Kuparuk_sites_format.txt",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "application/pdf",
-                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fluxnet/Arctic_Flux/comp/mcfadden_flux_guide.pdf",
-                    "description": "Data Set Documentation",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Documentation",
+                    "downloadURL": "https://data.ornldaac.earthdata.nasa.gov/public/fluxnet/Arctic_Flux/comp/mcfadden_flux_guide.pdf",
+                    "mediaType": "application/pdf",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "image/png",
-                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/fluxnet_logo_square.png",
-                    "description": "Browse Image",
                     "@type": "dcat:Distribution",
+                    "description": "Browse Image",
+                    "downloadURL": "https://daac.ornl.gov/graphics/browse/project/square/fluxnet_logo_square.png",
+                    "mediaType": "image/png",
                     "title": "Get a related visualization"
                 }
             ],
+            "graphic-preview-description": "Browse Image",
+            "graphic-preview-file": "https://daac.ornl.gov/graphics/browse/project/square/fluxnet_logo_square.png",
+            "identifier": "C2776912302-ORNL_CLOUD",
+            "issued": "2023-10-02",
+            "keyword": [
+                "atmospheric chemistry",
+                "earth science",
+                "land surface",
+                "atmospheric pressure",
+                "atmospheric radiation",
+                "atmospheric temperature",
+                "atmospheric water vapor",
+                "atmospheric winds",
+                "vegetation",
+                "biosphere",
+                "soils",
+                "atmosphere"
+            ],
+            "landingPage": "https://doi.org/10.3334/ORNLDAAC/629",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-10-10",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "ORNL_DAAC"
+            },
             "spatial": "-171.0 45.0 -130.0 69.0",
+            "temporal": "1994-01-01T00:00:00Z/1997-01-01T23:59:59Z",
             "theme": [
                 "Fluxnet",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Arctic Tundra Flux Study in the Kuparuk River Basin (Alaska), 1994-1996"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-PLS-3-RDR-FULLRES-V1.0",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Morgan",
+                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
+            },
+            "description": "This data set contains raw data from the Plasma Science instrument (PLS) on the Galileo spacecraft for all Jupiter orbits. These data have been reformatted into ASCII tables to facilitate data processing and analysis.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-pls-3-rdr-fullres-v1.0_33x8-29cw",
             "issued": "2021-05-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-26",
-            "references": [
-                "https://pds.nasa.gov"
-            ],
             "keyword": [
                 "galileo",
                 "jupiter",
@@ -61711,256 +61713,265 @@
                 "europa",
                 "callisto"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Morgan",
-                "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
-            },
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=GO-J-PLS-3-RDR-FULLRES-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.go-j-pls-3-rdr-fullres-v1.0_33x8-29cw",
-            "description": "This data set contains raw data from the Plasma Science instrument (PLS) on the Galileo spacecraft for all Jupiter orbits. These data have been reformatted into ASCII tables to facilitate data processing and analysis.",
-            "title": "GALILEO JUPITER RDR FULL RESOLUTION PLASMA DATA V1.0",
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
+            "title": "GALILEO JUPITER RDR FULL RESOLUTION PLASMA DATA V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-COMPIL-3-TNO-CEN-POLARIM-V2.0",
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
-                "support archives",
-                "asteroid"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "The dataset contains a summary of polarimetric observations of Transneptunian objects (including Pluto-Charon system) and Centaurs published by February 8, 2011.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-compil-3-tno-cen-polarim-v2.0_3429-b7py",
+            "issued": "2018-06-26",
+            "keyword": [
+                "support archives",
+                "asteroid"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=EAR-A-COMPIL-3-TNO-CEN-POLARIM-V2.0",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ear-a-compil-3-tno-cen-polarim-v2.0_3429-b7py",
-            "description": "The dataset contains a summary of polarimetric observations of Transneptunian objects (including Pluto-Charon system) and Centaurs published by February 8, 2011.",
-            "title": "POLARIMETRY OF TRANSNEPTUNIAN OBJECTS AND CENTAURS V2.0",
-            "programCode": [
-                "026:005"
+            "references": [
+                "https://pds.nasa.gov"
             ],
             "theme": [
                 "Earth Science"
             ],
-            "accrualPeriodicity": "irregular"
+            "title": "POLARIMETRY OF TRANSNEPTUNIAN OBJECTS AND CENTAURS V2.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGN-V-RDRS-5-GDR-TOPOGRAPHIC-V1.0",
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
-                "venus",
-                "magellan"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Morgan",
                 "hasEmail": "mailto:thomas.h.morgan@nasa.gov"
             },
+            "description": "This data set contains the Magellan Global Topographic Data Record (GTDR). The range to surface is derived by fitting altimeter echoes from the fan-beam altimetry antenna as a function of time to Hagfors' radar backscatter model templates. The ranges are subtracted from the spacecraft radial coordinate (derived from Doppler tracking), yielding measurements of planetary radius. The data are filtered to remove low-frequency errors in the in-plane elements of each spacecraft orbit, and then re-sampled into sinusoidal, Mercator, and north and south polar stereographic projections at a resolution of about 5x5 kilometers per pixel.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgn-v-rdrs-5-gdr-topographic-v1.0_3445-5v2s",
+            "issued": "2021-05-21",
+            "keyword": [
+                "venus",
+                "magellan"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=MGN-V-RDRS-5-GDR-TOPOGRAPHIC-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2023-01-26",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.mgn-v-rdrs-5-gdr-topographic-v1.0_3445-5v2s",
-            "description": "This data set contains the Magellan Global Topographic Data Record (GTDR). The range to surface is derived by fitting altimeter echoes from the fan-beam altimetry antenna as a function of time to Hagfors' radar backscatter model templates. The ranges are subtracted from the spacecraft radial coordinate (derived from Doppler tracking), yielding measurements of planetary radius. The data are filtered to remove low-frequency errors in the in-plane elements of each spacecraft orbit, and then re-sampled into sinusoidal, Mercator, and north and south polar stereographic projections at a resolution of about 5x5 kilometers per pixel.",
-            "title": "MGN V RDRS 5 GLOBAL DATA RECORD TOPOGRAPHIC V1.0",
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
+            "title": "MGN V RDRS 5 GLOBAL DATA RECORD TOPOGRAPHIC V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/SLR/SLR_ILRSACORB_001",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "International Laser Ranging Service (ILRS), SLR Analysis Center (AC) Orbit Product, Greenbelt, MD, USA:NASA Crustal Dynamics Data Information System (CDDIS), Accessed [[enter user data access date]] at doi: 10.5067/SLR/SLR_ILRSACORB_001",
-            "issued": "2016-01-01",
-            "temporal": "2016-01-01T00:00:00Z/2025-01-20T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2025-01-16",
-            "keyword": [
-                "earth science",
-                "solid earth",
-                "tectonics",
-                "gravity/gravitational field",
-                "geodetics"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "undefined",
                 "hasEmail": "mailto:support-cddis@nasa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "CDDIS"
-            },
-            "identifier": "C1604286250-CDDIS",
             "description": "This derived product set consists of Satellite Laser Ranging Final Orbit Product (weekly files, generated weekly) from the NASA Crustal Dynamics Data Information System (CDDIS). SLR provides unambiguous range measurements to mm precision that can be aggregated over the global network to provide very accurate satellite orbits, time histories of station position and motion, and many other geophysical parameters. SLR operates in the optical region and is the only space geodetic technique that measures unambiguous range directly. Analysis of SLR data contributes to the terrestrial reference frame, modeling of the spatial and temporal variations of the Earth's gravitational field, and monitoring of millimeter-level variations in the location of the center of mass of the total Earth system (solid Earth-atmosphere-oceans). In addition, SLR provides precise orbit determination for spaceborne radar altimeter missions. It provides a means for sub-nanosecond global time transfer, and a basis for special tests of the Theory of General Relativity. Analysis Centers (ACs) of the International Laser Ranging Service (ILRS) retrieve SLR data on regular schedules to produce precise orbits identifying the position and velocity of satellites equipped with retroreflectors. The individual ILRS AC solutions are used by the Analysis Center Coordinators (ACC) to generate the official ILRS final combined orbit products, as well as backup combination. The final products are considered the most consistent and highest quality ILRS solutions; they consist of weekly orbit files, generated on a weekly basis with a typical delay of 3 days. All orbit solution files utilize the extended standard product-3 (SP3) format and span 7 days from 00:00 to 23:45 UTC.",
-            "title": "Satellite Laser Ranging (SLR) AC Orbit Product (daily files, generated weekly) from NASA CDDIS",
-            "programCode": [
-                "026:001"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSLR%2FSLR_ILRSACORB_001",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FSLR%2FSLR_ILRSACORB_001",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cddis.nasa.gov/archive/slr/products",
-                    "description": "URL for retrieval of SLR derived products through https",
                     "@type": "dcat:Distribution",
+                    "description": "URL for retrieval of SLR derived products through https",
+                    "downloadURL": "https://cddis.nasa.gov/archive/slr/products",
+                    "mediaType": "text/html",
                     "title": "Download this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://cddis.nasa.gov/Data_and_Derived_Products/SLR/SLR_product_holdings.html",
-                    "description": "URL for more information about SLR derived products",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about SLR derived products",
+                    "downloadURL": "https://cddis.nasa.gov/Data_and_Derived_Products/SLR/SLR_product_holdings.html",
+                    "mediaType": "text/html",
                     "title": "View documentation related to this dataset"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "http://doi.org/10.5067/SLR/SLR_ILRSACORB_001",
-                    "description": "URL for more information about SLR derived products",
                     "@type": "dcat:Distribution",
+                    "description": "URL for more information about SLR derived products",
+                    "downloadURL": "http://doi.org/10.5067/SLR/SLR_ILRSACORB_001",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 }
             ],
+            "identifier": "C1604286250-CDDIS",
+            "issued": "2016-01-01",
+            "keyword": [
+                "earth science",
+                "solid earth",
+                "tectonics",
+                "gravity/gravitational field",
+                "geodetics"
+            ],
+            "landingPage": "https://doi.org/10.5067/SLR/SLR_ILRSACORB_001",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-16",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "CDDIS"
+            },
             "spatial": "-180.0 -90.0 180.0 90.0",
+            "temporal": "2016-01-01T00:00:00Z/2025-01-20T00:00:00Z",
             "theme": [
                 "ILRS",
                 "geospatial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Satellite Laser Ranging (SLR) AC Orbit Product (daily files, generated weekly) from NASA CDDIS"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0638-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-03-12T07:36:25.000 to 2015-03-12T10:05:58.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0638-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "international rosetta mission",
+                "67p/churyumov-gerasimenko 1 (1969 r1)"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC2-0638-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc2-0638-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 2 phase 2015-03-11 to 2015-06-30. It is a Global Gravity measurement at the comet 67P and covers the time 2015-03-12T07:36:25.000 to 2015-03-12T10:05:58.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0638 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 2 0638 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1130-V1.0",
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
+            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-10-26T05:24:15.000 to 2015-10-26T07:30:12.000.",
+            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1130-v1.0",
+            "issued": "2021-05-21",
+            "keyword": [
+                "67p/churyumov-gerasimenko 1 (1969 r1)",
+                "international rosetta mission"
+            ],
+            "landingPage": "https://pds.nasa.gov/ds-view/pds/viewDataset.jsp?dsid=RO-C-RSI-1%2F2%2F3-ESC4-1130-V1.0",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-05-21",
+            "programCode": [
+                "026:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "urn:nasa:pds:context_pds3:data_set:data_set.ro-c-rsi-1-2-3-esc4-1130-v1.0",
-            "description": "This is a Rosetta Radio Science data set, collected during the COMET ESCORT 4 phase 2015-10-22 to 2015-12-31. It is a Global Gravity measurement at the comet 67P and covers the time 2015-10-26T05:24:15.000 to 2015-10-26T07:30:12.000.",
-            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1130 V1.0",
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
+            "title": "ROSETTA-ORBITER 67P RSI 1/2/3\n                                     COMET ESCORT 4 1130 V1.0"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://data.nasa.gov/d/348s-juew",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "026:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "John M. Kusterer",
+                "hasEmail": "mailto:john.m.kusterer@nasa.gov"
+            },
+            "description": "Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations (CALIPSO) was launched on April 28, 2006 to study the impact of clouds and aerosols on the Earth\u2019s radiation budget and climate. It flies in formation with five other satellites in the international \u201cA-Train\u201d (PDF) constellation for coincident Earth observations. The CALIPSO satellite comprises three instruments, the Cloud-Aerosol LIdar with Orthogonal Polarization (CALIOP), the Imaging Infrared Radiometer (IIR), and the Wide Field Camera (WFC). CALIPSO is a joint satellite mission between NASA and the French Agency, CNES. These data consist 5 km aerosol layer data.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://eosweb.larc.nasa.gov/project/calipso/cal_lid_l2_01kmclay-valstage1-V1-10_table",
+                    "mediaType": "text/html"
+                }
+            ],
+            "identifier": "NASA-0000165",
             "issued": "2018-06-25",
-            "temporal": "2006-06-13/2007-03-13",
-            "@type": "dcat:Dataset",
-            "modified": "2020-01-29",
             "keyword": [
                 "atmospheric science",
                 "cloud",
@@ -61970,891 +61981,894 @@
                 "aerosol",
                 "radiation"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "John M. Kusterer",
-                "hasEmail": "mailto:john.m.kusterer@nasa.gov"
-            },
+            "landingPage": "https://data.nasa.gov/d/348s-juew",
+            "modified": "2020-01-29",
+            "programCode": [
+                "026:004"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Aeronautics and Space Administration"
             },
-            "identifier": "NASA-0000165",
-            "description": "Cloud-Aerosol Lidar and Infrared Pathfinder Satellite Observations (CALIPSO) was launched on April 28, 2006 to study the impact of clouds and aerosols on the Earth\u2019s radiation budget and climate. It flies in formation with five other satellites in the international \u201cA-Train\u201d (PDF) constellation for coincident Earth observations. The CALIPSO satellite comprises three instruments, the Cloud-Aerosol LIdar with Orthogonal Polarization (CALIOP), the Imaging Infrared Radiometer (IIR), and the Wide Field Camera (WFC). CALIPSO is a joint satellite mission between NASA and the French Agency, CNES. These data consist 5 km aerosol layer data.",
-            "title": "CALIPSO Lidar L2 1 km Cloud Layer Data V1-10",
-            "programCode": [
-                "026:004"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://eosweb.larc.nasa.gov/project/calipso/cal_lid_l2_01kmclay-valstage1-V1-10_table",
-                    "mediaType": "text/html"
-                }
-            ],
-            "accrualPeriodicity": "irregular",
+            "temporal": "2006-06-13/2007-03-13",
             "theme": [
                 "Earth Science"
-            ]
+            ],
+            "title": "CALIPSO Lidar L2 1 km Cloud Layer Data V1-10"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://doi.org/10.5067/S6AP4-2LRNR",
             "bureauCode": [
                 "026:00"
             ],
             "citation": "Ocean Surface Topography Science Team. 2021-06-22. Sentinel-6A MF Jason-CS L2 P4 Altimeter Low Resolution (LR) NRT Reduced Ocean Surface Topography   . Version F. PO.DAAC. Archived by National Aeronautics and Space Administration, U.S. Government, PO.DAAC. https://doi.org/10.5067/S6AP4-2LRNR.",
-            "issued": "2020-12-07",
-            "temporal": "2020-12-07T13:34:56.105Z/2023-05-29T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2023-05-26",
-            "references": [
-                "https://doi.org/10.1016/j.rse.2021.112395"
-            ],
-            "keyword": [
-                "earth science",
-                "sea surface topography",
-                "ocean waves",
-                "oceans"
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
-            "identifier": "C1968980576-POCLOUD",
-            "description": "Provides low resolution (LR) near real time (NRT; 3-hour latency) measurements of sea surface height anomaly (SSHA), Significant Wave Height (SWH), and Wind Speed. The NRT product is analogous to the Jason-3 OGDR product.",
-            "release-place": "PO.DAAC",
-            "graphic-preview-description": "Thumbnail image for Website",
             "creator": "Ocean Surface Topography Science Team",
-            "title": "Sentinel-6A MF Jason-CS L2 P4 Altimeter Low Resolution (LR) NRT Reduced Ocean Surface Topography",
-            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON_CS_S6A_L2_ALT_LR_RED_OST_NRT_F.jpg",
-            "programCode": [
-                "026:001"
-            ],
+            "description": "Provides low resolution (LR) near real time (NRT; 3-hour latency) measurements of sea surface height anomaly (SSHA), Significant Wave Height (SWH), and Wind Speed. The NRT product is analogous to the Jason-3 OGDR product.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FS6AP4-2LRNR",
-                    "description": "Search results for publications that cite this dataset by its DOI.",
                     "@type": "dcat:Distribution",
+                    "description": "Search results for publications that cite this dataset by its DOI.",
+                    "downloadURL": "https://scholar.google.com/scholar?q=10.5067%2FS6AP4-2LRNR",
+                    "mediaType": "text/html",
                     "title": "Google Scholar search results"
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
-                    "downloadURL": "https://podaac.jpl.nasa.gov/dataset/JASON_CS_S6A_L2_ALT_LR_RED_OST_NRT_F",
-                    "description": "Data Set Landing Page",
                     "@type": "dcat:Distribution",
+                    "description": "Data Set Landing Page",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/dataset/JASON_CS_S6A_L2_ALT_LR_RED_OST_NRT_F",
+                    "mediaType": "text/html",
                     "title": "This dataset's landing page"
                 },
                 {
-                    "mediaType": "image/jpeg",
-                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON_CS_S6A_L2_ALT_LR_RED_OST_NRT_F.jpg",
-                    "description": "Thumbnail image for Website",
                     "@type": "dcat:Distribution",
+                    "description": "Thumbnail image for Website",
+                    "downloadURL": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON_CS_S6A_L2_ALT_LR_RED_OST_NRT_F.jpg",
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
-                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C1968980576-POCLOUD",
-                    "description": "HTTPS endpoint for data browse and download",
                     "@type": "dcat:Distribution",
+                    "description": "HTTPS endpoint for data browse and download",
+                    "downloadURL": "https://cmr.earthdata.nasa.gov/virtual-directory/collections/C1968980576-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through a directory map"
                 },
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1968980576-POCLOUD",
-                    "description": "Browse granule search results in Earthdata Search",
                     "@type": "dcat:Distribution",
+                    "description": "Browse granule search results in Earthdata Search",
+                    "downloadURL": "https://search.earthdata.nasa.gov/search/granules?p=C1968980576-POCLOUD",
+                    "mediaType": "text/html",
                     "title": "Download this dataset through Earthdata Search"
                 }
             ],
+            "graphic-preview-description": "Thumbnail image for Website",
+            "graphic-preview-file": "https://podaac.jpl.nasa.gov/Podaac/thumbnails/JASON_CS_S6A_L2_ALT_LR_RED_OST_NRT_F.jpg",
+            "identifier": "C1968980576-POCLOUD",
+            "issued": "2020-12-07",
+            "keyword": [
+                "earth science",
+                "sea surface topography",
+                "ocean waves",
+                "oceans"
+            ],
+            "landingPage": "https://doi.org/10.5067/S6AP4-2LRNR",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2023-05-26",
+            "programCode": [
+                "026:001"
+            ],
+            "publisher": {
```

