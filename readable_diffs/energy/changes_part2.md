# Change History for energy.json (Part 2)

### Changes from 31606f9 to dd2190f (Part 2/2)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "DOE-019-COAL-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Data on coal receipts in short tons. Data organized by electric power sector, i.e., electric utility, independent power producers, commercial and institutional, and coke plants. Quarterly and annual data available. Based on Form EIA-3 and Form EIA-923 data. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15633,51 +15623,51 @@
                     "title": "Coal Data Browser"
                 }
             ],
+            "identifier": "DOE-019-540445699",
+            "isPartOf": "DOE-019-COAL-COLLECTION1",
             "keyword": [
                 "API",
                 "coal",
                 "coal receipts"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-27",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/?id=coal",
                 "http://www.eia.gov/survey/#coal"
             ],
+            "spatial": "United States",
+            "temporal": "2008/2014",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Data: Receipts Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Data: Stocks Application Programming Interface (API)",
-            "description": "Data on coal stocks in short tons. Data organized by electric power sector, i.e., electric utility, independent power producers, commercial and institutional, and coke plants. Quarterly and annual data available. Based on Form EIA-3 and Form EIA-923 data. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-27",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445700",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/coal/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2008/2014",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "DOE-019-COAL-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Data on coal stocks in short tons. Data organized by electric power sector, i.e., electric utility, independent power producers, commercial and institutional, and coke plants. Quarterly and annual data available. Based on Form EIA-3 and Form EIA-923 data. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15696,52 +15686,52 @@
                     "title": "Coal Data Browser"
                 }
             ],
+            "identifier": "DOE-019-540445700",
+            "isPartOf": "DOE-019-COAL-COLLECTION1",
             "keyword": [
                 "API",
                 "coal",
                 "coal stockpiles",
                 "coal stocks"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-27",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/?id=coal",
                 "http://www.eia.gov/survey/#coal"
             ],
+            "spatial": "United States",
+            "temporal": "2008/2014",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Data: Stocks Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Data: Ash Content Application Programming Interface (API)",
-            "description": "Data on the percentage of ash in coal. Ash increases the weight of coal, adds to the cost of handling, and can affect its burning characteristics. Ash content is measured as a percent by weight of coal on an \"as received\" or a \"dry\" (moisture-free, usually part of a laboratory analysis) basis.  Data organized by electric power sector, i.e., electric utility, independent power producers, commercial and institutional, and coke plants. Quarterly and annual data available. Based on Form EIA-3 and Form EIA-923 data. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-27",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445701",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/coal/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2008/2014",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "DOE-019-COAL-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Data on the percentage of ash in coal. Ash increases the weight of coal, adds to the cost of handling, and can affect its burning characteristics. Ash content is measured as a percent by weight of coal on an \"as received\" or a \"dry\" (moisture-free, usually part of a laboratory analysis) basis.  Data organized by electric power sector, i.e., electric utility, independent power producers, commercial and institutional, and coke plants. Quarterly and annual data available. Based on Form EIA-3 and Form EIA-923 data. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15760,51 +15750,51 @@
                     "title": "Coal Data Browser"
                 }
             ],
+            "identifier": "DOE-019-540445701",
+            "isPartOf": "DOE-019-COAL-COLLECTION1",
             "keyword": [
                 "API",
                 "coal",
                 "coal ash content"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-27",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/?id=coal",
                 "http://www.eia.gov/survey/#coal"
             ],
+            "spatial": "United States",
+            "temporal": "2008/2014",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Data: Ash Content Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Data: Sulfur Content Application Programming Interface (API)",
-            "description": "Data on the quality of coal. Determined by the percentage of sulfur in the coal. Data organized by electric power sector, i.e., electric utility, independent power producers, commercial and institutional, and coke plants. Quarterly and annual data available. Based on Form EIA-3 and Form EIA-923 data.Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-27",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445702",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/coal/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2008/2014",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "DOE-019-COAL-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Data on the quality of coal. Determined by the percentage of sulfur in the coal. Data organized by electric power sector, i.e., electric utility, independent power producers, commercial and institutional, and coke plants. Quarterly and annual data available. Based on Form EIA-3 and Form EIA-923 data.Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15823,52 +15813,52 @@
                     "title": "Coal Data Browser"
                 }
             ],
+            "identifier": "DOE-019-540445702",
+            "isPartOf": "DOE-019-COAL-COLLECTION1",
             "keyword": [
                 "API",
                 "coal",
                 "coal sulfur",
                 "sulfur content"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-27",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/?id=coal",
                 "http://www.eia.gov/survey/#coal"
             ],
+            "spatial": "United States",
+            "temporal": "2008/2014",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Data: Sulfur Content Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Data: Coal shipments to the electric power sector: quantity, by mine state Application Programming Interface (API)",
-            "description": "Data on the quantity of coal that is shipped to the electric power sector. Data organized by mine state and by coal, i.e., lignite, anthracite, subbituminous, bituminous, waste coal, and synfuel coal. Quarterly and annual data available. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-27",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445716",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/coal/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2008/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-COAL-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Data on the quantity of coal that is shipped to the electric power sector. Data organized by mine state and by coal, i.e., lignite, anthracite, subbituminous, bituminous, waste coal, and synfuel coal. Quarterly and annual data available. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15887,6 +15877,8 @@
                     "title": "Coal shipments to the electric power sector: quantity, by mine state API"
                 }
             ],
+            "identifier": "DOE-019-540445716",
+            "isPartOf": "DOE-019-COAL-COLLECTION1",
             "keyword": [
                 "API",
                 "coal",
@@ -15894,43 +15886,41 @@
                 "coal shipments",
                 "electric power sector"
             ],
-            "bureauCode": [
-                "019:20"
-            ],
+            "landingPage": "http://www.eia.gov/coal/",
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-27",
             "programCode": [
                 "019:022"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/?id=coal",
                 "http://www.eia.gov/survey/#coal"
             ],
+            "spatial": "United States",
+            "temporal": "2008/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Data: Coal shipments to the electric power sector: quantity, by mine state Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Short-Term Energy Outlook: U.S. Economy Application Programming Interface (API)",
-            "description": "This API provides data back to 1990 and projections annually, monthly, and quarterly for 18 months. It provides data on economic output, income, expenditures, employment, production and price indexes. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-07",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445738",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/forecasts/steo/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "rights": "The EIA API is offered as a free public service, although registration is required.",
-            "spatial": "United States",
-            "temporal": "1990/2015",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides data back to 1990 and projections annually, monthly, and quarterly for 18 months. It provides data on economic output, income, expenditures, employment, production and price indexes. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15949,6 +15939,7 @@
                     "title": "STEO Data Browser"
                 }
             ],
+            "identifier": "DOE-019-540445738",
             "keyword": [
                 "API",
                 "STEO",
@@ -15958,44 +15949,44 @@
                 "forecast",
                 "projections"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/forecasts/steo/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-07",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/"
             ],
+            "rights": "The EIA API is offered as a free public service, although registration is required.",
+            "spatial": "United States",
+            "temporal": "1990/2015",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Short-Term Energy Outlook: U.S. Economy Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "State Energy Data System (SEDS) : Conversion Factors Application Programming Interface (API)",
-            "description": "This API provides the conversion factors to change physical units to Btu. EIA's State Energy Data System (SEDS) is a comprehensive data set that consists of annual time series estimates of state-level energy use by major economic sectors, energy production and State-level energy price and expenditure data. The system provides data back from 1960. Data are presented in physical units, Btu, and dollars.  Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-24",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445744",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/state/seds/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1960/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides the conversion factors to change physical units to Btu. EIA's State Energy Data System (SEDS) is a comprehensive data set that consists of annual time series estimates of state-level energy use by major economic sectors, energy production and State-level energy price and expenditure data. The system provides data back from 1960. Data are presented in physical units, Btu, and dollars.  Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16009,6 +16000,7 @@
                     "title": "SEDS: Conversion Factors API"
                 }
             ],
+            "identifier": "DOE-019-540445744",
             "keyword": [
                 "API",
                 "Btu",
@@ -16016,45 +16008,43 @@
                 "state energy data system",
                 "unit conversion"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/state/seds/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-24",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/state/seds/seds-technical-notes-complete.cfm"
             ],
+            "spatial": "United States",
+            "temporal": "1960/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "State Energy Data System (SEDS) : Conversion Factors Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data: Non-Hydroelectric Renewables Application Programming Interface (API)",
-            "description": "This API provides international data on non-hydroelectric renewables. Data on electricity capacity and generation. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445765",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-IEDAE-Collection1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on non-hydroelectric renewables. Data on electricity capacity and generation. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16073,6 +16063,8 @@
                     "title": "International Energy Portal"
                 }
             ],
+            "identifier": "DOE-019-540445765",
+            "isPartOf": "DOE-019-IEDAE-Collection1",
             "keyword": [
                 "API",
                 "global data",
@@ -16081,42 +16073,40 @@
                 "renewable energy generation",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
-            ],
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=renewable"
             ],
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data: Non-Hydroelectric Renewables Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data: Vented and Flared Natural Gas Application Programming Interface (API)",
-            "description": "This API provides international data on  vented and flared natural gas production. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445770",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-IEDNG-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on  vented and flared natural gas production. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16135,6 +16125,8 @@
                     "title": "Vented and Flared Natural Gas API"
                 }
             ],
+            "identifier": "DOE-019-540445770",
+            "isPartOf": "DOE-019-IEDNG-COLLECTION1",
             "keyword": [
                 "API",
                 "global data",
@@ -16142,45 +16134,43 @@
                 "natural gas production",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=natural%20gas"
             ],
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data: Vented and Flared Natural Gas Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data: Flared Natural Gas Application Programming Interface (API)",
-            "description": "This API provides international data on carbon dioxide emissions from flared natural gas. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445777",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1980/2014",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-IEDNG-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on carbon dioxide emissions from flared natural gas. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16199,6 +16189,8 @@
                     "title": "International Energy Portal"
                 }
             ],
+            "identifier": "DOE-019-540445777",
+            "isPartOf": "DOE-019-IEDNG-COLLECTION1",
             "keyword": [
                 "API",
                 "global data",
@@ -16206,45 +16198,43 @@
                 "natural gas emissions",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=natural%20gas"
             ],
+            "spatial": "Global",
+            "temporal": "1980/2014",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data: Flared Natural Gas Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data: Other Products Application Programming Interface (API)",
-            "description": "This API provides international data on other petroleum products production, consumption, imports, and exports. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445791",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-IEDPOL-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on other petroleum products production, consumption, imports, and exports. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16258,6 +16248,8 @@
                     "title": "Other Petroleum Products API"
                 }
             ],
+            "identifier": "DOE-019-540445791",
+            "isPartOf": "DOE-019-IEDPOL-COLLECTION1",
             "keyword": [
                 "API",
                 "global data",
@@ -16268,45 +16260,43 @@
                 "petroleum production",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=petroleum"
             ],
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data: Other Products Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data: Fuel Ethanol Application Programming Interface (API)",
-            "description": "This API provides international data on fuel ethanol production and consumption. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445793",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-IEDPOL-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on fuel ethanol production and consumption. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16325,6 +16315,8 @@
                     "title": "Fuel Ethanol API"
                 }
             ],
+            "identifier": "DOE-019-540445793",
+            "isPartOf": "DOE-019-IEDPOL-COLLECTION1",
             "keyword": [
                 "API",
                 "fuel ethanol consumption",
@@ -16333,53 +16325,53 @@
                 "international data",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=petroleum"
             ],
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data: Fuel Ethanol Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Production by MSHA ID, Mine Operation, Union Status, and Average Number of Employees and Hours 2011",
-            "description": "Data on U.S mining operation (i.e., operation name, mailing address, telephone number, State and county of operation, etc.), annual coal production, code definitions, union status, labor hours, and employment data. Annual time series extend back to 1983. Based on EIA Form-7A data.",
-            "modified": "2013-06-05",
             "accessLevel": "public",
-            "identifier": "DOE-019-6745396547",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_7a/instructions.pdf",
-            "landingPage": "http://www.eia.gov/coal/data.cfm",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2011-01-01/2011-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-CPMSHAID-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_7a/instructions.pdf",
+            "description": "Data on U.S mining operation (i.e., operation name, mailing address, telephone number, State and county of operation, etc.), annual coal production, code definitions, union status, labor hours, and employment data. Annual time series extend back to 1983. Based on EIA Form-7A data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://inventory.data.gov/dataset/acaaed6b-8c28-4795-a376-650792a5c9cb/resource/52e0b0cf-c0cb-47e7-828e-11135f3b25cd/download/coalpublic2011-2.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "Coal Production 2011",
-                    "downloadURL": "https://inventory.data.gov/dataset/acaaed6b-8c28-4795-a376-650792a5c9cb/resource/52e0b0cf-c0cb-47e7-828e-11135f3b25cd/download/coalpublic2011-2.xls"
+                    "title": "Coal Production 2011"
                 }
             ],
+            "identifier": "DOE-019-6745396547",
+            "isPartOf": "DOE-019-CPMSHAID-COLLECTION1",
             "keyword": [
                 "coal data",
                 "coal data file",
@@ -16390,45 +16382,43 @@
                 "coal production file",
                 "energy"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/data.cfm",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2013-06-05",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_7a/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2011-01-01/2011-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Production by MSHA ID, Mine Operation, Union Status, and Average Number of Employees and Hours 2011"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Data: Coal shipments to the electric power sector: heat content, by mine state Application Programming Interface (API)",
-            "description": "Data on the heat content of coal that is shipped to the electric power sector. Data organized by mine state and by coal, i.e., lignite, anthracite, subbituminous, bituminous, waste coal, and synfuel coal. Quarterly and annual data available. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-27",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445717",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/coal/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2008/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-COAL-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Data on the heat content of coal that is shipped to the electric power sector. Data organized by mine state and by coal, i.e., lignite, anthracite, subbituminous, bituminous, waste coal, and synfuel coal. Quarterly and annual data available. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16447,6 +16437,8 @@
                     "title": "Coal shipments to the electric power sector: heat content, by mine state API"
                 }
             ],
+            "identifier": "DOE-019-540445717",
+            "isPartOf": "DOE-019-COAL-COLLECTION1",
             "keyword": [
                 "API",
                 "coal",
@@ -16455,46 +16447,44 @@
                 "electric power sector",
                 "heat content"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-27",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/?id=coal",
                 "http://www.eia.gov/survey/#coal"
             ],
+            "spatial": "United States",
+            "temporal": "2008/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Data: Coal shipments to the electric power sector: heat content, by mine state Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Data: Coal shipments to the electric power sector: ash content, by mine state Application Programming Interface (API)",
-            "description": "Data on the ash content of coal that is shipped to the electric power sector. Data organized by mine state and by coal, i.e., lignite, anthracite, subbituminous, bituminous, waste coal, and synfuel coal. Quarterly and annual data available. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-27",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445718",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/coal/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2008/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-COAL-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Data on the ash content of coal that is shipped to the electric power sector. Data organized by mine state and by coal, i.e., lignite, anthracite, subbituminous, bituminous, waste coal, and synfuel coal. Quarterly and annual data available. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16513,6 +16503,8 @@
                     "title": "Coal Data Browser"
                 }
             ],
+            "identifier": "DOE-019-540445718",
+            "isPartOf": "DOE-019-COAL-COLLECTION1",
             "keyword": [
                 "API",
                 "ash content",
@@ -16520,46 +16512,44 @@
                 "coal shipments",
                 "electric power sector"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-27",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/?id=coal",
                 "http://www.eia.gov/survey/#coal"
             ],
+            "spatial": "United States",
+            "temporal": "2008/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Data: Coal shipments to the electric power sector: ash content, by mine state Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Data: Coal shipments to the electric power sector: sulfur content, by mine state Application Programming Interface (API)",
-            "description": "Data on the sulfur content of coal that is shipped to the electric power sector. Data organized by mine state and by coal, i.e., lignite, anthracite, subbituminous, bituminous, waste coal, and synfuel coal. Quarterly and annual data available. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-27",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445719",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/coal/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2008/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-COAL-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Data on the sulfur content of coal that is shipped to the electric power sector. Data organized by mine state and by coal, i.e., lignite, anthracite, subbituminous, bituminous, waste coal, and synfuel coal. Quarterly and annual data available. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16578,6 +16568,8 @@
                     "title": "Coal shipments to the electric power sector: sulfur content, by mine state API"
                 }
             ],
+            "identifier": "DOE-019-540445719",
+            "isPartOf": "DOE-019-COAL-COLLECTION1",
             "keyword": [
                 "API",
                 "coal",
@@ -16585,46 +16577,44 @@
                 "electric power sector",
                 "sulfur content"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-27",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/?id=coal",
                 "http://www.eia.gov/survey/#coal"
             ],
+            "spatial": "United States",
+            "temporal": "2008/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Data: Coal shipments to the electric power sector: sulfur content, by mine state Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Data: Coal shipments to the electric power sector: by mine Application Programming Interface (API)",
-            "description": "Data on coal shipments to the electric power sector by mine. Quarterly and annual data available. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-27",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445720",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/coal/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2008/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-COAL-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Data on coal shipments to the electric power sector by mine. Quarterly and annual data available. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16643,52 +16633,52 @@
                     "title": "Coal shipments to the electric power sector: by mine API"
                 }
             ],
+            "identifier": "DOE-019-540445720",
+            "isPartOf": "DOE-019-COAL-COLLECTION1",
             "keyword": [
                 "API",
                 "coal",
                 "coal shipments",
                 "electric power sector"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-27",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/?id=coal",
                 "http://www.eia.gov/survey/#coal"
             ],
+            "spatial": "United States",
+            "temporal": "2008/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Data: Coal shipments to the electric power sector: by mine Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Petroleum Data: Crude Reserves and Production Application Programming Interface (API)",
-            "description": "Data on the proved reserves,  production, and drilling of crude oil, lease condensates, natural gas, and natural gas wells. Monthly and annual data available. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-31",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445724",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/petroleum/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "rights": "The EIA API is offered as a free public service, although registration is required.",
-            "spatial": "United States",
-            "temporal": "1977/2015",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Data on the proved reserves,  production, and drilling of crude oil, lease condensates, natural gas, and natural gas wells. Monthly and annual data available. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16702,6 +16692,7 @@
                     "title": "Crude Reserves and Production API"
                 }
             ],
+            "identifier": "DOE-019-540445724",
             "keyword": [
                 "API",
                 "crude oil",
@@ -16716,45 +16707,45 @@
                 "proved reserves",
                 "residual fuel"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/petroleum/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-31",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=petroleum",
                 "http://www.eia.gov/survey/#petroleum"
             ],
+            "rights": "The EIA API is offered as a free public service, although registration is required.",
+            "spatial": "United States",
+            "temporal": "1977/2015",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Petroleum Data: Crude Reserves and Production Application Programming Interface (API)"
         },
         {
-            "@type": "dcat:Dataset",
-            "title": "Short-Term Energy Outlook: U.S. CO2 Emissions Application Programming Interface (API)",
-            "description": "This API provides data back to 1990 and projections annually, monthly, and quarterly for 18 months. Summarizes CO2 emissions from coal, fossil fuels, natural gas, and petroleum and other liquid fuels.Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-07",
-            "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445736",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/forecasts/steo/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1990/2015",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides data back to 1990 and projections annually, monthly, and quarterly for 18 months. Summarizes CO2 emissions from coal, fossil fuels, natural gas, and petroleum and other liquid fuels.Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16773,6 +16764,7 @@
                     "title": "STEO Data Browser"
                 }
             ],
+            "identifier": "DOE-019-540445736",
             "keyword": [
                 "API",
                 "STEO",
@@ -16781,44 +16773,43 @@
                 "forecasts",
                 "projections"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/forecasts/steo/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-07",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/"
             ],
+            "spatial": "United States",
+            "temporal": "1990/2015",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Short-Term Energy Outlook: U.S. CO2 Emissions Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Short-Term Energy Outlook: U.S. Weather Application Programming Interface (API)",
-            "description": "This API provides data back to 1990 and projections annually, monthly, and quarterly for 18 months. It provides data on U.S. heating degree days and cooling degree days.  Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-07",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445737",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/forecasts/steo/index.cfm",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1990/2015",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides data back to 1990 and projections annually, monthly, and quarterly for 18 months. It provides data on U.S. heating degree days and cooling degree days.  Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16837,50 +16828,50 @@
                     "title": "STEO Data Browser"
                 }
             ],
+            "identifier": "DOE-019-540445737",
             "keyword": [
                 "STEO",
                 "cooling degree days",
                 "heating degree days",
                 "projections"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/forecasts/steo/index.cfm",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-07",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/"
             ],
+            "spatial": "United States",
+            "temporal": "1990/2015",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Short-Term Energy Outlook: U.S. Weather Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "State Energy Data System (SEDS) : Consumption Application Programming Interface (API)",
-            "description": "This API provides state-level and national-level energy consumption data. Data organized by major economic sectors. EIA's State Energy Data System (SEDS) is a comprehensive data set that consists of annual time series estimates of state-level energy use by major economic sectors, energy production and and State-level energy price and expenditure data. The system provides data back from 1960. Data are presented in physical units, Btu, and dollars. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-24",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445739",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/state/seds/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1960/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides state-level and national-level energy consumption data. Data organized by major economic sectors. EIA's State Energy Data System (SEDS) is a comprehensive data set that consists of annual time series estimates of state-level energy use by major economic sectors, energy production and and State-level energy price and expenditure data. The system provides data back from 1960. Data are presented in physical units, Btu, and dollars. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16894,6 +16885,7 @@
                     "title": "SEDS: Consumption API"
                 }
             ],
+            "identifier": "DOE-019-540445739",
             "keyword": [
                 "API",
                 "SEDS",
@@ -16901,44 +16893,43 @@
                 "state energy consumption",
                 "state energy data system"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/state/seds/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-24",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/state/seds/seds-technical-notes-complete.cfm"
             ],
+            "spatial": "United States",
+            "temporal": "1960/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "State Energy Data System (SEDS) : Consumption Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "State Energy Data System (SEDS) : Production Application Programming Interface (API)",
-            "description": "This API contains state-level and national-level data on energy production. EIA's State Energy Data System (SEDS) is a comprehensive data set that consists of annual time series estimates of state-level energy production by major economic sectors, energy production and State-level energy price and expenditure data. The system provides data back from 1960. Data are presented in physical units, Btu, and dollars. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-24",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445741",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/state/seds/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1960/2012",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API contains state-level and national-level data on energy production. EIA's State Energy Data System (SEDS) is a comprehensive data set that consists of annual time series estimates of state-level energy production by major economic sectors, energy production and State-level energy price and expenditure data. The system provides data back from 1960. Data are presented in physical units, Btu, and dollars. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -16949,11 +16940,12 @@
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://api.eia.gov/category/?api_key=YOUR_API_KEY_HERE&category_id=40207",
+                    "description": "API",
                     "format": "API",
-                    "title": "SEDS: Production API",
-                    "description": "API"
+                    "title": "SEDS: Production API"
                 }
             ],
+            "identifier": "DOE-019-540445741",
             "keyword": [
                 "API",
                 "SEDS",
@@ -16961,44 +16953,43 @@
                 "state data",
                 "state energy data system"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/state/seds/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-24",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/state/seds/seds-technical-notes-complete.cfm"
             ],
+            "spatial": "United States",
+            "temporal": "1960/2012",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "State Energy Data System (SEDS) : Production Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "State Energy Data System (SEDS) : Population Application Programming Interface (API)",
-            "description": "This API provides state-level population, in addition to the U.S. total population. EIA's State Energy Data System (SEDS) is a comprehensive data set that consists of annual time series estimates of state-level energy use by major economic sectors, energy production and State-level energy price and expenditure data. The system provides data back from 1960. Data are presented in physical units, Btu, and dollars.  Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-24",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445742",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/state/seds/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1960/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides state-level population, in addition to the U.S. total population. EIA's State Energy Data System (SEDS) is a comprehensive data set that consists of annual time series estimates of state-level energy use by major economic sectors, energy production and State-level energy price and expenditure data. The system provides data back from 1960. Data are presented in physical units, Btu, and dollars.  Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17013,6 +17004,7 @@
                     "title": "SEDS: Population API"
                 }
             ],
+            "identifier": "DOE-019-540445742",
             "keyword": [
                 "API",
                 "SEDS",
@@ -17021,45 +17013,43 @@
                 "state population",
                 "united states population"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/state/seds/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-24",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/state/seds/seds-technical-notes-complete.cfm"
             ],
+            "spatial": "United States",
+            "temporal": "1960/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "State Energy Data System (SEDS) : Population Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data: Marketed Natural Gas Application Programming Interface (API)",
-            "description": "This API provides international data on marketed natural gas production. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445759",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-IEDNG-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on marketed natural gas production. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17078,6 +17068,8 @@
                     "title": "International Energy Data: Marketed Natural Gas API"
                 }
             ],
+            "identifier": "DOE-019-540445759",
+            "isPartOf": "DOE-019-IEDNG-COLLECTION1",
             "keyword": [
                 "API",
                 "global data",
@@ -17085,45 +17077,43 @@
                 "natural gas production",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=natural%20gas"
             ],
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data: Marketed Natural Gas Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data: Dry Natural Gas Application Programming Interface (API)",
-            "description": "This API provides international data on dry natural gas production, consumption, imports, and exports. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445760",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-IEDNG-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on dry natural gas production, consumption, imports, and exports. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17132,9 +17122,9 @@
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/beta/api/qb.cfm?category=1506090",
                     "mediaType": "text/html",
-                    "title": "API Web Page",
-                    "downloadURL": "https://www.eia.gov/beta/api/qb.cfm?category=1506090"
+                    "title": "API Web Page"
                 },
                 {
                     "@type": "dcat:Distribution",
@@ -17143,6 +17133,8 @@
                     "title": "International Energy Data: Dry Natural Gas API"
                 }
             ],
+            "identifier": "DOE-019-540445760",
+            "isPartOf": "DOE-019-IEDNG-COLLECTION1",
             "keyword": [
                 "API",
                 "global data",
@@ -17153,42 +17145,40 @@
                 "natural gas production",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
-            ],
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=natural%20gas"
             ],
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data: Dry Natural Gas Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data: Crude Oil including Lease Condensate Application Programming Interface (API)",
-            "description": "This API provides international data on crude oil including lease condensate production, imports, exports, and reserves. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445782",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-IEDPOL-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on crude oil including lease condensate production, imports, exports, and reserves. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17207,6 +17197,8 @@
                     "title": "Crude Oil including Lease Condensate API"
                 }
             ],
+            "identifier": "DOE-019-540445782",
+            "isPartOf": "DOE-019-IEDPOL-COLLECTION1",
             "keyword": [
                 "API",
                 "crude oil exports",
@@ -17217,45 +17209,43 @@
                 "international data",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=petroleum"
             ],
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data: Crude Oil including Lease Condensate Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data: Biodiesel Application Programming Interface (API)",
-            "description": "This API provides international data on biodiesel production and consumption. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445794",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-IEDAE-Collection1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on biodiesel production and consumption. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17274,6 +17264,8 @@
                     "title": "Biodiesel API"
                 }
             ],
+            "identifier": "DOE-019-540445794",
+            "isPartOf": "DOE-019-IEDAE-Collection1",
             "keyword": [
                 "API",
                 "biodiesel consumption",
@@ -17282,45 +17274,43 @@
                 "international data",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=petroleum"
             ],
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data: Biodiesel Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data: Hydroelectric Pumped Storage Application Programming Interface (API)",
-            "description": "This API provides international data on hydroelectric pumped storage capacity and generation. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445795",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-IEDAE-Collection1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on hydroelectric pumped storage capacity and generation. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17339,6 +17329,8 @@
                     "title": "International Energy Portal"
                 }
             ],
+            "identifier": "DOE-019-540445795",
+            "isPartOf": "DOE-019-IEDAE-Collection1",
             "keyword": [
                 "API",
                 "global data",
@@ -17348,45 +17340,43 @@
                 "renewable energy generation",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=renewable"
             ],
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data: Hydroelectric Pumped Storage Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data: Solar Application Programming Interface (API)",
-            "description": "This API provides international data on solar capacity and generation. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445796",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-IEDAE-Collection1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on solar capacity and generation. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17405,6 +17395,8 @@
                     "title": "International Solar API"
                 }
             ],
+            "identifier": "DOE-019-540445796",
+            "isPartOf": "DOE-019-IEDAE-Collection1",
             "keyword": [
                 "API",
                 "global data",
@@ -17415,45 +17407,43 @@
                 "solar energy generation",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=renewable"
             ],
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data: Solar Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data: Tide and Wave Application Programming Interface (API)",
-            "description": "This API provides international data on the electricity capacity and generation of tide and wave energy. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445797",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-IEDAE-Collection1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on the electricity capacity and generation of tide and wave energy. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17472,6 +17462,8 @@
                     "title": "Tide and Wave API"
                 }
             ],
+            "identifier": "DOE-019-540445797",
+            "isPartOf": "DOE-019-IEDAE-Collection1",
             "keyword": [
                 "API",
                 "global data",
@@ -17482,46 +17474,43 @@
                 "wave capacity",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=renewable"
             ],
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data: Tide and Wave Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Electricity Data: Receipts of Fossil Fuels by Electricity Plants Application Programming Interface (API)",
-            "description": "This API provides data on receipts of fossil fuels by electricity plants. Data organized by fuel type, i.e., coal, bituminous coal, subbituminous coal, lignite coal, petroleum liquids, petroleum coke, and natural gas. Also by sector, i.e., electric power, electric utility, independent power producers, commercial, and industrial. Annual, quarterly, and monthly data available.  Based on Form EIA-423 and Form EIA-923 data. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-27",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445675",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/electricity/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "rights": "The EIA API is offered as a free public service, although registration is required.",
-            "spatial": "United States",
-            "temporal": "2008/2015",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
-            "isPartOf": "DOE-019-EDFF-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides data on receipts of fossil fuels by electricity plants. Data organized by fuel type, i.e., coal, bituminous coal, subbituminous coal, lignite coal, petroleum liquids, petroleum coke, and natural gas. Also by sector, i.e., electric power, electric utility, independent power producers, commercial, and industrial. Annual, quarterly, and monthly data available.  Based on Form EIA-423 and Form EIA-923 data. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17540,49 +17529,50 @@
                     "title": "Electricity Data Browser"
                 }
             ],
+            "identifier": "DOE-019-540445675",
+            "isPartOf": "DOE-019-EDFF-COLLECTION1",
             "keyword": [
                 "API",
                 "fossil fuel",
                 "fossil fuels receipts"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-27",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=electricity",
                 "http://www.eia.gov/survey/#eia-923",
                 "http://www.eia.gov/survey/#eia-423"
-            ]
+            ],
+            "rights": "The EIA API is offered as a free public service, although registration is required.",
+            "spatial": "United States",
+            "temporal": "2008/2015",
+            "title": "Electricity Data: Receipts of Fossil Fuels by Electricity Plants Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Natural Gas Data: Imports and Exports/Pipelines Application Programming Interface (API)",
-            "description": "Data on natural gas imports and exports. Data organized by country, by U.S. state, by point of entry, and point of exit. Monthly and annual data available.  Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-31",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445685",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/naturalgas/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1999/2015",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
-            "isPartOf": "DOE-019-NGD-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Data on natural gas imports and exports. Data organized by country, by U.S. state, by point of entry, and point of exit. Monthly and annual data available.  Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17596,52 +17586,52 @@
                     "title": "Natural Gas Imports and Exports/Pipelines API"
                 }
             ],
+            "identifier": "DOE-019-540445685",
+            "isPartOf": "DOE-019-NGD-COLLECTION1",
             "keyword": [
                 "API",
                 "interstate natural gas",
                 "natural gas exports",
                 "natural gas imports"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/naturalgas/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-31",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=natural%20gas",
                 "http://www.eia.gov/survey/#naturalgas"
             ],
+            "spatial": "United States",
+            "temporal": "1999/2015",
             "theme": [
                 "energy"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Coal Data: Coal shipments to the electric power sector: by plant Application Programming Interface (API)",
-            "description": "Data on coal shipments to the electric power sector by plant. Quarterly and annual data available. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-27",
-            "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445721",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/coal/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2008/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
+            ],
+            "title": "Natural Gas Data: Imports and Exports/Pipelines Application Programming Interface (API)"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-COAL-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Data on coal shipments to the electric power sector by plant. Quarterly and annual data available. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17660,52 +17650,52 @@
                     "title": "Coal Data Browser"
                 }
             ],
+            "identifier": "DOE-019-540445721",
+            "isPartOf": "DOE-019-COAL-COLLECTION1",
             "keyword": [
                 "API",
                 "coal",
                 "coal shipments",
                 "electric power sector"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-27",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/?id=coal",
                 "http://www.eia.gov/survey/#coal"
             ],
+            "spatial": "United States",
+            "temporal": "2008/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Data: Coal shipments to the electric power sector: by plant Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "State Energy Data System (SEDS) : Prices & Expenditures Application Programming Interface (API)",
-            "description": "This API provides state-level and national-level energy prices and expenditures. Data organized by major economic sectors. EIA's State Energy Data System (SEDS) is a comprehensive data set that consists of annual time series estimates of state-level energy use by major economic sectors, energy production and State-level energy price and expenditure data. The system provides data back from 1960. Data are presented in physical units, Btu, and dollars. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-24",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445740",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/state/seds/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "rights": "The EIA API is offered as a free public service, although registration is required.",
-            "spatial": "United States",
-            "temporal": "1970/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides state-level and national-level energy prices and expenditures. Data organized by major economic sectors. EIA's State Energy Data System (SEDS) is a comprehensive data set that consists of annual time series estimates of state-level energy use by major economic sectors, energy production and State-level energy price and expenditure data. The system provides data back from 1960. Data are presented in physical units, Btu, and dollars. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17719,6 +17709,7 @@
                     "title": "SEDS: Prices and Expenditures API"
                 }
             ],
+            "identifier": "DOE-019-540445740",
             "keyword": [
                 "API",
                 "SEDS",
@@ -17728,44 +17719,44 @@
                 "state energy prices",
                 "state energy system"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/state/seds/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-24",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/state/seds/seds-technical-notes-complete.cfm"
             ],
+            "rights": "The EIA API is offered as a free public service, although registration is required.",
+            "spatial": "United States",
+            "temporal": "1970/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "State Energy Data System (SEDS) : Prices & Expenditures Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "State Energy Data System (SEDS): GDP Application Programming Interface (API)",
-            "description": "This API provides state-level and national-level GDP. EIA's State Energy Data System (SEDS) is a comprehensive data set that consists of annual time series estimates of state-level energy use by major economic sectors, energy production and State-level energy price and expenditure data. The system provides data back from 1960. Data are presented in physical units, Btu, and dollars.  Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-24",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445743",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/state/seds/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1970/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides state-level and national-level GDP. EIA's State Energy Data System (SEDS) is a comprehensive data set that consists of annual time series estimates of state-level energy use by major economic sectors, energy production and State-level energy price and expenditure data. The system provides data back from 1960. Data are presented in physical units, Btu, and dollars.  Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17779,6 +17770,7 @@
                     "title": "SEDS: GDP API"
                 }
             ],
+            "identifier": "DOE-019-540445743",
             "keyword": [
                 "API",
                 "GDP",
@@ -17787,45 +17779,43 @@
                 "state energy data system",
                 "united states GDP"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/state/seds/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-24",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/state/seds/seds-technical-notes-complete.cfm"
             ],
+            "spatial": "United States",
+            "temporal": "1970/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "State Energy Data System (SEDS): GDP Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data Application Programming Interface (API)",
-            "description": "This API provides international data on energy sources (e.g., coal, electricity, natural gas, petroleum, coal, renewables) and activities (e.g., consumption, imports, exports, carbon emissions, prices, production). Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445745",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-IEDAD-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on energy sources (e.g., coal, electricity, natural gas, petroleum, coal, renewables) and activities (e.g., consumption, imports, exports, carbon emissions, prices, production). Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17844,6 +17834,8 @@
                     "title": "International Energy Portal"
                 }
             ],
+            "identifier": "DOE-019-540445745",
+            "isPartOf": "DOE-019-IEDAD-COLLECTION1",
             "keyword": [
                 "API",
                 "coal price",
@@ -17867,45 +17859,43 @@
                 "petroleum reserves",
                 "petroleum stocks"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/"
             ],
+            "spatial": "United States",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data: Coal Application Programming Interface (API)",
-            "description": "This API provides international data on coal consumption, imports, exports, and carbon dioxide emissions. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445746",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-IEDC-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on coal consumption, imports, exports, and carbon dioxide emissions. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17924,6 +17914,8 @@
                     "title": "International Energy Portal"
                 }
             ],
+            "identifier": "DOE-019-540445746",
+            "isPartOf": "DOE-019-IEDC-COLLECTION1",
             "keyword": [
                 "API",
                 "coal carbon emissions",
@@ -17934,42 +17926,40 @@
                 "international data",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
-            ],
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=coal"
             ],
+            "spatial": "United States",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data: Coal Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data: Electricity Application Programming Interface (API)",
-            "description": "This API provides international data on electricity consumption, imports, exports, capacity, distribution losses, generation, and net imports.  Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445747",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-IEDAD-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on electricity consumption, imports, exports, capacity, distribution losses, generation, and net imports.  Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -17988,51 +17978,51 @@
                     "title": "International Energy Portal"
                 }
             ],
+            "identifier": "DOE-019-540445747",
+            "isPartOf": "DOE-019-IEDAD-COLLECTION1",
             "keyword": [
                 "API",
                 "global data",
                 "international data",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=electricity"
             ],
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data: Electricity Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data: Gross Natural Gas Application Programming Interface (API)",
-            "description": "This API provides international data on gross natural gas production, reserves, and carbon dioxide emissions. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445748",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-IEDNG-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on gross natural gas production, reserves, and carbon dioxide emissions. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18051,6 +18041,8 @@
                     "title": "International Energy Data: Gross Natural Gas API"
                 }
             ],
+            "identifier": "DOE-019-540445748",
+            "isPartOf": "DOE-019-IEDNG-COLLECTION1",
             "keyword": [
                 "API",
                 "global data",
@@ -18061,42 +18053,40 @@
                 "international data",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
-            ],
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "https://www.eia.gov/tools/glossary/index.php?id=natural%20gas"
             ],
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data: Gross Natural Gas Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data: Petroleum Application Programming Interface (API)",
-            "description": "This API provides international data on petroleum consumption, stocks, and carbon dioxide emissions. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445749",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-IEDPOL-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on petroleum consumption, stocks, and carbon dioxide emissions. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18115,6 +18105,8 @@
                     "title": "International Energy Portal"
                 }
             ],
+            "identifier": "DOE-019-540445749",
+            "isPartOf": "DOE-019-IEDPOL-COLLECTION1",
             "keyword": [
                 "API",
                 "global data",
@@ -18124,45 +18116,43 @@
                 "petroleum stocks",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=petroleum"
             ],
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data: Petroleum Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data: Total Primary Coal Application Programming Interface (API)",
-            "description": "This API provides international data on total primary coal production and reserves. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445750",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-IEDC-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on total primary coal production and reserves. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18181,6 +18171,8 @@
                     "title": "International Energy Data: Total Primary Coal API"
                 }
             ],
+            "identifier": "DOE-019-540445750",
+            "isPartOf": "DOE-019-IEDC-COLLECTION1",
             "keyword": [
                 "API",
                 "coal production",
@@ -18190,45 +18182,43 @@
                 "total primary coal",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=coal"
             ],
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data: Total Primary Coal Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data: Hard Coal Application Programming Interface (API)",
-            "description": "This API provides  international data on hard coal production and reserves. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445751",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-IEDC-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides  international data on hard coal production and reserves. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18247,6 +18237,8 @@
                     "title": "International Energy Portal"
                 }
             ],
+            "identifier": "DOE-019-540445751",
+            "isPartOf": "DOE-019-IEDC-COLLECTION1",
             "keyword": [
                 "API",
                 "coal",
@@ -18257,42 +18249,40 @@
                 "international data",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
-            ],
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=coal"
             ],
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data: Hard Coal Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data: Anthracite Application Programming Interface (API)",
-            "description": "This API provides international data on anthracite coal production. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445752",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-IEDC-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on anthracite coal production. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18311,6 +18301,8 @@
                     "title": "International Energy Data: Anthracite Coal API"
                 }
             ],
+            "identifier": "DOE-019-540445752",
+            "isPartOf": "DOE-019-IEDC-COLLECTION1",
             "keyword": [
                 "API",
                 "anthracite coal",
@@ -18320,45 +18312,43 @@
                 "international data",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=coal"
             ],
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data: Anthracite Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data: Bituminous Application Programming Interface (API)",
-            "description": "This API provides  international data on bituminous coal production. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445753",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-IEDC-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides  international data on bituminous coal production. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18377,6 +18367,8 @@
                     "title": "International Energy Data: Bituminous Coal API"
                 }
             ],
+            "identifier": "DOE-019-540445753",
+            "isPartOf": "DOE-019-IEDC-COLLECTION1",
             "keyword": [
                 "API",
                 "bituminous coal",
@@ -18386,42 +18378,40 @@
                 "international data",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
-            ],
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=coal"
             ],
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data: Bituminous Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data: Lignite Application Programming Interface (API)",
-            "description": "This API provides  international data on lignite coal production and reserves. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445754",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-IEDC-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides  international data on lignite coal production and reserves. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18440,6 +18430,8 @@
                     "title": "International Energy Data: Lignite Coal API"
                 }
             ],
+            "identifier": "DOE-019-540445754",
+            "isPartOf": "DOE-019-IEDC-COLLECTION1",
             "keyword": [
                 "API",
                 "coal production",
@@ -18449,45 +18441,43 @@
                 "lignite coal",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=coal"
             ],
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data: Lignite Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data: Metallurgical Coal Application Programming Interface (API)",
-            "description": "This API provides international data on metallurgical coal production and reserves. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445755",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-IEDC-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on metallurgical coal production and reserves. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18506,6 +18496,8 @@
                     "title": "International Energy Data: Metallurgical Coal API"
                 }
             ],
+            "identifier": "DOE-019-540445755",
+            "isPartOf": "DOE-019-IEDC-COLLECTION1",
             "keyword": [
                 "API",
                 "coal production",
@@ -18515,46 +18507,43 @@
                 "metallurgical coal",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=coal"
             ],
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data: Metallurgical Coal Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data: Hard Coal Briquettes Application Programming Interface (API)",
-            "description": "This API provides international data on hard coal briquettes production. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445756",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "rights": "The EIA API is offered as a free public service, although registration is required.",
-            "spatial": "Global",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-IEDC-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on hard coal briquettes production. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18573,6 +18562,8 @@
                     "title": "International Energy Data: Hard Coal Briquettes API"
                 }
             ],
+            "identifier": "DOE-019-540445756",
+            "isPartOf": "DOE-019-IEDC-COLLECTION1",
             "keyword": [
                 "API",
                 "coal production",
@@ -18582,45 +18573,44 @@
                 "international data",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=coal"
             ],
+            "rights": "The EIA API is offered as a free public service, although registration is required.",
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data: Hard Coal Briquettes Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data: Lignite Briquettes Application Programming Interface (API)",
-            "description": "This API provides international data on lignite coal briquettes production. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445757",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-IEDC-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on lignite coal briquettes production. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18639,6 +18629,8 @@
                     "title": "International Energy Data: Lignite Briquettes API"
                 }
             ],
+            "identifier": "DOE-019-540445757",
+            "isPartOf": "DOE-019-IEDC-COLLECTION1",
             "keyword": [
                 "APi",
                 "coal production",
@@ -18648,42 +18640,40 @@
                 "lignite briquettes",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
-            ],
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=coal"
             ],
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data: Lignite Briquettes Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data: Metallurgical Coke Application Programming Interface (API)",
-            "description": "This API provides international data on metallurgical coke production. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445758",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-IEDC-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on metallurgical coke production. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18702,6 +18692,8 @@
                     "title": "International Energy Data: Metallurgical Coke API"
                 }
             ],
+            "identifier": "DOE-019-540445758",
+            "isPartOf": "DOE-019-IEDC-COLLECTION1",
             "keyword": [
                 "API",
                 "coal production",
@@ -18711,42 +18703,40 @@
                 "metallurgical coke",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
-            ],
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=coal"
             ],
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data: Metallurgical Coke Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data: Nuclear Application Programming Interface (API)",
-            "description": "This API provides international data on nuclear electricity capacity and generation. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445761",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-IEDAE-Collection1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on nuclear electricity capacity and generation. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18765,6 +18755,8 @@
                     "title": "International Energy Portal"
                 }
             ],
+            "identifier": "DOE-019-540445761",
+            "isPartOf": "DOE-019-IEDAE-Collection1",
             "keyword": [
                 "API",
                 "global data",
@@ -18774,44 +18766,43 @@
                 "nuclear generation",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=nuclear"
             ],
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data: Nuclear Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Petroleum Data: Summary Application Programming Interface (API)",
-            "description": "Data on petroleum production, imports, inputs, stocks, exports, and prices. Weekly, monthly, and annual data available. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-31",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445722",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/petroleum/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1989/2015",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Data on petroleum production, imports, inputs, stocks, exports, and prices. Weekly, monthly, and annual data available. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18825,6 +18816,7 @@
                     "title": "Petroleum Data: Summary API"
                 }
             ],
+            "identifier": "DOE-019-540445722",
             "keyword": [
                 "butane",
                 "crude oil",
@@ -18839,46 +18831,44 @@
                 "petroleum",
                 "residual fuel"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/petroleum/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-31",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=petroleum",
                 "http://www.eia.gov/survey/#petroleum"
             ],
+            "spatial": "United States",
+            "temporal": "1989/2015",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Petroleum Data: Summary Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data: Total Petroleum and Other Liquids Application Programming Interface (API)",
-            "description": "This API provides international data on total petroleum and other liquids production. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445778",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1980/2014",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-IEDPOL-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on total petroleum and other liquids production. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18897,6 +18887,8 @@
                     "title": "Total Petroleum and Other Liquids API"
                 }
             ],
+            "identifier": "DOE-019-540445778",
+            "isPartOf": "DOE-019-IEDPOL-COLLECTION1",
             "keyword": [
                 "API",
                 "global data",
@@ -18904,45 +18896,43 @@
                 "petroleum production",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=petroleum"
             ],
+            "spatial": "Global",
+            "temporal": "1980/2014",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data: Total Petroleum and Other Liquids Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data: Crude Oil, NGPL, and Other Liquids Application Programming Interface (API)",
-            "description": "This API provides international data on crude oil, NGPL, and other liquids production. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445780",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-IEDPOL-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on crude oil, NGPL, and other liquids production. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -18961,6 +18951,8 @@
                     "title": "International Energy Portal"
                 }
             ],
+            "identifier": "DOE-019-540445780",
+            "isPartOf": "DOE-019-IEDPOL-COLLECTION1",
             "keyword": [
                 "API",
                 "crude oil production",
@@ -18970,45 +18962,42 @@
                 "ngpl production",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=petroleum"
             ],
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data: Crude Oil, NGPL, and Other Liquids Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data: per Capita Application Programming Interface (API)",
-            "description": "This API provides international data on energy consumption per capita and carbon dioxide emissions per capita. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445772",
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "rights": "The EIA API is offered as a free public service, although registration is required.",
-            "spatial": "Global",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-IEDAD-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "description": "This API provides international data on energy consumption per capita and carbon dioxide emissions per capita. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19027,6 +19016,8 @@
                     "title": "International Energy Data: per Capita API"
                 }
             ],
+            "identifier": "DOE-019-540445772",
+            "isPartOf": "DOE-019-IEDAD-COLLECTION1",
             "keyword": [
                 "API",
                 "carbon dioxide emissions",
@@ -19036,44 +19027,44 @@
                 "international data",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/"
             ],
+            "rights": "The EIA API is offered as a free public service, although registration is required.",
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data: per Capita Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Petroleum Data: Prices Application Programming Interface (API)",
-            "description": "Prices of petroleum products and crude oil. Weekly, monthly, and annual data available. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-08-03",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445723",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/petroleum/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1983/2015",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1W",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Prices of petroleum products and crude oil. Weekly, monthly, and annual data available. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19087,6 +19078,7 @@
                     "title": "Petroleum Data: Prices API"
                 }
             ],
+            "identifier": "DOE-019-540445723",
             "keyword": [
                 "API",
                 "crude oil",
@@ -19103,45 +19095,44 @@
                 "petroleum prices",
                 "residual fuel"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/petroleum/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-08-03",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=petroleum",
                 "http://www.eia.gov/survey/#petroleum"
             ],
+            "spatial": "United States",
+            "temporal": "1983/2015",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Petroleum Data: Prices Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Petroleum Data: Refining and Processing Application Programming Interface (API)",
-            "description": "Data on petroleum inputs, production, yield, and capacity. Weekly, monthly and annual data available. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-31",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445725",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/petroleum/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1992/2015",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Data on petroleum inputs, production, yield, and capacity. Weekly, monthly and annual data available. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19155,6 +19146,7 @@
                     "title": "Petroleum Data: Refining and Processing API"
                 }
             ],
+            "identifier": "DOE-019-540445725",
             "keyword": [
                 "API",
                 "crude oil",
@@ -19168,46 +19160,44 @@
                 "petroleum production",
                 "petroleum yield"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/petroleum/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-31",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=petroleum",
                 "http://www.eia.gov/survey/#petroleum"
             ],
+            "spatial": "United States",
+            "temporal": "1992/2015",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Petroleum Data: Refining and Processing Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data: Fossil Fuels Application Programming Interface (API)",
-            "description": "This API provides international data on fossil fuels electricity capacity and electricity net generation. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445762",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-IEDAD-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on fossil fuels electricity capacity and electricity net generation. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19226,6 +19216,8 @@
                     "title": "International Energy Data: Fossil Fuels API"
                 }
             ],
+            "identifier": "DOE-019-540445762",
+            "isPartOf": "DOE-019-IEDAD-COLLECTION1",
             "keyword": [
                 "API",
                 "fossil fuel capacity",
@@ -19234,45 +19226,43 @@
                 "international data",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=petroleum"
             ],
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data: Fossil Fuels Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data: Renewables Application Programming Interface (API)",
-            "description": "This API provides international data on renewable electricity capacity and electricity generation. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445763",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-IEDAE-Collection1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on renewable electricity capacity and electricity generation. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19291,6 +19281,8 @@
                     "title": "International Energy Portal"
                 }
             ],
+            "identifier": "DOE-019-540445763",
+            "isPartOf": "DOE-019-IEDAE-Collection1",
             "keyword": [
                 "API",
                 "global data",
@@ -19300,42 +19292,40 @@
                 "renewable energy generation",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
-            ],
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=renewable"
             ],
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data: Renewables Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data: Hydroelectricity Application Programming Interface (API)",
-            "description": "This API provides international data on hydroelectric energy capacity and generation. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445764",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-IEDAE-Collection1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on hydroelectric energy capacity and generation. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19354,6 +19344,8 @@
                     "title": "International Energy Portal"
                 }
             ],
+            "identifier": "DOE-019-540445764",
+            "isPartOf": "DOE-019-IEDAE-Collection1",
             "keyword": [
                 "API",
                 "global data",
@@ -19364,45 +19356,43 @@
                 "renewable energy generation",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=renewable"
             ],
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data: Hydroelectricity Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data: Geothermal Application Programming Interface (API)",
-            "description": "This API provides international data on geothermal electricity capacity and electricity generation. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445766",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-IEDAE-Collection1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on geothermal electricity capacity and electricity generation. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19421,6 +19411,8 @@
                     "title": "International Energy Portal"
                 }
             ],
+            "identifier": "DOE-019-540445766",
+            "isPartOf": "DOE-019-IEDAE-Collection1",
             "keyword": [
                 "API",
                 "geothermal capacity",
@@ -19431,45 +19423,42 @@
                 "renewable energy",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=renewable"
             ],
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data: Geothermal Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data: Wind Application Programming Interface (API)",
-            "description": "This API provides international data on wind electricity capacity and generation. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445768",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "rights": "The EIA API is offered as a free public service, although registration is required.",
-            "spatial": "Global",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-IEDAE-Collection1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on wind electricity capacity and generation. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19488,6 +19477,8 @@
                     "title": "International Energy Data: Wind API"
                 }
             ],
+            "identifier": "DOE-019-540445768",
+            "isPartOf": "DOE-019-IEDAE-Collection1",
             "keyword": [
                 "API",
                 "global data",
@@ -19497,45 +19488,44 @@
                 "wind energy",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=renewable"
             ],
+            "rights": "The EIA API is offered as a free public service, although registration is required.",
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data: Wind Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data: Biomass and Waste Application Programming Interface (API)",
-            "description": "This API provides international data on biomass energy and waste energy capacity and generation. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445769",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-IEDAE-Collection1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on biomass energy and waste energy capacity and generation. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19554,6 +19544,8 @@
                     "title": "International Energy Data: Biomass and Waste API"
                 }
             ],
+            "identifier": "DOE-019-540445769",
+            "isPartOf": "DOE-019-IEDAE-Collection1",
             "keyword": [
                 "API",
                 "biomass waste",
@@ -19562,42 +19554,40 @@
                 "renewable energy",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
-            ],
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=renewable"
             ],
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data: Biomass and Waste Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data: Primary Energy Application Programming Interface (API)",
-            "description": "This API provides international data on primary energy production, consumption, and carbon dioxide emissions. Also data on population. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445771",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-IEDAD-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on primary energy production, consumption, and carbon dioxide emissions. Also data on population. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19616,6 +19606,8 @@
                     "title": "International Energy Portal"
                 }
             ],
+            "identifier": "DOE-019-540445771",
+            "isPartOf": "DOE-019-IEDAD-COLLECTION1",
             "keyword": [
                 "API",
                 "global data",
@@ -19625,45 +19617,43 @@
                 "primary energy production",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/"
             ],
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data: Primary Energy Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data: Energy Intensity Using Market Exchange Rates Application Programming Interface (API)",
-            "description": "This API provides international data on energy intensity and carbon dioxide intensity using market exchange rates. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445773",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-IEDAD-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on energy intensity and carbon dioxide intensity using market exchange rates. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19682,6 +19672,8 @@
                     "title": "Energy Intensity Using Market Exchange Rates API"
                 }
             ],
+            "identifier": "DOE-019-540445773",
+            "isPartOf": "DOE-019-IEDAD-COLLECTION1",
             "keyword": [
                 "API",
                 "carbon dioxide intensity",
@@ -19690,45 +19682,43 @@
                 "international data",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/"
             ],
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data: Energy Intensity Using Market Exchange Rates Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data: Energy Intensity Using Purchasing Power Parities Application Programming Interface (API)",
-            "description": "This API provides international data on energy intensity and carbon dioxide intensity using purchasing power parities. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445774",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-IEDAD-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on energy intensity and carbon dioxide intensity using purchasing power parities. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19747,6 +19737,8 @@
                     "title": "API Web Page"
                 }
             ],
+            "identifier": "DOE-019-540445774",
+            "isPartOf": "DOE-019-IEDAD-COLLECTION1",
             "keyword": [
                 "API",
                 "carbon dioxide intensity",
@@ -19755,45 +19747,43 @@
                 "international data",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/"
             ],
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data: Energy Intensity Using Purchasing Power Parities Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data: Reinjected Natural Gas Application Programming Interface (API)",
-            "description": "This API provides international data on reinjected natural gas production. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445775",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-IEDNG-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on reinjected natural gas production. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19812,6 +19802,8 @@
                     "title": "Reinjected Natural Gas API"
                 }
             ],
+            "identifier": "DOE-019-540445775",
+            "isPartOf": "DOE-019-IEDNG-COLLECTION1",
             "keyword": [
                 "API",
                 "global data",
@@ -19819,45 +19811,43 @@
                 "natural gas production",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/"
             ],
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data: Reinjected Natural Gas Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data: Consumed Natural Gas Application Programming Interface (API)",
-            "description": "This API provides international data on consumed natural gas carbon dioxide emissions. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445776",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-IEDNG-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on consumed natural gas carbon dioxide emissions. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19876,6 +19866,8 @@
                     "title": "International Energy Portal"
                 }
             ],
+            "identifier": "DOE-019-540445776",
+            "isPartOf": "DOE-019-IEDNG-COLLECTION1",
             "keyword": [
                 "API",
                 "global data",
@@ -19883,45 +19875,43 @@
                 "natural gas emissions",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=natural%20gas"
             ],
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data: Consumed Natural Gas Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data: Refinery Processing Gain Application Programming Interface (API)",
-            "description": "This API provides international data on refinery processing gain production. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445781",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-IEDPOL-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on refinery processing gain production. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19940,6 +19930,8 @@
                     "title": "Refinery Processing Gain API"
                 }
             ],
+            "identifier": "DOE-019-540445781",
+            "isPartOf": "DOE-019-IEDPOL-COLLECTION1",
             "keyword": [
                 "API",
                 "global data",
@@ -19947,45 +19939,43 @@
                 "refinery data",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=petroleum"
             ],
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data: Refinery Processing Gain Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data: NGPL Application Programming Interface (API)",
-            "description": "This API provides international data on natural gas plant liquids (NGPL) production. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445783",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-IEDPOL-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on natural gas plant liquids (NGPL) production. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -19994,9 +19984,9 @@
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/beta/api/qb.cfm?category=1506474",
                     "mediaType": "text/html",
-                    "title": "API Web Page",
-                    "downloadURL": "https://www.eia.gov/beta/api/qb.cfm?category=1506474"
+                    "title": "API Web Page"
                 },
                 {
                     "@type": "dcat:Distribution",
@@ -20005,6 +19995,8 @@
                     "title": "International NGPL API"
                 }
             ],
+            "identifier": "DOE-019-540445783",
+            "isPartOf": "DOE-019-IEDPOL-COLLECTION1",
             "keyword": [
                 "API",
                 "NGPL",
@@ -20014,45 +20006,43 @@
                 "natural gas plant liquids production",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=petroleum"
             ],
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data: NGPL Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data: Other Liquids Application Programming Interface (API)",
-            "description": "This API provides international data on other liquids production. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445784",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-IEDPOL-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on other liquids production. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -20071,6 +20061,8 @@
                     "title": "International Energy Portal"
                 }
             ],
+            "identifier": "DOE-019-540445784",
+            "isPartOf": "DOE-019-IEDPOL-COLLECTION1",
             "keyword": [
                 "API",
                 "global data",
@@ -20079,45 +20071,43 @@
                 "liquid fuels production",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=petroleum"
             ],
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data: Other Liquids Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data: Motor Gasoline Application Programming Interface (API)",
-            "description": "This API provides international data on motor gasoline production, consumption, imports, and exports. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445785",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-IEDPOL-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on motor gasoline production, consumption, imports, and exports. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -20136,6 +20126,8 @@
                     "title": "International Energy Portal"
                 }
             ],
+            "identifier": "DOE-019-540445785",
+            "isPartOf": "DOE-019-IEDPOL-COLLECTION1",
             "keyword": [
                 "API",
                 "gasoline consumption",
@@ -20147,45 +20139,43 @@
                 "motor gasoline",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=petroleum"
             ],
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data: Motor Gasoline Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data: Kerosene Application Programming Interface (API)",
-            "description": "This API provides international data on kerosene production, consumption, imports, and exports. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445787",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-IEDPOL-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on kerosene production, consumption, imports, and exports. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -20204,6 +20194,8 @@
                     "title": "International Energy Portal"
                 }
             ],
+            "identifier": "DOE-019-540445787",
+            "isPartOf": "DOE-019-IEDPOL-COLLECTION1",
             "keyword": [
                 "API",
                 "global data",
@@ -20214,46 +20206,43 @@
                 "kerosene production",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=petroleum"
             ],
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data: Kerosene Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data: Distillate Fuel Oil Application Programming Interface (API)",
-            "description": "This API provides international data on distillate fuel oil production, consumption, imports, exports, and bunkers. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445788",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "rights": "The EIA API is offered as a free public service, although registration is required.",
-            "spatial": "Global",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-IEDPOL-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on distillate fuel oil production, consumption, imports, exports, and bunkers. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -20272,6 +20261,8 @@
                     "title": "International Energy Portal"
                 }
             ],
+            "identifier": "DOE-019-540445788",
+            "isPartOf": "DOE-019-IEDPOL-COLLECTION1",
             "keyword": [
                 "API",
                 "distillate fuel oil",
@@ -20283,45 +20274,44 @@
                 "international data",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=petroleum"
             ],
+            "rights": "The EIA API is offered as a free public service, although registration is required.",
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data: Distillate Fuel Oil Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data: Liquefied Petroleum Gases Application Programming Interface (API)",
-            "description": "This API provides international data on liquefied petroleum gases production, consumption, imports, and exports. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445790",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-IEDPOL-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on liquefied petroleum gases production, consumption, imports, and exports. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -20340,6 +20330,8 @@
                     "title": "International Energy Portal"
                 }
             ],
+            "identifier": "DOE-019-540445790",
+            "isPartOf": "DOE-019-IEDPOL-COLLECTION1",
             "keyword": [
                 "API",
                 "LGP",
@@ -20348,44 +20340,43 @@
                 "liquefied petroleum gases",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=petroleum"
             ],
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data: Liquefied Petroleum Gases Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Petroleum Data: Imports/Exports and Movements Application Programming Interface (API)",
-            "description": "Imports and exports of petroleum products and crude oil. Weekly, monthly, and annual data available. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-31",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445726",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/petroleum/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1981/2015",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Imports and exports of petroleum products and crude oil. Weekly, monthly, and annual data available. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -20399,6 +20390,7 @@
                     "title": "Petroleum Data: Imports/Exports and Movements API"
                 }
             ],
+            "identifier": "DOE-019-540445726",
             "keyword": [
                 "AAPI",
                 "crude oil",
@@ -20408,45 +20400,44 @@
                 "petroleum exports",
                 "petroleum imports"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/petroleum/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-31",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=petroleum",
                 "http://www.eia.gov/survey/#petroleum"
             ],
+            "spatial": "Global",
+            "temporal": "1981/2015",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Petroleum Data: Imports/Exports and Movements Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Petroleum Data: Stocks Application Programming Interface (API)",
-            "description": "Data on petroleum and crude oil stocks. Weekly, monthly, and annual data available. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-31",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445727",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/petroleum/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1981/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Data on petroleum and crude oil stocks. Weekly, monthly, and annual data available. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -20460,6 +20451,7 @@
                     "title": "Petroleum Data: Stocks API"
                 }
             ],
+            "identifier": "DOE-019-540445727",
             "keyword": [
                 "API",
                 "crude oil",
@@ -20468,45 +20460,44 @@
                 "petroleum",
                 "petroleum stocks"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/petroleum/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-31",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=petroleum",
                 "http://www.eia.gov/survey/#petroleum"
             ],
+            "spatial": "United States",
+            "temporal": "1981/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Petroleum Data: Stocks Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Petroleum Data: Consumption/Sales Application Programming Interface (API)",
-            "description": "Data on the consumption and sales of petroleum products. Weekly, monthly, and annual data available. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-31",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445728",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/petroleum/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1983/2015",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Data on the consumption and sales of petroleum products. Weekly, monthly, and annual data available. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -20520,6 +20511,7 @@
                     "title": "Petroleum Data: Consumption/Sales API"
                 }
             ],
+            "identifier": "DOE-019-540445728",
             "keyword": [
                 "API",
                 "fuel oil consumption",
@@ -20529,45 +20521,44 @@
                 "petroleum consumption",
                 "petroleum sales"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/petroleum/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-31",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=petroleum",
                 "http://www.eia.gov/survey/#petroleum"
             ],
+            "spatial": "United States",
+            "temporal": "1983/2015",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Petroleum Data: Consumption/Sales Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Short-Term Energy Outlook: U.S. Prices Application Programming Interface (API)",
-            "description": "This API provides data back to 1990 and projections annually, monthly, and quarterly for 18 months.  Summarizes the outlook for prices of petroleum, natural gas, electricity and coal. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-07",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445729",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/forecasts/steo/index.cfm",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1990/2015",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides data back to 1990 and projections annually, monthly, and quarterly for 18 months.  Summarizes the outlook for prices of petroleum, natural gas, electricity and coal. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -20586,6 +20577,7 @@
                     "title": "STEO Data Browser"
                 }
             ],
+            "identifier": "DOE-019-540445729",
             "keyword": [
                 "API",
                 "STEO",
@@ -20596,52 +20588,50 @@
                 "petroleum prices",
                 "projections"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/forecasts/steo/index.cfm",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-07",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/"
             ],
+            "spatial": "United States",
+            "temporal": "1990/2015",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Short-Term Energy Outlook: U.S. Prices Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Short-Term Energy Outlook: International Petroleum and Other Liquids Application Programming Interface (API)",
-            "description": "This API provides data back to 1990 and projections annually, monthly, and quarterly for 18 months.  Summarizes the outlook for supply, consumption, inventory, and production capacity for international petroleum and other liquids. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-07",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445730",
-            "dataQuality": true,
-            "describedByType": "text/html",
-            "landingPage": "http://www.eia.gov/forecasts/steo/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "rights": "The EIA API is offered as a free public service, although registration is required.",
-            "spatial": "Global",
-            "temporal": "1990/2015",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedByType": "text/html",
+            "description": "This API provides data back to 1990 and projections annually, monthly, and quarterly for 18 months.  Summarizes the outlook for supply, consumption, inventory, and production capacity for international petroleum and other liquids. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://api.eia.gov/category/?api_key=YOUR_API_KEY_HERE&category_id=829716",
                     "mediaType": "application/json",
-                    "title": "STEO: International Petroleum and Other Liquids API",
-                    "downloadURL": "https://api.eia.gov/category/?api_key=YOUR_API_KEY_HERE&category_id=829716"
+                    "title": "STEO: International Petroleum and Other Liquids API"
                 },
                 {
                     "@type": "dcat:Distribution",
@@ -20655,6 +20645,7 @@
                     "title": "STEO Data Browser"
                 }
             ],
+            "identifier": "DOE-019-540445730",
             "keyword": [
                 "API",
                 "STEO",
@@ -20663,44 +20654,44 @@
                 "petroleum production",
                 "projections"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/forecasts/steo/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-07",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/"
             ],
+            "rights": "The EIA API is offered as a free public service, although registration is required.",
+            "spatial": "Global",
+            "temporal": "1990/2015",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Short-Term Energy Outlook: International Petroleum and Other Liquids Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Short-Term Energy Outlook: U.S. Petroleum and Other Liquids Application Programming Interface (API)",
-            "description": "This API provides data back to 1990 and projections annually, monthly, and quarterly for 18 months.  Summarizes the outlook for U.S. petroleum and other liquids supply, consumption, inventories, refining, and prices.  Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-07",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445731",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/forecasts/steo/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1990/2015",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides data back to 1990 and projections annually, monthly, and quarterly for 18 months.  Summarizes the outlook for U.S. petroleum and other liquids supply, consumption, inventories, refining, and prices.  Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -20719,6 +20710,7 @@
                     "title": "STEO Data Browser"
                 }
             ],
+            "identifier": "DOE-019-540445731",
             "keyword": [
                 "API",
                 "STEO",
@@ -20729,44 +20721,43 @@
                 "petroleum supply",
                 "projections"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/forecasts/steo/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-07",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/"
             ],
+            "spatial": "United States",
+            "temporal": "1990/2015",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Short-Term Energy Outlook: U.S. Petroleum and Other Liquids Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Short-Term Energy Outlook: U.S. Natural Gas Application Programming Interface (API)",
-            "description": "This API provides data back to 1990 and projections annually, monthly, and quarterly for 18 months. Summarizes the outlook for supply, consumption, inventories, and prices for U.S. natural gas. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-07",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445732",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/forecasts/steo/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1990/2015",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides data back to 1990 and projections annually, monthly, and quarterly for 18 months. Summarizes the outlook for supply, consumption, inventories, and prices for U.S. natural gas. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -20785,6 +20776,7 @@
                     "title": "STEO Data Browser"
                 }
             ],
+            "identifier": "DOE-019-540445732",
             "keyword": [
                 "STEO",
                 "natural gas",
@@ -20792,44 +20784,43 @@
                 "natural gas projections",
                 "projections"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/forecasts/steo/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-07",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/"
             ],
+            "spatial": "United States",
+            "temporal": "1990/2015",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Short-Term Energy Outlook: U.S. Natural Gas Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Short-Term Energy Outlook: U.S. Electricity Application Programming Interface (API)",
-            "description": "This API provides data back to 1990 and projections annually, monthly, and quarterly for 18 months.  Summarizes the outlook for U.S electricity generation, consumption, retail prices, fuel consumption, fuel inventories, fuel costs, residential usage, and residential customers. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-07",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445733",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/forecasts/steo/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1990/2015",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides data back to 1990 and projections annually, monthly, and quarterly for 18 months.  Summarizes the outlook for U.S electricity generation, consumption, retail prices, fuel consumption, fuel inventories, fuel costs, residential usage, and residential customers. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -20848,6 +20839,7 @@
                     "title": "STEO Data Browser"
                 }
             ],
+            "identifier": "DOE-019-540445733",
             "keyword": [
                 "API",
                 "STEO",
@@ -20856,44 +20848,43 @@
                 "electricity projections",
                 "projections"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/forecasts/steo/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-07",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/"
             ],
+            "spatial": "United States",
+            "temporal": "1990/2015",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Short-Term Energy Outlook: U.S. Electricity Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Short-Term Energy Outlook: U.S. Coal Application Programming Interface (API)",
-            "description": "This API provides data back to 1990 and projections annually, monthly, and quarterly for 18 months.  Summarizes the outlook for supply, consumption, inventories, prices and market indicators for U.S. coal. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-07",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445734",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/forecasts/steo/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1990/2015",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides data back to 1990 and projections annually, monthly, and quarterly for 18 months.  Summarizes the outlook for supply, consumption, inventories, prices and market indicators for U.S. coal. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -20912,6 +20903,7 @@
                     "title": "STEO Data Browser"
                 }
             ],
+            "identifier": "DOE-019-540445734",
             "keyword": [
                 "API",
                 "STEO",
@@ -20923,42 +20915,40 @@
                 "coal supply",
                 "projections"
             ],
-            "bureauCode": [
-                "019:20"
-            ],
+            "landingPage": "http://www.eia.gov/forecasts/steo/",
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-07",
             "programCode": [
                 "019:022"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/"
             ],
+            "spatial": "United States",
+            "temporal": "1990/2015",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Short-Term Energy Outlook: U.S. Coal Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data: Solar, Tide, Wave, Fuel Cell Application Programming Interface (API)",
-            "description": "This API provides international data on  solar, tide, wave, and fuel cell energy  capacity and generation. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445767",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-IEDAE-Collection1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on  solar, tide, wave, and fuel cell energy  capacity and generation. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -20977,6 +20967,8 @@
                     "title": "International Energy Data: Solar, Tide, Wave, Fuel Cell API"
                 }
             ],
+            "identifier": "DOE-019-540445767",
+            "isPartOf": "DOE-019-IEDAE-Collection1",
             "keyword": [
                 "API",
                 "global data",
@@ -20985,46 +20977,43 @@
                 "renewable energy generation",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=renewable"
             ],
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data: Solar, Tide, Wave, Fuel Cell Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data: Refined Petroleum Products Application Programming Interface (API)",
-            "description": "This API provides international data on the production, imports, exports, and bunkering of refined petroleum products. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445779",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "rights": "The EIA API is offered as a free public service, although registration is required.",
-            "spatial": "Global",
-            "temporal": "1980/2014",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-IEDPOL-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on the production, imports, exports, and bunkering of refined petroleum products. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -21043,6 +21032,8 @@
                     "title": "International Energy Portal"
                 }
             ],
+            "identifier": "DOE-019-540445779",
+            "isPartOf": "DOE-019-IEDPOL-COLLECTION1",
             "keyword": [
                 "API",
                 "global data",
@@ -21051,44 +21042,43 @@
                 "refined petroleum products",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=petroleum"
             ],
+            "rights": "The EIA API is offered as a free public service, although registration is required.",
+            "spatial": "Global",
+            "temporal": "1980/2014",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data: Refined Petroleum Products Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data: Jet Fuel Application Programming Interface (API)",
-            "description": "This API provides international data on jet fuel production, consumption, imports, and exports. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445786",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-IEDPOL-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on jet fuel production, consumption, imports, and exports. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -21107,6 +21097,8 @@
                     "title": "International Energy Portal"
                 }
             ],
+            "identifier": "DOE-019-540445786",
+            "isPartOf": "DOE-019-IEDPOL-COLLECTION1",
             "keyword": [
                 "API",
                 "global data",
@@ -21118,45 +21110,43 @@
                 "jet fuel production",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=petroleum"
             ],
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data: Jet Fuel Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data: Residual Fuel Oil Application Programming Interface (API)",
-            "description": "This API provides international data on residual fuel oil production, consumption, imports, exports, and bunkers. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445789",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-IEDPOL-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on residual fuel oil production, consumption, imports, exports, and bunkers. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -21175,51 +21165,51 @@
                     "title": "International Energy Portal"
                 }
             ],
+            "identifier": "DOE-019-540445789",
+            "isPartOf": "DOE-019-IEDPOL-COLLECTION1",
             "keyword": [
                 "API",
                 "international data",
                 "residuel fuel",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=petroleum"
             ],
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data: Residual Fuel Oil Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data: Biofuels Application Programming Interface (API)",
-            "description": "This API provides international data on biofuel production and consumption. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-05-18",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445792",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-IEDAE-Collection1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on biofuel production and consumption. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -21238,6 +21228,8 @@
                     "title": "International Energy Portal"
                 }
             ],
+            "identifier": "DOE-019-540445792",
+            "isPartOf": "DOE-019-IEDAE-Collection1",
             "keyword": [
                 "API",
                 "biofuels consumpton",
@@ -21246,43 +21238,44 @@
                 "international data",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-18",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=petroleum"
             ],
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data: Biofuels Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual Electric Generator Report - Latest Year",
-            "description": "Annual U.S. generator level data about generators at electric power plants owned and operated by electric utilities and nonutilities (including independent power producers, combined heat and power producers, and other industrials). Based on EIA Form-860 d",
-            "modified": "2016-02-16",
             "accessLevel": "public",
-            "identifier": "DOE-019-EIA-AEGR-COLL1",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_860/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia860/index.html",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_860/form.pdf",
+            "description": "Annual U.S. generator level data about generators at electric power plants owned and operated by electric utilities and nonutilities (including independent power producers, combined heat and power producers, and other industrials). Based on EIA Form-860 d",
+            "identifier": "DOE-019-EIA-AEGR-COLL1",
             "keyword": [
                 "EIA-860",
                 "annual data",
@@ -21309,50 +21302,49 @@
                 "winter capability",
                 "winter capacity"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia860/index.html",
+            "language": [
+                "us-EN"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2016-02-16",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "us-EN"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
+            "spatial": "United States",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual Electric Generator Report - Latest Year"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual Energy Outlook",
-            "description": "The Annual Energy Outlook presents longterm annual projections of energy supply, demand, and prices focused on the U.S. through 2050, based on results from EIA's National Energy Modeling System (NEMS). NEMS enables EIA to make projections under alternative, internally-consistent sets of assumptions, the results of which are presented as cases. The analysis in AEO2014 focuses on five primary cases: a Reference case,\r\nLow and High Economic Growth cases, and Low and High Oil Price cases. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2019-01-24",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-AEO-Collection1",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/forecasts/aeo/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2011/2040",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "The Annual Energy Outlook presents longterm annual projections of energy supply, demand, and prices focused on the U.S. through 2050, based on results from EIA's National Energy Modeling System (NEMS). NEMS enables EIA to make projections under alternative, internally-consistent sets of assumptions, the results of which are presented as cases. The analysis in AEO2014 focuses on five primary cases: a Reference case,\r\nLow and High Economic Growth cases, and Low and High Oil Price cases. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
-                    "title": "Annual Energy Outlook Interactive Table Browser",
                     "description": "EIA's Annual Energy Outlook 2019 provides modeled projections of domestic energy markets through 2050, and it includes cases with different assumptions about macroeconomic growth, world oil prices, and technological progress.",
-                    "downloadURL": "https://www.eia.gov/outlooks/aeo/data/browser/"
+                    "downloadURL": "https://www.eia.gov/outlooks/aeo/data/browser/",
+                    "mediaType": "text/html",
+                    "title": "Annual Energy Outlook Interactive Table Browser"
                 }
             ],
+            "identifier": "DOE-019-AEO-Collection1",
             "keyword": [
                 "API",
                 "consumption",
@@ -21377,41 +21369,41 @@
                 "weather",
                 "weather forecast"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/forecasts/aeo/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2019-01-24",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
+            "spatial": "United States",
+            "temporal": "2011/2040",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual Energy Outlook"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Data Collection",
-            "description": "International and domestic data on coal production, consumption, prices, reserves, stocks, imports, exports, distribution, and transportation rates. Weekly, monthly, and annual data available.",
-            "modified": "2014-10-06",
             "accessLevel": "public",
-            "identifier": "DOE-019-COAL-COLLECTION1",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/coal/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1940/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1W",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "International and domestic data on coal production, consumption, prices, reserves, stocks, imports, exports, distribution, and transportation rates. Weekly, monthly, and annual data available.",
+            "identifier": "DOE-019-COAL-COLLECTION1",
             "keyword": [
                 "Demonstrated Reserve Base",
                 "coal consumption",
@@ -21437,38 +21429,38 @@
                 "spot price",
                 "underground mining"
             ],
-            "bureauCode": [
-                "019:20"
-            ],
+            "landingPage": "http://www.eia.gov/coal/",
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2014-10-06",
             "programCode": [
                 "019:022"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
+            "spatial": "Global",
+            "temporal": "1940/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Data Collection"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Production by MSHA ID",
-            "description": "Data on U.S mining operation (i.e., operation name, mailing address, telephone number, State and county of operation, etc.), annual coal production, code definitions, and union status. Annual time series extend back to 1983. Based on EIA Form-7A data.",
-            "modified": "2018-11-02",
             "accessLevel": "public",
-            "identifier": "DOE-019-CPMSHAID-COLLECTION1",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_7a/instructions.pdf",
-            "landingPage": "http://www.eia.gov/coal/data.cfm",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "State and County",
-            "temporal": "1991-01-01/1991-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_7a/instructions.pdf",
+            "description": "Data on U.S mining operation (i.e., operation name, mailing address, telephone number, State and county of operation, etc.), annual coal production, code definitions, and union status. Annual time series extend back to 1983. Based on EIA Form-7A data.",
+            "identifier": "DOE-019-CPMSHAID-COLLECTION1",
             "keyword": [
                 "coal data",
                 "coal data file",
@@ -21479,43 +21471,44 @@
                 "coal production file",
                 "energy"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/data.cfm",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2018-11-02",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_7a/form.pdf"
             ],
+            "spatial": "State and County",
+            "temporal": "1991-01-01/1991-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Production by MSHA ID"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Company Level Petroleum Imports",
-            "description": "Monthly data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
-            "modified": "2016-02-16",
             "accessLevel": "public",
-            "identifier": "DOE-019-CLPI-COLLECTION1",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
-            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
+            "description": "Monthly data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
+            "identifier": "DOE-019-CLPI-COLLECTION1",
             "keyword": [
                 "company imports",
                 "crude oil imports",
@@ -21527,44 +21520,44 @@
                 "petroleum imports",
                 "residual fuel oil imports"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2016-02-16",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_814/form.pdf",
                 "http://www.eia.gov/survey/form/eia_814/instructions.pdf"
             ],
+            "spatial": "United States",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Company Level Petroleum Imports"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Crude Oil Imports",
-            "description": "Imports by origin of all grades of crude oil, i.e., heavy sour, heavy sweet, light sour, light sweet,  and medium  crude oil. View data by country, by world region, or by OPEC and non-OPEC status.  Data in monthly or annual time series.  Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2016-02-16",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-COI-COLLECTION1",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/petroleum/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Imports by origin of all grades of crude oil, i.e., heavy sour, heavy sweet, light sour, light sweet,  and medium  crude oil. View data by country, by world region, or by OPEC and non-OPEC status.  Data in monthly or annual time series.  Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
+            "identifier": "DOE-019-COI-COLLECTION1",
             "keyword": [
                 "API",
                 "OPEC",
@@ -21573,179 +21566,178 @@
                 "petroleum",
                 "petroleum imports"
             ],
-            "bureauCode": [
-                "019:20"
-            ],
+            "landingPage": "http://www.eia.gov/petroleum/",
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2016-02-16",
             "programCode": [
                 "019:022"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
+            "spatial": "Global",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Crude Oil Imports"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Electricity Data - Consumption",
-            "description": "This API provides data on U.S. consumption for electricity generation in Btu. Data organized by fuel type, i.e., coal, petroleum liquids, petroleum coke, and  natural gas. Data also organized by sector, i.e., electric power, electric utility, commercial and industrial. Annual, quarterly, and monthly data available. Based on Form EIA-906, Form EIA-920, and Form EIA-923 data.  Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2016-02-16",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-EDC-COLLECTION1",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/electricity/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2001/2015",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides data on U.S. consumption for electricity generation in Btu. Data organized by fuel type, i.e., coal, petroleum liquids, petroleum coke, and  natural gas. Data also organized by sector, i.e., electric power, electric utility, commercial and industrial. Annual, quarterly, and monthly data available. Based on Form EIA-906, Form EIA-920, and Form EIA-923 data.  Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
+            "identifier": "DOE-019-EDC-COLLECTION1",
             "keyword": [
                 "API",
                 "conusumption",
                 "electricity generation"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2016-02-16",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=electricity",
                 "http://www.eia.gov/survey/#eia-923"
             ],
+            "spatial": "United States",
+            "temporal": "2001/2015",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Electricity Data - Consumption"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Electricity Data - Retail Sales",
-            "description": "This API provides  data on retail sales of electricity by major end-use sectors, i.e., residential, commercial, industrial, and transportation. Based on Form EIA-826 and Form EIA-861 data. Annual, quarterly, and monthly data available.",
-            "modified": "2016-02-16",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-EDRP-COLLECTION1",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/electricity/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2001/2015",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides  data on retail sales of electricity by major end-use sectors, i.e., residential, commercial, industrial, and transportation. Based on Form EIA-826 and Form EIA-861 data. Annual, quarterly, and monthly data available.",
+            "identifier": "DOE-019-EDRP-COLLECTION1",
             "keyword": [
                 "API",
                 "electricity sales",
                 "retail sales"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2016-02-16",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/#eia-826",
                 "http://www.eia.gov/tools/glossary/index.cfm?id=electricity",
                 "http://www.eia.gov/survey/#eia-861"
             ],
-            "theme": [
-                "energy"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Electricity Price by State",
-            "description": "Annual data on the average price of retail electricity to consumers. Data organized by U.S. state and by provider, i.e., total electric industry, full-service providers, restructured retail service providers, energy-only providers, and delivery-only service. Annual time series extend back to 1990. Based on Form EIA-861 data.",
-            "modified": "2016-02-16",
-            "accessLevel": "public",
-            "identifier": "DOE-019-AEPS-COLLECTION1",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/state/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
             "spatial": "United States",
-            "temporal": "1990/2012",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
+            "temporal": "2001/2015",
+            "theme": [
+                "energy"
+            ],
+            "title": "Electricity Data - Retail Sales"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
+            "description": "Annual data on the average price of retail electricity to consumers. Data organized by U.S. state and by provider, i.e., total electric industry, full-service providers, restructured retail service providers, energy-only providers, and delivery-only service. Annual time series extend back to 1990. Based on Form EIA-861 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "title": "Average Price by State by Provider",
                     "description": "Average Electricity Price by State by Provider",
-                    "downloadURL": "https://www.eia.gov/electricity/data/state/avgprice_annual.xlsx"
+                    "downloadURL": "https://www.eia.gov/electricity/data/state/avgprice_annual.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Average Price by State by Provider"
                 }
             ],
+            "identifier": "DOE-019-AEPS-COLLECTION1",
             "keyword": [
                 "commercial electricity price industrial electricity price",
                 "electricity price",
                 "residential electricity price"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/state/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2016-02-16",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_861/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "1990/2012",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual Electricity Price by State"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data - Alternative Energy",
-            "description": "This API provides international data on alternative energy such as biodiesel production and consumption. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2016-02-17",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-IEDAE-Collection1",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on alternative energy such as biodiesel production and consumption. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
+            "identifier": "DOE-019-IEDAE-Collection1",
             "keyword": [
                 "API",
                 "biodiesel consumption",
@@ -21754,44 +21746,44 @@
                 "international data",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2016-02-17",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=petroleum"
             ],
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data - Alternative Energy"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data - Coal",
-            "description": "This API provides international data on coal production. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2016-02-17",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-IEDC-COLLECTION1",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on coal production. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
+            "identifier": "DOE-019-IEDC-COLLECTION1",
             "keyword": [
                 "API",
                 "anthracite coal",
@@ -21801,44 +21793,44 @@
                 "international data",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2016-02-17",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=coal"
             ],
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data - Coal"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data - Natural Gas",
-            "description": "This collection provides international data on natural gas. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2016-02-17",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-IEDNG-COLLECTION1",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This collection provides international data on natural gas. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
+            "identifier": "DOE-019-IEDNG-COLLECTION1",
             "keyword": [
                 "API",
                 "global data",
@@ -21846,43 +21838,44 @@
                 "natural gas emissions",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2016-02-17",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=natural%20gas"
             ],
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data - Natural Gas"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual Electric Power Industry Data",
-            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data.",
-            "modified": "2016-02-16",
             "accessLevel": "public",
-            "identifier": "DOE-019-AEPID-Collection1",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
+            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data.",
+            "identifier": "DOE-019-AEPID-Collection1",
             "keyword": [
                 "AMI",
                 "AMR",
@@ -21917,44 +21910,43 @@
                 "revenues",
                 "sales"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
+            "language": [
+                "us-EN"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2016-02-16",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "us-EN"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_861/form.pdf"
             ],
+            "spatial": "United States",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual Electric Power Industry Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Electricity Data - Fossil Fuels",
-            "description": "This provides data on the average cost of fossil. Data organized by fuel type, i.e., coal, bituminous coal, subbituminous coal, lignite coal, petroleum liquids, petroleum coke, and natural gas. Also by sector, i.e., electric power, electric utility, independent power producers, commercial, and industrial. Annual, quarterly, and monthly data available.  Based on Form EIA-423 and Form EIA-923 data. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2016-02-16",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-EDFF-COLLECTION1",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/electricity/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2008/2015",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This provides data on the average cost of fossil. Data organized by fuel type, i.e., coal, bituminous coal, subbituminous coal, lignite coal, petroleum liquids, petroleum coke, and natural gas. Also by sector, i.e., electric power, electric utility, independent power producers, commercial, and industrial. Annual, quarterly, and monthly data available.  Based on Form EIA-423 and Form EIA-923 data. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
+            "identifier": "DOE-019-EDFF-COLLECTION1",
             "keyword": [
                 "API",
                 "coal",
@@ -21964,46 +21956,46 @@
                 "petroleum coke",
                 "petroleum liquids"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2016-02-16",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/#eia-423",
                 "http://www.eia.gov/tools/glossary/index.cfm?id=electricity",
                 "http://www.eia.gov/survey/#eia-923"
             ],
+            "spatial": "United States",
+            "temporal": "2008/2015",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Electricity Data - Fossil Fuels"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Data - All Energy",
-            "description": "This API provides international data on energy sources (e.g., coal, electricity, natural gas, petroleum, coal, renewables) and activities (e.g., consumption, imports, exports, carbon emissions, prices, production). Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2016-02-16",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-IEDAD-COLLECTION1",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on energy sources (e.g., coal, electricity, natural gas, petroleum, coal, renewables) and activities (e.g., consumption, imports, exports, carbon emissions, prices, production). Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
+            "identifier": "DOE-019-IEDAD-COLLECTION1",
             "keyword": [
                 "API",
                 "coal price",
@@ -22027,44 +22019,44 @@
                 "petroleum reserves",
                 "petroleum stocks"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2016-02-16",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/"
             ],
-            "theme": [
-                "energy"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "International Energy Data - Petroleum and Other Liquids",
-            "description": "This API provides international data on crude oil including lease condensate production, imports, exports, and reserves. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2016-02-24",
-            "accessLevel": "restricted public",
-            "identifier": "DOE-019-IEDPOL-COLLECTION1",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
+            "spatial": "United States",
             "temporal": "1980/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
+            "theme": [
+                "energy"
+            ],
+            "title": "International Energy Data - All Energy"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides international data on crude oil including lease condensate production, imports, exports, and reserves. Data organized by country. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
+            "identifier": "DOE-019-IEDPOL-COLLECTION1",
             "keyword": [
                 "API",
                 "crude oil exports",
@@ -22075,44 +22067,44 @@
                 "international data",
                 "world data"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2016-02-24",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=petroleum"
             ],
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Data - Petroleum and Other Liquids"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Monthly Electric Utility Sales and Revenue",
-            "description": "Utility level retail sales of electricity and associated revenue. Organized by reporting month, state, and by end-use sector, i.e., residential, commercial, industrial, and transportation. Based on Form EIA-826 data.",
-            "modified": "2016-02-24",
             "accessLevel": "public",
-            "identifier": "DOE-019-MEUSR-COLLECTION1",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_826/instructions.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia826/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2008-01-01/2008-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_826/instructions.pdf",
+            "description": "Utility level retail sales of electricity and associated revenue. Organized by reporting month, state, and by end-use sector, i.e., residential, commercial, industrial, and transportation. Based on Form EIA-826 data.",
+            "identifier": "DOE-019-MEUSR-COLLECTION1",
             "keyword": [
                 "cents per kWh",
                 "commercial electric prices",
@@ -22132,44 +22124,44 @@
                 "state electric prices",
                 "transportation electric prices"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia826/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2016-02-24",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_826/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2008-01-01/2008-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Monthly Electric Utility Sales and Revenue"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Monthly Utility and Nonutility Fuel",
-            "description": "Monthly data on U.S. electric power generation, fuel consumption, stocks, and fuel heat content from utility power plants, nonutility power plants, and combined heat and power (CHP) plants. Data organized at the plant-level.  Based on Form EIA-906 data.",
-            "modified": "2016-02-24",
             "accessLevel": "public",
-            "identifier": "DOE-019-MUNF-COLLECTION1",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_923/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia923/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2002-01-01/2002-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_923/form.pdf",
+            "description": "Monthly data on U.S. electric power generation, fuel consumption, stocks, and fuel heat content from utility power plants, nonutility power plants, and combined heat and power (CHP) plants. Data organized at the plant-level.  Based on Form EIA-906 data.",
+            "identifier": "DOE-019-MUNF-COLLECTION1",
             "keyword": [
                 "coal receipts",
                 "electricity generating fuel",
@@ -22178,43 +22170,45 @@
                 "gas receipts",
                 "oil receipts"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia923/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2016-02-24",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_923/form.pdf",
                 "http://www.eia.gov/survey/form/eia_906/instructions_form.pdf",
                 "http://www.eia.gov/survey/form/eia_920/instructions_form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2002-01-01/2002-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Monthly Utility and Nonutility Fuel"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Natural Gas Data",
-            "description": "Data and statistics on natural gas prices, exploration and reserves, production, imports and exports, storage, pipelines, and consumption. Data released on a weekly, monthly and annual basis. International data on natural gas production, consumption, imports and exports, CO2 emissions, and reserves.",
-            "modified": "2016-02-24",
             "accessLevel": "public",
-            "identifier": "DOE-019-NGD-COLLECTION1",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/naturalgas/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Data and statistics on natural gas prices, exploration and reserves, production, imports and exports, storage, pipelines, and consumption. Data released on a weekly, monthly and annual basis. International data on natural gas production, consumption, imports and exports, CO2 emissions, and reserves.",
+            "identifier": "DOE-019-NGD-COLLECTION1",
             "keyword": [
                 "LNG",
                 "base gas",
@@ -22239,51 +22233,49 @@
                 "vented and flared",
                 "working gas"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/naturalgas/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2016-02-24",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Natural Gas Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual 2011 Electric Power Industry Data",
-            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
-            "modified": "2014-05-15",
             "accessLevel": "public",
-            "identifier": "DOE-019-63576357779",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
-            "issued": "2014-05-15",
-            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2011-01-01/2011-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-AEPID-Collection1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
+            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/zip/f86111.zip",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "Annual 2011 Electric Power Industry Data",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/zip/f86111.zip"
+                    "title": "Annual 2011 Electric Power Industry Data"
                 }
             ],
+            "identifier": "DOE-019-63576357779",
+            "isPartOf": "DOE-019-AEPID-Collection1",
+            "issued": "2014-05-15",
             "keyword": [
                 "AMI",
                 "AMR",
@@ -22318,54 +22310,54 @@
                 "revenues",
                 "sales"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2014-05-15",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_861/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2011-01-01/2011-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual 2011 Electric Power Industry Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual 2012 Electric Power Industry Data",
-            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
-            "modified": "2013-12-05",
             "accessLevel": "public",
-            "identifier": "DOE-019-63576357772",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
-            "issued": "2013-12-05",
-            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2012-01-01/2012-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-AEPID-Collection1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
+            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/zip/f8612012.zip",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "Annual 2012 Electric Power Industry Data",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/zip/f8612012.zip"
+                    "title": "Annual 2012 Electric Power Industry Data"
                 }
             ],
+            "identifier": "DOE-019-63576357772",
+            "isPartOf": "DOE-019-AEPID-Collection1",
+            "issued": "2013-12-05",
             "keyword": [
                 "AMI",
                 "AMR",
@@ -22400,54 +22392,54 @@
                 "revenues",
                 "sales"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2013-12-05",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_861/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2012-01-01/2012-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual 2012 Electric Power Industry Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual 2013 Electric Power Industry Data",
-            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
-            "modified": "2015-10-23",
             "accessLevel": "public",
-            "identifier": "DOE-019-63576357771",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
-            "issued": "2013-12-05",
-            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2013-01-01/2013-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-AEPID-Collection1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
+            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/zip/f8612013.zip",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "Annual 2013 Electric Power Industry Data",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/zip/f8612013.zip"
+                    "title": "Annual 2013 Electric Power Industry Data"
                 }
             ],
+            "identifier": "DOE-019-63576357771",
+            "isPartOf": "DOE-019-AEPID-Collection1",
+            "issued": "2013-12-05",
             "keyword": [
                 "AMI",
                 "AMR",
@@ -22482,54 +22474,54 @@
                 "revenues",
                 "sales"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-10-23",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_861/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2013-01-01/2013-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual 2013 Electric Power Industry Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual 2015 Electric Power Industry Data",
-            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
-            "modified": "2018-10-12",
             "accessLevel": "public",
-            "identifier": "DOE-019-63576357774",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
-            "issued": "2016-10-06",
-            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2015-01-01/2015-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-AEPID-Collection1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
+            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/zip/f8612015.zip",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "Annual Electric Power Industry Data 2015",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/zip/f8612015.zip"
+                    "title": "Annual Electric Power Industry Data 2015"
                 }
             ],
+            "identifier": "DOE-019-63576357774",
+            "isPartOf": "DOE-019-AEPID-Collection1",
+            "issued": "2016-10-06",
             "keyword": [
                 "AMI",
                 "AMR",
@@ -22564,54 +22556,54 @@
                 "revenues",
                 "sales"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2018-10-12",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_861/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2015-01-01/2015-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual 2015 Electric Power Industry Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual 2014 Electric Power Industry Data",
-            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
-            "modified": "2016-01-12",
             "accessLevel": "public",
-            "identifier": "DOE-019-63576357776",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
-            "issued": "2016-10-12",
-            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2014-01-01/2014-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-AEPID-Collection1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
+            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/zip/f8612014.zip",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "Annual 2014 Electric Power Industry Data",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/zip/f8612014.zip"
+                    "title": "Annual 2014 Electric Power Industry Data"
                 }
             ],
+            "identifier": "DOE-019-63576357776",
+            "isPartOf": "DOE-019-AEPID-Collection1",
+            "issued": "2016-10-12",
             "keyword": [
                 "AMI",
                 "AMR",
@@ -22646,101 +22638,101 @@
                 "revenues",
                 "sales"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2016-01-12",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_861/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2014-01-01/2014-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual 2014 Electric Power Industry Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Mines, Surface and Underground",
-            "description": "All operating surface and underground coal mines in the United States.",
-            "modified": "2019-01-18",
             "accessLevel": "public",
-            "identifier": "DOE-019-2332239999",
-            "dataQuality": true,
-            "describedBy": "https://www.eia.gov/survey/#eia-7a",
-            "issued": "2019-01-18",
-            "landingPage": "https://www.eia.gov/maps/layer_info-m.php",
-            "spatial": "united states",
-            "temporal": "2017-01-01/2017-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.eia.gov/survey/#eia-7a",
+            "description": "All operating surface and underground coal mines in the United States.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://www.eia.gov/maps/map_data/CoalMines_US_EIA.zip",
                     "format": "shapefile",
-                    "title": "Coal Mines, Surface and Underground",
-                    "downloadURL": "https://www.eia.gov/maps/map_data/CoalMines_US_EIA.zip"
+                    "mediaType": "application/zip",
+                    "title": "Coal Mines, Surface and Underground"
                 }
             ],
+            "identifier": "DOE-019-2332239999",
+            "issued": "2019-01-18",
             "keyword": [
                 "coal mines",
                 "surface mines",
                 "underground mines"
             ],
-            "bureauCode": [
-                "019:20"
-            ],
+            "landingPage": "https://www.eia.gov/maps/layer_info-m.php",
+            "modified": "2019-01-18",
             "programCode": [
                 "019:022"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
+            "spatial": "united states",
+            "temporal": "2017-01-01/2017-12-31",
             "theme": [
                 "geospatial"
-            ]
+            ],
+            "title": "Coal Mines, Surface and Underground"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Production by MSHA ID, Mine Operaton, Union Status, and Average Number of Employees and Hours 2016",
-            "description": "Data on U.S mining operation (i.e., operation name, mailing address, telephone number, State and county of operation, etc.), annual coal production, code definitions, and union status. Annual time series extend back to 1983. Based on EIA Form-7A data.",
-            "modified": "2018-11-02",
             "accessLevel": "public",
-            "identifier": "DOE-019-2332233223",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_7a/instructions.pdf",
-            "landingPage": "http://www.eia.gov/coal/data.cfm",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "State and County",
-            "temporal": "1991-01-01/1991-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-CPMSHAID-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_7a/instructions.pdf",
+            "description": "Data on U.S mining operation (i.e., operation name, mailing address, telephone number, State and county of operation, etc.), annual coal production, code definitions, and union status. Annual time series extend back to 1983. Based on EIA Form-7A data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "title": "Coal Production 2016",
                     "description": "Annual data on U.S. coal production, number of mines, productive capacity, recoverable reserves, employment, productivity, consumption, stocks, and prices",
-                    "downloadURL": "https://www.eia.gov/coal/data/public/xls/coalpublic2016.xls"
+                    "downloadURL": "https://www.eia.gov/coal/data/public/xls/coalpublic2016.xls",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Coal Production 2016"
                 }
             ],
+            "identifier": "DOE-019-2332233223",
+            "isPartOf": "DOE-019-CPMSHAID-COLLECTION1",
             "keyword": [
                 "coal data",
                 "coal data file",
@@ -22751,52 +22743,55 @@
                 "coal production file",
                 "energy"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/data.cfm",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2018-11-02",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_7a/form.pdf"
             ],
+            "spatial": "State and County",
+            "temporal": "1991-01-01/1991-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Production by MSHA ID, Mine Operaton, Union Status, and Average Number of Employees and Hours 2016"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual 2016 Electric Power Industry Data",
-            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
-            "modified": "2018-10-12",
             "accessLevel": "public",
-            "identifier": "DOE-019-63576357799",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
-            "landingPage": "https://www.eia.gov/electricity/data/eia861/index.php",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-AEPID-Collection1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:melinda.hobbs@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
+            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "title": "Annual 2016 Electric Power Industry Data",
                     "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/archive/zip/f8612016.zip"
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/archive/zip/f8612016.zip",
+                    "mediaType": "application/zip",
+                    "title": "Annual 2016 Electric Power Industry Data"
                 }
             ],
+            "identifier": "DOE-019-63576357799",
+            "isPartOf": "DOE-019-AEPID-Collection1",
             "keyword": [
                 "electric purchases",
                 "electric utility",
@@ -22805,50 +22800,50 @@
                 "electricity sales",
                 "net-metering"
             ],
-            "bureauCode": [
-                "019:20"
-            ],
+            "landingPage": "https://www.eia.gov/electricity/data/eia861/index.php",
+            "modified": "2018-10-12",
             "programCode": [
                 "019:220"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_861/form.pdf"
             ],
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual 2016 Electric Power Industry Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual 2017 Electric Power Industry Data",
-            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
-            "modified": "2018-10-12",
             "accessLevel": "public",
-            "identifier": "DOE-019-63576357798",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
-            "landingPage": "https://www.eia.gov/electricity/data/eia861/index.php",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-AEPID-Collection1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:melinda.hobbs@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
+            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "XLSX",
-                    "title": "Annual 2017 Electric Power Industry Data",
                     "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/zip/f8612017.zip"
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/zip/f8612017.zip",
+                    "format": "XLSX",
+                    "mediaType": "application/zip",
+                    "title": "Annual 2017 Electric Power Industry Data"
                 }
             ],
+            "identifier": "DOE-019-63576357798",
+            "isPartOf": "DOE-019-AEPID-Collection1",
             "keyword": [
                 "electric purchases",
                 "electric utility",
@@ -22857,50 +22852,47 @@
                 "electricity sales",
                 "net-metering"
             ],
-            "bureauCode": [
-                "019:20"
-            ],
+            "landingPage": "https://www.eia.gov/electricity/data/eia861/index.php",
+            "modified": "2018-10-12",
             "programCode": [
                 "019:220"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_861/form.pdf"
             ],
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual 2017 Electric Power Industry Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Company Level Petroleum Imports 2014",
-            "description": "Monthly 2014 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
-            "modified": "2015-05-12",
             "accessLevel": "public",
-            "identifier": "DOE-019-3456435499",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
-            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2013-01-01/2013-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-CLPI-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
+            "description": "Monthly 2014 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/2014/data/impa14d.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "Company Level Petroleum Imports",
-                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/2014/data/impa14d.xls"
+                    "title": "Company Level Petroleum Imports"
                 }
             ],
+            "identifier": "DOE-019-3456435499",
+            "isPartOf": "DOE-019-CLPI-COLLECTION1",
             "keyword": [
                 "company imports",
                 "crude oil imports",
@@ -22912,54 +22904,54 @@
                 "petroleum imports",
                 "residual fuel oil imports"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-05-12",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_814/form.pdf",
                 "http://www.eia.gov/survey/form/eia_814/instructions.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2013-01-01/2013-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Company Level Petroleum Imports 2014"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Company Level Petroleum Imports 2015",
-            "description": "Monthly 2015 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
-            "modified": "2016-05-12",
             "accessLevel": "public",
-            "identifier": "DOE-019-3456435498",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
-            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2013-01-01/2013-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-CLPI-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
+            "description": "Monthly 2015 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/2015/data/impa15d.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "Company Level Petroleum Imports",
-                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/2015/data/impa15d.xls"
+                    "title": "Company Level Petroleum Imports"
                 }
             ],
+            "identifier": "DOE-019-3456435498",
+            "isPartOf": "DOE-019-CLPI-COLLECTION1",
             "keyword": [
                 "company imports",
                 "crude oil imports",
@@ -22971,46 +22963,46 @@
                 "petroleum imports",
                 "residual fuel oil imports"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2016-05-12",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_814/form.pdf",
                 "http://www.eia.gov/survey/form/eia_814/instructions.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2013-01-01/2013-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Company Level Petroleum Imports 2015"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Company Level Petroleum Imports 2016",
-            "description": "Monthly 2016 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
-            "modified": "2017-05-12",
             "accessLevel": "public",
-            "identifier": "DOE-019-3456435497",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
-            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2013-01-01/2013-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-CLPI-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
+            "description": "Monthly 2016 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
+            "identifier": "DOE-019-3456435497",
+            "isPartOf": "DOE-019-CLPI-COLLECTION1",
             "keyword": [
                 "company imports",
                 "crude oil imports",
@@ -23022,54 +23014,54 @@
                 "petroleum imports",
                 "residual fuel oil imports"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2017-05-12",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_814/form.pdf",
                 "http://www.eia.gov/survey/form/eia_814/instructions.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2013-01-01/2013-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Company Level Petroleum Imports 2016"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Company Level Petroleum Imports 2017",
-            "description": "Monthly 2017 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
-            "modified": "2018-05-12",
             "accessLevel": "public",
-            "identifier": "DOE-019-3456435496",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
-            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2013-01-01/2013-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-CLPI-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
+            "description": "Monthly 2017 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/2017/data/impa17d.xlsx",
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "title": "Company Level Petroleum Imports",
-                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/2017/data/impa17d.xlsx"
+                    "title": "Company Level Petroleum Imports"
                 }
             ],
+            "identifier": "DOE-019-3456435496",
+            "isPartOf": "DOE-019-CLPI-COLLECTION1",
             "keyword": [
                 "company imports",
                 "crude oil imports",
@@ -23081,54 +23073,54 @@
                 "petroleum imports",
                 "residual fuel oil imports"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2018-05-12",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_814/form.pdf",
                 "http://www.eia.gov/survey/form/eia_814/instructions.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2013-01-01/2013-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Company Level Petroleum Imports 2017"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Monthly 2013 Utility and Nonutility Fuel Receipts and Fuel Quality Data",
-            "description": "Monthly 2013 data on U.S. electric power generation and fuel consumption, stocks, receipts, quality, costs, fuel supplier, and coal mine source from utility power plants, nonutility power plants, and combined heat and power (CHP) plants. Data organized at the plant-level.  Based on Form EIA-923 data. Monthly time series extend back to 2001.",
-            "modified": "2014-12-04",
             "accessLevel": "public",
-            "identifier": "DOE-019-5463727499",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_923/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia923/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2012-01-01/2012-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-MUNF-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_923/form.pdf",
+            "description": "Monthly 2013 data on U.S. electric power generation and fuel consumption, stocks, receipts, quality, costs, fuel supplier, and coal mine source from utility power plants, nonutility power plants, and combined heat and power (CHP) plants. Data organized at the plant-level.  Based on Form EIA-923 data. Monthly time series extend back to 2001.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia923/archive/xls/f923_2013.zip",
                     "mediaType": "application/zip",
-                    "title": "Monthly Utility and Nonutility Fuel 2013",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia923/archive/xls/f923_2013.zip"
+                    "title": "Monthly Utility and Nonutility Fuel 2013"
                 }
             ],
+            "identifier": "DOE-019-5463727499",
+            "isPartOf": "DOE-019-MUNF-COLLECTION1",
             "keyword": [
                 "coal receipts",
                 "electricity generating fuels",
@@ -23137,53 +23129,53 @@
                 "gas receipts",
                 "oil receipts"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia923/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2014-12-04",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_923/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2012-01-01/2012-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Monthly 2013 Utility and Nonutility Fuel Receipts and Fuel Quality Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Monthly 2014 Utility and Nonutility Fuel Receipts and Fuel Quality Data",
-            "description": "Monthly 2014 data on U.S. electric power generation and fuel consumption, stocks, receipts, quality, costs, fuel supplier, and coal mine source from utility power plants, nonutility power plants, and combined heat and power (CHP) plants. Data organized at the plant-level.  Based on Form EIA-923 data. Monthly time series extend back to 2001.",
-            "modified": "2021-03-03T20:15:50.032Z",
             "accessLevel": "public",
-            "identifier": "DOE-019-5463727493",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_923/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia923/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "rights": "true",
-            "temporal": "2012-01-01/2012-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-MUNF-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_923/form.pdf",
+            "description": "Monthly 2014 data on U.S. electric power generation and fuel consumption, stocks, receipts, quality, costs, fuel supplier, and coal mine source from utility power plants, nonutility power plants, and combined heat and power (CHP) plants. Data organized at the plant-level.  Based on Form EIA-923 data. Monthly time series extend back to 2001.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia923/archive/xls/f923_2014.zip",
                     "mediaType": "application/zip",
-                    "title": "Monthly Utility and Nonutility Fuel 2014",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia923/archive/xls/f923_2014.zip"
+                    "title": "Monthly Utility and Nonutility Fuel 2014"
                 }
             ],
+            "identifier": "DOE-019-5463727493",
+            "isPartOf": "DOE-019-MUNF-COLLECTION1",
             "keyword": [
                 "coal receipts",
                 "electricity generating fuels",
@@ -23192,50 +23184,50 @@
                 "gas receipts",
                 "oil receipts"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia923/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2021-03-03T20:15:50.032Z",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_923/form.pdf"
-            ]
+            ],
+            "rights": "true",
+            "temporal": "2012-01-01/2012-12-31",
+            "title": "Monthly 2014 Utility and Nonutility Fuel Receipts and Fuel Quality Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Monthly 2015 Utility and Nonutility Fuel Receipts and Fuel Quality Data",
-            "description": "Monthly 2015 data on U.S. electric power generation and fuel consumption, stocks, receipts, quality, costs, fuel supplier, and coal mine source from utility power plants, nonutility power plants, and combined heat and power (CHP) plants. Data organized at the plant-level.  Based on Form EIA-923 data. Monthly time series extend back to 2001.",
-            "modified": "2016-12-04",
             "accessLevel": "public",
-            "identifier": "DOE-019-5463727497",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_923/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia923/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2012-01-01/2012-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-MUNF-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_923/form.pdf",
+            "description": "Monthly 2015 data on U.S. electric power generation and fuel consumption, stocks, receipts, quality, costs, fuel supplier, and coal mine source from utility power plants, nonutility power plants, and combined heat and power (CHP) plants. Data organized at the plant-level.  Based on Form EIA-923 data. Monthly time series extend back to 2001.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia923/archive/xls/f923_2015.zip",
                     "mediaType": "application/zip",
-                    "title": "Monthly Utility and Nonutility Fuel 2015",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia923/archive/xls/f923_2015.zip"
+                    "title": "Monthly Utility and Nonutility Fuel 2015"
                 }
             ],
+            "identifier": "DOE-019-5463727497",
+            "isPartOf": "DOE-019-MUNF-COLLECTION1",
             "keyword": [
                 "coal receipts",
                 "electricity generating fuels",
@@ -23244,53 +23236,53 @@
                 "gas receipts",
                 "oil receipts"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia923/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2016-12-04",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_923/form.pdf"
             ],
-            "theme": [
-                "energy"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Monthly 2016 Utility and Nonutility Fuel Receipts and Fuel Quality Data",
-            "description": "Monthly 2016 data on U.S. electric power generation and fuel consumption, stocks, receipts, quality, costs, fuel supplier, and coal mine source from utility power plants, nonutility power plants, and combined heat and power (CHP) plants. Data organized at the plant-level.  Based on Form EIA-923 data. Monthly time series extend back to 2001.",
-            "modified": "2017-12-04",
-            "accessLevel": "public",
-            "identifier": "DOE-019-5463727496",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_923/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia923/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
             "spatial": "United States",
             "temporal": "2012-01-01/2012-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
+            "theme": [
+                "energy"
+            ],
+            "title": "Monthly 2015 Utility and Nonutility Fuel Receipts and Fuel Quality Data"
         },
-            "isPartOf": "DOE-019-MUNF-COLLECTION1",
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_923/form.pdf",
+            "description": "Monthly 2016 data on U.S. electric power generation and fuel consumption, stocks, receipts, quality, costs, fuel supplier, and coal mine source from utility power plants, nonutility power plants, and combined heat and power (CHP) plants. Data organized at the plant-level.  Based on Form EIA-923 data. Monthly time series extend back to 2001.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia923/archive/xls/f923_2016.zip",
                     "mediaType": "application/zip",
-                    "title": "Monthly Utility and Nonutility Fuel 2016",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia923/archive/xls/f923_2016.zip"
+                    "title": "Monthly Utility and Nonutility Fuel 2016"
                 }
             ],
+            "identifier": "DOE-019-5463727496",
+            "isPartOf": "DOE-019-MUNF-COLLECTION1",
             "keyword": [
                 "coal receipts",
                 "electricity generating fuels",
@@ -23299,53 +23291,53 @@
                 "gas receipts",
                 "oil receipts"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia923/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2017-12-04",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_923/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2012-01-01/2012-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Monthly 2016 Utility and Nonutility Fuel Receipts and Fuel Quality Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Monthly 2017 Utility and Nonutility Fuel Receipts and Fuel Quality Data",
-            "description": "Monthly 2017 data on U.S. electric power generation and fuel consumption, stocks, receipts, quality, costs, fuel supplier, and coal mine source from utility power plants, nonutility power plants, and combined heat and power (CHP) plants. Data organized at the plant-level.  Based on Form EIA-923 data. Monthly time series extend back to 2001.",
-            "modified": "2018-12-04",
             "accessLevel": "public",
-            "identifier": "DOE-019-5463727495",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_923/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia923/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2012-01-01/2012-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-MUNF-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_923/form.pdf",
+            "description": "Monthly 2017 data on U.S. electric power generation and fuel consumption, stocks, receipts, quality, costs, fuel supplier, and coal mine source from utility power plants, nonutility power plants, and combined heat and power (CHP) plants. Data organized at the plant-level.  Based on Form EIA-923 data. Monthly time series extend back to 2001.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia923/xls/f923_2017.zip",
                     "mediaType": "application/zip",
-                    "title": "Monthly Utility and Nonutility Fuel 2017",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia923/xls/f923_2017.zip"
+                    "title": "Monthly Utility and Nonutility Fuel 2017"
                 }
             ],
+            "identifier": "DOE-019-5463727495",
+            "isPartOf": "DOE-019-MUNF-COLLECTION1",
             "keyword": [
                 "coal receipts",
                 "electricity generating fuels",
@@ -23354,53 +23346,53 @@
                 "gas receipts",
                 "oil receipts"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia923/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2018-12-04",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_923/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2012-01-01/2012-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Monthly 2017 Utility and Nonutility Fuel Receipts and Fuel Quality Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Monthly Electric Utility Sales and Revenue Data 2013",
-            "description": "Utility level retail sales of electricity and associated revenue in 2013. Organized by reporting month, state, and by end-use sector, i.e., residential, commercial, industrial, and transportation. Based on Form EIA-826 data.",
-            "modified": "2014-12-18",
             "accessLevel": "public",
-            "identifier": "DOE-019-4567895699",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_826/instructions.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia826/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2013-01-01/2013-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-MEUSR-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_826/instructions.pdf",
+            "description": "Utility level retail sales of electricity and associated revenue in 2013. Organized by reporting month, state, and by end-use sector, i.e., residential, commercial, industrial, and transportation. Based on Form EIA-826 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia861m/archive/xls/f8262013.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "Monthly Electric Utility Sales and Revenue 2013",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia861m/archive/xls/f8262013.xls"
+                    "title": "Monthly Electric Utility Sales and Revenue 2013"
                 }
             ],
+            "identifier": "DOE-019-4567895699",
+            "isPartOf": "DOE-019-MEUSR-COLLECTION1",
             "keyword": [
                 "cents per kWh",
                 "commercial electric prices",
@@ -23420,53 +23412,53 @@
                 "state electric prices",
                 "transportation electric prices"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia826/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2014-12-18",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_826/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2013-01-01/2013-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Monthly Electric Utility Sales and Revenue Data 2013"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Monthly Electric Utility Sales and Revenue Data 2014",
-            "description": "Utility level retail sales of electricity and associated revenue in 2014. Organized by reporting month, state, and by end-use sector, i.e., residential, commercial, industrial, and transportation. Based on Form EIA-826 data.",
-            "modified": "2015-12-18",
             "accessLevel": "public",
-            "identifier": "DOE-019-4567895698",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_826/instructions.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia826/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2013-01-01/2013-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-MEUSR-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_826/instructions.pdf",
+            "description": "Utility level retail sales of electricity and associated revenue in 2014. Organized by reporting month, state, and by end-use sector, i.e., residential, commercial, industrial, and transportation. Based on Form EIA-826 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia861m/archive/xls/f8262014.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "Monthly Electric Utility Sales and Revenue 2014",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia861m/archive/xls/f8262014.xls"
+                    "title": "Monthly Electric Utility Sales and Revenue 2014"
                 }
             ],
+            "identifier": "DOE-019-4567895698",
+            "isPartOf": "DOE-019-MEUSR-COLLECTION1",
             "keyword": [
                 "cents per kWh",
                 "commercial electric prices",
@@ -23486,53 +23478,53 @@
                 "state electric prices",
                 "transportation electric prices"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia826/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-12-18",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_826/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2013-01-01/2013-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Monthly Electric Utility Sales and Revenue Data 2014"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Monthly Electric Utility Sales and Revenue Data 2015",
-            "description": "Utility level retail sales of electricity and associated revenue in 2015. Organized by reporting month, state, and by end-use sector, i.e., residential, commercial, industrial, and transportation. Based on Form EIA-826 data.",
-            "modified": "2016-12-18",
             "accessLevel": "public",
-            "identifier": "DOE-019-4567895697",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_826/instructions.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia826/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2013-01-01/2013-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-MEUSR-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_826/instructions.pdf",
+            "description": "Utility level retail sales of electricity and associated revenue in 2015. Organized by reporting month, state, and by end-use sector, i.e., residential, commercial, industrial, and transportation. Based on Form EIA-826 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia861m/archive/xls/f8262015.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "Monthly Electric Utility Sales and Revenue 2015",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia861m/archive/xls/f8262015.xls"
+                    "title": "Monthly Electric Utility Sales and Revenue 2015"
                 }
             ],
+            "identifier": "DOE-019-4567895697",
+            "isPartOf": "DOE-019-MEUSR-COLLECTION1",
             "keyword": [
                 "cents per kWh",
                 "commercial electric prices",
@@ -23552,53 +23544,53 @@
                 "state electric prices",
                 "transportation electric prices"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia826/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2016-12-18",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_826/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2013-01-01/2013-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Monthly Electric Utility Sales and Revenue Data 2015"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Monthly Electric Utility Sales and Revenue Data 2016",
-            "description": "Utility level retail sales of electricity and associated revenue in 2016. Organized by reporting month, state, and by end-use sector, i.e., residential, commercial, industrial, and transportation. Based on Form EIA-826 data.",
-            "modified": "2017-12-18",
             "accessLevel": "public",
-            "identifier": "DOE-019-4567895696",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_826/instructions.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia826/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2013-01-01/2013-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-MEUSR-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_826/instructions.pdf",
+            "description": "Utility level retail sales of electricity and associated revenue in 2016. Organized by reporting month, state, and by end-use sector, i.e., residential, commercial, industrial, and transportation. Based on Form EIA-826 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia861m/archive/xls/f8262016.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "Monthly Electric Utility Sales and Revenue 2016",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia861m/archive/xls/f8262016.xls"
+                    "title": "Monthly Electric Utility Sales and Revenue 2016"
                 }
             ],
+            "identifier": "DOE-019-4567895696",
+            "isPartOf": "DOE-019-MEUSR-COLLECTION1",
             "keyword": [
                 "cents per kWh",
                 "commercial electric prices",
@@ -23618,45 +23610,45 @@
                 "state electric prices",
                 "transportation electric prices"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia826/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2017-12-18",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_826/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2013-01-01/2013-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Monthly Electric Utility Sales and Revenue Data 2016"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Monthly Electric Utility Sales and Revenue Data 2017",
-            "description": "Utility level retail sales of electricity and associated revenue in 2017. Organized by reporting month, state, and by end-use sector, i.e., residential, commercial, industrial, and transportation. Based on Form EIA-826 data.",
-            "modified": "2018-12-18",
             "accessLevel": "public",
-            "identifier": "DOE-019-4567895695",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_826/instructions.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia826/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2013-01-01/2013-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-MEUSR-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_826/instructions.pdf",
+            "description": "Utility level retail sales of electricity and associated revenue in 2017. Organized by reporting month, state, and by end-use sector, i.e., residential, commercial, industrial, and transportation. Based on Form EIA-826 data.",
+            "identifier": "DOE-019-4567895695",
+            "isPartOf": "DOE-019-MEUSR-COLLECTION1",
             "keyword": [
                 "cents per kWh",
                 "commercial electric prices",
@@ -23676,54 +23668,54 @@
                 "state electric prices",
                 "transportation electric prices"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia826/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2018-12-18",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_826/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2013-01-01/2013-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Monthly Electric Utility Sales and Revenue Data 2017"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual 2011 Electric Generator Report",
-            "description": "Annual U.S. generator level data about generators at electric power plants owned and operated by electric utilities and nonutilities (including independent power producers, combined heat and power producers, and other industrials). Based on EIA Form-860 data. Data contained in a zip file.                                                                                                                                                        The zip file contains generator-specific information such as initial date of commercial operation, prime movers, generating capacity, energy sources, status of existing and proposed generators, proposed changes to existing generators, county and State location (including power plant address), ownership, and FERC qualifying facility status. The file also includes data on the ability to use multiple fuels; specifically, data on co-firing and fuel switching are included.",
-            "modified": "2012-01-15",
             "accessLevel": "public",
-            "identifier": "DOE-019-6358888878",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_860/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia860/index.html",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2010-01-01/2010-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-EIA-AEGR-COLL1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_860/form.pdf",
+            "description": "Annual U.S. generator level data about generators at electric power plants owned and operated by electric utilities and nonutilities (including independent power producers, combined heat and power producers, and other industrials). Based on EIA Form-860 data. Data contained in a zip file.                                                                                                                                                        The zip file contains generator-specific information such as initial date of commercial operation, prime movers, generating capacity, energy sources, status of existing and proposed generators, proposed changes to existing generators, county and State location (including power plant address), ownership, and FERC qualifying facility status. The file also includes data on the ability to use multiple fuels; specifically, data on co-firing and fuel switching are included.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia860/xls/eia8602011.zip",
                     "mediaType": "application/zip",
-                    "title": "Annual 2011 Electric Generator Report",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia860/xls/eia8602011.zip"
+                    "title": "Annual 2011 Electric Generator Report"
                 }
             ],
+            "identifier": "DOE-019-6358888878",
+            "isPartOf": "DOE-019-EIA-AEGR-COLL1",
             "keyword": [
                 "EIA-860",
                 "annual data",
@@ -23750,54 +23742,54 @@
                 "winter capability",
                 "winter capacity"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia860/index.html",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2012-01-15",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_860/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2010-01-01/2010-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual 2011 Electric Generator Report"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual 2012 Electric Generator Report",
-            "description": "Annual U.S. generator level data about generators at electric power plants owned and operated by electric utilities and nonutilities (including independent power producers, combined heat and power producers, and other industrials). Based on EIA Form-860 data. Data contained in a zip file.                                                                                                                                                        The zip file contains generator-specific information such as initial date of commercial operation, prime movers, generating capacity, energy sources, status of existing and proposed generators, proposed changes to existing generators, county and State location (including power plant address), ownership, and FERC qualifying facility status. The file also includes data on the ability to use multiple fuels; specifically, data on co-firing and fuel switching are included.",
-            "modified": "2013-01-15",
             "accessLevel": "public",
-            "identifier": "DOE-019-6358888868",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_860/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia860/index.html",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2010-01-01/2010-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-EIA-AEGR-COLL1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_860/form.pdf",
+            "description": "Annual U.S. generator level data about generators at electric power plants owned and operated by electric utilities and nonutilities (including independent power producers, combined heat and power producers, and other industrials). Based on EIA Form-860 data. Data contained in a zip file.                                                                                                                                                        The zip file contains generator-specific information such as initial date of commercial operation, prime movers, generating capacity, energy sources, status of existing and proposed generators, proposed changes to existing generators, county and State location (including power plant address), ownership, and FERC qualifying facility status. The file also includes data on the ability to use multiple fuels; specifically, data on co-firing and fuel switching are included.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia860/xls/eia8602012.zip",
                     "mediaType": "application/zip",
-                    "title": "Annual 2012 Electric Generator Report",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia860/xls/eia8602012.zip"
+                    "title": "Annual 2012 Electric Generator Report"
                 }
             ],
+            "identifier": "DOE-019-6358888868",
+            "isPartOf": "DOE-019-EIA-AEGR-COLL1",
             "keyword": [
                 "EIA-860",
                 "annual data",
@@ -23824,54 +23816,54 @@
                 "winter capability",
                 "winter capacity"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia860/index.html",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2013-01-15",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_860/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2010-01-01/2010-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual 2012 Electric Generator Report"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual 2013 Electric Generator Report",
-            "description": "Annual U.S. generator level data about generators at electric power plants owned and operated by electric utilities and nonutilities (including independent power producers, combined heat and power producers, and other industrials). Based on EIA Form-860 data. Data contained in a zip file.                                                                                                                                                        The zip file contains generator-specific information such as initial date of commercial operation, prime movers, generating capacity, energy sources, status of existing and proposed generators, proposed changes to existing generators, county and State location (including power plant address), ownership, and FERC qualifying facility status. The file also includes data on the ability to use multiple fuels; specifically, data on co-firing and fuel switching are included.",
-            "modified": "2014-01-15",
             "accessLevel": "public",
-            "identifier": "DOE-019-6358888858",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_860/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia860/index.html",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2010-01-01/2010-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-EIA-AEGR-COLL1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_860/form.pdf",
+            "description": "Annual U.S. generator level data about generators at electric power plants owned and operated by electric utilities and nonutilities (including independent power producers, combined heat and power producers, and other industrials). Based on EIA Form-860 data. Data contained in a zip file.                                                                                                                                                        The zip file contains generator-specific information such as initial date of commercial operation, prime movers, generating capacity, energy sources, status of existing and proposed generators, proposed changes to existing generators, county and State location (including power plant address), ownership, and FERC qualifying facility status. The file also includes data on the ability to use multiple fuels; specifically, data on co-firing and fuel switching are included.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia860/xls/eia8602013.zip",
                     "mediaType": "application/zip",
-                    "title": "Annual 2013 Electric Generator Report",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia860/xls/eia8602013.zip"
+                    "title": "Annual 2013 Electric Generator Report"
                 }
             ],
+            "identifier": "DOE-019-6358888858",
+            "isPartOf": "DOE-019-EIA-AEGR-COLL1",
             "keyword": [
                 "EIA-860",
                 "annual data",
@@ -23898,54 +23890,54 @@
                 "winter capability",
                 "winter capacity"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia860/index.html",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2014-01-15",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_860/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2010-01-01/2010-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual 2013 Electric Generator Report"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual 2017 Electric Generator Report",
-            "description": "Annual U.S. generator level data about generators at electric power plants owned and operated by electric utilities and nonutilities (including independent power producers, combined heat and power producers, and other industrials). Based on EIA Form-860 data. Data contained in a zip file.                                                                                                                                                        The zip file contains generator-specific information such as initial date of commercial operation, prime movers, generating capacity, energy sources, status of existing and proposed generators, proposed changes to existing generators, county and State location (including power plant address), ownership, and FERC qualifying facility status. The file also includes data on the ability to use multiple fuels; specifically, data on co-firing and fuel switching are included.",
-            "modified": "2018-09-13",
             "accessLevel": "public",
-            "identifier": "DOE-019-6358888818",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_860/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia860/index.html",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2010-01-01/2010-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-EIA-AEGR-COLL1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_860/form.pdf",
+            "description": "Annual U.S. generator level data about generators at electric power plants owned and operated by electric utilities and nonutilities (including independent power producers, combined heat and power producers, and other industrials). Based on EIA Form-860 data. Data contained in a zip file.                                                                                                                                                        The zip file contains generator-specific information such as initial date of commercial operation, prime movers, generating capacity, energy sources, status of existing and proposed generators, proposed changes to existing generators, county and State location (including power plant address), ownership, and FERC qualifying facility status. The file also includes data on the ability to use multiple fuels; specifically, data on co-firing and fuel switching are included.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia860/xls/eia8602017.zip",
                     "mediaType": "application/zip",
-                    "title": "Annual 2017 Electric Generator Report",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia860/xls/eia8602017.zip"
+                    "title": "Annual 2017 Electric Generator Report"
                 }
             ],
+            "identifier": "DOE-019-6358888818",
+            "isPartOf": "DOE-019-EIA-AEGR-COLL1",
             "keyword": [
                 "EIA-860",
                 "annual data",
@@ -23972,54 +23964,54 @@
                 "winter capability",
                 "winter capacity"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia860/index.html",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2018-09-13",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_860/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2010-01-01/2010-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual 2017 Electric Generator Report"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual 2014 Electric Generator Report",
-            "description": "Annual U.S. generator level data about generators at electric power plants owned and operated by electric utilities and nonutilities (including independent power producers, combined heat and power producers, and other industrials). Based on EIA Form-860 data. Data contained in a zip file.                                                                                                                                                        The zip file contains generator-specific information such as initial date of commercial operation, prime movers, generating capacity, energy sources, status of existing and proposed generators, proposed changes to existing generators, county and State location (including power plant address), ownership, and FERC qualifying facility status. The file also includes data on the ability to use multiple fuels; specifically, data on co-firing and fuel switching are included.",
-            "modified": "2015-01-15",
             "accessLevel": "public",
-            "identifier": "DOE-019-6358888848",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_860/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia860/index.html",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2010-01-01/2010-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-EIA-AEGR-COLL1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_860/form.pdf",
+            "description": "Annual U.S. generator level data about generators at electric power plants owned and operated by electric utilities and nonutilities (including independent power producers, combined heat and power producers, and other industrials). Based on EIA Form-860 data. Data contained in a zip file.                                                                                                                                                        The zip file contains generator-specific information such as initial date of commercial operation, prime movers, generating capacity, energy sources, status of existing and proposed generators, proposed changes to existing generators, county and State location (including power plant address), ownership, and FERC qualifying facility status. The file also includes data on the ability to use multiple fuels; specifically, data on co-firing and fuel switching are included.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia860/xls/eia8602014.zip",
                     "mediaType": "application/zip",
-                    "title": "Annual 2014 Electric Generator Report",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia860/xls/eia8602014.zip"
+                    "title": "Annual 2014 Electric Generator Report"
                 }
             ],
+            "identifier": "DOE-019-6358888848",
+            "isPartOf": "DOE-019-EIA-AEGR-COLL1",
             "keyword": [
                 "EIA-860",
                 "annual data",
@@ -24046,54 +24038,54 @@
                 "winter capability",
                 "winter capacity"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia860/index.html",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-01-15",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_860/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2010-01-01/2010-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual 2014 Electric Generator Report"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual 2015 Electric Generator Report",
-            "description": "Annual U.S. generator level data about generators at electric power plants owned and operated by electric utilities and nonutilities (including independent power producers, combined heat and power producers, and other industrials). Based on EIA Form-860 data. Data contained in a zip file.                                                                                                                                                        The zip file contains generator-specific information such as initial date of commercial operation, prime movers, generating capacity, energy sources, status of existing and proposed generators, proposed changes to existing generators, county and State location (including power plant address), ownership, and FERC qualifying facility status. The file also includes data on the ability to use multiple fuels; specifically, data on co-firing and fuel switching are included.",
-            "modified": "2016-01-15",
             "accessLevel": "public",
-            "identifier": "DOE-019-6358888838",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_860/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia860/index.html",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2010-01-01/2010-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-EIA-AEGR-COLL1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_860/form.pdf",
+            "description": "Annual U.S. generator level data about generators at electric power plants owned and operated by electric utilities and nonutilities (including independent power producers, combined heat and power producers, and other industrials). Based on EIA Form-860 data. Data contained in a zip file.                                                                                                                                                        The zip file contains generator-specific information such as initial date of commercial operation, prime movers, generating capacity, energy sources, status of existing and proposed generators, proposed changes to existing generators, county and State location (including power plant address), ownership, and FERC qualifying facility status. The file also includes data on the ability to use multiple fuels; specifically, data on co-firing and fuel switching are included.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia860/xls/eia8602015.zip",
                     "mediaType": "application/zip",
-                    "title": "Annual 2015 Electric Generator Report",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia860/xls/eia8602015.zip"
+                    "title": "Annual 2015 Electric Generator Report"
                 }
             ],
+            "identifier": "DOE-019-6358888838",
+            "isPartOf": "DOE-019-EIA-AEGR-COLL1",
             "keyword": [
                 "EIA-860",
                 "annual data",
@@ -24120,54 +24112,54 @@
                 "winter capability",
                 "winter capacity"
             ],
-            "bureauCode": [
-                "019:20"
-            ],
-            "programCode": [
-                "019:022"
-            ],
+            "landingPage": "http://www.eia.gov/electricity/data/eia860/index.html",
             "language": [
                 "en-US"
             ],
-            "references": [
-                "http://www.eia.gov/survey/form/eia_860/form.pdf"
-            ],
-            "theme": [
-                "energy"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual 2016 Electric Generator Report",
-            "description": "Annual U.S. generator level data about generators at electric power plants owned and operated by electric utilities and nonutilities (including independent power producers, combined heat and power producers, and other industrials). Based on EIA Form-860 data. Data contained in a zip file.                                                                                                                                                        The zip file contains generator-specific information such as initial date of commercial operation, prime movers, generating capacity, energy sources, status of existing and proposed generators, proposed changes to existing generators, county and State location (including power plant address), ownership, and FERC qualifying facility status. The file also includes data on the ability to use multiple fuels; specifically, data on co-firing and fuel switching are included.",
-            "modified": "2017-01-15",
-            "accessLevel": "public",
-            "identifier": "DOE-019-6358888828",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_860/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia860/index.html",
             "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2010-01-01/2010-12-31",
+            "modified": "2016-01-15",
+            "programCode": [
+                "019:022"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Energy Information Administration"
             },
+            "references": [
+                "http://www.eia.gov/survey/form/eia_860/form.pdf"
+            ],
+            "spatial": "United States",
+            "temporal": "2010-01-01/2010-12-31",
+            "theme": [
+                "energy"
+            ],
+            "title": "Annual 2015 Electric Generator Report"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-EIA-AEGR-COLL1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_860/form.pdf",
+            "description": "Annual U.S. generator level data about generators at electric power plants owned and operated by electric utilities and nonutilities (including independent power producers, combined heat and power producers, and other industrials). Based on EIA Form-860 data. Data contained in a zip file.                                                                                                                                                        The zip file contains generator-specific information such as initial date of commercial operation, prime movers, generating capacity, energy sources, status of existing and proposed generators, proposed changes to existing generators, county and State location (including power plant address), ownership, and FERC qualifying facility status. The file also includes data on the ability to use multiple fuels; specifically, data on co-firing and fuel switching are included.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia860/xls/eia8602016.zip",
                     "mediaType": "application/zip",
-                    "title": "Annual 2016 Electric Generator Report",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia860/xls/eia8602016.zip"
+                    "title": "Annual 2016 Electric Generator Report"
                 }
             ],
+            "identifier": "DOE-019-6358888828",
+            "isPartOf": "DOE-019-EIA-AEGR-COLL1",
             "keyword": [
                 "EIA-860",
                 "annual data",
@@ -24194,53 +24186,53 @@
                 "winter capability",
                 "winter capacity"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia860/index.html",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2017-01-15",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_860/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2010-01-01/2010-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual 2016 Electric Generator Report"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual 2000 Electric Power Industry Data",
-            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
-            "modified": "2007-03-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-3973434320",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2001-01-01/2001-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-AEPID-Collection1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
+            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/archive/zip/f86100.zip",
                     "mediaType": "application/zip",
-                    "title": "2000 EPI data EIA-861",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/archive/zip/f86100.zip"
+                    "title": "2000 EPI data EIA-861"
                 }
             ],
+            "identifier": "DOE-019-3973434320",
+            "isPartOf": "DOE-019-AEPID-Collection1",
             "keyword": [
                 "AMI",
                 "AMR",
@@ -24275,53 +24267,53 @@
                 "revenues",
                 "sales"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
+            "language": [
+                "us-EN"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2007-03-01",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "us-EN"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_861/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2001-01-01/2001-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual 2000 Electric Power Industry Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual 1999 Electric Power Industry Data",
-            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
-            "modified": "2007-03-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-3973434319",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2001-01-01/2001-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-AEPID-Collection1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
+            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/archive/zip/f86199.zip",
                     "mediaType": "application/zip",
-                    "title": "1999 EPI Data EIA-861",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/archive/zip/f86199.zip"
+                    "title": "1999 EPI Data EIA-861"
                 }
             ],
+            "identifier": "DOE-019-3973434319",
+            "isPartOf": "DOE-019-AEPID-Collection1",
             "keyword": [
                 "AMI",
                 "AMR",
@@ -24356,53 +24348,53 @@
                 "revenues",
                 "sales"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
+            "language": [
+                "us-EN"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2007-03-01",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "us-EN"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_861/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2001-01-01/2001-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual 1999 Electric Power Industry Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual 1998 Electric Power Industry Data",
-            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
-            "modified": "2007-03-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-3973434318",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2001-01-01/2001-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-AEPID-Collection1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
+            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/archive/zip/f86198.zip",
                     "mediaType": "application/zip",
-                    "title": "1998 EPI Data EIA-861",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/archive/zip/f86198.zip"
+                    "title": "1998 EPI Data EIA-861"
                 }
             ],
+            "identifier": "DOE-019-3973434318",
+            "isPartOf": "DOE-019-AEPID-Collection1",
             "keyword": [
                 "AMI",
                 "AMR",
@@ -24437,53 +24429,53 @@
                 "revenues",
                 "sales"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
+            "language": [
+                "us-EN"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2007-03-01",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "us-EN"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_861/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2001-01-01/2001-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual 1998 Electric Power Industry Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual 1997 Electric Power Industry Data",
-            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
-            "modified": "2007-03-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-3973434317",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2001-01-01/2001-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-AEPID-Collection1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
+            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/archive/zip/f86197.zip",
                     "mediaType": "application/zip",
-                    "title": "1997 EPI Data EIA-861",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/archive/zip/f86197.zip"
+                    "title": "1997 EPI Data EIA-861"
                 }
             ],
+            "identifier": "DOE-019-3973434317",
+            "isPartOf": "DOE-019-AEPID-Collection1",
             "keyword": [
                 "AMI",
                 "AMR",
@@ -24518,53 +24510,53 @@
                 "revenues",
                 "sales"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
+            "language": [
+                "us-EN"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2007-03-01",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "us-EN"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_861/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2001-01-01/2001-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual 1997 Electric Power Industry Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual 1996 Electric Power Industry Data",
-            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
-            "modified": "2007-03-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-3973434316",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2001-01-01/2001-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-AEPID-Collection1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
+            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/archive/zip/f86196.zip",
                     "mediaType": "application/zip",
-                    "title": "1996 EPI Data EIA-861",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/archive/zip/f86196.zip"
+                    "title": "1996 EPI Data EIA-861"
                 }
             ],
+            "identifier": "DOE-019-3973434316",
+            "isPartOf": "DOE-019-AEPID-Collection1",
             "keyword": [
                 "AMI",
                 "AMR",
@@ -24599,53 +24591,53 @@
                 "revenues",
                 "sales"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
+            "language": [
+                "us-EN"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2007-03-01",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "us-EN"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_861/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2001-01-01/2001-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual 1996 Electric Power Industry Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual 1995 Electric Power Industry Data",
-            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
-            "modified": "2007-03-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-3973434315",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2001-01-01/2001-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-AEPID-Collection1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
+            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/archive/zip/f86195.zip",
                     "mediaType": "application/zip",
-                    "title": "1995 EPI Data EIA-861",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/archive/zip/f86195.zip"
+                    "title": "1995 EPI Data EIA-861"
                 }
             ],
+            "identifier": "DOE-019-3973434315",
+            "isPartOf": "DOE-019-AEPID-Collection1",
             "keyword": [
                 "AMI",
                 "AMR",
@@ -24680,53 +24672,53 @@
                 "revenues",
                 "sales"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
+            "language": [
+                "us-EN"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2007-03-01",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "us-EN"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_861/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2001-01-01/2001-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual 1995 Electric Power Industry Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual 1994 Electric Power Industry Data",
-            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
-            "modified": "2007-03-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-3973434314",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2001-01-01/2001-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-AEPID-Collection1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
+            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/archive/zip/f86194.zip",
                     "mediaType": "application/zip",
-                    "title": "1994 EPI Data EIA-861",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/archive/zip/f86194.zip"
+                    "title": "1994 EPI Data EIA-861"
                 }
             ],
+            "identifier": "DOE-019-3973434314",
+            "isPartOf": "DOE-019-AEPID-Collection1",
             "keyword": [
                 "AMI",
                 "AMR",
@@ -24761,54 +24753,54 @@
                 "revenues",
                 "sales"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
+            "language": [
+                "us-EN"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2007-03-01",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "us-EN"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_861/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2001-01-01/2001-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual 1994 Electric Power Industry Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual 1993 Electric Power Industry Data",
-            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
-            "modified": "2007-03-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-3973434313",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2001-01-01/2001-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-AEPID-Collection1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
+            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/archive/zip/f86193.zip",
                     "mediaType": "application/zip",
-                    "title": "1993 EPI Data EIA-861",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/archive/zip/f86193.zip"
+                    "title": "1993 EPI Data EIA-861"
                 }
             ],
+            "identifier": "DOE-019-3973434313",
+            "isPartOf": "DOE-019-AEPID-Collection1",
             "keyword": [
                 "AMI",
                 "AMR",
@@ -24843,54 +24835,54 @@
                 "revenues",
                 "sales"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
+            "language": [
+                "us-EN"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2007-03-01",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "us-EN"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_861/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2001-01-01/2001-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual 1993 Electric Power Industry Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual 1992 Electric Power Industry Data",
-            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
-            "modified": "2007-03-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-3973434312",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2001-01-01/2001-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-AEPID-Collection1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
+            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/archive/zip/f86192.zip",
                     "mediaType": "application/zip",
-                    "title": "1992 EPI Data EIA-861",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/archive/zip/f86192.zip"
+                    "title": "1992 EPI Data EIA-861"
                 }
             ],
+            "identifier": "DOE-019-3973434312",
+            "isPartOf": "DOE-019-AEPID-Collection1",
             "keyword": [
                 "AMI",
                 "AMR",
@@ -24925,54 +24917,54 @@
                 "revenues",
                 "sales"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
+            "language": [
+                "us-EN"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2007-03-01",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "us-EN"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_861/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2001-01-01/2001-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual 1992 Electric Power Industry Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual 1990 Electric Power Industry Data",
-            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
-            "modified": "2007-03-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-3973434310",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2001-01-01/2001-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-AEPID-Collection1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
+            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/archive/zip/f86190.zip",
                     "mediaType": "application/zip",
-                    "title": "1990 EPI Data EIA-861",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/archive/zip/f86190.zip"
+                    "title": "1990 EPI Data EIA-861"
                 }
             ],
+            "identifier": "DOE-019-3973434310",
+            "isPartOf": "DOE-019-AEPID-Collection1",
             "keyword": [
                 "AMI",
                 "AMR",
@@ -25007,103 +24999,103 @@
                 "revenues",
                 "sales"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
+            "language": [
+                "us-EN"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2007-03-01",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "us-EN"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_861/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2001-01-01/2001-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual 1990 Electric Power Industry Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Crude Oil Imports Tracking Tool",
-            "description": "Maps and data for petroleum imports by type, crude oil grade, location, and country of origin.",
-            "modified": "2019-02-21",
             "accessLevel": "public",
-            "identifier": "DOE-019-2332233777",
-            "describedBy": "https://www.eia.gov/survey/form/eia_814/instructions.pdf",
-            "landingPage": "https://www.eia.gov/tools/",
-            "spatial": "PAD District",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:melinda.hobbs@eia.gov"
             },
+            "describedBy": "https://www.eia.gov/survey/form/eia_814/instructions.pdf",
+            "description": "Maps and data for petroleum imports by type, crude oil grade, location, and country of origin.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/petroleum/imports/browser/#/?vs=PET_IMPORTS.WORLD-US-ALL.A",
                     "mediaType": "text/html",
-                    "title": "Imports tool",
-                    "downloadURL": "https://www.eia.gov/petroleum/imports/browser/#/?vs=PET_IMPORTS.WORLD-US-ALL.A"
+                    "title": "Imports tool"
                 }
             ],
+            "identifier": "DOE-019-2332233777",
             "keyword": [
                 "crude oil",
                 "imports",
                 "petroleum imports"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "https://www.eia.gov/tools/",
+            "language": [
+                "us-EN"
             ],
+            "modified": "2019-02-21",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "us-EN"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "https://www.eia.gov/petroleum/imports/companylevel/"
             ],
+            "spatial": "PAD District",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Crude Oil Imports Tracking Tool"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual 1991 Electric Power Industry Data",
-            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
-            "modified": "2007-03-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-3973434311",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2001-01-01/2001-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-AEPID-Collection1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
+            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/archive/zip/f86191.zip",
                     "mediaType": "application/zip",
-                    "title": "1991 EPI Data EIA-861",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/archive/zip/f86191.zip"
+                    "title": "1991 EPI Data EIA-861"
                 }
             ],
+            "identifier": "DOE-019-3973434311",
+            "isPartOf": "DOE-019-AEPID-Collection1",
             "keyword": [
                 "AMI",
                 "AMR",
@@ -25138,53 +25130,53 @@
                 "revenues",
                 "sales"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
+            "language": [
+                "us-EN"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2007-03-01",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "us-EN"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_861/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2001-01-01/2001-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual 1991 Electric Power Industry Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Production by MSHA ID, Mine Operaton, Union Status, and Average Number of Employees and Hours 2017",
-            "description": "Data on U.S mining operation (i.e., operation name, mailing address, telephone number, State and county of operation, etc.), annual coal production, code definitions, and union status. Annual time series extend back to 1983. Based on EIA Form-7A data.",
-            "modified": "2018-11-02",
             "accessLevel": "public",
-            "identifier": "DOE-019-2332233232",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_7a/instructions.pdf",
-            "landingPage": "http://www.eia.gov/coal/data.cfm",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "State and County",
-            "temporal": "1991-01-01/1991-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-CPMSHAID-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_7a/instructions.pdf",
+            "description": "Data on U.S mining operation (i.e., operation name, mailing address, telephone number, State and county of operation, etc.), annual coal production, code definitions, and union status. Annual time series extend back to 1983. Based on EIA Form-7A data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/coal/data/public/xls/coalpublic2017.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "Coal Production 2017",
-                    "downloadURL": "https://www.eia.gov/coal/data/public/xls/coalpublic2017.xls"
+                    "title": "Coal Production 2017"
                 }
             ],
+            "identifier": "DOE-019-2332233232",
+            "isPartOf": "DOE-019-CPMSHAID-COLLECTION1",
             "keyword": [
                 "coal data",
                 "coal data file",
@@ -25195,152 +25187,152 @@
                 "coal production file",
                 "energy"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/data.cfm",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2018-11-02",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_7a/form.pdf"
             ],
+            "spatial": "State and County",
+            "temporal": "1991-01-01/1991-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Production by MSHA ID, Mine Operaton, Union Status, and Average Number of Employees and Hours 2017"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Tight Oil Production Estimates by Play",
-            "description": "Estimated monthly production derived from state administrative data. Data are back to January 2000.",
-            "modified": "2019-04-18",
             "accessLevel": "public",
-            "identifier": "DOE-019-4536758399",
-            "dataQuality": true,
-            "issued": "2018-01-02",
-            "landingPage": "https://www.eia.gov/petroleum/data.php#crude",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "State",
-            "temporal": "2003/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Estimated monthly production derived from state administrative data. Data are back to January 2000.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/energyexplained/data/U.S.%20tight%20oil%20production.xlsx",
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "title": "Tight oil",
-                    "downloadURL": "https://www.eia.gov/energyexplained/data/U.S.%20tight%20oil%20production.xlsx"
+                    "title": "Tight oil"
                 }
             ],
+            "identifier": "DOE-019-4536758399",
+            "issued": "2018-01-02",
             "keyword": [
                 "bakken",
                 "eagle ford",
                 "production",
                 "tight oil"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "https://www.eia.gov/petroleum/data.php#crude",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2019-04-18",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
+            "spatial": "State",
+            "temporal": "2003/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Tight Oil Production Estimates by Play"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Crude Oil and Petroleum Exports",
-            "description": "Monthly Crude Oil and Petroleum Products Exports . Data are back to January 1981 for petroleum products and back to January 1920 for crude oil.",
-            "modified": "2019-03-29",
             "accessLevel": "public",
-            "identifier": "DOE-019-4536758388",
-            "dataQuality": true,
-            "landingPage": "https://www.eia.gov/dnav/pet/pet_move_exp_dc_NUS-Z00_mbbl_m.htm",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1920/2019",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:melinda.hobbs@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Monthly Crude Oil and Petroleum Products Exports . Data are back to January 1981 for petroleum products and back to January 1920 for crude oil.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/dnav/pet/xls/PET_MOVE_EXP_DC_NUS-Z00_MBBL_M.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "oilexports",
-                    "downloadURL": "https://www.eia.gov/dnav/pet/xls/PET_MOVE_EXP_DC_NUS-Z00_MBBL_M.xls"
+                    "title": "oilexports"
                 }
             ],
+            "identifier": "DOE-019-4536758388",
             "keyword": [
                 "crude oil",
                 "crude oil exports",
                 "petroleum",
                 "petroleum exports"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "https://www.eia.gov/dnav/pet/pet_move_exp_dc_NUS-Z00_mbbl_m.htm",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2019-03-29",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
+            "spatial": "United States",
+            "temporal": "1920/2019",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Crude Oil and Petroleum Exports"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Dry Shale Gas Production Estimates by Play",
-            "description": "Estimated monthly production derived from state administrative data. Data are back to January 2000.",
-            "modified": "2019-04-18",
             "accessLevel": "public",
-            "identifier": "DOE-019-4536758398",
-            "dataQuality": true,
-            "issued": "2018-01-02",
-            "landingPage": "https://www.eia.gov/naturalgas/data.php",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "State",
-            "temporal": "2003/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Estimated monthly production derived from state administrative data. Data are back to January 2000.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/naturalgas/weekly/img/shale_gas_201902.xlsx",
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "title": "Shale Gas",
-                    "downloadURL": "https://www.eia.gov/naturalgas/weekly/img/shale_gas_201902.xlsx"
+                    "title": "Shale Gas"
                 }
             ],
+            "identifier": "DOE-019-4536758398",
+            "issued": "2018-01-02",
             "keyword": [
                 "Haynesville",
                 "Marcellus",
@@ -25352,42 +25344,41 @@
                 "production",
                 "shale gas"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "https://www.eia.gov/naturalgas/data.php",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2019-04-18",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
+            "spatial": "State",
+            "temporal": "2003/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Dry Shale Gas Production Estimates by Play"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "National Nuclear Security Administration Policies and Supplemental Directives",
-            "description": "NNSA uses NNSA Policies (NAPs) and Supplemental Directives (SDs) as its primary means to establish, communicate, and institutionalize policies, requirements, responsibilities, and procedures specific to NNSA elements and contractors. NAPs impart policy and requirements unique to the Administration or provide short-term notices until more formal direction can be provided. SDs are utilized, in conjunction with the Department's Directives System to indicate how NNSA will implement a Departmental directive in a cost efficient manner.",
-            "modified": "2015-11-30",
             "accessLevel": "public",
-            "identifier": "DOE-019-4721565656",
-            "dataQuality": true,
-            "describedBy": "http://www.nnsa.energy.gov/aboutus/ourprograms/administration/policysystem",
-            "landingPage": "http://nnsa.energy.gov/aboutus/ouroperations/managementandbudget/supplementaldirectives",
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "spatial": "United States",
-            "temporal": "2007-05-08/2011-03-17",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Nuclear Security Administration"
-            },
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "019:05"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Camille Torquato",
                 "hasEmail": "mailto:Camille.Torquato@nnsa.doe.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.nnsa.energy.gov/aboutus/ourprograms/administration/policysystem",
+            "description": "NNSA uses NNSA Policies (NAPs) and Supplemental Directives (SDs) as its primary means to establish, communicate, and institutionalize policies, requirements, responsibilities, and procedures specific to NNSA elements and contractors. NAPs impart policy and requirements unique to the Administration or provide short-term notices until more formal direction can be provided. SDs are utilized, in conjunction with the Department's Directives System to indicate how NNSA will implement a Departmental directive in a cost efficient manner.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -25395,6 +25386,7 @@
                     "title": "NNSA Directives"
                 }
             ],
+            "identifier": "DOE-019-4721565656",
             "keyword": [
                 "directives",
                 "law",
@@ -25405,107 +25397,107 @@
                 "supplemental directives",
                 "technical standards"
             ],
-            "bureauCode": [
-                "019:05"
+            "landingPage": "http://nnsa.energy.gov/aboutus/ouroperations/managementandbudget/supplementaldirectives",
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2015-11-30",
             "programCode": [
                 "019:047"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Nuclear Security Administration"
+            },
             "references": [
                 "http://www.nnsa.energy.gov/aboutus/ourprograms/administration/policysystem"
             ],
+            "spatial": "United States",
+            "temporal": "2007-05-08/2011-03-17",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "National Nuclear Security Administration Policies and Supplemental Directives"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "US DOE/NNSA Aerial Survey of Washington, DC",
-            "description": "The enclosed package represents radiation data collected with a helicopter over Washington, DC in 2013. The data were collected with an array of large thallium activated sodium iodide (NaI(Tl)) crystals and associated readout electronics to produce time and location referenced measurements.  These results represent raw data that have been calibrated  to physical units and validated. They do not include any further evaluation.",
-            "modified": "2014-10-30",
             "accessLevel": "public",
-            "identifier": "DOE-019-4589765578",
-            "dataQuality": true,
-            "describedBy": "http://nnsa.energy.gov/sites/default/files/nnsa/09-14-inlinefiles/2014-09-05%20DC%202013_GC%20Exposure_0.zip",
-            "landingPage": "http://www.nnsa.energy.gov/aboutus/ourprograms/emergencyoperationscounterterrorism/respondingtoemergencies-0-0/dcsurvey13",
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "spatial": "Washington DC",
-            "temporal": "2013-01-01/2013-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Nuclear Security Administration"
-            },
+            "bureauCode": [
+                "019:05"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Daniel Blumenthal",
                 "hasEmail": "mailto:Daniel.Blumenthal@nnsa.doe.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://nnsa.energy.gov/sites/default/files/nnsa/09-14-inlinefiles/2014-09-05%20DC%202013_GC%20Exposure_0.zip",
+            "description": "The enclosed package represents radiation data collected with a helicopter over Washington, DC in 2013. The data were collected with an array of large thallium activated sodium iodide (NaI(Tl)) crystals and associated readout electronics to produce time and location referenced measurements.  These results represent raw data that have been calibrated  to physical units and validated. They do not include any further evaluation.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "image/jpeg",
+                    "downloadURL": "https://nnsa.energy.gov/sites/default/files/nnsa/09-14-inlinefiles/2014-09-05%20DC%202013_GC%20Exposure_0.zip",
                     "format": "ZIP",
-                    "title": "NNSA Survey",
-                    "downloadURL": "https://nnsa.energy.gov/sites/default/files/nnsa/09-14-inlinefiles/2014-09-05%20DC%202013_GC%20Exposure_0.zip"
+                    "mediaType": "image/jpeg",
+                    "title": "NNSA Survey"
                 }
             ],
+            "identifier": "DOE-019-4589765578",
             "keyword": [
                 "environmental monitoring",
                 "nuclear",
                 "radiation",
                 "radiology"
             ],
-            "bureauCode": [
-                "019:05"
+            "landingPage": "http://www.nnsa.energy.gov/aboutus/ourprograms/emergencyoperationscounterterrorism/respondingtoemergencies-0-0/dcsurvey13",
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2014-10-30",
             "programCode": [
                 "019:047"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Nuclear Security Administration"
+            },
             "references": [
                 "http://nnsa.energy.gov/sites/default/files/nnsa/09-14-inlinefiles/2014-09-05%20DC%202013_GC%20Exposure_0.zip"
             ],
+            "spatial": "Washington DC",
+            "temporal": "2013-01-01/2013-12-31",
             "theme": [
                 "environment"
-            ]
+            ],
+            "title": "US DOE/NNSA Aerial Survey of Washington, DC"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "US DOE/NNSA and DoD Response to 2011 Fukushima Incident: Field Team Radiological Measurements",
-            "description": "Field Measurements describe activity and exposure rate. They have been collected by a variety of agencies from both fixed detector locations as well as by mobile field teams.   These results represent raw data that have been calibrated  to physical units and validated. They do not include any further evaluation.",
-            "modified": "2015-05-05",
             "accessLevel": "public",
-            "identifier": "DOE-019-5595665678",
-            "dataQuality": true,
-            "describedBy": "http://energy.gov/sites/prod/files/NNSADataRepositoryGuide_2.pdf",
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "rights": "null",
-            "spatial": "Fukushima-ken",
-            "temporal": "2011-03-12/2011-05-11",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Nuclear Security Administration"
-            },
+            "bureauCode": [
+                "019:05"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Daniel Blumenthal",
                 "hasEmail": "mailto:Daniel.Blumenthal@nnsa.doe.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://energy.gov/sites/prod/files/NNSADataRepositoryGuide_2.pdf",
+            "description": "Field Measurements describe activity and exposure rate. They have been collected by a variety of agencies from both fixed detector locations as well as by mobile field teams.   These results represent raw data that have been calibrated  to physical units and validated. They do not include any further evaluation.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "spreadsheet",
-                    "title": "Fukushima Measurements",
                     "describedBy": "http://energy.gov/sites/prod/files/NNSADataRepositoryGuide_2.pdf",
-                    "downloadURL": "https://energy.gov/sites/prod/files/FieldMeasurements_5.csv"
+                    "downloadURL": "https://energy.gov/sites/prod/files/FieldMeasurements_5.csv",
+                    "format": "spreadsheet",
+                    "mediaType": "text/csv",
+                    "title": "Fukushima Measurements"
                 }
             ],
+            "identifier": "DOE-019-5595665678",
             "keyword": [
                 "Fukushima",
                 "Japan",
@@ -25515,53 +25507,54 @@
                 "radiation",
                 "radiological"
             ],
-            "bureauCode": [
-                "019:05"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2015-05-05",
             "programCode": [
                 "019:047"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Nuclear Security Administration"
+            },
             "references": [
                 "http://energy.gov/sites/prod/files/NNSADataRepositoryGuide_2.pdf"
             ],
-            "theme": [
-                "environment"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "US DOE NNSA Response to 2011 Fukushima Incident: Iodine-131 Aerial Data Analysis",
-            "description": "The enclosed package represents radiation data collected with the fixed-wing aircraft (C-12) from 2-3 April 2011. The data were collected with an array of large thallium activated sodium iodide (NaI(Tl)) crystals and associated readout electronics to produce time and location referenced measurements.  These results represent raw data that have been analyzed to map the ground deposition of Iodine-131 released during the Fukushima Dai-ichi Nuclear Power Plant accident. They are calibrated to surface contamination units and validated. They do not include any further evaluation.",
-            "modified": "2014-05-03",
-            "accessLevel": "public",
-            "identifier": "DOE-019-5873466791",
-            "dataQuality": true,
-            "describedBy": "http://energy.gov/sites/prod/files/2014/05/f16/Iodine%20Deposition%20from%20Early%20Aerial%20Surveys.pdf",
-            "license": "https://creativecommons.org/licenses/by/4.0",
+            "rights": "null",
             "spatial": "Fukushima-ken",
-            "temporal": "2011/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Nuclear Security Administration"
+            "temporal": "2011-03-12/2011-05-11",
+            "theme": [
+                "environment"
+            ],
+            "title": "US DOE/NNSA and DoD Response to 2011 Fukushima Incident: Field Team Radiological Measurements"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "019:05"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Daniel Blumenthal",
                 "hasEmail": "mailto:Daniel.Blumenthal@nnsa.doe.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://energy.gov/sites/prod/files/2014/05/f16/Iodine%20Deposition%20from%20Early%20Aerial%20Surveys.pdf",
+            "description": "The enclosed package represents radiation data collected with the fixed-wing aircraft (C-12) from 2-3 April 2011. The data were collected with an array of large thallium activated sodium iodide (NaI(Tl)) crystals and associated readout electronics to produce time and location referenced measurements.  These results represent raw data that have been analyzed to map the ground deposition of Iodine-131 released during the Fukushima Dai-ichi Nuclear Power Plant accident. They are calibrated to surface contamination units and validated. They do not include any further evaluation.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kmz+xml",
-                    "format": "kmz",
-                    "title": "Fukushima Iodine-131 Aerial",
                     "describedBy": "http://energy.gov/sites/prod/files/2014/05/f16/Iodine%20Deposition%20from%20Early%20Aerial%20Surveys.pdf",
-                    "downloadURL": "https://energy.gov/sites/prod/files/2014/01/f6/Iodine%20Deposition%20from%20Early%20Aerial%20Surveys.kmz"
+                    "downloadURL": "https://energy.gov/sites/prod/files/2014/01/f6/Iodine%20Deposition%20from%20Early%20Aerial%20Surveys.kmz",
+                    "format": "kmz",
+                    "mediaType": "application/vnd.google-earth.kmz+xml",
+                    "title": "Fukushima Iodine-131 Aerial"
                 }
             ],
+            "identifier": "DOE-019-5873466791",
             "keyword": [
                 "Fukushima",
                 "Japan",
@@ -25571,53 +25564,53 @@
                 "radiation",
                 "radiological"
             ],
-            "bureauCode": [
-                "019:05"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2014-05-03",
             "programCode": [
                 "019:047"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Nuclear Security Administration"
+            },
             "references": [
                 "http://energy.gov/sites/prod/files/2014/05/f16/Iodine%20Deposition%20from%20Early%20Aerial%20Surveys.pdf"
             ],
+            "spatial": "Fukushima-ken",
+            "temporal": "2011/2013",
             "theme": [
                 "environment"
-            ]
+            ],
+            "title": "US DOE NNSA Response to 2011 Fukushima Incident: Iodine-131 Aerial Data Analysis"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "US DOE NNSA Response to 2011 Fukushima Incident: At-sea Aerial Data",
-            "description": "The enclosed package represents radiation data collected with the fixed-wing aircraft (C-12) off the east coast of Japan on three separate flights dated April 5, 2011, April 18, 2011, and May 9, 2011. The data were collected with an array of large thallium activated sodium iodide (NaI(T)) crystals and associated readout electronics to produce time and location referenced measurements.  These results represent raw data that have not been validated but not calibrated  to physical units. They do not include any further evaluation.",
-            "modified": "2014-05-02",
             "accessLevel": "public",
-            "identifier": "DOE-019-7845903211",
-            "dataQuality": true,
-            "describedBy": "http://energy.gov/sites/prod/files/2013/10/f3/AMS%20C12%20Sea%20Data%20Dictionary.pdf",
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "spatial": "Fukushima-ken",
-            "temporal": "2011-03-07/2011-03-19",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Nuclear Security Administration"
-            },
+            "bureauCode": [
+                "019:05"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Daniel Blumenthal",
                 "hasEmail": "mailto:Daniel.Blumenthal@nnsa.doe.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://energy.gov/sites/prod/files/2013/10/f3/AMS%20C12%20Sea%20Data%20Dictionary.pdf",
+            "description": "The enclosed package represents radiation data collected with the fixed-wing aircraft (C-12) off the east coast of Japan on three separate flights dated April 5, 2011, April 18, 2011, and May 9, 2011. The data were collected with an array of large thallium activated sodium iodide (NaI(T)) crystals and associated readout electronics to produce time and location referenced measurements.  These results represent raw data that have not been validated but not calibrated  to physical units. They do not include any further evaluation.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kmz+xml",
-                    "format": "kmz",
-                    "title": "Fukushima At-sea Aerial",
                     "describedBy": "http://energy.gov/sites/prod/files/2013/10/f3/AMS%20C12%20Sea%20Data%20Dictionary.pdf",
-                    "downloadURL": "https://energy.gov/sites/prod/files/2013/10/f3/AMS%20C12%20Sea%20Data.kmz"
+                    "downloadURL": "https://energy.gov/sites/prod/files/2013/10/f3/AMS%20C12%20Sea%20Data.kmz",
+                    "format": "kmz",
+                    "mediaType": "application/vnd.google-earth.kmz+xml",
+                    "title": "Fukushima At-sea Aerial"
                 }
             ],
+            "identifier": "DOE-019-7845903211",
             "keyword": [
                 "Fukushima",
                 "Japa",
@@ -25627,53 +25620,53 @@
                 "radiation",
                 "radiological"
             ],
-            "bureauCode": [
-                "019:05"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2014-05-02",
             "programCode": [
                 "019:047"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Nuclear Security Administration"
+            },
             "references": [
                 "http://energy.gov/sites/prod/files/2013/10/f3/AMS%20C12%20Sea%20Data%20Dictionary.pdf"
             ],
+            "spatial": "Fukushima-ken",
+            "temporal": "2011-03-07/2011-03-19",
             "theme": [
                 "environment"
-            ]
+            ],
+            "title": "US DOE NNSA Response to 2011 Fukushima Incident: At-sea Aerial Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "US DOE/NNSA Response to 2011 Fukushima Incident: Raw Aerial Data and Extracted Ground Exposure Rates and Cesium Deposition",
-            "description": "The enclosed package represents radiation data collected with the fixed-wing aircraft (C-12) from 2 April 2011 to 9 May 2011. The data were collected with an array of large thallium activated sodium iodide (NaI(T)) crystals and associated readout electronics to produce time and location referenced measurements.  These results represent raw data that have been calibrated  to physical units and validated. They do not include any further evaluation.",
-            "modified": "2013-04-11",
             "accessLevel": "public",
-            "identifier": "DOE-019-5273347659",
-            "dataQuality": true,
-            "describedBy": "http://energy.gov/sites/prod/files/HELP%2520-%2520DOE%2520AMS%2520C12_1.pdf",
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "spatial": "Fukushima-ken",
-            "temporal": "2011-04-02/2011-05-09",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Nuclear Security Administration"
-            },
+            "bureauCode": [
+                "019:05"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Daniel Blumenthal",
                 "hasEmail": "mailto:Daniel.Blumenthal@nnsa.doe.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://energy.gov/sites/prod/files/HELP%2520-%2520DOE%2520AMS%2520C12_1.pdf",
+            "description": "The enclosed package represents radiation data collected with the fixed-wing aircraft (C-12) from 2 April 2011 to 9 May 2011. The data were collected with an array of large thallium activated sodium iodide (NaI(T)) crystals and associated readout electronics to produce time and location referenced measurements.  These results represent raw data that have been calibrated  to physical units and validated. They do not include any further evaluation.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kmz+xml",
-                    "format": "kmz",
-                    "title": "Fukushima Aerial and Ground",
                     "describedBy": "http://energy.gov/sites/prod/files/NNSADataRepositoryGuide_2.pdf",
-                    "downloadURL": "https://energy.gov/sites/prod/files/DOE_AMS_C12_Cs134_Bq_20110630.kmz"
+                    "downloadURL": "https://energy.gov/sites/prod/files/DOE_AMS_C12_Cs134_Bq_20110630.kmz",
+                    "format": "kmz",
+                    "mediaType": "application/vnd.google-earth.kmz+xml",
+                    "title": "Fukushima Aerial and Ground"
                 }
             ],
+            "identifier": "DOE-019-5273347659",
             "keyword": [
                 "Fukushima",
                 "Japan",
@@ -25683,54 +25676,53 @@
                 "radiation",
                 "radiological"
             ],
-            "bureauCode": [
-                "019:05"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2013-04-11",
             "programCode": [
                 "019:047"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Nuclear Security Administration"
+            },
             "references": [
                 "http://energy.gov/sites/prod/files/HELP%2520-%2520DOE%2520AMS%2520C12_1.pdf"
             ],
+            "spatial": "Fukushima-ken",
+            "temporal": "2011-04-02/2011-05-09",
             "theme": [
                 "environment"
-            ]
+            ],
+            "title": "US DOE/NNSA Response to 2011 Fukushima Incident: Raw Aerial Data and Extracted Ground Exposure Rates and Cesium Deposition"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "US DOE/NNSA Response to 2011 Fukushima Incident: March 2011 Aerial Data",
-            "description": "The enclosed package represents radiation data collected with the fixed-wing aircraft (C-12) from 17 March 2011 to 19 March 2011. The data were collected with an array of large thallium activated sodium iodide (NaI(T)) crystals and associated readout electronics to produce time and location referenced measurements.  These results represent raw data that have been calibrated  to physical units and validated. They do not include any further evaluation.",
-            "modified": "2013-04-11",
             "accessLevel": "public",
-            "identifier": "DOE-019-1176156932",
-            "dataQuality": true,
-            "describedBy": "http://energy.gov/sites/prod/files/NNSADataRepositoryGuide_0.pdf",
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "rights": "null",
-            "spatial": "Fukushima-ken",
-            "temporal": "2011-03-07/2011-03-19",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Nuclear Security Administration"
-            },
+            "bureauCode": [
+                "019:05"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Daniel Blumenthal",
                 "hasEmail": "mailto:Daniel.Blumenthal@nnsa.doe.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://energy.gov/sites/prod/files/NNSADataRepositoryGuide_0.pdf",
+            "description": "The enclosed package represents radiation data collected with the fixed-wing aircraft (C-12) from 17 March 2011 to 19 March 2011. The data were collected with an array of large thallium activated sodium iodide (NaI(T)) crystals and associated readout electronics to produce time and location referenced measurements.  These results represent raw data that have been calibrated  to physical units and validated. They do not include any further evaluation.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kmz+xml",
-                    "format": "spreadsheet",
-                    "title": "Fukushima Aerial",
                     "describedBy": "http://energy.gov/sites/prod/files/NNSADataRepositoryGuide_2.pdf",
-                    "downloadURL": "https://energy.gov/sites/prod/files/CumulativeAMS21Mar2011.kmz"
+                    "downloadURL": "https://energy.gov/sites/prod/files/CumulativeAMS21Mar2011.kmz",
+                    "format": "spreadsheet",
+                    "mediaType": "application/vnd.google-earth.kmz+xml",
+                    "title": "Fukushima Aerial"
                 }
             ],
+            "identifier": "DOE-019-1176156932",
             "keyword": [
                 "Fukushima",
                 "Japan",
@@ -25740,46 +25732,44 @@
                 "radiation",
                 "radiological"
             ],
-            "bureauCode": [
-                "019:05"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2013-04-11",
             "programCode": [
                 "019:047"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Nuclear Security Administration"
+            },
             "references": [
                 "http://energy.gov/sites/prod/files/NNSADataRepositoryGuide_0.pdf"
             ],
+            "rights": "null",
+            "spatial": "Fukushima-ken",
+            "temporal": "2011-03-07/2011-03-19",
             "theme": [
                 "environment"
-            ]
+            ],
+            "title": "US DOE/NNSA Response to 2011 Fukushima Incident: March 2011 Aerial Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "US DOE/NNSA Response Data Repository",
-            "description": "This portal contains environmental radiological monitoring data collected in response to the nuclear emergency following the March 11th, 2011 Tohoku earthquake and tsunami. Available data sets include field measurements, field samples, and analysis results. It is designed to contain data sets from other large-scale response efforts should they occur.",
-            "modified": "2015-02-28",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-4578654567",
-            "dataQuality": true,
-            "describedBy": "https://www.nnsaresponsedata.net/",
-            "landingPage": "http://nnsaresponsedata.net/",
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "rights": "Need to request access",
-            "spatial": "DOE",
-            "temporal": "2011/2015",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Nuclear Security Administration"
-            },
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "019:05"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Daniel Blumenthal",
                 "hasEmail": "mailto:Daniel.Blumenthal@nnsa.doe.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.nnsaresponsedata.net/",
+            "description": "This portal contains environmental radiological monitoring data collected in response to the nuclear emergency following the March 11th, 2011 Tohoku earthquake and tsunami. Available data sets include field measurements, field samples, and analysis results. It is designed to contain data sets from other large-scale response efforts should they occur.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -25787,58 +25777,61 @@
                     "title": "NNSA Response"
                 }
             ],
+            "identifier": "DOE-019-4578654567",
             "keyword": [
                 "environmental monitoring",
                 "nuclear",
                 "radiation"
             ],
-            "bureauCode": [
-                "019:05"
+            "landingPage": "http://nnsaresponsedata.net/",
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2015-02-28",
             "programCode": [
                 "019:047"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Nuclear Security Administration"
+            },
             "references": [
                 "https://www.nnsaresponsedata.net/Users/NNSADataRepositoryGuide.pdf"
             ],
+            "rights": "Need to request access",
+            "spatial": "DOE",
+            "temporal": "2011/2015",
             "theme": [
                 "environment"
-            ]
+            ],
+            "title": "US DOE/NNSA Response Data Repository"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "US DOE/NNSA Response to 2011 Fukushima Incident: Instrument Samples (InSitu Measurements",
-            "description": "Field Samples are physical media collected during the response which are subsequently analyzed either in a laboratory or in the field using InSitu equipment. Common field samples include air filters and soil samples. Radiochemistry analysis typically reports the presence of specific radionuclides measured as total activity or as either activity/unit of mass or activity/unit of volume, depending upon the sample media. In addition, total beta and total alpha activity may be reported. Currently, air filter and soil sample analysis results may be downloaded through the data repository. Both data sets are similar; they contain a number of columns describing the collected sample as well as the results of radiochemical analysis. In addition, there are a number of special fields that are specific to a given sample type; e.g. Air Filters specify the filter type and total volume, while soil samples specify the sample weight. For convenience, the sample information and subsequent analysis has been flattened into a simple tabular format. Consequently, if a sample has multiple analysis results the sample collection values will be repeated through the set; e.g. sample ID#, barcode, latitude/longitude, collection date etc. To be included in the data repository, a given sample must meet the following criteria: has a valid latitude, longitude, and collection date; has been sent to a laboratory for analysis, or had analysis performed in the field; has at least one valid analysis result with a reportable unit, nuclide, and activity which has been validated by an authorized laboratory staff member.  These results represent raw data that have been calibrated  to physical units and validated. They do not include any further evaluation.",
-            "modified": "2013-04-11",
             "accessLevel": "public",
-            "identifier": "DOE-019-9181673421",
-            "dataQuality": true,
-            "describedBy": "http://energy.gov/sites/prod/files/NNSADataRepositoryGuide_2.pdf",
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "spatial": "Fukushima-ken",
-            "temporal": "2011-03-17/2011-07-02",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Nuclear Security Administration"
-            },
+            "bureauCode": [
+                "019:05"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Daniel Blumenthal",
                 "hasEmail": "mailto:Daniel.Blumenthal@nnsa.doe.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://energy.gov/sites/prod/files/NNSADataRepositoryGuide_2.pdf",
+            "description": "Field Samples are physical media collected during the response which are subsequently analyzed either in a laboratory or in the field using InSitu equipment. Common field samples include air filters and soil samples. Radiochemistry analysis typically reports the presence of specific radionuclides measured as total activity or as either activity/unit of mass or activity/unit of volume, depending upon the sample media. In addition, total beta and total alpha activity may be reported. Currently, air filter and soil sample analysis results may be downloaded through the data repository. Both data sets are similar; they contain a number of columns describing the collected sample as well as the results of radiochemical analysis. In addition, there are a number of special fields that are specific to a given sample type; e.g. Air Filters specify the filter type and total volume, while soil samples specify the sample weight. For convenience, the sample information and subsequent analysis has been flattened into a simple tabular format. Consequently, if a sample has multiple analysis results the sample collection values will be repeated through the set; e.g. sample ID#, barcode, latitude/longitude, collection date etc. To be included in the data repository, a given sample must meet the following criteria: has a valid latitude, longitude, and collection date; has been sent to a laboratory for analysis, or had analysis performed in the field; has at least one valid analysis result with a reportable unit, nuclide, and activity which has been validated by an authorized laboratory staff member.  These results represent raw data that have been calibrated  to physical units and validated. They do not include any further evaluation.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "spreadsheet",
-                    "title": "Fukushima Instrument Samples",
                     "describedBy": "http://energy.gov/sites/prod/files/NNSADataRepositoryGuide_2.pdf",
-                    "downloadURL": "https://energy.gov/sites/prod/files/FieldSampleInstrumentResults.csv"
+                    "downloadURL": "https://energy.gov/sites/prod/files/FieldSampleInstrumentResults.csv",
+                    "format": "spreadsheet",
+                    "mediaType": "text/csv",
+                    "title": "Fukushima Instrument Samples"
                 }
             ],
+            "identifier": "DOE-019-9181673421",
             "keyword": [
                 "Fukushima",
                 "Japan",
@@ -25848,53 +25841,53 @@
                 "radiation",
                 "radiological"
             ],
-            "bureauCode": [
-                "019:05"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2013-04-11",
             "programCode": [
                 "019:047"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Nuclear Security Administration"
+            },
             "references": [
                 "http://energy.gov/sites/prod/files/NNSADataRepositoryGuide_2.pdf"
             ],
+            "spatial": "Fukushima-ken",
+            "temporal": "2011-03-17/2011-07-02",
             "theme": [
                 "environment"
-            ]
+            ],
+            "title": "US DOE/NNSA Response to 2011 Fukushima Incident: Instrument Samples (InSitu Measurements"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "US DOE/NNSA and DoD Response to 2011 Fukushima Incident: Radiological Soil Samples",
-            "description": "Field Samples are physical media collected during the response which are subsequently analyzed either in a laboratory or in the field using InSitu equipment. Common field samples include air filters and soil samples. Radiochemistry analysis typically reports the presence of specific radionuclides measured as total activity or as either activity/unit of mass or activity/unit of volume, depending upon the sample media. In addition, total beta and total alpha activity may be reported. Currently, air filter and soil sample analysis results may be downloaded through the data repository. Both data sets are similar; they contain a number of columns describing the collected sample as well as the results of radiochemical analysis. In addition, there are a number of special fields that are specific to a given sample type; e.g., Air Filters specify the filter type and total volume, while soil samples specify the sample weight. For convenience, the sample information and subsequent analysis has been \"flattened\" into a simple tabular format. Consequently, if a sample has multiple analysis results the \"sample collection\" values will be repeated through the set; e.g. sample ID#, barcode, latitude/longitude, collection date etc. To be included in the data repository, a given sample must meet the following criteria: has a valid latitude, longitude, and collection date; has been sent to a laboratory for analysis, or had analysis performed in the field; has at least one valid analysis result with a reportable unit, nuclide, and activity which has been validated by an authorized laboratory staff member.  These results represent raw data that have been calibrated  to physical units and validated. They do not include any further evaluation.",
-            "modified": "2015-05-05",
             "accessLevel": "public",
-            "identifier": "DOE-019-5599457867",
-            "dataQuality": true,
-            "describedBy": "http://energy.gov/sites/prod/files/NNSADataRepositoryGuide_2.pdf",
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "spatial": "Fukushima-ken",
-            "temporal": "2011-03-15/2011-04-24",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Nuclear Security Administration"
-            },
+            "bureauCode": [
+                "019:05"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Daniel Blumenthal",
                 "hasEmail": "mailto:Daniel.Blumenthal@nnsa.doe.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://energy.gov/sites/prod/files/NNSADataRepositoryGuide_2.pdf",
+            "description": "Field Samples are physical media collected during the response which are subsequently analyzed either in a laboratory or in the field using InSitu equipment. Common field samples include air filters and soil samples. Radiochemistry analysis typically reports the presence of specific radionuclides measured as total activity or as either activity/unit of mass or activity/unit of volume, depending upon the sample media. In addition, total beta and total alpha activity may be reported. Currently, air filter and soil sample analysis results may be downloaded through the data repository. Both data sets are similar; they contain a number of columns describing the collected sample as well as the results of radiochemical analysis. In addition, there are a number of special fields that are specific to a given sample type; e.g., Air Filters specify the filter type and total volume, while soil samples specify the sample weight. For convenience, the sample information and subsequent analysis has been \"flattened\" into a simple tabular format. Consequently, if a sample has multiple analysis results the \"sample collection\" values will be repeated through the set; e.g. sample ID#, barcode, latitude/longitude, collection date etc. To be included in the data repository, a given sample must meet the following criteria: has a valid latitude, longitude, and collection date; has been sent to a laboratory for analysis, or had analysis performed in the field; has at least one valid analysis result with a reportable unit, nuclide, and activity which has been validated by an authorized laboratory staff member.  These results represent raw data that have been calibrated  to physical units and validated. They do not include any further evaluation.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "spreadsheet",
-                    "title": "Fukushima Soil Samples",
                     "describedBy": "http://energy.gov/sites/prod/files/NNSADataRepositoryGuide_2.pdf",
-                    "downloadURL": "https://energy.gov/sites/prod/files/FieldSampleSoilResults_2.csv"
+                    "downloadURL": "https://energy.gov/sites/prod/files/FieldSampleSoilResults_2.csv",
+                    "format": "spreadsheet",
+                    "mediaType": "text/csv",
+                    "title": "Fukushima Soil Samples"
                 }
             ],
+            "identifier": "DOE-019-5599457867",
             "keyword": [
                 "Fukushima",
                 "Japan",
@@ -25904,53 +25897,53 @@
                 "radiation",
                 "radiological"
             ],
-            "bureauCode": [
-                "019:05"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2015-05-05",
             "programCode": [
                 "019:047"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Nuclear Security Administration"
+            },
             "references": [
                 "http://energy.gov/sites/prod/files/NNSADataRepositoryGuide_2.pdf"
             ],
+            "spatial": "Fukushima-ken",
+            "temporal": "2011-03-15/2011-04-24",
             "theme": [
                 "environment"
-            ]
+            ],
+            "title": "US DOE/NNSA and DoD Response to 2011 Fukushima Incident: Radiological Soil Samples"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "US DOE/NNSA and DoD Response to 2011 Fukushima Incident: Radiological Air Samples",
-            "description": "Field Samples are physical media collected during the response which are subsequently analyzed either in a laboratory or in the field using InSitu equipment. Common field samples include air filters and soil samples. Radiochemistry analysis typically reports the presence of specific radionuclides measured as total activity or as either activity/unit of mass or activity/unit of volume, depending upon the sample media. In addition, total beta and total alpha activity may be reported. Currently, air filter and soil sample analysis results may be downloaded through the data repository. Both data sets are similar; they contain a number of columns describing the collected sample as well as the results of radiochemical analysis. In addition, there are a number of special fields that are specific to a given sample type; e.g. Air Filters specify the filter type and total volume, while soil samples specify the sample weight. For convenience, the sample information and subsequent analysis has been \"flattened\" into a simple tabular format. Consequently, if a sample has multiple analysis results the \"sample collection\" values will be repeated through the set; e.g., sample ID#, barcode, latitude/longitude, collection date etc. To be included in the data repository, a given sample must meet the following criteria: has a valid latitude, longitude, and collection date; has been sent to a laboratory for analysis, or had analysis performed in the field; has at least one valid analysis result with a reportable unit, nuclide, and activity which has been validated by an authorized laboratory staff member. These results represent raw data that have been calibrated  to physical units and validated. They do not include any further evaluation.",
-            "modified": "2013-04-11",
             "accessLevel": "public",
-            "identifier": "DOE-019-5596758933",
-            "dataQuality": true,
-            "describedBy": "http://energy.gov/sites/prod/files/NNSADataRepositoryGuide_2.pdf",
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "spatial": "Fukushima-ken",
-            "temporal": "2011-03-11/2011-05-13",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Nuclear Security Administration"
-            },
+            "bureauCode": [
+                "019:05"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Daniel Blumenthal",
                 "hasEmail": "mailto:Daniel.Blumenthal@nnsa.doe.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://energy.gov/sites/prod/files/NNSADataRepositoryGuide_2.pdf",
+            "description": "Field Samples are physical media collected during the response which are subsequently analyzed either in a laboratory or in the field using InSitu equipment. Common field samples include air filters and soil samples. Radiochemistry analysis typically reports the presence of specific radionuclides measured as total activity or as either activity/unit of mass or activity/unit of volume, depending upon the sample media. In addition, total beta and total alpha activity may be reported. Currently, air filter and soil sample analysis results may be downloaded through the data repository. Both data sets are similar; they contain a number of columns describing the collected sample as well as the results of radiochemical analysis. In addition, there are a number of special fields that are specific to a given sample type; e.g. Air Filters specify the filter type and total volume, while soil samples specify the sample weight. For convenience, the sample information and subsequent analysis has been \"flattened\" into a simple tabular format. Consequently, if a sample has multiple analysis results the \"sample collection\" values will be repeated through the set; e.g., sample ID#, barcode, latitude/longitude, collection date etc. To be included in the data repository, a given sample must meet the following criteria: has a valid latitude, longitude, and collection date; has been sent to a laboratory for analysis, or had analysis performed in the field; has at least one valid analysis result with a reportable unit, nuclide, and activity which has been validated by an authorized laboratory staff member. These results represent raw data that have been calibrated  to physical units and validated. They do not include any further evaluation.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "format": "spreadsheet",
-                    "title": "Fukushima Air Samples",
                     "describedBy": "http://energy.gov/sites/prod/files/NNSADataRepositoryGuide_2.pdf",
-                    "downloadURL": "https://energy.gov/sites/prod/files/FieldSampleAirResults_2.csv"
+                    "downloadURL": "https://energy.gov/sites/prod/files/FieldSampleAirResults_2.csv",
+                    "format": "spreadsheet",
+                    "mediaType": "text/csv",
+                    "title": "Fukushima Air Samples"
                 }
             ],
+            "identifier": "DOE-019-5596758933",
             "keyword": [
                 "Fukushima",
                 "Japan",
@@ -25960,51 +25953,51 @@
                 "radiation",
                 "radiological"
             ],
-            "bureauCode": [
-                "019:05"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2013-04-11",
             "programCode": [
                 "019:047"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Nuclear Security Administration"
+            },
             "references": [
                 "http://energy.gov/sites/prod/files/NNSADataRepositoryGuide_2.pdf"
             ],
+            "spatial": "Fukushima-ken",
+            "temporal": "2011-03-11/2011-05-13",
             "theme": [
                 "environment"
-            ]
+            ],
+            "title": "US DOE/NNSA and DoD Response to 2011 Fukushima Incident: Radiological Air Samples"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Sandia Environmental Management System",
-            "description": "Environmental Management System (EMS) to identify and mitigate risks and incorporate environmental management into daily work activities. EMS is a continuing cycle of planning, implementing, evaluating, and improving processes to achieve environmental goals",
-            "modified": "2014",
             "accessLevel": "public",
-            "identifier": "DOE-019-7985478599",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "spatial": "United States",
-            "temporal": "2005/2012",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Nuclear Security Administration/SNL"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "019:05"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Katrina Wagner",
                 "hasEmail": "mailto:kmwagne@sandia.gov"
             },
+            "dataQuality": true,
+            "description": "Environmental Management System (EMS) to identify and mitigate risks and incorporate environmental management into daily work activities. EMS is a continuing cycle of planning, implementing, evaluating, and improving processes to achieve environmental goals",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.sandia.gov/about/environment/environmental_management_system/sandia_new_mexico_environmental_management/index.html",
                     "mediaType": "application/pdf",
-                    "title": "Sandia EMS",
-                    "downloadURL": "https://www.sandia.gov/about/environment/environmental_management_system/sandia_new_mexico_environmental_management/index.html"
+                    "title": "Sandia EMS"
                 }
             ],
+            "identifier": "DOE-019-7985478599",
             "keyword": [
                 "EMS",
                 "EPA",
@@ -26012,96 +26005,93 @@
                 "Environmental",
                 "Safety and Health Policy"
             ],
-            "bureauCode": [
-                "019:05"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2014",
             "programCode": [
                 "019:051"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Nuclear Security Administration/SNL"
+            },
             "references": [
                 "http://www.sandia.gov/about/environment/environmental_management_system/sandia_new_mexico_environmental_management/index.html"
             ],
+            "spatial": "United States",
+            "temporal": "2005/2012",
             "theme": [
                 "environment"
-            ]
+            ],
+            "title": "Sandia Environmental Management System"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Locus",
-            "description": "ENV-EDA arranges for various samples of soil and water to be collected and sent to a number of analytical laboratories. These labs store the results in internal databases and then send delimited data files with results back to LANL.",
-            "modified": "2015-05-05",
             "accessLevel": "public",
-            "identifier": "DOE-019-1347856551",
-            "dataQuality": true,
-            "issued": "2013-03-14",
-            "landingPage": "http://www.intellusnm.com/",
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "rights": "The record data is paper-based and is properly stored in Federal archives in Denver, Colorado.null",
-            "spatial": "DOE",
-            "temporal": "2013/2015",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Nuclear Security Administration/LANL"
-            },
+            "bureauCode": [
+                "019:05"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Enrique Torres",
                 "hasEmail": "mailto:etorres@lanl.gov"
             },
+            "dataQuality": true,
+            "description": "ENV-EDA arranges for various samples of soil and water to be collected and sent to a number of analytical laboratories. These labs store the results in internal databases and then send delimited data files with results back to LANL.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.intellusnm.com/",
                     "mediaType": "text/html",
-                    "title": "Locus",
-                    "downloadURL": "https://www.intellusnm.com/"
+                    "title": "Locus"
                 }
             ],
+            "identifier": "DOE-019-1347856551",
+            "issued": "2013-03-14",
             "keyword": [
                 "Environmental Data and Analysis"
             ],
-            "bureauCode": [
-                "019:05"
+            "landingPage": "http://www.intellusnm.com/",
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2015-05-05",
             "programCode": [
                 "019:051"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Nuclear Security Administration/LANL"
+            },
             "references": [
                 "http://www.intellusnm.com/"
             ],
+            "rights": "The record data is paper-based and is properly stored in Federal archives in Denver, Colorado.null",
+            "spatial": "DOE",
+            "temporal": "2013/2015",
             "theme": [
                 "environment"
-            ]
+            ],
+            "title": "Locus"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "DOE NEPA Documents",
-            "description": "DOE NEPA Documents are available to members of the public, including categorical exclusion determinations, environmental assessments, environmental impact statements, findings of no significant impact, records of decision, mitigation action plans, notices of availability, notices of intent, supplement analyses, and other notices and documents.",
-            "modified": "2010-12-17",
             "accessLevel": "public",
-            "identifier": "DOE-019-4379345678",
-            "dataQuality": true,
-            "describedBy": "http://energy.gov/nepa/",
-            "issued": "2010-01-01",
-            "landingPage": "http://energy.gov/nepa/",
-            "license": "http://opendatacommons.org/licenses/pddl/",
-            "spatial": "United States",
-            "temporal": "1969/2014",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE"
-            },
             "accrualPeriodicity": "R/P1W",
+            "bureauCode": [
+                "019:60"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Eric Cohen",
                 "hasEmail": "mailto:eric.cohen@hq.doe.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://energy.gov/nepa/",
+            "description": "DOE NEPA Documents are available to members of the public, including categorical exclusion determinations, environmental assessments, environmental impact statements, findings of no significant impact, records of decision, mitigation action plans, notices of availability, notices of intent, supplement analyses, and other notices and documents.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -26110,6 +26100,8 @@
                     "title": "NEPA Documents"
                 }
             ],
+            "identifier": "DOE-019-4379345678",
+            "issued": "2010-01-01",
             "keyword": [
                 "ARRA",
                 "block",
@@ -26126,53 +26118,53 @@
                 "retrofit",
                 "transportation"
             ],
-            "bureauCode": [
-                "019:60"
+            "landingPage": "http://energy.gov/nepa/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://opendatacommons.org/licenses/pddl/",
+            "modified": "2010-12-17",
             "programCode": [
                 "019:053"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE"
+            },
             "references": [
                 "http://energy.gov/nepa/",
                 "http://energy.gov/nepa/nepa-documents"
             ],
+            "spatial": "United States",
+            "temporal": "1969/2014",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "DOE NEPA Documents"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "NEPANODE",
-            "description": "This site is part of pilot effort at the US Department of Energy (DOE) - Office of NEPA Policy and Compliance to evaluate providing IT web services as a shared service, hosted on the cloud, and using only Free and Open Source Software (FOSS). The site is a collaborative data and document sharing platform, data is made publically available both as a downloadable file in multiple Open Standard formats or as a web service using Open Geospatial Construtium (OGC) Open Standard services (WMS/WFS/WCS).",
-            "modified": "2014-05-30",
             "accessLevel": "public",
-            "identifier": "DOE-019-1457634891",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "rights": "This site is made available to federal staff and contractors working to implement the National Environmental Policy Act of 1969 (NEPA) and other related environmental reviews and permitting processes.",
-            "spatial": "United States",
-            "temporal": "2009-11-02/2010-02-12",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE General Counsel"
-            },
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "019:60"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Jediny",
                 "hasEmail": "mailto:John.Jediny@hq.doe.gov"
             },
+            "dataQuality": true,
+            "description": "This site is part of pilot effort at the US Department of Energy (DOE) - Office of NEPA Policy and Compliance to evaluate providing IT web services as a shared service, hosted on the cloud, and using only Free and Open Source Software (FOSS). The site is a collaborative data and document sharing platform, data is made publically available both as a downloadable file in multiple Open Standard formats or as a web service using Open Geospatial Construtium (OGC) Open Standard services (WMS/WFS/WCS).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://github.com/DOE-NEPA/nepanode_backup/",
-                    "title": "NEPANODE",
-                    "description": "This is an archive of the original site."
+                    "description": "This is an archive of the original site.",
+                    "title": "NEPANODE"
                 }
             ],
+            "identifier": "DOE-019-1457634891",
             "keyword": [
                 "GHG emissions",
                 "air quality",
@@ -26206,51 +26198,51 @@
                 "waste management and contamination",
                 "water resources"
             ],
-            "bureauCode": [
-                "019:60"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2014-05-30",
             "programCode": [
                 "019:053"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE General Counsel"
+            },
+            "rights": "This site is made available to federal staff and contractors working to implement the National Environmental Policy Act of 1969 (NEPA) and other related environmental reviews and permitting processes.",
+            "spatial": "United States",
+            "temporal": "2009-11-02/2010-02-12",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "NEPANODE"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "GC Guidance/Opinions",
-            "description": "This website contains general legal advice. It is not intended, nor should it be considered, a substitute for obtaining legal advice about the specific factual situation that you are dealing with. Often a small change in the facts and circumstance will compel a different legal conclusion. When in doubt, or where more specific legal advice is needed, please contact the appropriate office in the Office of the General Counsel.",
-            "modified": "2011-01-10",
             "accessLevel": "public",
-            "identifier": "DOE-019-4377452378",
-            "dataQuality": true,
-            "describedBy": "http://gc.energy.gov/guidance_opinions.htm",
-            "issued": "2010-03-30",
-            "landingPage": "http://energy.gov/gc/gc-guidanceopinions",
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "spatial": "United States",
-            "temporal": "1978/2011",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE General Counsel"
-            },
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "019:60"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jaclyn Clenney",
                 "hasEmail": "mailto:jaclyn.clenney@hq.doe.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://gc.energy.gov/guidance_opinions.htm",
+            "description": "This website contains general legal advice. It is not intended, nor should it be considered, a substitute for obtaining legal advice about the specific factual situation that you are dealing with. Often a small change in the facts and circumstance will compel a different legal conclusion. When in doubt, or where more specific legal advice is needed, please contact the appropriate office in the Office of the General Counsel.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://energy.gov/gc/guidance-opinions-0",
                     "mediaType": "text/html",
-                    "title": "GC Opinions",
-                    "downloadURL": "https://energy.gov/gc/guidance-opinions-0"
+                    "title": "GC Opinions"
                 }
             ],
+            "identifier": "DOE-019-4377452378",
+            "issued": "2010-03-30",
             "keyword": [
                 "conference",
                 "conflict of interest",
@@ -26269,15 +26261,19 @@
                 "recusal",
                 "standards of conduct"
             ],
-            "bureauCode": [
-                "019:60"
+            "landingPage": "http://energy.gov/gc/gc-guidanceopinions",
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2011-01-10",
             "programCode": [
                 "019:053"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE General Counsel"
+            },
             "references": [
                 "http://gc.energy.gov/documents/ContractorEmploymentRecordGuidance.pdf",
                 "http://gc.energy.gov/documents/Arbitration_Guidance_for_MO_Contractors.pdf",
@@ -26295,32 +26291,27 @@
                 "http://gc.energy.gov/rulemaking_policies.htm",
                 "http://gc.energy.gov/documents/GC_GUIDANCE_ON_CONFERENCES_7_2010.pdf"
             ],
-            "theme": [
-                "law enforcement"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "NEPAnode MapWarper",
-            "description": "This site is part of pilot effort at the US Department of Energy (DOE) - Office of NEPA Policy and Compliance to evaluate providing IT web services as a shared service, hosted on the cloud, and using only Free and Open Source Software (FOSS). The site is an integrated component of the larger NEPAnode project but is a stand alone service. The site allows users to upload static map images with no geographic data so that they can be accurately referenced/rectified on an webmap. This site allows for the revitalizing of otherwise unusable/archived maps such as historic maps, site surveys, site plans, etc. turning them into usable geographic data which is subsequently made available as a KML file for use in Google Earth/Maps and as a Web Mapping Service (WMS) for using in web-based webmapping application such as NEPAnode or in desktop GIS software.",
-            "modified": "2014-08-29",
-            "accessLevel": "public",
-            "identifier": "DOE-019-1457678395",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "rights": "This site is made publically available, but individual users can choose to post maps as public or private resources.",
             "spatial": "United States",
-            "temporal": "2014-07-01/2014-12-30",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE General Counsel"
+            "temporal": "1978/2011",
+            "theme": [
+                "law enforcement"
+            ],
+            "title": "GC Guidance/Opinions"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "019:60"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Jediny",
                 "hasEmail": "mailto:John.Jediny@hq.doe.gov"
             },
+            "dataQuality": true,
+            "description": "This site is part of pilot effort at the US Department of Energy (DOE) - Office of NEPA Policy and Compliance to evaluate providing IT web services as a shared service, hosted on the cloud, and using only Free and Open Source Software (FOSS). The site is an integrated component of the larger NEPAnode project but is a stand alone service. The site allows users to upload static map images with no geographic data so that they can be accurately referenced/rectified on an webmap. This site allows for the revitalizing of otherwise unusable/archived maps such as historic maps, site surveys, site plans, etc. turning them into usable geographic data which is subsequently made available as a KML file for use in Google Earth/Maps and as a Web Mapping Service (WMS) for using in web-based webmapping application such as NEPAnode or in desktop GIS software.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -26328,46 +26319,47 @@
                     "title": "NEPANODE MapWarper"
                 }
             ],
+            "identifier": "DOE-019-1457678395",
             "keyword": [
                 "georeferenced maps",
                 "historical data",
                 "historical maps"
             ],
-            "bureauCode": [
-                "019:60"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2014-08-29",
             "programCode": [
                 "019:053"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE General Counsel"
+            },
+            "rights": "This site is made publically available, but individual users can choose to post maps as public or private resources.",
+            "spatial": "United States",
+            "temporal": "2014-07-01/2014-12-30",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "NEPAnode MapWarper"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "U.S. Department of Energy (DOE) Categorical Exclusion (CX) Determinations Under the National Environmental Protection Act (NEPA) II",
-            "description": "To further transparency and openness, DOE established a policy to document and post online all CX determinations involving classes of actions listed in Appendix B to Subpart D of the DOE NEPA regulations (10 CFR Part 1021).  The database contains CX determinations required to be posted under the policy, and also some for which documentation and posting are optional, i.e., determinations involving classes of actions listed in Appendix A or made before the policy's effective date of November 2, 2009.  The database may be searched by state, CX applied, date range, DOE Program, Field, or Site Office, keyword, and whether the CX determination is for a project related to the American Recovery and Reinvestment Act (Recovery Act or ARRA) of 2009.  Links to CX determination documents are provided.  The database will be updated approximately monthly.  See http://www.gc.doe.gov/NEPA/categorical_exclusion_determinations.htm for information on DOE CX procedures. For further information on DOE's NEPA compliance program, see http://www.gc.energy.gov/nepa or  email:  askNEPA@hq.doe.gov.",
-            "modified": "2010-01-20",
             "accessLevel": "public",
-            "identifier": "DOE-019-1587334455",
-            "dataQuality": true,
-            "describedBy": "http://cxnepa.energy.gov",
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "spatial": "United States",
-            "temporal": "2009/2010",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE Offfice of General Council"
-            },
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "019:60"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Eric Cohen",
                 "hasEmail": "mailto:eric.cohen@hq.doe.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://cxnepa.energy.gov",
+            "description": "To further transparency and openness, DOE established a policy to document and post online all CX determinations involving classes of actions listed in Appendix B to Subpart D of the DOE NEPA regulations (10 CFR Part 1021).  The database contains CX determinations required to be posted under the policy, and also some for which documentation and posting are optional, i.e., determinations involving classes of actions listed in Appendix A or made before the policy's effective date of November 2, 2009.  The database may be searched by state, CX applied, date range, DOE Program, Field, or Site Office, keyword, and whether the CX determination is for a project related to the American Recovery and Reinvestment Act (Recovery Act or ARRA) of 2009.  Links to CX determination documents are provided.  The database will be updated approximately monthly.  See http://www.gc.doe.gov/NEPA/categorical_exclusion_determinations.htm for information on DOE CX procedures. For further information on DOE's NEPA compliance program, see http://www.gc.energy.gov/nepa or  email:  askNEPA@hq.doe.gov.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -26375,6 +26367,7 @@
                     "title": "CX Determinations II"
                 }
             ],
+            "identifier": "DOE-019-1587334455",
             "keyword": [
                 "10 CFR 1021",
                 "ARPA",
@@ -26518,45 +26511,45 @@
                 "tribe",
                 "water"
             ],
-            "bureauCode": [
-                "019:60"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2010-01-20",
             "programCode": [
                 "019:053"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE Offfice of General Council"
+            },
             "references": [
                 "http://cxnepa.energy.gov"
             ],
+            "spatial": "United States",
+            "temporal": "2009/2010",
             "theme": [
                 "environment and geography"
-            ]
+            ],
+            "title": "U.S. Department of Energy (DOE) Categorical Exclusion (CX) Determinations Under the National Environmental Protection Act (NEPA) II"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Raw Data for U. S. Department of Energy (DOE) Categorical Exclusion(CX) Determinations Under the National Environmental Policy Act (NEPA)",
-            "description": "To further transparency and openness, DOE established a policy to document and post online all CX determinations involving classes of actions listed in Appendix B to Subpart D of the DOE NEPA regulations (10 CFR Part 1021).  This raw data set contains CX determinations required to be posted under the policy, and also some for which documentation and posting are optional, i.e., determinations involving classes of actions listed in Appendix A or made before the policy's effective date of November 2, 2009.  The data set includes information by state, CX applied, date range, DOE Program, Field, or Site Office, keyword, and whether the CX determination is for a project related to the American Recovery and Reinvestment Act (Recovery Act or ARRA) of 2009.  The web address to the CX determination documents are provided.  This data set will be updated approximately monthly.  See www.gc.doe.gov/NEPA/categorical_exclusion_determinations.htm for information on DOE CX procedures. For further information on DOE's NEPA compliance program, see www.gc.energy.gov/nepa or  email:  askNEPA@hq.doe.gov.",
-            "modified": "2010-02-16",
             "accessLevel": "public",
-            "identifier": "DOE-019-1935446677",
-            "dataQuality": true,
-            "describedBy": "http://CXNEPA.energy.gov",
-            "issued": "2010-02-16",
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "spatial": "United States",
-            "temporal": "2009/2010",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE Offfice of General Council"
-            },
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "019:60"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Eric Cohen",
                 "hasEmail": "mailto:eric.cohen@hq.doe.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://CXNEPA.energy.gov",
+            "description": "To further transparency and openness, DOE established a policy to document and post online all CX determinations involving classes of actions listed in Appendix B to Subpart D of the DOE NEPA regulations (10 CFR Part 1021).  This raw data set contains CX determinations required to be posted under the policy, and also some for which documentation and posting are optional, i.e., determinations involving classes of actions listed in Appendix A or made before the policy's effective date of November 2, 2009.  The data set includes information by state, CX applied, date range, DOE Program, Field, or Site Office, keyword, and whether the CX determination is for a project related to the American Recovery and Reinvestment Act (Recovery Act or ARRA) of 2009.  The web address to the CX determination documents are provided.  This data set will be updated approximately monthly.  See www.gc.doe.gov/NEPA/categorical_exclusion_determinations.htm for information on DOE CX procedures. For further information on DOE's NEPA compliance program, see www.gc.energy.gov/nepa or  email:  askNEPA@hq.doe.gov.",
+            "identifier": "DOE-019-1935446677",
+            "issued": "2010-02-16",
             "keyword": [
                 "10 CFR 1021",
                 "ARPA",
@@ -26703,54 +26696,53 @@
                 "tribe",
                 "water"
             ],
-            "bureauCode": [
-                "019:60"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2010-02-16",
             "programCode": [
                 "019:053"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE Offfice of General Council"
+            },
             "references": [
                 "http://CXNEPA.energy.gov"
             ],
+            "spatial": "United States",
+            "temporal": "2009/2010",
             "theme": [
                 "environment and geography"
-            ]
+            ],
+            "title": "Raw Data for U. S. Department of Energy (DOE) Categorical Exclusion(CX) Determinations Under the National Environmental Policy Act (NEPA)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "U.S. Department of Energy (DOE) Categorical Exclusion (CX) Determinations Under the National Environmental Protection Act (NEPA)",
-            "description": "To further transparency and openness, DOE established a policy to document and post online all CX determinations involving classes of actions listed in Appendix B to Subpart D of the DOE NEPA regulations (10 CFR Part 1021). This database contains CX determinations required to be posted under the policy, and also some for which documentation and posting are optional, i.e., determinations involving classes of actions listed in Appendix A or made before the policy's effective date of November 2, 2009.",
-            "modified": "2010-12-17",
             "accessLevel": "public",
-            "identifier": "DOE-019-4378457688",
-            "dataQuality": true,
-            "describedBy": "http://energy.gov/nepa/nepa-documents/categorical-exclusion-determinations",
-            "issued": "2010-01-01",
-            "landingPage": "http://energy.gov/nepa/nepa-documents/categorical-exclusion-determinations",
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "spatial": "United States",
-            "temporal": "2009/2010",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE"
-            },
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "019:60"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Eric Cohen",
                 "hasEmail": "mailto:eric.cohen@hq.doe.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://energy.gov/nepa/nepa-documents/categorical-exclusion-determinations",
+            "description": "To further transparency and openness, DOE established a policy to document and post online all CX determinations involving classes of actions listed in Appendix B to Subpart D of the DOE NEPA regulations (10 CFR Part 1021). This database contains CX determinations required to be posted under the policy, and also some for which documentation and posting are optional, i.e., determinations involving classes of actions listed in Appendix A or made before the policy's effective date of November 2, 2009.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://energy.gov/nepa/nepa-documents/categorical-exclusion-determinations",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "CX Determinations",
-                    "downloadURL": "https://energy.gov/nepa/nepa-documents/categorical-exclusion-determinations"
+                    "title": "CX Determinations"
                 }
             ],
+            "identifier": "DOE-019-4378457688",
+            "issued": "2010-01-01",
             "keyword": [
                 "ARRA",
                 "block",
@@ -26767,55 +26759,54 @@
                 "retrofit",
                 "transportation"
             ],
-            "bureauCode": [
-                "019:60"
+            "landingPage": "http://energy.gov/nepa/nepa-documents/categorical-exclusion-determinations",
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2010-12-17",
             "programCode": [
                 "019:053"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE"
+            },
             "references": [
                 "http://energy.gov/node/289357"
             ],
+            "spatial": "United States",
+            "temporal": "2009/2010",
             "theme": [
                 "environment and geography"
-            ]
+            ],
+            "title": "U.S. Department of Energy (DOE) Categorical Exclusion (CX) Determinations Under the National Environmental Protection Act (NEPA)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "DOE User-Facilities and R&D Equipment",
-            "description": "This dataset contains information about hundreds of designated user-facilities and R&D equipment funded by the U.S. Department of Energy and accessible to the private sector. These facilities reside at DOE's National Laboratories throughout the United States and are meant to advance scientific research and accelerated technology commercialization.",
-            "modified": "2014-06-16",
             "accessLevel": "public",
-            "identifier": "DOE-019-9876543212",
-            "dataQuality": true,
-            "describedByType": "text/csv",
-            "landingPage": "http://energy.gov/oha",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "Copyright restrictions may apply to some items in this data asset",
-            "spatial": "United States",
-            "temporal": "2014/2014",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE Office of Science"
-            },
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Benjamin Brown",
                 "hasEmail": "mailto:Benjamin.Brown@science.doe.gov"
             },
+            "dataQuality": true,
+            "describedByType": "text/csv",
+            "description": "This dataset contains information about hundreds of designated user-facilities and R&D equipment funded by the U.S. Department of Energy and accessible to the private sector. These facilities reside at DOE's National Laboratories throughout the United States and are meant to advance scientific research and accelerated technology commercialization.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
-                    "title": "DOE User-Facilities and R&D Equipment",
-                    "description": "This dataset contains information about hundreds of designated user-facilities and R&D equipment funded by the U.S. Department of Energy and accessible to the private sector. These facilities reside at DOE's National Laboratories throughout the United States and are meant to advanced scientific research and accelerated technology commercialization.",
                     "describedByType": "text/csv",
-                    "downloadURL": "https://energy.gov/sites/prod/files/DOE_Facilities_Inventory_2014_16_06.csv"
+                    "description": "This dataset contains information about hundreds of designated user-facilities and R&D equipment funded by the U.S. Department of Energy and accessible to the private sector. These facilities reside at DOE's National Laboratories throughout the United States and are meant to advanced scientific research and accelerated technology commercialization.",
+                    "downloadURL": "https://energy.gov/sites/prod/files/DOE_Facilities_Inventory_2014_16_06.csv",
+                    "mediaType": "text/csv",
+                    "title": "DOE User-Facilities and R&D Equipment"
                 }
             ],
+            "identifier": "DOE-019-9876543212",
             "keyword": [
                 "Accelerator",
                 "Ames",
@@ -26859,42 +26850,41 @@
                 "lab",
                 "science"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://energy.gov/oha",
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2014-06-16",
             "programCode": [
                 "019:000"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE Office of Science"
+            },
+            "rights": "Copyright restrictions may apply to some items in this data asset",
+            "spatial": "United States",
+            "temporal": "2014/2014",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "DOE User-Facilities and R&D Equipment"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "OSTI.GOV",
-            "description": "OSTI.GOV is the primary search tool for DOE science, technology, and engineering research and development results and the organizational hub for information about the DOE Office of Scientific and Technical Information.  OSTI.GOV makes discoverable over 70 years of research results from DOE and its predecessor agencies.  Research results include journal articles/accepted manuscripts and related metadata; technical reports; scientific research datasets and collections; scientific software; patents; conference and workshop papers; books and theses; and multimedia.",
-            "modified": "2025-01-10T16:30:09.697Z",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-2964124376",
-            "dataQuality": true,
-            "landingPage": "http://www.osti.gov/",
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "rights": "copyright resctrictions may apply to some items in this dataset",
-            "spatial": "United States",
-            "temporal": "1940/2020",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE Office of Scientific and Technical Information"
-            },
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Carly Robinson",
                 "hasEmail": "mailto:comments@osti.gov"
             },
+            "dataQuality": true,
+            "description": "OSTI.GOV is the primary search tool for DOE science, technology, and engineering research and development results and the organizational hub for information about the DOE Office of Scientific and Technical Information.  OSTI.GOV makes discoverable over 70 years of research results from DOE and its predecessor agencies.  Research results include journal articles/accepted manuscripts and related metadata; technical reports; scientific research datasets and collections; scientific software; patents; conference and workshop papers; books and theses; and multimedia.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -26908,6 +26898,7 @@
                     "title": "OSTI.GOV"
                 }
             ],
+            "identifier": "DOE-019-2964124376",
             "keyword": [
                 "AEC",
                 "Atomic Energy Commission",
@@ -27015,55 +27006,54 @@
                 "weaponry",
                 "wind energy"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "http://www.osti.gov/",
+            "language": [
+                "en-US"
             ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2025-01-10T16:30:09.697Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE Office of Scientific and Technical Information"
+            },
+            "rights": "copyright resctrictions may apply to some items in this dataset",
+            "spatial": "United States",
+            "temporal": "1940/2020",
             "theme": [
                 "science"
-            ]
+            ],
+            "title": "OSTI.GOV"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "DOE PAGES",
-            "description": "The Department of Energy Public Access Gateway for Energy and Science (DOE PAGES) is the DOE search tool that makes scholarly scientific publications, resulting from DOE research funding, publicly accessible and discoverable at no charge to users.  Also provided are API and XML services.",
-            "modified": "2025-01-10T16:29:45.466Z",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-2956156643",
-            "dataQuality": true,
-            "landingPage": "http://www.osti.gov/pages/",
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "rights": "copyright resctrictions may apply to some items in this dataset.",
-            "spatial": "Global",
-            "temporal": "2012/2020",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE Office of Scientific and Technical Information"
-            },
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Natalie Barnett",
                 "hasEmail": "mailto:pagescomments@osti.gov"
             },
+            "dataQuality": true,
+            "description": "The Department of Energy Public Access Gateway for Energy and Science (DOE PAGES) is the DOE search tool that makes scholarly scientific publications, resulting from DOE research funding, publicly accessible and discoverable at no charge to users.  Also provided are API and XML services.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.osti.gov/pages/",
                     "mediaType": "text/html",
-                    "title": "DOE PAGES",
-                    "downloadURL": "https://www.osti.gov/pages/"
+                    "title": "DOE PAGES"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/xml",
+                    "downloadURL": "https://www.osti.gov/pages/pagesxml",
                     "format": "XML",
-                    "title": "XML Service",
-                    "downloadURL": "https://www.osti.gov/pages/pagesxml"
+                    "mediaType": "application/xml",
+                    "title": "XML Service"
                 },
                 {
                     "@type": "dcat:Distribution",
@@ -27072,6 +27062,7 @@
                     "title": "REST API"
                 }
             ],
+            "identifier": "DOE-019-2956156643",
             "keyword": [
                 "12 months",
                 "DOE",
@@ -27096,42 +27087,41 @@
                 "scientific journals",
                 "version of record"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "http://www.osti.gov/pages/",
+            "language": [
+                "en-US"
             ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2025-01-10T16:29:45.466Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE Office of Scientific and Technical Information"
+            },
+            "rights": "copyright resctrictions may apply to some items in this dataset.",
+            "spatial": "Global",
+            "temporal": "2012/2020",
             "theme": [
                 "science"
-            ]
+            ],
+            "title": "DOE PAGES"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "DOE ScienceCinema",
-            "description": "DOE ScienceCinema highlights scientific videos featuring leading-edge research from the U.S. Department of Energy.  Using innovative, state-of-the-art audio indexing and speech recognition technology from IBM Watson, ScienceCinema allows users to search for specific words and phrases spoken within video files.",
-            "modified": "2025-01-10T16:26:39.813Z",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-2957115645",
-            "dataQuality": true,
-            "landingPage": "http://www.osti.gov/sciencecinema/",
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "rights": "copyright resctrictions may apply to some items in this dataset",
-            "spatial": "Global",
-            "temporal": "2013/2020",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE Office of Scientific and Technical Information"
-            },
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Catherine Pepmiller",
                 "hasEmail": "mailto:sciencecinema@osti.gov"
             },
+            "dataQuality": true,
+            "description": "DOE ScienceCinema highlights scientific videos featuring leading-edge research from the U.S. Department of Energy.  Using innovative, state-of-the-art audio indexing and speech recognition technology from IBM Watson, ScienceCinema allows users to search for specific words and phrases spoken within video files.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -27145,6 +27135,7 @@
                     "title": "REST API"
                 }
             ],
+            "identifier": "DOE-019-2957115645",
             "keyword": [
                 "CERN",
                 "DOE",
@@ -27168,42 +27159,41 @@
                 "symposia",
                 "videos"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "http://www.osti.gov/sciencecinema/",
+            "language": [
+                "en-US"
             ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2025-01-10T16:26:39.813Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE Office of Scientific and Technical Information"
+            },
+            "rights": "copyright resctrictions may apply to some items in this dataset",
+            "spatial": "Global",
+            "temporal": "2013/2020",
             "theme": [
                 "science"
-            ]
+            ],
+            "title": "DOE ScienceCinema"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "DOE CODE",
-            "description": "A DOE software services platform and search tool for DOE-funded code.  DOE CODE provides functionality for collaboration, archiving, and discovery of scientific and business software.  DOE CODE replaces OSTI's old software center, the Energy Science and Technology Software Center (ESTSC).",
-            "modified": "2025-01-10T16:27:58.412Z",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-2964124377",
-            "describedByType": "software/html",
-            "landingPage": "https://www.osti.gov/doecode/",
-            "license": "https://project-open-data.cio.gov/unknown-license",
-            "rights": "copyright restrictions may apply to some items in this dataset",
-            "spatial": "United States",
-            "temporal": "2018/2020",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE Office of Scientific and Technical Information"
-            },
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Natalie Barnett",
                 "hasEmail": "mailto:doecode@osti.gov"
             },
+            "describedByType": "software/html",
+            "description": "A DOE software services platform and search tool for DOE-funded code.  DOE CODE provides functionality for collaboration, archiving, and discovery of scientific and business software.  DOE CODE replaces OSTI's old software center, the Energy Science and Technology Software Center (ESTSC).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -27217,6 +27207,7 @@
                     "title": "REST API"
                 }
             ],
+            "identifier": "DOE-019-2964124377",
             "keyword": [
                 "DOE",
                 "Department of Energy",
@@ -27229,43 +27220,42 @@
                 "science research",
                 "software"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.osti.gov/doecode/",
+            "language": [
+                "us-EN"
             ],
+            "license": "https://project-open-data.cio.gov/unknown-license",
+            "modified": "2025-01-10T16:27:58.412Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "us-EN"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE Office of Scientific and Technical Information"
+            },
+            "rights": "copyright restrictions may apply to some items in this dataset",
+            "spatial": "United States",
+            "temporal": "2018/2020",
             "theme": [
                 "science"
-            ]
+            ],
+            "title": "DOE CODE"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "DOE Patents",
-            "description": "DOE Patents, developed by the U.S. Department of Energy (DOE) Office of Scientific and Technical Information (OSTI), is a searchable database of patent information resulting from DOE-sponsored research and development (R&D).  Included here are patents that DOE sponsored through a variety of funding mechanisms, including grants, contracts, or cooperative agreements.",
-            "modified": "2025-01-10T16:27:13.094Z",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-2964124378",
-            "dataQuality": true,
-            "describedByType": "text/html",
-            "landingPage": "https://www.osti.gov/doepatents/",
-            "license": "https://project-open-data.cio.gov/unknown-license",
-            "rights": "copyright restriction may apply to some items in this dataset",
-            "spatial": "United States",
-            "temporal": "1940/2020",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE Office of Scientific and Technical Information"
-            },
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Lynn Davis",
                 "hasEmail": "mailto:doepatentscomments@osti.gov"
             },
+            "dataQuality": true,
+            "describedByType": "text/html",
+            "description": "DOE Patents, developed by the U.S. Department of Energy (DOE) Office of Scientific and Technical Information (OSTI), is a searchable database of patent information resulting from DOE-sponsored research and development (R&D).  Included here are patents that DOE sponsored through a variety of funding mechanisms, including grants, contracts, or cooperative agreements.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -27280,11 +27270,12 @@
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.osti.gov/doepatents/doepatentsxml",
                     "mediaType": "application/xml",
-                    "title": "XML Service",
-                    "downloadURL": "https://www.osti.gov/doepatents/doepatentsxml"
+                    "title": "XML Service"
                 }
             ],
+            "identifier": "DOE-019-2964124378",
             "keyword": [
                 "DOE",
                 "Department of Energy",
@@ -27303,51 +27294,51 @@
                 "technology",
                 "united states patent and trademark office"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.osti.gov/doepatents/",
+            "language": [
+                "us-EN"
             ],
+            "license": "https://project-open-data.cio.gov/unknown-license",
+            "modified": "2025-01-10T16:27:13.094Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "us-EN"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE Office of Scientific and Technical Information"
+            },
+            "rights": "copyright restriction may apply to some items in this dataset",
+            "spatial": "United States",
+            "temporal": "1940/2020",
             "theme": [
                 "science"
-            ]
+            ],
+            "title": "DOE Patents"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "OAI-PMH for DOE Research and Development Reports",
-            "description": "OSTI has established an OAI (Open Archives Initiative) server to allow harvesting of metadata for full-text DOE research and development reports contained in OSTI.GOV.  Included are reports in phsyics, chemistry, materials, biology, environmental sciences, energy technologies, engineering, computer and information science, renewable energy, and other topics.  These reports are produced by DOE, the DOE National Laboratories, and DOE contractors and grantees primarily from 1991 forward.",
-            "modified": "2025-01-10T16:26:15.369Z",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-2964124379",
-            "dataQuality": true,
-            "landingPage": "https://www.osti.gov/oai",
-            "license": "https://project-open-data.cio.gov/unknown-license",
-            "rights": "copyright restrictions may apply to some items in this dataset",
-            "spatial": "United States",
-            "temporal": "1940/2020",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE Office of Scientific and Technical Information"
-            },
             "accrualPeriodicity": "R/P1D",
-            "isPartOf": "DOE-019-2964124376",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Catherine Pepmiller",
                 "hasEmail": "mailto:OAIrecords@osti.gov"
             },
+            "dataQuality": true,
+            "description": "OSTI has established an OAI (Open Archives Initiative) server to allow harvesting of metadata for full-text DOE research and development reports contained in OSTI.GOV.  Included are reports in phsyics, chemistry, materials, biology, environmental sciences, energy technologies, engineering, computer and information science, renewable energy, and other topics.  These reports are produced by DOE, the DOE National Laboratories, and DOE contractors and grantees primarily from 1991 forward.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.osti.gov/oai/",
                     "mediaType": "application/xml",
-                    "title": "OSTI.GOV OAI-PMH",
-                    "downloadURL": "https://www.osti.gov/oai/"
+                    "title": "OSTI.GOV OAI-PMH"
                 }
             ],
+            "identifier": "DOE-019-2964124379",
+            "isPartOf": "DOE-019-2964124376",
             "keyword": [
                 "DOE",
                 "Department of Energy",
@@ -27371,43 +27362,41 @@
                 "science research",
                 "technology"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.osti.gov/oai",
+            "language": [
+                "us-EN"
             ],
+            "license": "https://project-open-data.cio.gov/unknown-license",
+            "modified": "2025-01-10T16:26:15.369Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "us-EN"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE Office of Scientific and Technical Information"
+            },
+            "rights": "copyright restrictions may apply to some items in this dataset",
+            "spatial": "United States",
+            "temporal": "1940/2020",
             "theme": [
                 "science"
-            ]
+            ],
+            "title": "OAI-PMH for DOE Research and Development Reports"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "DOE MARC Records",
-            "description": "The U.S. Department of Energy (DOE) Office of Scientific and Technical Information (OSTI) offers the ability to download records of DOE scientific and technical information (STI) in Machine-Readable Cataloging (MARC) record format.  Full-text documents are primarily from 1991 forward, but approximately 25% of the records with full-text are from earlier years.  OSTI.GOV includes STI documents that were produced by DOE, the DOE contractor community, and DOE granteees.  STI documents from DOE predecessor agencies - the U.S. Atomic Energy Commission (AEC) and the Energy Research and Development Administration (ERDA) - are also included.  Legacy documents are added as they become available in electronic format.  MARC records are available as soon as full-text documents are added to OSTI.GOV",
-            "modified": "2025-01-10T16:25:42.341Z",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-2964124380",
-            "dataQuality": true,
-            "landingPage": "https://www.osti.gov/marc-records",
-            "license": "https://project-open-data.cio.gov/unknown-license",
-            "rights": "copyright restrictions may apply to some items in this dataset",
-            "spatial": "United States",
-            "temporal": "1940/2020",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE Office of Scientific and Technical Information"
-            },
             "accrualPeriodicity": "R/P1D",
-            "isPartOf": "DOE-019-2964124376",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Catherine Pepmiller",
                 "hasEmail": "mailto:MARCrecords@osti.gov"
             },
+            "dataQuality": true,
+            "description": "The U.S. Department of Energy (DOE) Office of Scientific and Technical Information (OSTI) offers the ability to download records of DOE scientific and technical information (STI) in Machine-Readable Cataloging (MARC) record format.  Full-text documents are primarily from 1991 forward, but approximately 25% of the records with full-text are from earlier years.  OSTI.GOV includes STI documents that were produced by DOE, the DOE contractor community, and DOE granteees.  STI documents from DOE predecessor agencies - the U.S. Atomic Energy Commission (AEC) and the Energy Research and Development Administration (ERDA) - are also included.  Legacy documents are added as they become available in electronic format.  MARC records are available as soon as full-text documents are added to OSTI.GOV",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -27415,6 +27404,8 @@
                     "title": "DOE MARC Records"
                 }
             ],
+            "identifier": "DOE-019-2964124380",
+            "isPartOf": "DOE-019-2964124376",
             "keyword": [
                 "AEC",
                 "DOE",
@@ -27442,51 +27433,51 @@
                 "science",
                 "technology"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.osti.gov/marc-records",
+            "language": [
+                "us-EN"
             ],
+            "license": "https://project-open-data.cio.gov/unknown-license",
+            "modified": "2025-01-10T16:25:42.341Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "us-EN"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE Office of Scientific and Technical Information"
+            },
+            "rights": "copyright restrictions may apply to some items in this dataset",
+            "spatial": "United States",
+            "temporal": "1940/2020",
             "theme": [
                 "science"
-            ]
+            ],
+            "title": "DOE MARC Records"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Department of Energy M&O Small Business Subcontract Annual Summary (FY 2015)",
-            "description": "This contains a summary of all reported and validated M&O Prime Contractor 1st\u00a0tier subcontractor small business award dollars for the government\u2019s most recently completed fiscal year. The file summarizes the data by M&O contractor.",
-            "modified": "2016-01-21",
             "accessLevel": "public",
-            "identifier": "MOSRC-FY2015-SSR-01212016",
-            "license": "https://project-open-data.cio.gov/unknown-license",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of Small and Disadvantaged Business Utilization (OSDBU)",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Department of Energy"
-                }
-            },
+            "bureauCode": [
+                "019:60"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Hale",
                 "hasEmail": "mailto:john.hale@hq.doe.gov"
             },
+            "description": "This contains a summary of all reported and validated M&O Prime Contractor 1st\u00a0tier subcontractor small business award dollars for the government\u2019s most recently completed fiscal year. The file summarizes the data by M&O contractor.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://inventory.data.gov/dataset/dd865c8f-3d36-4910-9059-2d912f69bff0/resource/c4f79f9f-2df1-4d94-8b81-4e00d07c236d/download/fy201520mo20small20business20subcontracting20summary20report01212016.xlsx",
-                    "format": "xlsx",
-                    "title": "FY2015 MO Small Business Subcontracting Summary Report_01212016",
-                    "description": "This contains a summary of all reported and validated M&O Prime Contractor 1st\u00a0tier subcontractor small business award dollars for the government\u2019s most recently completed fiscal year. The file summarizes the data by M&O contractor.",
                     "describedBy": "http://energy.gov/management/management-operating-subcontract-reporting-capability-mosrc",
-                    "describedByType": "text/html"
+                    "describedByType": "text/html",
+                    "description": "This contains a summary of all reported and validated M&O Prime Contractor 1st\u00a0tier subcontractor small business award dollars for the government\u2019s most recently completed fiscal year. The file summarizes the data by M&O contractor.",
+                    "format": "xlsx",
+                    "title": "FY2015 MO Small Business Subcontracting Summary Report_01212016"
                 }
             ],
+            "identifier": "MOSRC-FY2015-SSR-01212016",
             "keyword": [
                 "MOSRC",
                 "Procurement",
@@ -27496,28 +27487,11 @@
                 "small business",
                 "subcontract"
             ],
-            "bureauCode": [
-                "019:60"
-            ],
+            "license": "https://project-open-data.cio.gov/unknown-license",
+            "modified": "2016-01-21",
             "programCode": [
                 "019:053"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Department of Energy M&O Small Business Subcontract Public Data Extract (FY 2015)",
-            "description": "This contains all reported and validated M&O Prime Contractor 1st\u00a0tier subcontractor small business award dollars for the government\u2019s most recently completed fiscal year. The file contains 55 data elements that represent a subset of FPDS-NG data.",
-            "modified": "2016-03-16",
-            "accessLevel": "public",
-            "identifier": "MOSRC-FY2015-SPDE-01212016",
-            "dataQuality": true,
-            "describedBy": "http://www.energy.gov/sites/prod/files/2016/01/f29/MOSRC%20Field%20Definitions%2001202016.pdf",
-            "describedByType": "application/msword",
-            "issued": "2015-01-29",
-            "landingPage": "http://www.energy.gov/management/management-operating-subcontract-reporting-capability-mosrc",
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "spatial": "United States",
-            "temporal": "2014-10-01/2015-09-30",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Small and Disadvantaged Business Utilization (OSDBU)",
@@ -27526,23 +27500,37 @@
                     "name": "Department of Energy"
                 }
             },
+            "title": "Department of Energy M&O Small Business Subcontract Annual Summary (FY 2015)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "019:60"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Hale",
                 "hasEmail": "mailto:john.hale@hq.doe.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.energy.gov/sites/prod/files/2016/01/f29/MOSRC%20Field%20Definitions%2001202016.pdf",
+            "describedByType": "application/msword",
+            "description": "This contains all reported and validated M&O Prime Contractor 1st\u00a0tier subcontractor small business award dollars for the government\u2019s most recently completed fiscal year. The file contains 55 data elements that represent a subset of FPDS-NG data.",
             "distribution": [
                 {
-                    "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "xlsx",
-                    "title": "FY2015 MO Small Business Subcontracting Report",
-                    "description": "This contains all reported and validated M&O Prime Contractor 1st\u00a0tier subcontractor small business award dollars for the government\u2019s most recently completed fiscal year. The file contains 55 data elements that represent a subset of FPDS-NG data.",
+                    "@type": "dcat:Distribution",
                     "describedBy": "http://energy.gov/management/management-operating-subcontract-reporting-capability-mosrc",
                     "describedByType": "text/html",
-                    "downloadURL": "https://www.energy.gov/sites/prod/files/2016/03/f30/FY2015%20MO%20Small%20Business%20Subcontracting%20Report_Public_2.xlsx"
+                    "description": "This contains all reported and validated M&O Prime Contractor 1st\u00a0tier subcontractor small business award dollars for the government\u2019s most recently completed fiscal year. The file contains 55 data elements that represent a subset of FPDS-NG data.",
+                    "downloadURL": "https://www.energy.gov/sites/prod/files/2016/03/f30/FY2015%20MO%20Small%20Business%20Subcontracting%20Report_Public_2.xlsx",
+                    "format": "xlsx",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "FY2015 MO Small Business Subcontracting Report"
                 }
             ],
+            "identifier": "MOSRC-FY2015-SPDE-01212016",
+            "issued": "2015-01-29",
             "keyword": [
                 "MOSRC",
                 "Procurement",
@@ -27550,40 +27538,39 @@
                 "small business",
                 "subcontractor"
             ],
-            "bureauCode": [
-                "019:60"
-            ],
+            "landingPage": "http://www.energy.gov/management/management-operating-subcontract-reporting-capability-mosrc",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2016-03-16",
             "programCode": [
                 "019:053"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Department of Energy Directives, Delegations, and Requirements (RevCom)",
-            "description": "Directives are the Department of Energy's primary means of establishing policies, requirements, responsibilities, and procedures for Departmental elements and contractors. In this database, the public can browse all Dept. of Energy directives (current and past).",
-            "modified": "2020-08-27",
-            "accessLevel": "restricted public",
-            "identifier": "DOE-019-0548762664",
-            "dataQuality": true,
-            "landingPage": "https://www.directives.doe.gov",
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "rights": "Requires creation of a user account to access the database",
-            "spatial": "DOE",
-            "temporal": "2008/2020",
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Directives Program",
+                "name": "Office of Small and Disadvantaged Business Utilization (OSDBU)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of Management"
+                    "name": "Department of Energy"
                 }
             },
+            "spatial": "United States",
+            "temporal": "2014-10-01/2015-09-30",
+            "title": "Department of Energy M&O Small Business Subcontract Public Data Extract (FY 2015)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "019:60"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Christopher Tirado",
                 "hasEmail": "mailto:christopher.tirado@hq.doe.gov"
             },
+            "dataQuality": true,
+            "description": "Directives are the Department of Energy's primary means of establishing policies, requirements, responsibilities, and procedures for Departmental elements and contractors. In this database, the public can browse all Dept. of Energy directives (current and past).",
+            "identifier": "DOE-019-0548762664",
             "keyword": [
                 "Directives review",
                 "Directives writers",
@@ -27594,52 +27581,54 @@
                 "Policies",
                 "RevCom"
             ],
-            "bureauCode": [
-                "019:60"
+            "landingPage": "https://www.directives.doe.gov",
+            "language": [
+                "en-US"
             ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2020-08-27",
             "programCode": [
                 "019:053"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "Corporate Management"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Department of Energy M&O Small Business Subcontract Annual Summary (FY 2016)",
-            "description": "This contains a summary of all reported and validated M&O Prime Contractor 1st\u00a0tier subcontractor small business award dollars for the government\u2019s most recently completed fiscal year. The file summarizes the data by M&O contractor.",
-            "modified": "2017-01-17",
-            "accessLevel": "public",
-            "identifier": "MOSRC-FY2016-SSR-01172017",
-            "license": "https://project-open-data.cio.gov/unknown-license",
-            "spatial": "United States",
-            "temporal": "2016-01-01/2016-12-31",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Small and Disadvantaged Business Utilization (OSDBU)",
+                "name": "Directives Program",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Department of Energy"
+                    "name": "Office of Management"
                 }
             },
+            "rights": "Requires creation of a user account to access the database",
+            "spatial": "DOE",
+            "temporal": "2008/2020",
+            "theme": [
+                "Corporate Management"
+            ],
+            "title": "Department of Energy Directives, Delegations, and Requirements (RevCom)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "019:60"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Hale",
                 "hasEmail": "mailto:john.hale@hq.doe.gov"
             },
+            "description": "This contains a summary of all reported and validated M&O Prime Contractor 1st\u00a0tier subcontractor small business award dollars for the government\u2019s most recently completed fiscal year. The file summarizes the data by M&O contractor.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "Excel",
-                    "title": "Department of Energy M&O Small Business Subcontract Annual Summary (FY 2016)",
                     "description": "This contains a summary of all reported and validated M&O Prime Contractor 1st\u00a0tier subcontractor small business award dollars for the government\u2019s most recently completed fiscal year. The file summarizes the data by M&O contractor.",
-                    "downloadURL": "https://inventory.data.gov/dataset/e2fe6ef2-7ccb-4f72-a186-dcfbc6c9b26b/resource/07fc72e6-f4a8-4e09-8c4b-565dd69e9995/download/department-of-energy-mo-small-business-subcontract-annual-summary-fy-2016.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/e2fe6ef2-7ccb-4f72-a186-dcfbc6c9b26b/resource/07fc72e6-f4a8-4e09-8c4b-565dd69e9995/download/department-of-energy-mo-small-business-subcontract-annual-summary-fy-2016.xlsx",
+                    "format": "Excel",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Department of Energy M&O Small Business Subcontract Annual Summary (FY 2016)"
                 }
             ],
+            "identifier": "MOSRC-FY2016-SSR-01172017",
             "keyword": [
                 "MOSRC",
                 "Procurement",
@@ -27649,28 +27638,11 @@
                 "small business",
                 "subcontract"
             ],
-            "bureauCode": [
-                "019:60"
-            ],
+            "license": "https://project-open-data.cio.gov/unknown-license",
+            "modified": "2017-01-17",
             "programCode": [
                 "019:053"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Department of Energy M&O Small Business Subcontract Public Data Extract (FY 2016)",
-            "description": "This contains all reported and validated M&O Prime Contractor 1st\u00a0tier subcontractor small business award dollars for the government\u2019s most recently completed fiscal year. The file contains 55 data elements that represent a subset of FPDS-NG data.",
-            "modified": "2017-01-17",
-            "accessLevel": "public",
-            "identifier": "MOSRC-FY2016-SPDE-01172017",
-            "dataQuality": true,
-            "describedBy": "http://www.energy.gov/sites/prod/files/2016/01/f29/MOSRC%20Field%20Definitions%2001202016.pdf",
-            "describedByType": "txt/xlsx",
-            "issued": "2015-01-29",
-            "landingPage": "http://www.energy.gov/management/management-operating-subcontract-reporting-capability-mosrc",
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "spatial": "United States",
-            "temporal": "2016-01-01/2016-12-31",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Small and Disadvantaged Business Utilization (OSDBU)",
@@ -27679,21 +27651,37 @@
                     "name": "Department of Energy"
                 }
             },
+            "spatial": "United States",
+            "temporal": "2016-01-01/2016-12-31",
+            "title": "Department of Energy M&O Small Business Subcontract Annual Summary (FY 2016)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "019:60"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Hale",
                 "hasEmail": "mailto:john.hale@hq.doe.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.energy.gov/sites/prod/files/2016/01/f29/MOSRC%20Field%20Definitions%2001202016.pdf",
+            "describedByType": "txt/xlsx",
+            "description": "This contains all reported and validated M&O Prime Contractor 1st\u00a0tier subcontractor small business award dollars for the government\u2019s most recently completed fiscal year. The file contains 55 data elements that represent a subset of FPDS-NG data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "Excel",
-                    "title": "Department of Energy M&O Small Business Subcontract Public Data Extract (FY 2016)",
                     "description": "This contains all reported and validated M&O Prime Contractor 1st\u00a0tier subcontractor small business award dollars for the government\u2019s most recently completed fiscal year. The file contains 55 data elements that represent a subset of FPDS-NG data.",
-                    "downloadURL": "https://inventory.data.gov/dataset/56f83731-9cad-4d37-a84e-bf656f3238bf/resource/99d2cfed-048e-4578-b28a-7cb734be6951/download/department-of-energy-mo-small-business-subcontract-public-data-extract-fy-2016.xlsx"
+                    "downloadURL": "https://inventory.data.gov/dataset/56f83731-9cad-4d37-a84e-bf656f3238bf/resource/99d2cfed-048e-4578-b28a-7cb734be6951/download/department-of-energy-mo-small-business-subcontract-public-data-extract-fy-2016.xlsx",
+                    "format": "Excel",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Department of Energy M&O Small Business Subcontract Public Data Extract (FY 2016)"
                 }
             ],
+            "identifier": "MOSRC-FY2016-SPDE-01172017",
+            "issued": "2015-01-29",
             "keyword": [
                 "MOSRC",
                 "Procurement",
@@ -27701,23 +27689,12 @@
                 "small business",
                 "subcontractor"
             ],
-            "bureauCode": [
-                "019:60"
-            ],
+            "landingPage": "http://www.energy.gov/management/management-operating-subcontract-reporting-capability-mosrc",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2017-01-17",
             "programCode": [
                 "019:053"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Department of Energy M&O Small Business Subcontract Annual Summary (FY 2017)",
-            "description": "This contains a summary of all reported and validated M&O Prime Contractor 1st\u00a0tier subcontractor small business award dollars for the government\u2019s most recently completed fiscal year. The file summarizes the data by M&O contractor.",
-            "modified": "2018-01-18",
-            "accessLevel": "public",
-            "identifier": "MOSRC-FY2017-SSR-011782018",
-            "license": "https://project-open-data.cio.gov/unknown-license",
-            "spatial": "United States",
-            "temporal": "2017-01-01/2017-12-31",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Small and Disadvantaged Business Utilization (OSDBU)",
@@ -27726,19 +27703,31 @@
                     "name": "Department of Energy"
                 }
             },
+            "spatial": "United States",
+            "temporal": "2016-01-01/2016-12-31",
+            "title": "Department of Energy M&O Small Business Subcontract Public Data Extract (FY 2016)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "019:60"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kent Hibben",
                 "hasEmail": "mailto:Kent.Hibben@hq.doe.gov"
             },
+            "description": "This contains a summary of all reported and validated M&O Prime Contractor 1st\u00a0tier subcontractor small business award dollars for the government\u2019s most recently completed fiscal year. The file summarizes the data by M&O contractor.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://inventory.data.gov/dataset/e50e3413-56f2-4b40-a635-a2075909f915/resource/83b7df8b-2837-421c-bdda-ad9ddf185538/download/department-of-energy-mo-small-business-subcontract-annual-summary-fy-2017.xlsx",
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "title": "Department of Energy M&O Small Business Subcontract Annual Summary (FY 2017)",
-                    "downloadURL": "https://inventory.data.gov/dataset/e50e3413-56f2-4b40-a635-a2075909f915/resource/83b7df8b-2837-421c-bdda-ad9ddf185538/download/department-of-energy-mo-small-business-subcontract-annual-summary-fy-2017.xlsx"
+                    "title": "Department of Energy M&O Small Business Subcontract Annual Summary (FY 2017)"
                 }
             ],
+            "identifier": "MOSRC-FY2017-SSR-011782018",
             "keyword": [
                 "MOSRC",
                 "Procurement",
@@ -27748,28 +27737,11 @@
                 "small business",
                 "subcontract"
             ],
-            "bureauCode": [
-                "019:60"
-            ],
+            "license": "https://project-open-data.cio.gov/unknown-license",
+            "modified": "2018-01-18",
             "programCode": [
                 "019:053"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Department of Energy M&O Small Business Subcontract Public Data Extract (FY 2017)",
-            "description": "This contains all reported and validated M&O Prime Contractor 1st\u00a0tier subcontractor small business award dollars for the government\u2019s most recently completed fiscal year. The file contains 55 data elements that represent a subset of FPDS-NG data.",
-            "modified": "2018-01-18",
-            "accessLevel": "public",
-            "identifier": "MOSRC-FY2017-SPDE-01182018",
-            "dataQuality": true,
-            "describedBy": "http://www.energy.gov/sites/prod/files/2016/01/f29/MOSRC%20Field%20Definitions%2001202016.pdf",
-            "describedByType": "txt/xlsx",
-            "issued": "2018-04-09",
-            "landingPage": "http://www.energy.gov/management/management-operating-subcontract-reporting-capability-mosrc",
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "spatial": "United States",
-            "temporal": "2017-01-01/2017-12-31",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Small and Disadvantaged Business Utilization (OSDBU)",
@@ -27778,20 +27750,36 @@
                     "name": "Department of Energy"
                 }
             },
+            "spatial": "United States",
+            "temporal": "2017-01-01/2017-12-31",
+            "title": "Department of Energy M&O Small Business Subcontract Annual Summary (FY 2017)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "019:60"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kent Hibben",
                 "hasEmail": "mailto:Kent.Hibben@hq.doe.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.energy.gov/sites/prod/files/2016/01/f29/MOSRC%20Field%20Definitions%2001202016.pdf",
+            "describedByType": "txt/xlsx",
+            "description": "This contains all reported and validated M&O Prime Contractor 1st\u00a0tier subcontractor small business award dollars for the government\u2019s most recently completed fiscal year. The file contains 55 data elements that represent a subset of FPDS-NG data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "downloadURL": "https://inventory.data.gov/dataset/c2c5ede6-1217-4e93-8c9f-effdeb2b11a6/resource/76a50a2e-3e08-4c1e-b68b-3a63c29558b4/download/department-of-energy-mo-small-business-subcontract-public-data-extract-fy-2017.xlsb",
                     "format": "xlsx",
-                    "title": "Department of Energy M&O Small Business Subcontract Public Data Extract (FY 2017)",
-                    "downloadURL": "https://inventory.data.gov/dataset/c2c5ede6-1217-4e93-8c9f-effdeb2b11a6/resource/76a50a2e-3e08-4c1e-b68b-3a63c29558b4/download/department-of-energy-mo-small-business-subcontract-public-data-extract-fy-2017.xlsb"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "Department of Energy M&O Small Business Subcontract Public Data Extract (FY 2017)"
                 }
             ],
+            "identifier": "MOSRC-FY2017-SPDE-01182018",
+            "issued": "2018-04-09",
             "keyword": [
                 "MOSRC",
                 "Procurement",
@@ -27799,76 +27787,60 @@
                 "small business",
                 "subcontractor"
             ],
-            "bureauCode": [
-                "019:60"
-            ],
+            "landingPage": "http://www.energy.gov/management/management-operating-subcontract-reporting-capability-mosrc",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2018-01-18",
             "programCode": [
                 "019:053"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Wind Integration National Dataset (WIND) Toolkit V2",
-            "description": "The Wind Integration National Dataset (WIND) Toolkit is an update and expansion of the Eastern and Western Wind Datasets, and is intended to support the next generation of integration studies. The WIND Toolkit includes meteorological conditions at multiple hub heights for more than 2,488,136 sites in the continental United States for the years 2007\u20132014. Collect and download, as CSV, a configurable set of data fields.",
-            "modified": "2022-11-16T20:28:34.101Z",
-            "accessLevel": "public",
-            "identifier": "WINDtoolkit_2007_2014_v2",
-            "dataQuality": true,
-            "landingPage": "https://www.nrel.gov/grid/wind-toolkit.html",
-            "rights": "true",
-            "spatial": "CONUS",
-            "temporal": "2007-01-01/2014-12-31",
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "National Renewable Energy Laboratory",
+                "name": "Office of Small and Disadvantaged Business Utilization (OSDBU)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "National Renewable Energy Laboratory"
+                    "name": "Department of Energy"
                 }
             },
+            "spatial": "United States",
+            "temporal": "2017-01-01/2017-12-31",
+            "title": "Department of Energy M&O Small Business Subcontract Public Data Extract (FY 2017)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Wind Toolkit Team",
                 "hasEmail": "mailto:WINDtoolkit@nrel.gov"
             },
+            "dataQuality": true,
+            "description": "The Wind Integration National Dataset (WIND) Toolkit is an update and expansion of the Eastern and Western Wind Datasets, and is intended to support the next generation of integration studies. The WIND Toolkit includes meteorological conditions at multiple hub heights for more than 2,488,136 sites in the continental United States for the years 2007\u20132014. Collect and download, as CSV, a configurable set of data fields.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://developer.nrel.gov/api/wind-toolkit/v2/wind/wtk-download",
-                    "title": "Wind Integration National Dataset (WIND) Toolkit",
-                    "description": "The Wind Integration National Dataset (WIND) Toolkit is an update and expansion of the Eastern and Western Wind Datasets, and is intended to support the next generation of integration studies. The WIND Toolkit includes meteorological conditions at multiple hub heights for more than 2,488,136 sites in the continental United States for the years 2007\u20132014. Collect and download, as CSV, a configurable set of data fields."
+                    "description": "The Wind Integration National Dataset (WIND) Toolkit is an update and expansion of the Eastern and Western Wind Datasets, and is intended to support the next generation of integration studies. The WIND Toolkit includes meteorological conditions at multiple hub heights for more than 2,488,136 sites in the continental United States for the years 2007\u20132014. Collect and download, as CSV, a configurable set of data fields.",
+                    "title": "Wind Integration National Dataset (WIND) Toolkit"
                 }
             ],
+            "identifier": "WINDtoolkit_2007_2014_v2",
             "keyword": [
                 "CONUS",
                 "NREL",
                 "wind energy"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.nrel.gov/grid/wind-toolkit.html",
+            "language": [
+                "en-US"
             ],
+            "modified": "2022-11-16T20:28:34.101Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Wind Integration National Dataset (WIND) Toolkit - Multi-year Annual Average - Canada",
-            "description": "This data provides modeled annual average wind speed for Southern Canada both onshore and offshore for the period 2007\u20132013.\n\nThis dataset was derived from the WIND Toolkit and may be used with the following citations:\n\nDraxl, C., B.M. Hodge, A. Clifton, and J. McCaa. 2015. Overview and Meteorological Validation of the Wind Integration National Dataset Toolkit (Technical Report, NREL/TP-5000-61740). Golden, CO: National Renewable Energy Laboratory.\n\nDraxl, C., B.M. Hodge, A. Clifton, and J. McCaa. 2015. \"The Wind Integration National Dataset (WIND) Toolkit.\" Applied Energy 151: 355366.\n\nLieberman-Cribbin, W., C. Draxl, and A. Clifton. 2014. Guide to Using the WIND Toolkit Validation Code (Technical Report, NREL/TP-5000-62595). Golden, CO: National Renewable Energy Laboratory.\n\nKing, J., A. Clifton, and B.M. Hodge. 2014. Validation of Power Output for the WIND Toolkit (Technical Report, NREL/TP-5D00-61714). Golden, CO: National Renewable Energy Laboratory.",
-            "modified": "2023-01-11T18:47:52.571Z",
-            "accessLevel": "public",
-            "identifier": "WTK_Canada_annavg",
-            "dataQuality": true,
-            "landingPage": "https://www.nrel.gov/gis/wind-resource-maps.html",
-            "rights": "true",
-            "temporal": "2007-01-01/2013-12-31",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Renewable Energy Laboratory",
@@ -27877,51 +27849,52 @@
                     "name": "National Renewable Energy Laboratory"
                 }
             },
+            "rights": "true",
+            "spatial": "CONUS",
+            "temporal": "2007-01-01/2014-12-31",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Wind Integration National Dataset (WIND) Toolkit V2"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Wind Toolkit Team",
                 "hasEmail": "mailto:WINDtoolkit@nrel.gov"
             },
+            "dataQuality": true,
+            "description": "This data provides modeled annual average wind speed for Southern Canada both onshore and offshore for the period 2007\u20132013.\n\nThis dataset was derived from the WIND Toolkit and may be used with the following citations:\n\nDraxl, C., B.M. Hodge, A. Clifton, and J. McCaa. 2015. Overview and Meteorological Validation of the Wind Integration National Dataset Toolkit (Technical Report, NREL/TP-5000-61740). Golden, CO: National Renewable Energy Laboratory.\n\nDraxl, C., B.M. Hodge, A. Clifton, and J. McCaa. 2015. \"The Wind Integration National Dataset (WIND) Toolkit.\" Applied Energy 151: 355366.\n\nLieberman-Cribbin, W., C. Draxl, and A. Clifton. 2014. Guide to Using the WIND Toolkit Validation Code (Technical Report, NREL/TP-5000-62595). Golden, CO: National Renewable Energy Laboratory.\n\nKing, J., A. Clifton, and B.M. Hodge. 2014. Validation of Power Output for the WIND Toolkit (Technical Report, NREL/TP-5D00-61714). Golden, CO: National Renewable Energy Laboratory.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "image/tiff",
-                    "title": "Wind Integration National Dataset (WIND) Toolkit - Multi-year Annual Average - Canada",
                     "description": "Draxl, C., B.M. Hodge, A. Clifton, and J. McCaa. 2015. Overview and Meteorological Validation of the Wind Integration National Dataset Toolkit (Technical Report, NREL/TP-5000-61740). Golden, CO: National Renewable Energy Laboratory.\n\nDraxl, C., B.M. Hodge, A. Clifton, and J. McCaa. 2015. \"The Wind Integration National Dataset (WIND) Toolkit.\" Applied Energy 151: 355366.\n\nLieberman-Cribbin, W., C. Draxl, and A. Clifton. 2014. Guide to Using the WIND Toolkit Validation Code (Technical Report, NREL/TP-5000-62595). Golden, CO: National Renewable Energy Laboratory.",
-                    "downloadURL": "https://www.nrel.gov/gis/assets/images/canada-wind-data.zip"
+                    "downloadURL": "https://www.nrel.gov/gis/assets/images/canada-wind-data.zip",
+                    "mediaType": "image/tiff",
+                    "title": "Wind Integration National Dataset (WIND) Toolkit - Multi-year Annual Average - Canada"
                 }
             ],
+            "identifier": "WTK_Canada_annavg",
             "keyword": [
                 "NREL",
                 "annual average",
                 "canada",
                 "wind speed"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.nrel.gov/gis/wind-resource-maps.html",
+            "language": [
+                "en-US"
             ],
+            "modified": "2023-01-11T18:47:52.571Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Wind Integration National Dataset (WIND) Toolkit - Multi-year Annual Average - Mexico",
-            "description": "This data provides modeled annual average wind speed for Mexico and surrounding areas both onshore and offshore for the period 2007\u20132013.\n\nThis dataset was derived from the WIND Toolkit and may be used with the following citations:\n\nDraxl, C., B.M. Hodge, A. Clifton, and J. McCaa. 2015. Overview and Meteorological Validation of the Wind Integration National Dataset Toolkit (Technical Report, NREL/TP-5000-61740). Golden, CO: National Renewable Energy Laboratory.\n\nDraxl, C., B.M. Hodge, A. Clifton, and J. McCaa. 2015. \"The Wind Integration National Dataset (WIND) Toolkit.\" Applied Energy 151: 355366.\n\nLieberman-Cribbin, W., C. Draxl, and A. Clifton. 2014. Guide to Using the WIND Toolkit Validation Code (Technical Report, NREL/TP-5000-62595). Golden, CO: National Renewable Energy Laboratory.\n\nKing, J., A. Clifton, and B.M. Hodge. 2014. Validation of Power Output for the WIND Toolkit (Technical Report, NREL/TP-5D00-61714). Golden, CO: National Renewable Energy Laboratory.",
-            "modified": "2023-01-11T18:36:50.274Z",
-            "accessLevel": "public",
-            "identifier": "WTK_Mexico_annavg",
-            "dataQuality": true,
-            "landingPage": "https://www.nrel.gov/gis/wind-resource-maps.html",
-            "rights": "true",
-            "temporal": "2007-01-01/2013-12-21",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Renewable Energy Laboratory",
@@ -27930,21 +27903,37 @@
                     "name": "National Renewable Energy Laboratory"
                 }
             },
+            "rights": "true",
+            "temporal": "2007-01-01/2013-12-31",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Wind Integration National Dataset (WIND) Toolkit - Multi-year Annual Average - Canada"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Wind Toolkit Team",
                 "hasEmail": "mailto:WINDtoolkit@nrel.gov"
             },
+            "dataQuality": true,
+            "description": "This data provides modeled annual average wind speed for Mexico and surrounding areas both onshore and offshore for the period 2007\u20132013.\n\nThis dataset was derived from the WIND Toolkit and may be used with the following citations:\n\nDraxl, C., B.M. Hodge, A. Clifton, and J. McCaa. 2015. Overview and Meteorological Validation of the Wind Integration National Dataset Toolkit (Technical Report, NREL/TP-5000-61740). Golden, CO: National Renewable Energy Laboratory.\n\nDraxl, C., B.M. Hodge, A. Clifton, and J. McCaa. 2015. \"The Wind Integration National Dataset (WIND) Toolkit.\" Applied Energy 151: 355366.\n\nLieberman-Cribbin, W., C. Draxl, and A. Clifton. 2014. Guide to Using the WIND Toolkit Validation Code (Technical Report, NREL/TP-5000-62595). Golden, CO: National Renewable Energy Laboratory.\n\nKing, J., A. Clifton, and B.M. Hodge. 2014. Validation of Power Output for the WIND Toolkit (Technical Report, NREL/TP-5D00-61714). Golden, CO: National Renewable Energy Laboratory.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "image/tiff",
-                    "title": "Wind Integration National Dataset (WIND) Toolkit - Multi-year Annual Average - Mexico",
                     "description": "This data provides modeled annual average wind speed for Mexico and surrounding areas both onshore and offshore for the period 2007\u20132013.\n\nThis dataset was derived from the WIND Toolkit and may be used with the following citations:\n\nDraxl, C., B.M. Hodge, A. Clifton, and J. McCaa. 2015. Overview and Meteorological Validation of the Wind Integration National Dataset Toolkit (Technical Report, NREL/TP-5000-61740). Golden, CO: National Renewable Energy Laboratory.\n\nDraxl, C., B.M. Hodge, A. Clifton, and J. McCaa. 2015. \"The Wind Integration National Dataset (WIND) Toolkit.\" Applied Energy 151: 355366.\n\nLieberman-Cribbin, W., C. Draxl, and A. Clifton. 2014. Guide to Using the WIND Toolkit Validation Code (Technical Report, NREL/TP-5000-62595). Golden, CO: National Renewable Energy Laboratory.\n\nKing, J., A. Clifton, and B.M. Hodge. 2014. Validation of Power Output for the WIND Toolkit (Technical Report, NREL/TP-5D00-61714). Golden, CO: National Renewable Energy Laboratory.",
-                    "downloadURL": "https://www.nrel.gov/gis/assets/images/mexico-wind-data.zip"
+                    "downloadURL": "https://www.nrel.gov/gis/assets/images/mexico-wind-data.zip",
+                    "mediaType": "image/tiff",
+                    "title": "Wind Integration National Dataset (WIND) Toolkit - Multi-year Annual Average - Mexico"
                 }
             ],
+            "identifier": "WTK_Mexico_annavg",
             "keyword": [
                 "NREL",
                 "annual average",
@@ -27952,83 +27941,67 @@
                 "mexico",
                 "wind speed"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.nrel.gov/gis/wind-resource-maps.html",
+            "language": [
+                "en-US"
             ],
+            "modified": "2023-01-11T18:36:50.274Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Wind Integration National Dataset (WIND) Toolkit - Multi-year Annual Average - United States",
-            "description": "This data provides modeled annual average wind speed for the contiguous United States both onshore and offshore for the period 2007\u20132013.\n\nThis dataset was derived from the WIND Toolkit and may be used with the following citations:\n\nDraxl, C., B.M. Hodge, A. Clifton, and J. McCaa. 2015. Overview and Meteorological Validation of the Wind Integration National Dataset Toolkit (Technical Report, NREL/TP-5000-61740). Golden, CO: National Renewable Energy Laboratory.\n\nDraxl, C., B.M. Hodge, A. Clifton, and J. McCaa. 2015. \"The Wind Integration National Dataset (WIND) Toolkit.\" Applied Energy 151: 355366.\n\nLieberman-Cribbin, W., C. Draxl, and A. Clifton. 2014. Guide to Using the WIND Toolkit Validation Code (Technical Report, NREL/TP-5000-62595). Golden, CO: National Renewable Energy Laboratory.\n\nKing, J., A. Clifton, and B.M. Hodge. 2014. Validation of Power Output for the WIND Toolkit (Technical Report, NREL/TP-5D00-61714). Golden, CO: National Renewable Energy Laboratory.",
-            "modified": "2023-01-11T18:51:50.693Z",
-            "accessLevel": "public",
-            "identifier": "WTK_US_annavg",
-            "dataQuality": true,
-            "landingPage": "https://www.nrel.gov/gis/wind-resource-maps.html",
-            "rights": "true",
-            "temporal": "2007-01-01/2013-12-31",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Renewable Energy Laboratory",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Department of Energy"
+                    "name": "National Renewable Energy Laboratory"
                 }
             },
+            "rights": "true",
+            "temporal": "2007-01-01/2013-12-21",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Wind Integration National Dataset (WIND) Toolkit - Multi-year Annual Average - Mexico"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Wind Toolkit Team",
                 "hasEmail": "mailto:WINDtoolkit@nrel.gov"
             },
+            "dataQuality": true,
+            "description": "This data provides modeled annual average wind speed for the contiguous United States both onshore and offshore for the period 2007\u20132013.\n\nThis dataset was derived from the WIND Toolkit and may be used with the following citations:\n\nDraxl, C., B.M. Hodge, A. Clifton, and J. McCaa. 2015. Overview and Meteorological Validation of the Wind Integration National Dataset Toolkit (Technical Report, NREL/TP-5000-61740). Golden, CO: National Renewable Energy Laboratory.\n\nDraxl, C., B.M. Hodge, A. Clifton, and J. McCaa. 2015. \"The Wind Integration National Dataset (WIND) Toolkit.\" Applied Energy 151: 355366.\n\nLieberman-Cribbin, W., C. Draxl, and A. Clifton. 2014. Guide to Using the WIND Toolkit Validation Code (Technical Report, NREL/TP-5000-62595). Golden, CO: National Renewable Energy Laboratory.\n\nKing, J., A. Clifton, and B.M. Hodge. 2014. Validation of Power Output for the WIND Toolkit (Technical Report, NREL/TP-5D00-61714). Golden, CO: National Renewable Energy Laboratory.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "image/tiff",
-                    "title": "Wind Integration National Dataset (WIND) Toolkit - Multi-year Annual Average - United States",
                     "description": "This data provides modeled annual average wind speed for the contiguous United States both onshore and offshore for the period 2007\u20132013.\n\nThis dataset was derived from the WIND Toolkit and may be used with the following citations:\n\nDraxl, C., B.M. Hodge, A. Clifton, and J. McCaa. 2015. Overview and Meteorological Validation of the Wind Integration National Dataset Toolkit (Technical Report, NREL/TP-5000-61740). Golden, CO: National Renewable Energy Laboratory.\n\nDraxl, C., B.M. Hodge, A. Clifton, and J. McCaa. 2015. \"The Wind Integration National Dataset (WIND) Toolkit.\" Applied Energy 151: 355366.\n\nLieberman-Cribbin, W., C. Draxl, and A. Clifton. 2014. Guide to Using the WIND Toolkit Validation Code (Technical Report, NREL/TP-5000-62595). Golden, CO: National Renewable Energy Laboratory.\n\nKing, J., A. Clifton, and B.M. Hodge. 2014. Validation of Power Output for the WIND Toolkit (Technical Report, NREL/TP-5D00-61714). Golden, CO: National Renewable Energy Laboratory.",
-                    "downloadURL": "https://www.nrel.gov/gis/assets/images/us-wind-data.zip"
+                    "downloadURL": "https://www.nrel.gov/gis/assets/images/us-wind-data.zip",
+                    "mediaType": "image/tiff",
+                    "title": "Wind Integration National Dataset (WIND) Toolkit - Multi-year Annual Average - United States"
                 }
             ],
+            "identifier": "WTK_US_annavg",
             "keyword": [
                 "CONUS",
                 "NREL",
                 "annual average",
                 "wind speed"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.nrel.gov/gis/wind-resource-maps.html",
+            "language": [
+                "en-US"
             ],
+            "modified": "2023-01-11T18:51:50.693Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "U.S. Biomethane Resources by County",
-            "description": "This dataset contains 2014 estimates of the methane generation potential by county from the following biogas sources: landfills, animal manure; wastewater treatment; and industrial, institutional, and commercial organic waste (IIC).",
-            "modified": "2023-01-11T18:59:28.378Z",
-            "accessLevel": "public",
-            "identifier": "Biogas_methane_2014",
-            "dataQuality": true,
-            "landingPage": "https://www.nrel.gov/gis/biomass.html",
-            "rights": "true",
-            "temporal": "2014-01-01/2014-12-31",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Renewable Energy Laboratory",
@@ -28037,51 +28010,51 @@
                     "name": "Department of Energy"
                 }
             },
+            "rights": "true",
+            "temporal": "2007-01-01/2013-12-31",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Wind Integration National Dataset (WIND) Toolkit - Multi-year Annual Average - United States"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Anelia Milbrandt",
                 "hasEmail": "mailto:Anelia.Milbrandt@nrel.gov"
             },
+            "dataQuality": true,
+            "description": "This dataset contains 2014 estimates of the methane generation potential by county from the following biogas sources: landfills, animal manure; wastewater treatment; and industrial, institutional, and commercial organic waste (IIC).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/octet-stream",
-                    "title": "U.S. Biomethane Resources by County",
                     "description": "This dataset contains 2014 estimates of the methane generation potential by county from the following biogas sources: landfills, animal manure; wastewater treatment; and industrial, institutional, and commercial organic waste (IIC).",
-                    "downloadURL": "https://www.nrel.gov/gis/assets/data/biomethane.zip"
+                    "downloadURL": "https://www.nrel.gov/gis/assets/data/biomethane.zip",
+                    "mediaType": "application/octet-stream",
+                    "title": "U.S. Biomethane Resources by County"
                 }
             ],
+            "identifier": "Biogas_methane_2014",
             "keyword": [
                 "Methane",
                 "NREL",
                 "biogas",
                 "u.s."
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.nrel.gov/gis/biomass.html",
+            "language": [
+                "en-US"
             ],
+            "modified": "2023-01-11T18:59:28.378Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "U.S. Solid Biomass Resources by County - Solid",
-            "description": "This dataset contains information about the biomass resources generated by county in the United States for 2014. It includes the following feedstock categories: crop residues, forest residues, primary mill residues, secondary mill residues, and urban wood waste.",
-            "modified": "2023-01-11T19:04:30.779Z",
-            "accessLevel": "public",
-            "identifier": "Biomass_solid_2014",
-            "dataQuality": true,
-            "landingPage": "https://www.nrel.gov/gis/biomass.html",
-            "rights": "true",
-            "temporal": "2014-01-01/2014-12-31",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Renewable Energy Laboratory",
@@ -28090,50 +28063,50 @@
                     "name": "Department of Energy"
                 }
             },
+            "rights": "true",
+            "temporal": "2014-01-01/2014-12-31",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "U.S. Biomethane Resources by County"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Anelia Milbrandt",
                 "hasEmail": "mailto:Anelia.Milbrandt@nrel.gov"
             },
+            "dataQuality": true,
+            "description": "This dataset contains information about the biomass resources generated by county in the United States for 2014. It includes the following feedstock categories: crop residues, forest residues, primary mill residues, secondary mill residues, and urban wood waste.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/octet-stream",
-                    "title": "U.S. Solid Biomass Resources by County - Solid",
                     "description": "This dataset contains information about the biomass resources generated by county in the United States for 2014. It includes the following feedstock categories: crop residues, forest residues, primary mill residues, secondary mill residues, and urban wood waste.",
-                    "downloadURL": "https://www.nrel.gov/gis/assets/data/solid-biomass.zip"
+                    "downloadURL": "https://www.nrel.gov/gis/assets/data/solid-biomass.zip",
+                    "mediaType": "application/octet-stream",
+                    "title": "U.S. Solid Biomass Resources by County - Solid"
                 }
             ],
+            "identifier": "Biomass_solid_2014",
             "keyword": [
                 "NREL",
                 "solid biomass",
                 "u.s."
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.nrel.gov/gis/biomass.html",
+            "language": [
+                "en-US"
             ],
+            "modified": "2023-01-11T19:04:30.779Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Developing Geothermal Plants",
-            "description": "This dataset contains locations of geothermal power plants in development within the United States as of the publication date and includes attributes for planned capacity. Geothermal developing plant data was aggregated from SNL Financial LC, the Geothermal Energy Association (GEA), press releases, operator websites and geothermal lease data. NREL performed independent research to validate locations of geothermal projects under development as of July 2014.",
-            "modified": "2023-01-11T20:00:50.789Z",
-            "accessLevel": "public",
-            "identifier": "dev_geo_plants_2014",
-            "dataQuality": true,
-            "landingPage": "https://www.nrel.gov/gis/geothermal.html",
-            "rights": "true",
-            "temporal": "2014-01-01/2014-12-31",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Renewable Energy Laboratory",
@@ -28142,51 +28115,51 @@
                     "name": "Department of Energy"
                 }
             },
+            "rights": "true",
+            "temporal": "2014-01-01/2014-12-31",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "U.S. Solid Biomass Resources by County - Solid"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NREL GDS",
                 "hasEmail": "mailto:GDS@nrel.gov"
             },
+            "dataQuality": true,
+            "description": "This dataset contains locations of geothermal power plants in development within the United States as of the publication date and includes attributes for planned capacity. Geothermal developing plant data was aggregated from SNL Financial LC, the Geothermal Energy Association (GEA), press releases, operator websites and geothermal lease data. NREL performed independent research to validate locations of geothermal projects under development as of July 2014.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/octet-stream",
-                    "title": "Developing Geothermal Plants",
                     "description": "This dataset contains locations of geothermal power plants in development within the United States as of the publication date and includes attributes for planned capacity. Geothermal developing plant data was aggregated from SNL Financial LC, the Geothermal Energy Association (GEA), press releases, operator websites and geothermal lease data. NREL performed independent research to validate locations of geothermal projects under development as of July 2014.",
-                    "downloadURL": "https://www.nrel.gov/gis/assets/data/developing-geothermal-plants.zip"
+                    "downloadURL": "https://www.nrel.gov/gis/assets/data/developing-geothermal-plants.zip",
+                    "mediaType": "application/octet-stream",
+                    "title": "Developing Geothermal Plants"
                 }
             ],
+            "identifier": "dev_geo_plants_2014",
             "keyword": [
                 "NREL",
                 "geothermal",
                 "power plants",
                 "u.s."
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.nrel.gov/gis/geothermal.html",
+            "language": [
+                "en-US"
             ],
+            "modified": "2023-01-11T20:00:50.789Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Relative Favorability of Deep Enhanced Geothermal Systems",
-            "description": "This dataset shows the relative favorability of deep Enhanced Geothermal Systems (EGS) in the contiguous United States based on levelized cost of electricity estimated from adequate temperature and depth combinations.",
-            "modified": "2023-01-11T20:04:18.897Z",
-            "accessLevel": "public",
-            "identifier": "deep_egs_geothermal",
-            "dataQuality": true,
-            "landingPage": "https://www.nrel.gov/gis/geothermal.html",
-            "rights": "true",
-            "temporal": "2009-01-01/2009-12-31",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Renewable Energy Laboratory",
@@ -28195,51 +28168,51 @@
                     "name": "Department of Energy"
                 }
             },
+            "rights": "true",
+            "temporal": "2014-01-01/2014-12-31",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Developing Geothermal Plants"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NREL GDS",
                 "hasEmail": "mailto:GDS@nrel.gov"
             },
+            "dataQuality": true,
+            "description": "This dataset shows the relative favorability of deep Enhanced Geothermal Systems (EGS) in the contiguous United States based on levelized cost of electricity estimated from adequate temperature and depth combinations.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/octet-stream",
-                    "title": "Relative Favorability of Deep Enhanced Geothermal Systems",
                     "description": "This dataset shows the relative favorability of deep Enhanced Geothermal Systems (EGS) in the contiguous United States based on levelized cost of electricity estimated from adequate temperature and depth combinations.",
-                    "downloadURL": "https://www.nrel.gov/gis/assets/data/egs.zip"
+                    "downloadURL": "https://www.nrel.gov/gis/assets/data/egs.zip",
+                    "mediaType": "application/octet-stream",
+                    "title": "Relative Favorability of Deep Enhanced Geothermal Systems"
                 }
             ],
+            "identifier": "deep_egs_geothermal",
             "keyword": [
                 "CONUS",
                 "EGS",
                 "NREL",
-                "geothermal"
-            ],
-            "bureauCode": [
-                "015:11"
-            ],
-            "programCode": [
-                "015:001"
+                "geothermal"
             ],
+            "landingPage": "https://www.nrel.gov/gis/geothermal.html",
             "language": [
                 "en-US"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Hydrogen Potential from Renewable Energy Resources (2007)",
-            "description": "This study was conducted in 2007 to estimate the potential for producing hydrogen from key renewable resources (onshore wind, solar photovoltaic, and biomass) by county in the United States and to create maps that allow the reader to easily visualize the results. To accomplish this objective, the authors analyzed renewable resource data both statistically and graphically utilizing a state-of-the-art Geographic Information System (GIS), a computer-based information system used to create and visualize geographic information. Land-use and environmental exclusions were applied to represent the most viable resources across the country. While wind, solar, and biomass are considered major renewable resources, other renewable energy resources could also be used for hydrogen production, thus contributing to hydrogen development locally and regionally. These additional resources include offshore wind, concentrating solar power, geothermal, hydropower, photoelectrochemical, and photobiological resources. This study found that approximately 1 billion metric tons of hydrogen could be produced annually from wind, solar, and biomass resources in the United States. The greatest potential for producing hydrogen from these key renewable resources is in the Great Plains region. In addition, this research suggests that renewable hydrogen has the potential to displace gasoline consumption in most states if and when a number of technical and scientific barriers can be overcome.",
-            "modified": "2023-01-11T20:07:25.181Z",
-            "accessLevel": "public",
-            "identifier": "hydrogen_re_source",
-            "dataQuality": true,
-            "landingPage": "https://www.nrel.gov/gis/hydrogen.html",
-            "rights": "true",
-            "temporal": "2007-01-01/2007-12-31",
+            "modified": "2023-01-11T20:04:18.897Z",
+            "programCode": [
+                "015:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Renewable Energy Laboratory",
@@ -28248,51 +28221,51 @@
                     "name": "Department of Energy"
                 }
             },
+            "rights": "true",
+            "temporal": "2009-01-01/2009-12-31",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Relative Favorability of Deep Enhanced Geothermal Systems"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NREL GDS",
                 "hasEmail": "mailto:GDS@nrel.gov"
             },
+            "dataQuality": true,
+            "description": "This study was conducted in 2007 to estimate the potential for producing hydrogen from key renewable resources (onshore wind, solar photovoltaic, and biomass) by county in the United States and to create maps that allow the reader to easily visualize the results. To accomplish this objective, the authors analyzed renewable resource data both statistically and graphically utilizing a state-of-the-art Geographic Information System (GIS), a computer-based information system used to create and visualize geographic information. Land-use and environmental exclusions were applied to represent the most viable resources across the country. While wind, solar, and biomass are considered major renewable resources, other renewable energy resources could also be used for hydrogen production, thus contributing to hydrogen development locally and regionally. These additional resources include offshore wind, concentrating solar power, geothermal, hydropower, photoelectrochemical, and photobiological resources. This study found that approximately 1 billion metric tons of hydrogen could be produced annually from wind, solar, and biomass resources in the United States. The greatest potential for producing hydrogen from these key renewable resources is in the Great Plains region. In addition, this research suggests that renewable hydrogen has the potential to displace gasoline consumption in most states if and when a number of technical and scientific barriers can be overcome.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/octet-stream",
-                    "title": "Hydrogen Potential from Renewable Energy Resources (2007)",
                     "description": "This study was conducted in 2007 to estimate the potential for producing hydrogen from key renewable resources (onshore wind, solar photovoltaic, and biomass) by county in the United States and to create maps that allow the reader to easily visualize the results. To accomplish this objective, the authors analyzed renewable resource data both statistically and graphically utilizing a state-of-the-art Geographic Information System (GIS), a computer-based information system used to create and visualize geographic information. Land-use and environmental exclusions were applied to represent the most viable resources across the country. While wind, solar, and biomass are considered major renewable resources, other renewable energy resources could also be used for hydrogen production, thus contributing to hydrogen development locally and regionally. These additional resources include offshore wind, concentrating solar power, geothermal, hydropower, photoelectrochemical, and photobiological resources. This study found that approximately 1 billion metric tons of hydrogen could be produced annually from wind, solar, and biomass resources in the United States. The greatest potential for producing hydrogen from these key renewable resources is in the Great Plains region. In addition, this research suggests that renewable hydrogen has the potential to displace gasoline consumption in most states if and when a number of technical and scientific barriers can be overcome.",
-                    "downloadURL": "https://www.nrel.gov/gis/assets/data/hydrogen.zip"
+                    "downloadURL": "https://www.nrel.gov/gis/assets/data/hydrogen.zip",
+                    "mediaType": "application/octet-stream",
+                    "title": "Hydrogen Potential from Renewable Energy Resources (2007)"
                 }
             ],
+            "identifier": "hydrogen_re_source",
             "keyword": [
                 "NREL",
                 "hydrogen",
                 "renewable energy",
                 "u.s."
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.nrel.gov/gis/hydrogen.html",
+            "language": [
+                "en-US"
             ],
+            "modified": "2023-01-11T20:07:25.181Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Operating Geothermal Plants",
-            "description": "This dataset contains locations of operating geothermal power plants within the United States as of the publication date. Geothermal power plant data was aggregated from SNL Financial LC, the Geothermal Energy Association (GEA), press releases and operator websites. NREL performed independent research to validate locations of geothermal plants based on aerial satellite imagery as of July 2014.",
-            "modified": "2023-01-11T20:10:29.241Z",
-            "accessLevel": "public",
-            "identifier": "op_geo_plants_2014",
-            "dataQuality": true,
-            "landingPage": "https://www.nrel.gov/gis/geothermal.html",
-            "rights": "true",
-            "temporal": "2014-01-01/2014-12-31",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Renewable Energy Laboratory",
@@ -28301,104 +28274,105 @@
                     "name": "Department of Energy"
                 }
             },
+            "rights": "true",
+            "temporal": "2007-01-01/2007-12-31",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Hydrogen Potential from Renewable Energy Resources (2007)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NREL GDS",
                 "hasEmail": "mailto:GDS@nrel.gov"
             },
+            "dataQuality": true,
+            "description": "This dataset contains locations of operating geothermal power plants within the United States as of the publication date. Geothermal power plant data was aggregated from SNL Financial LC, the Geothermal Energy Association (GEA), press releases and operator websites. NREL performed independent research to validate locations of geothermal plants based on aerial satellite imagery as of July 2014.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/octet-stream",
-                    "title": "Operating Geothermal Plants",
                     "description": "This dataset contains locations of operating geothermal power plants within the United States as of the publication date. Geothermal power plant data was aggregated from SNL Financial LC, the Geothermal Energy Association (GEA), press releases and operator websites. NREL performed independent research to validate locations of geothermal plants based on aerial satellite imagery as of July 2014.",
-                    "downloadURL": "https://www.nrel.gov/gis/assets/data/operating-geothermal-plants.zip"
+                    "downloadURL": "https://www.nrel.gov/gis/assets/data/operating-geothermal-plants.zip",
+                    "mediaType": "application/octet-stream",
+                    "title": "Operating Geothermal Plants"
                 }
             ],
+            "identifier": "op_geo_plants_2014",
             "keyword": [
                 "NREL",
                 "geothermal",
                 "power plants",
                 "u.s."
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.nrel.gov/gis/geothermal.html",
+            "language": [
+                "en-US"
             ],
+            "modified": "2023-01-11T20:10:29.241Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Wave Depth",
-            "description": "The project estimated the naturally available and technically recoverable U.S. wave energy resources, using a 51-month Wavewatch III hindcast database developed especially for this study by National Oceanographic and Atmospheric Administration's (NOAA's) National Centers for Environmental Prediction. For total resource estimation, wave power density in terms of kilowatts per meter is aggregated across a unit diameter circle. This approach is fully consistent with accepted global practice and includes the resource made available by the lateral transfer of wave energy along wave crests, which enables densities within a few kilometers of a linear array, even for fixed terminator devices.",
-            "modified": "2024-08-14T13:39:42.626Z",
-            "accessLevel": "public",
-            "identifier": "wave_depth",
-            "dataQuality": true,
-            "issued": "0014-07-30",
-            "landingPage": "https://www.nrel.gov/gis/maps-marine.html",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Renewable Energy Laboratory",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "National Renewable Energy Laboratory"
+                    "name": "Department of Energy"
                 }
             },
+            "rights": "true",
+            "temporal": "2014-01-01/2014-12-31",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Operating Geothermal Plants"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NREL GDS",
                 "hasEmail": "mailto:GDS@nrel.gov"
             },
+            "dataQuality": true,
+            "description": "The project estimated the naturally available and technically recoverable U.S. wave energy resources, using a 51-month Wavewatch III hindcast database developed especially for this study by National Oceanographic and Atmospheric Administration's (NOAA's) National Centers for Environmental Prediction. For total resource estimation, wave power density in terms of kilowatts per meter is aggregated across a unit diameter circle. This approach is fully consistent with accepted global practice and includes the resource made available by the lateral transfer of wave energy along wave crests, which enables densities within a few kilometers of a linear array, even for fixed terminator devices.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/octet-stream",
-                    "title": "Wave Depth",
                     "description": "The project estimated the naturally available and technically recoverable U.S. wave energy resources, using a 51-month Wavewatch III hindcast database developed especially for this study by National Oceanographic and Atmospheric Administration's (NOAA's) National Centers for Environmental Prediction. For total resource estimation, wave power density in terms of kilowatts per meter is aggregated across a unit diameter circle. This approach is fully consistent with accepted global practice and includes the resource made available by the lateral transfer of wave energy along wave crests, which enables densities within a few kilometers of a linear array, even for fixed terminator devices.",
-                    "downloadURL": "https://www.nrel.gov/gis/assets/data/wave_depth.zip"
+                    "downloadURL": "https://www.nrel.gov/gis/assets/data/wave_depth.zip",
+                    "mediaType": "application/octet-stream",
+                    "title": "Wave Depth"
                 }
             ],
+            "identifier": "wave_depth",
+            "issued": "0014-07-30",
             "keyword": [
                 "EPRI",
                 "NREL",
                 "u.s.",
                 "wave depth"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.nrel.gov/gis/maps-marine.html",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-08-14T13:39:42.626Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Wave Energy Period",
-            "description": "The project estimated the naturally available and technically recoverable U.S. wave energy resources, using a 51-month Wavewatch III hindcast database developed especially for this study by National Oceanographic and Atmospheric Administration's (NOAA's) National Centers for Environmental Prediction. For total resource estimation, wave power density in terms of kilowatts per meter is aggregated across a unit diameter circle. This approach is fully consistent with accepted global practice and includes the resource made available by the lateral transfer of wave energy along wave crests, which enables densities within a few kilometers of a linear array, even for fixed terminator devices.",
-            "modified": "2024-08-14T13:37:17.435Z",
-            "accessLevel": "public",
-            "identifier": "wave_energy_period",
-            "dataQuality": true,
-            "issued": "2014-07-30",
-            "landingPage": "https://www.nrel.gov/gis/maps-marine.html",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Renewable Energy Laboratory",
@@ -28407,51 +28381,51 @@
                     "name": "National Renewable Energy Laboratory"
                 }
             },
+            "rights": "true",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Wave Depth"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NREL GDS",
                 "hasEmail": "mailto:GDS@nrel.gov"
             },
+            "dataQuality": true,
+            "description": "The project estimated the naturally available and technically recoverable U.S. wave energy resources, using a 51-month Wavewatch III hindcast database developed especially for this study by National Oceanographic and Atmospheric Administration's (NOAA's) National Centers for Environmental Prediction. For total resource estimation, wave power density in terms of kilowatts per meter is aggregated across a unit diameter circle. This approach is fully consistent with accepted global practice and includes the resource made available by the lateral transfer of wave energy along wave crests, which enables densities within a few kilometers of a linear array, even for fixed terminator devices.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/octet-stream",
-                    "title": "Wave Energy Period",
                     "description": "The project estimated the naturally available and technically recoverable U.S. wave energy resources, using a 51-month Wavewatch III hindcast database developed especially for this study by National Oceanographic and Atmospheric Administration's (NOAA's) National Centers for Environmental Prediction. For total resource estimation, wave power density in terms of kilowatts per meter is aggregated across a unit diameter circle. This approach is fully consistent with accepted global practice and includes the resource made available by the lateral transfer of wave energy along wave crests, which enables densities within a few kilometers of a linear array, even for fixed terminator devices.",
-                    "downloadURL": "https://www.nrel.gov/gis/assets/data/wave_energy_period.zip"
+                    "downloadURL": "https://www.nrel.gov/gis/assets/data/wave_energy_period.zip",
+                    "mediaType": "application/octet-stream",
+                    "title": "Wave Energy Period"
                 }
             ],
+            "identifier": "wave_energy_period",
+            "issued": "2014-07-30",
             "keyword": [
                 "EPRI",
                 "NREL",
                 "u.s.",
                 "wave energy period"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.nrel.gov/gis/maps-marine.html",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-08-14T13:37:17.435Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Wave Significant Height",
-            "description": "The project estimated the naturally available and technically recoverable U.S. wave energy resources, using a 51-month Wavewatch III hindcast database developed especially for this study by National Oceanographic and Atmospheric Administration's (NOAA's) National Centers for Environmental Prediction. For total resource estimation, wave power density in terms of kilowatts per meter is aggregated across a unit diameter circle. This approach is fully consistent with accepted global practice and includes the resource made available by the lateral transfer of wave energy along wave crests, which enables densities within a few kilometers of a linear array, even for fixed terminator devices.",
-            "modified": "2024-08-14T13:44:54.402Z",
-            "accessLevel": "public",
-            "identifier": "wave_signif_ht",
-            "dataQuality": true,
-            "issued": "2014-07-30",
-            "landingPage": "https://www.nrel.gov/gis/maps-marine.html",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Renewable Energy Laboratory",
@@ -28460,51 +28434,51 @@
                     "name": "National Renewable Energy Laboratory"
                 }
             },
+            "rights": "true",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Wave Energy Period"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NREL GDS",
                 "hasEmail": "mailto:GDS@nrel.gov"
             },
+            "dataQuality": true,
+            "description": "The project estimated the naturally available and technically recoverable U.S. wave energy resources, using a 51-month Wavewatch III hindcast database developed especially for this study by National Oceanographic and Atmospheric Administration's (NOAA's) National Centers for Environmental Prediction. For total resource estimation, wave power density in terms of kilowatts per meter is aggregated across a unit diameter circle. This approach is fully consistent with accepted global practice and includes the resource made available by the lateral transfer of wave energy along wave crests, which enables densities within a few kilometers of a linear array, even for fixed terminator devices.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/octet-stream",
-                    "title": "Wave Significant Height",
                     "description": "The project estimated the naturally available and technically recoverable U.S. wave energy resources, using a 51-month Wavewatch III hindcast database developed especially for this study by National Oceanographic and Atmospheric Administration's (NOAA's) National Centers for Environmental Prediction. For total resource estimation, wave power density in terms of kilowatts per meter is aggregated across a unit diameter circle. This approach is fully consistent with accepted global practice and includes the resource made available by the lateral transfer of wave energy along wave crests, which enables densities within a few kilometers of a linear array, even for fixed terminator devices.",
-                    "downloadURL": "https://www.nrel.gov/gis/assets/data/wave_significant_height.zip"
+                    "downloadURL": "https://www.nrel.gov/gis/assets/data/wave_significant_height.zip",
+                    "mediaType": "application/octet-stream",
+                    "title": "Wave Significant Height"
                 }
             ],
+            "identifier": "wave_signif_ht",
+            "issued": "2014-07-30",
             "keyword": [
                 "EPRI",
                 "NREL",
                 "u.s.",
                 "wave hindcast"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.nrel.gov/gis/maps-marine.html",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-08-14T13:44:54.402Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Wave Hindcast",
-            "description": "The project estimated the naturally available and technically recoverable U.S. wave energy resources, using a 51-month Wavewatch III hindcast database developed especially for this study by National Oceanographic and Atmospheric Administration's (NOAA's) National Centers for Environmental Prediction. For total resource estimation, wave power density in terms of kilowatts per meter is aggregated across a unit diameter circle. This approach is fully consistent with accepted global practice and includes the resource made available by the lateral transfer of wave energy along wave crests, which enables densities within a few kilometers of a linear array, even for fixed terminator devices.",
-            "modified": "2024-08-14T13:38:00.406Z",
-            "accessLevel": "public",
-            "identifier": "wave_hindcast",
-            "dataQuality": true,
-            "issued": "2014-07-30",
-            "landingPage": "https://www.nrel.gov/gis/maps-marine.html",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Renewable Energy Laboratory",
@@ -28513,51 +28487,51 @@
                     "name": "National Renewable Energy Laboratory"
                 }
             },
+            "rights": "true",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Wave Significant Height"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NREL GDS",
                 "hasEmail": "mailto:GDS@nrel.gov"
             },
+            "dataQuality": true,
+            "description": "The project estimated the naturally available and technically recoverable U.S. wave energy resources, using a 51-month Wavewatch III hindcast database developed especially for this study by National Oceanographic and Atmospheric Administration's (NOAA's) National Centers for Environmental Prediction. For total resource estimation, wave power density in terms of kilowatts per meter is aggregated across a unit diameter circle. This approach is fully consistent with accepted global practice and includes the resource made available by the lateral transfer of wave energy along wave crests, which enables densities within a few kilometers of a linear array, even for fixed terminator devices.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/octet-stream",
-                    "title": "Wave Hindcast",
                     "description": "The project estimated the naturally available and technically recoverable U.S. wave energy resources, using a 51-month Wavewatch III hindcast database developed especially for this study by National Oceanographic and Atmospheric Administration's (NOAA's) National Centers for Environmental Prediction. For total resource estimation, wave power density in terms of kilowatts per meter is aggregated across a unit diameter circle. This approach is fully consistent with accepted global practice and includes the resource made available by the lateral transfer of wave energy along wave crests, which enables densities within a few kilometers of a linear array, even for fixed terminator devices.",
-                    "downloadURL": "https://www.nrel.gov/gis/assets/data/wave_hindcast_direction.zip"
+                    "downloadURL": "https://www.nrel.gov/gis/assets/data/wave_hindcast_direction.zip",
+                    "mediaType": "application/octet-stream",
+                    "title": "Wave Hindcast"
                 }
             ],
+            "identifier": "wave_hindcast",
+            "issued": "2014-07-30",
             "keyword": [
                 "NREL",
                 "EPRI",
                 "u.s.",
                 "wave hindcast"
             ],
-            "bureauCode": [
-                "015:11"
-            ],
-            "programCode": [
-                "015:001"
-            ],
+            "landingPage": "https://www.nrel.gov/gis/maps-marine.html",
             "language": [
                 "en-US"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Wave Power Density",
-            "description": "The project estimated the naturally available and technically recoverable U.S. wave energy resources, using a 51-month Wavewatch III hindcast database developed especially for this study by National Oceanographic and Atmospheric Administration's (NOAA's) National Centers for Environmental Prediction. For total resource estimation, wave power density in terms of kilowatts per meter is aggregated across a unit diameter circle. This approach is fully consistent with accepted global practice and includes the resource made available by the lateral transfer of wave energy along wave crests, which enables densities within a few kilometers of a linear array, even for fixed terminator devices.",
-            "modified": "2024-08-14T13:38:51.583Z",
-            "accessLevel": "public",
-            "identifier": "wave_power_density",
-            "dataQuality": true,
-            "issued": "2014-07-30",
-            "landingPage": "https://www.nrel.gov/gis/maps-marine.html",
-            "rights": "true",
+            "modified": "2024-08-14T13:38:00.406Z",
+            "programCode": [
+                "015:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Renewable Energy Laboratory",
@@ -28566,102 +28540,101 @@
                     "name": "National Renewable Energy Laboratory"
                 }
             },
+            "rights": "true",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Wave Hindcast"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NREL GDS",
                 "hasEmail": "mailto:GDS@nrel.gov"
             },
+            "dataQuality": true,
+            "description": "The project estimated the naturally available and technically recoverable U.S. wave energy resources, using a 51-month Wavewatch III hindcast database developed especially for this study by National Oceanographic and Atmospheric Administration's (NOAA's) National Centers for Environmental Prediction. For total resource estimation, wave power density in terms of kilowatts per meter is aggregated across a unit diameter circle. This approach is fully consistent with accepted global practice and includes the resource made available by the lateral transfer of wave energy along wave crests, which enables densities within a few kilometers of a linear array, even for fixed terminator devices.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/octet-stream",
-                    "title": "Wave Power Density",
                     "description": "The project estimated the naturally available and technically recoverable U.S. wave energy resources, using a 51-month Wavewatch III hindcast database developed especially for this study by National Oceanographic and Atmospheric Administration's (NOAA's) National Centers for Environmental Prediction. For total resource estimation, wave power density in terms of kilowatts per meter is aggregated across a unit diameter circle. This approach is fully consistent with accepted global practice and includes the resource made available by the lateral transfer of wave energy along wave crests, which enables densities within a few kilometers of a linear array, even for fixed terminator devices.",
-                    "downloadURL": "https://www.nrel.gov/gis/assets/data/wave_power_density.zip"
+                    "downloadURL": "https://www.nrel.gov/gis/assets/data/wave_power_density.zip",
+                    "mediaType": "application/octet-stream",
+                    "title": "Wave Power Density"
                 }
             ],
+            "identifier": "wave_power_density",
+            "issued": "2014-07-30",
             "keyword": [
                 "EPRI",
                 "NREL",
                 "u.s.",
                 "wave power density"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.nrel.gov/gis/maps-marine.html",
+            "language": [
+                "en-US"
             ],
+            "modified": "2024-08-14T13:38:51.583Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Solar Radiation Database (NSRDB)",
-            "description": "The NSRDB is a serially complete collection of hourly and half-hourly values of the three most common measurements of solar radiation\u2014global horizontal, direct normal, and diffuse horizontal irradiance\u2014and meteorological data. The current NSRDB is modeled using multi-channel measurements from geostationary satellites. The older versions of the NSRDB were modeled using cloud and weather information primarily collected at airports. A sufficient number of locations and temporal and spatial scales were used to represent regional solar radiation climates accurately.",
-            "modified": "2023-01-11T22:18:01.983Z",
-            "accessLevel": "public",
-            "identifier": "NSRDB",
-            "dataQuality": true,
-            "landingPage": "https://nsrdb.nrel.gov",
-            "rights": "true",
-            "temporal": "1998-01-01/2021-12-31",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Renewable Energy Laboratory",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Department of Energy"
+                    "name": "National Renewable Energy Laboratory"
                 }
             },
+            "rights": "true",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Wave Power Density"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NSRDB",
                 "hasEmail": "mailto:nsrdb@nrel.gov"
             },
+            "dataQuality": true,
+            "description": "The NSRDB is a serially complete collection of hourly and half-hourly values of the three most common measurements of solar radiation\u2014global horizontal, direct normal, and diffuse horizontal irradiance\u2014and meteorological data. The current NSRDB is modeled using multi-channel measurements from geostationary satellites. The older versions of the NSRDB were modeled using cloud and weather information primarily collected at airports. A sufficient number of locations and temporal and spatial scales were used to represent regional solar radiation climates accurately.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://developer.nrel.gov/docs/solar/nsrdb/",
-                    "title": "National Solar Radiation Database (NSRDB)",
-                    "description": "The NSRDB is a serially complete collection of hourly and half-hourly values of the three most common measurements of solar radiation\u2014global horizontal, direct normal, and diffuse horizontal irradiance\u2014and meteorological data. The current NSRDB is modeled using multi-channel measurements from geostationary satellites. The older versions of the NSRDB were modeled using cloud and weather information primarily collected at airports. A sufficient number of locations and temporal and spatial scales were used to represent regional solar radiation climates accurately."
+                    "description": "The NSRDB is a serially complete collection of hourly and half-hourly values of the three most common measurements of solar radiation\u2014global horizontal, direct normal, and diffuse horizontal irradiance\u2014and meteorological data. The current NSRDB is modeled using multi-channel measurements from geostationary satellites. The older versions of the NSRDB were modeled using cloud and weather information primarily collected at airports. A sufficient number of locations and temporal and spatial scales were used to represent regional solar radiation climates accurately.",
+                    "title": "National Solar Radiation Database (NSRDB)"
                 }
             ],
+            "identifier": "NSRDB",
             "keyword": [
                 "NREL",
                 "NSRDB",
                 "solar energy"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://nsrdb.nrel.gov",
+            "language": [
+                "en-US"
             ],
+            "modified": "2023-01-11T22:18:01.983Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Physical Solar Model version 3 Direct Normal Irradiance Multi-year Monthly Average",
-            "description": "This data provides monthly average daily total solar resource averaged over surface cells of 0.038 degrees in both latitude and longitude, or nominally 4 km in size. The solar radiation values represent the resource available to solar energy systems. The data was created using cloud properties which are generated using the AVHRR Pathfinder Atmospheres-Extended (PATMOS-x) algorithms. Fast all-sky radiation model for solar applications (FARMS) in conjunction with the cloud properties, and aerosol optical depth (AOD) and precipitable water vapor (PWV) from ancillary source are used to estimate direct normal irradiance (DNI) and global horizontal irradiance (GHI). The DNI and GHI are computed for clear skies using the REST2 model. For cloud scenes identified by the cloud mask, the FARMS is used to compute the DNI. The DNI for cloud scenes is then computed using the DISC model. The data are averaged from hourly model output over 19 years (1998-2016). The PATMOS-X model uses half-hourly radiance images in visible and infrared channels from the GOES series of geostationary weather satellites, daily snow cover data from the NSIDC and mixing ratio, temperature and pressure profiles from the Modern Era-Retrospective Analysis (MERRA-2) dataset. The REST2 model uses hourly aerosol optical depth from MERRA-2 to calculate GHI and DNI; water vapor and other inputs for REST 2 are obtained from the MERRA-2. \n\nThis dataset was derived from the NSRDB and may be used with the following citation:\n\nSengupta, M., Xie, Y., Lopez, A., Habte, A., Maclaurin, G., & Shelby, J. (2018). The national solar radiation data base (NSRDB). Renewable and Sustainable Energy Reviews, 89, 51-60.",
-            "modified": "2023-01-11T22:24:33.181Z",
-            "accessLevel": "public",
-            "identifier": "DNI_annavg_1998-2016",
-            "dataQuality": true,
-            "landingPage": "https://www.nrel.gov/gis/solar-resource-maps.html",
-            "rights": "true",
-            "temporal": "1998-01-01/2016-12-31",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Renewable Energy Laboratory",
@@ -28670,21 +28643,37 @@
                     "name": "Department of Energy"
                 }
             },
+            "rights": "true",
+            "temporal": "1998-01-01/2021-12-31",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "National Solar Radiation Database (NSRDB)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NSRDB",
                 "hasEmail": "mailto:nsrdb@nrel.gov"
             },
+            "dataQuality": true,
+            "description": "This data provides monthly average daily total solar resource averaged over surface cells of 0.038 degrees in both latitude and longitude, or nominally 4 km in size. The solar radiation values represent the resource available to solar energy systems. The data was created using cloud properties which are generated using the AVHRR Pathfinder Atmospheres-Extended (PATMOS-x) algorithms. Fast all-sky radiation model for solar applications (FARMS) in conjunction with the cloud properties, and aerosol optical depth (AOD) and precipitable water vapor (PWV) from ancillary source are used to estimate direct normal irradiance (DNI) and global horizontal irradiance (GHI). The DNI and GHI are computed for clear skies using the REST2 model. For cloud scenes identified by the cloud mask, the FARMS is used to compute the DNI. The DNI for cloud scenes is then computed using the DISC model. The data are averaged from hourly model output over 19 years (1998-2016). The PATMOS-X model uses half-hourly radiance images in visible and infrared channels from the GOES series of geostationary weather satellites, daily snow cover data from the NSIDC and mixing ratio, temperature and pressure profiles from the Modern Era-Retrospective Analysis (MERRA-2) dataset. The REST2 model uses hourly aerosol optical depth from MERRA-2 to calculate GHI and DNI; water vapor and other inputs for REST 2 are obtained from the MERRA-2. \n\nThis dataset was derived from the NSRDB and may be used with the following citation:\n\nSengupta, M., Xie, Y., Lopez, A., Habte, A., Maclaurin, G., & Shelby, J. (2018). The national solar radiation data base (NSRDB). Renewable and Sustainable Energy Reviews, 89, 51-60.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "image/tiff",
-                    "title": "Physical Solar Model version 3 Direct Normal Irradiance Multi-year Monthly Average",
                     "description": "This data provides monthly average daily total solar resource averaged over surface cells of 0.038 degrees in both latitude and longitude, or nominally 4 km in size. The solar radiation values represent the resource available to solar energy systems. The data was created using cloud properties which are generated using the AVHRR Pathfinder Atmospheres-Extended (PATMOS-x) algorithms. Fast all-sky radiation model for solar applications (FARMS) in conjunction with the cloud properties, and aerosol optical depth (AOD) and precipitable water vapor (PWV) from ancillary source are used to estimate direct normal irradiance (DNI) and global horizontal irradiance (GHI). The DNI and GHI are computed for clear skies using the REST2 model. For cloud scenes identified by the cloud mask, the FARMS is used to compute the DNI. The DNI for cloud scenes is then computed using the DISC model. The data are averaged from hourly model output over 19 years (1998-2016). The PATMOS-X model uses half-hourly radiance images in visible and infrared channels from the GOES series of geostationary weather satellites, daily snow cover data from the NSIDC and mixing ratio, temperature and pressure profiles from the Modern Era-Retrospective Analysis (MERRA-2) dataset. The REST2 model uses hourly aerosol optical depth from MERRA-2 to calculate GHI and DNI; water vapor and other inputs for REST 2 are obtained from the MERRA-2. \n\nThis dataset was derived from the NSRDB and may be used with the following citation:\n\nSengupta, M., Xie, Y., Lopez, A., Habte, A., Maclaurin, G., & Shelby, J. (2018). The national solar radiation data base (NSRDB). Renewable and Sustainable Energy Reviews, 89, 51-60.",
-                    "downloadURL": "https://www.nrel.gov/gis/assets/data/nsrdbv3_dni.zip"
+                    "downloadURL": "https://www.nrel.gov/gis/assets/data/nsrdbv3_dni.zip",
+                    "mediaType": "image/tiff",
+                    "title": "Physical Solar Model version 3 Direct Normal Irradiance Multi-year Monthly Average"
                 }
             ],
+            "identifier": "DNI_annavg_1998-2016",
             "keyword": [
                 "DNI",
                 "NREL",
@@ -28693,60 +28682,60 @@
                 "direct normal irradiance",
                 "solar energy"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.nrel.gov/gis/solar-resource-maps.html",
+            "language": [
+                "en-US"
             ],
+            "modified": "2023-01-11T22:24:33.181Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Physical Solar Model version 3 Direct Normal Irradiance Multi-year Monthly Average",
-            "description": "This data provides monthly average daily total solar resource averaged over surface cells of 0.038 degrees in both latitude and longitude, or nominally 4 km in size. The solar radiation values represent the resource available to solar energy systems. The data was created using cloud properties which are generated using the AVHRR Pathfinder Atmospheres-Extended (PATMOS-x) algorithms. Fast all-sky radiation model for solar applications (FARMS) in conjunction with the cloud properties, and aerosol optical depth (AOD) and precipitable water vapor (PWV) from ancillary source are used to estimate direct normal irradiance (DNI) and global horizontal irradiance (GHI). The DNI and GHI are computed for clear skies using the REST2 model. For cloud scenes identified by the cloud mask, the FARMS is used to compute the GHI. The DNI for cloud scenes is then computed using the DISC model. The data are averaged from hourly model output over 19 years (1998-2016). The PATMOS-X model uses half-hourly radiance images in visible and infrared channels from the GOES series of geostationary weather satellites, daily snow cover data from the NSIDC and mixing ratio, temperature and pressure profiles from the Modern Era-Retrospective Analysis (MERRA-2) dataset. The REST2 model uses hourly aerosol optical depth from MERRA-2 to calculate GHI and DNI; water vapor and other inputs for REST 2 are obtained from the MERRA-2.\n\nThis dataset was derived from the NSRDB and may be used with the following citation:\n\nSengupta, M., Xie, Y., Lopez, A., Habte, A., Maclaurin, G., & Shelby, J. (2018). The national solar radiation data base (NSRDB). Renewable and Sustainable Energy Reviews, 89, 51-60.",
-            "modified": "2023-01-12T00:21:57.537Z",
-            "accessLevel": "public",
-            "identifier": "DNI_monavg_1998-2016",
-            "dataQuality": true,
-            "landingPage": "https://www.nrel.gov/gis/solar-resource-maps.html",
-            "rights": "true",
-            "temporal": "1998-01-01/2016-12-31",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Renewable Energy Laboratory",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "National Renewable Energy Laboratory"
+                    "name": "Department of Energy"
                 }
             },
+            "rights": "true",
+            "temporal": "1998-01-01/2016-12-31",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Physical Solar Model version 3 Direct Normal Irradiance Multi-year Monthly Average"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NSRDB",
                 "hasEmail": "mailto:nsrdb@nrel.gov"
             },
+            "dataQuality": true,
+            "description": "This data provides monthly average daily total solar resource averaged over surface cells of 0.038 degrees in both latitude and longitude, or nominally 4 km in size. The solar radiation values represent the resource available to solar energy systems. The data was created using cloud properties which are generated using the AVHRR Pathfinder Atmospheres-Extended (PATMOS-x) algorithms. Fast all-sky radiation model for solar applications (FARMS) in conjunction with the cloud properties, and aerosol optical depth (AOD) and precipitable water vapor (PWV) from ancillary source are used to estimate direct normal irradiance (DNI) and global horizontal irradiance (GHI). The DNI and GHI are computed for clear skies using the REST2 model. For cloud scenes identified by the cloud mask, the FARMS is used to compute the GHI. The DNI for cloud scenes is then computed using the DISC model. The data are averaged from hourly model output over 19 years (1998-2016). The PATMOS-X model uses half-hourly radiance images in visible and infrared channels from the GOES series of geostationary weather satellites, daily snow cover data from the NSIDC and mixing ratio, temperature and pressure profiles from the Modern Era-Retrospective Analysis (MERRA-2) dataset. The REST2 model uses hourly aerosol optical depth from MERRA-2 to calculate GHI and DNI; water vapor and other inputs for REST 2 are obtained from the MERRA-2.\n\nThis dataset was derived from the NSRDB and may be used with the following citation:\n\nSengupta, M., Xie, Y., Lopez, A., Habte, A., Maclaurin, G., & Shelby, J. (2018). The national solar radiation data base (NSRDB). Renewable and Sustainable Energy Reviews, 89, 51-60.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "image/tiff",
-                    "title": "Physical Solar Model version 3 Global Horizontal Irradiance Multi-year Monthly Average",
                     "description": "This data provides monthly average daily total solar resource averaged over surface cells of 0.038 degrees in both latitude and longitude, or nominally 4 km in size. The solar radiation values represent the resource available to solar energy systems. The data was created using cloud properties which are generated using the AVHRR Pathfinder Atmospheres-Extended (PATMOS-x) algorithms. Fast all-sky radiation model for solar applications (FARMS) in conjunction with the cloud properties, and aerosol optical depth (AOD) and precipitable water vapor (PWV) from ancillary source are used to estimate direct normal irradiance (DNI) and global horizontal irradiance (GHI). The DNI and GHI are computed for clear skies using the REST2 model. For cloud scenes identified by the cloud mask, the FARMS is used to compute the GHI. The DNI for cloud scenes is then computed using the DISC model. The data are averaged from hourly model output over 19 years (1998-2016). The PATMOS-X model uses half-hourly radiance images in visible and infrared channels from the GOES series of geostationary weather satellites, daily snow cover data from the NSIDC and mixing ratio, temperature and pressure profiles from the Modern Era-Retrospective Analysis (MERRA-2) dataset. The REST2 model uses hourly aerosol optical depth from MERRA-2 to calculate GHI and DNI; water vapor and other inputs for REST 2 are obtained from the MERRA-2.\n\nThis dataset was derived from the NSRDB and may be used with the following citation:\n\nSengupta, M., Xie, Y., Lopez, A., Habte, A., Maclaurin, G., & Shelby, J. (2018). The national solar radiation data base (NSRDB). Renewable and Sustainable Energy Reviews, 89, 51-60.",
-                    "downloadURL": "https://www.nrel.gov/gis/assets/data/nsrdbv3_dni.zip"
+                    "downloadURL": "https://www.nrel.gov/gis/assets/data/nsrdbv3_dni.zip",
+                    "mediaType": "image/tiff",
+                    "title": "Physical Solar Model version 3 Global Horizontal Irradiance Multi-year Monthly Average"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "image/tiff",
-                    "title": "Physical Solar Model version 3 Direct Normal Irradiance Multi-year Monthly Average",
                     "description": "This data provides monthly average daily total solar resource averaged over surface cells of 0.038 degrees in both latitude and longitude, or nominally 4 km in size. The solar radiation values represent the resource available to solar energy systems. The data was created using cloud properties which are generated using the AVHRR Pathfinder Atmospheres-Extended (PATMOS-x) algorithms. Fast all-sky radiation model for solar applications (FARMS) in conjunction with the cloud properties, and aerosol optical depth (AOD) and precipitable water vapor (PWV) from ancillary source are used to estimate direct normal irradiance (DNI) and global horizontal irradiance (GHI). The DNI and GHI are computed for clear skies using the REST2 model. For cloud scenes identified by the cloud mask, the FARMS is used to compute the GHI. The DNI for cloud scenes is then computed using the DISC model. The data are averaged from hourly model output over 19 years (1998-2016). The PATMOS-X model uses half-hourly radiance images in visible and infrared channels from the GOES series of geostationary weather satellites, daily snow cover data from the NSIDC and mixing ratio, temperature and pressure profiles from the Modern Era-Retrospective Analysis (MERRA-2) dataset. The REST2 model uses hourly aerosol optical depth from MERRA-2 to calculate GHI and DNI; water vapor and other inputs for REST 2 are obtained from the MERRA-2.\n\nThis dataset was derived from the NSRDB and may be used with the following citation:\n\nSengupta, M., Xie, Y., Lopez, A., Habte, A., Maclaurin, G., & Shelby, J. (2018). The national solar radiation data base (NSRDB). Renewable and Sustainable Energy Reviews, 89, 51-60.",
-                    "downloadURL": "https://www.nrel.gov/gis/assets/data/nsrdbv3_dni.zip"
+                    "downloadURL": "https://www.nrel.gov/gis/assets/data/nsrdbv3_dni.zip",
+                    "mediaType": "image/tiff",
+                    "title": "Physical Solar Model version 3 Direct Normal Irradiance Multi-year Monthly Average"
                 }
             ],
+            "identifier": "DNI_monavg_1998-2016",
             "keyword": [
                 "DNI",
                 "NREL",
@@ -28755,53 +28744,53 @@
                 "monthly average",
                 "solar energy"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.nrel.gov/gis/solar-resource-maps.html",
+            "language": [
+                "en-US"
             ],
+            "modified": "2023-01-12T00:21:57.537Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Physical Solar Model version 3 Global Horizontal Irradiance Multi-year Annual Average",
-            "description": "This data provides annual average daily total solar resource averaged over surface cells of 0.038 degrees in both latitude and longitude, or nominally 4 km in size. The solar radiation values represent the resource available to solar energy systems. The data was created using cloud properties which are generated using the AVHRR Pathfinder Atmospheres-Extended (PATMOS-x) algorithms. Fast all-sky radiation model for solar applications (FARMS) in conjunction with the cloud properties, and aerosol optical depth (AOD) and precipitable water vapor (PWV) from ancillary source are used to estimate direct normal irradiance (DNI) and global horizontal irradiance (GHI). The DNI and GHI are computed for clear skies using the REST2 model. For cloud scenes identified by the cloud mask, the FARMS is used to compute the GHI. The DNI for cloud scenes is then computed using the DISC model. The data are averaged from hourly model output over 19 years (1998-2016). The PATMOS-X model uses half-hourly radiance images in visible and infrared channels from the GOES series of geostationary weather satellites, daily snow cover data from the NSIDC and mixing ratio, temperature and pressure profiles from the Modern Era-Retrospective Analysis (MERRA-2) dataset. The REST2 model uses hourly aerosol optical depth from MERRA-2 to calculate GHI and DNI; water vapor and other inputs for REST 2 are obtained from the MERRA-2.\n\nThis dataset was derived from the NSRDB and may be used with the following citation:\n\nSengupta, M., Xie, Y., Lopez, A., Habte, A., Maclaurin, G., & Shelby, J. (2018). The national solar radiation data base (NSRDB). Renewable and Sustainable Energy Reviews, 89, 51-60.",
-            "modified": "2023-01-11T22:40:07.448Z",
-            "accessLevel": "public",
-            "identifier": "GHI_annavg_1998-2016",
-            "dataQuality": true,
-            "landingPage": "https://www.nrel.gov/gis/solar-resource-maps.html",
-            "rights": "true",
-            "temporal": "1998-01-01/2016-12-31",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Renewable Energy Laboratory",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Department of Energy"
+                    "name": "National Renewable Energy Laboratory"
                 }
             },
+            "rights": "true",
+            "temporal": "1998-01-01/2016-12-31",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Physical Solar Model version 3 Direct Normal Irradiance Multi-year Monthly Average"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NSRDB",
                 "hasEmail": "mailto:nsrdb@nrel.gov"
             },
+            "dataQuality": true,
+            "description": "This data provides annual average daily total solar resource averaged over surface cells of 0.038 degrees in both latitude and longitude, or nominally 4 km in size. The solar radiation values represent the resource available to solar energy systems. The data was created using cloud properties which are generated using the AVHRR Pathfinder Atmospheres-Extended (PATMOS-x) algorithms. Fast all-sky radiation model for solar applications (FARMS) in conjunction with the cloud properties, and aerosol optical depth (AOD) and precipitable water vapor (PWV) from ancillary source are used to estimate direct normal irradiance (DNI) and global horizontal irradiance (GHI). The DNI and GHI are computed for clear skies using the REST2 model. For cloud scenes identified by the cloud mask, the FARMS is used to compute the GHI. The DNI for cloud scenes is then computed using the DISC model. The data are averaged from hourly model output over 19 years (1998-2016). The PATMOS-X model uses half-hourly radiance images in visible and infrared channels from the GOES series of geostationary weather satellites, daily snow cover data from the NSIDC and mixing ratio, temperature and pressure profiles from the Modern Era-Retrospective Analysis (MERRA-2) dataset. The REST2 model uses hourly aerosol optical depth from MERRA-2 to calculate GHI and DNI; water vapor and other inputs for REST 2 are obtained from the MERRA-2.\n\nThis dataset was derived from the NSRDB and may be used with the following citation:\n\nSengupta, M., Xie, Y., Lopez, A., Habte, A., Maclaurin, G., & Shelby, J. (2018). The national solar radiation data base (NSRDB). Renewable and Sustainable Energy Reviews, 89, 51-60.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "image/tiff",
-                    "title": "Physical Solar Model version 3 Global Horizontal Irradiance Multi-year Annual Average",
                     "description": "This data provides annual average daily total solar resource averaged over surface cells of 0.038 degrees in both latitude and longitude, or nominally 4 km in size. The solar radiation values represent the resource available to solar energy systems. The data was created using cloud properties which are generated using the AVHRR Pathfinder Atmospheres-Extended (PATMOS-x) algorithms. Fast all-sky radiation model for solar applications (FARMS) in conjunction with the cloud properties, and aerosol optical depth (AOD) and precipitable water vapor (PWV) from ancillary source are used to estimate direct normal irradiance (DNI) and global horizontal irradiance (GHI). The DNI and GHI are computed for clear skies using the REST2 model. For cloud scenes identified by the cloud mask, the FARMS is used to compute the GHI. The DNI for cloud scenes is then computed using the DISC model. The data are averaged from hourly model output over 19 years (1998-2016). The PATMOS-X model uses half-hourly radiance images in visible and infrared channels from the GOES series of geostationary weather satellites, daily snow cover data from the NSIDC and mixing ratio, temperature and pressure profiles from the Modern Era-Retrospective Analysis (MERRA-2) dataset. The REST2 model uses hourly aerosol optical depth from MERRA-2 to calculate GHI and DNI; water vapor and other inputs for REST 2 are obtained from the MERRA-2.\n\nThis dataset was derived from the NSRDB and may be used with the following citation:\n\nSengupta, M., Xie, Y., Lopez, A., Habte, A., Maclaurin, G., & Shelby, J. (2018). The national solar radiation data base (NSRDB). Renewable and Sustainable Energy Reviews, 89, 51-60.",
-                    "downloadURL": "https://www.nrel.gov/gis/assets/data/nsrdbv3_ghi.zip"
+                    "downloadURL": "https://www.nrel.gov/gis/assets/data/nsrdbv3_ghi.zip",
+                    "mediaType": "image/tiff",
+                    "title": "Physical Solar Model version 3 Global Horizontal Irradiance Multi-year Annual Average"
                 }
             ],
+            "identifier": "GHI_annavg_1998-2016",
             "keyword": [
                 "GHI",
                 "NREL",
@@ -28810,53 +28799,53 @@
                 "global horizontal irradiance",
                 "solar energy"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.nrel.gov/gis/solar-resource-maps.html",
+            "language": [
+                "en-US"
             ],
+            "modified": "2023-01-11T22:40:07.448Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Physical Solar Model version 3 Global Horizontal Irradiance Multi-year Monthly Average",
-            "description": "This data provides monthly average daily total solar resource averaged over surface cells of 0.038 degrees in both latitude and longitude, or nominally 4 km in size. The solar radiation values represent the resource available to solar energy systems. The data was created using cloud properties which are generated using the AVHRR Pathfinder Atmospheres-Extended (PATMOS-x) algorithms. Fast all-sky radiation model for solar applications (FARMS) in conjunction with the cloud properties, and aerosol optical depth (AOD) and precipitable water vapor (PWV) from ancillary source are used to estimate direct normal irradiance (DNI) and global horizontal irradiance (GHI). The DNI and GHI are computed for clear skies using the REST2 model. For cloud scenes identified by the cloud mask, the FARMS is used to compute the GHI. The DNI for cloud scenes is then computed using the DISC model. The data are averaged from hourly model output over 19 years (1998-2016). The PATMOS-X model uses half-hourly radiance images in visible and infrared channels from the GOES series of geostationary weather satellites, daily snow cover data from the NSIDC and mixing ratio, temperature and pressure profiles from the Modern Era-Retrospective Analysis (MERRA-2) dataset. The REST2 model uses hourly aerosol optical depth from MERRA-2 to calculate GHI and DNI; water vapor and other inputs for REST 2 are obtained from the MERRA-2.\n\nThis dataset was derived from the NSRDB and may be used with the following citation:\n\nSengupta, M., Xie, Y., Lopez, A., Habte, A., Maclaurin, G., & Shelby, J. (2018). The national solar radiation data base (NSRDB). Renewable and Sustainable Energy Reviews, 89, 51-60.",
-            "modified": "2023-01-12T22:57:33.452Z",
-            "accessLevel": "public",
-            "identifier": "GHI_monavg_1998-2016",
-            "dataQuality": true,
-            "landingPage": "https://www.nrel.gov/gis/solar-resource-maps.html",
-            "rights": "true",
-            "temporal": "1998-01-01/2106-12-31",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Renewable Energy Laboratory",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "National Renewable Energy Laboratory"
+                    "name": "Department of Energy"
                 }
             },
+            "rights": "true",
+            "temporal": "1998-01-01/2016-12-31",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Physical Solar Model version 3 Global Horizontal Irradiance Multi-year Annual Average"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NSRDB",
                 "hasEmail": "mailto:nsrdb@nrel.gov"
             },
+            "dataQuality": true,
+            "description": "This data provides monthly average daily total solar resource averaged over surface cells of 0.038 degrees in both latitude and longitude, or nominally 4 km in size. The solar radiation values represent the resource available to solar energy systems. The data was created using cloud properties which are generated using the AVHRR Pathfinder Atmospheres-Extended (PATMOS-x) algorithms. Fast all-sky radiation model for solar applications (FARMS) in conjunction with the cloud properties, and aerosol optical depth (AOD) and precipitable water vapor (PWV) from ancillary source are used to estimate direct normal irradiance (DNI) and global horizontal irradiance (GHI). The DNI and GHI are computed for clear skies using the REST2 model. For cloud scenes identified by the cloud mask, the FARMS is used to compute the GHI. The DNI for cloud scenes is then computed using the DISC model. The data are averaged from hourly model output over 19 years (1998-2016). The PATMOS-X model uses half-hourly radiance images in visible and infrared channels from the GOES series of geostationary weather satellites, daily snow cover data from the NSIDC and mixing ratio, temperature and pressure profiles from the Modern Era-Retrospective Analysis (MERRA-2) dataset. The REST2 model uses hourly aerosol optical depth from MERRA-2 to calculate GHI and DNI; water vapor and other inputs for REST 2 are obtained from the MERRA-2.\n\nThis dataset was derived from the NSRDB and may be used with the following citation:\n\nSengupta, M., Xie, Y., Lopez, A., Habte, A., Maclaurin, G., & Shelby, J. (2018). The national solar radiation data base (NSRDB). Renewable and Sustainable Energy Reviews, 89, 51-60.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "image/tiff",
-                    "title": "Physical Solar Model version 3 Global Horizontal Irradiance Multi-year Monthly Average",
                     "description": "This data provides monthly average daily total solar resource averaged over surface cells of 0.038 degrees in both latitude and longitude, or nominally 4 km in size. The solar radiation values represent the resource available to solar energy systems. The data was created using cloud properties which are generated using the AVHRR Pathfinder Atmospheres-Extended (PATMOS-x) algorithms. Fast all-sky radiation model for solar applications (FARMS) in conjunction with the cloud properties, and aerosol optical depth (AOD) and precipitable water vapor (PWV) from ancillary source are used to estimate direct normal irradiance (DNI) and global horizontal irradiance (GHI). The DNI and GHI are computed for clear skies using the REST2 model. For cloud scenes identified by the cloud mask, the FARMS is used to compute the GHI. The DNI for cloud scenes is then computed using the DISC model. The data are averaged from hourly model output over 19 years (1998-2016). The PATMOS-X model uses half-hourly radiance images in visible and infrared channels from the GOES series of geostationary weather satellites, daily snow cover data from the NSIDC and mixing ratio, temperature and pressure profiles from the Modern Era-Retrospective Analysis (MERRA-2) dataset. The REST2 model uses hourly aerosol optical depth from MERRA-2 to calculate GHI and DNI; water vapor and other inputs for REST 2 are obtained from the MERRA-2.\n\nThis dataset was derived from the NSRDB and may be used with the following citation:\n\nSengupta, M., Xie, Y., Lopez, A., Habte, A., Maclaurin, G., & Shelby, J. (2018). The national solar radiation data base (NSRDB). Renewable and Sustainable Energy Reviews, 89, 51-60.",
-                    "downloadURL": "https://www.nrel.gov/gis/assets/data/nsrdbv3_ghi.zip"
+                    "downloadURL": "https://www.nrel.gov/gis/assets/data/nsrdbv3_ghi.zip",
+                    "mediaType": "image/tiff",
+                    "title": "Physical Solar Model version 3 Global Horizontal Irradiance Multi-year Monthly Average"
                 }
             ],
+            "identifier": "GHI_monavg_1998-2016",
             "keyword": [
                 "GHI",
                 "NREL",
@@ -28865,30 +28854,14 @@
                 "monthly average",
                 "solar energy"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.nrel.gov/gis/solar-resource-maps.html",
+            "language": [
+                "en-US"
             ],
+            "modified": "2023-01-12T22:57:33.452Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "10-Hour - Closed-Loop Pumped Storage Hydropower Data",
-            "description": "The 10-hour, closed-loop PSH geospatial data include paired reservoir volume (gigaliter), capacity (megawatts), distance between reservoirs (kilometer), head height (meter), transmission spurline distance (kilometer), transmission spurline costs ($), and total cost ($/kilowatt).",
-            "modified": "2023-03-16T16:43:08.327Z",
-            "accessLevel": "public",
-            "identifier": "closedPSH_10hr",
-            "dataQuality": true,
-            "issued": "2022-05-31",
-            "landingPage": "https://www.nrel.gov/gis/psh-supply-curves.html",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Renewable Energy Laboratory",
@@ -28897,76 +28870,92 @@
                     "name": "National Renewable Energy Laboratory"
                 }
             },
+            "rights": "true",
+            "temporal": "1998-01-01/2106-12-31",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Physical Solar Model version 3 Global Horizontal Irradiance Multi-year Monthly Average"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Evan Rosenlieb",
                 "hasEmail": "mailto:Evan.Rosenlieb@nrel.gov"
             },
+            "dataQuality": true,
+            "description": "The 10-hour, closed-loop PSH geospatial data include paired reservoir volume (gigaliter), capacity (megawatts), distance between reservoirs (kilometer), head height (meter), transmission spurline distance (kilometer), transmission spurline costs ($), and total cost ($/kilowatt).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "title": "10-Hour - Closed-Loop Pumped Storage Hydropower Data",
                     "description": "The 10-hour, closed-loop PSH geospatial data include paired reservoir volume (gigaliter), capacity (megawatts), distance between reservoirs (kilometer), head height (meter), transmission spurline distance (kilometer), transmission spurline costs ($), and total cost ($/kilowatt).",
-                    "downloadURL": "https://www.nrel.gov/gis/assets/data/wave_significant_height.zip"
+                    "downloadURL": "https://www.nrel.gov/gis/assets/data/wave_significant_height.zip",
+                    "mediaType": "application/zip",
+                    "title": "10-Hour - Closed-Loop Pumped Storage Hydropower Data"
                 }
             ],
+            "identifier": "closedPSH_10hr",
+            "issued": "2022-05-31",
             "keyword": [
                 "NREL",
                 "closed loop",
                 "pumped storage hydropower",
                 "u.s."
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.nrel.gov/gis/psh-supply-curves.html",
+            "language": [
+                "en-US"
             ],
+            "modified": "2023-03-16T16:43:08.327Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Renewable Energy Laboratory",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "National Renewable Energy Laboratory"
+                }
+            },
             "references": [
                 "https://www.nrel.gov/docs/fy22osti/81277.pdf"
             ],
+            "rights": "true",
             "theme": [
                 "geospatial"
-            ]
+            ],
+            "title": "10-Hour - Closed-Loop Pumped Storage Hydropower Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Idaho National Laboratory",
-            "description": "INL is the nation\u2019s leading center for nuclear energy research and development. INL works in each of the strategic goal areas of DOE: energy, national security, science and environment.",
-            "modified": "2025-01-07T19:05:01.860Z",
             "accessLevel": "public",
-            "identifier": "DOE-019-2080254472",
-            "dataQuality": true,
-            "landingPage": "https://www.inl.gov/",
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "rights": "true",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Idaho National Laboratory",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Idaho National Laboratory"
-                }
-            },
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Carl Fennen",
                 "hasEmail": "mailto:carl.fennen@inl.gov"
             },
+            "dataQuality": true,
+            "description": "INL is the nation\u2019s leading center for nuclear energy research and development. INL works in each of the strategic goal areas of DOE: energy, national security, science and environment.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://inl.gov/",
                     "mediaType": "text/html",
-                    "title": "Idaho National Laboratory",
-                    "downloadURL": "https://inl.gov/"
+                    "title": "Idaho National Laboratory"
                 }
             ],
+            "identifier": "DOE-019-2080254472",
             "keyword": [
                 "nuclear",
                 "energy",
@@ -28974,47 +28963,50 @@
                 "national security",
                 "science"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.inl.gov/",
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2025-01-07T19:05:01.860Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Idaho National Laboratory",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Idaho National Laboratory"
+                }
+            },
+            "rights": "true",
+            "title": "Idaho National Laboratory"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Office of Nuclear Energy website",
-            "description": "The Office of Nuclear Energy's (NE) primary mission is to advance nuclear power as a resource capable of making major contributions in meeting our Nation\u2019s energy supply, environmental, and energy security needs. We seek to resolve technical, cost, safety, security and regulatory issues through research, development and demonstration. By focusing on the development of advanced nuclear technologies, NE supports the Administration\u2019s goals of providing domestic sources of secure energy, reducing greenhouse gases, and enhancing national security.\r\n\r\nNE\u2019s program is guided by the four research objectives detailed in its Nuclear Energy Research and Development Roadmap:\r\n\r\nDevelop technologies and other solutions that can improve the reliability, sustain the safety, and extend the life of current reactors. \r\nDevelop improvements in the affordability of new reactors to enable nuclear energy to help meet the Administration\u2019s energy security and climate change goals. \r\nDevelop sustainable fuel cycles. \r\nUnderstand and minimize the risks of nuclear proliferation and terrorism. \r\nNE serves present and future U.S. energy needs by developing critical technologies for the future and helping to train tomorrow\u2019s workforce. The benefits of nuclear power as a safe, carbon-free, reliable and secure source of energy make it an essential element in our Nation\u2019s energy and environmental future.",
-            "modified": "2022-07-12T19:23:35.234Z",
             "accessLevel": "public",
-            "identifier": "DOE-019-6654897611",
-            "dataQuality": true,
-            "describedByType": "text/html",
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "rights": "true",
-            "spatial": "DOE",
-            "temporal": "1982/2014",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE Nuclear Energy"
-            },
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Andrew Richards",
                 "hasEmail": "mailto:Andrew.richards@hq.doe.gov"
             },
+            "dataQuality": true,
+            "describedByType": "text/html",
+            "description": "The Office of Nuclear Energy's (NE) primary mission is to advance nuclear power as a resource capable of making major contributions in meeting our Nation\u2019s energy supply, environmental, and energy security needs. We seek to resolve technical, cost, safety, security and regulatory issues through research, development and demonstration. By focusing on the development of advanced nuclear technologies, NE supports the Administration\u2019s goals of providing domestic sources of secure energy, reducing greenhouse gases, and enhancing national security.\r\n\r\nNE\u2019s program is guided by the four research objectives detailed in its Nuclear Energy Research and Development Roadmap:\r\n\r\nDevelop technologies and other solutions that can improve the reliability, sustain the safety, and extend the life of current reactors. \r\nDevelop improvements in the affordability of new reactors to enable nuclear energy to help meet the Administration\u2019s energy security and climate change goals. \r\nDevelop sustainable fuel cycles. \r\nUnderstand and minimize the risks of nuclear proliferation and terrorism. \r\nNE serves present and future U.S. energy needs by developing critical technologies for the future and helping to train tomorrow\u2019s workforce. The benefits of nuclear power as a safe, carbon-free, reliable and secure source of energy make it an essential element in our Nation\u2019s energy and environmental future.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://energy.gov/ne/office-nuclear-energy",
                     "mediaType": "text/html",
-                    "title": "Nuclear Energy web",
-                    "downloadURL": "https://energy.gov/ne/office-nuclear-energy"
+                    "title": "Nuclear Energy web"
                 }
             ],
+            "identifier": "DOE-019-6654897611",
             "keyword": [
                 "advanced modeling and simulation",
                 "fuel cycle technologies",
@@ -29025,40 +29017,40 @@
                 "nuclear energy university program",
                 "nuclear facility operations"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2022-07-12T19:23:35.234Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE Nuclear Energy"
+            },
+            "rights": "true",
+            "spatial": "DOE",
+            "temporal": "1982/2014",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Office of Nuclear Energy website"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Office of Nuclear Energy Document Library",
-            "description": "The library contains over 260 documents regarding nuclear energy projects of DOE.",
-            "modified": "2014-10-30",
             "accessLevel": "public",
-            "identifier": "DOE-019-6633765611",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "spatial": "DOE",
-            "temporal": "1982/2014",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE Office of Nuclear Energy"
-            },
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Andrew Richards",
                 "hasEmail": "mailto:Andrew.richards@hq.doe.gov"
             },
+            "dataQuality": true,
+            "description": "The library contains over 260 documents regarding nuclear energy projects of DOE.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -29066,6 +29058,7 @@
                     "title": "Nuclear Energy Library"
                 }
             ],
+            "identifier": "DOE-019-6633765611",
             "keyword": [
                 "agreement",
                 "database",
@@ -29074,49 +29067,49 @@
                 "quarterly reports",
                 "scorecards"
             ],
-            "bureauCode": [
-                "019:20"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2014-10-30",
             "programCode": [
                 "019:014"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE Office of Nuclear Energy"
+            },
+            "spatial": "DOE",
+            "temporal": "1982/2014",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Office of Nuclear Energy Document Library"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Nuclear Energy Webpage",
-            "description": "The Office of Nuclear Energy\u2019s (NE) primary mission is to advance nuclear power as a resource capable of making major contributions in meeting our Nation\u2019s energy supply, environmental, and energy security needs. We seek to resolve technical, cost, safety, security and regulatory issues through research, development and demonstration. By focusing on the development of advanced nuclear technologies, NE supports the Administration\u2019s goals of providing domestic sources of secure energy, reducing greenhouse gases, and enhancing national security.\r\n\r\nNE\u2019s program is guided by the four research objectives detailed in its Nuclear Energy Research and Development Roadmap:\r\n\u2022Develop technologies and other solutions that can improve the reliability, sustain the safety, and extend the life of current reactors.\r\n\u2022Develop improvements in the affordability of new reactors to enable nuclear energy to help meet the Administration\u2019s energy security and climate change goals.\r\n\u2022Develop sustainable fuel cycles.\r\n\u2022Understand and minimize the risks of nuclear proliferation and terrorism.\r\n\r\nNE serves present and future U.S. energy needs by developing critical technologies for the future and helping to train tomorrow\u2019s workforce. The benefits of nuclear power as a safe, carbon-free, reliable and secure source of energy make it an essential element in our Nation\u2019s energy and environmental future.",
-            "modified": "2015-10-30",
             "accessLevel": "public",
-            "identifier": "DOE-019-2416184566",
-            "dataQuality": true,
-            "issued": "2009-09-30",
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "spatial": "DOE",
-            "temporal": "2015/2000",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE Office of Nuclear Energy"
-            },
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Deborah Sharpe",
                 "hasEmail": "mailto:deborah.sharpe@nuclear.energy.gov"
             },
+            "dataQuality": true,
+            "description": "The Office of Nuclear Energy\u2019s (NE) primary mission is to advance nuclear power as a resource capable of making major contributions in meeting our Nation\u2019s energy supply, environmental, and energy security needs. We seek to resolve technical, cost, safety, security and regulatory issues through research, development and demonstration. By focusing on the development of advanced nuclear technologies, NE supports the Administration\u2019s goals of providing domestic sources of secure energy, reducing greenhouse gases, and enhancing national security.\r\n\r\nNE\u2019s program is guided by the four research objectives detailed in its Nuclear Energy Research and Development Roadmap:\r\n\u2022Develop technologies and other solutions that can improve the reliability, sustain the safety, and extend the life of current reactors.\r\n\u2022Develop improvements in the affordability of new reactors to enable nuclear energy to help meet the Administration\u2019s energy security and climate change goals.\r\n\u2022Develop sustainable fuel cycles.\r\n\u2022Understand and minimize the risks of nuclear proliferation and terrorism.\r\n\r\nNE serves present and future U.S. energy needs by developing critical technologies for the future and helping to train tomorrow\u2019s workforce. The benefits of nuclear power as a safe, carbon-free, reliable and secure source of energy make it an essential element in our Nation\u2019s energy and environmental future.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://energy.gov/ne/office-nuclear-energy",
                     "mediaType": "text/html",
-                    "title": "Nuclear Energy Webpage",
-                    "downloadURL": "https://energy.gov/ne/office-nuclear-energy"
+                    "title": "Nuclear Energy Webpage"
                 }
             ],
+            "identifier": "DOE-019-2416184566",
+            "issued": "2009-09-30",
             "keyword": [
                 "advanced modeling",
                 "advanced simulation",
@@ -29126,81 +29119,80 @@
                 "nuclear reactor",
                 "space power"
             ],
-            "bureauCode": [
-                "019:20"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2015-10-30",
             "programCode": [
                 "019:014"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE Office of Nuclear Energy"
+            },
+            "spatial": "DOE",
+            "temporal": "2015/2000",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Nuclear Energy Webpage"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "DOE Global Energy Storage Database",
-            "description": "Information on grid-connected energy storage projects and relevant state and federal policies",
-            "modified": "2020-01-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-2020013001",
-            "landingPage": "https://www.sandia.gov/ess-ssl/global-energy-storage-database/",
-            "license": "https://www.sandia.gov/ess-ssl/global-energy-storage-database/",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of Electricity"
-            },
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Imre Gyuk",
                 "hasEmail": "mailto:gesdb@sandia.gov"
             },
+            "description": "Information on grid-connected energy storage projects and relevant state and federal policies",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.sandia.gov/ess-ssl/global-energy-storage-database/",
+                    "description": "Information on grid-connected energy storage projects and relevant state and federal policies",
                     "format": "text/csv",
-                    "title": "DOE Global Energy Storage Database",
-                    "description": "Information on grid-connected energy storage projects and relevant state and federal policies"
+                    "title": "DOE Global Energy Storage Database"
                 }
             ],
+            "identifier": "DOE-019-2020013001",
             "keyword": [
                 "Energy Storage",
                 "Geospatial"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "https://www.sandia.gov/ess-ssl/global-energy-storage-database/",
+            "language": [
+                "us-EN"
             ],
+            "license": "https://www.sandia.gov/ess-ssl/global-energy-storage-database/",
+            "modified": "2020-01-01",
             "programCode": [
                 "019:015"
             ],
-            "language": [
-                "us-EN"
-            ]
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of Electricity"
+            },
+            "title": "DOE Global Energy Storage Database"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Office of Electricity website",
-            "description": "The Office of Electricity (OE) provides national leadership to ensure that the Nation\u2019s energy delivery system is secure, resilient and reliable. OE works to develop new technologies to improve the infrastructure that brings electricity into our homes, offices, and factories, and the federal and state electricity policies and programs that shape electricity system planning and market operations. OE also works to bolster the resiliency of the electric grid and assists with restoration when major energy supply interruptions occur.",
-            "modified": "2019-10-21",
             "accessLevel": "public",
-            "identifier": "DOE-019-6668545421",
-            "dataQuality": true,
-            "license": "http://opendatacommons.org/licenses/pddl/",
-            "spatial": "United States",
-            "temporal": "2003/2014",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE Office of Electricity"
-            },
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Terri Lee",
                 "hasEmail": "mailto:terri.lee@hq.doe.gov"
             },
+            "dataQuality": true,
+            "description": "The Office of Electricity (OE) provides national leadership to ensure that the Nation\u2019s energy delivery system is secure, resilient and reliable. OE works to develop new technologies to improve the infrastructure that brings electricity into our homes, offices, and factories, and the federal and state electricity policies and programs that shape electricity system planning and market operations. OE also works to bolster the resiliency of the electric grid and assists with restoration when major energy supply interruptions occur.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -29208,6 +29200,7 @@
                     "title": "Electricity web"
                 }
             ],
+            "identifier": "DOE-019-6668545421",
             "keyword": [
                 "DOE grid technology",
                 "advanced grid intergration",
@@ -29221,36 +29214,37 @@
                 "power systems research and engineering",
                 "technology development"
             ],
-            "bureauCode": [
-                "019:20"
+            "language": [
+                "en-US"
             ],
+            "license": "http://opendatacommons.org/licenses/pddl/",
+            "modified": "2019-10-21",
             "programCode": [
                 "019:015"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE Office of Electricity"
+            },
+            "spatial": "United States",
+            "temporal": "2003/2014",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Office of Electricity website"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Office of Electricity Information Center",
-            "description": "The information center contains various information and documents, such as congressional testimony, recovery act, educational materials, reporting, library, etc.",
-            "modified": "2014-10-30",
             "accessLevel": "public",
-            "identifier": "DOE-019-3423784456",
-            "license": "http://opendatacommons.org/licenses/pddl/",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE Office of Electricity"
-            },
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Terri Lee",
                 "hasEmail": "mailto:terri.lee@hq.doe.gov"
             },
+            "description": "The information center contains various information and documents, such as congressional testimony, recovery act, educational materials, reporting, library, etc.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -29258,6 +29252,7 @@
                     "title": "Electricity Information Center"
                 }
             ],
+            "identifier": "DOE-019-3423784456",
             "keyword": [
                 "congressional testimony",
                 "educational materials",
@@ -29265,15 +29260,20 @@
                 "recovery act",
                 "reporting"
             ],
-            "bureauCode": [
-                "019:20"
+            "language": [
+                "en-US"
             ],
+            "license": "http://opendatacommons.org/licenses/pddl/",
+            "modified": "2014-10-30",
             "programCode": [
                 "019:015"
             ],
-            "language": [
-                "en-US"
-            ]
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE Office of Electricity"
+            },
+            "title": "Office of Electricity Information Center"
         }
-    ]
+    ],
+    "describedBy": "https://project-open-data.cio.gov/v1.1/schema/catalog.json"
 }
```

