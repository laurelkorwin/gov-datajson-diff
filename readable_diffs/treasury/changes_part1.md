# Change History for treasury.json

### Changes from 31606f9 to dd2190f
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
diff --git a/treasury.json b/treasury.json
index 6b11e5d..2f27528 100644
--- a/treasury.json
+++ b/treasury.json
@@ -3,117 +3,124 @@
     "@id": "http://www.treasury.gov/data.json",
     "@type": "dcat:Catalog",
     "conformsTo": "https://project-open-data.cio.gov/v1.1/schema",
-    "describedBy": "https://project-open-data.cio.gov/v1.1/schema/catalog.json",
     "dataset": [
         {
             "@type": "dcat:Dataset",
-            "identifier": "015-BEP-001",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:20"
+            ],
+            "contactPoint": {
+                "fn": "External Relations",
+                "hasEmail": "mailto:moneyfactory.info@bep.gov"
+            },
+            "description": "The number of notes printed in a Fiscal Year by denomination",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://moneyfactory.gov/resources/productionannual.html",
                     "downloadURL": "https://inventory.data.gov/dataset/2b1dcd52-058e-410f-b656-f35962738c4f/resource/72a33ebb-3efe-455b-9e41-0733aaed7780",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Annual Production Figures of United States Currency",
-            "description": "The number of notes printed in a Fiscal Year by denomination",
+            "identifier": "015-BEP-001",
             "keyword": [
                 "currency",
                 "denomination",
                 "printing"
             ],
+            "landingPage": "http://moneyfactory.gov/resources/productionannual.html",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2012-10-01",
+            "programCode": [
+                "015:064"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of Engraving and Printing",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "BEP",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "BEP"
-                },
-                "name": "Bureau of Engraving and Printing"
-            },
-            "contactPoint": {
-                "fn": "External Relations",
-                "hasEmail": "mailto:moneyfactory.info@bep.gov"
+            "title": "Annual Production Figures of United States Currency"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
-                "015:20"
-            ],
-            "programCode": [
-                "015:064"
+                "015:60"
             ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://moneyfactory.gov/resources/productionannual.html"
+            "contactPoint": {
+                "fn": "CDFI Fund Help Desk",
+                "hasEmail": "mailto:cdfihelp@cdfi.treas.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-CDFI-002",
+            "description": "CDFI Fund Searchable Award Database with list of awardees/allocatees",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.cdfifund.gov/research-data/Pages/default.aspx",
                     "downloadURL": "https://www.cdfifund.gov/awards/state-awards/Pages/default.aspx",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Community Development Financial Institutions Fund - Searchable Awards Database",
-            "description": "CDFI Fund Searchable Award Database with list of awardees/allocatees",
+            "identifier": "015-CDFI-002",
+            "issued": "2015-06-02T00:00:00",
             "keyword": [
                 "Community Development Financial Institutions Fund",
                 "CDFI",
                 "CDFI Awardee",
                 "CDFI Allocatee"
             ],
+            "landingPage": "https://www.cdfifund.gov/research-data/Pages/default.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2015-06-02",
+            "primaryITInvestmentUII": "015-000006002",
+            "programCode": [
+                "015:017"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Community Development Financial Institutions Fund",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "CDFI",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "CDFI"
-                },
-                "name": "Community Development Financial Institutions Fund"
-            },
-            "contactPoint": {
-                "fn": "CDFI Fund Help Desk",
-                "hasEmail": "mailto:cdfihelp@cdfi.treas.gov"
+            "title": "Community Development Financial Institutions Fund - Searchable Awards Database"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:60"
             ],
-            "programCode": [
-                "015:017"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "https://www.cdfifund.gov/research-data/Pages/default.aspx",
-            "primaryITInvestmentUII": "015-000006002",
-            "issued": "2015-06-02T00:00:00"
+            "contactPoint": {
+                "fn": "CDFI Fund Help Desk",
+                "hasEmail": "mailto:cdfihelp@cdfi.treas.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-CDFI-003",
+            "description": "This data set contains eleven years of data provided by Community Development Financial Institutions (CDFIs) through the CDFI Fund data collection system known as the Community Investment Impact System (CIIS). The data collected covers fiscal years (FY) 2003 through 2013 and contains Institution Level Report (ILR) data on 728 CDFIs.  In general, these CDFIs have provided information on their operations, financial status, and impact in their communities.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.cdfifund.gov/research-data/Pages/default.aspx",
                     "downloadURL": "https://www.cdfifund.gov/Documents/Forms/Awards.aspx",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Data on CDFI Program Awardees",
-            "description": "This data set contains eleven years of data provided by Community Development Financial Institutions (CDFIs) through the CDFI Fund data collection system known as the Community Investment Impact System (CIIS). The data collected covers fiscal years (FY) 2003 through 2013 and contains Institution Level Report (ILR) data on 728 CDFIs.  In general, these CDFIs have provided information on their operations, financial status, and impact in their communities.",
+            "identifier": "015-CDFI-003",
+            "issued": "2015-06-30T00:00:00",
             "keyword": [
                 "CDFI",
                 "Community Development Financial Institutions Fund",
@@ -122,104 +129,104 @@
                 "Institution Level Report",
                 "ILR"
             ],
+            "landingPage": "https://www.cdfifund.gov/research-data/Pages/default.aspx",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2015-06-30",
+            "primaryITInvestmentUII": "015-000006002",
+            "programCode": [
+                "015:017"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Community Development Financial Institutions",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "CDFI",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "CDFI"
-                },
-                "name": "Community Development Financial Institutions"
-            },
-            "contactPoint": {
-                "fn": "CDFI Fund Help Desk",
-                "hasEmail": "mailto:cdfihelp@cdfi.treas.gov"
+            "title": "Data on CDFI Program Awardees"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:60"
             ],
-            "programCode": [
-                "015:017"
-            ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "https://www.cdfifund.gov/research-data/Pages/default.aspx",
-            "primaryITInvestmentUII": "015-000006002",
-            "issued": "2015-06-30T00:00:00"
+            "contactPoint": {
+                "fn": "CDFI Fund Help Desk",
+                "hasEmail": "mailto:cdfihelp@cdfi.treas.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-CDFI-001",
+            "description": "Search for New Markets Tax Credit Allocatees serving specific states. New Markets Tax Credit Program allocatees can make investments in all 50 states, the District of Columbia, Puerto Rico, and certain U.S. Territories. Known as Community Development Entities, allocatees have approved service areas that range from local to national in scale. \r\n\r\nThis search function was designed to allow organizations to search for CDEs that may have available NMTC allocation authority remaining. The map above and the search function below will display results by service area for allocatees that have received awards from 2012 to the present. The map displays allocatees that have specified those states in their designated service areas. To search for CDEs with a national service area, which may invest anywhere in the country, select \"National\" from the drop-down Service Area search box below. All search results will appear at the bottom of this page.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.cdfifund.gov/research-data/Pages/default.aspx",
                     "downloadURL": "https://www.cdfifund.gov/awards/nmtc/Pages/default.aspx",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "New Markets Tax Credit Investments Program States Served Database",
-            "description": "Search for New Markets Tax Credit Allocatees serving specific states. New Markets Tax Credit Program allocatees can make investments in all 50 states, the District of Columbia, Puerto Rico, and certain U.S. Territories. Known as Community Development Entities, allocatees have approved service areas that range from local to national in scale. \r\n\r\nThis search function was designed to allow organizations to search for CDEs that may have available NMTC allocation authority remaining. The map above and the search function below will display results by service area for allocatees that have received awards from 2012 to the present. The map displays allocatees that have specified those states in their designated service areas. To search for CDEs with a national service area, which may invest anywhere in the country, select \"National\" from the drop-down Service Area search box below. All search results will appear at the bottom of this page.",
+            "identifier": "015-CDFI-001",
+            "issued": "2015-06-02T00:00:00",
             "keyword": [
                 "NMTC",
                 "New Markets Tax Credits",
                 "CDFI",
                 "Community Development Financial Institutions Fund"
             ],
+            "landingPage": "https://www.cdfifund.gov/research-data/Pages/default.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2015-06-02",
+            "primaryITInvestmentUII": "015-000006002",
+            "programCode": [
+                "015:017"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Community Development Financial Institutions",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "CDFI",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "CDFI"
-                },
-                "name": "Community Development Financial Institutions"
-            },
-            "contactPoint": {
-                "fn": "CDFI Fund Help Desk",
-                "hasEmail": "mailto:cdfihelp@cdfi.treas.gov"
+            "title": "New Markets Tax Credit Investments Program States Served Database"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
-                "015:60"
-            ],
-            "programCode": [
-                "015:017"
+                "015:00"
             ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "https://www.cdfifund.gov/research-data/Pages/default.aspx",
-            "primaryITInvestmentUII": "015-000006002",
-            "issued": "2015-06-02T00:00:00"
+            "contactPoint": {
+                "fn": "Department of the Treasury",
+                "hasEmail": "mailto:digital@treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-033",
+            "description": "Treasury plans to sell up to $10 billion of securities per month, subject to market conditions.  This is in addition to principal paydowns (currently ranging between $2 and $4 billion per month).   If the sales proceeded at the full $10 billion per month, the portfolio would be unwound in whole over approximately one year, depending on future rates of prepayments. If market conditions change and Treasury slows asset sales, it is possible that the unwind will take a longer period of time.  Dealer scorecard shows a ranking of buyers of MBS securities by amount purchased monthly and overall.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/Pages/mbs-purchase-program.aspx",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/Documents/March%202012%20Dealer%20Scorecard.pdf",
-                    "mediaType": "application/pdf",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/pdf"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/Pages/mbs-purchase-program.aspx",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/Documents/March%202012%20Dealer%20Scorecard.xlsx",
-                    "mediaType": "application/vnd.ms-excel",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.ms-excel"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "Agency MBS Purchase Program - Dealer Scorecard",
-            "description": "Treasury plans to sell up to $10 billion of securities per month, subject to market conditions.  This is in addition to principal paydowns (currently ranging between $2 and $4 billion per month).   If the sales proceeded at the full $10 billion per month, the portfolio would be unwound in whole over approximately one year, depending on future rates of prepayments. If market conditions change and Treasury slows asset sales, it is possible that the unwind will take a longer period of time.  Dealer scorecard shows a ranking of buyers of MBS securities by amount purchased monthly and overall.",
+            "identifier": "015-DO-033",
+            "issued": "2014-08-31T00:00:00",
             "keyword": [
                 "Agency MBS Purchase Program",
                 "MBS Sale",
@@ -227,48 +234,48 @@
                 "Fannie Mae",
                 "Freddie Mae."
             ],
+            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/Pages/mbs-purchase-program.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2014-08-13",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Department of the Treasury",
-                "hasEmail": "mailto:digital@treasury.gov"
+            "title": "Agency MBS Purchase Program - Dealer Scorecard"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/Pages/mbs-purchase-program.aspx",
-            "issued": "2014-08-31T00:00:00"
+            "contactPoint": {
+                "fn": "Department of the Treasury",
+                "hasEmail": "mailto:digital@treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-031",
+            "description": "Treasury plans to sell up to $10 billion of securities per month, subject to market conditions.  This is in addition to principal paydowns (currently ranging between $2 and $4 billion per month).   If the sales proceeded at the full $10 billion per month, the portfolio would be unwound in whole over approximately one year, depending on future rates of prepayments. If market conditions change and Treasury slows asset sales, it is possible that the unwind will take a longer period of time.  Sell off of MBS securities ended March 2012.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/Pages/mbs-purchase-program.aspx",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/Documents/March%202012%20Portfolio%20by%20month.pdf",
-                    "mediaType": "application/pdf",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "Agency MBS Purchase Program - Portfolio by month",
-            "description": "Treasury plans to sell up to $10 billion of securities per month, subject to market conditions.  This is in addition to principal paydowns (currently ranging between $2 and $4 billion per month).   If the sales proceeded at the full $10 billion per month, the portfolio would be unwound in whole over approximately one year, depending on future rates of prepayments. If market conditions change and Treasury slows asset sales, it is possible that the unwind will take a longer period of time.  Sell off of MBS securities ended March 2012.",
+            "identifier": "015-DO-031",
+            "issued": "2014-08-31T00:00:00",
             "keyword": [
                 "Agency MBS Purchase Program",
                 "MBS Sale",
@@ -276,48 +283,48 @@
                 "Fannie Mae",
                 "Freddie Mae."
             ],
+            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/Pages/mbs-purchase-program.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2014-08-13",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Department of the Treasury",
-                "hasEmail": "mailto:digital@treasury.gov"
+            "title": "Agency MBS Purchase Program - Portfolio by month"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/Pages/mbs-purchase-program.aspx",
-            "issued": "2014-08-31T00:00:00"
+            "contactPoint": {
+                "fn": "Department of the Treasury",
+                "hasEmail": "mailto:digital@treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-034",
+            "description": "Treasury plans to sell up to $10 billion of securities per month, subject to market conditions.  This is in addition to principal paydowns (currently ranging between $2 and $4 billion per month).   If the sales proceeded at the full $10 billion per month, the portfolio would be unwound in whole over approximately one year, depending on future rates of prepayments. If market conditions change and Treasury slows asset sales, it is possible that the unwind will take a longer period of time.  Shows range of prices MBS securities were purchased for.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/Pages/mbs-purchase-program.aspx",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/Documents/Portfolio%20Disposition%20Trade%20Data_Final.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.ms-excel"
                 }
             ],
-            "accrualPeriodicity": "R/P1D",
-            "title": "Agency MBS Purchase Program - Portfolio Disposition Trade Data",
-            "description": "Treasury plans to sell up to $10 billion of securities per month, subject to market conditions.  This is in addition to principal paydowns (currently ranging between $2 and $4 billion per month).   If the sales proceeded at the full $10 billion per month, the portfolio would be unwound in whole over approximately one year, depending on future rates of prepayments. If market conditions change and Treasury slows asset sales, it is possible that the unwind will take a longer period of time.  Shows range of prices MBS securities were purchased for.",
+            "identifier": "015-DO-034",
+            "issued": "2014-08-31T00:00:00",
             "keyword": [
                 "Agency MBS Purchase Program",
                 "MBS Sale",
@@ -325,48 +332,48 @@
                 "Fannie Mae",
                 "Freddie Mae."
             ],
+            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/Pages/mbs-purchase-program.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2014-08-13",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Department of the Treasury",
-                "hasEmail": "mailto:digital@treasury.gov"
+            "title": "Agency MBS Purchase Program - Portfolio Disposition Trade Data"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/Pages/mbs-purchase-program.aspx",
-            "issued": "2014-08-31T00:00:00"
+            "contactPoint": {
+                "fn": "Department of the Treasury",
+                "hasEmail": "mailto:digital@treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-032",
+            "description": "Treasury plans to sell up to $10 billion of securities per month, subject to market conditions.  This is in addition to principal paydowns (currently ranging between $2 and $4 billion per month).   If the sales proceeded at the full $10 billion per month, the portfolio would be unwound in whole over approximately one year, depending on future rates of prepayments. If market conditions change and Treasury slows asset sales, it is possible that the unwind will take a longer period of time.  Excel data shows the total principal and interest that the Treasury received from purchase to sell off of the MBS securities.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/Pages/mbs-purchase-program.aspx",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/Documents/March%202012%20MBS%20Principal%20and%20Interest%20Monthly%20Breakout.pdf",
-                    "mediaType": "application/pdf",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "Agency MBS Purchase Program - Principal and Interest Received",
-            "description": "Treasury plans to sell up to $10 billion of securities per month, subject to market conditions.  This is in addition to principal paydowns (currently ranging between $2 and $4 billion per month).   If the sales proceeded at the full $10 billion per month, the portfolio would be unwound in whole over approximately one year, depending on future rates of prepayments. If market conditions change and Treasury slows asset sales, it is possible that the unwind will take a longer period of time.  Excel data shows the total principal and interest that the Treasury received from purchase to sell off of the MBS securities.",
+            "identifier": "015-DO-032",
+            "issued": "2014-08-31T00:00:00",
             "keyword": [
                 "Agency MBS Purchase Program",
                 "MBS Sale",
@@ -374,48 +381,48 @@
                 "Fannie Mae",
                 "Freddie Mae."
             ],
+            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/Pages/mbs-purchase-program.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2023-12-08",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Department of the Treasury",
-                "hasEmail": "mailto:digital@treasury.gov"
+            "title": "Agency MBS Purchase Program - Principal and Interest Received"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/Pages/mbs-purchase-program.aspx",
-            "issued": "2014-08-31T00:00:00"
+            "contactPoint": {
+                "fn": "Department of the Treasury",
+                "hasEmail": "mailto:digital@treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-030",
+            "description": "Treasury plans to sell up to $10 billion of securities per month, subject to market conditions.  This is in addition to principal paydowns (currently ranging between $2 and $4 billion per month).   If the sales proceeded at the full $10 billion per month, the portfolio would be unwound in whole over approximately one year, depending on future rates of prepayments. If market conditions change and Treasury slows asset sales, it is possible that the unwind will take a longer period of time.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/Pages/mbs-purchase-program.aspx",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/Documents/March%202012%20Trades%20By%20Month.pdf",
-                    "mediaType": "application/pdf",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "Agency MBS Purchase Program - Trades by month",
-            "description": "Treasury plans to sell up to $10 billion of securities per month, subject to market conditions.  This is in addition to principal paydowns (currently ranging between $2 and $4 billion per month).   If the sales proceeded at the full $10 billion per month, the portfolio would be unwound in whole over approximately one year, depending on future rates of prepayments. If market conditions change and Treasury slows asset sales, it is possible that the unwind will take a longer period of time.",
+            "identifier": "015-DO-030",
+            "issued": "2014-08-31T00:00:00",
             "keyword": [
                 "Agency MBS Purchase Program",
                 "MBS Sale",
@@ -423,263 +430,263 @@
                 "Fannie Mae",
                 "Freddie Mae."
             ],
+            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/Pages/mbs-purchase-program.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2023-12-08",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Department of the Treasury",
-                "hasEmail": "mailto:digital@treasury.gov"
+            "title": "Agency MBS Purchase Program - Trades by month"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/Pages/mbs-purchase-program.aspx",
-            "issued": "2014-08-31T00:00:00"
+            "contactPoint": {
+                "fn": "Office of Economic Policy",
+                "hasEmail": "mailto:digital@treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-053",
+            "description": "Under Public Law 102-321, the Department of Treasury is required to produce annual estimates of Total Taxable Resources (TTR), Treasury's estimates of the relative fiscal capacity of the states. TTR was developed as an outgrowth of a Congressionally mandated study on Federal, State, and local government fiscal relations entitled \"Federal-Sate-Local Fiscal Relations: Technical Papers, Vol. 2, Office of State and Local Finance, Department of Treasury, September 1986\".",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/economic-policy/taxable-resources/Pages/Total-Taxable-Resources.aspx",
                     "downloadURL": "http://www.treasury.gov/resource-center/economic-policy/taxable-resources/Documents/TTR%20tables%202012.xlsx",
-                    "mediaType": "application/vnd.ms-excel",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.ms-excel"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/economic-policy/taxable-resources/Pages/Total-Taxable-Resources.aspx",
                     "downloadURL": "http://www.treasury.gov/resource-center/economic-policy/taxable-resources/Documents/tables%202011.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.ms-excel"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/economic-policy/taxable-resources/Pages/Total-Taxable-Resources.aspx",
                     "downloadURL": "http://www.treasury.gov/resource-center/economic-policy/taxable-resources/Documents/TTR%20tables%202014.xlsx",
-                    "mediaType": "application/vnd.ms-excel",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.ms-excel"
                 }
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "title": "Annual Estimates of Total Taxable Resources",
-            "description": "Under Public Law 102-321, the Department of Treasury is required to produce annual estimates of Total Taxable Resources (TTR), Treasury's estimates of the relative fiscal capacity of the states. TTR was developed as an outgrowth of a Congressionally mandated study on Federal, State, and local government fiscal relations entitled \"Federal-Sate-Local Fiscal Relations: Technical Papers, Vol. 2, Office of State and Local Finance, Department of Treasury, September 1986\".",
+            "identifier": "015-DO-053",
+            "issued": "1999-09-30T00:00:00",
             "keyword": [
                 "Total Taxable Resources",
                 "Annual Estimate",
                 "Annual Estimates Total Taxable Resources"
             ],
+            "landingPage": "http://www.treasury.gov/resource-center/economic-policy/taxable-resources/Pages/Total-Taxable-Resources.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2013-09-27",
+            "programCode": [
+                "015:003"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Office of Economic Policy",
-                "hasEmail": "mailto:digital@treasury.gov"
-            },
-            "accessLevel": "public",
-            "bureauCode": [
-                "015:00"
-            ],
-            "programCode": [
-                "015:003"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/resource-center/economic-policy/taxable-resources/Pages/Total-Taxable-Resources.aspx",
             "references": [
                 "http://www.treasury.gov/resource-center/economic-policy/taxable-resources/Pages/Total-Taxable-Resources.aspx"
             ],
-            "issued": "1999-09-30T00:00:00"
+            "title": "Annual Estimates of Total Taxable Resources"
         },
         {
             "@type": "dcat:Dataset",
-            "identifier": "015-DO-091",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "015:00"
+            ],
+            "contactPoint": {
+                "fn": "Department of the Treasury",
+                "hasEmail": "mailto:Digital@Treasury.gov"
+            },
+            "description": "Part A: The following articles by the Federal Reserve are about TIC data, or make significant use of TIC data.  Part B: The following statistics from the Bureau of Economic Analysis (BEA) use adjusted TIC data.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/articles.aspx",
                     "downloadURL": "http://www.treasury.gov/ticdata/Publish/shla2013r.pdf",
-                    "mediaType": "application/pdf",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/P3M",
-            "title": "Articles on the Treasury International Capital System (TIC)",
-            "description": "Part A: The following articles by the Federal Reserve are about TIC data, or make significant use of TIC data.  Part B: The following statistics from the Bureau of Economic Analysis (BEA) use adjusted TIC data.",
+            "identifier": "015-DO-091",
+            "issued": "2015-02-27T00:00:00",
             "keyword": [
                 "BEA",
                 "TIC",
                 "Federal Reserve",
                 "Bureau of Economic Analysis"
             ],
+            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/articles.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2014-08-19",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Department of the Treasury",
-                "hasEmail": "mailto:Digital@Treasury.gov"
+            "title": "Articles on the Treasury International Capital System (TIC)"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/articles.aspx",
-            "issued": "2015-02-27T00:00:00"
+            "contactPoint": {
+                "fn": "Office of Debt Management",
+                "hasEmail": "mailto:Debt.Management@treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-043",
+            "description": "The table provides the following data: issue date, coupon or auction high rate, security type, cusip, maturity date, total issue amount and various designated investor class categories.  This table provides investor class allotments for marketable Treasury bill auctions. Data are ordered by issue date.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/Pages/investor_class_auction.aspx",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/Documents/Website%20IC%20allotments---Bills--Aug%202001-Sep%202009.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.ms-excel"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/Pages/investor_class_auction.aspx",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/Documents/August%207_2014%20IC%20Bills.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.ms-excel"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "Auction Allotments By Investor Class For Marketable Treasury Bill Securities",
-            "description": "The table provides the following data: issue date, coupon or auction high rate, security type, cusip, maturity date, total issue amount and various designated investor class categories.  This table provides investor class allotments for marketable Treasury bill auctions. Data are ordered by issue date.",
+            "identifier": "015-DO-043",
+            "issued": "2014-08-31T00:00:00",
             "keyword": [
                 "Investor Class Auction Allotments",
                 "Treasury Bills"
             ],
+            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/Pages/investor_class_auction.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2009-09-30",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Office of Debt Management",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Office of Debt Management"
-            },
-            "contactPoint": {
-                "fn": "Office of Debt Management",
-                "hasEmail": "mailto:Debt.Management@treasury.gov"
+            "title": "Auction Allotments By Investor Class For Marketable Treasury Bill Securities"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/Pages/investor_class_auction.aspx",
-            "issued": "2014-08-31T00:00:00"
+            "contactPoint": {
+                "fn": "Office of Debt Management",
+                "hasEmail": "mailto:Debt.Management@treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-042",
+            "description": "Data are ordered by issue date. The table provides the following data: issue date, coupon or auction high rate, security type, cusip, maturity date, total issue amount and various designated investor class categories.  This table provides investor class allotments for marketable Treasury coupon auctions. Data are ordered by issue date. This table was previously published as the PDO-4 table in the quarterly Treasury Bulletin.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/Pages/investor_class_auction.aspx",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/Documents/Website%20PDO-4-A-Coupons%20Jan%202000-Sep%202009.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.ms-excel"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/Pages/investor_class_auction.aspx",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/Documents/November%2024_2014%20IC%20Coupons.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.ms-excel"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "Auction Allotments By Investor Class For Marketable Treasury Coupon Securities",
-            "description": "Data are ordered by issue date. The table provides the following data: issue date, coupon or auction high rate, security type, cusip, maturity date, total issue amount and various designated investor class categories.  This table provides investor class allotments for marketable Treasury coupon auctions. Data are ordered by issue date. This table was previously published as the PDO-4 table in the quarterly Treasury Bulletin.",
+            "identifier": "015-DO-042",
+            "issued": "2014-08-31T00:00:00",
             "keyword": [
                 "Investor Class Auction Allotments",
                 "Treasury Coupons"
             ],
+            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/Pages/investor_class_auction.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2009-09-30",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Office of Debt Management",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Office of Debt Management"
-            },
-            "contactPoint": {
-                "fn": "Office of Debt Management",
-                "hasEmail": "mailto:Debt.Management@treasury.gov"
+            "title": "Auction Allotments By Investor Class For Marketable Treasury Coupon Securities"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/Pages/investor_class_auction.aspx",
-            "issued": "2014-08-31T00:00:00"
+            "contactPoint": {
+                "fn": "James Kostiw",
+                "hasEmail": "mailto:o_f_a_c@do.treas.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-131",
+            "describedBy": "https://www.treasury.gov/ofac/downloads/sanctions/1.0/sdn_advanced.xsd",
+            "description": "To make it easier to comply with OFAC's sanctions regulations, OFAC offers all of its non-SDN sanctions lists in a consolidated set of data files \"the Consolidated Sanctions List\".  These consolidated files comply with all OFAC's existing data standards.  In the future, if OFAC creates a new non-SDN style list, the office will add the new data associated with that list to these consolidated data files if appropriate.  While the consolidated sanctions list data files are not part of OFAC's list of Specially Designated Nationals and Blocked Persons \"the SDN List,\" the records in these consolidated files may also appear on the SDN List. 02262021",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.treasury.gov/ofac/downloads/sanctions/1.0/sdn_advanced.xsd",
                     "describedByType": "text/xml",
                     "downloadURL": "https://www.treasury.gov/ofac/downloads/sanctions/1.0/cons_advanced.xml",
-                    "mediaType": "text/xml",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/xml"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Consolidated (non-SDN) Sanctions List",
-            "description": "To make it easier to comply with OFAC's sanctions regulations, OFAC offers all of its non-SDN sanctions lists in a consolidated set of data files \"the Consolidated Sanctions List\".  These consolidated files comply with all OFAC's existing data standards.  In the future, if OFAC creates a new non-SDN style list, the office will add the new data associated with that list to these consolidated data files if appropriate.  While the consolidated sanctions list data files are not part of OFAC's list of Specially Designated Nationals and Blocked Persons \"the SDN List,\" the records in these consolidated files may also appear on the SDN List. 02262021",
+            "identifier": "015-DO-131",
             "keyword": [
                 "OFAC",
                 "Office of Foreign Assets Control",
@@ -693,50 +700,50 @@
                 "non-SDN sanctions list",
                 "sanctions list"
             ],
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2018-08-15",
+            "programCode": [
+                "015:004"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Office of Foreign Assets Control",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Office of Foreign Assets Control"
-            },
-            "contactPoint": {
-                "fn": "James Kostiw",
-                "hasEmail": "mailto:o_f_a_c@do.treas.gov"
-            },
-            "accessLevel": "public",
-            "bureauCode": [
-                "015:00"
-            ],
-            "programCode": [
-                "015:004"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "describedBy": "https://www.treasury.gov/ofac/downloads/sanctions/1.0/sdn_advanced.xsd",
             "references": [
                 "https://www.treasury.gov/resource-center/sanctions/SDN-List/Documents/sdn_advanced_notes.pdf",
                 "https://www.treasury.gov/resource-center/sanctions/SDN-List/Pages/consolidated.aspx"
-            ]
+            ],
+            "title": "Consolidated (non-SDN) Sanctions List"
         },
         {
             "@type": "dcat:Dataset",
-            "identifier": "015-DO-037",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "015:00"
+            ],
+            "contactPoint": {
+                "fn": "Office of Debt Management",
+                "hasEmail": "mailto:debt.management@do.treas.gov"
+            },
+            "description": "These rates are the daily secondary market quotation on the most recently auctioned Treasury Bills for each maturity tranche (4-week, 13-week, 26-week, and 52-week) that Treasury currently issues new Bills. Market quotations are obtained at approximately 3:30 PM each business day by the Federal Reserve Bank of New York. The Bank Discount rate is the rate at which a Bill is quoted in the secondary market and is based on the par value, amount of the discount and a 360-day year. The Coupon Equivalent, also called the Bond Equivalent, or the Investment Yield, is the bill's yield based on the purchase price, discount, and a 365- or 366-day year. The Coupon Equivalent can be used to compare the yield on a discount bill to the yield on a nominal coupon bond that pays semiannual interest.  Data updated daily on weekdays.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx?data=billrates",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1D",
-            "title": "Daily Treasury Bill Rates Data",
-            "description": "These rates are the daily secondary market quotation on the most recently auctioned Treasury Bills for each maturity tranche (4-week, 13-week, 26-week, and 52-week) that Treasury currently issues new Bills. Market quotations are obtained at approximately 3:30 PM each business day by the Federal Reserve Bank of New York. The Bank Discount rate is the rate at which a Bill is quoted in the secondary market and is based on the par value, amount of the discount and a 360-day year. The Coupon Equivalent, also called the Bond Equivalent, or the Investment Yield, is the bill's yield based on the purchase price, discount, and a 365- or 366-day year. The Coupon Equivalent can be used to compare the yield on a discount bill to the yield on a nominal coupon bond that pays semiannual interest.  Data updated daily on weekdays.",
+            "identifier": "015-DO-037",
+            "issued": "2014-08-31T00:00:00",
             "keyword": [
                 "Treasury Bills",
                 "T Bills",
@@ -751,46 +758,46 @@
                 "Investment Yield",
                 "Maturity Tranche. May 2019"
             ],
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2019-05-06",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Federal Reserve Bank of New York",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Federal Reserve Bank of New York"
-            },
-            "contactPoint": {
-                "fn": "Office of Debt Management",
-                "hasEmail": "mailto:debt.management@do.treas.gov"
+            "title": "Daily Treasury Bill Rates Data"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "issued": "2014-08-31T00:00:00"
+            "contactPoint": {
+                "fn": "Office of Debt Management",
+                "hasEmail": "mailto:debt.management@do.treas.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-038",
+            "description": "The Long-Term Composite Rate is the unweighted average of bid yields on all outstanding fixed-coupon bonds neither due nor callable in less than 10 years.  Dataset updated daily every weekday.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx?data=longtermrate",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1D",
-            "title": "Daily Treasury Long Term Rate Data",
-            "description": "The Long-Term Composite Rate is the unweighted average of bid yields on all outstanding fixed-coupon bonds neither due nor callable in less than 10 years.  Dataset updated daily every weekday.",
+            "identifier": "015-DO-038",
+            "issued": "2014-08-31T00:00:00",
             "keyword": [
                 "Long Term Rate",
                 "LT Composite",
@@ -803,46 +810,46 @@
                 "unweighted average of bid yields",
                 "non callable bonds"
             ],
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2014-08-18",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Office of Debt Management",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Office of Debt Management"
-            },
-            "contactPoint": {
-                "fn": "Office of Debt Management",
-                "hasEmail": "mailto:debt.management@do.treas.gov"
+            "title": "Daily Treasury Long Term Rate Data"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "issued": "2014-08-31T00:00:00"
+            "contactPoint": {
+                "fn": "Office of Debt Managment",
+                "hasEmail": "mailto:debt.management@do.treas.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-039",
+            "description": "The Long-Term Real Rate Average is the unweighted average of bid real yields on all outstanding TIPS with remaing maturities of more than 10 years and is intended as a proxy for long-term real rates.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx?data=reallongtermrate",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1D",
-            "title": "Daily Treasury Real Long Term Rates",
-            "description": "The Long-Term Real Rate Average is the unweighted average of bid real yields on all outstanding TIPS with remaing maturities of more than 10 years and is intended as a proxy for long-term real rates.",
+            "identifier": "015-DO-039",
+            "issued": "2014-08-31T00:00:00",
             "keyword": [
                 "Long Term Real Rate Average",
                 "unweighted average",
@@ -851,46 +858,46 @@
                 "Maturities",
                 "LT Real Average (10> yrs)"
             ],
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2014-08-18",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Office of Debt Management",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Office of Debt Management"
-            },
-            "contactPoint": {
-                "fn": "Office of Debt Managment",
-                "hasEmail": "mailto:debt.management@do.treas.gov"
+            "title": "Daily Treasury Real Long Term Rates"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "issued": "2014-08-31T00:00:00"
+            "contactPoint": {
+                "fn": "Office of Debt Management",
+                "hasEmail": "mailto:debt.management@do.treas.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-036",
+            "description": "These rates are commonly referred to as \"Real Constant Maturity Treasury\" rates, or R-CMTs. Real yields on Treasury Inflation Protected Securities (TIPS) at \"constant maturity\" are interpolated by the U.S. Treasury from Treasury's daily real yield curve. These real market yields are calculated from composites of secondary market quotations obtained by the Federal Reserve Bank of New York. The real yield values are read from the real yield curve at fixed maturities, currently 5, 7, 10, 20, and 30 years. This method provides a real yield for a 10 year maturity, for example, even if no outstanding security has exactly 10 years remaining to maturity.  Dataset updated daily every weekday.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx?data=realyield",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1D",
-            "title": "Daily Treasury Real Yield Curve Rates",
-            "description": "These rates are commonly referred to as \"Real Constant Maturity Treasury\" rates, or R-CMTs. Real yields on Treasury Inflation Protected Securities (TIPS) at \"constant maturity\" are interpolated by the U.S. Treasury from Treasury's daily real yield curve. These real market yields are calculated from composites of secondary market quotations obtained by the Federal Reserve Bank of New York. The real yield values are read from the real yield curve at fixed maturities, currently 5, 7, 10, 20, and 30 years. This method provides a real yield for a 10 year maturity, for example, even if no outstanding security has exactly 10 years remaining to maturity.  Dataset updated daily every weekday.",
+            "identifier": "015-DO-036",
+            "issued": "2014-08-18T00:00:00",
             "keyword": [
                 "Real Yield",
                 "Curve Rates",
@@ -904,46 +911,46 @@
                 "R-CMTs",
                 "TIPS"
             ],
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2014-08-18",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Office of Debt Management",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Office of Debt Management"
-            },
-            "contactPoint": {
-                "fn": "Office of Debt Management",
-                "hasEmail": "mailto:debt.management@do.treas.gov"
+            "title": "Daily Treasury Real Yield Curve Rates"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "issued": "2014-08-18T00:00:00"
+            "contactPoint": {
+                "fn": "Office of Debt Management",
+                "hasEmail": "mailto:debt.management@do.treas.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-035",
+            "description": "These rates are commonly referred to as \"Constant Maturity Treasury\" rates, or CMTs. Yields are interpolated by the Treasury from the daily yield curve. This curve, which relates the yield on a security to its time to maturity is based on the closing market bid yields on actively traded Treasury securities in the over-the-counter market. These market yields are calculated from composites of quotations obtained by the Federal Reserve Bank of New York. The yield values are read from the yield curve at fixed maturities, currently 1, 3 and 6 months and 1, 2, 3, 5, 7, 10, 20, and 30 years. This method provides a yield for a 10 year maturity, for example, even if no outstanding security has exactly 10 years remaining to maturity.  Dataset is updated daily from Monday to Friday",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx?data=yield",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1D",
-            "title": "Daily Treasury Yield Curve Dates",
-            "description": "These rates are commonly referred to as \"Constant Maturity Treasury\" rates, or CMTs. Yields are interpolated by the Treasury from the daily yield curve. This curve, which relates the yield on a security to its time to maturity is based on the closing market bid yields on actively traded Treasury securities in the over-the-counter market. These market yields are calculated from composites of quotations obtained by the Federal Reserve Bank of New York. The yield values are read from the yield curve at fixed maturities, currently 1, 3 and 6 months and 1, 2, 3, 5, 7, 10, 20, and 30 years. This method provides a yield for a 10 year maturity, for example, even if no outstanding security has exactly 10 years remaining to maturity.  Dataset is updated daily from Monday to Friday",
+            "identifier": "015-DO-035",
+            "issued": "2014-08-31T00:00:00",
             "keyword": [
                 "Daily Yield",
                 "Curve Rates",
@@ -961,47 +968,46 @@
                 "Constant Maturity",
                 "CMTs"
             ],
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2014-08-18",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Office of Debt Management",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Office of Debt Management"
-            },
-            "contactPoint": {
-                "fn": "Office of Debt Management",
-                "hasEmail": "mailto:debt.management@do.treas.gov"
+            "title": "Daily Treasury Yield Curve Dates"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "issued": "2014-08-31T00:00:00"
+            "contactPoint": {
+                "fn": "Office of Debt Management",
+                "hasEmail": "mailto:digital@treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-021",
+            "description": "These rates are the daily secondary market quotation on the most recently auctioned Treasury Bills for each maturity tranche (4-week, 13-week, 26-week, and 52-week) that Treasury currently issues new Bills. Market quotations are obtained at approximately 3:30 PM each business day by the Federal Reserve Bank of New York. The Bank Discount rate is the rate at which a Bill is quoted in the secondary market and is based on the par value, amount of the discount and a 360-day year. The Coupon Equivalent, also called the Bond Equivalent, or the Investment Yield, is the bill's yield based on the purchase price, discount, and a 365- or 366-day year. The Coupon Equivalent can be used to compare the yield on a discount bill to the yield on a nominal coupon bond that pays semiannual interest.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx?data=billrates",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx?data=billrates",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1D",
-            "title": "Interest Rate Statistics - Daily Treasury Bill Rates",
-            "description": "These rates are the daily secondary market quotation on the most recently auctioned Treasury Bills for each maturity tranche (4-week, 13-week, 26-week, and 52-week) that Treasury currently issues new Bills. Market quotations are obtained at approximately 3:30 PM each business day by the Federal Reserve Bank of New York. The Bank Discount rate is the rate at which a Bill is quoted in the secondary market and is based on the par value, amount of the discount and a 360-day year. The Coupon Equivalent, also called the Bond Equivalent, or the Investment Yield, is the bill's yield based on the purchase price, discount, and a 365- or 366-day year. The Coupon Equivalent can be used to compare the yield on a discount bill to the yield on a nominal coupon bond that pays semiannual interest.",
+            "identifier": "015-DO-021",
             "keyword": [
                 "statistics",
                 "interest",
@@ -1012,94 +1018,94 @@
                 "real yield curve",
                 "interest rates"
             ],
+            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx?data=billrates",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2023-12-08",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Office of Debt Management",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Office of Debt Management"
-            },
-            "contactPoint": {
-                "fn": "Office of Debt Management",
-                "hasEmail": "mailto:digital@treasury.gov"
+            "title": "Interest Rate Statistics - Daily Treasury Bill Rates"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx?data=billrates"
+            "contactPoint": {
+                "fn": "Office of Debt Management",
+                "hasEmail": "mailto:digital@treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-022",
+            "description": "Long Term Real Rate Average: The Long-Term Real Rate Average is the unweighted average of bid real yields on all outstanding TIPS with remaing maturities of more than 10 years and is intended as a proxy for long-term real rates.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx?data=reallongtermrate",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx?data=reallongtermrate",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Interest Rate Statistics - Daily Treasury Real Long Term Rate Averages",
-            "description": "Long Term Real Rate Average: The Long-Term Real Rate Average is the unweighted average of bid real yields on all outstanding TIPS with remaing maturities of more than 10 years and is intended as a proxy for long-term real rates.",
+            "identifier": "015-DO-022",
             "keyword": [
                 "long term real average rate",
                 "unweighted",
                 "lt",
                 "bid"
             ],
+            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx?data=reallongtermrate",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2023-12-08",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Office of Debt Management",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Office of Debt Management"
-            },
-            "contactPoint": {
-                "fn": "Office of Debt Management",
-                "hasEmail": "mailto:digital@treasury.gov"
+            "title": "Interest Rate Statistics - Daily Treasury Real Long Term Rate Averages"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx?data=reallongtermrate"
+            "contactPoint": {
+                "fn": "Office of Debt Management",
+                "hasEmail": "mailto:digital@treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-020",
+            "description": "These rates are commonly referred to as Constant Maturity Treasury rates, or CMTs. Yields are interpolated by the Treasury from the daily yield curve. This curve, which relates the yield on a security to its time to maturity is based on the closing market bid yields on actively traded Treasury securities in the over-the-counter market. These market yields are calculated from composites of quotations obtained by the Federal Reserve Bank of New York. The yield values are read from the yield curve at fixed maturities, currently 1, 3 and 6 months and 1, 2, 3, 5, 7, 10, 20, and 30 years. This method provides a yield for a 10 year maturity, for example, even if no outstanding security has exactly 10 years remaining to maturity.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx?data=yield",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx?data=yield",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1D",
-            "title": "Interest Rate Statistics - Daily Treasury Yield Curve Rates",
-            "description": "These rates are commonly referred to as Constant Maturity Treasury rates, or CMTs. Yields are interpolated by the Treasury from the daily yield curve. This curve, which relates the yield on a security to its time to maturity is based on the closing market bid yields on actively traded Treasury securities in the over-the-counter market. These market yields are calculated from composites of quotations obtained by the Federal Reserve Bank of New York. The yield values are read from the yield curve at fixed maturities, currently 1, 3 and 6 months and 1, 2, 3, 5, 7, 10, 20, and 30 years. This method provides a yield for a 10 year maturity, for example, even if no outstanding security has exactly 10 years remaining to maturity.",
+            "identifier": "015-DO-020",
             "keyword": [
                 "statistics",
                 "interest",
@@ -1110,47 +1116,48 @@
                 "real yield curve",
                 "interest rates"
             ],
+            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx?data=yield",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2023-12-08",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Office of Debt Management",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Office of Debt Management"
-            },
-            "contactPoint": {
-                "fn": "Office of Debt Management",
-                "hasEmail": "mailto:digital@treasury.gov"
+            "title": "Interest Rate Statistics - Daily Treasury Yield Curve Rates"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx?data=yield"
+            "contactPoint": {
+                "fn": "Department of the Treasury",
+                "hasEmail": "mailto:Digital@Treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-123",
+            "description": "This Sixth Tranche Report to Congress meets the requirement for reporting at the $350 billion commitment level under section 105(b) of the Emergency Economic Stabilization Act of 2008 (EESA).  Recent transactions under the Auto Supplier Support Program, Consumer and Business Lending Initiative, Home Affordable Modification Program, and Systemically Significant Failing Institutions Program, when combined with $3.6 billion of transactions under the Capital Purchase Program, bring the total investment amount to $376.7 billion as April 17, 2009. Treasury will submit the next report when transactions reach the $400 billion level.\r\n\r\nThe Report addresses the following six areas:\r\n\r\n\u2022   A description of all the transactions made during the reporting period.\r\n\u2022   A description of the pricing mechanism for the transactions.\r\n\u2022   A justification of the price paid for, and other financial terms associated with, the \r\ntransactions.\r\n\u2022   A description of the impact of the exercise of such authority on the financial system.\r\n\u2022   A description of the challenges that remain in the financial system, including any benchmarks \r\nyet to be achieved.\r\n\u2022   An estimate of additional actions under the authority provided pursuant to the EESA that may be \r\nnecessary to address such challenges.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/Other-Reports.aspx",
                     "downloadURL": "https://www.treasury.gov/initiatives/financial-stability/reports/Documents/TARP%20Cost%20Estimates%20-%20March%2031%202010.pdf",
-                    "mediaType": "application/pdf",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Lastest TARP Reports:  Tranche Report",
-            "description": "This Sixth Tranche Report to Congress meets the requirement for reporting at the $350 billion commitment level under section 105(b) of the Emergency Economic Stabilization Act of 2008 (EESA).  Recent transactions under the Auto Supplier Support Program, Consumer and Business Lending Initiative, Home Affordable Modification Program, and Systemically Significant Failing Institutions Program, when combined with $3.6 billion of transactions under the Capital Purchase Program, bring the total investment amount to $376.7 billion as April 17, 2009. Treasury will submit the next report when transactions reach the $400 billion level.\r\n\r\nThe Report addresses the following six areas:\r\n\r\n\u2022   A description of all the transactions made during the reporting period.\r\n\u2022   A description of the pricing mechanism for the transactions.\r\n\u2022   A justification of the price paid for, and other financial terms associated with, the \r\ntransactions.\r\n\u2022   A description of the impact of the exercise of such authority on the financial system.\r\n\u2022   A description of the challenges that remain in the financial system, including any benchmarks \r\nyet to be achieved.\r\n\u2022   An estimate of additional actions under the authority provided pursuant to the EESA that may be \r\nnecessary to address such challenges.",
+            "identifier": "015-DO-123",
+            "issued": "2015-05-29T00:00:00",
             "keyword": [
                 "TARP",
                 "Tranche Report",
@@ -1158,54 +1165,54 @@
                 "EESA",
                 "CPP"
             ],
+            "landingPage": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/Other-Reports.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2009-04-24",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Department of the Treasury",
-                "hasEmail": "mailto:Digital@Treasury.gov"
+            "title": "Lastest TARP Reports:  Tranche Report"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/Other-Reports.aspx",
-            "issued": "2015-05-29T00:00:00"
+            "contactPoint": {
+                "fn": "Department of the Treasury",
+                "hasEmail": "mailto:Digital@Treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-104",
+            "description": "This report is a cumulative survey, sourced from the Monthly Servicer Survey, of HAMP application activity and complies with Section 1483 of the Dodd-Frank Wall Street Reform and Consumer Protection Act. It shows the number of requests received, processed, approved, and denied by each servicer for each month and program to date.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/HAMP-Servicer.aspx",
                     "downloadURL": "https://www.treasury.gov/initiatives/financial-stability/reports/Documents/revised%20HAMP%20Application%20Activity%20by%20Servicer%20December%202017.pdf",
-                    "mediaType": "application/pdf",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/pdf"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/HAMP-Servicer.aspx",
                     "downloadURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Documents/February%20HAMP%20Application%20Activity%20by%20Servicer.pdf",
-                    "mediaType": "application/pdf",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "Latest TARP Report:  HAMP Application Activity by Servicer",
-            "description": "This report is a cumulative survey, sourced from the Monthly Servicer Survey, of HAMP application activity and complies with Section 1483 of the Dodd-Frank Wall Street Reform and Consumer Protection Act. It shows the number of requests received, processed, approved, and denied by each servicer for each month and program to date.",
+            "identifier": "015-DO-104",
+            "issued": "2015-05-29T00:00:00",
             "keyword": [
                 "TARP",
                 "HAMP",
@@ -1214,48 +1221,48 @@
                 "Dodd-Frank",
                 "Wall Street Reform"
             ],
+            "landingPage": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/HAMP-Servicer.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2015-04-29",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Department of the Treasury",
-                "hasEmail": "mailto:Digital@Treasury.gov"
+            "title": "Latest TARP Report:  HAMP Application Activity by Servicer"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/HAMP-Servicer.aspx",
-            "issued": "2015-05-29T00:00:00"
+            "contactPoint": {
+                "fn": "Department of the Treasury",
+                "hasEmail": "mailto:Digital@Treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-108",
+            "description": "The Summary presents the latest information about the HHF program in each of the 18 states and the District of Columbia, including the number of homeowners who have received assistance as well as trends in the local area housing market.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/HHF.aspx",
                     "downloadURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Documents/Q4%202014%20Hardest%20Hit%20Fund%20Program%20Performance%20Summary.pdf",
-                    "mediaType": "application/pdf",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/P3M",
-            "title": "Latest TARP Report:  Hardest Hit Fund Performance Summary",
-            "description": "The Summary presents the latest information about the HHF program in each of the 18 states and the District of Columbia, including the number of homeowners who have received assistance as well as trends in the local area housing market.",
+            "identifier": "015-DO-108",
+            "issued": "2015-05-29T00:00:00",
             "keyword": [
                 "TARP",
                 "HHF",
@@ -1263,48 +1270,48 @@
                 "DC",
                 "Housing Market"
             ],
+            "landingPage": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/HHF.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2015-03-11",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Department of the Treasury",
-                "hasEmail": "mailto:Digital@Treasury.gov"
+            "title": "Latest TARP Report:  Hardest Hit Fund Performance Summary"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/HHF.aspx",
-            "issued": "2015-05-29T00:00:00"
+            "contactPoint": {
+                "fn": "Department of the Treasury",
+                "hasEmail": "mailto:Digital@Treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-109",
+            "description": "Quarterly reports of housing funding showing, delinquency rate, demographics, borrower income and other pertinent borrower information.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/Housing-Finance-Agency-Aggregate-Report.aspx",
                     "downloadURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Documents/HFA%20Aggregate%20Q42014%20Report.pdf",
-                    "mediaType": "application/pdf",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/P3M",
-            "title": "Latest TARP Report:  Housing Finance Agency (HFA) Aggregate Report",
-            "description": "Quarterly reports of housing funding showing, delinquency rate, demographics, borrower income and other pertinent borrower information.",
+            "identifier": "015-DO-109",
+            "issued": "2015-05-29T00:00:00",
             "keyword": [
                 "TARP",
                 "Housing Finance Agency",
@@ -1314,48 +1321,48 @@
                 "loans",
                 "mortgage"
             ],
+            "landingPage": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/Housing-Finance-Agency-Aggregate-Report.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2015-03-30",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Department of the Treasury",
-                "hasEmail": "mailto:Digital@Treasury.gov"
+            "title": "Latest TARP Report:  Housing Finance Agency (HFA) Aggregate Report"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/Housing-Finance-Agency-Aggregate-Report.aspx",
-            "issued": "2015-05-29T00:00:00"
+            "contactPoint": {
+                "fn": "Department of the Treasury",
+                "hasEmail": "mailto:Digital@Treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-116",
+            "description": "This one-time report to Congress provided information on the Asset Guarantee Program, in compliance with a requirement to report within 90 days on the establishment of any insurance program under Section 102(a) of EESA.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/Section-102-Report.aspx",
                     "downloadURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Documents/sec102ReportToCongress.pdf",
-                    "mediaType": "application/pdf",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Latest TARP Report: Section 102 Report (December 31, 2008)",
-            "description": "This one-time report to Congress provided information on the Asset Guarantee Program, in compliance with a requirement to report within 90 days on the establishment of any insurance program under Section 102(a) of EESA.",
+            "identifier": "015-DO-116",
+            "issued": "2015-05-29T00:00:00",
             "keyword": [
                 "EESA",
                 "TARP",
@@ -1363,95 +1370,95 @@
                 "Asset Guarantee Program",
                 "Congress"
             ],
+            "landingPage": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/Section-102-Report.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2012-07-13",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Department of the Treasury",
-                "hasEmail": "mailto:Digital@Treasury.gov"
+            "title": "Latest TARP Report: Section 102 Report (December 31, 2008)"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P6M",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/Section-102-Report.aspx",
-            "issued": "2015-05-29T00:00:00"
+            "contactPoint": {
+                "fn": "Department of the Treasury",
+                "hasEmail": "mailto:Digital@treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-120",
+            "description": "These periodic reports provide details on the sale of warrants, which includes information on auctions as well as on how the sale price was determined in the case of any repurchase of warrants by a TARP recipient. These reports are generally published every six months.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/Warrant-Disposition-Reports.aspx",
                     "downloadURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Documents/December%202012%20Warrant%20Disposition%20Report.pdf",
-                    "mediaType": "application/pdf",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/P6M",
-            "title": "Latest TARP Reports:   Warrant Disposition Reports",
-            "description": "These periodic reports provide details on the sale of warrants, which includes information on auctions as well as on how the sale price was determined in the case of any repurchase of warrants by a TARP recipient. These reports are generally published every six months.",
+            "identifier": "015-DO-120",
+            "issued": "2015-05-29T00:00:00",
             "keyword": [
                 "TARP",
                 "Warrant Disposition",
                 "CPP"
             ],
+            "landingPage": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/Warrant-Disposition-Reports.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2013-03-13",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Department of the Treasury",
-                "hasEmail": "mailto:Digital@treasury.gov"
+            "title": "Latest TARP Reports:   Warrant Disposition Reports"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/Warrant-Disposition-Reports.aspx",
-            "issued": "2015-05-29T00:00:00"
+            "contactPoint": {
+                "fn": "Department of the Treasury",
+                "hasEmail": "mailto:Digital@Treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-113",
+            "description": "These annual reports contain the financial statements for TARP, the Government Accountability Office's (GAO) audit opinion on those financial statements, a separate opinion on OFS' internal controls over financial reporting, and results of GAO's tests of OFS' compliance with selected laws and regulations. The AFR is produced annually for the prior fiscal year and released during the last quarter of the calendar year.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/Annual-Agency-Financial-Reports.aspx",
                     "downloadURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Documents/FY2014%20OFS%20AFR%20FINAL%20-%20Nov%206%202014.pdf",
-                    "mediaType": "application/pdf",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "title": "Latest TARP Reports:  Annual Agency Financial Report",
-            "description": "These annual reports contain the financial statements for TARP, the Government Accountability Office's (GAO) audit opinion on those financial statements, a separate opinion on OFS' internal controls over financial reporting, and results of GAO's tests of OFS' compliance with selected laws and regulations. The AFR is produced annually for the prior fiscal year and released during the last quarter of the calendar year.",
+            "identifier": "015-DO-113",
+            "issued": "2015-05-29T00:00:00",
             "keyword": [
                 "TARP",
                 "GAO",
@@ -1459,96 +1466,96 @@
                 "AFR",
                 "Annual Agency Financial Report"
             ],
+            "landingPage": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/Annual-Agency-Financial-Reports.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2014-11-07",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Department of the Treasury",
-                "hasEmail": "mailto:Digital@Treasury.gov"
+            "title": "Latest TARP Reports:  Annual Agency Financial Report"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/Annual-Agency-Financial-Reports.aspx",
-            "issued": "2015-05-29T00:00:00"
+            "contactPoint": {
+                "fn": "Department of the Treasury",
+                "hasEmail": "mailto:Digital@Treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-121",
+            "description": "The purpose of this special report is to review the implementation of the SPOC requirement by the largest servicers participating in MHA. This report is intended to serve as a basis for a broader discussion on how the SPOC requirement can best be implemented for all servicers, not only those participating in MHA, so that communication between the homeowner and servicer can be improved from the dismal conditions that marked the beginning of the crisis.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/Other-Reports.aspx",
                     "downloadURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Documents/SPOC%20Special%20Report_Final.pdf",
-                    "mediaType": "application/pdf",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Latest TARP Reports:  Making Contact: The Path to Improving Mortgage Industry Communication with Homeowners",
-            "description": "The purpose of this special report is to review the implementation of the SPOC requirement by the largest servicers participating in MHA. This report is intended to serve as a basis for a broader discussion on how the SPOC requirement can best be implemented for all servicers, not only those participating in MHA, so that communication between the homeowner and servicer can be improved from the dismal conditions that marked the beginning of the crisis.",
+            "identifier": "015-DO-121",
+            "issued": "2015-05-29T00:00:00",
             "keyword": [
                 "TARP",
                 "Mortgage Industry",
                 "MHA",
                 "Making Home Affordable"
             ],
+            "landingPage": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/Other-Reports.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2012-11-14",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Department of the Treasury",
-                "hasEmail": "mailto:Digital@Treasury.gov"
+            "title": "Latest TARP Reports:  Making Contact: The Path to Improving Mortgage Industry Communication with Homeowners"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/Other-Reports.aspx",
-            "issued": "2015-05-29T00:00:00"
+            "contactPoint": {
+                "fn": "Department of the Treasury",
+                "hasEmail": "mailto:Digital@Treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-110",
+            "description": "The Making Home Affordable Program Performance Report, which provides detailed metrics on the Making Home Affordable (MHA) Program is changing from a monthly report to a quarterly release. The last monthly report was for May 2014. Each quarterly report will contain the detailed assessments of the performance of servicers participating in the Making Home Affordable program. Treasury provides information about servicer performance through two types of data: \r\n\u2022Compliance data, which reflects servicer compliance with specific MHA guidelines; and\r\n\u2022Program results data, which reflects how timely and effectively servicers assist eligible homeowners and report program activity.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/Making-Home-Affordable-Program-Performance-Report.aspx",
                     "downloadURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Documents/4Q14%20Quarterly%20MHA%20Report%20Final3.pdf",
-                    "mediaType": "application/pdf",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/P3M",
-            "title": "Latest TARP Reports:  Making Home Affordable Program Performance Report",
-            "description": "The Making Home Affordable Program Performance Report, which provides detailed metrics on the Making Home Affordable (MHA) Program is changing from a monthly report to a quarterly release. The last monthly report was for May 2014. Each quarterly report will contain the detailed assessments of the performance of servicers participating in the Making Home Affordable program. Treasury provides information about servicer performance through two types of data: \r\n\u2022Compliance data, which reflects servicer compliance with specific MHA guidelines; and\r\n\u2022Program results data, which reflects how timely and effectively servicers assist eligible homeowners and report program activity.",
+            "identifier": "015-DO-110",
+            "issued": "2015-05-29T00:00:00",
             "keyword": [
                 "TARP",
                 "Making Home Affordable",
@@ -1556,48 +1563,48 @@
                 "Servicer Performance",
                 "Homeowners"
             ],
+            "landingPage": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/Making-Home-Affordable-Program-Performance-Report.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2015-03-11",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Department of the Treasury",
-                "hasEmail": "mailto:Digital@Treasury.gov"
+            "title": "Latest TARP Reports:  Making Home Affordable Program Performance Report"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/Making-Home-Affordable-Program-Performance-Report.aspx",
-            "issued": "2015-05-29T00:00:00"
+            "contactPoint": {
+                "fn": "Department of the Treasury",
+                "hasEmail": "mailto:Digital@Treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-111",
+            "description": "OFS's authority to make new financial commitments under the Troubled Asset Relief Program (TARP) ended on October 3, 2010. Since then, OFS has\r\nfocused on winding down the remaining TARP investments in a manner that balances speed of exit with maximizing taxpayer returns. OFS also continues to\r\ntake actions to help homeowners prevent avoidable foreclosures.\r\nFor detailed information about OFS\u2019s progress in exiting its remaining TARP investments, please see the Monthly Report to Congress pursuant to section\r\n105(a) of the Emergency Economic Stabilization Act (EESA), available online at: http://www.treasury.gov/initiatives/financialstability/\r\nreports/Pages/Monthly-Report-to-Congress.aspx.\r\nFor detailed information about OFS\u2019s efforts to help homeowners prevent avoidable foreclosure, please see the Making Home Affordable Program\r\nPerformance Report, available online at: http://www.treasury.gov/initiatives/financial-stability/reports/Pages/Making-Home-Affordable-Program-\r\nPerformance-Report.aspx.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/Quarterly-Admin-Activity-Report.aspx",
                     "downloadURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Documents/OFS%20Admin%20Obligations%20BOC%20-%20Q1%20FY%2015.pdf",
-                    "mediaType": "application/pdf",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/P3M",
-            "title": "Latest TARP Reports:  OFS Quarterly Administrative Activity Report",
-            "description": "OFS's authority to make new financial commitments under the Troubled Asset Relief Program (TARP) ended on October 3, 2010. Since then, OFS has\r\nfocused on winding down the remaining TARP investments in a manner that balances speed of exit with maximizing taxpayer returns. OFS also continues to\r\ntake actions to help homeowners prevent avoidable foreclosures.\r\nFor detailed information about OFS\u2019s progress in exiting its remaining TARP investments, please see the Monthly Report to Congress pursuant to section\r\n105(a) of the Emergency Economic Stabilization Act (EESA), available online at: http://www.treasury.gov/initiatives/financialstability/\r\nreports/Pages/Monthly-Report-to-Congress.aspx.\r\nFor detailed information about OFS\u2019s efforts to help homeowners prevent avoidable foreclosure, please see the Making Home Affordable Program\r\nPerformance Report, available online at: http://www.treasury.gov/initiatives/financial-stability/reports/Pages/Making-Home-Affordable-Program-\r\nPerformance-Report.aspx.",
+            "identifier": "015-DO-111",
+            "issued": "2015-05-29T00:00:00",
             "keyword": [
                 "TARP",
                 "OFS",
@@ -1605,95 +1612,95 @@
                 "foreclosure",
                 "making home affordable"
             ],
+            "landingPage": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/Quarterly-Admin-Activity-Report.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2015-02-12",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Department of the Treasury",
-                "hasEmail": "mailto:Digital@Treasury.gov"
+            "title": "Latest TARP Reports:  OFS Quarterly Administrative Activity Report"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/Quarterly-Admin-Activity-Report.aspx",
-            "issued": "2015-05-29T00:00:00"
+            "contactPoint": {
+                "fn": "Department of the Treasury",
+                "hasEmail": "mailto:Digtail@Treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-112",
+            "description": "Treasury produced a quarterly report on PPIP through September 2013 that provided detailed information on the funds, their investments, and returns. It was typically released within one month after the end of each quarter.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/Public-Private-Investment-Program-Quarterly-Report.aspx",
                     "downloadURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Documents/External%20Report%2013%20-9%20Final.pdf",
-                    "mediaType": "application/pdf",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/P3M",
-            "title": "Latest TARP Reports:  Public Private Investment Program Quarterly Report",
-            "description": "Treasury produced a quarterly report on PPIP through September 2013 that provided detailed information on the funds, their investments, and returns. It was typically released within one month after the end of each quarter.",
+            "identifier": "015-DO-112",
+            "issued": "2015-05-29T00:00:00",
             "keyword": [
                 "TARP",
                 "Public Private Investment Program",
                 "PPIP"
             ],
+            "landingPage": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/Public-Private-Investment-Program-Quarterly-Report.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2013-10-28",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Department of the Treasury",
-                "hasEmail": "mailto:Digtail@Treasury.gov"
+            "title": "Latest TARP Reports:  Public Private Investment Program Quarterly Report"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/Public-Private-Investment-Program-Quarterly-Report.aspx",
-            "issued": "2015-05-29T00:00:00"
+            "contactPoint": {
+                "fn": "Department of the Treasury",
+                "hasEmail": "mailto:Digital@Treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-115",
+            "description": "Treasury has produced retrospective reports on TARP covering each of the last three years. These reports provide comprehensive information on the milestones achieved during the previous year by each TARP program, as well as TARP as a whole.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/TARP-Annual-Retrospectives.aspx",
                     "downloadURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Documents/TARP%20Four%20Year%20Retrospective%20Report.pdf",
-                    "mediaType": "application/pdf",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "title": "Latest TARP Reports:  TARP Annual Retrospectives",
-            "description": "Treasury has produced retrospective reports on TARP covering each of the last three years. These reports provide comprehensive information on the milestones achieved during the previous year by each TARP program, as well as TARP as a whole.",
+            "identifier": "015-DO-115",
+            "issued": "2015-05-29T00:00:00",
             "keyword": [
                 "TARP",
                 "Annual Retrospectives",
@@ -1702,48 +1709,48 @@
                 "3 year",
                 "4 year"
             ],
+            "landingPage": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/TARP-Annual-Retrospectives.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2013-03-14",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Department of the Treasury",
-                "hasEmail": "mailto:Digital@Treasury.gov"
+            "title": "Latest TARP Reports:  TARP Annual Retrospectives"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/TARP-Annual-Retrospectives.aspx",
-            "issued": "2015-05-29T00:00:00"
+            "contactPoint": {
+                "fn": "Department of the Treasury",
+                "hasEmail": "mailto:Digital@Treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-117",
+            "description": "TARP Housing Transaction Reports show TARP investments in Making Home Affordable, the Hardest Hit Fund, and the FHA Short Refinance Program and are updated to reflect transactions such as periodic adjustments to MHA program participation caps and MHA incentive payments. Transactions Reports are published to this website within two business days of the completion of any new transaction.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/TARP-Housing-Transaction-Reports.aspx",
                     "downloadURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Documents/Housing%20Transactions%20Report%20as%20of%2005.14.2015.pdf",
-                    "mediaType": "application/pdf",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/P1W",
-            "title": "Latest TARP Reports:  TARP Housing Transaction Reports",
-            "description": "TARP Housing Transaction Reports show TARP investments in Making Home Affordable, the Hardest Hit Fund, and the FHA Short Refinance Program and are updated to reflect transactions such as periodic adjustments to MHA program participation caps and MHA incentive payments. Transactions Reports are published to this website within two business days of the completion of any new transaction.",
+            "identifier": "015-DO-117",
+            "issued": "2015-05-29T00:00:00",
             "keyword": [
                 "TARP",
                 "Housing Transaction Report",
@@ -1753,72 +1760,72 @@
                 "MHA",
                 "HHF"
             ],
+            "landingPage": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/TARP-Housing-Transaction-Reports.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2015-05-14",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Department of the Treasury",
-                "hasEmail": "mailto:Digital@Treasury.gov"
+            "title": "Latest TARP Reports:  TARP Housing Transaction Reports"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/TARP-Housing-Transaction-Reports.aspx",
-            "issued": "2015-05-29T00:00:00"
+            "contactPoint": {
+                "fn": "Department of the Treasury",
+                "hasEmail": "mailto:Digital@Treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-118",
+            "description": "Transactions Investment Program Reports provide transaction-level detail for all TARP programs except housing programs. Information found in these report includes: investment amount, capital repayments, warrant dispositions, and exchanges. Transactions Reports are published to this website within two business days of the completion of any new transaction. \r\n\r\nOn September 27, 2013, the Office of Financial Stability updated the format of the Transactions Investment Program Reports.  The changes are identified in the TARP Transactions Report \u2013 Investments Crosswalk (CPP).",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/TARP-Investment-Program-Transaction-Reports.aspx",
                     "downloadURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Documents/10-16-15%20Transactions%20Report%20as%20of%2010-14-15_INVESTMENT_ConvenienceCopy.xlsx",
-                    "mediaType": "application/vnd.ms-excel",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.ms-excel"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/TARP-Investment-Program-Transaction-Reports.aspx",
                     "downloadURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Documents/10-06-15%20Transactions%20Report%20as%20of%2010-02-15_INVESTMENT_ConvenienceCopy.xlsx",
-                    "mediaType": "application/vnd.ms-excel",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.ms-excel"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/TARP-Investment-Program-Transaction-Reports.aspx",
                     "downloadURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Documents/10-01-15%20Transactions%20Report%20as%20of%2009-29-15_INVESTMENT_ConvenienceCopy.xlsx",
-                    "mediaType": "application/vnd.ms-excel",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.ms-excel"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/TARP-Investment-Program-Transaction-Reports.aspx",
                     "downloadURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Documents/09-23-15%20Transactions%20Report%20as%20of%2009-21-15_INVESTMENT_ConvenienceCopy.xlsx",
-                    "mediaType": "application/vnd.ms-excel",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.ms-excel"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/TARP-Investment-Program-Transaction-Reports.aspx",
                     "downloadURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Documents/09-11-15%20Transactions%20Report%20as%20of%2009-09-15_INVESTMENT_ConvenienceCopy.xlsx",
-                    "mediaType": "application/vnd.ms-excel",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.ms-excel"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Latest TARP Reports:  TARP Investment Program Transaction Reports",
-            "description": "Transactions Investment Program Reports provide transaction-level detail for all TARP programs except housing programs. Information found in these report includes: investment amount, capital repayments, warrant dispositions, and exchanges. Transactions Reports are published to this website within two business days of the completion of any new transaction. \r\n\r\nOn September 27, 2013, the Office of Financial Stability updated the format of the Transactions Investment Program Reports.  The changes are identified in the TARP Transactions Report \u2013 Investments Crosswalk (CPP).",
+            "identifier": "015-DO-118",
+            "issued": "2015-05-29T00:00:00",
             "keyword": [
                 "TARP",
                 "Investment Program Transaction Report",
@@ -1827,51 +1834,51 @@
                 "warrant dispositions",
                 "exchanges."
             ],
+            "landingPage": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/TARP-Investment-Program-Transaction-Reports.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2015-05-13",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Department of the Treasury",
-                "hasEmail": "mailto:Digital@Treasury.gov"
-            },
-            "accessLevel": "public",
-            "bureauCode": [
-                "015:00"
-            ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/TARP-Investment-Program-Transaction-Reports.aspx",
             "references": [
                 "http://www.treasury.gov/initiatives/financial-stability/reports/SiteAssets/Pages/TARP-Investment-Program-Transaction-Reports/TARP%20Transactions%20Report%20%E2%80%93%20Investments%20Crosswalk%20(CPP).pdf"
             ],
-            "issued": "2015-05-29T00:00:00"
+            "title": "Latest TARP Reports:  TARP Investment Program Transaction Reports"
         },
         {
             "@type": "dcat:Dataset",
-            "identifier": "015-DO-122",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:00"
+            ],
+            "contactPoint": {
+                "fn": "Department of the Treasury",
+                "hasEmail": "mailto:Digital@Treasury.gov"
+            },
+            "description": "A banking organization holds capital to guard against uncertainty. Capital reassures an institution\u2019s depositors, creditors and counterparties--and the institution itself--that an event such as an unexpected surge in losses or an unanticipated deterioration in earnings will not impair its ability to engage in lending to creditworthy borrowers and protect the savings of its depositors. During this period of heightened economic uncertainty, U.S. federal banking supervisors believe that the largest U.S. bank holding companies (BHCs) should have a capital buffer sufficient to withstand losses and allow them to meet the credit needs of their customers in a more severe recession than is anticipated. For this reason, the Federal Reserve and other bank supervisors embarked on a comprehensive simultaneous assessment of the capital held by the 19 largest U.S. BHCs in February of this year.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/Other-Reports.aspx",
                     "downloadURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Documents/SCAPresults.pdf",
-                    "mediaType": "application/pdf",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "LAtest TARP Reports:  The Supervisory Capital Assessment Program",
-            "description": "A banking organization holds capital to guard against uncertainty. Capital reassures an institution\u2019s depositors, creditors and counterparties--and the institution itself--that an event such as an unexpected surge in losses or an unanticipated deterioration in earnings will not impair its ability to engage in lending to creditworthy borrowers and protect the savings of its depositors. During this period of heightened economic uncertainty, U.S. federal banking supervisors believe that the largest U.S. bank holding companies (BHCs) should have a capital buffer sufficient to withstand losses and allow them to meet the credit needs of their customers in a more severe recession than is anticipated. For this reason, the Federal Reserve and other bank supervisors embarked on a comprehensive simultaneous assessment of the capital held by the 19 largest U.S. BHCs in February of this year.",
+            "identifier": "015-DO-122",
+            "issued": "2015-05-29T00:00:00",
             "keyword": [
                 "TARP",
                 "Supervisory Capital Assessment Program",
@@ -1879,48 +1886,48 @@
                 "Wells Fargo",
                 "State Street"
             ],
+            "landingPage": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/Other-Reports.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2009-05-07",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Department of the Treasury",
-                "hasEmail": "mailto:Digital@Treasury.gov"
+            "title": "LAtest TARP Reports:  The Supervisory Capital Assessment Program"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/Other-Reports.aspx",
-            "issued": "2015-05-29T00:00:00"
+            "contactPoint": {
+                "fn": "Department of the Treasury",
+                "hasEmail": "mailto:Digital@Treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-119",
+            "description": "Section 105(b) of EESA required Treasury to provide detailed reports to Congress on every $50 billion commitment of TARP funds. Treasury's authority to make new TARP commitments ended on October 3, 2010; Treasury therefore no longer issues Tranche Reports. All previous Tranche Reports produced by Treasury can be accessed here.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/Tranche-Reports.aspx",
                     "downloadURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Documents/Eighth%20Tranche%20Report_2009%2010%2007.pdf",
-                    "mediaType": "application/pdf",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Latest TARP Reports:  Tranche Reports",
-            "description": "Section 105(b) of EESA required Treasury to provide detailed reports to Congress on every $50 billion commitment of TARP funds. Treasury's authority to make new TARP commitments ended on October 3, 2010; Treasury therefore no longer issues Tranche Reports. All previous Tranche Reports produced by Treasury can be accessed here.",
+            "identifier": "015-DO-119",
+            "issued": "2015-05-29T00:00:00",
             "keyword": [
                 "TARP",
                 "EESA",
@@ -1929,48 +1936,48 @@
                 "AIFP",
                 "AIG"
             ],
+            "landingPage": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/Tranche-Reports.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2009-10-08",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Department of the Treasury",
-                "hasEmail": "mailto:Digital@Treasury.gov"
+            "title": "Latest TARP Reports:  Tranche Reports"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/Tranche-Reports.aspx",
-            "issued": "2015-05-29T00:00:00"
+            "contactPoint": {
+                "fn": "Department of the Treasury",
+                "hasEmail": "mailto:Digital@Treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-124",
+            "description": "This report provides updated, unaudited cost estimates for the TARP investments, using publicly available data through March 31, 2010. The table below compares these new estimates with the costs reflected in the 2011 President\u2019s Budget, which were based on valuations through November 30, 2009.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/Other-Reports.aspx",
                     "downloadURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Documents/TARP%20Cost%20Estimates%20-%20March%2031%202010.pdf",
-                    "mediaType": "application/pdf",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Latest TARP Reports:  Troubled Asset Relief Program (TARP) Investments as of March 31, 2010",
-            "description": "This report provides updated, unaudited cost estimates for the TARP investments, using publicly available data through March 31, 2010. The table below compares these new estimates with the costs reflected in the 2011 President\u2019s Budget, which were based on valuations through November 30, 2009.",
+            "identifier": "015-DO-124",
+            "issued": "2015-05-29T00:00:00",
             "keyword": [
                 "TARP",
                 "CPP",
@@ -1979,112 +1986,112 @@
                 "PPIP",
                 "2011 President's Budgethttps://apps.treasuryecm.gov/sites/spike/_layouts/SPIKE/DatasetDetailPage.aspx?DatasetId=1564#"
             ],
+            "landingPage": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/Other-Reports.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2010-05-21",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Department of the Treasury",
-                "hasEmail": "mailto:Digital@Treasury.gov"
+            "title": "Latest TARP Reports:  Troubled Asset Relief Program (TARP) Investments as of March 31, 2010"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/Other-Reports.aspx",
-            "issued": "2015-05-29T00:00:00"
+            "contactPoint": {
+                "fn": "Department of the Treasury",
+                "hasEmail": "mailto:digita@treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-050",
+            "description": "Calendnar from Office of Economic Policy showing when economic indicators were released in 2012, 2013, 2014",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://home.treasury.gov/data/monitoring-the-economy",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/monitoring-the-economy/Documents/2013%20%20EP%20Indicators%20Calendar%20-%20monthly.pdf",
-                    "mediaType": "application/pdf",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/pdf"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://home.treasury.gov/data/monitoring-the-economy",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/monitoring-the-economy/Documents/2012%20EP%20Indicators%20Calendar%20-%20monthly.pdf",
-                    "mediaType": "application/pdf",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/pdf"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://home.treasury.gov/data/monitoring-the-economy",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/monitoring-the-economy/Documents/EP%20Indicators%20Calendar%20Rescheduled%20Dates%20for%20Oct,%20Nov,%20Dec%202013.pdf",
-                    "mediaType": "application/pdf",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/pdf"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://home.treasury.gov/data/monitoring-the-economy",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/monitoring-the-economy/Documents/2014%20EP%20Indicators%20Calendar%20-%20monthly%20(Portrait).pdf",
-                    "mediaType": "application/pdf",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "title": "Office of Economic Policy - Economic Indicators Calendar",
-            "description": "Calendnar from Office of Economic Policy showing when economic indicators were released in 2012, 2013, 2014",
+            "identifier": "015-DO-050",
+            "issued": "2014-08-31T00:00:00",
             "keyword": [
                 "EP Indicators Calendar",
                 "Office of Economic Policy Indicators Calendar"
             ],
+            "landingPage": "https://home.treasury.gov/data/monitoring-the-economy",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2012-12-20",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Department of the Treasury",
-                "hasEmail": "mailto:digita@treasury.gov"
+            "title": "Office of Economic Policy - Economic Indicators Calendar"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "https://home.treasury.gov/data/monitoring-the-economy",
-            "issued": "2014-08-31T00:00:00"
+            "contactPoint": {
+                "fn": "Department of the Treasury",
+                "hasEmail": "mailto:digital@treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-044",
+            "description": "The Office of Economic Policy monitors key economic indicators to produce the summary tables of monthly and quarterly U.S. economic statistics.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://home.treasury.gov/data/monitoring-the-economy",
                     "downloadURL": "https://home.treasury.gov/system/files/226/monthly_ECONOMIC_DATA_TABLES.pdf",
-                    "mediaType": "application/pdf",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "Office of Economic Policy - Monthly Economic Indicators Data Tables",
-            "description": "The Office of Economic Policy monitors key economic indicators to produce the summary tables of monthly and quarterly U.S. economic statistics.",
+            "identifier": "015-DO-044",
+            "issued": "2014-08-31T00:00:00",
             "keyword": [
                 "Monthly Economic Data",
                 "Unemployment Rate",
@@ -2095,48 +2102,48 @@
                 "Industrial Production",
                 "Capacity Utilization."
             ],
+            "landingPage": "https://home.treasury.gov/data/monitoring-the-economy",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2014-08-01",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Department of the Treasury",
-                "hasEmail": "mailto:digital@treasury.gov"
+            "title": "Office of Economic Policy - Monthly Economic Indicators Data Tables"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "https://home.treasury.gov/data/monitoring-the-economy",
-            "issued": "2014-08-31T00:00:00"
+            "contactPoint": {
+                "fn": "Department of the Treasury",
+                "hasEmail": "mailto:Digital@treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-045",
+            "description": "Shows quarterly economic indicators such as GDP growth, price indexes, exports and imports, savings rate, unit labor cost and productivity.   Data covers 2010 to 2013 as well as quarter 1 and 2 in 2014.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://home.treasury.gov/data/monitoring-the-economy",
                     "downloadURL": "https://home.treasury.gov/system/files/226/quarterly-ECONOMIC-DATA-TABLES.pdf",
-                    "mediaType": "application/pdf",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/P3M",
-            "title": "Office of Economic Policy - Quarterly economic indicator tables",
-            "description": "Shows quarterly economic indicators such as GDP growth, price indexes, exports and imports, savings rate, unit labor cost and productivity.   Data covers 2010 to 2013 as well as quarter 1 and 2 in 2014.",
+            "identifier": "015-DO-045",
+            "issued": "2014-08-31T00:00:00",
             "keyword": [
                 "Quarterly economic indicator",
                 "GDP",
@@ -2145,244 +2152,244 @@
                 "productivity. unit labor cost",
                 "hourly compensation"
             ],
+            "landingPage": "https://home.treasury.gov/data/monitoring-the-economy",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2014-07-30",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Department of the Treasury",
-                "hasEmail": "mailto:Digital@treasury.gov"
+            "title": "Office of Economic Policy - Quarterly economic indicator tables"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "https://home.treasury.gov/data/monitoring-the-economy",
-            "issued": "2014-08-31T00:00:00"
+            "contactPoint": {
+                "fn": "Office of Economic Policy",
+                "hasEmail": "mailto:digital@treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-059",
+            "description": "Statement of Assistant Secretary for Economic Policy for the Treasury Borrowing Advisory Committee.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/quarterly-refunding/Pages/Economic-Policy-Statements-to-TBAC.aspx",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/quarterly-refunding/Pages/Economic-Policy-Statements-to-TBAC.aspx",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P3M",
-            "title": "Quarterly Refunding - Office of Economic Policy Statements to Treasury Borrowing Advisory Committee",
-            "description": "Statement of Assistant Secretary for Economic Policy for the Treasury Borrowing Advisory Committee.",
+            "identifier": "015-DO-059",
+            "issued": "2014-11-30T00:00:00",
             "keyword": [
                 "TBAC",
                 "Treasury Borrowing Advisory Committee",
                 "Quarterly Refunding",
                 "Office of Economy Policy"
             ],
+            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/quarterly-refunding/Pages/Economic-Policy-Statements-to-TBAC.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2014-11-05",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Office of Economic Policy",
-                "hasEmail": "mailto:digital@treasury.gov"
-            },
-            "accessLevel": "public",
-            "bureauCode": [
-                "015:00"
-            ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/quarterly-refunding/Pages/Economic-Policy-Statements-to-TBAC.aspx",
             "references": [
                 "http://www.treasury.gov/resource-center/data-chart-center/quarterly-refunding/Pages/Economic-Policy-Statements-to-TBAC.aspx"
             ],
-            "issued": "2014-11-30T00:00:00"
+            "title": "Quarterly Refunding - Office of Economic Policy Statements to Treasury Borrowing Advisory Committee"
         },
         {
             "@type": "dcat:Dataset",
-            "identifier": "015-DO-056",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "015:00"
+            ],
+            "contactPoint": {
+                "fn": "Department of the Treasury",
+                "hasEmail": "mailto:digital@treasury.gov"
+            },
+            "description": "The U.S. Department of the Treasury's current estimates of net marketable borrowing.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/quarterly-refunding/Pages/Quarterly-Financing-Estimates.aspx",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/quarterly-refunding/Pages/Quarterly-Financing-Estimates.aspx",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P3M",
-            "title": "Quarterly Refunding - Quarterly Financing Estimates",
-            "description": "The U.S. Department of the Treasury's current estimates of net marketable borrowing.",
+            "identifier": "015-DO-056",
+            "issued": "2014-11-05T00:00:00",
             "keyword": [
                 "Borrowing Estimates",
                 "Quarterly Refunding"
             ],
+            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/quarterly-refunding/Pages/Quarterly-Financing-Estimates.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2014-11-03",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Department of the Treasury",
-                "hasEmail": "mailto:digital@treasury.gov"
-            },
-            "accessLevel": "public",
-            "bureauCode": [
-                "015:00"
-            ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/quarterly-refunding/Pages/Quarterly-Financing-Estimates.aspx",
             "references": [
                 "http://www.treasury.gov/resource-center/data-chart-center/quarterly-refunding/Pages/Quarterly-Financing-Estimates.aspx"
             ],
-            "issued": "2014-11-05T00:00:00"
+            "title": "Quarterly Refunding - Quarterly Financing Estimates"
         },
         {
             "@type": "dcat:Dataset",
-            "identifier": "015-DO-058",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "015:00"
+            ],
+            "contactPoint": {
+                "fn": "Department of the Treasury",
+                "hasEmail": "mailto:Digital@Treasury.gov"
+            },
+            "description": "Quarterly refunding auction schedule",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/quarterly-refunding/Documents/auctions.pdf",
-                    "mediaType": "application/pdf",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/P3M",
-            "title": "Quarterly Refunding Auction Schedule",
-            "description": "Quarterly refunding auction schedule",
+            "identifier": "015-DO-058",
+            "issued": "2014-11-30T00:00:00",
             "keyword": [
                 "Quarterly refunding",
                 "Auction Schedule"
             ],
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2014-11-05",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Department of the Treasury",
-                "hasEmail": "mailto:Digital@Treasury.gov"
+            "title": "Quarterly Refunding Auction Schedule"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "issued": "2014-11-30T00:00:00"
+            "contactPoint": {
+                "fn": "Department of the Treasury",
+                "hasEmail": "mailto:digital@treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-057",
+            "description": "Department of the Treasury offers Treasury securities to refund maturing Treasury notes specified in this tentative schedule.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/quarterly-refunding/Documents/auctions.xml",
-                    "mediaType": "text/xml",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/xml"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/quarterly-refunding/Documents/auctions.pdf",
-                    "mediaType": "application/pdf",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/P3M",
-            "title": "Quarterly Refunding auction schedule of Treasury securities.",
-            "description": "Department of the Treasury offers Treasury securities to refund maturing Treasury notes specified in this tentative schedule.",
+            "identifier": "015-DO-057",
+            "issued": "2014-11-30T00:00:00",
             "keyword": [
                 "Quarterly Refunding Auction Schedule",
                 "Quarterly Refunding",
                 "Auction Schedule",
                 "Treasury Security Auction"
             ],
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2014-11-05",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Department of the Treasury",
-                "hasEmail": "mailto:digital@treasury.gov"
+            "title": "Quarterly Refunding auction schedule of Treasury securities."
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "issued": "2014-11-30T00:00:00"
+            "contactPoint": {
+                "fn": "James Kostiw",
+                "hasEmail": "mailto:o_f_a_c@do.treas.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-083",
+            "describedBy": "http://www.treasury.gov/ofac/downloads/sanctions/1.0/sdn_advanced.xsd",
+            "description": "As part of its enforcement efforts, OFAC publishes a list of individuals and companies owned or controlled by, or acting for or on behalf of, targeted countries. It also lists individuals, groups, and entities, such as terrorists and narcotics traffickers designated under programs that are not country-specific. Collectively, such individuals and companies are called \"Specially Designated Nationals\" or \"SDNs.\" Their assets are blocked and U.S. persons are generally prohibited from dealing with them.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "describedBy": "http://www.treasury.gov/ofac/downloads/sanctions/1.0/sdn_advanced.xsd",
                     "describedByType": "text/xml",
                     "downloadURL": "http://www.treasury.gov/ofac/downloads/sanctions/1.0/sdn_advanced.xml",
-                    "mediaType": "text/xml",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/xml"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Specially Designated Nationals (SDN) and Blocked Persons List",
-            "description": "As part of its enforcement efforts, OFAC publishes a list of individuals and companies owned or controlled by, or acting for or on behalf of, targeted countries. It also lists individuals, groups, and entities, such as terrorists and narcotics traffickers designated under programs that are not country-specific. Collectively, such individuals and companies are called \"Specially Designated Nationals\" or \"SDNs.\" Their assets are blocked and U.S. persons are generally prohibited from dealing with them.",
+            "identifier": "015-DO-083",
             "keyword": [
                 "OFAC",
                 "Office of Foreign Assets Control",
@@ -2394,69 +2401,69 @@
                 "sanctions list",
                 "blocked list"
             ],
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2016-11-01",
+            "programCode": [
+                "015:004"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Office of Foreign Assets Control",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Office of Foreign Assets Control"
-            },
-            "contactPoint": {
-                "fn": "James Kostiw",
-                "hasEmail": "mailto:o_f_a_c@do.treas.gov"
-            },
-            "accessLevel": "public",
-            "bureauCode": [
-                "015:00"
-            ],
-            "programCode": [
-                "015:004"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "describedBy": "http://www.treasury.gov/ofac/downloads/sanctions/1.0/sdn_advanced.xsd",
             "references": [
                 "http://www.treasury.gov/resource-center/sanctions/SDN-List/Documents/sdn_advanced_notes.pdf",
                 "https://www.treasury.gov/resource-center/sanctions/SDN-List/Pages/sdn_data.aspx"
-            ]
+            ],
+            "title": "Specially Designated Nationals (SDN) and Blocked Persons List"
         },
         {
             "@type": "dcat:Dataset",
-            "identifier": "015-DO-129",
-            "distribution": [
-                {
-                    "accessURL": "https://home.treasury.gov/system/files/256/SSBCI-Transactions-Dataset.csv",
-                    "downloadURL": "https://home.treasury.gov/system/files/256/SSBCI-Data-Publication-Narrative.pdf",
-                    "mediaType": "application/pdf",
-                    "@type": "dcat:Distribution"
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:00"
+            ],
+            "contactPoint": {
+                "fn": "Jeffrey Stout",
+                "hasEmail": "mailto:jeffrey.stout@treasury.gov"
+            },
+            "description": "The State Small Business Credit Initiative (SSBCI)Transactions Dataset is a set of files reporting transaction level data for all transactions conducted through the SSBCI program from inception in 2011 through December 31, 2016. This dataset categorizes transactions by program type, according to the five approved SSBCI programs: Capital Access Programs, Collateral Support Programs, Loan Guarantee Programs, Loan Participation Programs, and Venture Capital Programs. The transaction level data was reported to Treasury by Participating States on an annual basis, as required by the Allocation Agreements. Participating States included all 50 states, the District of Columbia, American Samoa, Guam, Northern Mariana Islands, Puerto Rico and the U.S. Virgin Islands. The data fields provided here include the total financing amount, the amount of federal dollars expended, the date of the transaction, and the industry, zip code, and FTEs of the business receiving financing at the point of transaction, among other fields. The data files are available for public use. This dataset provides quantitative information that can be used for analysis of federal expenditure in supporting small business and economic development in identifying how and where federal financing was used.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://home.treasury.gov/system/files/256/SSBCI-Transactions-Dataset.csv",
+                    "downloadURL": "https://home.treasury.gov/system/files/256/SSBCI-Data-Publication-Narrative.pdf",
+                    "mediaType": "application/pdf"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://home.treasury.gov/system/files/256/SSBCI-Transactions-Dataset.csv",
                     "downloadURL": "https://home.treasury.gov/system/files/256/SSBCI-Data-Definitions.pdf",
-                    "mediaType": "application/pdf",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/pdf"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://home.treasury.gov/system/files/256/SSBCI-Transactions-Dataset.csv",
                     "downloadURL": "https://home.treasury.gov/system/files/256/SSBCI-Data-Documentation.pdf",
-                    "mediaType": "application/pdf",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/pdf"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://home.treasury.gov/system/files/256/SSBCI-Transactions-Dataset.csv",
                     "downloadURL": "https://home.treasury.gov/system/files/256/SSBCI-Data-Release-Protocol.pdf",
-                    "mediaType": "application/pdf",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "State Small Business Credit Initiative (SSBCI) Transactions Dataset",
-            "description": "The State Small Business Credit Initiative (SSBCI)Transactions Dataset is a set of files reporting transaction level data for all transactions conducted through the SSBCI program from inception in 2011 through December 31, 2016. This dataset categorizes transactions by program type, according to the five approved SSBCI programs: Capital Access Programs, Collateral Support Programs, Loan Guarantee Programs, Loan Participation Programs, and Venture Capital Programs. The transaction level data was reported to Treasury by Participating States on an annual basis, as required by the Allocation Agreements. Participating States included all 50 states, the District of Columbia, American Samoa, Guam, Northern Mariana Islands, Puerto Rico and the U.S. Virgin Islands. The data fields provided here include the total financing amount, the amount of federal dollars expended, the date of the transaction, and the industry, zip code, and FTEs of the business receiving financing at the point of transaction, among other fields. The data files are available for public use. This dataset provides quantitative information that can be used for analysis of federal expenditure in supporting small business and economic development in identifying how and where federal financing was used.",
+            "identifier": "015-DO-129",
+            "issued": "2017-08-01T00:00:00",
             "keyword": [
                 "small business",
                 "finance",
@@ -2474,102 +2481,101 @@
                 "state",
                 "initiative"
             ],
+            "landingPage": "https://home.treasury.gov/system/files/256/SSBCI-Transactions-Dataset.csv",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2017-08-03",
+            "programCode": [
+                "015:060"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "U.S. Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "U.S. Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Jeffrey Stout",
-                "hasEmail": "mailto:jeffrey.stout@treasury.gov"
+            "rights": "This data is available for public access.",
+            "title": "State Small Business Credit Initiative (SSBCI) Transactions Dataset"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:060"
-            ],
-            "rights": "This data is available for public access.",
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "https://home.treasury.gov/system/files/256/SSBCI-Transactions-Dataset.csv",
-            "issued": "2017-08-01T00:00:00"
+            "contactPoint": {
+                "fn": "Department of the Treasury",
+                "hasEmail": "mailto:Digital@Treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-106",
+            "description": "Treasury and the U.S. Department of Housing and Urban Development (HUD) jointly produce a Monthly Housing Scorecard on the health of the nation\u2019s housing market.  The Scorecard is generally released during the first week of each month.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/Monthly-Housing-Scorecard.aspx",
                     "downloadURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Documents/april%20scrd%20spotlight.pdf",
-                    "mediaType": "application/pdf",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "TARP Monthly Housing Scorecard",
-            "description": "Treasury and the U.S. Department of Housing and Urban Development (HUD) jointly produce a Monthly Housing Scorecard on the health of the nation\u2019s housing market.  The Scorecard is generally released during the first week of each month.",
+            "identifier": "015-DO-106",
+            "issued": "2015-05-29T00:00:00",
             "keyword": [
                 "TARP",
                 "HUD",
                 "Monthly Housing Scorecard"
             ],
+            "landingPage": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/Monthly-Housing-Scorecard.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2015-05-13",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Department of the Treasury",
-                "hasEmail": "mailto:Digital@Treasury.gov"
+            "title": "TARP Monthly Housing Scorecard"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/Monthly-Housing-Scorecard.aspx",
-            "issued": "2015-05-29T00:00:00"
+            "contactPoint": {
+                "fn": "Department of the Treasury",
+                "hasEmail": "mailto:Digital@Treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-105",
+            "description": "The purpose of the Making Home Affordable \u00a9 (MHA) Data File is to provide the general public with a comprehensive view of the Obama Administration's MHA programs to more fully understand their impact in a continued commitment to transparency. Because protecting the identities of MHA participants is of primary importance, the Treasury Department conducts a thorough analysis and takes steps to ensure the anonymity of individual borrowers. \r\n\r\nThe MHA Data File consists of three sets of loan-level mortgage modification data: The First Lien Modification Program, the Second Lien Modification Program, and the Home Affordable Foreclosure Alternatives Program. The First Lien Modification Program also contains one additional subset - the net present value (NPV) file. Each set is subdivided into ten geographic regions that cover the United States and its territories. The data are presented in comma separated value (CSV) format and total roughly 3 gigabytes in size. \r\n\r\nThe information contained in these files is data reported by servicers. Please consult the MHA Data File User Guide for a description of certain data quality issues and variances which could affect the use or interpretation of the data.  Treasury and the MHA Program Administrator continue to work with servicers to monitor data quality and remediate known issues.\r\n\r\nThese files are cumulative and will be refreshed monthly, providing users with up-to-date MHA data. The Making Home Affordable Data Files include information on:\r\n\r\n\u2022Home Affordable Foreclosure Alternatives (HAFA) Program, \r\n\u2022Principal Reduction Alternative (PRA), \r\n\u2022Second Lien Modification Program (2MP), \r\n\u2022Home Affordable Unemployment Program (UP), \r\n\u2022FHA-HAMP and \r\n\u2022Rural Development HAMP (RD-HAMP). \r\nPRA, UP, Treasury FHA-HAMP, and RD-HAMP are included in the First Lien Modification files, with 2MP and HAFA in separate files. The Making Home Affordable Data File User Guide has been updated to reflect these additions.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/mha_publicfile.aspx",
                     "downloadURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Documents/MHA%20Data%20File%20Summary_new.pdf",
-                    "mediaType": "application/pdf",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/pdf"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/mha_publicfile.aspx",
                     "downloadURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Documents/MHA%20Data%20File%20User%20Guide%20v8.0%20FINAL.PDF",
-                    "mediaType": "application/pdf",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "TARP Report:  Making Home Affordable Data File",
-            "description": "The purpose of the Making Home Affordable \u00a9 (MHA) Data File is to provide the general public with a comprehensive view of the Obama Administration's MHA programs to more fully understand their impact in a continued commitment to transparency. Because protecting the identities of MHA participants is of primary importance, the Treasury Department conducts a thorough analysis and takes steps to ensure the anonymity of individual borrowers. \r\n\r\nThe MHA Data File consists of three sets of loan-level mortgage modification data: The First Lien Modification Program, the Second Lien Modification Program, and the Home Affordable Foreclosure Alternatives Program. The First Lien Modification Program also contains one additional subset - the net present value (NPV) file. Each set is subdivided into ten geographic regions that cover the United States and its territories. The data are presented in comma separated value (CSV) format and total roughly 3 gigabytes in size. \r\n\r\nThe information contained in these files is data reported by servicers. Please consult the MHA Data File User Guide for a description of certain data quality issues and variances which could affect the use or interpretation of the data.  Treasury and the MHA Program Administrator continue to work with servicers to monitor data quality and remediate known issues.\r\n\r\nThese files are cumulative and will be refreshed monthly, providing users with up-to-date MHA data. The Making Home Affordable Data Files include information on:\r\n\r\n\u2022Home Affordable Foreclosure Alternatives (HAFA) Program, \r\n\u2022Principal Reduction Alternative (PRA), \r\n\u2022Second Lien Modification Program (2MP), \r\n\u2022Home Affordable Unemployment Program (UP), \r\n\u2022FHA-HAMP and \r\n\u2022Rural Development HAMP (RD-HAMP). \r\nPRA, UP, Treasury FHA-HAMP, and RD-HAMP are included in the First Lien Modification files, with 2MP and HAFA in separate files. The Making Home Affordable Data File User Guide has been updated to reflect these additions.",
+            "identifier": "015-DO-105",
             "keyword": [
                 "TARP",
                 "Making Home Affordable",
@@ -2578,113 +2584,113 @@
                 "UP",
                 "HAFA."
             ],
+            "landingPage": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/mha_publicfile.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2015-05-12",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Department of the Treasury",
-                "hasEmail": "mailto:Digital@Treasury.gov"
+            "title": "TARP Report:  Making Home Affordable Data File"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/mha_publicfile.aspx"
+            "contactPoint": {
+                "fn": "Department of the Treasury",
+                "hasEmail": "mailto:Digital@Treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-103",
+            "description": "These reports, released in conjunction with the monthly MHA Program Performance Report, include mortgage modification activity under HAMP by metropolitan area.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/HAMP-Report.aspx",
                     "downloadURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Documents/MSA%20Data%20May%202014.pdf",
-                    "mediaType": "application/pdf",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/pdf"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/HAMP-Report.aspx",
                     "downloadURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Documents/MSA%20Data%20April%202014.pdf",
-                    "mediaType": "application/pdf",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "TARP Reports:  HAMP Activity by Metropolitan Statistical Area",
-            "description": "These reports, released in conjunction with the monthly MHA Program Performance Report, include mortgage modification activity under HAMP by metropolitan area.",
+            "identifier": "015-DO-103",
+            "issued": "2015-05-29T00:00:00",
             "keyword": [
                 "TARP",
                 "HAMP",
                 "Metropolitan Statistical Area",
                 "Making Home Affordable"
             ],
+            "landingPage": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/HAMP-Report.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2014-07-10",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Department of the Treasury",
-                "hasEmail": "mailto:Digital@Treasury.gov"
+            "title": "TARP Reports:  HAMP Activity by Metropolitan Statistical Area"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/HAMP-Report.aspx",
-            "issued": "2015-05-29T00:00:00"
+            "contactPoint": {
+                "fn": "Office of Financial Stability",
+                "hasEmail": "mailto:digital@treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-010",
+            "description": "The Troubled Asset Relief Program (TARP) played a critical role in breaking the back of the financial crisis and laying a foundation for future growth. It included a comprehensive set of measures to recapitalize the financial system, restart the credit markets, restore confidence, and lower borrowing costs for businesses and families. This dataset shows Trouble Asset Relief Program (TARP) investment transactions.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/initiatives/financial-stability/Pages/default.aspx",
                     "downloadURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Documents/Daily_TARP_Update%20-%2008.28.2014.pdf",
-                    "mediaType": "application/pdf",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/pdf"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/initiatives/financial-stability/Pages/default.aspx",
                     "downloadURL": "http://www.treasury.gov/initiatives/financial-stability/reports/Pages/TARP-Tracker.aspx",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/initiatives/financial-stability/Pages/default.aspx",
                     "downloadURL": "http://data.treasury.gov/feed.svc/TroubledAssetReliefProgramData",
-                    "mediaType": "application/rss+xml",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/rss+xml"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "TARP Transactions Report, Capital Purchase Program (Investments)",
-            "description": "The Troubled Asset Relief Program (TARP) played a critical role in breaking the back of the financial crisis and laying a foundation for future growth. It included a comprehensive set of measures to recapitalize the financial system, restart the credit markets, restore confidence, and lower borrowing costs for businesses and families. This dataset shows Trouble Asset Relief Program (TARP) investment transactions.",
+            "identifier": "015-DO-010",
             "keyword": [
                 "tarp",
                 "troubled asset relief program",
@@ -2693,247 +2699,247 @@
                 "2008",
                 "recession"
             ],
+            "landingPage": "http://www.treasury.gov/initiatives/financial-stability/Pages/default.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2013-11-01",
+            "programCode": [
+                "015:044"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Office of Financial Stability",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Office of Financial Stability"
-            },
-            "contactPoint": {
-                "fn": "Office of Financial Stability",
-                "hasEmail": "mailto:digital@treasury.gov"
+            "title": "TARP Transactions Report, Capital Purchase Program (Investments)"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:044"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/initiatives/financial-stability/Pages/default.aspx"
+            "contactPoint": {
+                "fn": "Department of the Treasury",
+                "hasEmail": "mailto:digital@treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-064",
+            "description": "List showing Treasury Borrowing Advisory Committee members. The Committee's membership includes representatives from firms that actively trade Treasury securities and firms that make large investments in Treasury securities. The Committee responds to questions and discussion charts presented by Treasury via a formal report to the Secretary of the Treasury.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/quarterly-refunding/Pages/members-index.aspx",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/quarterly-refunding/Documents/TBAC%20website%20version%20October%202014.pdf",
-                    "mediaType": "application/pdf",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/P3M",
-            "title": "Treasury Borrowing Advisory Committee Members",
-            "description": "List showing Treasury Borrowing Advisory Committee members. The Committee's membership includes representatives from firms that actively trade Treasury securities and firms that make large investments in Treasury securities. The Committee responds to questions and discussion charts presented by Treasury via a formal report to the Secretary of the Treasury.",
+            "identifier": "015-DO-064",
+            "issued": "2014-11-30T00:00:00",
             "keyword": [
                 "TBAC",
                 "Treasury Borrowing Advisory Committee"
             ],
+            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/quarterly-refunding/Pages/members-index.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2014-10-31",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Department of the Treasury",
-                "hasEmail": "mailto:digital@treasury.gov"
-            },
-            "accessLevel": "public",
-            "bureauCode": [
-                "015:00"
-            ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/quarterly-refunding/Pages/members-index.aspx",
             "references": [
                 "http://www.treasury.gov/resource-center/data-chart-center/quarterly-refunding/Pages/overview.aspx"
             ],
-            "issued": "2014-11-30T00:00:00"
+            "title": "Treasury Borrowing Advisory Committee Members"
         },
         {
             "@type": "dcat:Dataset",
-            "identifier": "015-DO-127",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:00"
+            ],
+            "contactPoint": {
+                "fn": "Treasury International Capital",
+                "hasEmail": "mailto:digital@treasury.gov"
+            },
+            "description": "Archives of Treasury International Capital (TIC) data that were released monthly on Treasury's TIC website. The archived data cover: purchases and sales of long-term securities by foreign-residents; claims and liabilities to foreign-residents reported monthly/quarterly by banks and brokers/dealers of securities; claims and liabilities to foreign-residents reported quarterly by nonbanks; and holdings and settlements of derivatives contracts with foreign-residents reported quarterly by businesses with large holdings of derivatives contracts.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticarchives.aspx",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Documents/ticrel_20150916.zip",
-                    "mediaType": "application/zip",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/zip"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Treasury International Capital (TIC) - Archives of TIC Monthly Data Releases",
-            "description": "Archives of Treasury International Capital (TIC) data that were released monthly on Treasury's TIC website. The archived data cover: purchases and sales of long-term securities by foreign-residents; claims and liabilities to foreign-residents reported monthly/quarterly by banks and brokers/dealers of securities; claims and liabilities to foreign-residents reported quarterly by nonbanks; and holdings and settlements of derivatives contracts with foreign-residents reported quarterly by businesses with large holdings of derivatives contracts.",
+            "identifier": "015-DO-127",
             "keyword": [
                 "Treasury International Capital",
                 "TIC",
                 "long-term securities",
                 "claims and liabilities"
             ],
+            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticarchives.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2015-11-07",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Treasury International Capital",
-                "hasEmail": "mailto:digital@treasury.gov"
+            "title": "Treasury International Capital (TIC) - Archives of TIC Monthly Data Releases"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticarchives.aspx"
+            "contactPoint": {
+                "fn": "Treasury International Capital",
+                "hasEmail": "mailto:digital@treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-024",
+            "description": "Annual Surveys of Foreign Portfolio Holdings of U.S. Securities at end-June",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticpress.aspx",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticpress.aspx#2",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "title": "Treasury International Capital (TIC) - TIC Press Releases - Annual Surveys of Foreign Portfolio Holdings of U.S. Securities at end-June",
-            "description": "Annual Surveys of Foreign Portfolio Holdings of U.S. Securities at end-June",
+            "identifier": "015-DO-024",
             "keyword": [
                 "Treasury International Capital",
                 "TIC",
                 "TIC Press Releases",
                 "Annual Surveys of Foreign Portfolio Holdings"
             ],
+            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticpress.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2014-04-30",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Treasury International Capital",
-                "hasEmail": "mailto:digital@treasury.gov"
+            "references": [
+                "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticfaq1.aspx"
+            ],
+            "title": "Treasury International Capital (TIC) - TIC Press Releases - Annual Surveys of Foreign Portfolio Holdings of U.S. Securities at end-June"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticpress.aspx",
-            "references": [
-                "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticfaq1.aspx"
-            ]
+            "contactPoint": {
+                "fn": "Treasury International Capital",
+                "hasEmail": "mailto:digital@treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-025",
+            "description": "Treasury International Capital System (TIC) Press Releases - Annual Surveys of U.S. Portfolio Holdings of Foreign Securities at end-year",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/index.aspx",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticpress.aspx#3",
-                    "mediaType": "application/vnd.ms-excel",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.ms-excel"
                 }
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "title": "Treasury International Capital (TIC) - TIC Press Releases - Annual Surveys of U.S. Portfolio Holdings of Foreign Securities at end-year",
-            "description": "Treasury International Capital System (TIC) Press Releases - Annual Surveys of U.S. Portfolio Holdings of Foreign Securities at end-year",
+            "identifier": "015-DO-025",
             "keyword": [
                 "Treasury International Capital",
                 "TIC",
                 "TIC  Press Releases",
                 "Annual Surveys of Foreign Securities Holdings"
             ],
+            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/index.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2013-10-31",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Treasury International Capital",
-                "hasEmail": "mailto:digital@treasury.gov"
+            "references": [
+                "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticfaq1.aspx"
+            ],
+            "title": "Treasury International Capital (TIC) - TIC Press Releases - Annual Surveys of U.S. Portfolio Holdings of Foreign Securities at end-year"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/index.aspx",
-            "references": [
-                "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticfaq1.aspx"
-            ]
+            "contactPoint": {
+                "fn": "Treasury International Capital",
+                "hasEmail": "mailto:digital@treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-023",
+            "description": "TIC Press Releases - Monthly Releases and Archives of Treasury International Capital (TIC) Data {Across-U.S. Border Financial Flows}",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticpress.aspx#1",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Documents/npr_history.csv",
-                    "mediaType": "text/csv",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/csv"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "Treasury International Capital (TIC) - TIC Press Releases - Monthly Releases and Archives of Treasury International Capital (TIC) Data {Across U.S. Border Financial Flows}",
-            "description": "TIC Press Releases - Monthly Releases and Archives of Treasury International Capital (TIC) Data {Across-U.S. Border Financial Flows}",
+            "identifier": "015-DO-023",
             "keyword": [
                 "Treasury International Capital System",
                 "TIC",
@@ -2941,272 +2947,273 @@
                 "Financial Flows",
                 "TIC Press Releases"
             ],
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2014-04-15",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Treasury International Capital",
-                "hasEmail": "mailto:digital@treasury.gov"
-            },
-            "accessLevel": "public",
-            "bureauCode": [
-                "015:00"
-            ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "references": [
                 "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticpr-faqs-2006nov16.aspx",
                 "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/index.aspx"
-            ]
+            ],
+            "title": "Treasury International Capital (TIC) - TIC Press Releases - Monthly Releases and Archives of Treasury International Capital (TIC) Data {Across U.S. Border Financial Flows}"
         },
         {
             "@type": "dcat:Dataset",
-            "identifier": "015-DO-029",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "015:00"
+            ],
+            "contactPoint": {
+                "fn": "Treasury International Capital",
+                "hasEmail": "mailto:digital@treasury.gov"
+            },
+            "description": "Treasury International Capital (TIC): U.S. Banking Data (reported by banks and all other financial firms) - monthly Claims on all foreign residents by type and counterparty.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticlaim.aspx",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Documents/bctype.csv",
-                    "mediaType": "text/csv",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/csv"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticlaim.aspx",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Documents/bctype.txt",
-                    "mediaType": "text/plain",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/plain"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticlaim.aspx",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Documents/bctype_history.txt",
-                    "mediaType": "text/plain",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/plain"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticlaim.aspx",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Documents/bctype_history.csv",
-                    "mediaType": "text/csv",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/csv"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "Treasury International Capital (TIC) - U.S. Banking Data -  Claims on foreign-residents (reported by banks and all other financial firms) - Claims on all foreign residents by type and counterparty",
-            "description": "Treasury International Capital (TIC): U.S. Banking Data (reported by banks and all other financial firms) - monthly Claims on all foreign residents by type and counterparty.",
+            "identifier": "015-DO-029",
             "keyword": [
                 "Department of the Treasury",
                 "TIC",
                 "U.S. Financial Firms Claims on Foreign Residents"
             ],
+            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticlaim.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2014-02-28",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Treasury International Capital",
-                "hasEmail": "mailto:digital@treasury.gov"
+            "title": "Treasury International Capital (TIC) - U.S. Banking Data -  Claims on foreign-residents (reported by banks and all other financial firms) - Claims on all foreign residents by type and counterparty"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticlaim.aspx"
+            "contactPoint": {
+                "fn": "Treasury International Capital",
+                "hasEmail": "mailto:digital@treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-028",
+            "description": "U.S. Banking Data (reported by banks and all other financial firms) - monthly U.S. Financial Firms' Liabilities to Foreign Residents. \r\n- Liabilities to all foreign residents, by type and holder",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticliab.aspx",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Documents/bltype_history.txt",
-                    "mediaType": "text/plain",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/plain"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticliab.aspx",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Documents/bltype_history.csv",
-                    "mediaType": "text/csv",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/csv"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticliab.aspx",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Documents/bltype.csv",
-                    "mediaType": "text/csv",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/csv"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticliab.aspx",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Documents/bltype.txt",
-                    "mediaType": "text/plain",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/plain"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "Treasury International Capital (TIC) - U.S. Banking Data -  U.S. Financial Firms' Liabilities to Foreign Residents - A.Liabilities to all foreign residents, by type and holder",
-            "description": "U.S. Banking Data (reported by banks and all other financial firms) - monthly U.S. Financial Firms' Liabilities to Foreign Residents. \r\n- Liabilities to all foreign residents, by type and holder",
+            "identifier": "015-DO-028",
             "keyword": [
                 "Treasury International Capital",
                 "TIC",
                 "U.S. Banking Data - Liabilities to foreign-residents"
             ],
+            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticliab.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2014-02-08",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Treasury International Capital",
-                "hasEmail": "mailto:digital@treasury.gov"
+            "title": "Treasury International Capital (TIC) - U.S. Banking Data -  U.S. Financial Firms' Liabilities to Foreign Residents - A.Liabilities to all foreign residents, by type and holder"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticliab.aspx"
+            "contactPoint": {
+                "fn": "Department of the Treasury",
+                "hasEmail": "mailto:Digital@Treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-075",
+            "description": "U.S. Transactions with Foreigners in Long-Term Securities by country.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/country-longterm.aspx",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/country-longterm.aspx",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Treasury International Capital (TIC) - U.S. Transactions with Foreign Residents in Long Term Securities - Gross & Net Purchases by All Foreigners of long term Asset Backed Securities (ABS) - Gross Foreign Purchases and Sales by Country",
-            "description": "U.S. Transactions with Foreigners in Long-Term Securities by country.",
+            "identifier": "015-DO-075",
+            "issued": "2014-11-30T00:00:00",
             "keyword": [
                 "long term Asset-Backed Securities",
                 "Gross Foreign Purchases and Sales by country",
                 "US Residents",
                 "Foreign Residents"
             ],
+            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/country-longterm.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2010-11-07",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Department of the Treasury",
-                "hasEmail": "mailto:Digital@Treasury.gov"
+            "title": "Treasury International Capital (TIC) - U.S. Transactions with Foreign Residents in Long Term Securities - Gross & Net Purchases by All Foreigners of long term Asset Backed Securities (ABS) - Gross Foreign Purchases and Sales by Country"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/country-longterm.aspx",
-            "issued": "2014-11-30T00:00:00"
+            "contactPoint": {
+                "fn": "Department of the Treasury",
+                "hasEmail": "mailto:Digital@Treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-073",
+            "description": "Total Foreign Purchases and sales of long-term U.S. asset-backed securities",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticsec.aspx",
                     "downloadURL": "http://www.treasury.gov/ticdata/Publish/us_abs_net.txt",
-                    "mediaType": "text/plain",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/plain"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "Treasury International Capital (TIC) - U.S. Transactions with Foreign Residents in Long Term Securities - Gross & Net Purchases by All Foreigners of long-term Asset-Backed Securities (ABS) - Foreign Net purchases of U.S. ABS",
-            "description": "Total Foreign Purchases and sales of long-term U.S. asset-backed securities",
+            "identifier": "015-DO-073",
+            "issued": "2014-11-30T00:00:00",
             "keyword": [
                 "Long term asset-backed securities (ABS)",
                 "net foreign purchases of US ABS"
             ],
+            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticsec.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2014-06-18",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Department of the Treasury",
-                "hasEmail": "mailto:Digital@Treasury.gov"
+            "title": "Treasury International Capital (TIC) - U.S. Transactions with Foreign Residents in Long Term Securities - Gross & Net Purchases by All Foreigners of long-term Asset-Backed Securities (ABS) - Foreign Net purchases of U.S. ABS"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticsec.aspx",
-            "issued": "2014-11-30T00:00:00"
+            "contactPoint": {
+                "fn": "Department of the Treasury",
+                "hasEmail": "mailto:Digital@Treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-074",
+            "description": "Total purchases and sales of long-term foreign asset-backed securities by US Residents (In Millions of dollars) (For net transactions: Negative entries indicate net US purchases of foreign securities, or a net outflow of capital from the United States; positive entries indicate US sales of foreign securities)",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/index.aspx",
                     "downloadURL": "http://www.treasury.gov/ticdata/Publish/frgn_abs_net.txt",
-                    "mediaType": "text/plain",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/plain"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "Treasury International Capital (TIC) - U.S. Transactions with Foreign Residents in Long Term Securities - Gross & Net Purchases by All Foreigners of long-term Asset-Backed Securities (ABS) - U.S. Net purchases of Foreign ABS",
-            "description": "Total purchases and sales of long-term foreign asset-backed securities by US Residents (In Millions of dollars) (For net transactions: Negative entries indicate net US purchases of foreign securities, or a net outflow of capital from the United States; positive entries indicate US sales of foreign securities)",
+            "identifier": "015-DO-074",
+            "issued": "2014-11-30T00:00:00",
             "keyword": [
                 "Long-term foreign asset-backed securities",
                 "asset backed securities",
@@ -3214,47 +3221,47 @@
                 "Foreign Residents",
                 "US Residents"
             ],
+            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/index.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2014-06-18",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Department of the Treasury",
-                "hasEmail": "mailto:Digital@Treasury.gov"
+            "title": "Treasury International Capital (TIC) - U.S. Transactions with Foreign Residents in Long Term Securities - Gross & Net Purchases by All Foreigners of long-term Asset-Backed Securities (ABS) - U.S. Net purchases of Foreign ABS"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/index.aspx",
-            "issued": "2014-11-30T00:00:00"
+            "contactPoint": {
+                "fn": "Treasury International Capital (TIC)",
+                "hasEmail": "mailto:digital@treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-082",
+            "description": "Treasury International Capital (TIC) Monthly reports on gross purchases and sales of US long term securities as well as foreign long term securities",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticpress.aspx#1",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "Treasury International Capital (TIC) - U.S. Transactions with Foreign Residents in Long Term Securities - Gross Foreign Purchases and Sales Monthly Releases and Archives of Treasury International Capital (TIC) Data {Across-U.S. Border Financial Flows}",
-            "description": "Treasury International Capital (TIC) Monthly reports on gross purchases and sales of US long term securities as well as foreign long term securities",
+            "identifier": "015-DO-082",
+            "issued": "2014-11-30T00:00:00",
             "keyword": [
                 "Foreign purchases",
                 "Foreign Sales",
@@ -3269,59 +3276,59 @@
                 "Foreign Bonds",
                 "Foreign Stocks"
             ],
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2014-10-16",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Treasury International Capital (TIC)",
-                "hasEmail": "mailto:digital@treasury.gov"
+            "title": "Treasury International Capital (TIC) - U.S. Transactions with Foreign Residents in Long Term Securities - Gross Foreign Purchases and Sales Monthly Releases and Archives of Treasury International Capital (TIC) Data {Across-U.S. Border Financial Flows}"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "issued": "2014-11-30T00:00:00"
+            "contactPoint": {
+                "fn": "Department of the Treasury",
+                "hasEmail": "mailto:Digital@Treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-077",
+            "description": "Foreign purchases and sales of long-term domestic and foreign securities by type.  Data column titles correspond to column titles in Treasury Bulletin Table CM-VI-4, excluding CM-VI-4 columns (1) and (8).  Refer to CNTRYCDS.TXT file for \"Cntry Code\" identification.  All amounts in millions of dollars.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/index.aspx",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Documents/s1_globl.csv",
-                    "mediaType": "text/csv",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/csv"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/index.aspx",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Documents/s1_globl.txt",
-                    "mediaType": "text/csv",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/csv"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/index.aspx",
                     "downloadURL": "http://www.treasury.gov/ticdata/Publish/s1_globl.tic",
-                    "mediaType": "text/plain",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/plain"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "Treasury International Capital (TIC) - U.S. Transactions with Foreign Residents in Long Term Securities - Gross Foreign Purchases and Sales, by country globally",
-            "description": "Foreign purchases and sales of long-term domestic and foreign securities by type.  Data column titles correspond to column titles in Treasury Bulletin Table CM-VI-4, excluding CM-VI-4 columns (1) and (8).  Refer to CNTRYCDS.TXT file for \"Cntry Code\" identification.  All amounts in millions of dollars.",
+            "identifier": "015-DO-077",
+            "issued": "2014-11-30T00:00:00",
             "keyword": [
                 "Asset Backed securities",
                 "Long term securities",
@@ -3330,47 +3337,47 @@
                 "long term domestic securities",
                 "long term foreign securities"
             ],
+            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/index.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2014-10-01",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Department of the Treasury",
-                "hasEmail": "mailto:Digital@Treasury.gov"
+            "title": "Treasury International Capital (TIC) - U.S. Transactions with Foreign Residents in Long Term Securities - Gross Foreign Purchases and Sales, by country globally"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/index.aspx",
-            "issued": "2014-11-30T00:00:00"
+            "contactPoint": {
+                "fn": "Treasury International Capital (TIC)",
+                "hasEmail": "mailto:digital@treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-081",
+            "description": "Foreign purchases and sales of long-term domestic and foreign securities by type.  Data column titles correspond to column titles in Treasury Bulletin Table CM-VI-4, excluding CM-VI-4 columns (1) and (8).  Refer to CNTRYCDS.TXT file for \"Cntry Code\" identification.  All amounts in millions of dollars.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "downloadURL": "http://www.treasury.gov/ticdata/Publish/s1_other.tic",
-                    "mediaType": "text/plain",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/plain"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "Treasury International Capital (TIC) - U.S. Transactions with Foreign Residents in Long Term Securities - Gross Foreign Purchases and Sales, by country in Africa, International Organizations and Others",
-            "description": "Foreign purchases and sales of long-term domestic and foreign securities by type.  Data column titles correspond to column titles in Treasury Bulletin Table CM-VI-4, excluding CM-VI-4 columns (1) and (8).  Refer to CNTRYCDS.TXT file for \"Cntry Code\" identification.  All amounts in millions of dollars.",
+            "identifier": "015-DO-081",
+            "issued": "2014-11-30T00:00:00",
             "keyword": [
                 "Foreign purchases",
                 "Foreign Sales",
@@ -3388,46 +3395,46 @@
                 "Foreign Bonds",
                 "Foreign Stocks"
             ],
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2014-10-01",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Treasury International Capital (TIC)",
-                "hasEmail": "mailto:digital@treasury.gov"
+            "title": "Treasury International Capital (TIC) - U.S. Transactions with Foreign Residents in Long Term Securities - Gross Foreign Purchases and Sales, by country in Africa, International Organizations and Others"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "issued": "2014-11-30T00:00:00"
+            "contactPoint": {
+                "fn": "Treasury International Capital (TIC)",
+                "hasEmail": "mailto:digital@treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-080",
+            "description": "Foreign purchases and sales of long term domestic and foreign securities by type.  Data column titles correspond to column titles in Treasury Bulletin Table CM-VI-4, excluding CM-VI-4 columns (1) and (8).  Refer to CNTRYCDS.TXT file for \"Cntry Code\" identification.  All amounts in millions of dollars.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "downloadURL": "http://www.treasury.gov/ticdata/Publish/s1_asia.tic",
-                    "mediaType": "text/plain",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/plain"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "Treasury International Capital (TIC) - U.S. Transactions with Foreign Residents in Long Term Securities - Gross Foreign Purchases and Sales, by country in Asia",
-            "description": "Foreign purchases and sales of long term domestic and foreign securities by type.  Data column titles correspond to column titles in Treasury Bulletin Table CM-VI-4, excluding CM-VI-4 columns (1) and (8).  Refer to CNTRYCDS.TXT file for \"Cntry Code\" identification.  All amounts in millions of dollars.",
+            "identifier": "015-DO-080",
+            "issued": "2014-11-30T00:00:00",
             "keyword": [
                 "Foreign purchases",
                 "Foreign Sales",
@@ -3443,46 +3450,46 @@
                 "Foreign Bonds",
                 "Foreign Stocks"
             ],
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2014-10-01",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Treasury International Capital (TIC)",
-                "hasEmail": "mailto:digital@treasury.gov"
+            "title": "Treasury International Capital (TIC) - U.S. Transactions with Foreign Residents in Long Term Securities - Gross Foreign Purchases and Sales, by country in Asia"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "issued": "2014-11-30T00:00:00"
+            "contactPoint": {
+                "fn": "Treasury International Capital (TIC)",
+                "hasEmail": "mailto:digital@treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-078",
+            "description": "Foreign purchases and sales of long-term domestic and foreign securities by type.  Data column titles correspond to column titles in Treasury Bulletin Table CM-VI-4, excluding CM-VI-4 columns (1) and (8).  Refer to CNTRYCDS.TXT file for \"Cntry Code\" identification.  All amounts in millions of dollars.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "downloadURL": "http://www.treasury.gov/ticdata/Publish/s1_europ.tic",
-                    "mediaType": "text/plain",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/plain"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "Treasury International Capital (TIC) - U.S. Transactions with Foreign Residents in Long Term Securities - Gross Foreign Purchases and Sales, by country in Europe and Canada",
-            "description": "Foreign purchases and sales of long-term domestic and foreign securities by type.  Data column titles correspond to column titles in Treasury Bulletin Table CM-VI-4, excluding CM-VI-4 columns (1) and (8).  Refer to CNTRYCDS.TXT file for \"Cntry Code\" identification.  All amounts in millions of dollars.",
+            "identifier": "015-DO-078",
+            "issued": "2014-11-30T00:00:00",
             "keyword": [
                 "Foreign purchases",
                 "Foreign Sales",
@@ -3499,46 +3506,46 @@
                 "Foreign Bonds",
                 "Foreign Stocks"
             ],
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2014-10-01",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Treasury International Capital (TIC)",
-                "hasEmail": "mailto:digital@treasury.gov"
+            "title": "Treasury International Capital (TIC) - U.S. Transactions with Foreign Residents in Long Term Securities - Gross Foreign Purchases and Sales, by country in Europe and Canada"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "issued": "2014-11-30T00:00:00"
+            "contactPoint": {
+                "fn": "Department of the Treasury",
+                "hasEmail": "mailto:Digital@Treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-079",
+            "description": "Foreign purchases and sales of long-term domestic and foreign securities by type.  Data column titles correspond to column titles in Treasury Bulletin Table CM-VI-4, excluding CM-VI-4 columns (1) and (8).  Refer to CNTRYCDS.TXT file for \"Cntry Code\" identification.  All amounts in millions of dollars.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "downloadURL": "http://www.treasury.gov/ticdata/Publish/s1_latam.tic",
-                    "mediaType": "text/plain",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/plain"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "Treasury International Capital (TIC) - U.S. Transactions with Foreign Residents in Long Term Securities - Gross Foreign Purchases and Sales, by country in Latin America and Carribean",
-            "description": "Foreign purchases and sales of long-term domestic and foreign securities by type.  Data column titles correspond to column titles in Treasury Bulletin Table CM-VI-4, excluding CM-VI-4 columns (1) and (8).  Refer to CNTRYCDS.TXT file for \"Cntry Code\" identification.  All amounts in millions of dollars.",
+            "identifier": "015-DO-079",
+            "issued": "2014-11-30T00:00:00",
             "keyword": [
                 "Foreign purchases",
                 "Foreign Sales",
@@ -3555,47 +3562,47 @@
                 "Foreign Bonds",
                 "Foreign Stocks"
             ],
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2014-10-01",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Department of the Treasury",
-                "hasEmail": "mailto:Digital@Treasury.gov"
+            "title": "Treasury International Capital (TIC) - U.S. Transactions with Foreign Residents in Long Term Securities - Gross Foreign Purchases and Sales, by country in Latin America and Carribean"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "issued": "2014-11-30T00:00:00"
+            "contactPoint": {
+                "fn": "Treasury International Capital (TIC)",
+                "hasEmail": "mailto:digital@treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-040",
+            "description": "Treasury International Capital (TIC)\r\n  - U.S. Transactions with Foreign Residents in Long Term Securities\r\n     - Net Foreign Purchases of U.S. long term securities by major foreign sector\r\n        - U.S. Corporate & Other Bonds",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticsec.aspx",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Documents/corpsect.txt",
-                    "mediaType": "text/plain",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/plain"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "Treasury International Capital (TIC) - U.S. Transactions with Foreign Residents in Long Term Securities - Net Foreign Purchases of U.S. long term securities by major foreign sector - U.S. Corporate & Other Bonds",
-            "description": "Treasury International Capital (TIC)\r\n  - U.S. Transactions with Foreign Residents in Long Term Securities\r\n     - Net Foreign Purchases of U.S. long term securities by major foreign sector\r\n        - U.S. Corporate & Other Bonds",
+            "identifier": "015-DO-040",
+            "issued": "2014-11-24T00:00:00",
             "keyword": [
                 "Treasury International Capital",
                 "TIC",
@@ -3603,48 +3610,48 @@
                 "Net Foreign Purchases of U.S. long term securities by major foreign sector",
                 "U.S. Corporate & Other Bonds"
             ],
+            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticsec.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2023-12-08",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Treasury International Capital (TIC)",
-                "hasEmail": "mailto:digital@treasury.gov"
+            "title": "Treasury International Capital (TIC) - U.S. Transactions with Foreign Residents in Long Term Securities - Net Foreign Purchases of U.S. long term securities by major foreign sector - U.S. Corporate & Other Bonds"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticsec.aspx",
-            "issued": "2014-11-24T00:00:00"
+            "contactPoint": {
+                "fn": "Treasury International Capital (TIC)",
+                "hasEmail": "mailto:digital@treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-041",
+            "description": "Treasury International Capital (TIC)\r\n - U.S. Transactions with Foreign Residents in Long Term Securities\r\n    - Net Foreign Purchases of U.S. long term securities by major foreign sector\r\n       - U.S. Stocks",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticsec.aspx",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Documents/stksect.txt",
-                    "mediaType": "text/plain",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/plain"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "Treasury International Capital (TIC) - U.S. Transactions with Foreign Residents in Long Term Securities - Net Foreign Purchases of U.S. long term securities by major foreign sector - U.S. Stocks",
-            "description": "Treasury International Capital (TIC)\r\n - U.S. Transactions with Foreign Residents in Long Term Securities\r\n    - Net Foreign Purchases of U.S. long term securities by major foreign sector\r\n       - U.S. Stocks",
+            "identifier": "015-DO-041",
+            "issued": "2014-11-24T00:00:00",
             "keyword": [
                 "Treasury International Capital",
                 "TIC",
@@ -3652,150 +3659,150 @@
                 "Net Foreign Purchases of U.S. long term securities by major foreign sector",
                 "U.S. Stocks"
             ],
+            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticsec.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2023-12-08",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Treasury International Capital (TIC)",
-                "hasEmail": "mailto:digital@treasury.gov"
+            "title": "Treasury International Capital (TIC) - U.S. Transactions with Foreign Residents in Long Term Securities - Net Foreign Purchases of U.S. long term securities by major foreign sector - U.S. Stocks"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticsec.aspx",
-            "issued": "2014-11-24T00:00:00"
+            "contactPoint": {
+                "fn": "Treasury International Capital",
+                "hasEmail": "mailto:digital@treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-026",
+            "description": "Treasury International Capital (TIC): \r\n   - U.S. Transactions with Foreign Residents in Long Term Securities\r\n       - Net Foreign Purchases of U.S. long-term securities by major foreign sector \r\n           - U.S. Gov't Corp. & Federally-sponsored Agency Bonds",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticsec.aspx",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Documents/agnsect.txt",
-                    "mediaType": "text/plain",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/plain"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "Treasury International Capital (TIC) - U.S. Transactions with Foreign Residents in Long Term Securities - Net Foreign Purchases of U.S. long-term securities by major foreign sector - U.S. Gov't Corp. & Federally-sponsored Agency Bonds",
-            "description": "Treasury International Capital (TIC): \r\n   - U.S. Transactions with Foreign Residents in Long Term Securities\r\n       - Net Foreign Purchases of U.S. long-term securities by major foreign sector \r\n           - U.S. Gov't Corp. & Federally-sponsored Agency Bonds",
+            "identifier": "015-DO-026",
             "keyword": [
                 "Treasury International Capital",
                 "TIC",
                 "U.S. International Portfolio Investment",
                 "Long-Term Securities"
             ],
+            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticsec.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2014-02-28",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Treasury International Capital",
-                "hasEmail": "mailto:digital@treasury.gov"
+            "references": [
+                "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticfaq1.aspx"
+            ],
+            "title": "Treasury International Capital (TIC) - U.S. Transactions with Foreign Residents in Long Term Securities - Net Foreign Purchases of U.S. long-term securities by major foreign sector - U.S. Gov't Corp. & Federally-sponsored Agency Bonds"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticsec.aspx",
-            "references": [
-                "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticfaq1.aspx"
-            ]
+            "contactPoint": {
+                "fn": "Treasury International Capital",
+                "hasEmail": "mailto:digital@treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-027",
+            "description": "Special Series for U.S. Securities. \r\nNet Foreign Purchases of U.S. long-term securities by major foreign sector - U.S. Treasury Bonds & Notes",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticsec.aspx",
                     "downloadURL": "http://www.treasury.gov/ticdata/Publish/tressect.txt",
-                    "mediaType": "text/plain",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/plain"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "Treasury International Capital (TIC) - U.S. Transactions with Foreign Residents in Long Term Securities - Net Foreign Purchases of U.S. long-term securities by major foreign sector - U.S. Treasury Bonds & Notes",
-            "description": "Special Series for U.S. Securities. \r\nNet Foreign Purchases of U.S. long-term securities by major foreign sector - U.S. Treasury Bonds & Notes",
+            "identifier": "015-DO-027",
             "keyword": [
                 "Treasury International Capital",
                 "TIC",
                 "1.U.S. Treasury Bonds & Notes"
             ],
+            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticsec.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2014-01-01",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Treasury International Capital",
-                "hasEmail": "mailto:digital@treasury.gov"
+            "title": "Treasury International Capital (TIC) - U.S. Transactions with Foreign Residents in Long Term Securities - Net Foreign Purchases of U.S. long-term securities by major foreign sector - U.S. Treasury Bonds & Notes"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticsec.aspx"
+            "contactPoint": {
+                "fn": "Department of the Treasury",
+                "hasEmail": "mailto:Digital@Treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-071",
+            "description": "Net Transactions in Foreign Long-Term Securities by US Residents, millions of dollars, as of:  September 2014.  Negative entries indicate net U.S. purchases of foreign securities, or an outflow of capital from the United States.  Positive entries indicate U.S. sales of foreign securities",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticsec.aspx",
                     "downloadURL": "http://www.treasury.gov/ticdata/Publish/snetfor.txt",
-                    "mediaType": "text/plain",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/plain"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticsec.aspx",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Documents/snetfor.csv",
-                    "mediaType": "text/csv",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/csv"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "Treasury International Capital (TIC) - U.S. Transactions with Foreign Residents in Long Term Securities - Net purchases of Foreign long term securities (Monthly)",
-            "description": "Net Transactions in Foreign Long-Term Securities by US Residents, millions of dollars, as of:  September 2014.  Negative entries indicate net U.S. purchases of foreign securities, or an outflow of capital from the United States.  Positive entries indicate U.S. sales of foreign securities",
+            "identifier": "015-DO-071",
+            "issued": "2014-11-30T00:00:00",
             "keyword": [
                 "Foreign Long Term Securities",
                 "Foreign Stocks",
@@ -3803,162 +3810,162 @@
                 "Asset Backed securities",
                 "US resident purchases of Securities"
             ],
+            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticsec.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2014-06-18",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Department of the Treasury",
-                "hasEmail": "mailto:Digital@Treasury.gov"
+            "title": "Treasury International Capital (TIC) - U.S. Transactions with Foreign Residents in Long Term Securities - Net purchases of Foreign long term securities (Monthly)"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticsec.aspx",
-            "issued": "2014-11-30T00:00:00"
+            "contactPoint": {
+                "fn": "Department of the Treasury",
+                "hasEmail": "mailto:Digital@Treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-072",
+            "description": "Net Transactions in Foreign Long-Term Securities by US Residents, millions of dollars, as of:  September 2014.  Negative entries indicate net U.S. purchases of foreign securities, or an outflow of capital from the United States.  Positive entries indicate U.S. sales of foreign securities",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticsec.aspx",
                     "downloadURL": "http://www.treasury.gov/ticdata/Publish/snetforq.txt",
-                    "mediaType": "text/plain",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/plain"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticsec.aspx",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Documents/snetforq.csv",
-                    "mediaType": "text/csv",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/csv"
                 }
             ],
-            "accrualPeriodicity": "R/P3M",
-            "title": "Treasury International Capital (TIC) - U.S. Transactions with Foreign Residents in Long Term Securities - Net purchases of Foreign long term securities (Quarterly)",
-            "description": "Net Transactions in Foreign Long-Term Securities by US Residents, millions of dollars, as of:  September 2014.  Negative entries indicate net U.S. purchases of foreign securities, or an outflow of capital from the United States.  Positive entries indicate U.S. sales of foreign securities",
+            "identifier": "015-DO-072",
+            "issued": "2014-11-30T00:00:00",
             "keyword": [
                 "Foreign Long Term Securities",
                 "Foreign Bonds",
                 "Foreign Stocks",
                 "US resident purchases of foreign securities."
             ],
+            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticsec.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2014-10-31",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Department of the Treasury",
-                "hasEmail": "mailto:Digital@Treasury.gov"
+            "title": "Treasury International Capital (TIC) - U.S. Transactions with Foreign Residents in Long Term Securities - Net purchases of Foreign long term securities (Quarterly)"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticsec.aspx",
-            "issued": "2014-11-30T00:00:00"
+            "contactPoint": {
+                "fn": "Treasury International Capital (TIC)",
+                "hasEmail": "mailto:digital@treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-046",
+            "description": "Treasury International Capital (TIC)\r\n - U.S. Transactions with Foreign Residents in Long Term Securities\r\n   - Other Acquisitions of U.S. Long term Securities\r\n     - (REVISED 11-16-2012) Estimates by the Federal Reserve Bank of New York of unrecorded principal repayments to foreigners on domestic corporate and agency asset-backed securities (ABS).",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/absprin.aspx",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Documents/absdata.txt",
-                    "mediaType": "text/plain",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/plain"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/absprin.aspx",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Documents/absdata.csv",
-                    "mediaType": "text/csv",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/csv"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Treasury International Capital (TIC) - U.S. Transactions with Foreign Residents in Long Term Securities - Other Acquisitions of U.S. Long term Securities - Estimates by the Federal Reserve Bank of New York of unrecorded principal repayments to foreigners",
-            "description": "Treasury International Capital (TIC)\r\n - U.S. Transactions with Foreign Residents in Long Term Securities\r\n   - Other Acquisitions of U.S. Long term Securities\r\n     - (REVISED 11-16-2012) Estimates by the Federal Reserve Bank of New York of unrecorded principal repayments to foreigners on domestic corporate and agency asset-backed securities (ABS).",
+            "identifier": "015-DO-046",
+            "issued": "2014-11-24T00:00:00",
             "keyword": [
                 "Treasury International Capital",
                 "TIC",
                 "U.S. Transactions with Foreign Residents in Long Term Securities",
                 "Other Acquisitions of U.S. Long term Securities"
             ],
+            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/absprin.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2012-11-16",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Treasury International Capital (TIC)",
-                "hasEmail": "mailto:digital@treasury.gov"
+            "title": "Treasury International Capital (TIC) - U.S. Transactions with Foreign Residents in Long Term Securities - Other Acquisitions of U.S. Long term Securities - Estimates by the Federal Reserve Bank of New York of unrecorded principal repayments to foreigners"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/absprin.aspx",
-            "issued": "2014-11-24T00:00:00"
+            "contactPoint": {
+                "fn": "Treasury International Capital (TIC)",
+                "hasEmail": "mailto:digital@treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-047",
+            "description": "Treasury International Capital (TIC)\r\n - U.S. Transactions with Foreign Residents in Long Term Securities\r\n   - Other Acquisitions of U.S. Long-term Securities\r\n    - Estimated foreign portfolio acquisitions of U.S. stocks through stock swaps",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/swapstk.aspx",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Documents/swapdata.txt",
-                    "mediaType": "text/plain",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/plain"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/swapstk.aspx",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Documents/swapdata.csv",
-                    "mediaType": "text/csv",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/csv"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Treasury International Capital (TIC) - U.S. Transactions with Foreign Residents in Long Term Securities - Other Acquisitions of U.S. Long-term Securities - Estimated foreign portfolio acquisitions of U.S. stocks",
-            "description": "Treasury International Capital (TIC)\r\n - U.S. Transactions with Foreign Residents in Long Term Securities\r\n   - Other Acquisitions of U.S. Long-term Securities\r\n    - Estimated foreign portfolio acquisitions of U.S. stocks through stock swaps",
+            "identifier": "015-DO-047",
+            "issued": "2014-11-24T00:00:00",
             "keyword": [
                 "Treasury International Capital",
                 "TIC",
@@ -3966,54 +3973,54 @@
                 "Other Acquisitions of U.S. Long-term Securities",
                 "Estimated foreign portfolio acquisitions of U.S. stocks"
             ],
+            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/swapstk.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2007-09-06",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Treasury International Capital (TIC)",
-                "hasEmail": "mailto:digital@treasury.gov"
+            "title": "Treasury International Capital (TIC) - U.S. Transactions with Foreign Residents in Long Term Securities - Other Acquisitions of U.S. Long-term Securities - Estimated foreign portfolio acquisitions of U.S. stocks"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/swapstk.aspx",
-            "issued": "2014-11-24T00:00:00"
+            "contactPoint": {
+                "fn": "Treasury International Capital (TIC)",
+                "hasEmail": "mailto:digital@treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-070",
+            "description": "Foreign Net Purchases of U.S. Long-Term Securities, Millions of Dollars as of:  September 2014",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticsec.aspx",
                     "downloadURL": "http://www.treasury.gov/ticdata/Publish/snetusq.txt",
-                    "mediaType": "text/plain",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/plain"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticsec.aspx",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Documents/snetusq.csv",
-                    "mediaType": "text/csv",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/csv"
                 }
             ],
-            "accrualPeriodicity": "R/P3M",
-            "title": "Treasury International Capital (TIC) - U.S. Transactions with Foreign Residents in Long Term Securities - Recent Net Foreign Purchases by Country (Quarterly)",
-            "description": "Foreign Net Purchases of U.S. Long-Term Securities, Millions of Dollars as of:  September 2014",
+            "identifier": "015-DO-070",
+            "issued": "2014-11-30T00:00:00",
             "keyword": [
                 "Long Term Securities",
                 "Treasury Bonds",
@@ -4021,48 +4028,48 @@
                 "Corporate Stocks",
                 "Foreign Residents"
             ],
+            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticsec.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2014-06-18",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Treasury International Capital (TIC)",
-                "hasEmail": "mailto:digital@treasury.gov"
+            "title": "Treasury International Capital (TIC) - U.S. Transactions with Foreign Residents in Long Term Securities - Recent Net Foreign Purchases by Country (Quarterly)"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticsec.aspx",
-            "issued": "2014-11-30T00:00:00"
+            "contactPoint": {
+                "fn": "Treasury International Capital (TIC)",
+                "hasEmail": "mailto:digital@treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-048",
+            "description": "Treasury International Capital (TIC)\r\n - U.S. Transactions with Foreign Residents in Long Term Securities\r\n   - Special Series for Foreign Securities\r\n     - Net Purchases of Foreign Long term Securities by type of foreign security",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticsec.aspx",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Documents/netfsec.txt",
-                    "mediaType": "text/plain",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/plain"
                 }
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "title": "Treasury International Capital (TIC) - U.S. Transactions with Foreign Residents in Long Term Securities - Special Series for Foreign Securities - Net Purchases of Foreign Long term Securities by type of foreign security",
-            "description": "Treasury International Capital (TIC)\r\n - U.S. Transactions with Foreign Residents in Long Term Securities\r\n   - Special Series for Foreign Securities\r\n     - Net Purchases of Foreign Long term Securities by type of foreign security",
+            "identifier": "015-DO-048",
+            "issued": "2014-11-24T00:00:00",
             "keyword": [
                 "Treasury International Capital",
                 "TIC",
@@ -4070,101 +4077,101 @@
                 "Special Series for Foreign Securities",
                 "Net Purchases of Foreign Long term Securities by type of foreign security"
             ],
+            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticsec.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2023-12-08",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Treasury International Capital (TIC)",
-                "hasEmail": "mailto:digital@treasury.gov"
+            "title": "Treasury International Capital (TIC) - U.S. Transactions with Foreign Residents in Long Term Securities - Special Series for Foreign Securities - Net Purchases of Foreign Long term Securities by type of foreign security"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticsec.aspx",
-            "issued": "2014-11-24T00:00:00"
+            "contactPoint": {
+                "fn": "Department of the Treasury",
+                "hasEmail": "mailto:Digital@Treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-076",
+            "description": "Foreign purchases and sales of long-term domestic and foreign securities by type.  Data column titles correspond to column titles in Treasury Bulletin Table CM-VI-4, excluding CM-VI-4 columns (1) and (8).  All Countries and IROs (99996)  All amounts in millions of dollars.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticsec.aspx",
                     "downloadURL": "http://www.treasury.gov/ticdata/Publish/s1_99996.txt",
-                    "mediaType": "text/plain",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/plain"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Treasury International Capital (TIC) - U.S. Transactions with Foreign Residents in Long Term Securities Gross Foreign Purchases and Sales, by country grand total",
-            "description": "Foreign purchases and sales of long-term domestic and foreign securities by type.  Data column titles correspond to column titles in Treasury Bulletin Table CM-VI-4, excluding CM-VI-4 columns (1) and (8).  All Countries and IROs (99996)  All amounts in millions of dollars.",
+            "identifier": "015-DO-076",
+            "issued": "2014-11-30T00:00:00",
             "keyword": [
                 "Asset backed securities",
                 "gross purchases by foreigners from US Residents",
                 "gross sales by foreigners to US Residents"
             ],
+            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticsec.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2014-06-18",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Department of the Treasury",
-                "hasEmail": "mailto:Digital@Treasury.gov"
+            "title": "Treasury International Capital (TIC) - U.S. Transactions with Foreign Residents in Long Term Securities Gross Foreign Purchases and Sales, by country grand total"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticsec.aspx",
-            "issued": "2014-11-30T00:00:00"
+            "contactPoint": {
+                "fn": "Treasury International Capital (TIC)",
+                "hasEmail": "mailto:digital@treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-069",
+            "description": "U.S. Transactions with Foreign-Residents in Long-Term Securities - Recent Net Foreign Purchases, by country. The data is collated by month.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticsec.aspx",
                     "downloadURL": "http://www.treasury.gov/ticdata/Publish/snetus.txt",
-                    "mediaType": "text/plain",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/plain"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticsec.aspx",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Documents/snetus.csv",
-                    "mediaType": "text/csv",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/csv"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "Treasury International Capital (TIC) - U.S. Transactions with Foreign Residents in LongTerm Securities - Recent Net Foreign Purchases by Country (Monthly)",
-            "description": "U.S. Transactions with Foreign-Residents in Long-Term Securities - Recent Net Foreign Purchases, by country. The data is collated by month.",
+            "identifier": "015-DO-069",
+            "issued": "2014-11-30T00:00:00",
             "keyword": [
                 "Foreign residents",
                 "Long term securities",
@@ -4172,48 +4179,48 @@
                 "corporate bonds",
                 "corporate stocks"
             ],
+            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticsec.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2014-06-18",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Treasury International Capital (TIC)",
-                "hasEmail": "mailto:digital@treasury.gov"
+            "title": "Treasury International Capital (TIC) - U.S. Transactions with Foreign Residents in LongTerm Securities - Recent Net Foreign Purchases by Country (Monthly)"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticsec.aspx",
-            "issued": "2014-11-30T00:00:00"
+            "contactPoint": {
+                "fn": "Department of the Treasury",
+                "hasEmail": "mailto:Digital@Treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-084",
+            "description": "Foreign holdings of U.S. securities, and U.S. holdings of foreign securities.  Major foreign holders of US Securities.  Monthly Holdings of U.S. Long-term Securities at Current Market Value by Foreign Residents.  Monthly Holdings of Foreign Long-term Securities at Current Market Value by U.S. Residents.  Includes: Total holdings by all U.S. residents; by type, holder and issuer.  U.S. holdings by country of issuer (files include both recent and historical data).  Monthly Holdings of Short-term Debt.  Types of foreign portfolio investment in the United States (quarterly). Total U.S. banking & securities liabilities to foreign residents",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticsec2.aspx",
                     "downloadURL": "https://www.treasury.gov/resource-center/data-chart-center/tic/Documents/mfh.txt",
-                    "mediaType": "text/plain",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/plain"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Treasury International Capital: Securities (B): Portfolio Holdings of U.S and Foreign Securities",
-            "description": "Foreign holdings of U.S. securities, and U.S. holdings of foreign securities.  Major foreign holders of US Securities.  Monthly Holdings of U.S. Long-term Securities at Current Market Value by Foreign Residents.  Monthly Holdings of Foreign Long-term Securities at Current Market Value by U.S. Residents.  Includes: Total holdings by all U.S. residents; by type, holder and issuer.  U.S. holdings by country of issuer (files include both recent and historical data).  Monthly Holdings of Short-term Debt.  Types of foreign portfolio investment in the United States (quarterly). Total U.S. banking & securities liabilities to foreign residents",
+            "identifier": "015-DO-084",
+            "issued": "2015-02-28T00:00:00",
             "keyword": [
                 "Foreign Holdings",
                 "US Securities",
@@ -4221,205 +4228,204 @@
                 "US Resident",
                 "Foreign Resident"
             ],
+            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticsec2.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2014-06-16",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Department of the Treasury",
-                "hasEmail": "mailto:Digital@Treasury.gov"
+            "title": "Treasury International Capital: Securities (B): Portfolio Holdings of U.S and Foreign Securities"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/tic/Pages/ticsec2.aspx",
-            "issued": "2015-02-28T00:00:00"
+            "contactPoint": {
+                "fn": "Digital Treasury",
+                "hasEmail": "mailto:Digital@Treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-128",
+            "description": "Treasury Cost Savings and Avoidance from 2012 to 2018",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "downloadURL": "https://www.treasury.gov/jsonfiles/costsavings.json",
-                    "mediaType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/json"
                 }
             ],
-            "accrualPeriodicity": "R/P3M",
-            "title": "Treasury IT Reform Cost Savings/ Avoidance",
-            "description": "Treasury Cost Savings and Avoidance from 2012 to 2018",
+            "identifier": "015-DO-128",
+            "issued": "2015-11-30T00:00:00",
             "keyword": [
                 "Cost Savings",
                 "Cost Avoidance"
             ],
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2015-11-30",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Digital Treasury",
-                "hasEmail": "mailto:Digital@Treasury.gov"
+            "title": "Treasury IT Reform Cost Savings/ Avoidance"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "issued": "2015-11-30T00:00:00"
+            "contactPoint": {
+                "fn": "Office of Business Affairs and Public Liaison",
+                "hasEmail": "mailto:OfficeofBusinessAffairsandPublicLiaison@treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-051",
+            "description": "Treasury's official blog, featuring blog posts from Treasury's senior officials and staff sharing news, announcements and information about the work done at the Treasury Department.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "downloadURL": "http://www.treasury.gov/rss/Pages/RSS.aspx?config=TreasuryNotes",
-                    "mediaType": "application/rss+xml",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/rss+xml"
                 }
             ],
-            "accrualPeriodicity": "R/P1D",
-            "title": "Treasury Notes And Blog Posts",
-            "description": "Treasury's official blog, featuring blog posts from Treasury's senior officials and staff sharing news, announcements and information about the work done at the Treasury Department.",
+            "identifier": "015-DO-051",
             "keyword": [
                 "Treasury Notes",
                 "Blogs",
                 "News",
                 "Announcements"
             ],
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2014-08-29",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Office of Business Affairs and Public Liaison",
-                "hasEmail": "mailto:OfficeofBusinessAffairsandPublicLiaison@treasury.gov"
+            "title": "Treasury Notes And Blog Posts"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/"
+            "contactPoint": {
+                "fn": "Office of Business Affairs and Public Liaison",
+                "hasEmail": "mailto:OfficeofBusinessAffairsandPublicLiaison@treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-052",
+            "description": "Department of the Treasury press releases",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/press-center/press-releases/Pages/default.aspx",
                     "downloadURL": "http://www.treasury.gov/press-center/press-releases/Pages/default.aspx",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1D",
-            "title": "Treasury Press Releases",
-            "description": "Department of the Treasury press releases",
+            "identifier": "015-DO-052",
             "keyword": [
                 "Press Release"
             ],
+            "landingPage": "http://www.treasury.gov/press-center/press-releases/Pages/default.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2014-08-29",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of the Treasury",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Department of the Treasury"
-            },
-            "contactPoint": {
-                "fn": "Office of Business Affairs and Public Liaison",
-                "hasEmail": "mailto:OfficeofBusinessAffairsandPublicLiaison@treasury.gov"
+            "title": "Treasury Press Releases"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:00"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/press-center/press-releases/Pages/default.aspx"
+            "contactPoint": {
+                "fn": "Office of Financial Stability",
+                "hasEmail": "mailto:digital@treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-DO-011",
+            "description": "The Department of the Treasury has significant responsibilities related to the Recovery Act. Treasury has nine programs - including several initiatives involving tax changes that will affect almost all Americans, and will deliver an estimated $150 billion of direct relief to Americans and their families. This dataset provided a state-by-state dataset related to each of the programs.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/recovery-act/Pages/Recovery-Act-Data-Visualization.aspx",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/recovery-act/Documents/Treasury%20Recovery%20Act%20Data%20as%20of%207-31-2010.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.ms-excel"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/recovery-act/Pages/Recovery-Act-Data-Visualization.aspx",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/recovery-act/Documents/Treasury%20Recovery%20Act%20Data%20as%20of%209-30-2010.xls",
-                    "mediaType": "application/vnd.ms-excel",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.ms-excel"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/recovery-act/Pages/Recovery-Act-Data-Visualization.aspx",
                     "downloadURL": "http://data.treasury.gov/feed.svc/RecoveryData",
-                    "mediaType": "application/rss+xml",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/rss+xml"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/recovery-act/Pages/Recovery-Act-Data-Visualization.aspx",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/recovery-act/Datasets/ARRA.09.30.2010.xml",
-                    "mediaType": "text/xml",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/xml"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/resource-center/data-chart-center/recovery-act/Pages/Recovery-Act-Data-Visualization.aspx",
                     "downloadURL": "http://www.treasury.gov/resource-center/data-chart-center/recovery-act/Pages/TextView.aspx?data=arra&month=9&day=30&year=2010",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Treasury Recovery Act Data",
-            "description": "The Department of the Treasury has significant responsibilities related to the Recovery Act. Treasury has nine programs - including several initiatives involving tax changes that will affect almost all Americans, and will deliver an estimated $150 billion of direct relief to Americans and their families. This dataset provided a state-by-state dataset related to each of the programs.",
+            "identifier": "015-DO-011",
             "keyword": [
                 "recovery act",
                 "2009",
@@ -4431,92 +4437,92 @@
                 "homebuyer",
                 "low-income housing"
             ],
+            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/recovery-act/Pages/Recovery-Act-Data-Visualization.aspx",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2013-11-01",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Office of Financial Stability",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "DO",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "DO"
-                },
-                "name": "Office of Financial Stability"
-            },
-            "contactPoint": {
-                "fn": "Office of Financial Stability",
-                "hasEmail": "mailto:digital@treasury.gov"
+            "title": "Treasury Recovery Act Data"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
-                "015:00"
-            ],
-            "programCode": [
-                "015:000"
+                "015:04"
             ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/resource-center/data-chart-center/recovery-act/Pages/Recovery-Act-Data-Visualization.aspx"
+            "contactPoint": {
+                "fn": "Financial Crimes Enforcement Network",
+                "hasEmail": "mailto:FRC@fincen.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-FinCEN-004",
+            "description": "As part of fulfilling its mission to safeguard the financial system and promote national security, FinCEN, through its Financial Institution Advisory Program, issues public and non-public advisories to financial institutions concerning money laundering or terrorist financing threats and vulnerabilities for the purpose of enabling financial institutions to guard against such threats.  Advisories often contain illicit activity typologies, red flags that facilitate monitoring, and guidance on complying with FinCEN regulations to address those threats and vulnerabilities.  Financial institutions may use this information to enhance their Anti-Money Laundering (AML) monitoring systems for more valuable suspicious activity reporting.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "downloadURL": "https://www.fincen.gov/resources/advisoriesbulletinsfact-sheets",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "FinCEN Advisories/Bulletins/Fact Sheets",
-            "description": "As part of fulfilling its mission to safeguard the financial system and promote national security, FinCEN, through its Financial Institution Advisory Program, issues public and non-public advisories to financial institutions concerning money laundering or terrorist financing threats and vulnerabilities for the purpose of enabling financial institutions to guard against such threats.  Advisories often contain illicit activity typologies, red flags that facilitate monitoring, and guidance on complying with FinCEN regulations to address those threats and vulnerabilities.  Financial institutions may use this information to enhance their Anti-Money Laundering (AML) monitoring systems for more valuable suspicious activity reporting.",
+            "identifier": "015-FinCEN-004",
+            "issued": "2016-10-25T00:00:00",
             "keyword": [
                 "FinCEN",
                 "Financial Institution Advisory Program",
                 "money laundering",
                 "terrorist financing"
             ],
+            "license": "http://opendefinition.org/licenses/cc-zero/",
             "modified": "2023-12-08",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Financial Crimes Enforcement Network",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "FinCEN",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "FinCEN"
-                },
-                "name": "Financial Crimes Enforcement Network"
-            },
-            "contactPoint": {
-                "fn": "Financial Crimes Enforcement Network",
-                "hasEmail": "mailto:FRC@fincen.gov"
+            "title": "FinCEN Advisories/Bulletins/Fact Sheets"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:04"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://opendefinition.org/licenses/cc-zero/",
-            "issued": "2016-10-25T00:00:00"
+            "contactPoint": {
+                "fn": "Financial Crimes Enforcement Network",
+                "hasEmail": "mailto:frc@FinCEN.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-FinCEN-002",
+            "description": "Under the Bank Secrecy Act (BSA), 31 U.S.C. 5311 et seq., and its implementing regulations at 31 C.F.R. Chapter X (formerly 31 C.F.R. Part 103), FinCEN may bring an enforcement action for violations of the reporting, recordkeeping, or other requirements of the BSA. FinCEN's Office of Enforcement evaluates enforcement matters that may result in a variety of remedies, including the assessment of civil money penalties. For example, civil money penalties may be assessed for recordkeeping violations under 31 C.F.R \u00a71010.415 (formerly 31 C.F.R. \u00a7103.29), or for reporting violations for failing to file a currency transaction report (CTR) in violation of 31 C.F.R. \u00a71010.311 (formerly 31 C.F.R. \u00a7103.22), a suspicious activity report (SAR) in violation of 31 C.F.R. \u00a7 1021.320 (formerly 31 C.F.R. \u00a7103.21), or a report of foreign bank and financial accounts (FBAR) in violation of 31 C.F.R \u00a71010.350 (formerly 31 C.F.R. \u00a7103.24). FinCEN also takes enforcement actions against money services businesses (MSBs) for failure to register with FinCEN in violation of 31 C.F.R \u00a71022.380 (formerly 31 C.F.R. \u00a7103.41).",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "downloadURL": "https://www.fincen.gov/news-room/enforcement-actions",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "FinCEN Enforcement Actions for Violations of the Bank Secrecy Act",
-            "description": "Under the Bank Secrecy Act (BSA), 31 U.S.C. 5311 et seq., and its implementing regulations at 31 C.F.R. Chapter X (formerly 31 C.F.R. Part 103), FinCEN may bring an enforcement action for violations of the reporting, recordkeeping, or other requirements of the BSA. FinCEN's Office of Enforcement evaluates enforcement matters that may result in a variety of remedies, including the assessment of civil money penalties. For example, civil money penalties may be assessed for recordkeeping violations under 31 C.F.R \u00a71010.415 (formerly 31 C.F.R. \u00a7103.29), or for reporting violations for failing to file a currency transaction report (CTR) in violation of 31 C.F.R. \u00a71010.311 (formerly 31 C.F.R. \u00a7103.22), a suspicious activity report (SAR) in violation of 31 C.F.R. \u00a7 1021.320 (formerly 31 C.F.R. \u00a7103.21), or a report of foreign bank and financial accounts (FBAR) in violation of 31 C.F.R \u00a71010.350 (formerly 31 C.F.R. \u00a7103.24). FinCEN also takes enforcement actions against money services businesses (MSBs) for failure to register with FinCEN in violation of 31 C.F.R \u00a71022.380 (formerly 31 C.F.R. \u00a7103.41).",
+            "identifier": "015-FinCEN-002",
             "keyword": [
                 "financial crimes enforcement network",
                 "fincen",
@@ -4535,136 +4541,136 @@
                 "record keeping violations",
                 "office of enforcement"
             ],
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2016-10-03",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Financial Crimes Enforcement Network",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "FinCEN",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "FinCEN"
-                },
-                "name": "Financial Crimes Enforcement Network"
-            },
-            "contactPoint": {
-                "fn": "Financial Crimes Enforcement Network",
-                "hasEmail": "mailto:frc@FinCEN.gov"
+            "title": "FinCEN Enforcement Actions for Violations of the Bank Secrecy Act"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:04"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/"
+            "contactPoint": {
+                "fn": "Financial Crimes Enforcement Network",
+                "hasEmail": "mailto:FRC@fincen.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-FinCEN-006",
+            "description": "The MSB Registrant Search Web page contains entities that have registered as Money Services Businesses (MSBs) pursuant to the Bank Secrecy Act (BSA) regulations at 31 CFR 1022.380(a)-(f), administered by the Financial Crimes Enforcement Network (FinCEN). The MSB Registrant Search Web page reflects information exactly as provided by the registrant. Posted entries should include: (1) Registrant's legal name, (2) Registrant's \"doing business as\" name (if applicable), (3) Registrant's address, (4) MSB activities in which the Registrant engages, (5) states in which the Registrant engages in MSB activities, (6) number of branches, (7) date the registration form was signed, and (8) date the registration form was received.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "downloadURL": "https://www.fincen.gov/financial_institutions/msb/msbstateselector.html",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Money Services Business (MSB) Registrant Search",
-            "description": "The MSB Registrant Search Web page contains entities that have registered as Money Services Businesses (MSBs) pursuant to the Bank Secrecy Act (BSA) regulations at 31 CFR 1022.380(a)-(f), administered by the Financial Crimes Enforcement Network (FinCEN). The MSB Registrant Search Web page reflects information exactly as provided by the registrant. Posted entries should include: (1) Registrant's legal name, (2) Registrant's \"doing business as\" name (if applicable), (3) Registrant's address, (4) MSB activities in which the Registrant engages, (5) states in which the Registrant engages in MSB activities, (6) number of branches, (7) date the registration form was signed, and (8) date the registration form was received.",
+            "identifier": "015-FinCEN-006",
+            "issued": "2016-10-31T00:00:00",
             "keyword": [
                 "Money Services Business (MSB) Registrant",
                 "MSB Registrant",
                 "FinCEN"
             ],
+            "license": "http://opendefinition.org/licenses/cc-zero/",
             "modified": "2016-10-31",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Financial Crimes Enforcement Network",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "FinCEN",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "FinCEN"
-                },
-                "name": "Financial Crimes Enforcement Network"
-            },
-            "contactPoint": {
-                "fn": "Financial Crimes Enforcement Network",
-                "hasEmail": "mailto:FRC@fincen.gov"
+            "title": "Money Services Business (MSB) Registrant Search"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:04"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://opendefinition.org/licenses/cc-zero/",
-            "issued": "2016-10-31T00:00:00"
+            "contactPoint": {
+                "fn": "Financial Crimes Enforcement Network",
+                "hasEmail": "mailto:FRC@fincen.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-FinCEN-005",
+            "description": "Suspicious Activity Report (SAR) Advisory Key Terms is a consolidated listing of these SAR narrative key terms and a link to the related FinCEN advisory/other publication. This list will be updated as new advisories are published.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "downloadURL": "https://www.fincen.gov/suspicious-activity-report-sar-advisory-key-terms",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Suspicious Activity Report (SAR) Advisory Key Terms",
-            "description": "Suspicious Activity Report (SAR) Advisory Key Terms is a consolidated listing of these SAR narrative key terms and a link to the related FinCEN advisory/other publication. This list will be updated as new advisories are published.",
+            "identifier": "015-FinCEN-005",
+            "issued": "2016-10-26T00:00:00",
             "keyword": [
                 "Suspicious Activity Report",
                 "SAR",
                 "FinCEN"
             ],
+            "license": "http://opendefinition.org/licenses/cc-zero/",
             "modified": "2016-10-26",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Financial Crimes Enforcement Network",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "FinCEN",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "FinCEN"
-                },
-                "name": "Financial Crimes Enforcement Network"
-            },
-            "contactPoint": {
-                "fn": "Financial Crimes Enforcement Network",
-                "hasEmail": "mailto:FRC@fincen.gov"
+            "title": "Suspicious Activity Report (SAR) Advisory Key Terms"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:04"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://opendefinition.org/licenses/cc-zero/",
-            "issued": "2016-10-26T00:00:00"
+            "contactPoint": {
+                "fn": "Financial Crimes Enforcement Network",
+                "hasEmail": "mailto:FRC@fincen.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-FinCEN-001",
+            "description": "Suspicious Activity Report (SAR) statistics generated by this tool solely reflect the data submitted on FinCEN Form 111. Use of this form for FinCEN SARs was voluntary during the period of March 1, 2012 through March 31, 2013 and mandatory starting on April 1, 2013. FinCEN Form 111 has replaced the individual legacy SAR types formerly filed on TD F 90-22.47 (Depository Institutions), FinCEN Form 109 (Money Services Business), FinCEN Form 102 (Casinos & Card Clubs), and FinCEN Form 101 (Securities & Futures Industries). The statistics are based on the Bank Secrecy Act Identification Number of each record within the SAR system. The Bank Secrecy Act Identification Number is a unique number assigned to each SAR submitted. Statistical data for SARs are updated as information is processed and refreshed data is periodically made available for this tool. For this reason, there may be discrepancies between the statistical figures returned from queries performed at different times. In addition, slight differences in query criteria may return different statistical results. Also note that the statistics generated by this tool do not include SAR fields that contain unknown or blank data. To the extent statistics including blank or unknown data are tabulated outside of this tool for other purposes, there may be discrepancies between statistics generated by this tool and those generated through other means. FinCEN makes no claims, promises or guarantees about the accuracy or completeness of the statistical figures provided from this tool and expressly disclaims liability for errors, omissions, or discrepancies in the statistical figures.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.fincen.gov/reports/sar-stats",
                     "downloadURL": "https://www.fincen.gov/reports/sar-stats",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "Suspicious Activity Report Statistics (SAR Stats)",
-            "description": "Suspicious Activity Report (SAR) statistics generated by this tool solely reflect the data submitted on FinCEN Form 111. Use of this form for FinCEN SARs was voluntary during the period of March 1, 2012 through March 31, 2013 and mandatory starting on April 1, 2013. FinCEN Form 111 has replaced the individual legacy SAR types formerly filed on TD F 90-22.47 (Depository Institutions), FinCEN Form 109 (Money Services Business), FinCEN Form 102 (Casinos & Card Clubs), and FinCEN Form 101 (Securities & Futures Industries). The statistics are based on the Bank Secrecy Act Identification Number of each record within the SAR system. The Bank Secrecy Act Identification Number is a unique number assigned to each SAR submitted. Statistical data for SARs are updated as information is processed and refreshed data is periodically made available for this tool. For this reason, there may be discrepancies between the statistical figures returned from queries performed at different times. In addition, slight differences in query criteria may return different statistical results. Also note that the statistics generated by this tool do not include SAR fields that contain unknown or blank data. To the extent statistics including blank or unknown data are tabulated outside of this tool for other purposes, there may be discrepancies between statistics generated by this tool and those generated through other means. FinCEN makes no claims, promises or guarantees about the accuracy or completeness of the statistical figures provided from this tool and expressly disclaims liability for errors, omissions, or discrepancies in the statistical figures.",
+            "identifier": "015-FinCEN-001",
             "keyword": [
                 "suspicious activity report",
                 "sar",
@@ -4675,4083 +4681,4084 @@
                 "FinCEN Form 109",
                 "FinCEN Form 102"
             ],
+            "landingPage": "https://www.fincen.gov/reports/sar-stats",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2016-11-15",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Financial Crimes Enforcement Network",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "FinCEN",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "FinCEN"
-                },
-                "name": "Financial Crimes Enforcement Network"
-            },
-            "contactPoint": {
-                "fn": "Financial Crimes Enforcement Network",
-                "hasEmail": "mailto:FRC@fincen.gov"
-            },
-            "accessLevel": "public",
-            "bureauCode": [
-                "015:04"
-            ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "https://www.fincen.gov/reports/sar-stats",
             "references": [
                 "https://www.fincen.gov/reports/sar-stats"
-            ]
+            ],
+            "title": "Suspicious Activity Report Statistics (SAR Stats)"
         },
         {
             "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q4-004",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "015:12"
+            ],
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            },
+            "describedBy": "http://www.treasurydirect.gov/instit/annceresult/annceresult_query.htm",
+            "description": "Query for U.S. Treasury marketable securities data.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://transparency.treasury.gov/dataset/auction-query-page",
                     "describedBy": "http://www.treasurydirect.gov/instit/annceresult/annceresult_query.htm",
                     "describedByType": "text/html",
                     "downloadURL": "http://www.treasurydirect.gov/TA_WS/securities/search?startdate=2014-01-01&enddate=2014-02-01&format=json",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 }
             ],
-            "accrualPeriodicity": "R/P1D",
-            "title": "Auction Query Page",
-            "description": "Query for U.S. Treasury marketable securities data.",
+            "identifier": "015-BFS-2014Q4-004",
+            "issued": "2014-08-22T00:00:00",
             "keyword": [
                 "auction / marketable securities / bill / note /  bond"
             ],
+            "landingPage": "https://transparency.treasury.gov/dataset/auction-query-page",
             "modified": "2015-05-04",
+            "primaryITInvestmentUII": "015-000000061",
+            "programCode": [
+                "015:035"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Auction Query Page"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:035"
-            ],
-            "describedBy": "http://www.treasurydirect.gov/instit/annceresult/annceresult_query.htm",
-            "landingPage": "https://transparency.treasury.gov/dataset/auction-query-page",
-            "primaryITInvestmentUII": "015-000000061",
-            "issued": "2014-08-22T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q4-002",
+            "describedBy": "http://www.treasurydirect.gov/instit/instit.htm",
+            "description": "Auction results data displays the latest auction results for U.S. Treasury marketable securities including term, type, CMB/Reopening, CUSIP, issue date, high yield, rate, or discount margin, investment rate/spread, and price per $100.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://transparency.treasury.gov/dataset/auction-results",
                     "describedBy": "http://www.treasurydirect.gov/instit/instit.htm",
                     "describedByType": "text/html",
                     "downloadURL": "http://www.treasurydirect.gov/TA_WS/securities/auctioned?format=json&day=7",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Auction Results",
-            "description": "Auction results data displays the latest auction results for U.S. Treasury marketable securities including term, type, CMB/Reopening, CUSIP, issue date, high yield, rate, or discount margin, investment rate/spread, and price per $100.",
+            "identifier": "015-BFS-2014Q4-002",
+            "issued": "2014-08-22T00:00:00",
             "keyword": [
                 "auction results / CUSIP / auction"
             ],
+            "landingPage": "https://transparency.treasury.gov/dataset/auction-results",
             "modified": "2015-05-04",
+            "primaryITInvestmentUII": "015-000000061",
+            "programCode": [
+                "015:035"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Auction Results"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:035"
-            ],
-            "describedBy": "http://www.treasurydirect.gov/instit/instit.htm",
-            "landingPage": "https://transparency.treasury.gov/dataset/auction-results",
-            "primaryITInvestmentUII": "015-000000061",
-            "issued": "2014-08-22T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q1-10",
+            "describedBy": "http://www.treasurydirect.gov/govt/rates/pd/avg/avg.htm",
+            "description": "This dataset shows the average interest rates for U.S. Treasury securities for the most recent month compared with the same month of the previous year. The data is broken down by the various marketable and non-marketable securities. The summary page for the data provides links for monthly reports from 2001 through the current year. Average Interest Rates are calculated on the total unmatured interest-bearing debt. The average interest rates for total marketable, total non-marketable and total interest-bearing debt do not include the U.S. Treasury Inflation-Protected Securities.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.transparency.treasury.gov/dataset/average-interest-rates-on-us-treasury-securities",
                     "describedBy": "http://www.treasurydirect.gov/govt/rates/pd/avg/avg.htm",
                     "describedByType": "text/html",
                     "downloadURL": "http://www.treasurydirect.gov/govt/rates/pd/avg/avg.htm",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Average Interest Rate for Treasury Securities",
-            "description": "This dataset shows the average interest rates for U.S. Treasury securities for the most recent month compared with the same month of the previous year. The data is broken down by the various marketable and non-marketable securities. The summary page for the data provides links for monthly reports from 2001 through the current year. Average Interest Rates are calculated on the total unmatured interest-bearing debt. The average interest rates for total marketable, total non-marketable and total interest-bearing debt do not include the U.S. Treasury Inflation-Protected Securities.",
+            "identifier": "015-BFS-2014Q1-10",
+            "issued": "2013-10-31T00:00:00",
             "keyword": [
                 "Interest Rate / Marketable Securities / Non-Marketable Securities"
             ],
+            "landingPage": "https://www.transparency.treasury.gov/dataset/average-interest-rates-on-us-treasury-securities",
             "modified": "2016-07-28",
+            "primaryITInvestmentUII": "015-000000032",
+            "programCode": [
+                "015:034"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Average Interest Rate for Treasury Securities"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:034"
-            ],
-            "describedBy": "http://www.treasurydirect.gov/govt/rates/pd/avg/avg.htm",
-            "landingPage": "https://www.transparency.treasury.gov/dataset/average-interest-rates-on-us-treasury-securities",
-            "primaryITInvestmentUII": "015-000000032",
-            "issued": "2013-10-31T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q3-056",
+            "describedBy": "https://fiscaldata.treasury.gov/datasets/average-interest-rates-treasury-securities/",
+            "description": "The Average Interest Rates on U.S. Treasury Securities dataset provides average interest rates on U.S. Treasury securities on a monthly basis. Its primary purpose is to show the average interest rate on a variety of marketable and non-marketable Treasury securities. Marketable securities consist of Treasury Bills, Notes, Bonds, Treasury Inflation-Protected Securities (TIPS), Floating Rate Notes (FRNs), and Federal Financing Bank (FFB) securities. Non-marketable securities consist of Domestic Series, Foreign Series, State and Local Government Series (SLGS), U.S. Savings Securities, and Government Account Series (GAS) securities. Marketable securities are negotiable and transferable and may be sold on the secondary market. Non-marketable securities are not negotiable or transferrable and are not sold on the secondary market. This is a useful dataset for investors and bond holders to compare how interest rates on Treasury securities have changed over time.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/average-interest-rates-treasury-securities/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/average-interest-rates-treasury-securities/",
                     "describedByType": "text/html",
                     "downloadURL": "https://fiscaldata.treasury.gov/datasets/average-interest-rates-treasury-securities/",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/average-interest-rates-treasury-securities/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/average-interest-rates-treasury-securities/",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.transparency.treasury.gov/services/api/fiscal_service/v2/accounting/od/avg_interest_rates",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "Average Interest Rates on U.S. Treasury Securities",
-            "description": "The Average Interest Rates on U.S. Treasury Securities dataset provides average interest rates on U.S. Treasury securities on a monthly basis. Its primary purpose is to show the average interest rate on a variety of marketable and non-marketable Treasury securities. Marketable securities consist of Treasury Bills, Notes, Bonds, Treasury Inflation-Protected Securities (TIPS), Floating Rate Notes (FRNs), and Federal Financing Bank (FFB) securities. Non-marketable securities consist of Domestic Series, Foreign Series, State and Local Government Series (SLGS), U.S. Savings Securities, and Government Account Series (GAS) securities. Marketable securities are negotiable and transferable and may be sold on the secondary market. Non-marketable securities are not negotiable or transferrable and are not sold on the secondary market. This is a useful dataset for investors and bond holders to compare how interest rates on Treasury securities have changed over time.",
+            "identifier": "015-BFS-2014Q3-056",
             "keyword": [
                 "average interest rate / interest-bearing debt / debt / interest rates / savings bonds/ treasury securities / treasury bills / treasury bonds / treasury notes / marketable securities / non-marketable securities/ slgs / frns / tips"
             ],
+            "landingPage": "https://fiscaldata.treasury.gov/datasets/average-interest-rates-treasury-securities/",
             "modified": "2020-07-07",
+            "primaryITInvestmentUII": "015-000000060",
+            "programCode": [
+                "015:034"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Average Interest Rates on U.S. Treasury Securities"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:034"
-            ],
-            "describedBy": "https://fiscaldata.treasury.gov/datasets/average-interest-rates-treasury-securities/",
-            "landingPage": "https://fiscaldata.treasury.gov/datasets/average-interest-rates-treasury-securities/",
-            "primaryITInvestmentUII": "015-000000060"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q3-045",
+            "describedBy": "https://fiscal.treasury.gov/reports-statements/financial-report/balance-sheets.html",
+            "description": "The balance sheets show the Government's assets, liabilities, and net position. When combined with stewardship information, this information presents a more comprehensive understanding of the Government's financial position. The net position for earmarked funds is shown separately.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://transparency.treasury.gov/dataset/us-government-balance-sheets",
                     "describedBy": "https://fiscal.treasury.gov/reports-statements/financial-report/balance-sheets.html",
                     "describedByType": "text/html",
                     "downloadURL": "https://api.transparency.treasury.gov/services/api/fiscal_service/v1/accounting/od/balance_sheets",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 }
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "title": "Balance Sheets",
-            "description": "The balance sheets show the Government's assets, liabilities, and net position. When combined with stewardship information, this information presents a more comprehensive understanding of the Government's financial position. The net position for earmarked funds is shown separately.",
+            "identifier": "015-BFS-2014Q3-045",
+            "issued": "2015-09-30T00:00:00",
             "keyword": [
                 "Balance Sheets"
             ],
+            "landingPage": "https://transparency.treasury.gov/dataset/us-government-balance-sheets",
             "modified": "2019-06-25",
+            "primaryITInvestmentUII": "015-000000032",
+            "programCode": [
+                "015:031"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Balance Sheets"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:031"
-            ],
-            "describedBy": "https://fiscal.treasury.gov/reports-statements/financial-report/balance-sheets.html",
-            "landingPage": "https://transparency.treasury.gov/dataset/us-government-balance-sheets",
-            "primaryITInvestmentUII": "015-000000032",
-            "issued": "2015-09-30T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q3-067",
+            "describedBy": "http://www.treasurydirect.gov/govt/reports/pd/pd_bearregsec.pdf",
+            "description": "Dollar amounts for the definitive marketable securities, bearer and registered securities",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://transparency.treasury.gov/dataset/bearer-and-registered-securities",
                     "describedBy": "http://www.treasurydirect.gov/govt/reports/pd/pd_bearregsec.pdf",
                     "describedByType": "application/pdf",
                     "downloadURL": "http://www.treasurydirect.gov/govt/reports/pd/pd_bearregsec.pdf",
-                    "mediaType": "application/pdf",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Bearer and Registered Securities",
-            "description": "Dollar amounts for the definitive marketable securities, bearer and registered securities",
+            "identifier": "015-BFS-2014Q3-067",
+            "issued": "2014-05-12T00:00:00",
             "keyword": [
                 "definitive marketable securities"
             ],
+            "landingPage": "https://transparency.treasury.gov/dataset/bearer-and-registered-securities",
             "modified": "2016-07-28",
+            "primaryITInvestmentUII": "015-000000062",
+            "programCode": [
+                "015:033"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Bearer and Registered Securities"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:033"
-            ],
-            "describedBy": "http://www.treasurydirect.gov/govt/reports/pd/pd_bearregsec.pdf",
-            "landingPage": "https://transparency.treasury.gov/dataset/bearer-and-registered-securities",
-            "primaryITInvestmentUII": "015-000000062",
-            "issued": "2014-05-12T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q3-062",
+            "describedBy": "http://www.treasurydirect.gov/instit/annceresult/buybacks/buybacks_annce.htm",
+            "description": "Buyback Announcements displays announcements of periodic buy backs of unmatured U.S. Treasury marketable securities.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://transparency.treasury.gov/dataset/buyback-announcements",
                     "describedBy": "http://www.treasurydirect.gov/instit/annceresult/buybacks/buybacks_annce.htm",
                     "describedByType": "text/html",
                     "downloadURL": "http://www.treasurydirect.gov/instit/annceresult/buybacks/buybacks_annce.htm",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Buyback Announcements",
-            "description": "Buyback Announcements displays announcements of periodic buy backs of unmatured U.S. Treasury marketable securities.",
+            "identifier": "015-BFS-2014Q3-062",
+            "issued": "2014-05-12T00:00:00",
             "keyword": [
                 "buyback / unmatured marketable securities"
             ],
+            "landingPage": "https://transparency.treasury.gov/dataset/buyback-announcements",
             "modified": "2018-10-24",
+            "primaryITInvestmentUII": "015-000000061",
+            "programCode": [
+                "015:035"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Buyback Announcements"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:035"
-            ],
-            "describedBy": "http://www.treasurydirect.gov/instit/annceresult/buybacks/buybacks_annce.htm",
-            "landingPage": "https://transparency.treasury.gov/dataset/buyback-announcements",
-            "primaryITInvestmentUII": "015-000000061",
-            "issued": "2014-05-12T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q3-063",
+            "describedBy": "http://www.treasurydirect.gov/instit/annceresult/buybacks/buybacks_results.htm",
+            "description": "Buyback Results displays results of periodic buy backs of unmatured U.S. Treasury marketable securities.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://transparency.treasury.gov/dataset/buyback-results",
                     "describedBy": "http://www.treasurydirect.gov/instit/annceresult/buybacks/buybacks_results.htm",
                     "describedByType": "text/html",
                     "downloadURL": "http://www.treasurydirect.gov/instit/annceresult/buybacks/buybacks_results.htm",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Buyback Results",
-            "description": "Buyback Results displays results of periodic buy backs of unmatured U.S. Treasury marketable securities.",
+            "identifier": "015-BFS-2014Q3-063",
+            "issued": "2014-05-12T00:00:00",
             "keyword": [
                 "buyback / unmatured marketable securities"
             ],
+            "landingPage": "https://transparency.treasury.gov/dataset/buyback-results",
             "modified": "2018-10-24",
+            "primaryITInvestmentUII": "015-000000061",
+            "programCode": [
+                "015:035"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Buyback Results"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:035"
-            ],
-            "describedBy": "http://www.treasurydirect.gov/instit/annceresult/buybacks/buybacks_results.htm",
-            "landingPage": "https://transparency.treasury.gov/dataset/buyback-results",
-            "primaryITInvestmentUII": "015-000000061",
-            "issued": "2014-05-12T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q3-084",
+            "describedBy": "https://www.treasurydirect.gov/GA-SL/SLGS/selectCREBDate.htm",
+            "description": "Section 54 of the Internal Revenue Code (IRC) describes regulations for the issuance and use of clean renewable energy bonds (CREBs). The following table of maturities and rates specify the appropriate credit rates for the specified maturities under this program.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://transparency.treasury.gov/dataset/clean-renewable-energy-bond-rates",
                     "describedBy": "https://www.treasurydirect.gov/GA-SL/SLGS/selectCREBDate.htm",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.treasurydirect.gov/GA-SL/SLGS/selectCREBDate.htm",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1D",
-            "title": "Clean Renewable Energy Bond Rates",
-            "description": "Section 54 of the Internal Revenue Code (IRC) describes regulations for the issuance and use of clean renewable energy bonds (CREBs). The following table of maturities and rates specify the appropriate credit rates for the specified maturities under this program.",
+            "identifier": "015-BFS-2014Q3-084",
+            "issued": "2014-05-12T00:00:00",
             "keyword": [
                 "interest rates for clean renewable energy bonds"
             ],
+            "landingPage": "https://transparency.treasury.gov/dataset/clean-renewable-energy-bond-rates",
             "modified": "2016-07-28",
+            "primaryITInvestmentUII": "015-000000060",
+            "programCode": [
+                "015:034"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Clean Renewable Energy Bond Rates"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:034"
-            ],
-            "describedBy": "https://www.treasurydirect.gov/GA-SL/SLGS/selectCREBDate.htm",
-            "landingPage": "https://transparency.treasury.gov/dataset/clean-renewable-energy-bond-rates",
-            "primaryITInvestmentUII": "015-000000060",
-            "issued": "2014-05-12T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q1-01",
+            "describedBy": "https://www.fiscal.treasury.gov/reports-statements/combined-statement/",
+            "description": "Starting with Fiscal Year 2001, the Annual Report and Annual Report Appendix have been combined and renamed the Combined Statement of Receipts, Outlays, and Balances of the United States Government (Combined Statement). The Combined Statement is recognized as the official publication of receipts and outlays with which all other reports containing similar data must be in agreement. It presents budgetary results at the summary and detail level. It is part of a triad of publications that includes: the Monthly Treasury Statement, a report of the government receipts and outlays that is based on agency reporting, and the Daily Treasury Statement, summarizing data on the cash and debt operations of the Treasury based on reporting of the Treasury account balances of the Federal Reserve banks.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://transparency.treasury.gov/dataset/combined-statement-of-receipts-outlays-and-balances",
                     "describedBy": "https://www.fiscal.treasury.gov/reports-statements/combined-statement/",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.fiscal.treasury.gov/reports-statements/combined-statement/current.html",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Combined Statement of Receipts, Outlays, and Balances",
-            "description": "Starting with Fiscal Year 2001, the Annual Report and Annual Report Appendix have been combined and renamed the Combined Statement of Receipts, Outlays, and Balances of the United States Government (Combined Statement). The Combined Statement is recognized as the official publication of receipts and outlays with which all other reports containing similar data must be in agreement. It presents budgetary results at the summary and detail level. It is part of a triad of publications that includes: the Monthly Treasury Statement, a report of the government receipts and outlays that is based on agency reporting, and the Daily Treasury Statement, summarizing data on the cash and debt operations of the Treasury based on reporting of the Treasury account balances of the Federal Reserve banks.",
+            "identifier": "015-BFS-2014Q1-01",
+            "issued": "2013-10-31T00:00:00",
             "keyword": [
                 "annual report / combined statement"
             ],
+            "landingPage": "https://transparency.treasury.gov/dataset/combined-statement-of-receipts-outlays-and-balances",
             "modified": "2019-06-25",
+            "primaryITInvestmentUII": "015-000000032",
+            "programCode": [
+                "015:031"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Combined Statement of Receipts, Outlays, and Balances"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:031"
-            ],
-            "describedBy": "https://www.fiscal.treasury.gov/reports-statements/combined-statement/",
-            "landingPage": "https://transparency.treasury.gov/dataset/combined-statement-of-receipts-outlays-and-balances",
-            "primaryITInvestmentUII": "015-000000032",
-            "issued": "2013-10-31T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q3-038",
+            "describedBy": "http://www.treasurydirect.gov/govt/reports/tma/contractdisputes.htm",
+            "description": "The receipt account 203101, Recoveries from Federal Agencies for Settlement of Claims from Contract Disputes is one of the Treasury Managed Accounts. The account balances below have been identified by agency. The balances are to be reviewed by federal agencies and confirmed to Treasury, Fiscal Service on a quarterly basis.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://transparency.treasury.gov/dataset/contract-disputes-receivables",
                     "describedBy": "http://www.treasurydirect.gov/govt/reports/tma/contractdisputes.htm",
                     "describedByType": "text/html",
                     "downloadURL": "http://www.treasurydirect.gov/govt/reports/tma/contractdisputes.htm",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P3M",
-            "title": "Contract Disputes Receivables",
-            "description": "The receipt account 203101, Recoveries from Federal Agencies for Settlement of Claims from Contract Disputes is one of the Treasury Managed Accounts. The account balances below have been identified by agency. The balances are to be reviewed by federal agencies and confirmed to Treasury, Fiscal Service on a quarterly basis.",
+            "identifier": "015-BFS-2014Q3-038",
+            "issued": "2014-05-12T00:00:00",
             "keyword": [
                 "Receivables"
             ],
+            "landingPage": "https://transparency.treasury.gov/dataset/contract-disputes-receivables",
             "modified": "2016-07-28",
+            "primaryITInvestmentUII": "015-000000032",
+            "programCode": [
+                "015:031"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Contract Disputes Receivables"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:031"
-            ],
-            "describedBy": "http://www.treasurydirect.gov/govt/reports/tma/contractdisputes.htm",
-            "landingPage": "https://transparency.treasury.gov/dataset/contract-disputes-receivables",
-            "primaryITInvestmentUII": "015-000000032",
-            "issued": "2014-05-12T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q1-03",
+            "describedBy": "https://fiscaldata.treasury.gov/datasets/daily-treasury-statement/",
+            "description": "The Daily Treasury Statement dataset contains a series of tables showing the daily cash and debt operations of the U.S. Treasury. The data includes operating cash balance, deposits and withdrawals of cash, public debt transactions, federal tax deposits, income tax refunds issued (by check and electronic funds transfer (EFT)), short-term cash investments, and issues and redemptions of securities. All figures are rounded to the nearest million.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/daily-treasury-statement/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/daily-treasury-statement/",
                     "describedByType": "text/html",
                     "downloadURL": "https://fiscaldata.treasury.gov/datasets/daily-treasury-statement/",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/daily-treasury-statement/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/daily-treasury-statement/",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.transparency.treasury.gov/services/api/fiscal_service/v1/accounting/dts/dts_table_1",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/daily-treasury-statement/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/daily-treasury-statement/",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.transparency.treasury.gov/services/api/fiscal_service/v1/accounting/dts/dts_table_2",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/daily-treasury-statement/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/daily-treasury-statement/",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.transparency.treasury.gov/services/api/fiscal_service/v1/accounting/dts/dts_table_3a",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/daily-treasury-statement/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/daily-treasury-statement/",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.transparency.treasury.gov/services/api/fiscal_service/v1/accounting/dts/dts_table_3b",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/daily-treasury-statement/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/daily-treasury-statement/",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.transparency.treasury.gov/services/api/fiscal_service/v1/accounting/dts/dts_table_3c",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/daily-treasury-statement/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/daily-treasury-statement/",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.transparency.treasury.gov/services/api/fiscal_service/v1/accounting/dts/dts_table_4",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/daily-treasury-statement/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/daily-treasury-statement/",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.transparency.treasury.gov/services/api/fiscal_service/v1/accounting/dts/dts_table_5",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/daily-treasury-statement/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/daily-treasury-statement/",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.transparency.treasury.gov/services/api/fiscal_service/v1/accounting/dts/dts_table_6",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 }
             ],
-            "accrualPeriodicity": "R/P1D",
-            "title": "Daily Treasury Statement (DTS)",
-            "description": "The Daily Treasury Statement dataset contains a series of tables showing the daily cash and debt operations of the U.S. Treasury. The data includes operating cash balance, deposits and withdrawals of cash, public debt transactions, federal tax deposits, income tax refunds issued (by check and electronic funds transfer (EFT)), short-term cash investments, and issues and redemptions of securities. All figures are rounded to the nearest million.",
+            "identifier": "015-BFS-2014Q1-03",
             "keyword": [
                 "DTS/ debt / revenue / savings bonds / spending / US debt / daily treasury statement / cash balance / federal tax refund / us securities / treasury securities / debt limit / treasury cash balance"
             ],
+            "landingPage": "https://fiscaldata.treasury.gov/datasets/daily-treasury-statement/",
             "modified": "2020-07-28",
+            "primaryITInvestmentUII": "015-000000032",
+            "programCode": [
+                "015:031"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Daily Treasury Statement (DTS)"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:031"
-            ],
-            "describedBy": "https://fiscaldata.treasury.gov/datasets/daily-treasury-statement/",
-            "landingPage": "https://fiscaldata.treasury.gov/datasets/daily-treasury-statement/",
-            "primaryITInvestmentUII": "015-000000032"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2016Q3-002",
+            "describedBy": "https://www.transparency.treasury.gov/dataset/data-registry/registry#meta-data",
+            "description": "The purpose of the Fiscal Service Data Registry is to promote the common identification, use and sharing of data/information across the federal government.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.transparency.treasury.gov/dataset/data-registry",
                     "describedBy": "https://www.transparency.treasury.gov/dataset/data-registry/registry#meta-data",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.transparency.treasury.gov/dataset/data-registry/registry#meta-data",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Data Registry",
-            "description": "The purpose of the Fiscal Service Data Registry is to promote the common identification, use and sharing of data/information across the federal government.",
+            "identifier": "015-BFS-2016Q3-002",
+            "issued": "2016-08-11T00:00:00",
             "keyword": [
                 "Registry / Data Elements"
             ],
+            "landingPage": "https://www.transparency.treasury.gov/dataset/data-registry",
             "modified": "2019-06-25",
+            "primaryITInvestmentUII": "015-000200020",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Data Registry"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "describedBy": "https://www.transparency.treasury.gov/dataset/data-registry/registry#meta-data",
-            "landingPage": "https://www.transparency.treasury.gov/dataset/data-registry",
-            "primaryITInvestmentUII": "015-000200020",
-            "issued": "2016-08-11T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q1-02",
+            "describedBy": "http://www.treasurydirect.gov/govt/reports/pd/pd_debtposactrpt.htm",
+            "description": "The Debt Position and Activity Report shows the current and historical debt position of the U.S. Department of the Treasury in relation to debt held by the public, intragovernmental holdings, and statutory debt limit. Issue and redemption activity are also provided in this report.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://transparency.treasury.gov/dataset/debt-position-and-activity-report",
                     "describedBy": "http://www.treasurydirect.gov/govt/reports/pd/pd_debtposactrpt.htm",
                     "describedByType": "text/html",
                     "downloadURL": "http://www.treasurydirect.gov/govt/reports/pd/pd_debtposactrpt.htm",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "Debt Position and Activity Report",
-            "description": "The Debt Position and Activity Report shows the current and historical debt position of the U.S. Department of the Treasury in relation to debt held by the public, intragovernmental holdings, and statutory debt limit. Issue and redemption activity are also provided in this report.",
+            "identifier": "015-BFS-2014Q1-02",
+            "issued": "2013-10-31T00:00:00",
             "keyword": [
                 "Current and historical debt position"
             ],
+            "landingPage": "https://transparency.treasury.gov/dataset/debt-position-and-activity-report",
             "modified": "2016-07-28",
+            "primaryITInvestmentUII": "015-000000032",
+            "programCode": [
+                "015:034"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Debt Position and Activity Report"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:034"
-            ],
-            "describedBy": "http://www.treasurydirect.gov/govt/reports/pd/pd_debtposactrpt.htm",
-            "landingPage": "https://transparency.treasury.gov/dataset/debt-position-and-activity-report",
-            "primaryITInvestmentUII": "015-000000032",
-            "issued": "2013-10-31T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q3-065",
+            "describedBy": "https://fiscaldata.treasury.gov/datasets/debt-to-the-penny/",
+            "description": "The Debt to the Penny dataset provides information about the total outstanding public debt and is reported each day. Debt to the Penny is made up of intragovernmental holdings and debt held by the public, including securities issued by the U.S. Treasury. Total public debt outstanding is composed of Treasury Bills, Notes, Bonds, Treasury Inflation-Protected Securities (TIPS), Floating Rate Notes (FRNs), and Federal Financing Bank (FFB) securities, as well as Domestic Series, Foreign Series, State and Local Government Series (SLGS), U.S. Savings Securities, and Government Account Series (GAS) securities. Debt to the Penny is updated at 3:00 PM EST each business day with data from the previous business day.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/debt-to-the-penny/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/debt-to-the-penny/",
                     "describedByType": "text/html",
                     "downloadURL": "https://fiscaldata.treasury.gov/datasets/debt-to-the-penny/",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/debt-to-the-penny/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/debt-to-the-penny/",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.transparency.treasury.gov/services/api/fiscal_service/v2/accounting/od/debt_to_penny",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 }
             ],
-            "accrualPeriodicity": "R/P1D",
-            "title": "Debt to the Penny",
-            "description": "The Debt to the Penny dataset provides information about the total outstanding public debt and is reported each day. Debt to the Penny is made up of intragovernmental holdings and debt held by the public, including securities issued by the U.S. Treasury. Total public debt outstanding is composed of Treasury Bills, Notes, Bonds, Treasury Inflation-Protected Securities (TIPS), Floating Rate Notes (FRNs), and Federal Financing Bank (FFB) securities, as well as Domestic Series, Foreign Series, State and Local Government Series (SLGS), U.S. Savings Securities, and Government Account Series (GAS) securities. Debt to the Penny is updated at 3:00 PM EST each business day with data from the previous business day.",
+            "identifier": "015-BFS-2014Q3-065",
             "keyword": [
                 "debt / daily / public debt / penny /  Federal / Government / Treasury / Securities / Government Debt"
             ],
+            "landingPage": "https://fiscaldata.treasury.gov/datasets/debt-to-the-penny/",
             "modified": "2020-07-28",
+            "primaryITInvestmentUII": "015-000000060",
+            "programCode": [
+                "015:034"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Debt to the Penny"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:034"
-            ],
-            "describedBy": "https://fiscaldata.treasury.gov/datasets/debt-to-the-penny/",
-            "landingPage": "https://fiscaldata.treasury.gov/datasets/debt-to-the-penny/",
-            "primaryITInvestmentUII": "015-000000060"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q3-050",
+            "describedBy": "https://www.fiscal.treasury.gov/reference-guidance/fast-book/",
+            "description": "The FAST Book is Supplement 1 to Volume I of the Treasury Financial Manual. It lists receipt, appropriation, and other fund account symbols and titles assigned by the Department of the Treasury. FAST Book I displays the two-digit department regular codes. FAST Book II displays the three-digit agency identifier codes.  This data set is Receipt Account Symbols and Titles only.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://transparency.treasury.gov/dataset/federal-account-symbols-and-titles-the-fast-book",
                     "describedBy": "https://www.fiscal.treasury.gov/reference-guidance/fast-book/",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.fiscal.treasury.gov/reference-guidance/fast-book/",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Federal Account Symbols and Titles: The FAST Book",
-            "description": "The FAST Book is Supplement 1 to Volume I of the Treasury Financial Manual. It lists receipt, appropriation, and other fund account symbols and titles assigned by the Department of the Treasury. FAST Book I displays the two-digit department regular codes. FAST Book II displays the three-digit agency identifier codes.  This data set is Receipt Account Symbols and Titles only.",
+            "identifier": "015-BFS-2014Q3-050",
+            "issued": "2014-05-12T00:00:00",
             "keyword": [
                 "FAST Book I"
             ],
+            "landingPage": "https://transparency.treasury.gov/dataset/federal-account-symbols-and-titles-the-fast-book",
             "modified": "2019-06-25",
+            "primaryITInvestmentUII": "015-000000032",
+            "programCode": [
+                "015:031"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Federal Account Symbols and Titles: The FAST Book"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:031"
-            ],
-            "describedBy": "https://www.fiscal.treasury.gov/reference-guidance/fast-book/",
-            "landingPage": "https://transparency.treasury.gov/dataset/federal-account-symbols-and-titles-the-fast-book",
-            "primaryITInvestmentUII": "015-000000032",
-            "issued": "2014-05-12T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q1-05",
+            "describedBy": "http://www.treasurydirect.gov/govt/reports/tbp/tbp.htm",
+            "description": "Federal agencies with legal authority granted by Congress through legislation may borrow funds from Treasury to operate credit programs to loan or guarantee loans for nonfederal borrowers, such as small businesses, students, veterans, and farmers. Public Debt reports the detail records of the loan transactions between Treasury and other federal agencies and accounts for and reports Treasury loans receivable and the related interest receivable.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://transparency.treasury.gov/dataset/federal-borrowings-program-reports-detail-principal-and-accrued-balances-and-summary-general-ledger-balances",
                     "describedBy": "http://www.treasurydirect.gov/govt/reports/tbp/tbp.htm",
                     "describedByType": "text/html",
                     "downloadURL": "http://www.treasurydirect.gov/govt/reports/tbp/tbp.htm",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "Federal Borrowings Program Reports: Detail Principal and Accrued Balances and Summary General Ledger Balances",
-            "description": "Federal agencies with legal authority granted by Congress through legislation may borrow funds from Treasury to operate credit programs to loan or guarantee loans for nonfederal borrowers, such as small businesses, students, veterans, and farmers. Public Debt reports the detail records of the loan transactions between Treasury and other federal agencies and accounts for and reports Treasury loans receivable and the related interest receivable.",
+            "identifier": "015-BFS-2014Q1-05",
+            "issued": "2013-10-31T00:00:00",
             "keyword": [
                 "Federal Borrowings Program Data"
             ],
+            "landingPage": "https://transparency.treasury.gov/dataset/federal-borrowings-program-reports-detail-principal-and-accrued-balances-and-summary-general-ledger-balances",
             "modified": "2016-07-28",
+            "primaryITInvestmentUII": "015-000000032",
+            "programCode": [
+                "015:034"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Federal Borrowings Program Reports: Detail Principal and Accrued Balances and Summary General Ledger Balances"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:034"
-            ],
-            "describedBy": "http://www.treasurydirect.gov/govt/reports/tbp/tbp.htm",
-            "landingPage": "https://transparency.treasury.gov/dataset/federal-borrowings-program-reports-detail-principal-and-accrued-balances-and-summary-general-ledger-balances",
-            "primaryITInvestmentUII": "015-000000032",
-            "issued": "2013-10-31T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q3-091",
+            "describedBy": "https://www.treasurydirect.gov/govt/rates/tcir/tcir_opdcrir.htm",
+            "description": "Federal Credit Similar Maturity Rates:  Rates are displayed from 1 year or less to 20 years or more for fiscal years 1992 previous fiscal year.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://transparency.treasury.gov/dataset/federal-credit-similar-maturity-rates",
                     "describedBy": "https://www.treasurydirect.gov/govt/rates/tcir/tcir_opdcrir.htm",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.treasurydirect.gov/govt/rates/tcir/tcir_opdcrir.htm",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "title": "Federal Credit Similar Maturity Rates",
-            "description": "Federal Credit Similar Maturity Rates:  Rates are displayed from 1 year or less to 20 years or more for fiscal years 1992 previous fiscal year.",
+            "identifier": "015-BFS-2014Q3-091",
+            "issued": "2014-05-12T00:00:00",
             "keyword": [
                 "federal credit similar maturity rates"
             ],
+            "landingPage": "https://transparency.treasury.gov/dataset/federal-credit-similar-maturity-rates",
             "modified": "2016-07-28",
+            "primaryITInvestmentUII": "015-000000062",
+            "programCode": [
+                "015:033"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Federal Credit Similar Maturity Rates"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:033"
-            ],
-            "describedBy": "https://www.treasurydirect.gov/govt/rates/tcir/tcir_opdcrir.htm",
-            "landingPage": "https://transparency.treasury.gov/dataset/federal-credit-similar-maturity-rates",
-            "primaryITInvestmentUII": "015-000000062",
-            "issued": "2014-05-12T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q3-097",
+            "describedBy": "http://www.treasurydirect.gov/govt/reports/fip/acctstmt/acctstmt.htm",
+            "description": "Statements for agencies investing in Government Account Series Securities through FedInvest",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://transparency.treasury.gov/dataset/federal-investments-account-statements",
                     "describedBy": "http://www.treasurydirect.gov/govt/reports/fip/acctstmt/acctstmt.htm",
                     "describedByType": "text/html",
                     "downloadURL": "http://www.treasurydirect.gov/govt/reports/fip/acctstmt/acctstmt.htm",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "Federal Investments Account Statements",
-            "description": "Statements for agencies investing in Government Account Series Securities through FedInvest",
+            "identifier": "015-BFS-2014Q3-097",
+            "issued": "2014-05-12T00:00:00",
             "keyword": [
                 "Federal Investment program account statements"
             ],
+            "landingPage": "https://transparency.treasury.gov/dataset/federal-investments-account-statements",
             "modified": "2016-07-28",
+            "primaryITInvestmentUII": "015-000000060",
+            "programCode": [
+                "015:034"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Federal Investments Account Statements"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:034"
-            ],
-            "describedBy": "http://www.treasurydirect.gov/govt/reports/fip/acctstmt/acctstmt.htm",
-            "landingPage": "https://transparency.treasury.gov/dataset/federal-investments-account-statements",
-            "primaryITInvestmentUII": "015-000000060",
-            "issued": "2014-05-12T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q3-081",
+            "describedBy": "https://www.treasurydirect.gov/govt/rates/rates_fip.htm",
+            "description": "The daily pricing file provides current market prices for investments (short, buy, or mean), redemptions (cover, sell, or bid) and end of day portfolio valuations.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.transparency.treasury.gov/dataset/federal-investments-program-rates-and-prices",
                     "describedBy": "https://www.treasurydirect.gov/govt/rates/rates_fip.htm",
                     "describedByType": "text/html",
                     "downloadURL": "https://api.transparency.treasury.gov/services/api/fiscal_service/v1/accounting/od/fip_rates_prices",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 }
             ],
-            "accrualPeriodicity": "R/P1D",
-            "title": "Federal Investments Program Rates and Prices",
-            "description": "The daily pricing file provides current market prices for investments (short, buy, or mean), redemptions (cover, sell, or bid) and end of day portfolio valuations.",
+            "identifier": "015-BFS-2014Q3-081",
+            "issued": "2017-02-21T00:00:00",
             "keyword": [
                 "federal investment rates / prices"
             ],
+            "landingPage": "https://www.transparency.treasury.gov/dataset/federal-investments-program-rates-and-prices",
             "modified": "2017-03-31",
-            "publisher": {
+            "primaryITInvestmentUII": "015-000000060",
+            "programCode": [
+                "015:034"
+            ],
+            "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Federal Investments Program Rates and Prices"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:034"
-            ],
-            "describedBy": "https://www.treasurydirect.gov/govt/rates/rates_fip.htm",
-            "landingPage": "https://www.transparency.treasury.gov/dataset/federal-investments-program-rates-and-prices",
-            "primaryITInvestmentUII": "015-000000060",
-            "issued": "2017-02-21T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q1-07",
+            "describedBy": "https://www.fiscal.treasury.gov/reports-statements/financial-report/",
+            "description": "The FR provides the President, Congress, and the American People with a comprehensive view of the federal government's finances, i.e., its financial position and condition, its revenues and costs, assets and liabilities, and other obligations and commitments.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://transparency.treasury.gov/dataset/financial-report-of-the-united-states-government",
                     "describedBy": "https://www.fiscal.treasury.gov/reports-statements/financial-report/",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.fiscal.treasury.gov/reports-statements/financial-report/",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Financial Report (FR) of the United States Government",
-            "description": "The FR provides the President, Congress, and the American People with a comprehensive view of the federal government's finances, i.e., its financial position and condition, its revenues and costs, assets and liabilities, and other obligations and commitments.",
+            "identifier": "015-BFS-2014Q1-07",
+            "issued": "2013-10-31T00:00:00",
             "keyword": [
                 "frusg / cfs"
             ],
+            "landingPage": "https://transparency.treasury.gov/dataset/financial-report-of-the-united-states-government",
             "modified": "2019-06-25",
+            "primaryITInvestmentUII": "015-000000032",
+            "programCode": [
+                "015:031"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Financial Report (FR) of the United States Government"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:031"
-            ],
-            "describedBy": "https://www.fiscal.treasury.gov/reports-statements/financial-report/",
-            "landingPage": "https://transparency.treasury.gov/dataset/financial-report-of-the-united-states-government",
-            "primaryITInvestmentUII": "015-000000032",
-            "issued": "2013-10-31T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2016Q3-003",
+            "describedBy": "https://fiscal.treasury.gov/data",
+            "description": "Fiscal Service business messages (schemas) define the structure of XML documents, specify data types for attribute values and data element content that allow machines to carry out rules made by the Bureau.  \nXML Schema - A specification to define the structure of XML documents and to specify data types for attribute values and data element content.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscal.treasury.gov/data",
                     "describedBy": "https://fiscal.treasury.gov/data",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.fiscal.treasury.gov/data/index.html",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Fiscal Service Data Exchange Listing",
-            "description": "Fiscal Service business messages (schemas) define the structure of XML documents, specify data types for attribute values and data element content that allow machines to carry out rules made by the Bureau.  \nXML Schema - A specification to define the structure of XML documents and to specify data types for attribute values and data element content.",
+            "identifier": "015-BFS-2016Q3-003",
+            "issued": "2016-05-05T00:00:00",
             "keyword": [
                 "Business Messages / XML Schema"
             ],
+            "landingPage": "https://fiscal.treasury.gov/data",
             "modified": "2016-05-05",
+            "primaryITInvestmentUII": "015-000200020",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Fiscal Service Data Exchange Listing"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "describedBy": "https://fiscal.treasury.gov/data",
-            "landingPage": "https://fiscal.treasury.gov/data",
-            "primaryITInvestmentUII": "015-000200020",
-            "issued": "2016-05-05T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q3-070",
+            "describedBy": "https://fiscaldata.treasury.gov/datasets/gift-contributions-reduce-debt-held-by-public/",
+            "description": "The Gift Contributions to Reduce Debt Held by the Public dataset provides the monthly total for gift contributions received by the U.S. Treasury that were donated to reduce the public debt. These donations can include money, outstanding government obligations (such as savings bonds) and property that is sold for cash. Gifts may be classified as inter vivos (from a living person) or testamentary bequests (from a person's will).",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/gift-contributions-reduce-debt-held-by-public/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/gift-contributions-reduce-debt-held-by-public/",
                     "describedByType": "text/html",
                     "downloadURL": "https://fiscaldata.treasury.gov/datasets/gift-contributions-reduce-debt-held-by-public/",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/gift-contributions-reduce-debt-held-by-public/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/gift-contributions-reduce-debt-held-by-public/",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.transparency.treasury.gov/services/api/fiscal_service/v2/accounting/od/gift_contributions",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "Gift Contributions to Reduce Debt Held by the Public",
-            "description": "The Gift Contributions to Reduce Debt Held by the Public dataset provides the monthly total for gift contributions received by the U.S. Treasury that were donated to reduce the public debt. These donations can include money, outstanding government obligations (such as savings bonds) and property that is sold for cash. Gifts may be classified as inter vivos (from a living person) or testamentary bequests (from a person's will).",
+            "identifier": "015-BFS-2014Q3-070",
             "keyword": [
                 "debt / revenue / public debt / contributions / us debt / federal government debt / reduce US debt / gift contribution to reduce US debt / donation to reduce US debt"
             ],
+            "landingPage": "https://fiscaldata.treasury.gov/datasets/gift-contributions-reduce-debt-held-by-public/",
             "modified": "2020-07-07",
+            "primaryITInvestmentUII": "015-000000060",
+            "programCode": [
+                "015:034"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Gift Contributions to Reduce Debt Held by the Public"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:034"
-            ],
-            "describedBy": "https://fiscaldata.treasury.gov/datasets/gift-contributions-reduce-debt-held-by-public/",
-            "landingPage": "https://fiscaldata.treasury.gov/datasets/gift-contributions-reduce-debt-held-by-public/",
-            "primaryITInvestmentUII": "015-000000060"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q3-086",
+            "describedBy": "https://www.treasurydirect.gov/GA-SL/SLGS/selectGTCDate.htm",
+            "description": "Section 1400N(l) of the Internal Revenue Code describes regulations for the issuance and use of Gulf Tax Credit (GTC) Bonds. GTC Rates were published each business day from April 24, 2006 to December 31, 2006.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://transparency.treasury.gov/dataset/gulf-tax-credit-bond-rates",
                     "describedBy": "https://www.treasurydirect.gov/GA-SL/SLGS/selectGTCDate.htm",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.treasurydirect.gov/GA-SL/SLGS/selectGTCDate.htm",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1D",
-            "title": "Gulf Tax Credit Bond Rates",
-            "description": "Section 1400N(l) of the Internal Revenue Code describes regulations for the issuance and use of Gulf Tax Credit (GTC) Bonds. GTC Rates were published each business day from April 24, 2006 to December 31, 2006.",
+            "identifier": "015-BFS-2014Q3-086",
+            "issued": "2014-05-12T00:00:00",
             "keyword": [
                 "interest rates for gulf tax credit bonds"
             ],
+            "landingPage": "https://transparency.treasury.gov/dataset/gulf-tax-credit-bond-rates",
             "modified": "2016-07-28",
+            "primaryITInvestmentUII": "015-000000060",
+            "programCode": [
+                "015:034"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Gulf Tax Credit Bond Rates"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:034"
-            ],
-            "describedBy": "https://www.treasurydirect.gov/GA-SL/SLGS/selectGTCDate.htm",
-            "landingPage": "https://transparency.treasury.gov/dataset/gulf-tax-credit-bond-rates",
-            "primaryITInvestmentUII": "015-000000060",
-            "issued": "2014-05-12T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q3-071",
+            "describedBy": "https://fiscaldata.treasury.gov/datasets/historical-debt-outstanding/",
+            "description": "Historical Debt Outstanding is a dataset that provides a summary of the U.S. government's total outstanding debt at the end of each fiscal year from 1789 to the current year. Between 1789 and 1842, the fiscal year began in January. From January 1842 until 1977, the fiscal year began in July. From July 1977 onwards, the fiscal year has started in October. Between 1789 and 1919, debt outstanding was presented as of the first day of the next fiscal year. From 1920 onwards, debt outstanding has been presented as of the final day of the fiscal year. This is a high-level summary of historical public debt and does not contain a breakdown of the debt components.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/historical-debt-outstanding/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/historical-debt-outstanding/",
                     "describedByType": "text/html",
                     "downloadURL": "https://fiscaldata.treasury.gov/datasets/historical-debt-outstanding/",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/historical-debt-outstanding/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/historical-debt-outstanding/",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.transparency.treasury.gov/services/api/fiscal_service/v2/accounting/od/debt_outstanding",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 }
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "title": "Historical Debt Outstanding",
-            "description": "Historical Debt Outstanding is a dataset that provides a summary of the U.S. government's total outstanding debt at the end of each fiscal year from 1789 to the current year. Between 1789 and 1842, the fiscal year began in January. From January 1842 until 1977, the fiscal year began in July. From July 1977 onwards, the fiscal year has started in October. Between 1789 and 1919, debt outstanding was presented as of the first day of the next fiscal year. From 1920 onwards, debt outstanding has been presented as of the final day of the fiscal year. This is a high-level summary of historical public debt and does not contain a breakdown of the debt components.",
+            "identifier": "015-BFS-2014Q3-071",
             "keyword": [
                 "debt / public debt / government debt / U.S. government / US government / debt outstanding / total debt"
             ],
+            "landingPage": "https://fiscaldata.treasury.gov/datasets/historical-debt-outstanding/",
             "modified": "2019-09-30",
+            "primaryITInvestmentUII": "015-000000060",
+            "programCode": [
+                "015:034"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Historical Debt Outstanding"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:034"
-            ],
-            "describedBy": "https://fiscaldata.treasury.gov/datasets/historical-debt-outstanding/",
-            "landingPage": "https://fiscaldata.treasury.gov/datasets/historical-debt-outstanding/",
-            "primaryITInvestmentUII": "015-000000060"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q3-098",
+            "describedBy": "http://www.treasurydirect.gov/govt/reports/fip/intcost/intcost.htm",
+            "description": "Interest Reports by investment fund",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://transparency.treasury.gov/dataset/interest-cost-by-fund",
                     "describedBy": "http://www.treasurydirect.gov/govt/reports/fip/intcost/intcost.htm",
                     "describedByType": "text/html",
                     "downloadURL": "https://api.transparency.treasury.gov/services/api/fiscal_service/v1/accounting/od/interest_cost_fund",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "Interest Cost by Fund",
-            "description": "Interest Reports by investment fund",
+            "identifier": "015-BFS-2014Q3-098",
+            "issued": "2016-11-30T00:00:00",
             "keyword": [
                 "Federal investment fund interest reports"
             ],
+            "landingPage": "https://transparency.treasury.gov/dataset/interest-cost-by-fund",
             "modified": "2017-03-31",
+            "primaryITInvestmentUII": "015-000000060",
+            "programCode": [
+                "015:034"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Interest Cost by Fund"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:034"
-            ],
-            "describedBy": "http://www.treasurydirect.gov/govt/reports/fip/intcost/intcost.htm",
-            "landingPage": "https://transparency.treasury.gov/dataset/interest-cost-by-fund",
-            "primaryITInvestmentUII": "015-000000060",
-            "issued": "2016-11-30T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q3-103",
+            "describedBy": "https://fiscaldata.treasury.gov/datasets/interest-expense-debt-outstanding/",
+            "description": "The Interest Expense on Debt Outstanding dataset provides monthly and fiscal year-to-date values for interest expenses on federal government debt, that is, the cost to the U.S. for borrowing money (calculated at a specified rate and period of time). U.S. debt includes Treasury notes and bonds, foreign and domestic series certificates of indebtedness, savings bonds, Government Account Series (GAS), State and Local Government Series (SLGS) and other special purpose securities. While interest expenses are what the government pays to investors who loan money to the government, how much the government pays in interest depends on both the total federal debt and the interest rate investors charged when they loaned the money. This dataset is useful for those who wish to track the cost of maintaining federal debt.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/interest-expense-debt-outstanding/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/interest-expense-debt-outstanding/",
                     "describedByType": "text/html",
                     "downloadURL": "https://fiscaldata.treasury.gov/datasets/interest-expense-debt-outstanding/",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/interest-expense-debt-outstanding/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/interest-expense-debt-outstanding/",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.transparency.treasury.gov/services/api/fiscal_service/v2/accounting/od/interest_expense",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "Interest Expense on the Debt Outstanding",
-            "description": "The Interest Expense on Debt Outstanding dataset provides monthly and fiscal year-to-date values for interest expenses on federal government debt, that is, the cost to the U.S. for borrowing money (calculated at a specified rate and period of time). U.S. debt includes Treasury notes and bonds, foreign and domestic series certificates of indebtedness, savings bonds, Government Account Series (GAS), State and Local Government Series (SLGS) and other special purpose securities. While interest expenses are what the government pays to investors who loan money to the government, how much the government pays in interest depends on both the total federal debt and the interest rate investors charged when they loaned the money. This dataset is useful for those who wish to track the cost of maintaining federal debt.",
+            "identifier": "015-BFS-2014Q3-103",
             "keyword": [
                 "interest / debt /  US debt / interest on debt / federal debt / government debt / treasury bills / treasury notes / treasury bonds / government account series / public debt"
             ],
+            "landingPage": "https://fiscaldata.treasury.gov/datasets/interest-expense-debt-outstanding/",
             "modified": "2020-07-07",
+            "primaryITInvestmentUII": "015-000000060",
+            "programCode": [
+                "015:034"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Interest Expense on the Debt Outstanding"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:034"
-            ],
-            "describedBy": "https://fiscaldata.treasury.gov/datasets/interest-expense-debt-outstanding/",
-            "landingPage": "https://fiscaldata.treasury.gov/datasets/interest-expense-debt-outstanding/",
-            "primaryITInvestmentUII": "015-000000060"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q3-037",
+            "describedBy": "http://www.treasurydirect.gov/govt/reports/tma/uninvested.htm",
+            "description": "Interest on Uninvested Funds account 20X1880 was established pursuant to the Federal Credit Reform Act of 1990, which was intended to more accurately measure the costs of Federal credit programs. Agencies who borrow from Treasury are required to calculate their own interest income and expense.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://transparency.treasury.gov/dataset/interest-on-uninvested-funds",
                     "describedBy": "http://www.treasurydirect.gov/govt/reports/tma/uninvested.htm",
                     "describedByType": "text/html",
                     "downloadURL": "http://www.treasurydirect.gov/govt/reports/tma/uninvested.htm",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P3M",
-            "title": "Interest on Uninvested Funds",
-            "description": "Interest on Uninvested Funds account 20X1880 was established pursuant to the Federal Credit Reform Act of 1990, which was intended to more accurately measure the costs of Federal credit programs. Agencies who borrow from Treasury are required to calculate their own interest income and expense.",
+            "identifier": "015-BFS-2014Q3-037",
+            "issued": "2014-05-12T00:00:00",
             "keyword": [
                 "Interest / Uninvested Funds"
             ],
+            "landingPage": "https://transparency.treasury.gov/dataset/interest-on-uninvested-funds",
             "modified": "2016-07-28",
+            "primaryITInvestmentUII": "015-000000032",
+            "programCode": [
+                "015:031"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Interest on Uninvested Funds"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:031"
-            ],
-            "describedBy": "http://www.treasurydirect.gov/govt/reports/tma/uninvested.htm",
-            "landingPage": "https://transparency.treasury.gov/dataset/interest-on-uninvested-funds",
-            "primaryITInvestmentUII": "015-000000032",
-            "issued": "2014-05-12T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q3-099",
+            "describedBy": "http://www.treasurydirect.gov/govt/reports/fip/hold/hold.htm",
+            "description": "Holdings by investment fund",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://transparency.treasury.gov/dataset/investment-funds-summary-holdings-reports",
                     "describedBy": "http://www.treasurydirect.gov/govt/reports/fip/hold/hold.htm",
                     "describedByType": "text/html",
                     "downloadURL": "http://www.treasurydirect.gov/govt/reports/fip/hold/hold.htm",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "Investment Funds Summary Holdings Reports",
-            "description": "Holdings by investment fund",
+            "identifier": "015-BFS-2014Q3-099",
+            "issued": "2014-05-12T00:00:00",
             "keyword": [
                 "Federal investment fund holdings"
             ],
+            "landingPage": "https://transparency.treasury.gov/dataset/investment-funds-summary-holdings-reports",
             "modified": "2016-07-28",
+            "primaryITInvestmentUII": "015-000000060",
+            "programCode": [
+                "015:034"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Investment Funds Summary Holdings Reports"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:034"
-            ],
-            "describedBy": "http://www.treasurydirect.gov/govt/reports/fip/hold/hold.htm",
-            "landingPage": "https://transparency.treasury.gov/dataset/investment-funds-summary-holdings-reports",
-            "primaryITInvestmentUII": "015-000000060",
-            "issued": "2014-05-12T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q3-105",
+            "describedBy": "https://www.transparency.treasury.gov/article/api-title-xii-advance-activities-schedule",
+            "description": "The Judgment Fund is available to pay most court judgments and Justice Department compromise settlements of actual or imminent litigation against the government.  In this report, Judgment Fund payments are categorized as either Administrative or Litigative. Administrative payments are for certain claims settled by agencies without involvement from the Department of Justice (DOJ).  Litigative payments are for claims that involve DOJ as representative of the defendant agency.  Litigative payments include payments resulting from a settlement with the claimant before or during litigation as well as those resulting from a judge's order.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.transparency.treasury.gov/dataset/judgment-fund",
                     "describedBy": "https://www.transparency.treasury.gov/article/api-title-xii-advance-activities-schedule",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.fiscal.treasury.gov/judgment-fund/annual-report-congress.html",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "title": "Judgment Fund Transparency Report",
-            "description": "The Judgment Fund is available to pay most court judgments and Justice Department compromise settlements of actual or imminent litigation against the government.  In this report, Judgment Fund payments are categorized as either Administrative or Litigative. Administrative payments are for certain claims settled by agencies without involvement from the Department of Justice (DOJ).  Litigative payments are for claims that involve DOJ as representative of the defendant agency.  Litigative payments include payments resulting from a settlement with the claimant before or during litigation as well as those resulting from a judge's order.",
+            "identifier": "015-BFS-2014Q3-105",
+            "issued": "2014-05-12T00:00:00",
             "keyword": [
                 "Transparency / Judgment Fund / Justice Department"
             ],
+            "landingPage": "https://www.transparency.treasury.gov/dataset/judgment-fund",
             "modified": "2019-07-05",
+            "primaryITInvestmentUII": "015-000000201",
+            "programCode": [
+                "015:032"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Judgment Fund Transparency Report"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:032"
-            ],
-            "describedBy": "https://www.transparency.treasury.gov/article/api-title-xii-advance-activities-schedule",
-            "landingPage": "https://www.transparency.treasury.gov/dataset/judgment-fund",
-            "primaryITInvestmentUII": "015-000000201",
-            "issued": "2014-05-12T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q3-085",
+            "describedBy": "https://www.treasurydirect.gov/GA-SL/SLGS/selectMWTCDate.htm",
+            "description": "Section 1400N(l) of the Internal Revenue Code provides rules for the issuance and use of Midwestern tax credit (MWTC) bonds. MWTC Rates were published each business day from March 30, 2009 to March 9, 2012.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://transparency.treasury.gov/dataset/midwestern-tax-credit-bond-rates",
                     "describedBy": "https://www.treasurydirect.gov/GA-SL/SLGS/selectMWTCDate.htm",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.treasurydirect.gov/GA-SL/SLGS/selectMWTCDate.htm",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1D",
-            "title": "Midwestern Tax Credit Bond Rates",
-            "description": "Section 1400N(l) of the Internal Revenue Code provides rules for the issuance and use of Midwestern tax credit (MWTC) bonds. MWTC Rates were published each business day from March 30, 2009 to March 9, 2012.",
+            "identifier": "015-BFS-2014Q3-085",
+            "issued": "2014-05-12T00:00:00",
             "keyword": [
                 "interest rates for Midwestern tax credit bonds"
             ],
+            "landingPage": "https://transparency.treasury.gov/dataset/midwestern-tax-credit-bond-rates",
             "modified": "2016-07-28",
+            "primaryITInvestmentUII": "015-000000060",
+            "programCode": [
+                "015:034"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Midwestern Tax Credit Bond Rates"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:034"
-            ],
-            "describedBy": "https://www.treasurydirect.gov/GA-SL/SLGS/selectMWTCDate.htm",
-            "landingPage": "https://transparency.treasury.gov/dataset/midwestern-tax-credit-bond-rates",
-            "primaryITInvestmentUII": "015-000000060",
-            "issued": "2014-05-12T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q3-061",
+            "describedBy": "https://www.treasurydirect.gov/instit/annceresult/tipscpi/tipscpi.htm",
+            "description": "Treasury Inflation-Protected Securities, also known as TIPS, are securities whose principal is tied to the Consumer Price Index. With inflation, the principal increases. With deflation, it decreases. When the security matures, the U.S. Treasury pays the original or adjusted principal, whichever is greater.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://transparency.treasury.gov/dataset/monthly-reference-cpi-numbers-and-daily-index-ratios-table-tips-cpi-data",
                     "describedBy": "https://www.treasurydirect.gov/instit/annceresult/tipscpi/tipscpi.htm",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.treasurydirect.gov/instit/annceresult/tipscpi/tipscpi.htm",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "Monthly Reference CPI Numbers and Daily Index Ratios Table (TIPS/CPI Data)",
-            "description": "Treasury Inflation-Protected Securities, also known as TIPS, are securities whose principal is tied to the Consumer Price Index. With inflation, the principal increases. With deflation, it decreases. When the security matures, the U.S. Treasury pays the original or adjusted principal, whichever is greater.",
+            "identifier": "015-BFS-2014Q3-061",
+            "issued": "2014-05-12T00:00:00",
             "keyword": [
                 "TIPS-CPI / index ratios"
             ],
+            "landingPage": "https://transparency.treasury.gov/dataset/monthly-reference-cpi-numbers-and-daily-index-ratios-table-tips-cpi-data",
             "modified": "2016-07-28",
+            "primaryITInvestmentUII": "015-000000061",
+            "programCode": [
+                "015:035"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Monthly Reference CPI Numbers and Daily Index Ratios Table (TIPS/CPI Data)"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:035"
-            ],
-            "describedBy": "https://www.treasurydirect.gov/instit/annceresult/tipscpi/tipscpi.htm",
-            "landingPage": "https://transparency.treasury.gov/dataset/monthly-reference-cpi-numbers-and-daily-index-ratios-table-tips-cpi-data",
-            "primaryITInvestmentUII": "015-000000061",
-            "issued": "2014-05-12T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q3-058",
+            "describedBy": "https://www.treasurydirect.gov/govt/reports/slgs/slgs_mnthlyslgsstat.htm",
+            "description": "Current Month Balances for Securities Outstanding and Principal Outstanding for SLGS",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://transparency.treasury.gov/dataset/monthly-slgs-statistics",
                     "describedBy": "https://www.treasurydirect.gov/govt/reports/slgs/slgs_mnthlyslgsstat.htm",
                     "describedByType": "text/html",
                     "downloadURL": "https://api.transparency.treasury.gov/services/api/fiscal_service/v1/accounting/od/slgs_statistics",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "Monthly SLGS Statistics",
-            "description": "Current Month Balances for Securities Outstanding and Principal Outstanding for SLGS",
+            "identifier": "015-BFS-2014Q3-058",
+            "issued": "2017-01-31T00:00:00",
             "keyword": [
                 "SLGS Securities outstanding / principal outstanding"
             ],
+            "landingPage": "https://transparency.treasury.gov/dataset/monthly-slgs-statistics",
             "modified": "2017-03-31",
+            "primaryITInvestmentUII": "015-000000060",
+            "programCode": [
+                "015:034"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Monthly SLGS Statistics"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:034"
-            ],
-            "describedBy": "https://www.treasurydirect.gov/govt/reports/slgs/slgs_mnthlyslgsstat.htm",
-            "landingPage": "https://transparency.treasury.gov/dataset/monthly-slgs-statistics",
-            "primaryITInvestmentUII": "015-000000060",
-            "issued": "2017-01-31T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q1-11",
+            "describedBy": "https://fiscaldata.treasury.gov/datasets/monthly-statement-public-debt/",
+            "description": "The Monthly Statement of the Public Debt (MSPD) details the Treasury's outstanding debts and the statutory debt limit. Debt is categorized by whether it is marketable or non-marketable and whether it is debt held by the public or debt held by government agencies. All amounts are reported in millions of U.S. dollars. Data is published on the fourth business day of each month, detailing the debt as of the end of the previous month.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/monthly-statement-public-debt/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/monthly-statement-public-debt/",
                     "describedByType": "text/html",
                     "downloadURL": "https://fiscaldata.treasury.gov/datasets/monthly-statement-public-debt/",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/monthly-statement-public-debt/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/monthly-statement-public-debt/",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.transparency.treasury.gov/services/api/fiscal_service/v1/debt/mspd/mspd_table_1",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/monthly-statement-public-debt/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/monthly-statement-public-debt/",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.transparency.treasury.gov/services/api/fiscal_service/v1/debt/mspd/mspd_table_2",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/monthly-statement-public-debt/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/monthly-statement-public-debt/",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.transparency.treasury.gov/services/api/fiscal_service/v1/debt/mspd/mspd_table_3",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/monthly-statement-public-debt/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/monthly-statement-public-debt/",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.transparency.treasury.gov/services/api/fiscal_service/v1/debt/mspd/mspd_table_3_market",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/monthly-statement-public-debt/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/monthly-statement-public-debt/",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.transparency.treasury.gov/services/api/fiscal_service/v1/debt/mspd/mspd_table_3_nonmarket",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/monthly-statement-public-debt/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/monthly-statement-public-debt/",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.transparency.treasury.gov/services/api/fiscal_service/v1/debt/mspd/mspd_table_4",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/monthly-statement-public-debt/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/monthly-statement-public-debt/",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.transparency.treasury.gov/services/api/fiscal_service/v1/debt/mspd/mspd_table_5",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "Monthly Statement of the Public Debt (MSPD)",
-            "description": "The Monthly Statement of the Public Debt (MSPD) details the Treasury's outstanding debts and the statutory debt limit. Debt is categorized by whether it is marketable or non-marketable and whether it is debt held by the public or debt held by government agencies. All amounts are reported in millions of U.S. dollars. Data is published on the fourth business day of each month, detailing the debt as of the end of the previous month.",
+            "identifier": "015-BFS-2014Q1-11",
             "keyword": [
                 "monthly / debt / public debt / government debt / Treasury / monthly statement public debt / mspd / us debt / debt limit"
             ],
+            "landingPage": "https://fiscaldata.treasury.gov/datasets/monthly-statement-public-debt/",
             "modified": "2020-07-08",
+            "primaryITInvestmentUII": "015-000000032",
+            "programCode": [
+                "015:034"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Monthly Statement of the Public Debt (MSPD)"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:034"
-            ],
-            "describedBy": "https://fiscaldata.treasury.gov/datasets/monthly-statement-public-debt/",
-            "landingPage": "https://fiscaldata.treasury.gov/datasets/monthly-statement-public-debt/",
-            "primaryITInvestmentUII": "015-000000032"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q1-13",
+            "describedBy": "https://fiscaldata.treasury.gov/datasets/monthly-treasury-statement/",
+            "description": "The Monthly Treasury Statement (MTS) dataset provides information on the flow of money into and out of the U.S. Department of the Treasury. It includes how deficits are funded, such as borrowing from the public or reducing operating cash, and how surpluses are distributed. Further tables categorize spending (outlays) by department and agency, revenue (receipts) by specific taxes or other government sources of income, and transactions with trust funds such as Social Security or Medicare. All values are reported in millions of U.S. dollars.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/monthly-treasury-statement/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/monthly-treasury-statement/",
                     "describedByType": "text/html",
                     "downloadURL": "https://fiscaldata.treasury.gov/datasets/monthly-treasury-statement/",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/monthly-treasury-statement/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/monthly-treasury-statement/",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.transparency.treasury.gov/services/api/fiscal_service/v1/accounting/mts/mts_table_1",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/monthly-treasury-statement/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/monthly-treasury-statement/",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.transparency.treasury.gov/services/api/fiscal_service/v1/accounting/mts/mts_table_2",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/monthly-treasury-statement/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/monthly-treasury-statement/",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.transparency.treasury.gov/services/api/fiscal_service/v1/accounting/mts/mts_table_3",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/monthly-treasury-statement/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/monthly-treasury-statement/",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.transparency.treasury.gov/services/api/fiscal_service/v1/accounting/mts/mts_table_4",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/monthly-treasury-statement/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/monthly-treasury-statement/",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.transparency.treasury.gov/services/api/fiscal_service/v1/accounting/mts/mts_table_5",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/monthly-treasury-statement/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/monthly-treasury-statement/",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.transparency.treasury.gov/services/api/fiscal_service/v1/accounting/mts/mts_table_6",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/monthly-treasury-statement/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/monthly-treasury-statement/",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.transparency.treasury.gov/services/api/fiscal_service/v1/accounting/mts/mts_table_6a",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/monthly-treasury-statement/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/monthly-treasury-statement/",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.transparency.treasury.gov/services/api/fiscal_service/v1/accounting/mts/mts_table_6b",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/monthly-treasury-statement/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/monthly-treasury-statement/",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.transparency.treasury.gov/services/api/fiscal_service/v1/accounting/mts/mts_table_6c",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/monthly-treasury-statement/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/monthly-treasury-statement/",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.transparency.treasury.gov/services/api/fiscal_service/v1/accounting/mts/mts_table_6d",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/monthly-treasury-statement/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/monthly-treasury-statement/",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.transparency.treasury.gov/services/api/fiscal_service/v1/accounting/mts/mts_table_6e",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/monthly-treasury-statement/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/monthly-treasury-statement/",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.transparency.treasury.gov/services/api/fiscal_service/v1/accounting/mts/mts_table_7",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/monthly-treasury-statement/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/monthly-treasury-statement/",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.transparency.treasury.gov/services/api/fiscal_service/v1/accounting/mts/mts_table_8",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/monthly-treasury-statement/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/monthly-treasury-statement/",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.transparency.treasury.gov/services/api/fiscal_service/v1/accounting/mts/mts_table_9",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "Monthly Treasury Statement (MTS)",
-            "description": "The Monthly Treasury Statement (MTS) dataset provides information on the flow of money into and out of the U.S. Department of the Treasury. It includes how deficits are funded, such as borrowing from the public or reducing operating cash, and how surpluses are distributed. Further tables categorize spending (outlays) by department and agency, revenue (receipts) by specific taxes or other government sources of income, and transactions with trust funds such as Social Security or Medicare. All values are reported in millions of U.S. dollars.",
+            "identifier": "015-BFS-2014Q1-13",
             "keyword": [
                 "debt / revenue / spending / federal government / surplus",
                 "deficit / Treasury / US Treasury / outlays / receipts / monthly treasury statement / mts"
             ],
+            "landingPage": "https://fiscaldata.treasury.gov/datasets/monthly-treasury-statement/",
             "modified": "2020-07-14",
+            "primaryITInvestmentUII": "015-000000032",
+            "programCode": [
+                "015:031"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Monthly Treasury Statement (MTS)"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:031"
-            ],
-            "describedBy": "https://fiscaldata.treasury.gov/datasets/monthly-treasury-statement/",
-            "landingPage": "https://fiscaldata.treasury.gov/datasets/monthly-treasury-statement/",
-            "primaryITInvestmentUII": "015-000000032"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q3-104",
+            "describedBy": "http://www.treasurydirect.gov/govt/reports/ir/ir_netdisc.pdf",
+            "description": "The Net Discount Activity report displays the amount of premium less discount for Marketable and Nonmarketable Securities as reported to the Financial Management Service.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://transparency.treasury.gov/dataset/net-discount-activity-report",
                     "describedBy": "http://www.treasurydirect.gov/govt/reports/ir/ir_netdisc.pdf",
                     "describedByType": "application/pdf",
                     "downloadURL": "http://www.treasurydirect.gov/govt/reports/ir/ir_netdisc.pdf",
-                    "mediaType": "application/pdf",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/pdf"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "Net Discount Activity Report",
-            "description": "The Net Discount Activity report displays the amount of premium less discount for Marketable and Nonmarketable Securities as reported to the Financial Management Service.",
+            "identifier": "015-BFS-2014Q3-104",
+            "issued": "2014-05-12T00:00:00",
             "keyword": [
                 "marketable and non-marketable premium less discount"
             ],
+            "landingPage": "https://transparency.treasury.gov/dataset/net-discount-activity-report",
             "modified": "2016-07-28",
+            "primaryITInvestmentUII": "015-000000060",
+            "programCode": [
+                "015:034"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Net Discount Activity Report"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:034"
-            ],
-            "describedBy": "http://www.treasurydirect.gov/govt/reports/ir/ir_netdisc.pdf",
-            "landingPage": "https://transparency.treasury.gov/dataset/net-discount-activity-report",
-            "primaryITInvestmentUII": "015-000000060",
-            "issued": "2014-05-12T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q3-047",
+            "describedBy": "https://fiscal.treasury.gov/reports-statements/financial-report/current-report.html",
+            "description": "The notes for statements on the Financial Report of the US Government.  Fiscal Service will issue specific data sets in future Open Data Policy releases.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://transparency.treasury.gov/dataset/notes-to-financial-statements",
                     "describedBy": "https://fiscal.treasury.gov/reports-statements/financial-report/current-report.html",
                     "describedByType": "text/html",
                     "downloadURL": "https://fiscal.treasury.gov/reports-statements/financial-report/current-report.html",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "title": "Notes to Financial Statements",
-            "description": "The notes for statements on the Financial Report of the US Government.  Fiscal Service will issue specific data sets in future Open Data Policy releases.",
+            "identifier": "015-BFS-2014Q3-047",
+            "issued": "2014-05-12T00:00:00",
             "keyword": [
                 "Notes"
             ],
+            "landingPage": "https://transparency.treasury.gov/dataset/notes-to-financial-statements",
             "modified": "2019-06-25",
+            "primaryITInvestmentUII": "015-000000032",
+            "programCode": [
+                "015:031"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Notes to Financial Statements"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:031"
-            ],
-            "describedBy": "https://fiscal.treasury.gov/reports-statements/financial-report/current-report.html",
-            "landingPage": "https://transparency.treasury.gov/dataset/notes-to-financial-statements",
-            "primaryITInvestmentUII": "015-000000032",
-            "issued": "2014-05-12T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q3-040",
+            "describedBy": "https://fiscal.treasury.gov/reports-statements/combined-statement/receipts-by-dept.html",
+            "description": "Quarterly report that lists the receipts and amount by Departments.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://transparency.treasury.gov/dataset/preliminary-receipts-by-department",
                     "describedBy": "https://fiscal.treasury.gov/reports-statements/combined-statement/receipts-by-dept.html",
                     "describedByType": "text/html",
                     "downloadURL": "https://fiscal.treasury.gov/reports-statements/combined-statement/receipts-by-dept.html",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "title": "Preliminary Receipts by Department",
-            "description": "Quarterly report that lists the receipts and amount by Departments.",
+            "identifier": "015-BFS-2014Q3-040",
+            "issued": "2014-05-12T00:00:00",
             "keyword": [
                 "Receipts"
             ],
+            "landingPage": "https://transparency.treasury.gov/dataset/preliminary-receipts-by-department",
             "modified": "2019-06-25",
+            "primaryITInvestmentUII": "015-000000032",
+            "programCode": [
+                "015:031"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Preliminary Receipts by Department"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:031"
-            ],
-            "describedBy": "https://fiscal.treasury.gov/reports-statements/combined-statement/receipts-by-dept.html",
-            "landingPage": "https://transparency.treasury.gov/dataset/preliminary-receipts-by-department",
-            "primaryITInvestmentUII": "015-000000032",
-            "issued": "2014-05-12T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q3-100",
+            "describedBy": "http://www.treasurydirect.gov/govt/reports/fip/podr/podr.htm",
+            "description": "Daily Principal Outstanding",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://transparency.treasury.gov/dataset/principal-outstanding-detail-reports",
                     "describedBy": "http://www.treasurydirect.gov/govt/reports/fip/podr/podr.htm",
                     "describedByType": "text/html",
                     "downloadURL": "http://www.treasurydirect.gov/govt/reports/fip/podr/podr.htm",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "Principal Outstanding Detail Reports",
-            "description": "Daily Principal Outstanding",
+            "identifier": "015-BFS-2014Q3-100",
+            "issued": "2014-05-12T00:00:00",
             "keyword": [
                 "Federal Investment daily principal outstanding"
             ],
+            "landingPage": "https://transparency.treasury.gov/dataset/principal-outstanding-detail-reports",
             "modified": "2016-07-28",
+            "primaryITInvestmentUII": "015-000000060",
+            "programCode": [
+                "015:034"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Principal Outstanding Detail Reports"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:034"
-            ],
-            "describedBy": "http://www.treasurydirect.gov/govt/reports/fip/podr/podr.htm",
-            "landingPage": "https://transparency.treasury.gov/dataset/principal-outstanding-detail-reports",
-            "primaryITInvestmentUII": "015-000000060",
-            "issued": "2014-05-12T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q3-082",
+            "describedBy": "https://www.treasurydirect.gov/GA-SL/SLGS/selectQTCDate.htm",
+            "description": "Section 54A of the Internal Revenue Code (IRC) provides rules for the issuance and use of qualified tax credit bonds including new clean renewable energy bonds, qualified energy conservation bonds, qualified zone academy bonds, and qualified school construction bonds.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.treasurydirect.gov/govt/rates/rates_irstcb.htm",
                     "describedBy": "https://www.treasurydirect.gov/GA-SL/SLGS/selectQTCDate.htm",
                     "describedByType": "text/html",
                     "downloadURL": "https://api.transparency.treasury.gov/services/api/fiscal_service/v1/accounting/od/qualified_tax",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 }
             ],
-            "accrualPeriodicity": "R/P1D",
-            "title": "Qualified Tax Credit Bond Rates",
-            "description": "Section 54A of the Internal Revenue Code (IRC) provides rules for the issuance and use of qualified tax credit bonds including new clean renewable energy bonds, qualified energy conservation bonds, qualified zone academy bonds, and qualified school construction bonds.",
+            "identifier": "015-BFS-2014Q3-082",
+            "issued": "2017-02-22T00:00:00",
             "keyword": [
                 "interest rates for Qualified tax credit bonds"
             ],
+            "landingPage": "https://www.treasurydirect.gov/govt/rates/rates_irstcb.htm",
             "modified": "2017-03-31",
+            "primaryITInvestmentUII": "015-000000060",
+            "programCode": [
+                "015:034"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Qualified Tax Credit Bond Rates"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:034"
-            ],
-            "describedBy": "https://www.treasurydirect.gov/GA-SL/SLGS/selectQTCDate.htm",
-            "landingPage": "https://www.treasurydirect.gov/govt/rates/rates_irstcb.htm",
-            "primaryITInvestmentUII": "015-000000060",
-            "issued": "2017-02-22T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q3-083",
+            "describedBy": "https://www.treasurydirect.gov/GA-SL/SLGS/selectQZABDate.htm",
+            "description": "Section 1397E of the Internal Revenue Code (IRC) provides rules for the issuance and use of qualified zone academy bonds (QZABs) issued on or before October 3, 2008. Sections 54A and 54E provide rules for the issuance and use of qualified zone academy bonds (QZABs) issued after October 3, 2008.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://transparency.treasury.gov/dataset/qualified-zone-academy-bond-rates",
                     "describedBy": "https://www.treasurydirect.gov/GA-SL/SLGS/selectQZABDate.htm",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.treasurydirect.gov/GA-SL/SLGS/selectQZABDate.htm",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1D",
-            "title": "Qualified Zone Academy Bond Rates",
-            "description": "Section 1397E of the Internal Revenue Code (IRC) provides rules for the issuance and use of qualified zone academy bonds (QZABs) issued on or before October 3, 2008. Sections 54A and 54E provide rules for the issuance and use of qualified zone academy bonds (QZABs) issued after October 3, 2008.",
+            "identifier": "015-BFS-2014Q3-083",
+            "issued": "2014-05-12T00:00:00",
             "keyword": [
                 "interest rates for qualified zone academy bonds"
             ],
+            "landingPage": "https://transparency.treasury.gov/dataset/qualified-zone-academy-bond-rates",
             "modified": "2016-07-28",
+            "primaryITInvestmentUII": "015-000000060",
+            "programCode": [
+                "015:034"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Qualified Zone Academy Bond Rates"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:034"
-            ],
-            "describedBy": "https://www.treasurydirect.gov/GA-SL/SLGS/selectQZABDate.htm",
-            "landingPage": "https://transparency.treasury.gov/dataset/qualified-zone-academy-bond-rates",
-            "primaryITInvestmentUII": "015-000000060",
-            "issued": "2014-05-12T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q3-043",
+            "describedBy": "https://fiscal.treasury.gov/reports-statements/financial-report/reconciliations-of-net-operating-cost.html",
+            "description": "These statements reconcile the results of operations (net operating cost) on the Statements of Operations and Changes in Net Position to the unified budget deficit. The premise of the reconciliation is that the accrual and budgetary accounting bases share transaction data.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://transparency.treasury.gov/dataset/reconciliations-of-net-operating-cost-and-unified-budget-deficit",
                     "describedBy": "https://fiscal.treasury.gov/reports-statements/financial-report/reconciliations-of-net-operating-cost.html",
                     "describedByType": "text/html",
                     "downloadURL": "https://fiscal.treasury.gov/reports-statements/financial-report/reconciliations-of-net-operating-cost.html",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "title": "Reconciliations of Net Operating Cost and Unified Budget Deficit",
-            "description": "These statements reconcile the results of operations (net operating cost) on the Statements of Operations and Changes in Net Position to the unified budget deficit. The premise of the reconciliation is that the accrual and budgetary accounting bases share transaction data.",
+            "identifier": "015-BFS-2014Q3-043",
+            "issued": "2014-05-12T00:00:00",
             "keyword": [
                 "Net Operating Cost / Unified Budget Deficit"
             ],
+            "landingPage": "https://transparency.treasury.gov/dataset/reconciliations-of-net-operating-cost-and-unified-budget-deficit",
             "modified": "2019-06-25",
+            "primaryITInvestmentUII": "015-000000032",
+            "programCode": [
+                "015:031"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Reconciliations of Net Operating Cost and Unified Budget Deficit"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:031"
-            ],
-            "describedBy": "https://fiscal.treasury.gov/reports-statements/financial-report/reconciliations-of-net-operating-cost.html",
-            "landingPage": "https://transparency.treasury.gov/dataset/reconciliations-of-net-operating-cost-and-unified-budget-deficit",
-            "primaryITInvestmentUII": "015-000000032",
-            "issued": "2014-05-12T00:00:00"
-        },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q1-14",
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            },
+            "describedBy": "https://fiscaldata.treasury.gov/datasets/record-setting-auction-data/",
+            "description": "Record-Setting Auction Data provides record highs and lows from U.S. Treasury auctions. This includes lowest and highest rates/yields, highest offering amount, and highest bid-to-cover ratios as well as the dates for these record-setting auctions. The data also indicates the security type and term. Security types include Treasury Bills, Treasury Notes, Treasury Nonds, Cash Management Bills (CMBs), Floating Rate Notes (FRNs), and Treasury Inflation-Protected Securities (TIPS). Security terms range from a few days for CMBs to 30-year securities. The U.S. Treasury uses an auction process to sell these marketable securities and determine their rate or yield. Marketable securities can be bought, sold, or transferred after they are originally issued.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/record-setting-auction-data/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/record-setting-auction-data/",
                     "describedByType": "text/html",
                     "downloadURL": "https://fiscaldata.treasury.gov/datasets/record-setting-auction-data/",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/record-setting-auction-data/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/record-setting-auction-data/",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.transparency.treasury.gov/services/api/fiscal_service/v2/accounting/od/record_setting_auction",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Record-Setting Auction Data",
-            "description": "Record-Setting Auction Data provides record highs and lows from U.S. Treasury auctions. This includes lowest and highest rates/yields, highest offering amount, and highest bid-to-cover ratios as well as the dates for these record-setting auctions. The data also indicates the security type and term. Security types include Treasury Bills, Treasury Notes, Treasury Nonds, Cash Management Bills (CMBs), Floating Rate Notes (FRNs), and Treasury Inflation-Protected Securities (TIPS). Security terms range from a few days for CMBs to 30-year securities. The U.S. Treasury uses an auction process to sell these marketable securities and determine their rate or yield. Marketable securities can be bought, sold, or transferred after they are originally issued.",
+            "identifier": "015-BFS-2014Q1-14",
             "keyword": [
                 "auctions / debt / rates / yields / securities / treasury securities / treasury auctions / treasury bills / treasury notes / treasury bonds / TIPS / FRNs / CMBs / treasury rates / treasury offerings"
             ],
+            "landingPage": "https://fiscaldata.treasury.gov/datasets/record-setting-auction-data/",
             "modified": "2020-07-30",
+            "primaryITInvestmentUII": "015-000000032",
+            "programCode": [
+                "015:035"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Record-Setting Auction Data"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P6M",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:035"
-            ],
-            "describedBy": "https://fiscaldata.treasury.gov/datasets/record-setting-auction-data/",
-            "landingPage": "https://fiscaldata.treasury.gov/datasets/record-setting-auction-data/",
-            "primaryITInvestmentUII": "015-000000032"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q3-096",
+            "describedBy": "https://fiscaldata.treasury.gov/datasets/redemption-tables/",
+            "description": "The Redemption Tables dataset contains monthly tables that list the redemption value, interest earned, and yield of accrual savings bonds. Accrual savings bonds included in the dataset were issued as far back as 1941. Each monthly report lists the redemption value of all bonds at the time of publication. Investors and bond owners can use this dataset as an easy and understandable reference to know the redemption value of the bonds they hold.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/redemption-tables/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/redemption-tables/",
                     "describedByType": "text/html",
                     "downloadURL": "https://fiscaldata.treasury.gov/datasets/redemption-tables/",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/redemption-tables/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/redemption-tables/",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.transparency.treasury.gov/services/api/fiscal_service/v1/accounting/od/redemption_tables",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 }
             ],
-            "accrualPeriodicity": "R/P6M",
-            "title": "Redemption Tables",
-            "description": "The Redemption Tables dataset contains monthly tables that list the redemption value, interest earned, and yield of accrual savings bonds. Accrual savings bonds included in the dataset were issued as far back as 1941. Each monthly report lists the redemption value of all bonds at the time of publication. Investors and bond owners can use this dataset as an easy and understandable reference to know the redemption value of the bonds they hold.",
+            "identifier": "015-BFS-2014Q3-096",
             "keyword": [
                 "savings bonds / redeem / value / Series EE bonds / Series E bonds / Series I bonds /  savings bond redemption"
             ],
+            "landingPage": "https://fiscaldata.treasury.gov/datasets/redemption-tables/",
             "modified": "2020-05-20",
+            "primaryITInvestmentUII": "015-000000062",
+            "programCode": [
+                "015:033"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Redemption Tables"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:033"
-            ],
-            "describedBy": "https://fiscaldata.treasury.gov/datasets/redemption-tables/",
-            "landingPage": "https://fiscaldata.treasury.gov/datasets/redemption-tables/",
-            "primaryITInvestmentUII": "015-000000062"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q3-075",
+            "describedBy": "http://www.treasurydirect.gov/govt/reports/pd/pd_sbntables_downloadable_files.htm",
+            "description": "The downloadable files posted on this page include the Savings Bonds and Notes (SBN) tables in their entirety",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://transparency.treasury.gov/dataset/savings-bonds-and-notes-tables-and-downloadable-files",
                     "describedBy": "http://www.treasurydirect.gov/govt/reports/pd/pd_sbntables_downloadable_files.htm",
                     "describedByType": "text/html",
                     "downloadURL": "http://www.treasurydirect.gov/govt/reports/pd/pd_sbntables_downloadable_files.htm",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "Savings Bonds and Notes (SBN) Tables and Downloadable Files",
-            "description": "The downloadable files posted on this page include the Savings Bonds and Notes (SBN) tables in their entirety",
+            "identifier": "015-BFS-2014Q3-075",
+            "issued": "2014-05-12T00:00:00",
             "keyword": [
                 "savings bonds and notes / sales and redemptions"
             ],
+            "landingPage": "https://transparency.treasury.gov/dataset/savings-bonds-and-notes-tables-and-downloadable-files",
             "modified": "2016-07-28",
+            "primaryITInvestmentUII": "015-000000062",
+            "programCode": [
+                "015:033"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Savings Bonds and Notes (SBN) Tables and Downloadable Files"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:033"
-            ],
-            "describedBy": "http://www.treasurydirect.gov/govt/reports/pd/pd_sbntables_downloadable_files.htm",
-            "landingPage": "https://transparency.treasury.gov/dataset/savings-bonds-and-notes-tables-and-downloadable-files",
-            "primaryITInvestmentUII": "015-000000062",
-            "issued": "2014-05-12T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2020Q4-001",
+            "describedBy": "https://fiscaldata.treasury.gov/datasets/savings-bonds-securities/",
+            "description": "The Savings Bonds Securities dataset details how many non-marketable savings bonds have been sold and their value, reported each month. This dataset also contains information about the interest rates and average maturities of these non-marketable savings bonds.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/savings-bonds-securities/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/savings-bonds-securities/",
                     "describedByType": "text/html",
                     "downloadURL": "https://fiscaldata.treasury.gov/datasets/savings-bonds-securities/",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/savings-bonds-securities/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/savings-bonds-securities/",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.transparency.treasury.gov/services/api/fiscal_service/v1/accounting/od/slgs_savings_bonds",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "Savings Bonds Securities",
-            "description": "The Savings Bonds Securities dataset details how many non-marketable savings bonds have been sold and their value, reported each month. This dataset also contains information about the interest rates and average maturities of these non-marketable savings bonds.",
+            "identifier": "015-BFS-2020Q4-001",
             "keyword": [
                 "pieces / amounts / years to maturity / SLGS statistics / debt / savings bonds / securities /  bond value / non-marketable savings bonds / treasuries / interest rates / average maturity"
             ],
+            "landingPage": "https://fiscaldata.treasury.gov/datasets/savings-bonds-securities/",
             "modified": "2020-07-16",
+            "primaryITInvestmentUII": "015-000000061",
+            "programCode": [
+                "015:035"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Savings Bonds Securities"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P6M",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:035"
-            ],
-            "describedBy": "https://fiscaldata.treasury.gov/datasets/savings-bonds-securities/",
-            "landingPage": "https://fiscaldata.treasury.gov/datasets/savings-bonds-securities/",
-            "primaryITInvestmentUII": "015-000000061"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q3-094",
+            "describedBy": "https://fiscaldata.treasury.gov/datasets/savings-bond-value-files/",
+            "description": "The Savings Bond Value Files dataset is used by developers of bond pricing programs to update their systems with new redemption values for accrual savings bonds (Series E, EE, I & Savings Notes). The core data is the same as the Redemption Tables but there are differences in format, amount of data, and date range. The Savings Bonds Value Files dataset is meant for programmers and developers to read in redemption values without having to first convert PDFs.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/savings-bond-value-files/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/savings-bond-value-files/",
                     "describedByType": "text/html",
                     "downloadURL": "https://fiscaldata.treasury.gov/datasets/savings-bond-value-files/",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/savings-bond-value-files/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/savings-bond-value-files/",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.transparency.treasury.gov/services/api/fiscal_service/v1/accounting/od/sb_value",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 }
             ],
-            "accrualPeriodicity": "R/P6M",
-            "title": "Savings Bonds Value Files",
-            "description": "The Savings Bond Value Files dataset is used by developers of bond pricing programs to update their systems with new redemption values for accrual savings bonds (Series E, EE, I & Savings Notes). The core data is the same as the Redemption Tables but there are differences in format, amount of data, and date range. The Savings Bonds Value Files dataset is meant for programmers and developers to read in redemption values without having to first convert PDFs.",
+            "identifier": "015-BFS-2014Q3-094",
             "keyword": [
                 "savings bonds / interest rates / value / redemption tables / interest / yield / plaintext / savings bond"
             ],
+            "landingPage": "https://fiscaldata.treasury.gov/datasets/savings-bond-value-files/",
             "modified": "2020-06-02",
+            "primaryITInvestmentUII": "015-000000062",
+            "programCode": [
+                "015:033"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Savings Bonds Value Files"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:033"
-            ],
-            "describedBy": "https://fiscaldata.treasury.gov/datasets/savings-bond-value-files/",
-            "landingPage": "https://fiscaldata.treasury.gov/datasets/savings-bond-value-files/",
-            "primaryITInvestmentUII": "015-000000062"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q3-076",
+            "describedBy": "https://fiscaldata.treasury.gov/datasets/schedules-federal-debt/",
+            "description": "The Schedules of Federal Debt dataset provides monthly and fiscal year-to-date changes in federal debt. It shows increases (borrowing) and decreases (repayments) in debt. The data notes whether the debt is debt held by the public or intragovernmental holdings. These two categories are further broken down into principal debt, accrued interest payable, and net unamortized premiums/discounts. All figures are rounded to the nearest million.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/schedules-federal-debt/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/schedules-federal-debt/",
                     "describedByType": "text/html",
                     "downloadURL": "https://fiscaldata.treasury.gov/datasets/schedules-federal-debt/",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/schedules-federal-debt/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/schedules-federal-debt/",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.transparency.treasury.gov/services/api/fiscal_service/v1/accounting/od/schedules_fed_debt",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/schedules-federal-debt/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/schedules-federal-debt/",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.transparency.treasury.gov/services/api/fiscal_service/v1/accounting/od/schedules_fed_debt_fytd",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "Schedules of Federal Debt",
-            "description": "The Schedules of Federal Debt dataset provides monthly and fiscal year-to-date changes in federal debt. It shows increases (borrowing) and decreases (repayments) in debt. The data notes whether the debt is debt held by the public or intragovernmental holdings. These two categories are further broken down into principal debt, accrued interest payable, and net unamortized premiums/discounts. All figures are rounded to the nearest million.",
+            "identifier": "015-BFS-2014Q3-076",
             "keyword": [
                 "schedules / debt / public debt /  US debt / federal debt / accrued interest on the debt / interest on the debt / intragovernmental holdings"
             ],
+            "landingPage": "https://fiscaldata.treasury.gov/datasets/schedules-federal-debt/",
             "modified": "2020-07-07",
+            "primaryITInvestmentUII": "015-000000060",
+            "programCode": [
+                "015:034"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Schedules of Federal Debt"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:034"
-            ],
-            "describedBy": "https://fiscaldata.treasury.gov/datasets/schedules-federal-debt/",
-            "landingPage": "https://fiscaldata.treasury.gov/datasets/schedules-federal-debt/",
-            "primaryITInvestmentUII": "015-000000060"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q3-080",
+            "describedBy": "http://www.treasurydirect.gov/govt/reports/pd/pd_tdsecuritiesissued.xlsm",
+            "description": "Shows sales, incoming transfers, redemptions, amount outstanding, number of accounts in TreasuryDirect",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://transparency.treasury.gov/dataset/securities-issued-in-treasurydirect",
                     "describedBy": "http://www.treasurydirect.gov/govt/reports/pd/pd_tdsecuritiesissued.xlsm",
                     "describedByType": "text/html",
                     "downloadURL": "http://www.treasurydirect.gov/govt/reports/pd/pd_tdsecuritiesissued.xlsm",
-                    "mediaType": "application/vnd.ms-excel",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.ms-excel"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "Securities Issued in TreasuryDirect",
-            "description": "Shows sales, incoming transfers, redemptions, amount outstanding, number of accounts in TreasuryDirect",
+            "identifier": "015-BFS-2014Q3-080",
+            "issued": "2014-05-12T00:00:00",
             "keyword": [
                 "securities sold in TreasuryDirect"
             ],
+            "landingPage": "https://transparency.treasury.gov/dataset/securities-issued-in-treasurydirect",
             "modified": "2016-07-28",
+            "primaryITInvestmentUII": "015-000000062",
+            "programCode": [
+                "015:033"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Securities Issued in TreasuryDirect"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:033"
-            ],
-            "describedBy": "http://www.treasurydirect.gov/govt/reports/pd/pd_tdsecuritiesissued.xlsm",
-            "landingPage": "https://transparency.treasury.gov/dataset/securities-issued-in-treasurydirect",
-            "primaryITInvestmentUII": "015-000000062",
-            "issued": "2014-05-12T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q3-057",
+            "describedBy": "https://www.treasurydirect.gov/GA-SL/SLGS/selectSLGSDate.htm",
+            "description": "The State and Local Government Series (SLGS) securities program was established in 1972 as the result of federal legislation enacted in 1969 which restricted state and local governments from earning arbitrage profits by investing bond proceeds in higher yielding investments.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://transparency.treasury.gov/dataset/state-and-local-government-series-daily-rate-table",
                     "describedBy": "https://www.treasurydirect.gov/GA-SL/SLGS/selectSLGSDate.htm",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.treasurydirect.gov/GA-SL/SLGS/selectSLGSDate.htm",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1D",
-            "title": "State and Local Government Series Daily Rate Table",
-            "description": "The State and Local Government Series (SLGS) securities program was established in 1972 as the result of federal legislation enacted in 1969 which restricted state and local governments from earning arbitrage profits by investing bond proceeds in higher yielding investments.",
+            "identifier": "015-BFS-2014Q3-057",
+            "issued": "2014-05-12T00:00:00",
             "keyword": [
                 "state and local government series / daily rate / arbitrage"
             ],
+            "landingPage": "https://transparency.treasury.gov/dataset/state-and-local-government-series-daily-rate-table",
             "modified": "2016-07-28",
+            "primaryITInvestmentUII": "015-000000060",
+            "programCode": [
+                "015:034"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "State and Local Government Series Daily Rate Table"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:034"
-            ],
-            "describedBy": "https://www.treasurydirect.gov/GA-SL/SLGS/selectSLGSDate.htm",
-            "landingPage": "https://transparency.treasury.gov/dataset/state-and-local-government-series-daily-rate-table",
-            "primaryITInvestmentUII": "015-000000060",
-            "issued": "2014-05-12T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2020Q4-002",
+            "describedBy": "https://fiscaldata.treasury.gov/datasets/slgs-securities/",
+            "description": "The State and Local Government Series Securities (Non-Marketable) dataset details how many non-marketable State and Local Government Securities (SLGS) have been sold and their value, reported each month. This dataset also includes information about how many bonds have yet to mature and their timeline to maturity, organized in various buckets: 0-3 months to maturity, 3-6 months, etc.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/slgs-securities/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/slgs-securities/",
                     "describedByType": "text/html",
                     "downloadURL": "https://fiscaldata.treasury.gov/datasets/slgs-securities/",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/slgs-securities/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/slgs-securities/",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.transparency.treasury.gov/services/api/fiscal_service/v1/accounting/od/slgs_securities",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 }
             ],
-            "accrualPeriodicity": "R/P1D",
-            "title": "State and Local Government Series Securities (Non-Marketable)",
-            "description": "The State and Local Government Series Securities (Non-Marketable) dataset details how many non-marketable State and Local Government Securities (SLGS) have been sold and their value, reported each month. This dataset also includes information about how many bonds have yet to mature and their timeline to maturity, organized in various buckets: 0-3 months to maturity, 3-6 months, etc.",
+            "identifier": "015-BFS-2020Q4-002",
             "keyword": [
                 "SLGS / non-marketable / interest rates / state / local / securities / non-marketable securities /  government securities / time deposit  demand deposit / subscriptions / state and local securities"
             ],
+            "landingPage": "https://fiscaldata.treasury.gov/datasets/slgs-securities/",
             "modified": "2020-07-30",
+            "primaryITInvestmentUII": "015-000000061",
+            "programCode": [
+                "015:035"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "State and Local Government Series Securities (Non-Marketable)"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:035"
-            ],
-            "describedBy": "https://fiscaldata.treasury.gov/datasets/slgs-securities/",
-            "landingPage": "https://fiscaldata.treasury.gov/datasets/slgs-securities/",
-            "primaryITInvestmentUII": "015-000000061"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q3-044",
+            "describedBy": "https://fiscal.treasury.gov/reports-statements/financial-report/statements-of-change-cash-balance.html",
+            "description": "The primary purpose of these statements is to report how the annual unified budget deficit relates to the change in the Government's cash and other monetary assets and debt held by the public. It explains why the unified budget deficit normally would not result in an equivalent change in the Government's cash and other monetary assets.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://transparency.treasury.gov/dataset/statements-of-changes-in-cash-balance-from-unified-budget-and-other-activities",
                     "describedBy": "https://fiscal.treasury.gov/reports-statements/financial-report/statements-of-change-cash-balance.html",
                     "describedByType": "text/html",
                     "downloadURL": "https://fiscal.treasury.gov/reports-statements/financial-report/statements-of-change-cash-balance.html",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "title": "Statements of Changes in Cash Balance from Unified Budget and Other Activities",
-            "description": "The primary purpose of these statements is to report how the annual unified budget deficit relates to the change in the Government's cash and other monetary assets and debt held by the public. It explains why the unified budget deficit normally would not result in an equivalent change in the Government's cash and other monetary assets.",
+            "identifier": "015-BFS-2014Q3-044",
+            "issued": "2014-05-12T00:00:00",
             "keyword": [
                 "Cash Balance / Unified Budget"
             ],
+            "landingPage": "https://transparency.treasury.gov/dataset/statements-of-changes-in-cash-balance-from-unified-budget-and-other-activities",
             "modified": "2019-06-25",
+            "primaryITInvestmentUII": "015-000000032",
+            "programCode": [
+                "015:031"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Statements of Changes in Cash Balance from Unified Budget and Other Activities"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:031"
-            ],
-            "describedBy": "https://fiscal.treasury.gov/reports-statements/financial-report/statements-of-change-cash-balance.html",
-            "landingPage": "https://transparency.treasury.gov/dataset/statements-of-changes-in-cash-balance-from-unified-budget-and-other-activities",
-            "primaryITInvestmentUII": "015-000000032",
-            "issued": "2014-05-12T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q3-041",
+            "describedBy": "https://fiscal.treasury.gov/reports-statements/financial-report/statement-of-net-cost.html",
+            "description": "These statements present the year over year net cost of United States Government operations, including the operations related to earmarked funds (funds financed by specifically identified revenues, often supplemented by other financing sources, which remain available over time).",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://transparency.treasury.gov/dataset/statements-of-net-cost",
                     "describedBy": "https://fiscal.treasury.gov/reports-statements/financial-report/statement-of-net-cost.html",
                     "describedByType": "text/html",
                     "downloadURL": "https://fiscal.treasury.gov/reports-statements/financial-report/statement-of-net-cost.html",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "title": "Statements of Net Cost",
-            "description": "These statements present the year over year net cost of United States Government operations, including the operations related to earmarked funds (funds financed by specifically identified revenues, often supplemented by other financing sources, which remain available over time).",
+            "identifier": "015-BFS-2014Q3-041",
+            "issued": "2014-05-12T00:00:00",
             "keyword": [
                 "Net Cost"
             ],
+            "landingPage": "https://transparency.treasury.gov/dataset/statements-of-net-cost",
             "modified": "2019-06-25",
+            "primaryITInvestmentUII": "015-000000032",
+            "programCode": [
+                "015:031"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Statements of Net Cost"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:031"
-            ],
-            "describedBy": "https://fiscal.treasury.gov/reports-statements/financial-report/statement-of-net-cost.html",
-            "landingPage": "https://transparency.treasury.gov/dataset/statements-of-net-cost",
-            "primaryITInvestmentUII": "015-000000032",
-            "issued": "2014-05-12T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q3-042",
+            "describedBy": "https://fiscal.treasury.gov/reports-statements/financial-report/statements-of-operations-changes.html",
+            "description": "These statements report the results of Government operations, which include the results of operations for earmarked funds. They include non-exchange revenues that are generated principally by the Government's sovereign power to tax, levy duties, and assess fines and penalties. These statements also present the cost of Government operations, net of revenue earned from the sale of goods and services to the public (exchange revenue). They further include certain adjustments and unreconciled transactions that affect the net position.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://transparency.treasury.gov/dataset/statements-of-operations-and-changes-in-net-position",
                     "describedBy": "https://fiscal.treasury.gov/reports-statements/financial-report/statements-of-operations-changes.html",
                     "describedByType": "text/html",
                     "downloadURL": "https://fiscal.treasury.gov/reports-statements/financial-report/statements-of-operations-changes.html",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "title": "Statements of Operations and Changes in Net Position",
-            "description": "These statements report the results of Government operations, which include the results of operations for earmarked funds. They include non-exchange revenues that are generated principally by the Government's sovereign power to tax, levy duties, and assess fines and penalties. These statements also present the cost of Government operations, net of revenue earned from the sale of goods and services to the public (exchange revenue). They further include certain adjustments and unreconciled transactions that affect the net position.",
+            "identifier": "015-BFS-2014Q3-042",
+            "issued": "2014-05-12T00:00:00",
             "keyword": [
                 "Net Position"
             ],
+            "landingPage": "https://transparency.treasury.gov/dataset/statements-of-operations-and-changes-in-net-position",
             "modified": "2019-06-25",
+            "primaryITInvestmentUII": "015-000000032",
+            "programCode": [
+                "015:031"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Statements of Operations and Changes in Net Position"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:031"
-            ],
-            "describedBy": "https://fiscal.treasury.gov/reports-statements/financial-report/statements-of-operations-changes.html",
-            "landingPage": "https://transparency.treasury.gov/dataset/statements-of-operations-and-changes-in-net-position",
-            "primaryITInvestmentUII": "015-000000032",
-            "issued": "2014-05-12T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q3-046",
+            "describedBy": "https://fiscal.treasury.gov/reports-statements/financial-report/statements-of-social-insurance.html",
+            "description": "The Statements of Social Insurance provide estimates of the status of the most significant social insurance programs: Social Security, Medicare, Railroad Retirement, and Black Lung social insurance programs.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://transparency.treasury.gov/dataset/statements-of-social-insurance-and-changes-in-social-insurance-amounts",
                     "describedBy": "https://fiscal.treasury.gov/reports-statements/financial-report/statements-of-social-insurance.html",
                     "describedByType": "text/html",
                     "downloadURL": "https://fiscal.treasury.gov/reports-statements/financial-report/statements-of-social-insurance.html",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "title": "Statements of Social Insurance and Changes in Social Insurance Amounts",
-            "description": "The Statements of Social Insurance provide estimates of the status of the most significant social insurance programs: Social Security, Medicare, Railroad Retirement, and Black Lung social insurance programs.",
+            "identifier": "015-BFS-2014Q3-046",
+            "issued": "2014-05-12T00:00:00",
             "keyword": [
                 "Social Insurance"
             ],
+            "landingPage": "https://transparency.treasury.gov/dataset/statements-of-social-insurance-and-changes-in-social-insurance-amounts",
             "modified": "2019-06-25",
+            "primaryITInvestmentUII": "015-000000032",
+            "programCode": [
+                "015:031"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Statements of Social Insurance and Changes in Social Insurance Amounts"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:031"
-            ],
-            "describedBy": "https://fiscal.treasury.gov/reports-statements/financial-report/statements-of-social-insurance.html",
-            "landingPage": "https://transparency.treasury.gov/dataset/statements-of-social-insurance-and-changes-in-social-insurance-amounts",
-            "primaryITInvestmentUII": "015-000000032",
-            "issued": "2014-05-12T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q3-066",
+            "describedBy": "http://www.treasurydirect.gov/govt/reports/pd/pd_accountrpt.htm",
+            "description": "The Accountability Report is comprised of the following five separate financial statements: Balance Sheet; Statement of Net Cost; Statement of Change in Net Position; Statement of Budgetary Resources, and Statement of Custodial Activity",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://transparency.treasury.gov/dataset/the-accountability-report",
                     "describedBy": "http://www.treasurydirect.gov/govt/reports/pd/pd_accountrpt.htm",
                     "describedByType": "text/html",
                     "downloadURL": "http://www.treasurydirect.gov/govt/reports/pd/pd_accountrpt.htm",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "The Accountability Report",
-            "description": "The Accountability Report is comprised of the following five separate financial statements: Balance Sheet; Statement of Net Cost; Statement of Change in Net Position; Statement of Budgetary Resources, and Statement of Custodial Activity",
+            "identifier": "015-BFS-2014Q3-066",
+            "issued": "2014-05-12T00:00:00",
             "keyword": [
                 "Accountability / financial statements"
             ],
+            "landingPage": "https://transparency.treasury.gov/dataset/the-accountability-report",
             "modified": "2016-07-28",
+            "primaryITInvestmentUII": "015-000000060",
+            "programCode": [
+                "015:034"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "The Accountability Report"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:034"
-            ],
-            "describedBy": "http://www.treasurydirect.gov/govt/reports/pd/pd_accountrpt.htm",
-            "landingPage": "https://transparency.treasury.gov/dataset/the-accountability-report",
-            "primaryITInvestmentUII": "015-000000060",
-            "issued": "2014-05-12T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q1-18",
+            "describedBy": "http://www.treasurydirect.gov/govt/reports/tfmp/tfmp_advactivitiessched.htm",
+            "description": "This table shows what the states are borrowing from the Unemployment Trust Fund in order to pay unemployment benefits.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://transparency.treasury.gov/dataset/title-xii-advance-activities-schedule",
                     "describedBy": "http://www.treasurydirect.gov/govt/reports/tfmp/tfmp_advactivitiessched.htm",
                     "describedByType": "text/html",
                     "downloadURL": "http://www.treasurydirect.gov/govt/reports/tfmp/tfmp_advactivitiessched.htm",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Title XII Advance Activities Schedule",
-            "description": "This table shows what the states are borrowing from the Unemployment Trust Fund in order to pay unemployment benefits.",
+            "identifier": "015-BFS-2014Q1-18",
+            "issued": "2013-10-31T00:00:00",
             "keyword": [
                 "Unemployment Trust Fund borrowings by states"
             ],
+            "landingPage": "https://transparency.treasury.gov/dataset/title-xii-advance-activities-schedule",
             "modified": "2016-07-28",
+            "primaryITInvestmentUII": "015-000000032",
+            "programCode": [
+                "015:034"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Title XII Advance Activities Schedule"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:034"
-            ],
-            "describedBy": "http://www.treasurydirect.gov/govt/reports/tfmp/tfmp_advactivitiessched.htm",
-            "landingPage": "https://transparency.treasury.gov/dataset/title-xii-advance-activities-schedule",
-            "primaryITInvestmentUII": "015-000000032",
-            "issued": "2013-10-31T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q4-001",
+            "describedBy": "http://www.treasurydirect.gov/instit/annceresult/press/press_auctionresults.htm",
+            "description": "Today's Auction Results displays U.S. Treasury marketable securities Noncompetitive Results, Competitive Results, and Announcements and Results by Auction Year.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://transparency.treasury.gov/dataset/today-auction-results",
                     "describedBy": "http://www.treasurydirect.gov/instit/annceresult/press/press_auctionresults.htm",
                     "describedByType": "text/html",
                     "downloadURL": "http://www.treasurydirect.gov/TA_WS/securities/auctioned?format=json&day=0",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 }
             ],
-            "accrualPeriodicity": "R/P1D",
-            "title": "Today's Auction Results",
-            "description": "Today's Auction Results displays U.S. Treasury marketable securities Noncompetitive Results, Competitive Results, and Announcements and Results by Auction Year.",
+            "identifier": "015-BFS-2014Q4-001",
+            "issued": "2014-08-22T00:00:00",
             "keyword": [
                 "competitive results / noncompetitive results / auction / CUSIP"
             ],
+            "landingPage": "https://transparency.treasury.gov/dataset/today-auction-results",
             "modified": "2015-05-04",
+            "primaryITInvestmentUII": "015-000000061",
+            "programCode": [
+                "015:035"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Today's Auction Results"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:035"
-            ],
-            "describedBy": "http://www.treasurydirect.gov/instit/annceresult/press/press_auctionresults.htm",
-            "landingPage": "https://transparency.treasury.gov/dataset/today-auction-results",
-            "primaryITInvestmentUII": "015-000000061",
-            "issued": "2014-08-22T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q3-106",
+            "describedBy": "https://www.sam.fms.treas.gov/sampublic/tasbetc.htm",
+            "description": "A list of values for Treasury Account Symbols (TAS) and Business Event Type Codes (BETC).",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://transparency.treasury.gov/dataset/treasury-account-symbols",
                     "describedBy": "https://www.sam.fms.treas.gov/sampublic/tasbetc.htm",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.sam.fms.treas.gov/sampublic/tasbetc.htm",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Treasury Account Symbols",
-            "description": "A list of values for Treasury Account Symbols (TAS) and Business Event Type Codes (BETC).",
+            "identifier": "015-BFS-2014Q3-106",
+            "issued": "2014-05-12T00:00:00",
             "keyword": [
                 "Treasury Account Symbol / Business Event Type Code / TAS / BETC"
             ],
+            "landingPage": "https://transparency.treasury.gov/dataset/treasury-account-symbols",
             "modified": "2016-07-28",
+            "primaryITInvestmentUII": "015-000000032",
+            "programCode": [
+                "015:031"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Treasury Account Symbols"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:031"
-            ],
-            "describedBy": "https://www.sam.fms.treas.gov/sampublic/tasbetc.htm",
-            "landingPage": "https://transparency.treasury.gov/dataset/treasury-account-symbols",
-            "primaryITInvestmentUII": "015-000000032",
-            "issued": "2014-05-12T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q3-138",
+            "describedBy": "https://www.fiscal.treasury.gov/fsreports/rpt/treasBulletin/treasBulletin_home.htm",
+            "description": "The Treasury Bulletin contains a mix of narratives, tables and charts related to Treasury issues, Federal Financial operations, International statistics, and Financial commitments of the U.S. Government.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://transparency.treasury.gov/dataset/treasury-bulletin",
                     "describedBy": "https://www.fiscal.treasury.gov/fsreports/rpt/treasBulletin/treasBulletin_home.htm",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.fiscal.treasury.gov/fsreports/rpt/treasBulletin/treasBulletin_home.htm",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "title": "Treasury Bulletin",
-            "description": "The Treasury Bulletin contains a mix of narratives, tables and charts related to Treasury issues, Federal Financial operations, International statistics, and Financial commitments of the U.S. Government.",
+            "identifier": "015-BFS-2014Q3-138",
+            "issued": "2014-05-12T00:00:00",
             "keyword": [
                 "Fiscal Operations / Treasury Bulletin"
             ],
-            "modified": "2019-06-25",
+            "landingPage": "https://transparency.treasury.gov/dataset/treasury-bulletin",
+            "modified": "2019-06-25",
+            "primaryITInvestmentUII": "015-000000032",
+            "programCode": [
+                "015:031"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Treasury Bulletin"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:031"
-            ],
-            "describedBy": "https://www.fiscal.treasury.gov/fsreports/rpt/treasBulletin/treasBulletin_home.htm",
-            "landingPage": "https://transparency.treasury.gov/dataset/treasury-bulletin",
-            "primaryITInvestmentUII": "015-000000032",
-            "issued": "2014-05-12T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2017Q2-002",
+            "describedBy": "https://fiscaldata.treasury.gov/datasets/treasury-offset-program/",
+            "description": "This dataset is a summary of five different programs in which states, the District of Columbia (D.C.), and U.S. territories can apply offsets from federal payments\ntowards delinquent debt. These programs are income tax, state reciprocal tax agreements, unemployment insurance, child support, and Supplemental Nutrition\nAssistance Program (SNAP).",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/treasury-offset-program/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/treasury-offset-program/",
                     "describedByType": "text/html",
                     "downloadURL": "https://fiscaldata.treasury.gov/datasets/treasury-offset-program/",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/treasury-offset-program/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/treasury-offset-program/",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.transparency.treasury.gov/services/api/fiscal_service/v1/debt/top/top_federal",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/treasury-offset-program/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/treasury-offset-program/",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.transparency.treasury.gov/services/api/fiscal_service/v1/debt/top/top_state",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "Treasury Offset Program",
-            "description": "This dataset is a summary of five different programs in which states, the District of Columbia (D.C.), and U.S. territories can apply offsets from federal payments\ntowards delinquent debt. These programs are income tax, state reciprocal tax agreements, unemployment insurance, child support, and Supplemental Nutrition\nAssistance Program (SNAP).",
+            "identifier": "015-BFS-2017Q2-002",
             "keyword": [
                 "fiscal service / treasury / federal / state / government / debt / collections / offset / revenue / taxes / debt / income tax / child support / SNAP / government collections / offset / Treasury / delinquent debt / federal withholdings"
             ],
+            "landingPage": "https://fiscaldata.treasury.gov/datasets/treasury-offset-program/",
             "modified": "2020-07-15",
+            "primaryITInvestmentUII": "015-000000026",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Treasury Offset Program"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "describedBy": "https://fiscaldata.treasury.gov/datasets/treasury-offset-program/",
-            "landingPage": "https://fiscaldata.treasury.gov/datasets/treasury-offset-program/",
-            "primaryITInvestmentUII": "015-000000026"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q1-04",
+            "describedBy": "https://fiscaldata.treasury.gov/datasets/treasury-reporting-rates-exchange/",
+            "description": "The Treasury Reporting Rates of Exchange dataset provides the U.S. government's authoritative exchange rates to ensure consistency for foreign currency units and U.S. dollar equivalents across all reporting done by agencies of the government. This report covers any foreign currencies in which the U.S. government has an interest, including: receipts and disbursements, accrued revenues and expenditures, authorizations, obligations, receivables and payables, refunds, and similar reverse transaction items. The Secretary of the Treasury has the sole authority to establish the exchange rates for all foreign currencies or credits reported by government agencies under federal law.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/treasury-reporting-rates-exchange/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/treasury-reporting-rates-exchange/",
                     "describedByType": "text/html",
                     "downloadURL": "https://fiscaldata.treasury.gov/datasets/treasury-reporting-rates-exchange/",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/treasury-reporting-rates-exchange/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/treasury-reporting-rates-exchange/",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.transparency.treasury.gov/services/api/fiscal_service/v1/accounting/od/rates_of_exchange",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 }
             ],
-            "accrualPeriodicity": "R/P3M",
-            "title": "Treasury Reporting Rates of Exchange",
-            "description": "The Treasury Reporting Rates of Exchange dataset provides the U.S. government's authoritative exchange rates to ensure consistency for foreign currency units and U.S. dollar equivalents across all reporting done by agencies of the government. This report covers any foreign currencies in which the U.S. government has an interest, including: receipts and disbursements, accrued revenues and expenditures, authorizations, obligations, receivables and payables, refunds, and similar reverse transaction items. The Secretary of the Treasury has the sole authority to establish the exchange rates for all foreign currencies or credits reported by government agencies under federal law.",
+            "identifier": "015-BFS-2014Q1-04",
             "keyword": [
                 "exchange rates / foreign currency / Currency / Treasury / US Dollar / Foreign Currency / foreign exchange"
             ],
+            "landingPage": "https://fiscaldata.treasury.gov/datasets/treasury-reporting-rates-exchange/",
             "modified": "2020-07-15",
+            "primaryITInvestmentUII": "015-000000032",
+            "programCode": [
+                "015:031"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Treasury Reporting Rates of Exchange"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:031"
-            ],
-            "describedBy": "https://fiscaldata.treasury.gov/datasets/treasury-reporting-rates-exchange/",
-            "landingPage": "https://fiscaldata.treasury.gov/datasets/treasury-reporting-rates-exchange/",
-            "primaryITInvestmentUII": "015-000000032"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q1-17",
+            "describedBy": "http://www.treasurydirect.gov/instit/annceresult/press/press.htm",
+            "description": "Results of recent auctions of Treasury securities, including offering amount, issue date, amount awarded, discount rate or interest rate",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://transparency.treasury.gov/dataset/treasury-securities-auction-results",
                     "describedBy": "http://www.treasurydirect.gov/instit/annceresult/press/press.htm",
                     "describedByType": "text/html",
                     "downloadURL": "http://www.treasurydirect.gov/instit/annceresult/press/press.htm",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Treasury Securities Auction Results",
-            "description": "Results of recent auctions of Treasury securities, including offering amount, issue date, amount awarded, discount rate or interest rate",
+            "identifier": "015-BFS-2014Q1-17",
+            "issued": "2013-10-31T00:00:00",
             "keyword": [
                 "Treasury Securities Auction Results"
             ],
+            "landingPage": "https://transparency.treasury.gov/dataset/treasury-securities-auction-results",
             "modified": "2016-07-28",
+            "primaryITInvestmentUII": "015-000000032",
+            "programCode": [
+                "015:035"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Treasury Securities Auction Results"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:035"
-            ],
-            "describedBy": "http://www.treasurydirect.gov/instit/annceresult/press/press.htm",
-            "landingPage": "https://transparency.treasury.gov/dataset/treasury-securities-auction-results",
-            "primaryITInvestmentUII": "015-000000032",
-            "issued": "2013-10-31T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q3-090",
+            "describedBy": "https://www.treasurydirect.gov/govt/rates/tcir/tcir_index_opdirannual.htm",
+            "description": "In February of 1997, the Fiscal Assistant Secretary of the U.S. Department of the Treasury delegated to the Bureau of the Public Debt the responsibility of providing interest rate certification to various agencies.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.transparency.treasury.gov/dataset/treasurys-certified-interest-rates-annual-interest-rate-certification",
                     "describedBy": "https://www.treasurydirect.gov/govt/rates/tcir/tcir_index_opdirannual.htm",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.treasurydirect.gov/govt/rates/tcir/tcir_index_opdirannual.htm",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "title": "Treasury's Certified Interest Rates Annual (Annual Interest Rate Certification)",
-            "description": "In February of 1997, the Fiscal Assistant Secretary of the U.S. Department of the Treasury delegated to the Bureau of the Public Debt the responsibility of providing interest rate certification to various agencies.",
+            "identifier": "015-BFS-2014Q3-090",
+            "issued": "2014-05-12T00:00:00",
             "keyword": [
                 "Treasury certified interest rates annual"
             ],
+            "landingPage": "https://www.transparency.treasury.gov/dataset/treasurys-certified-interest-rates-annual-interest-rate-certification",
             "modified": "2016-07-28",
+            "primaryITInvestmentUII": "015-000000060",
+            "programCode": [
+                "015:034"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Treasury's Certified Interest Rates Annual (Annual Interest Rate Certification)"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:034"
-            ],
-            "describedBy": "https://www.treasurydirect.gov/govt/rates/tcir/tcir_index_opdirannual.htm",
-            "landingPage": "https://www.transparency.treasury.gov/dataset/treasurys-certified-interest-rates-annual-interest-rate-certification",
-            "primaryITInvestmentUII": "015-000000060",
-            "issued": "2014-05-12T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q3-087",
+            "describedBy": "https://www.treasurydirect.gov/govt/rates/tcir/tcir_index_opdirmnt.htm",
+            "description": "In February of 1997, the Fiscal Assistant Secretary of the U.S. Department of the Treasury delegated to the Bureau of the Public Debt the responsibility of providing interest rate certification to various agencies. The U.S. Department of Treasury certifies these rates.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.transparency.treasury.gov/dataset/treasurys-certified-interest-rates-monthly-interest-rate-certification",
                     "describedBy": "https://www.treasurydirect.gov/govt/rates/tcir/tcir_index_opdirmnt.htm",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.treasurydirect.gov/govt/rates/tcir/tcir_index_opdirmnt.htm",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "Treasury's Certified Interest Rates Monthly (Monthly Interest Rate Certification)",
-            "description": "In February of 1997, the Fiscal Assistant Secretary of the U.S. Department of the Treasury delegated to the Bureau of the Public Debt the responsibility of providing interest rate certification to various agencies. The U.S. Department of Treasury certifies these rates.",
+            "identifier": "015-BFS-2014Q3-087",
+            "issued": "2014-05-12T00:00:00",
             "keyword": [
                 "Treasury certified interest rates monthly"
             ],
+            "landingPage": "https://www.transparency.treasury.gov/dataset/treasurys-certified-interest-rates-monthly-interest-rate-certification",
             "modified": "2016-07-28",
+            "primaryITInvestmentUII": "015-000000060",
+            "programCode": [
+                "015:034"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Treasury's Certified Interest Rates Monthly (Monthly Interest Rate Certification)"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:034"
-            ],
-            "describedBy": "https://www.treasurydirect.gov/govt/rates/tcir/tcir_index_opdirmnt.htm",
-            "landingPage": "https://www.transparency.treasury.gov/dataset/treasurys-certified-interest-rates-monthly-interest-rate-certification",
-            "primaryITInvestmentUII": "015-000000060",
-            "issued": "2014-05-12T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q3-088",
+            "describedBy": "https://www.treasurydirect.gov/govt/rates/tcir/tcir_index_opdirqtr.htm",
+            "description": "In February of 1997, the Fiscal Assistant Secretary of the U.S. Department of the Treasury delegated to the Bureau of the Public Debt the responsibility of providing interest rate certification to various agencies.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.transparency.treasury.gov/dataset/treasurys-certified-interest-rates-quarter-interest-rate-certification",
                     "describedBy": "https://www.treasurydirect.gov/govt/rates/tcir/tcir_index_opdirqtr.htm",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.treasurydirect.gov/govt/rates/tcir/tcir_index_opdirqtr.htm",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P3M",
-            "title": "Treasury's Certified Interest Rates Quarter (Quarterly Interest Rate Certification)",
-            "description": "In February of 1997, the Fiscal Assistant Secretary of the U.S. Department of the Treasury delegated to the Bureau of the Public Debt the responsibility of providing interest rate certification to various agencies.",
+            "identifier": "015-BFS-2014Q3-088",
+            "issued": "2014-05-12T00:00:00",
             "keyword": [
                 "Treasury certified interest rates quarterly"
             ],
+            "landingPage": "https://www.transparency.treasury.gov/dataset/treasurys-certified-interest-rates-quarter-interest-rate-certification",
             "modified": "2016-07-28",
+            "primaryITInvestmentUII": "015-000000060",
+            "programCode": [
+                "015:034"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Treasury's Certified Interest Rates Quarter (Quarterly Interest Rate Certification)"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P6M",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:034"
-            ],
-            "describedBy": "https://www.treasurydirect.gov/govt/rates/tcir/tcir_index_opdirqtr.htm",
-            "landingPage": "https://www.transparency.treasury.gov/dataset/treasurys-certified-interest-rates-quarter-interest-rate-certification",
-            "primaryITInvestmentUII": "015-000000060",
-            "issued": "2014-05-12T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q3-089",
+            "describedBy": "https://www.treasurydirect.gov/govt/rates/tcir/tcir_index_opdirsemi.htm",
+            "description": "In February of 1997, the Fiscal Assistant Secretary of the U.S. Department of the Treasury delegated to the Bureau of the Public Debt the responsibility of providing interest rate certification to various agencies.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.transparency.treasury.gov/dataset/treasurys-certified-interest-rates-semi-annual-interest-rate-certification",
                     "describedBy": "https://www.treasurydirect.gov/govt/rates/tcir/tcir_index_opdirsemi.htm",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.treasurydirect.gov/govt/rates/tcir/tcir_index_opdirsemi.htm",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P6M",
-            "title": "Treasury's Certified Interest Rates Semi-Annual (Semi-Annual Interest Rate Certification)",
-            "description": "In February of 1997, the Fiscal Assistant Secretary of the U.S. Department of the Treasury delegated to the Bureau of the Public Debt the responsibility of providing interest rate certification to various agencies.",
+            "identifier": "015-BFS-2014Q3-089",
+            "issued": "2014-05-12T00:00:00",
             "keyword": [
                 "Treasury certified interest rates semi-annual"
             ],
+            "landingPage": "https://www.transparency.treasury.gov/dataset/treasurys-certified-interest-rates-semi-annual-interest-rate-certification",
             "modified": "2016-07-28",
+            "primaryITInvestmentUII": "015-000000060",
+            "programCode": [
+                "015:034"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Treasury's Certified Interest Rates Semi-Annual (Semi-Annual Interest Rate Certification)"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:034"
-            ],
-            "describedBy": "https://www.treasurydirect.gov/govt/rates/tcir/tcir_index_opdirsemi.htm",
-            "landingPage": "https://www.transparency.treasury.gov/dataset/treasurys-certified-interest-rates-semi-annual-interest-rate-certification",
-            "primaryITInvestmentUII": "015-000000060",
-            "issued": "2014-05-12T00:00:00"
-        },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2017Q2-003",
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            },
+            "describedBy": "https://transparency.treasury.gov/dataset/treasury-report-on-receivables",
+            "description": "Treasury Report on Receivables and Debt Collection Activities (TROR) is the federal government\u2019s primary means for collecting data on the status of non-tax receivables (delinquent and non-delinquent debt) owed to the United States.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://transparency.treasury.gov/dataset/treasury-report-on-receivables",
                     "describedBy": "https://transparency.treasury.gov/dataset/treasury-report-on-receivables",
                     "describedByType": "text/html",
                     "downloadURL": "https://transparency.treasury.gov/dataset/treasury-report-on-receivables",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1D",
-            "title": "TROR and Debt Collection Activities",
-            "description": "Treasury Report on Receivables and Debt Collection Activities (TROR) is the federal government\u2019s primary means for collecting data on the status of non-tax receivables (delinquent and non-delinquent debt) owed to the United States.",
+            "identifier": "015-BFS-2017Q2-003",
+            "issued": "2016-10-24T00:00:00",
             "keyword": [
                 "fiscal service / treasury / federal / government / debt / collections"
             ],
+            "landingPage": "https://transparency.treasury.gov/dataset/treasury-report-on-receivables",
             "modified": "2017-02-01",
+            "primaryITInvestmentUII": "015-000000026",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "TROR and Debt Collection Activities"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "describedBy": "https://transparency.treasury.gov/dataset/treasury-report-on-receivables",
-            "landingPage": "https://transparency.treasury.gov/dataset/treasury-report-on-receivables",
-            "primaryITInvestmentUII": "015-000000026",
-            "issued": "2016-10-24T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q1-06",
+            "describedBy": "http://www.treasurydirect.gov/govt/reports/tfmp/tfmp.htm",
+            "description": "Monthly reports for each trust fund managed by the Bureau of the Fiscal Service",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://transparency.treasury.gov/dataset/trust-fund-financial-reports",
                     "describedBy": "http://www.treasurydirect.gov/govt/reports/tfmp/tfmp.htm",
                     "describedByType": "text/html",
                     "downloadURL": "http://www.treasurydirect.gov/govt/reports/tfmp/tfmp.htm",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Trust Fund Financial Reports",
-            "description": "Monthly reports for each trust fund managed by the Bureau of the Fiscal Service",
+            "identifier": "015-BFS-2014Q1-06",
+            "issued": "2013-10-31T00:00:00",
             "keyword": [
                 "Federal Government Investment Trust Funds"
             ],
+            "landingPage": "https://transparency.treasury.gov/dataset/trust-fund-financial-reports",
             "modified": "2016-07-28",
+            "primaryITInvestmentUII": "015-000000032",
+            "programCode": [
+                "015:034"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Trust Fund Financial Reports"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:034"
-            ],
-            "describedBy": "http://www.treasurydirect.gov/govt/reports/tfmp/tfmp.htm",
-            "landingPage": "https://transparency.treasury.gov/dataset/trust-fund-financial-reports",
-            "primaryITInvestmentUII": "015-000000032",
-            "issued": "2013-10-31T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q3-074",
+            "describedBy": "https://fiscaldata.treasury.gov/datasets/savings-bonds-issues-redemptions-maturities-by-series/",
+            "description": "The U.S. Treasury Savings Bonds: Issues, Redemptions, and Maturities by Series dataset provides the number of savings bonds that are issued, redeemed, and outstanding each month. The data is broken down by each series of savings bond (for example, Series E, Series EE, Series I, etc.) as well as whether the bonds are matured or unmatured. For each series, the difference between the number of savings bonds redeemed and issued is the number of outstanding savings bonds. This dataset does not contain information on the values or yields of the savings bonds.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/savings-bonds-issues-redemptions-maturities-by-series/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/savings-bonds-issues-redemptions-maturities-by-series/",
                     "describedByType": "text/html",
                     "downloadURL": "https://fiscaldata.treasury.gov/datasets/savings-bonds-issues-redemptions-maturities-by-series/",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/savings-bonds-issues-redemptions-maturities-by-series/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/savings-bonds-issues-redemptions-maturities-by-series/",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.transparency.treasury.gov/services/api/fiscal_service/v1/accounting/od/savings_bonds_report",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/savings-bonds-issues-redemptions-maturities-by-series/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/savings-bonds-issues-redemptions-maturities-by-series/",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.transparency.treasury.gov/services/api/fiscal_service/v1/accounting/od/savings_bonds_mud",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/savings-bonds-issues-redemptions-maturities-by-series/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/savings-bonds-issues-redemptions-maturities-by-series/",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.transparency.treasury.gov/services/api/fiscal_service/v1/accounting/od/savings_bonds_pcs",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "U.S. Treasury Savings Bonds: Issues, Redemptions, and Maturities by Series",
-            "description": "The U.S. Treasury Savings Bonds: Issues, Redemptions, and Maturities by Series dataset provides the number of savings bonds that are issued, redeemed, and outstanding each month. The data is broken down by each series of savings bond (for example, Series E, Series EE, Series I, etc.) as well as whether the bonds are matured or unmatured. For each series, the difference between the number of savings bonds redeemed and issued is the number of outstanding savings bonds. This dataset does not contain information on the values or yields of the savings bonds.",
+            "identifier": "015-BFS-2014Q3-074",
             "keyword": [
                 "savings bonds / issues / redemptions / maturities / Treasury bonds / series EE / matured bonds /  issued savings bonds / redeemed savings bonds / series E / series I / series HH"
             ],
+            "landingPage": "https://fiscaldata.treasury.gov/datasets/savings-bonds-issues-redemptions-maturities-by-series/",
             "modified": "2020-07-16",
+            "primaryITInvestmentUII": "015-000000062",
+            "programCode": [
+                "015:033"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "U.S. Treasury Savings Bonds: Issues, Redemptions, and Maturities by Series"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:033"
-            ],
-            "describedBy": "https://fiscaldata.treasury.gov/datasets/savings-bonds-issues-redemptions-maturities-by-series/",
-            "landingPage": "https://fiscaldata.treasury.gov/datasets/savings-bonds-issues-redemptions-maturities-by-series/",
-            "primaryITInvestmentUII": "015-000000062"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q1-09",
+            "describedBy": "https://fiscaldata.treasury.gov/datasets/status-report-government-gold-reserve/",
+            "description": "The U.S. Treasury-Owned Gold dataset provides the amount of gold that is available across various U.S. Treasury-maintained locations. The data shows whether the gold is held in deep storage or working stock, that is, available to the U.S. Mint as raw material for the creation of congressionally authorized coins. The dataset includes the weight of gold in troy ounces (a measurement unit still used today for precious metals and gunpowder) and the book value in dollars. The book value is not the market value, but instead represents the total number of troy ounces multiplied by a value established by law ($42.222), set in 1973.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/status-report-government-gold-reserve/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/status-report-government-gold-reserve/",
                     "describedByType": "text/html",
                     "downloadURL": "https://fiscaldata.treasury.gov/datasets/status-report-government-gold-reserve/",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://fiscaldata.treasury.gov/datasets/status-report-government-gold-reserve/",
                     "describedBy": "https://fiscaldata.treasury.gov/datasets/status-report-government-gold-reserve/",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.transparency.treasury.gov/services/api/fiscal_service/v2/accounting/od/gold_reserve",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "U.S. Treasury-Owned Gold",
-            "description": "The U.S. Treasury-Owned Gold dataset provides the amount of gold that is available across various U.S. Treasury-maintained locations. The data shows whether the gold is held in deep storage or working stock, that is, available to the U.S. Mint as raw material for the creation of congressionally authorized coins. The dataset includes the weight of gold in troy ounces (a measurement unit still used today for precious metals and gunpowder) and the book value in dollars. The book value is not the market value, but instead represents the total number of troy ounces multiplied by a value established by law ($42.222), set in 1973.",
+            "identifier": "015-BFS-2014Q1-09",
             "keyword": [
                 "Gold / fort knox / US mint gold / gold reserve / treasury gold / troy ounce / value of gold reserves / gold bullion / gold book value / NY Vault"
             ],
+            "landingPage": "https://fiscaldata.treasury.gov/datasets/status-report-government-gold-reserve/",
             "modified": "2020-07-06",
+            "primaryITInvestmentUII": "015-000000032",
+            "programCode": [
+                "015:031"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "U.S. Treasury-Owned Gold"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:031"
-            ],
-            "describedBy": "https://fiscaldata.treasury.gov/datasets/status-report-government-gold-reserve/",
-            "landingPage": "https://fiscaldata.treasury.gov/datasets/status-report-government-gold-reserve/",
-            "primaryITInvestmentUII": "015-000000032"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q3-093",
+            "describedBy": "https://www.treasurydirect.gov/govt/rates/rates_tfr.htm",
+            "description": "Quarterly yields from 1999 to the present",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://transparency.treasury.gov/dataset/unemployment-trust-funds-quarterly-yields",
                     "describedBy": "https://www.treasurydirect.gov/govt/rates/rates_tfr.htm",
                     "describedByType": "text/html",
                     "downloadURL": "https://api.transparency.treasury.gov/services/api/fiscal_service/v1/accounting/od/utf_qtr_yields",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 }
             ],
-            "accrualPeriodicity": "R/P3M",
-            "title": "Unemployment Trust Funds Quarterly Yields",
-            "description": "Quarterly yields from 1999 to the present",
+            "identifier": "015-BFS-2014Q3-093",
+            "issued": "2016-12-31T00:00:00",
             "keyword": [
                 "unemployment trust fund quarterly yields"
             ],
+            "landingPage": "https://transparency.treasury.gov/dataset/unemployment-trust-funds-quarterly-yields",
             "modified": "2017-03-31",
+            "primaryITInvestmentUII": "015-000000060",
+            "programCode": [
+                "015:034"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Unemployment Trust Funds Quarterly Yields"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:034"
-            ],
-            "describedBy": "https://www.treasurydirect.gov/govt/rates/rates_tfr.htm",
-            "landingPage": "https://transparency.treasury.gov/dataset/unemployment-trust-funds-quarterly-yields",
-            "primaryITInvestmentUII": "015-000000060",
-            "issued": "2016-12-31T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q4-003",
+            "describedBy": "http://www.treasurydirect.gov/instit/instit.htm?upcoming",
+            "description": "Upcoming auction data displays announcement data for U.S. Treasury marketable securities including term, type, CMB/Reopening, CUSIP, offering amount, auction date, and  issue date.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://transparency.treasury.gov/dataset/upcoming-auctions",
                     "describedBy": "http://www.treasurydirect.gov/instit/instit.htm?upcoming",
                     "describedByType": "text/html",
                     "downloadURL": "http://www.treasurydirect.gov/TA_WS/securities/announced?format=json",
-                    "mediaType": "application/vnd.api+json",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.api+json"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Upcoming Auctions",
-            "description": "Upcoming auction data displays announcement data for U.S. Treasury marketable securities including term, type, CMB/Reopening, CUSIP, offering amount, auction date, and  issue date.",
+            "identifier": "015-BFS-2014Q4-003",
+            "issued": "2014-08-22T00:00:00",
             "keyword": [
                 "upcoming auction / auction announcement / CUSIP / auction"
             ],
+            "landingPage": "https://transparency.treasury.gov/dataset/upcoming-auctions",
             "modified": "2015-05-04",
+            "primaryITInvestmentUII": "015-000000061",
+            "programCode": [
+                "015:035"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "Upcoming Auctions"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:035"
-            ],
-            "describedBy": "http://www.treasurydirect.gov/instit/instit.htm?upcoming",
-            "landingPage": "https://transparency.treasury.gov/dataset/upcoming-auctions",
-            "primaryITInvestmentUII": "015-000000061",
-            "issued": "2014-08-22T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2015Q3-003",
+            "describedBy": "https://www.usaspending.gov/#/download_center/data_dictionary",
+            "description": "The source for raw agency-submitted financial assistance files and quarterly DATA Act files (which include account, contract, financial assistance, and subaward data). This agency data is submitted directly by agencies or pulled in from external federal systems. All data is presented to agency Senior Accountable Officials for review and certification via the DATA Act Broker. These submissions form the primary basis for the data displayed on the USAspending.gov website.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/#/",
                     "describedBy": "https://www.usaspending.gov/#/download_center/data_dictionary",
                     "describedByType": "text/html",
                     "downloadURL": "https://files.usaspending.gov/agency_submissions/",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "USAspending.gov Broker Submission Data (Raw Files)",
-            "description": "The source for raw agency-submitted financial assistance files and quarterly DATA Act files (which include account, contract, financial assistance, and subaward data). This agency data is submitted directly by agencies or pulled in from external federal systems. All data is presented to agency Senior Accountable Officials for review and certification via the DATA Act Broker. These submissions form the primary basis for the data displayed on the USAspending.gov website.",
+            "identifier": "015-BFS-2015Q3-003",
+            "issued": "2015-01-15T00:00:00",
             "keyword": [
                 "Federal Contracts/Contracts/Awards/Grants/Loans/Loan Guarantees/FFATA/Subawards/Subcontracts/Subcontracts/Insurance/Assistance/Financial Assistance/Other Financial Assistance/Direct Payment/Purchase Cards/USAspendingPurchase/Travel/Fleet/Contractor/contracting agency Top/DATA Act/Data Transparency"
             ],
+            "landingPage": "https://www.usaspending.gov/#/",
             "modified": "2019-06-25",
+            "primaryITInvestmentUII": "015-999990047",
+            "programCode": [
+                "015:031"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "USAspending.gov Broker Submission Data (Raw Files)"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:031"
-            ],
-            "describedBy": "https://www.usaspending.gov/#/download_center/data_dictionary",
-            "landingPage": "https://www.usaspending.gov/#/",
-            "primaryITInvestmentUII": "015-999990047",
-            "issued": "2015-01-15T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2015Q3-002",
+            "describedBy": "https://fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
+            "description": "The official source of spending data for the U.S. Government. Data is sourced from the DATA Act Broker (which draws from a number of federal systems as well as data directly submitted by agencies) on a nightly basis and presented to the public for display and download. Significant effort has gone into 'unlocking' the data through intuitive displays, charts, and deep-dive analyses. The major data categories are account data, award data, and subaward data. Award data is linked to subaward data, and account data is linked to award data. In the case of award and subaward data, contextual information about location, recipients, place of performance, etc. are provided.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/#/",
                     "describedBy": "https://fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.usaspending.gov/#/download_center/award_data_archive",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/#/",
                     "describedBy": "https://fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.usaspending.gov/#/download_center/custom_award_data",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/#/",
                     "describedBy": "https://fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
                     "describedByType": "text/html",
                     "downloadURL": "https://api.usaspending.gov",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1D",
-            "title": "USAspending.gov Federal Award, Subaward, and Account Data",
-            "description": "The official source of spending data for the U.S. Government. Data is sourced from the DATA Act Broker (which draws from a number of federal systems as well as data directly submitted by agencies) on a nightly basis and presented to the public for display and download. Significant effort has gone into 'unlocking' the data through intuitive displays, charts, and deep-dive analyses. The major data categories are account data, award data, and subaward data. Award data is linked to subaward data, and account data is linked to award data. In the case of award and subaward data, contextual information about location, recipients, place of performance, etc. are provided.",
+            "identifier": "015-BFS-2015Q3-002",
+            "issued": "2015-01-15T00:00:00",
             "keyword": [
                 "Federal Contracts/Contracts/Awards/Grants/Loans/Loan Guarantees/FFATA/Subawards/Subcontracts/Subcontracts/Insurance/Assistance/Financial Assistance/Other Financial Assistance/Direct Payment/Purchase Cards/USAspendingPurchase/Travel/Fleet/Contractor/contracting agency Top/DATA Act/Data Transparency"
             ],
+            "landingPage": "https://www.usaspending.gov/#/",
             "modified": "2018-06-30",
+            "primaryITInvestmentUII": "015-999990047",
+            "programCode": [
+                "015:031"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "USAspending.gov Federal Award, Subaward, and Account Data"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "015:12"
             ],
-            "programCode": [
-                "015:031"
-            ],
-            "describedBy": "https://fiscal.treasury.gov/fsservices/gov/data-trans/dt-daims.htm",
-            "landingPage": "https://www.usaspending.gov/#/",
-            "primaryITInvestmentUII": "015-999990047",
-            "issued": "2015-01-15T00:00:00"
+            "contactPoint": {
+                "fn": "Lee Burke",
+                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-BFS-2014Q3-126",
+            "describedBy": "http://tfm.fiscal.treasury.gov/v1/supplements/ussgl/ussgl_part_1.html?id=3",
+            "description": "Annual report that includes chart of accounts, accounts and definitions, account transactions, account attributes for USSGL proprietary account and budgetary account reporting, crosswalks to standard external reports for fiscal year reporting, crosswalks for reclassified statements for fiscal year reporting, and GTAS validations and edits.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://transparency.treasury.gov/dataset/ussgl-tfm-part-1-fiscal-year-reporting",
                     "describedBy": "http://tfm.fiscal.treasury.gov/v1/supplements/ussgl/ussgl_part_1.html?id=3",
                     "describedByType": "text/html",
                     "downloadURL": "http://tfm.fiscal.treasury.gov/v1/supplements/ussgl/ussgl_part_1.html",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "title": "USSGL TFM Part 1 Fiscal Year Reporting",
-            "description": "Annual report that includes chart of accounts, accounts and definitions, account transactions, account attributes for USSGL proprietary account and budgetary account reporting, crosswalks to standard external reports for fiscal year reporting, crosswalks for reclassified statements for fiscal year reporting, and GTAS validations and edits.",
+            "identifier": "015-BFS-2014Q3-126",
+            "issued": "2014-05-12T00:00:00",
             "keyword": [
                 "USSGL / Account Transactions"
             ],
+            "landingPage": "https://transparency.treasury.gov/dataset/ussgl-tfm-part-1-fiscal-year-reporting",
             "modified": "2016-07-28",
+            "primaryITInvestmentUII": "015-000000032",
+            "programCode": [
+                "015:031"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Bureau of the Fiscal Service",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "Fiscal Service",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "Fiscal Service"
-                },
-                "name": "Bureau of the Fiscal Service"
-            },
-            "contactPoint": {
-                "fn": "Lee Burke",
-                "hasEmail": "mailto:lee.burke@fiscal.treasury.gov"
+            "title": "USSGL TFM Part 1 Fiscal Year Reporting"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
-                "015:12"
-            ],
-            "programCode": [
-                "015:031"
+                "015:45"
             ],
-            "describedBy": "http://tfm.fiscal.treasury.gov/v1/supplements/ussgl/ussgl_part_1.html?id=3",
-            "landingPage": "https://transparency.treasury.gov/dataset/ussgl-tfm-part-1-fiscal-year-reporting",
-            "primaryITInvestmentUII": "015-000000032",
-            "issued": "2014-05-12T00:00:00"
+            "contactPoint": {
+                "fn": "Kevin Pierce",
+                "hasEmail": "mailto:sis@irs.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-IRS-SOI-COUNTYINC",
+            "describedBy": "https://www.irs.gov/statistics/soi-tax-stats-county-data",
+            "description": "This annual study provides county income and tax data (and State totals) that include the number of returns, which approximates the number of households; number of personal exemptions, which approximates the population; adjusted gross income; wages and salaries; dividends before exclusion; and interest received. Data are based on the addresses reported on U.S. Individual Income Tax Returns (Forms 1040) filed with the IRS. SOI collects these data as part of its annual study on Individual Tax Return Statistics by Geographic Areas, County Data.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.irs.gov/statistics/soi-tax-stats-county-data",
                     "describedBy": "https://www.irs.gov/statistics/soi-tax-stats-county-data",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.irs.gov/statistics/soi-tax-stats-county-data",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Individuals, County Data",
-            "description": "This annual study provides county income and tax data (and State totals) that include the number of returns, which approximates the number of households; number of personal exemptions, which approximates the population; adjusted gross income; wages and salaries; dividends before exclusion; and interest received. Data are based on the addresses reported on U.S. Individual Income Tax Returns (Forms 1040) filed with the IRS. SOI collects these data as part of its annual study on Individual Tax Return Statistics by Geographic Areas, County Data.",
+            "identifier": "015-IRS-SOI-COUNTYINC",
             "keyword": [
                 "IRS",
                 "statistics of income",
@@ -8761,50 +8768,50 @@
                 "income data",
                 "income tax"
             ],
+            "landingPage": "https://www.irs.gov/statistics/soi-tax-stats-county-data",
             "modified": "2024-02-29",
+            "primaryITInvestmentUII": "015-000000021",
+            "programCode": [
+                "015:042"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Statistics of Income (SOI)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "IRS",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "IRS"
-                },
-                "name": "Statistics of Income (SOI)"
-            },
-            "contactPoint": {
-                "fn": "Kevin Pierce",
-                "hasEmail": "mailto:sis@irs.gov"
+            "title": "Individuals, County Data"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:45"
             ],
-            "programCode": [
-                "015:042"
-            ],
-            "describedBy": "https://www.irs.gov/statistics/soi-tax-stats-county-data",
-            "landingPage": "https://www.irs.gov/statistics/soi-tax-stats-county-data",
-            "primaryITInvestmentUII": "015-000000021"
+            "contactPoint": {
+                "fn": "Kevin Pierce",
+                "hasEmail": "mailto:sis@irs.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-IRS-SOI-MIGRATION",
+            "describedBy": "http://www.irs.gov/statistics/soi-tax-stats-migration-data",
+            "description": "This annual study provides migration pattern data for the United States by State or by county and are available for inflows (the number of new residents who moved to a State or county and where they migrated from) and outflows (the number of residents who left a State or county and where they moved to). The data include the number of returns filed, number of personal exemptions claimed, total adjusted gross income, and aggregate migration flows at the State level, by the size of adjusted gross income (AGI) and by age of the primary taxpayer. Data are collected and based on year-to-year address changes reported on U.S. Individual Income Tax Returns (Form 1040) filed with the IRS. SOI collects these data as part of its Individual Income Tax Return (Form 1040) Statistics program, Data by Geographic Areas, U.S. Population Migration Data.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.irs.gov/statistics/soi-tax-stats-migration-data",
                     "describedBy": "http://www.irs.gov/statistics/soi-tax-stats-migration-data",
                     "describedByType": "text/html",
                     "downloadURL": "http://www.irs.gov/statistics/soi-tax-stats-migration-data",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Individuals, State and County Migration data",
-            "description": "This annual study provides migration pattern data for the United States by State or by county and are available for inflows (the number of new residents who moved to a State or county and where they migrated from) and outflows (the number of residents who left a State or county and where they moved to). The data include the number of returns filed, number of personal exemptions claimed, total adjusted gross income, and aggregate migration flows at the State level, by the size of adjusted gross income (AGI) and by age of the primary taxpayer. Data are collected and based on year-to-year address changes reported on U.S. Individual Income Tax Returns (Form 1040) filed with the IRS. SOI collects these data as part of its Individual Income Tax Return (Form 1040) Statistics program, Data by Geographic Areas, U.S. Population Migration Data.",
+            "identifier": "015-IRS-SOI-MIGRATION",
             "keyword": [
                 "IRS",
                 "statistics of income",
@@ -8818,50 +8825,50 @@
                 "mover",
                 "population"
             ],
+            "landingPage": "http://www.irs.gov/statistics/soi-tax-stats-migration-data",
             "modified": "2024-06-27",
+            "primaryITInvestmentUII": "015-000000021",
+            "programCode": [
+                "015:042"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Statistics of Income (SOI)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "IRS",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "IRS"
-                },
-                "name": "Statistics of Income (SOI)"
-            },
-            "contactPoint": {
-                "fn": "Kevin Pierce",
-                "hasEmail": "mailto:sis@irs.gov"
+            "title": "Individuals, State and County Migration data"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:45"
             ],
-            "programCode": [
-                "015:042"
-            ],
-            "describedBy": "http://www.irs.gov/statistics/soi-tax-stats-migration-data",
-            "landingPage": "http://www.irs.gov/statistics/soi-tax-stats-migration-data",
-            "primaryITInvestmentUII": "015-000000021"
+            "contactPoint": {
+                "fn": "Cynthia Belmonte",
+                "hasEmail": "mailto:sis@irs.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-IRS-SOI-990PFFDE",
+            "describedBy": "https://www.irs.gov/statistics/soi-tax-stats-annual-extract-of-tax-exempt-organization-financial-data",
+            "description": "Annual extract of select Form 990PF financial data items captured on the IRS Master File produced solely for release to the general public.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.irs.gov/statistics/soi-tax-stats-annual-extract-of-tax-exempt-organization-financial-data",
                     "describedBy": "https://www.irs.gov/statistics/soi-tax-stats-annual-extract-of-tax-exempt-organization-financial-data",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.irs.gov/statistics/soi-tax-stats-annual-extract-of-tax-exempt-organization-financial-data",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Tax-Exempt Organizations (Private Foundations) Financial Data Extract",
-            "description": "Annual extract of select Form 990PF financial data items captured on the IRS Master File produced solely for release to the general public.",
+            "identifier": "015-IRS-SOI-990PFFDE",
             "keyword": [
                 "IRS",
                 "statistics of income",
@@ -8873,50 +8880,51 @@
                 "grant",
                 "form 990-pf"
             ],
+            "landingPage": "https://www.irs.gov/statistics/soi-tax-stats-annual-extract-of-tax-exempt-organization-financial-data",
             "modified": "2023-11-22",
+            "primaryITInvestmentUII": "015-000000021",
+            "programCode": [
+                "015:042"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Statistics of Income (SOI)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "IRS",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "IRS"
-                },
-                "name": "Statistics of Income (SOI)"
-            },
-            "contactPoint": {
-                "fn": "Cynthia Belmonte",
-                "hasEmail": "mailto:sis@irs.gov"
+            "title": "Tax-Exempt Organizations (Private Foundations) Financial Data Extract"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:45"
             ],
-            "programCode": [
-                "015:042"
-            ],
-            "describedBy": "https://www.irs.gov/statistics/soi-tax-stats-annual-extract-of-tax-exempt-organization-financial-data",
-            "landingPage": "https://www.irs.gov/statistics/soi-tax-stats-annual-extract-of-tax-exempt-organization-financial-data",
-            "primaryITInvestmentUII": "015-000000021"
+            "contactPoint": {
+                "fn": "Amber Thompson",
+                "hasEmail": "mailto:tege.eo.ceo@irs.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-IRS-TEGE-TEOS",
+            "describedBy": "https://www.irs.gov/charities-non-profits/tax-exempt-organization-search-teos-teos-improvements",
+            "description": "The IRS Tax Exempt Organization Search tool allows users to find information about an organization's tax-exempt status under the Internal Revenue Code and its tax filings. This includes checking eligibility for tax-deductible contributions (Pub. 78 Data), Form 990 Series Returns, Form 990-N (e-Postcard), Automatic Revocation of Exemption List, and copies of Determination Letters. You can use the online search tool or download data sets in bulk.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.irs.gov/charities-non-profits/tax-exempt-organization-search",
                     "describedBy": "https://www.irs.gov/charities-non-profits/tax-exempt-organization-search-teos-teos-improvements",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.irs.gov/charities-non-profits/tax-exempt-organization-search",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Tax Exempt Organization Search",
-            "description": "The IRS Tax Exempt Organization Search tool allows users to find information about an organization's tax-exempt status under the Internal Revenue Code and its tax filings. This includes checking eligibility for tax-deductible contributions (Pub. 78 Data), Form 990 Series Returns, Form 990-N (e-Postcard), Automatic Revocation of Exemption List, and copies of Determination Letters. You can use the online search tool or download data sets in bulk.",
+            "identifier": "015-IRS-TEGE-TEOS",
+            "issued": "2024-07-17T00:00:00",
             "keyword": [
                 "IRS",
                 "Tax-Exempt Organizations",
@@ -8929,51 +8937,50 @@
                 "Tax Exempt Organization Search",
                 "TEOS"
             ],
+            "landingPage": "https://www.irs.gov/charities-non-profits/tax-exempt-organization-search",
             "modified": "2024-07-17",
+            "primaryITInvestmentUII": "015-000000021",
+            "programCode": [
+                "015:042"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "IRS",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "IRS",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "IRS"
-                },
-                "name": "IRS"
-            },
-            "contactPoint": {
-                "fn": "Amber Thompson",
-                "hasEmail": "mailto:tege.eo.ceo@irs.gov"
+            "title": "Tax Exempt Organization Search"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:45"
             ],
-            "programCode": [
-                "015:042"
-            ],
-            "describedBy": "https://www.irs.gov/charities-non-profits/tax-exempt-organization-search-teos-teos-improvements",
-            "landingPage": "https://www.irs.gov/charities-non-profits/tax-exempt-organization-search",
-            "primaryITInvestmentUII": "015-000000021",
-            "issued": "2024-07-17T00:00:00"
+            "contactPoint": {
+                "fn": "Paul Arnsberger",
+                "hasEmail": "mailto:sis@irs.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-IRS-SOI-F990",
+            "describedBy": "https://www.irs.gov/statistics/soi-tax-stats-charities-and-other-tax-exempt-organizations-statistics",
+            "description": "This annual study provides balance sheet and income statement data for organizations classified as tax-exempt under subsections 501(c)(3)-(9) of the Internal Revenue Code.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.irs.gov/statistics/soi-tax-stats-charities-and-other-tax-exempt-organizations-statistics",
                     "describedBy": "https://www.irs.gov/statistics/soi-tax-stats-charities-and-other-tax-exempt-organizations-statistics",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.irs.gov/statistics/soi-tax-stats-charities-and-other-tax-exempt-organizations-statistics",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Tax-Exempt Organizations (Except Private Foundations)",
-            "description": "This annual study provides balance sheet and income statement data for organizations classified as tax-exempt under subsections 501(c)(3)-(9) of the Internal Revenue Code.",
+            "identifier": "015-IRS-SOI-F990",
             "keyword": [
                 "IRS",
                 "statistics of income",
@@ -8985,50 +8992,50 @@
                 "grant",
                 "form 990"
             ],
+            "landingPage": "https://www.irs.gov/statistics/soi-tax-stats-charities-and-other-tax-exempt-organizations-statistics",
             "modified": "2024-06-21",
+            "primaryITInvestmentUII": "015-000000021",
+            "programCode": [
+                "015:042"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Statistics of Income (SOI)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "IRS",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "IRS"
-                },
-                "name": "Statistics of Income (SOI)"
-            },
-            "contactPoint": {
-                "fn": "Paul Arnsberger",
-                "hasEmail": "mailto:sis@irs.gov"
+            "title": "Tax-Exempt Organizations (Except Private Foundations)"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:45"
             ],
-            "programCode": [
-                "015:042"
-            ],
-            "describedBy": "https://www.irs.gov/statistics/soi-tax-stats-charities-and-other-tax-exempt-organizations-statistics",
-            "landingPage": "https://www.irs.gov/statistics/soi-tax-stats-charities-and-other-tax-exempt-organizations-statistics",
-            "primaryITInvestmentUII": "015-000000021"
+            "contactPoint": {
+                "fn": "Paul Arnsberger",
+                "hasEmail": "mailto:sis@irs.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-IRS-SOI-F990FDE",
+            "describedBy": "https://www.irs.gov/statistics/soi-tax-stats-annual-extract-of-tax-exempt-organization-financial-data",
+            "description": "Annual extract of select Form 990 financial data items captured on the IRS Master File produced solely for release to the general public.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.irs.gov/statistics/soi-tax-stats-annual-extract-of-tax-exempt-organization-financial-data",
                     "describedBy": "https://www.irs.gov/statistics/soi-tax-stats-annual-extract-of-tax-exempt-organization-financial-data",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.irs.gov/statistics/soi-tax-stats-annual-extract-of-tax-exempt-organization-financial-data",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Tax-Exempt Organizations (Except Private Foundations) Financial Data Extract",
-            "description": "Annual extract of select Form 990 financial data items captured on the IRS Master File produced solely for release to the general public.",
+            "identifier": "015-IRS-SOI-F990FDE",
             "keyword": [
                 "IRS",
                 "statistics of income",
@@ -9040,50 +9047,50 @@
                 "grant",
                 "form 990"
             ],
+            "landingPage": "https://www.irs.gov/statistics/soi-tax-stats-annual-extract-of-tax-exempt-organization-financial-data",
             "modified": "2016-04-27",
+            "primaryITInvestmentUII": "015-000000021",
+            "programCode": [
+                "015:042"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Statistics of Income (SOI)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "IRS",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "IRS"
-                },
-                "name": "Statistics of Income (SOI)"
-            },
-            "contactPoint": {
-                "fn": "Paul Arnsberger",
-                "hasEmail": "mailto:sis@irs.gov"
+            "title": "Tax-Exempt Organizations (Except Private Foundations) Financial Data Extract"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:45"
             ],
-            "programCode": [
-                "015:042"
-            ],
-            "describedBy": "https://www.irs.gov/statistics/soi-tax-stats-annual-extract-of-tax-exempt-organization-financial-data",
-            "landingPage": "https://www.irs.gov/statistics/soi-tax-stats-annual-extract-of-tax-exempt-organization-financial-data",
-            "primaryITInvestmentUII": "015-000000021"
+            "contactPoint": {
+                "fn": "Cynthia Belmonte",
+                "hasEmail": "mailto:sis@irs.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-IRS-SOI-F990PF",
+            "describedBy": "https://www.irs.gov/statistics/soi-tax-stats-domestic-private-foundation-and-charitable-trust-statistics",
+            "description": "This annual study provides balance sheet and income statement data for domestic private foundations and charitable trusts filing a Form 990-PF, Return of Private Foundation.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.irs.gov/statistics/soi-tax-stats-domestic-private-foundation-and-charitable-trust-statistics",
                     "describedBy": "https://www.irs.gov/statistics/soi-tax-stats-domestic-private-foundation-and-charitable-trust-statistics",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.irs.gov/statistics/soi-tax-stats-domestic-private-foundation-and-charitable-trust-statistics",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Tax-Exempt Organizations (Private Foundations)",
-            "description": "This annual study provides balance sheet and income statement data for domestic private foundations and charitable trusts filing a Form 990-PF, Return of Private Foundation.",
+            "identifier": "015-IRS-SOI-F990PF",
             "keyword": [
                 "IRS",
                 "statistics of income",
@@ -9095,50 +9102,50 @@
                 "grant",
                 "form 990-pf"
             ],
+            "landingPage": "https://www.irs.gov/statistics/soi-tax-stats-domestic-private-foundation-and-charitable-trust-statistics",
             "modified": "2024-07-05",
+            "primaryITInvestmentUII": "015-000000021",
+            "programCode": [
+                "015:042"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Statistics of Income (SOI)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "IRS",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "IRS"
-                },
-                "name": "Statistics of Income (SOI)"
-            },
-            "contactPoint": {
-                "fn": "Cynthia Belmonte",
-                "hasEmail": "mailto:sis@irs.gov"
+            "title": "Tax-Exempt Organizations (Private Foundations)"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:45"
             ],
-            "programCode": [
-                "015:042"
-            ],
-            "describedBy": "https://www.irs.gov/statistics/soi-tax-stats-domestic-private-foundation-and-charitable-trust-statistics",
-            "landingPage": "https://www.irs.gov/statistics/soi-tax-stats-domestic-private-foundation-and-charitable-trust-statistics",
-            "primaryITInvestmentUII": "015-000000021"
+            "contactPoint": {
+                "fn": "Kevin Pierce",
+                "hasEmail": "mailto:sis@irs.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-IRS-SOI-ZIPCODE",
+            "describedBy": "http://www.irs.gov/statistics/soi-tax-stats-individual-income-tax-statistics-zip-code-data-soi",
+            "description": "This annual study provides selected income and tax items classified by State, ZIP Code, and the size of adjusted gross income. These data include the number of returns, which approximates the number of households; the number of personal exemptions, which approximates the population; adjusted gross income; wages and salaries; dividends before exclusion; and interest received. Data are based who reported on U.S. Individual Income Tax Returns (Forms 1040) filed with the IRS. SOI collects these data as part of its Individual Income Tax Return (Form 1040) Statistics program, Data by Geographic Areas, ZIP Code Data.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.irs.gov/statistics/soi-tax-stats-individual-income-tax-statistics-zip-code-data-soi",
                     "describedBy": "http://www.irs.gov/statistics/soi-tax-stats-individual-income-tax-statistics-zip-code-data-soi",
                     "describedByType": "text/html",
                     "downloadURL": "http://www.irs.gov/statistics/soi-tax-stats-individual-income-tax-statistics-zip-code-data-soi",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Individuals, ZIP Code Data",
-            "description": "This annual study provides selected income and tax items classified by State, ZIP Code, and the size of adjusted gross income. These data include the number of returns, which approximates the number of households; the number of personal exemptions, which approximates the population; adjusted gross income; wages and salaries; dividends before exclusion; and interest received. Data are based who reported on U.S. Individual Income Tax Returns (Forms 1040) filed with the IRS. SOI collects these data as part of its Individual Income Tax Return (Form 1040) Statistics program, Data by Geographic Areas, ZIP Code Data.",
+            "identifier": "015-IRS-SOI-ZIPCODE",
             "keyword": [
                 "IRS",
                 "statistics of income",
@@ -9148,47 +9155,46 @@
                 "income tax",
                 "form 1040"
             ],
+            "landingPage": "http://www.irs.gov/statistics/soi-tax-stats-individual-income-tax-statistics-zip-code-data-soi",
             "modified": "2024-06-07",
+            "primaryITInvestmentUII": "015-000000021",
+            "programCode": [
+                "015:042"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Statistics of Income (SOI)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "IRS",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "IRS"
-                },
-                "name": "Statistics of Income (SOI)"
-            },
-            "contactPoint": {
-                "fn": "Kevin Pierce",
-                "hasEmail": "mailto:sis@irs.gov"
+            "title": "Individuals, ZIP Code Data"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
-                "015:45"
-            ],
-            "programCode": [
-                "015:042"
+                "015:05"
             ],
-            "describedBy": "http://www.irs.gov/statistics/soi-tax-stats-individual-income-tax-statistics-zip-code-data-soi",
-            "landingPage": "http://www.irs.gov/statistics/soi-tax-stats-individual-income-tax-statistics-zip-code-data-soi",
-            "primaryITInvestmentUII": "015-000000021"
+            "contactPoint": {
+                "fn": "Office of Information Technology, Web Team",
+                "hasEmail": "mailto:ITWebTeam@tigta.treas.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TIGTA-0010",
+            "description": "TIGTA Monthly Reports on Received ARRA funds",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/tigta/recovery_tigtareports.shtml",
                     "downloadURL": "http://www.treasury.gov/tigta/recovery_tigtareports.shtml",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "title": "ARRA Funds Monthly Report",
-            "description": "TIGTA Monthly Reports on Received ARRA funds",
+            "identifier": "015-TIGTA-0010",
             "keyword": [
                 "monthly",
                 "report",
@@ -9203,46 +9209,46 @@
                 "inspector general",
                 "ig"
             ],
+            "landingPage": "http://www.treasury.gov/tigta/recovery_tigtareports.shtml",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2023-12-08",
+            "programCode": [
+                "015:015"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Office of Audit",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TIGTA",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TIGTA"
-                },
-                "name": "Office of Audit"
-            },
-            "contactPoint": {
-                "fn": "Office of Information Technology, Web Team",
-                "hasEmail": "mailto:ITWebTeam@tigta.treas.gov"
+            "title": "ARRA Funds Monthly Report"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "015:05"
             ],
-            "programCode": [
-                "015:015"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/tigta/recovery_tigtareports.shtml"
+            "contactPoint": {
+                "fn": "Office of Information Technology, Web Team",
+                "hasEmail": "mailto:ITWebTeam@tigta.treas.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TIGTA-0007",
+            "description": "TIGTA's Annual Audit Plans contain an overview of TIGTA's audit resources and brief descriptions of the audits TIGTA plans to start during the current fiscal year.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/tigta/oa_auditplans.shtml",
                     "downloadURL": "http://www.treasury.gov/tigta/oa_auditplans.shtml",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "title": "Audit Plans",
-            "description": "TIGTA's Annual Audit Plans contain an overview of TIGTA's audit resources and brief descriptions of the audits TIGTA plans to start during the current fiscal year.",
+            "identifier": "015-TIGTA-0007",
             "keyword": [
                 "audit",
                 "plan",
@@ -9251,46 +9257,46 @@
                 "inspector general",
                 "ig"
             ],
+            "landingPage": "http://www.treasury.gov/tigta/oa_auditplans.shtml",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2023-12-08",
+            "programCode": [
+                "015:015"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Office of Audit",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TIGTA",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TIGTA"
-                },
-                "name": "Office of Audit"
-            },
-            "contactPoint": {
-                "fn": "Office of Information Technology, Web Team",
-                "hasEmail": "mailto:ITWebTeam@tigta.treas.gov"
+            "title": "Audit Plans"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "015:05"
             ],
-            "programCode": [
-                "015:015"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/tigta/oa_auditplans.shtml"
+            "contactPoint": {
+                "fn": "Office of Information Technology, Web Team",
+                "hasEmail": "mailto:ITWebTeam@tigta.treas.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TIGTA-0001",
+            "description": "TIGTA's Audit Reports review and recommend improvements on all aspects of the IRS's administration of the tax system.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/tigta/oa_auditreports.shtml",
                     "downloadURL": "http://www.treasury.gov/tigta/oa_auditreports.shtml",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "title": "Audit Reports",
-            "description": "TIGTA's Audit Reports review and recommend improvements on all aspects of the IRS's administration of the tax system.",
+            "identifier": "015-TIGTA-0001",
             "keyword": [
                 "audit",
                 "tigta",
@@ -9301,47 +9307,47 @@
                 "inspector general",
                 "ig"
             ],
+            "landingPage": "http://www.treasury.gov/tigta/oa_auditreports.shtml",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2023-12-08",
+            "programCode": [
+                "015:015"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Office of Audit",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TIGTA",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TIGTA"
-                },
-                "name": "Office of Audit"
-            },
-            "contactPoint": {
-                "fn": "Office of Information Technology, Web Team",
-                "hasEmail": "mailto:ITWebTeam@tigta.treas.gov"
+            "title": "Audit Reports"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:05"
             ],
-            "programCode": [
-                "015:015"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/tigta/oa_auditreports.shtml"
+            "contactPoint": {
+                "fn": "Office of Information Technology, Web Team",
+                "hasEmail": "mailto:ITWebTeam@tigta.treas.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TIGTA-0012",
+            "description": "Requests and Responses to Member of Congress for various information",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/tigta/recovery_congress.shtml",
                     "downloadURL": "http://www.treasury.gov/tigta/recovery_congress.shtml",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Congressional Correspondence",
-            "description": "Requests and Responses to Member of Congress for various information",
+            "identifier": "015-TIGTA-0012",
             "keyword": [
                 "congress",
                 "congressional",
@@ -9352,47 +9358,47 @@
                 "ig",
                 "tigta"
             ],
+            "landingPage": "http://www.treasury.gov/tigta/recovery_congress.shtml",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2023-12-08",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Office of IG",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TIGTA",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TIGTA"
-                },
-                "name": "Office of IG"
-            },
-            "contactPoint": {
-                "fn": "Office of Information Technology, Web Team",
-                "hasEmail": "mailto:ITWebTeam@tigta.treas.gov"
+            "title": "Congressional Correspondence"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:05"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/tigta/recovery_congress.shtml"
+            "contactPoint": {
+                "fn": "David Barnes",
+                "hasEmail": "mailto:TIGTAcommunications@tigta.treas.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TIGTA-0009",
+            "description": "TIGTA's Congressional Testimony contains the Inspector General's written testimony for Congressional hearings.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/tigta/publications_congress.shtml",
                     "downloadURL": "http://www.treasury.gov/tigta/publications_congress.shtml",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Congressional Testimony",
-            "description": "TIGTA's Congressional Testimony contains the Inspector General's written testimony for Congressional hearings.",
+            "identifier": "015-TIGTA-0009",
             "keyword": [
                 "congress",
                 "congressional",
@@ -9401,47 +9407,47 @@
                 "inspector general",
                 "ig"
             ],
+            "landingPage": "http://www.treasury.gov/tigta/publications_congress.shtml",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2023-12-08",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Office of Communications",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TIGTA",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TIGTA"
-                },
-                "name": "Office of Communications"
-            },
-            "contactPoint": {
-                "fn": "David Barnes",
-                "hasEmail": "mailto:TIGTAcommunications@tigta.treas.gov"
+            "title": "Congressional Testimony"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:05"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/tigta/publications_congress.shtml"
+            "contactPoint": {
+                "fn": "Office of Information Technology, Web Team",
+                "hasEmail": "mailto:ITWebTeam@tigta.treas.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TIGTA-0013",
+            "description": "Specific delegations of authority issued by the Inspector General, or equivalent level executives ot their subordinate officers or employees which redelegate authorities delegated to them or their subordinates.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/tigta/important_foia_ad_dele.shtml",
                     "downloadURL": "http://www.treasury.gov/tigta/important_foia_ad_dele.shtml",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Delegation Orders",
-            "description": "Specific delegations of authority issued by the Inspector General, or equivalent level executives ot their subordinate officers or employees which redelegate authorities delegated to them or their subordinates.",
+            "identifier": "015-TIGTA-0013",
             "keyword": [
                 "delegation",
                 "authority",
@@ -9450,92 +9456,92 @@
                 "inspector general",
                 "ig"
             ],
+            "landingPage": "http://www.treasury.gov/tigta/important_foia_ad_dele.shtml",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2023-12-08",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Office of IG",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TIGTA",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TIGTA"
-                },
-                "name": "Office of IG"
-            },
-            "contactPoint": {
-                "fn": "Office of Information Technology, Web Team",
-                "hasEmail": "mailto:ITWebTeam@tigta.treas.gov"
+            "title": "Delegation Orders"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "015:05"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/tigta/important_foia_ad_dele.shtml"
+            "contactPoint": {
+                "fn": "Office of Information Technology, Web Team",
+                "hasEmail": "mailto:ITWebTeam@tigta.treas.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TIGTA-0016",
+            "description": "Press releases from the Department of Justice concerning the IRS.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/tigta/oi_doj.shtml",
                     "downloadURL": "http://www.treasury.gov/tigta/oi_doj.shtml",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "title": "Department of Justice Press Releases",
-            "description": "Press releases from the Department of Justice concerning the IRS.",
+            "identifier": "015-TIGTA-0016",
             "keyword": [
                 "justice",
                 "press",
                 "release",
                 "IRS"
             ],
+            "landingPage": "http://www.treasury.gov/tigta/oi_doj.shtml",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2023-12-08",
+            "programCode": [
+                "015:016"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Department of Justice",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TIGTA",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TIGTA"
-                },
-                "name": "Department of Justice"
-            },
-            "contactPoint": {
-                "fn": "Office of Information Technology, Web Team",
-                "hasEmail": "mailto:ITWebTeam@tigta.treas.gov"
+            "title": "Department of Justice Press Releases"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "015:05"
             ],
-            "programCode": [
-                "015:016"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/tigta/oi_doj.shtml"
+            "contactPoint": {
+                "fn": "Office of Information Technology, Web Team",
+                "hasEmail": "mailto:ITWebTeam@tigta.treas.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TIGTA-0002",
+            "description": "TIGTA's inspections and evaluations monitor IRS compliance and performance in IRS challenge areas.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/tigta/oie_iereports.shtml",
                     "downloadURL": "http://www.treasury.gov/tigta/oie_iereports.shtml",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "title": "I&E Reports",
-            "description": "TIGTA's inspections and evaluations monitor IRS compliance and performance in IRS challenge areas.",
+            "identifier": "015-TIGTA-0002",
             "keyword": [
                 "tigta",
                 "inspection",
@@ -9548,46 +9554,46 @@
                 "inspector general",
                 "ig"
             ],
+            "landingPage": "http://www.treasury.gov/tigta/oie_iereports.shtml",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2023-12-08",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Office of Inspections and Evaluations",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TIGTA",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TIGTA"
-                },
-                "name": "Office of Inspections and Evaluations"
-            },
-            "contactPoint": {
-                "fn": "Office of Information Technology, Web Team",
-                "hasEmail": "mailto:ITWebTeam@tigta.treas.gov"
+            "title": "I&E Reports"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "015:05"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/tigta/oie_iereports.shtml"
+            "contactPoint": {
+                "fn": "Office of Information Technology, Web Team",
+                "hasEmail": "mailto:ITWebTeam@tigta.treas.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TIGTA-0004",
+            "description": "TIGTA's Investigations Highlights of investigations",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/tigta/oi_highlights.shtml",
                     "downloadURL": "http://www.treasury.gov/tigta/oi_highlights.shtml",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "title": "Investigation Highlights",
-            "description": "TIGTA's Investigations Highlights of investigations",
+            "identifier": "015-TIGTA-0004",
             "keyword": [
                 "tigta",
                 "investigations",
@@ -9596,46 +9602,46 @@
                 "inspector general",
                 "ig"
             ],
+            "landingPage": "http://www.treasury.gov/tigta/oi_highlights.shtml",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2023-12-08",
+            "programCode": [
+                "015:016"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Office of Investigations",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TIGTA",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TIGTA"
-                },
-                "name": "Office of Investigations"
-            },
-            "contactPoint": {
-                "fn": "Office of Information Technology, Web Team",
-                "hasEmail": "mailto:ITWebTeam@tigta.treas.gov"
+            "title": "Investigation Highlights"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "015:05"
             ],
-            "programCode": [
-                "015:016"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/tigta/oi_highlights.shtml"
+            "contactPoint": {
+                "fn": "Office of Information Technology, Web Team",
+                "hasEmail": "mailto:ITWebTeam@tigta.treas.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TIGTA-0019",
+            "description": "A listing of the information systems in use by TIGTA.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/tigta/important_foia_mis.shtml",
                     "downloadURL": "http://www.treasury.gov/tigta/important_foia_mis.shtml",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "title": "Major Information Systems",
-            "description": "A listing of the information systems in use by TIGTA.",
+            "identifier": "015-TIGTA-0019",
             "keyword": [
                 "information",
                 "systems",
@@ -9646,46 +9652,46 @@
                 "enterprise",
                 "information technology"
             ],
+            "landingPage": "http://www.treasury.gov/tigta/important_foia_mis.shtml",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2023-12-08",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Information Technology",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TIGTA",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TIGTA"
-                },
-                "name": "Information Technology"
-            },
-            "contactPoint": {
-                "fn": "Office of Information Technology, Web Team",
-                "hasEmail": "mailto:ITWebTeam@tigta.treas.gov"
+            "title": "Major Information Systems"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "015:05"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/tigta/important_foia_mis.shtml"
+            "contactPoint": {
+                "fn": "Office of Information Technology, Web Team",
+                "hasEmail": "mailto:ITWebTeam@tigta.treas.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TIGTA-0014",
+            "description": "TIGTA's annual letters to the Secretary of the Treasury present TIGTA's views on the management and performance challenges facing the IRS in the current fiscal year.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/tigta/oa_management.shtml",
                     "downloadURL": "http://www.treasury.gov/tigta/oa_management.shtml",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "title": "Management Performance Challenges Facing IRS",
-            "description": "TIGTA's annual letters to the Secretary of the Treasury present TIGTA's views on the management and performance challenges facing the IRS in the current fiscal year.",
+            "identifier": "015-TIGTA-0014",
             "keyword": [
                 "annual",
                 "letters",
@@ -9699,46 +9705,46 @@
                 "inspector general",
                 "ig"
             ],
+            "landingPage": "http://www.treasury.gov/tigta/oa_management.shtml",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2023-12-08",
+            "programCode": [
+                "015:015"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Office of Audit",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TIGTA",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TIGTA"
-                },
-                "name": "Office of Audit"
-            },
-            "contactPoint": {
-                "fn": "Office of Information Technology, Web Team",
-                "hasEmail": "mailto:ITWebTeam@tigta.treas.gov"
+            "title": "Management Performance Challenges Facing IRS"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "015:05"
             ],
-            "programCode": [
-                "015:015"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/tigta/oa_management.shtml"
+            "contactPoint": {
+                "fn": "Office of Information Technology, Web Team",
+                "hasEmail": "mailto:ITWebTeam@tigta.treas.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TIGTA-0017",
+            "description": "Memorandums of Understanding issued between TIGTA and other governmental agencies.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/tigta/important_foia_ad_memo.shtml",
                     "downloadURL": "http://www.treasury.gov/tigta/important_foia_ad_memo.shtml",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "title": "Memorandums of Understanding",
-            "description": "Memorandums of Understanding issued between TIGTA and other governmental agencies.",
+            "identifier": "015-TIGTA-0017",
             "keyword": [
                 "memo",
                 "memorandum",
@@ -9747,46 +9753,46 @@
                 "ig",
                 "understanding"
             ],
+            "landingPage": "http://www.treasury.gov/tigta/important_foia_ad_memo.shtml",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2023-12-08",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "TIGTA",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TIGTA",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TIGTA"
-                },
-                "name": "TIGTA"
-            },
-            "contactPoint": {
-                "fn": "Office of Information Technology, Web Team",
-                "hasEmail": "mailto:ITWebTeam@tigta.treas.gov"
+            "title": "Memorandums of Understanding"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "015:05"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/tigta/important_foia_ad_memo.shtml"
+            "contactPoint": {
+                "fn": "Office of Information Technology, Web Team",
+                "hasEmail": "mailto:ITWebTeam@tigta.treas.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TIGTA-0018",
+            "description": "Locations of TIGTA Offices",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/tigta/oi_office.shtml",
                     "downloadURL": "http://www.treasury.gov/tigta/oi_office.shtml",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "title": "Office Locations",
-            "description": "Locations of TIGTA Offices",
+            "identifier": "015-TIGTA-0018",
             "keyword": [
                 "investigations",
                 "tigta",
@@ -9795,47 +9801,47 @@
                 "locations",
                 "offices"
             ],
+            "landingPage": "http://www.treasury.gov/tigta/oi_office.shtml",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2023-12-08",
+            "programCode": [
+                "015:016"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Office of Investigations",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TIGTA",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TIGTA"
-                },
-                "name": "Office of Investigations"
-            },
-            "contactPoint": {
-                "fn": "Office of Information Technology, Web Team",
-                "hasEmail": "mailto:ITWebTeam@tigta.treas.gov"
+            "title": "Office Locations"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:05"
             ],
-            "programCode": [
-                "015:016"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/tigta/oi_office.shtml"
+            "contactPoint": {
+                "fn": "Office of Information Technology, Web Team",
+                "hasEmail": "mailto:ITWebTeam@tigta.treas.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TIGTA-0005",
+            "description": "TIGTA established this system in which delegated authorities, policies, procedures and guidelines are issued in a systematic manner.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/tigta/important_foia_ad_oper.shtml",
                     "downloadURL": "http://www.treasury.gov/tigta/important_foia_ad_oper.shtml",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Operations Manual",
-            "description": "TIGTA established this system in which delegated authorities, policies, procedures and guidelines are issued in a systematic manner.",
+            "identifier": "015-TIGTA-0005",
             "keyword": [
                 "operations",
                 "manual",
@@ -9846,47 +9852,47 @@
                 "inspector general",
                 "ig"
             ],
+            "landingPage": "http://www.treasury.gov/tigta/important_foia_ad_oper.shtml",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2023-12-08",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Office of Mission Support",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TIGTA",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TIGTA"
-                },
-                "name": "Office of Mission Support"
-            },
-            "contactPoint": {
-                "fn": "Office of Information Technology, Web Team",
-                "hasEmail": "mailto:ITWebTeam@tigta.treas.gov"
+            "title": "Operations Manual"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:05"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/tigta/important_foia_ad_oper.shtml"
+            "contactPoint": {
+                "fn": "Office of Information Technology, Web Team",
+                "hasEmail": "mailto:ITWebTeam@tigta.treas.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TIGTA-0020",
+            "description": "Organizational chart of TIGTA",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/tigta/about_orgchart.shtml",
                     "downloadURL": "http://www.treasury.gov/tigta/about_orgchart.shtml",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Organizational Chart",
-            "description": "Organizational chart of TIGTA",
+            "identifier": "015-TIGTA-0020",
             "keyword": [
                 "organizational",
                 "chart",
@@ -9895,46 +9901,46 @@
                 "ig",
                 "executives"
             ],
+            "landingPage": "http://www.treasury.gov/tigta/about_orgchart.shtml",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2023-12-08",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Office of Mission Support",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TIGTA",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TIGTA"
-                },
-                "name": "Office of Mission Support"
-            },
-            "contactPoint": {
-                "fn": "Office of Information Technology, Web Team",
-                "hasEmail": "mailto:ITWebTeam@tigta.treas.gov"
+            "title": "Organizational Chart"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "015:05"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/tigta/about_orgchart.shtml"
+            "contactPoint": {
+                "fn": "Office of Information Technology, Web Team",
+                "hasEmail": "mailto:ITWebTeam@tigta.treas.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TIGTA-0015",
+            "description": "The objective of the external quality control review program is to foster quality audits by Inspector General offices through an independent assessment of the effectiveness of the internal quality control system in providing reasonable assurance that applicable audit standards and requirements are being followed.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/tigta/oa_peerreports.shtml",
                     "downloadURL": "http://www.treasury.gov/tigta/oa_peerreports.shtml",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "title": "Peer Review Reports",
-            "description": "The objective of the external quality control review program is to foster quality audits by Inspector General offices through an independent assessment of the effectiveness of the internal quality control system in providing reasonable assurance that applicable audit standards and requirements are being followed.",
+            "identifier": "015-TIGTA-0015",
             "keyword": [
                 "peer",
                 "review",
@@ -9943,47 +9949,47 @@
                 "inspector general",
                 "ig"
             ],
+            "landingPage": "http://www.treasury.gov/tigta/oa_peerreports.shtml",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2023-12-08",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Council of the Inspector Generals",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TIGTA",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TIGTA"
-                },
-                "name": "Council of the Inspector Generals"
-            },
-            "contactPoint": {
-                "fn": "Office of Information Technology, Web Team",
-                "hasEmail": "mailto:ITWebTeam@tigta.treas.gov"
+            "title": "Peer Review Reports"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:05"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/tigta/oa_peerreports.shtml"
+            "contactPoint": {
+                "fn": "David Barnes",
+                "hasEmail": "mailto:TIGTAcommunications@tigta.treas.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TIGTA-0008",
+            "description": "TIGTA's Press Room: press releases, key facts, TIGTA statistics, press contact information.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/tigta/publications_press.shtml",
                     "downloadURL": "http://www.treasury.gov/tigta/publications_press.shtml",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Press Releases",
-            "description": "TIGTA's Press Room: press releases, key facts, TIGTA statistics, press contact information.",
+            "identifier": "015-TIGTA-0008",
             "keyword": [
                 "press",
                 "audit",
@@ -9993,46 +9999,46 @@
                 "inspector general",
                 "ig"
             ],
+            "landingPage": "http://www.treasury.gov/tigta/publications_press.shtml",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2023-12-08",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Office of Communications",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TIGTA",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TIGTA"
-                },
-                "name": "Office of Communications"
-            },
-            "contactPoint": {
-                "fn": "David Barnes",
-                "hasEmail": "mailto:TIGTAcommunications@tigta.treas.gov"
+            "title": "Press Releases"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "015:05"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/tigta/publications_press.shtml"
+            "contactPoint": {
+                "fn": "Office of Information Technology, Web Team",
+                "hasEmail": "mailto:ITWebTeam@tigta.treas.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TIGTA-0006",
+            "description": "The Recovery Act provides separate funding to the Treasury Inspector General for Tax Administration to be used in oversight activities of IRS programs which includes audits conducted using Recovery Act funds.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/tigta/recovery_reports_fy13_static.shtml",
                     "downloadURL": "http://www.treasury.gov/tigta/recovery_reports_fy13_static.shtml",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "title": "Recovery Act Reports",
-            "description": "The Recovery Act provides separate funding to the Treasury Inspector General for Tax Administration to be used in oversight activities of IRS programs which includes audits conducted using Recovery Act funds.",
+            "identifier": "015-TIGTA-0006",
             "keyword": [
                 "report",
                 "ARRA",
@@ -10044,47 +10050,47 @@
                 "inspector general",
                 "ig"
             ],
+            "landingPage": "http://www.treasury.gov/tigta/recovery_reports_fy13_static.shtml",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2023-12-08",
+            "programCode": [
+                "015:015"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Office of Audit",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TIGTA",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TIGTA"
-                },
-                "name": "Office of Audit"
-            },
-            "contactPoint": {
-                "fn": "Office of Information Technology, Web Team",
-                "hasEmail": "mailto:ITWebTeam@tigta.treas.gov"
+            "title": "Recovery Act Reports"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:05"
             ],
-            "programCode": [
-                "015:015"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/tigta/recovery_reports_fy13_static.shtml"
+            "contactPoint": {
+                "fn": "Office of Information Technology, Web Team",
+                "hasEmail": "mailto:ITWebTeam@tigta.treas.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TIGTA-0003",
+            "description": "TIGTA's Semiannual Reports contain updated facts, figures and accomplishments for Congress.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/tigta/publications_semi.shtml",
                     "downloadURL": "http://www.treasury.gov/tigta/publications_semi.shtml",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Semi Annual Report",
-            "description": "TIGTA's Semiannual Reports contain updated facts, figures and accomplishments for Congress.",
+            "identifier": "015-TIGTA-0003",
             "keyword": [
                 "tigta",
                 "semiannual",
@@ -10095,46 +10101,46 @@
                 "inspector general",
                 "ig"
             ],
+            "landingPage": "http://www.treasury.gov/tigta/publications_semi.shtml",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2023-12-08",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Office of Mission Support",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TIGTA",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TIGTA"
-                },
-                "name": "Office of Mission Support"
-            },
-            "contactPoint": {
-                "fn": "Office of Information Technology, Web Team",
-                "hasEmail": "mailto:ITWebTeam@tigta.treas.gov"
+            "title": "Semi Annual Report"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "015:05"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/tigta/publications_semi.shtml"
+            "contactPoint": {
+                "fn": "Office of Information Technology, Web Team",
+                "hasEmail": "mailto:ITWebTeam@tigta.treas.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TIGTA-0011",
+            "description": "TIGTA Work Plan",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "http://www.treasury.gov/tigta/recovery_programplan.shtml",
                     "downloadURL": "http://www.treasury.gov/tigta/recovery_programplan.shtml",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "title": "TIGTA Program Plan",
-            "description": "TIGTA Work Plan",
+            "identifier": "015-TIGTA-0011",
             "keyword": [
                 "program",
                 "plan",
@@ -10143,137 +10149,138 @@
                 "inspector general",
                 "ig"
             ],
+            "landingPage": "http://www.treasury.gov/tigta/recovery_programplan.shtml",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2023-12-08",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "Office of Mission Support",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TIGTA",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TIGTA"
-                },
-                "name": "Office of Mission Support"
-            },
-            "contactPoint": {
-                "fn": "Office of Information Technology, Web Team",
-                "hasEmail": "mailto:ITWebTeam@tigta.treas.gov"
+            "title": "TIGTA Program Plan"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
-                "015:05"
-            ],
-            "programCode": [
-                "015:000"
+                "015:13"
             ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "http://www.treasury.gov/tigta/recovery_programplan.shtml"
+            "contactPoint": {
+                "fn": "Mason, Quinton",
+                "hasEmail": "mailto:ttbfoia@ttb.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TTB-1",
+            "description": "Forms summarizing the Offers in Compromise accepted by TTB under the Collect the Revenue program code.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.ttb.gov/what-we-do/enforcement/offers-in-compromise",
                     "downloadURL": "https://www.ttb.gov/what-we-do/enforcement/offers-in-compromise",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Abstracts of Offers in Compromise (CTR)",
-            "description": "Forms summarizing the Offers in Compromise accepted by TTB under the Collect the Revenue program code.",
+            "identifier": "015-TTB-1",
             "keyword": [
                 "Compromise"
             ],
+            "landingPage": "https://www.ttb.gov/what-we-do/enforcement/offers-in-compromise",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2023-06-22",
+            "programCode": [
+                "015:026"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "TTB",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TTB",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TTB"
-                },
-                "name": "TTB"
-            },
-            "contactPoint": {
-                "fn": "Mason, Quinton",
-                "hasEmail": "mailto:ttbfoia@ttb.gov"
+            "title": "Abstracts of Offers in Compromise (CTR)"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:13"
             ],
-            "programCode": [
-                "015:026"
-            ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "https://www.ttb.gov/what-we-do/enforcement/offers-in-compromise"
+            "contactPoint": {
+                "fn": "Mason, Quinton",
+                "hasEmail": "mailto:ttbfoia@ttb.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TTB-2",
+            "description": "Forms summarizing the Offers in Compromise accepted by TTB under the Protect the Public program code.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.ttb.gov/what-we-do/enforcement/offers-in-compromise",
                     "downloadURL": "https://www.ttb.gov/what-we-do/enforcement/offers-in-compromise",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Abstracts of Offers in Compromise (PTP)",
-            "description": "Forms summarizing the Offers in Compromise accepted by TTB under the Protect the Public program code.",
+            "identifier": "015-TTB-2",
             "keyword": [
                 "Compromise"
             ],
+            "landingPage": "https://www.ttb.gov/what-we-do/enforcement/offers-in-compromise",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2023-06-22",
+            "programCode": [
+                "015:027"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "TTB",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TTB",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TTB"
-                },
-                "name": "TTB"
-            },
-            "contactPoint": {
-                "fn": "Mason, Quinton",
-                "hasEmail": "mailto:ttbfoia@ttb.gov"
+            "title": "Abstracts of Offers in Compromise (PTP)"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:13"
             ],
-            "programCode": [
-                "015:027"
-            ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "https://www.ttb.gov/what-we-do/enforcement/offers-in-compromise"
+            "contactPoint": {
+                "fn": "Mason, Quinton",
+                "hasEmail": "mailto:ttbfoia@ttb.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TTB-3",
+            "describedBy": "https://www.ttb.gov/glossary",
+            "description": "Table listing the domestic production of alcohol and tobacco by fiscal year (FY 1993 - FY 1995).",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.ttb.gov/images/pdfs/statistics/95news06.htm",
                     "describedBy": "https://www.ttb.gov/glossary",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.ttb.gov/images/pdfs/statistics/95news06.htm",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Alcohol and Tobacco Domestic Production Report",
-            "description": "Table listing the domestic production of alcohol and tobacco by fiscal year (FY 1993 - FY 1995).",
+            "identifier": "015-TTB-3",
             "keyword": [
                 "Alcohol",
                 "tobacco",
@@ -10285,98 +10292,98 @@
                 "snuff",
                 "TTB"
             ],
+            "landingPage": "https://www.ttb.gov/images/pdfs/statistics/95news06.htm",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "1995-09-30",
+            "programCode": [
+                "015:026"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "TTB",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TTB",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TTB"
-                },
-                "name": "TTB"
-            },
-            "contactPoint": {
-                "fn": "Mason, Quinton",
-                "hasEmail": "mailto:ttbfoia@ttb.gov"
+            "title": "Alcohol and Tobacco Domestic Production Report"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "015:13"
             ],
-            "programCode": [
-                "015:026"
-            ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "describedBy": "https://www.ttb.gov/glossary",
-            "landingPage": "https://www.ttb.gov/images/pdfs/statistics/95news06.htm"
+            "contactPoint": {
+                "fn": "Mason, Quinton",
+                "hasEmail": "mailto:ttbfoia@ttb.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TTB-4",
+            "describedBy": "https://www.ttb.gov/foia",
+            "description": "This dataset contains a list of Freedom of Information Act (FOIA) requests for fiscal year 2010 that include the date requested, date received, requestor, file number, and information requested.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.ttb.gov/foia/foia-logs",
                     "describedBy": "https://www.ttb.gov/foia",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.ttb.gov/foia/foia-logs",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "title": "Alcohol and Tobacco Tax and Trade Bureau (TTB) FOIA Request Logs",
-            "description": "This dataset contains a list of Freedom of Information Act (FOIA) requests for fiscal year 2010 that include the date requested, date received, requestor, file number, and information requested.",
+            "identifier": "015-TTB-4",
             "keyword": [
                 "FOIA",
                 "TTB"
             ],
+            "landingPage": "https://www.ttb.gov/foia/foia-logs",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2023-12-08",
+            "programCode": [
+                "015:027"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "TTB",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TTB",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TTB"
-                },
-                "name": "TTB"
-            },
-            "contactPoint": {
-                "fn": "Mason, Quinton",
-                "hasEmail": "mailto:ttbfoia@ttb.gov"
+            "title": "Alcohol and Tobacco Tax and Trade Bureau (TTB) FOIA Request Logs"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:13"
             ],
-            "programCode": [
-                "015:027"
-            ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "describedBy": "https://www.ttb.gov/foia",
-            "landingPage": "https://www.ttb.gov/foia/foia-logs"
+            "contactPoint": {
+                "fn": "Mason, Quinton",
+                "hasEmail": "mailto:ttbfoia@ttb.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TTB-6",
+            "describedBy": "https://www.ttb.gov/images/pdfs/2004_1_rulling_carbohydrate_calc.pdf",
+            "description": "Methods used to verify calorie, fat, carbohydrate, and protein content statements on alcohol beverage labels and advertisements.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.ttb.gov/scientific-services-division/alcohol-fact-labeling-methods",
                     "describedBy": "https://www.ttb.gov/images/pdfs/2004_1_rulling_carbohydrate_calc.pdf",
                     "describedByType": "application/pdf",
                     "downloadURL": "https://www.ttb.gov/scientific-services-division/alcohol-fact-labeling-methods",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Alcohol Fact Labeling Methods",
-            "description": "Methods used to verify calorie, fat, carbohydrate, and protein content statements on alcohol beverage labels and advertisements.",
+            "identifier": "015-TTB-6",
             "keyword": [
                 "Analytical methods",
                 "calorie",
@@ -10386,92 +10393,90 @@
                 "alcohol beverage labels",
                 "TTB"
             ],
+            "landingPage": "https://www.ttb.gov/scientific-services-division/alcohol-fact-labeling-methods",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2021-09-24",
+            "programCode": [
+                "015:027"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "TTB",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TTB",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TTB"
-                },
-                "name": "TTB"
-            },
-            "contactPoint": {
-                "fn": "Mason, Quinton",
-                "hasEmail": "mailto:ttbfoia@ttb.gov"
+            "references": [
+                "https://www.ttb.gov/images/pdfs/rulings/2004-1.pdf"
+            ],
+            "title": "Alcohol Fact Labeling Methods"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "015:13"
             ],
-            "programCode": [
-                "015:027"
-            ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "describedBy": "https://www.ttb.gov/images/pdfs/2004_1_rulling_carbohydrate_calc.pdf",
-            "landingPage": "https://www.ttb.gov/scientific-services-division/alcohol-fact-labeling-methods",
-            "references": [
-                "https://www.ttb.gov/images/pdfs/rulings/2004-1.pdf"
-            ]
+            "contactPoint": {
+                "fn": "Mason, Quinton",
+                "hasEmail": "mailto:ttbfoia@ttb.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TTB-7",
+            "describedBy": "https://www.ttb.gov/glossary",
+            "description": "List of alcohol fuel production amounts as reported on ATF F 5110.75.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.ttb.gov/images/pdfs/statistics/95newa07.htm",
                     "describedBy": "https://www.ttb.gov/glossary",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.ttb.gov/images/pdfs/statistics/95newa07.htm",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "title": "Alcohol Fuel Production",
-            "description": "List of alcohol fuel production amounts as reported on ATF F 5110.75.",
+            "identifier": "015-TTB-7",
             "keyword": [
                 "alcohol",
                 "fuel",
                 "TTB"
             ],
+            "landingPage": "https://www.ttb.gov/images/pdfs/statistics/95newa07.htm",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "1995-09-30",
+            "programCode": [
+                "015:026"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "TTB",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TTB",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TTB"
-                },
-                "name": "TTB"
-            },
-            "contactPoint": {
-                "fn": "Mason, Quinton",
-                "hasEmail": "mailto:ttbfoia@ttb.gov"
+            "title": "Alcohol Fuel Production"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:13"
             ],
-            "programCode": [
-                "015:026"
-            ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "describedBy": "https://www.ttb.gov/glossary",
-            "landingPage": "https://www.ttb.gov/images/pdfs/statistics/95newa07.htm"
+            "contactPoint": {
+                "fn": "Thornton, Karen",
+                "hasEmail": "mailto:RegulationsInquiries@ttb.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "theme": [
-                "geospatial"
-            ],
-            "identifier": "015-TTB-8",
+            "description": "Use the American Viticultural Area (AVA) Map Explorer to view the boundaries of all established and proposed AVAs. The Map Explorer has information about each AVA, including its state and county, when it was established, what other AVAs it contains or is within, and a link to its codified official boundary description. You can even plot an address on the Map Explorer to see if that location is within an AVA. You can also download \"shapefiles\" for the various AVAs, which you can use with geographic information system (GIS) software.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -10483,15 +10488,14 @@
                     "title": "Original Metadata"
                 },
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.ttb.gov/wine/ava-map-explorer",
                     "downloadURL": "https://www.ttb.gov/wine/ava-map-explorer",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "AVA Map Explorer",
-            "description": "Use the American Viticultural Area (AVA) Map Explorer to view the boundaries of all established and proposed AVAs. The Map Explorer has information about each AVA, including its state and county, when it was established, what other AVAs it contains or is within, and a link to its codified official boundary description. You can even plot an address on the Map Explorer to see if that location is within an AVA. You can also download \"shapefiles\" for the various AVAs, which you can use with geographic information system (GIS) software.",
+            "identifier": "015-TTB-8",
+            "issued": "2019-12-31T00:00:00",
             "keyword": [
                 "viticultural",
                 "wine",
@@ -10500,147 +10504,150 @@
                 "AVA",
                 "geospatial"
             ],
+            "landingPage": "https://www.ttb.gov/wine/ava-map-explorer",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2024-10-31",
+            "programCode": [
+                "015:026"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "TTB",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TTB",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TTB"
-                },
-                "name": "TTB"
-            },
-            "contactPoint": {
-                "fn": "Thornton, Karen",
-                "hasEmail": "mailto:RegulationsInquiries@ttb.gov"
+            "theme": [
+                "geospatial"
+            ],
+            "title": "AVA Map Explorer"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:13"
             ],
-            "programCode": [
-                "015:026"
-            ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "https://www.ttb.gov/wine/ava-map-explorer",
-            "issued": "2019-12-31T00:00:00"
+            "contactPoint": {
+                "fn": "Mason, Quinton",
+                "hasEmail": "mailto:ttbfoia@ttb.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TTB-9",
+            "describedBy": "https://www.ttb.gov/glossary",
+            "description": "Yearly and monthly statistical releases taken directly from the Brewer's Report of Operations TTB F 5130.9 and the Quarterly Brewer's Report of Operations TTB F 5130.26.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.ttb.gov/beer/statistics",
                     "describedBy": "https://www.ttb.gov/glossary",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.ttb.gov/beer/statistics",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "Beer Production and Operations Reports",
-            "description": "Yearly and monthly statistical releases taken directly from the Brewer's Report of Operations TTB F 5130.9 and the Quarterly Brewer's Report of Operations TTB F 5130.26.",
+            "identifier": "015-TTB-9",
             "keyword": [
                 "TTB",
                 "beer",
                 "brewer",
                 "brewpub"
             ],
+            "landingPage": "https://www.ttb.gov/beer/statistics",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2023-12-08",
+            "programCode": [
+                "015:026"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "TTB",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TTB",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TTB"
-                },
-                "name": "TTB"
-            },
-            "contactPoint": {
-                "fn": "Mason, Quinton",
-                "hasEmail": "mailto:ttbfoia@ttb.gov"
+            "title": "Beer Production and Operations Reports"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:13"
             ],
-            "programCode": [
-                "015:026"
-            ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "describedBy": "https://www.ttb.gov/glossary",
-            "landingPage": "https://www.ttb.gov/beer/statistics"
+            "contactPoint": {
+                "fn": "Mason, Quinton",
+                "hasEmail": "mailto:ttbfoia@ttb.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TTB-10",
+            "description": "Methods used to analyze alcohol beverages for the analytes listed in the table.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.ttb.gov/scientific-services-division/beverage-alcohol-methods",
                     "downloadURL": "https://www.ttb.gov/scientific-services-division/beverage-alcohol-methods",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Beverage Alcohol Methods",
-            "description": "Methods used to analyze alcohol beverages for the analytes listed in the table.",
+            "identifier": "015-TTB-10",
             "keyword": [
                 "Analytical methods",
                 "analyze alcohol",
                 "alcohol beverage",
                 "TTB"
             ],
+            "landingPage": "https://www.ttb.gov/scientific-services-division/beverage-alcohol-methods",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2023-07-06",
+            "programCode": [
+                "015:027"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "TTB",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TTB",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TTB"
-                },
-                "name": "TTB"
-            },
-            "contactPoint": {
-                "fn": "Mason, Quinton",
-                "hasEmail": "mailto:ttbfoia@ttb.gov"
+            "title": "Beverage Alcohol Methods"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:13"
             ],
-            "programCode": [
-                "015:027"
-            ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "https://www.ttb.gov/scientific-services-division/beverage-alcohol-methods"
+            "contactPoint": {
+                "fn": "Mason, Quinton",
+                "hasEmail": "mailto:ttbfoia@ttb.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TTB-11",
+            "describedBy": "https://www.ttb.gov/glossary",
+            "description": "Monthly distilled spirits statistical release reports compiled using data from:\r\n\r\nMonthly Report of Processing (Denaturing) Operations Form 5110.43\r\nMonthly Report of Production Operations Form 5110.40\r\nMonthly Report of Processing Operations Form 5110.25\r\nMonthly Report of Storage Operations Form 5110.11",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.ttb.gov/distilled-spirits/statistics",
                     "describedBy": "https://www.ttb.gov/glossary",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.ttb.gov/distilled-spirits/statistics",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "Distilled Spirits Production and Operations Reports",
-            "description": "Monthly distilled spirits statistical release reports compiled using data from:\r\n\r\nMonthly Report of Processing (Denaturing) Operations Form 5110.43\r\nMonthly Report of Production Operations Form 5110.40\r\nMonthly Report of Processing Operations Form 5110.25\r\nMonthly Report of Storage Operations Form 5110.11",
+            "identifier": "015-TTB-11",
             "keyword": [
                 "Alcohol",
                 "distilled",
@@ -10651,48 +10658,47 @@
                 "denaturing",
                 "TTB"
             ],
+            "landingPage": "https://www.ttb.gov/distilled-spirits/statistics",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2023-12-08",
+            "programCode": [
+                "015:026"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "TTB",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TTB",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TTB"
-                },
-                "name": "TTB"
-            },
-            "contactPoint": {
-                "fn": "Mason, Quinton",
-                "hasEmail": "mailto:ttbfoia@ttb.gov"
+            "title": "Distilled Spirits Production and Operations Reports"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:13"
             ],
-            "programCode": [
-                "015:026"
-            ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "describedBy": "https://www.ttb.gov/glossary",
-            "landingPage": "https://www.ttb.gov/distilled-spirits/statistics"
+            "contactPoint": {
+                "fn": "Mason, Quinton",
+                "hasEmail": "mailto:ttbfoia@ttb.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TTB-12",
+            "description": "Determining whether your product is unfit for beverage purposes has become much easier. The Nonbeverage Products Laboratory has developed several tools to streamline the process and remove the majority of subjectivity. Please use these guidelines and provide an unfit for beverage statement with your formula submissions.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.ttb.gov/scientific-services-division/dbmenu3sub1",
                     "downloadURL": "https://www.ttb.gov/scientific-services-division/dbmenu3sub1",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Drawback Tutorial",
-            "description": "Determining whether your product is unfit for beverage purposes has become much easier. The Nonbeverage Products Laboratory has developed several tools to streamline the process and remove the majority of subjectivity. Please use these guidelines and provide an unfit for beverage statement with your formula submissions.",
+            "identifier": "015-TTB-12",
             "keyword": [
                 "Flavors",
                 "TTB",
@@ -10700,96 +10706,96 @@
                 "Unfit",
                 "limited_ingredients"
             ],
+            "landingPage": "https://www.ttb.gov/scientific-services-division/dbmenu3sub1",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2023-06-01",
+            "programCode": [
+                "015:027"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "TTB",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TTB",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TTB"
-                },
-                "name": "TTB"
-            },
-            "contactPoint": {
-                "fn": "Mason, Quinton",
-                "hasEmail": "mailto:ttbfoia@ttb.gov"
+            "title": "Drawback Tutorial"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "015:13"
             ],
-            "programCode": [
-                "015:027"
-            ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "https://www.ttb.gov/scientific-services-division/dbmenu3sub1"
+            "contactPoint": {
+                "fn": "Mason, Quinton",
+                "hasEmail": "mailto:ttbfoia@ttb.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TTB-14",
+            "describedBy": "https://www.ttb.gov/glossary",
+            "description": "The Freedom of Information Act (FOIA) requires every Federal agency to submit a report to the Attorney General of the United States annually [pursuant to 5 U.S.C. 552(e)(1)], providing detailed information concerning the administration of the Act. TTB's submission is included in the Department of the Treasury's report.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.ttb.gov/foia/foia-annual-reports",
                     "describedBy": "https://www.ttb.gov/glossary",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.ttb.gov/foia/foia-annual-reports",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "title": "Freedom of Information Act (FOIA) Annual Reports",
-            "description": "The Freedom of Information Act (FOIA) requires every Federal agency to submit a report to the Attorney General of the United States annually [pursuant to 5 U.S.C. 552(e)(1)], providing detailed information concerning the administration of the Act. TTB's submission is included in the Department of the Treasury's report.",
+            "identifier": "015-TTB-14",
             "keyword": [
                 "FOIA",
                 "annual reports",
                 "TTB"
             ],
+            "landingPage": "https://www.ttb.gov/foia/foia-annual-reports",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2023-12-08",
+            "programCode": [
+                "015:027"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "TTB",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TTB",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TTB"
-                },
-                "name": "TTB"
-            },
-            "contactPoint": {
-                "fn": "Mason, Quinton",
-                "hasEmail": "mailto:ttbfoia@ttb.gov"
+            "title": "Freedom of Information Act (FOIA) Annual Reports"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "015:13"
             ],
-            "programCode": [
-                "015:027"
-            ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "describedBy": "https://www.ttb.gov/glossary",
-            "landingPage": "https://www.ttb.gov/foia/foia-annual-reports"
+            "contactPoint": {
+                "fn": "Mason, Quinton",
+                "hasEmail": "mailto:ttbfoia@ttb.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TTB-15",
+            "description": "As part of the Freedom of Information Act (FOIA), we are required to make available to the public records that are requested and released on a frequent basis. With that in mind, we publish a list of alcohol industry members who hold permits under the Federal Alcohol Administration Act. These permits allow production, bottling, importation, or distribution of beverage alcohol products.   This page also contains distilled spirits quarterly reports  (1st Qtr FY 15 thru 4th Qtr FY 17), spirits producer and bottler permit list (2010 \u2013 October 31, 2017), spirits producers and bottlers listing, 2012-2019 beverage spirits producers and bottlers by average taxable removals (in proof gallons), bonded wine producers count by state, and brewery count by state.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.ttb.gov/foia/list-of-permittees",
                     "downloadURL": "https://www.ttb.gov/foia/list-of-permittees",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1W",
-            "title": "Frequently Requested Listings",
-            "description": "As part of the Freedom of Information Act (FOIA), we are required to make available to the public records that are requested and released on a frequent basis. With that in mind, we publish a list of alcohol industry members who hold permits under the Federal Alcohol Administration Act. These permits allow production, bottling, importation, or distribution of beverage alcohol products.   This page also contains distilled spirits quarterly reports  (1st Qtr FY 15 thru 4th Qtr FY 17), spirits producer and bottler permit list (2010 \u2013 October 31, 2017), spirits producers and bottlers listing, 2012-2019 beverage spirits producers and bottlers by average taxable removals (in proof gallons), bonded wine producers count by state, and brewery count by state.",
+            "identifier": "015-TTB-15",
             "keyword": [
                 "spirits",
                 "producer",
@@ -10809,49 +10815,50 @@
                 "alcohol industry members",
                 "beverage alcohol products"
             ],
+            "landingPage": "https://www.ttb.gov/foia/list-of-permittees",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2023-12-08",
+            "programCode": [
+                "015:026"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "TTB",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TTB",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TTB"
-                },
-                "name": "TTB"
-            },
-            "contactPoint": {
-                "fn": "Mason, Quinton",
-                "hasEmail": "mailto:ttbfoia@ttb.gov"
+            "title": "Frequently Requested Listings"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:13"
             ],
-            "programCode": [
-                "015:026"
-            ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "https://www.ttb.gov/foia/list-of-permittees"
+            "contactPoint": {
+                "fn": "Mason, Quinton",
+                "hasEmail": "mailto:ttbfoia@ttb.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TTB-16",
+            "describedBy": "https://www.ttb.gov/glossary",
+            "description": "This dataset contains a list of historical tax rates for distilled spirits, wine, beer, and tobacco products.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.ttb.gov/tax-audit/historical-tax-rates",
                     "describedBy": "https://www.ttb.gov/glossary",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.ttb.gov/tax-audit/historical-tax-rates",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Historical Tax Rates",
-            "description": "This dataset contains a list of historical tax rates for distilled spirits, wine, beer, and tobacco products.",
+            "identifier": "015-TTB-16",
             "keyword": [
                 "tax",
                 "rates",
@@ -10862,50 +10869,50 @@
                 "tobacco",
                 "TTB"
             ],
+            "landingPage": "https://www.ttb.gov/tax-audit/historical-tax-rates",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2013-12-23",
+            "programCode": [
+                "015:026"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "TTB",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TTB",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TTB"
-                },
-                "name": "TTB"
-            },
-            "contactPoint": {
-                "fn": "Mason, Quinton",
-                "hasEmail": "mailto:ttbfoia@ttb.gov"
+            "title": "Historical Tax Rates"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:13"
             ],
-            "programCode": [
-                "015:026"
-            ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "describedBy": "https://www.ttb.gov/glossary",
-            "landingPage": "https://www.ttb.gov/tax-audit/historical-tax-rates"
+            "contactPoint": {
+                "fn": "Mason, Quinton",
+                "hasEmail": "mailto:ttbfoia@ttb.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TTB-17",
+            "describedBy": "https://www.ttb.gov/glossary",
+            "description": "Table that lists by fiscal year the number of stills seized, gallons of illicit spirits seized, and the gallons of mash seized.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.ttb.gov/images/pdfs/statistics/95newa08.htm",
                     "describedBy": "https://www.ttb.gov/glossary",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.ttb.gov/images/pdfs/statistics/95newa08.htm",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Illicit Liquor (\"Moonshine\")",
-            "description": "Table that lists by fiscal year the number of stills seized, gallons of illicit spirits seized, and the gallons of mash seized.",
+            "identifier": "015-TTB-17",
             "keyword": [
                 "moonshine",
                 "liquor",
@@ -10914,337 +10921,336 @@
                 "spirits",
                 "TTB"
             ],
+            "landingPage": "https://www.ttb.gov/images/pdfs/statistics/95newa08.htm",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "1995-09-30",
+            "programCode": [
+                "015:026"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "TTB",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TTB",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TTB"
-                },
-                "name": "TTB"
-            },
-            "contactPoint": {
-                "fn": "Mason, Quinton",
-                "hasEmail": "mailto:ttbfoia@ttb.gov"
+            "title": "Illicit Liquor (\"Moonshine\")"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:13"
             ],
-            "programCode": [
-                "015:026"
-            ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "describedBy": "https://www.ttb.gov/glossary",
-            "landingPage": "https://www.ttb.gov/images/pdfs/statistics/95newa08.htm"
+            "contactPoint": {
+                "fn": "Mason, Quinton",
+                "hasEmail": "mailto:ttbfoia@ttb.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TTB-22",
+            "description": "Listing of petitions to establish American Viticultural Areas (AVAs) that TTB has accepted as perfected in accordance with Part 9 of TTB regulations.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.ttb.gov/wine/list-of-pending-american-viticultural-areas-petitions",
                     "downloadURL": "https://www.ttb.gov/wine/list-of-pending-american-viticultural-areas-petitions",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "List of Pending American Viticultural Areas Petitions",
-            "description": "Listing of petitions to establish American Viticultural Areas (AVAs) that TTB has accepted as perfected in accordance with Part 9 of TTB regulations.",
+            "identifier": "015-TTB-22",
             "keyword": [
                 "viticultural",
                 "petition",
                 "wine"
             ],
+            "landingPage": "https://www.ttb.gov/wine/list-of-pending-american-viticultural-areas-petitions",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2023-07-24",
+            "programCode": [
+                "015:027"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "TTB",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TTB",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TTB"
-                },
-                "name": "TTB"
-            },
-            "contactPoint": {
-                "fn": "Mason, Quinton",
-                "hasEmail": "mailto:ttbfoia@ttb.gov"
+            "title": "List of Pending American Viticultural Areas Petitions"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:13"
             ],
-            "programCode": [
-                "015:027"
-            ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "https://www.ttb.gov/wine/list-of-pending-american-viticultural-areas-petitions"
+            "contactPoint": {
+                "fn": "Mason, Quinton",
+                "hasEmail": "mailto:ttbfoia@ttb.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TTB-32",
+            "description": "Written determinations that remove regulated industry members\u2019 ability to legally operate under the Protect the Public program code.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.ttb.gov/what-we-do/enforcement/offers-in-compromise",
                     "downloadURL": "https://www.ttb.gov/what-we-do/enforcement/offers-in-compromise",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Orders of revocation, suspension, or annulment of permits (PTP)",
-            "description": "Written determinations that remove regulated industry members\u2019 ability to legally operate under the Protect the Public program code.",
+            "identifier": "015-TTB-32",
             "keyword": [
                 "revocation",
                 "suspension",
                 "annulment",
                 "permit"
             ],
+            "landingPage": "https://www.ttb.gov/what-we-do/enforcement/offers-in-compromise",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2020-07-31",
+            "programCode": [
+                "015:027"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "TTB",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TTB",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TTB"
-                },
-                "name": "TTB"
-            },
-            "contactPoint": {
-                "fn": "Mason, Quinton",
-                "hasEmail": "mailto:ttbfoia@ttb.gov"
+            "title": "Orders of revocation, suspension, or annulment of permits (PTP)"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:13"
             ],
-            "programCode": [
-                "015:027"
-            ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "https://www.ttb.gov/what-we-do/enforcement/offers-in-compromise"
+            "contactPoint": {
+                "fn": "Mason, Quinton",
+                "hasEmail": "mailto:ttbfoia@ttb.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TTB-33",
+            "description": "TTB is committed to facilitating voluntary compliance through education and outreach. View the upcoming events where you\u2019ll find us, or submit a request for TTB to participate in your event.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.ttb.gov/outreach/outreach-program",
                     "downloadURL": "https://www.ttb.gov/outreach/outreach-program",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Outreach",
-            "description": "TTB is committed to facilitating voluntary compliance through education and outreach. View the upcoming events where you\u2019ll find us, or submit a request for TTB to participate in your event.",
+            "identifier": "015-TTB-33",
             "keyword": [
                 "outreach",
                 "webinars",
                 "conferences"
             ],
+            "landingPage": "https://www.ttb.gov/outreach/outreach-program",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2023-06-22",
+            "programCode": [
+                "015:026"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "TTB",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TTB",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TTB"
-                },
-                "name": "TTB"
-            },
-            "contactPoint": {
-                "fn": "Mason, Quinton",
-                "hasEmail": "mailto:ttbfoia@ttb.gov"
+            "title": "Outreach"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "015:13"
             ],
-            "programCode": [
-                "015:026"
-            ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "https://www.ttb.gov/outreach/outreach-program"
+            "contactPoint": {
+                "fn": "Mason, Quinton",
+                "hasEmail": "mailto:ttbfoia@ttb.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TTB-34",
+            "describedBy": "https://www.ttb.gov/glossary",
+            "description": "This information is compiled to show the average turnaround time it takes TTB to process applications to operate new businesses. This data pertains to the segment of applications which are received through TTB's electronic application system, Permits Online (PONL). The average number of days to process represents the average number of days elapsed from the date the National Revenue Center receives the application through the date that the applicant is approved to operate.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.ttb.gov/nrc/statistics-original-applications-to-operate",
                     "describedBy": "https://www.ttb.gov/glossary",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.ttb.gov/nrc/statistics-original-applications-to-operate",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1D",
-            "title": "Permit Application Processing Times",
-            "description": "This information is compiled to show the average turnaround time it takes TTB to process applications to operate new businesses. This data pertains to the segment of applications which are received through TTB's electronic application system, Permits Online (PONL). The average number of days to process represents the average number of days elapsed from the date the National Revenue Center receives the application through the date that the applicant is approved to operate.",
+            "identifier": "015-TTB-34",
             "keyword": [
                 "permits",
                 "applications",
                 "PONL",
                 "TTB"
             ],
+            "landingPage": "https://www.ttb.gov/nrc/statistics-original-applications-to-operate",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2023-12-08",
+            "programCode": [
+                "015:027"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "TTB",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TTB",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TTB"
-                },
-                "name": "TTB"
-            },
-            "contactPoint": {
-                "fn": "Mason, Quinton",
-                "hasEmail": "mailto:ttbfoia@ttb.gov"
+            "title": "Permit Application Processing Times"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "015:13"
             ],
-            "programCode": [
-                "015:027"
-            ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "describedBy": "https://www.ttb.gov/glossary",
-            "landingPage": "https://www.ttb.gov/nrc/statistics-original-applications-to-operate"
+            "contactPoint": {
+                "fn": "Mason, Quinton",
+                "hasEmail": "mailto:ttbfoia@ttb.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TTB-36",
+            "describedBy": "https://www.ttb.gov/formulation/fonl-processing-times",
+            "description": "This current processing times chart shows up-to-date processing information for beverage alcohol formulas, both those that require sample analysis and those that do not. Use this chart, which we update daily, to estimate when your formula application is likely to be processed.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.ttb.gov/formulation/fonl-processing-times",
                     "describedBy": "https://www.ttb.gov/formulation/fonl-processing-times",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.ttb.gov/images/foia/form_stats.csv",
-                    "mediaType": "text/csv",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/csv"
                 }
             ],
-            "accrualPeriodicity": "R/P1D",
-            "title": "Processing Times for Beverage Alcohol Formulas",
-            "description": "This current processing times chart shows up-to-date processing information for beverage alcohol formulas, both those that require sample analysis and those that do not. Use this chart, which we update daily, to estimate when your formula application is likely to be processed.",
+            "identifier": "015-TTB-36",
             "keyword": [
                 "TTB",
                 "alcohol formulation",
                 "beverage alcohol",
                 "sample analysis"
             ],
+            "landingPage": "https://www.ttb.gov/formulation/fonl-processing-times",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2023-12-08",
+            "programCode": [
+                "015:027"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "TTB",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TTB",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TTB"
-                },
-                "name": "TTB"
-            },
-            "contactPoint": {
-                "fn": "Mason, Quinton",
-                "hasEmail": "mailto:ttbfoia@ttb.gov"
+            "title": "Processing Times for Beverage Alcohol Formulas"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "015:13"
             ],
-            "programCode": [
-                "015:027"
-            ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "describedBy": "https://www.ttb.gov/formulation/fonl-processing-times",
-            "landingPage": "https://www.ttb.gov/formulation/fonl-processing-times"
+            "contactPoint": {
+                "fn": "Mason, Quinton",
+                "hasEmail": "mailto:ttbfoia@ttb.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TTB-37",
+            "describedBy": "https://www.ttb.gov/labeling/processing-times#chart",
+            "description": "Table of current alcohol label processing times.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.ttb.gov/labeling/processing-times",
                     "describedBy": "https://www.ttb.gov/labeling/processing-times#chart",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.ttb.gov/images/foia/cola_stats.xml",
-                    "mediaType": "text/xml",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/xml"
                 }
             ],
-            "accrualPeriodicity": "R/P1D",
-            "title": "Processing Times for Label Applications",
-            "description": "Table of current alcohol label processing times.",
+            "identifier": "015-TTB-37",
             "keyword": [
                 "alcohol",
                 "labels",
                 "processing times",
                 "TTB"
             ],
+            "landingPage": "https://www.ttb.gov/labeling/processing-times",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2023-12-08",
+            "programCode": [
+                "015:027"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "TTB",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TTB",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TTB"
-                },
-                "name": "TTB"
-            },
-            "contactPoint": {
-                "fn": "Mason, Quinton",
-                "hasEmail": "mailto:ttbfoia@ttb.gov"
+            "title": "Processing Times for Label Applications"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "015:13"
             ],
-            "programCode": [
-                "015:027"
-            ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "describedBy": "https://www.ttb.gov/labeling/processing-times#chart",
-            "landingPage": "https://www.ttb.gov/labeling/processing-times"
+            "contactPoint": {
+                "fn": "Mason, Quinton",
+                "hasEmail": "mailto:ttbfoia@ttb.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TTB-13",
+            "description": "Quarterly breakdown of the Firearms and Ammunition Excise Tax (FAET) collections which are broken out between handguns, long guns, and ammunition (calculated per returns)",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.ttb.gov/foia/electronic-reading-room",
                     "downloadURL": "https://www.ttb.gov/images/foia/xls/Quarterly-breakdown-of-FAET-collections.xlsx",
-                    "mediaType": "application/vnd.ms-excel",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "application/vnd.ms-excel"
                 }
             ],
-            "accrualPeriodicity": "R/P3M",
-            "title": "Quarterly breakdown of the Firearms and Ammunition Excise Tax (FAET) collections which are broken out between handguns, long guns, and ammunition (calculated per returns)",
-            "description": "Quarterly breakdown of the Firearms and Ammunition Excise Tax (FAET) collections which are broken out between handguns, long guns, and ammunition (calculated per returns)",
+            "identifier": "015-TTB-13",
             "keyword": [
                 "firearms",
                 "ammunition",
@@ -11253,49 +11259,50 @@
                 "shells",
                 "cartridges"
             ],
+            "landingPage": "https://www.ttb.gov/foia/electronic-reading-room",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2023-12-08",
+            "programCode": [
+                "015:026"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "TTB",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TTB",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TTB"
-                },
-                "name": "TTB"
-            },
-            "contactPoint": {
-                "fn": "Mason, Quinton",
-                "hasEmail": "mailto:ttbfoia@ttb.gov"
+            "title": "Quarterly breakdown of the Firearms and Ammunition Excise Tax (FAET) collections which are broken out between handguns, long guns, and ammunition (calculated per returns)"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "015:13"
             ],
-            "programCode": [
-                "015:026"
-            ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "https://www.ttb.gov/foia/electronic-reading-room"
+            "contactPoint": {
+                "fn": "Mason, Quinton",
+                "hasEmail": "mailto:ttbfoia@ttb.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TTB-44",
+            "describedBy": "https://www.ttb.gov/glossary",
+            "description": "This dataset consists of quarterly and annual statistical reports on taxes collected by TTB.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.ttb.gov/tax-audit/tax-collections",
                     "describedBy": "https://www.ttb.gov/glossary",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.ttb.gov/tax-audit/tax-collections",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P3M",
-            "title": "Tax Collections-All",
-            "description": "This dataset consists of quarterly and annual statistical reports on taxes collected by TTB.",
+            "identifier": "015-TTB-44",
             "keyword": [
                 "Tax",
                 "taxes",
@@ -11312,50 +11319,50 @@
                 "spirits",
                 "TTB"
             ],
+            "landingPage": "https://www.ttb.gov/tax-audit/tax-collections",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2023-12-08",
+            "programCode": [
+                "015:026"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "TTB",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TTB",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TTB"
-                },
-                "name": "TTB"
-            },
-            "contactPoint": {
-                "fn": "Mason, Quinton",
-                "hasEmail": "mailto:ttbfoia@ttb.gov"
+            "title": "Tax Collections-All"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:13"
             ],
-            "programCode": [
-                "015:026"
-            ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "describedBy": "https://www.ttb.gov/glossary",
-            "landingPage": "https://www.ttb.gov/tax-audit/tax-collections"
+            "contactPoint": {
+                "fn": "Mason, Quinton",
+                "hasEmail": "mailto:ttbfoia@ttb.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TTB-45",
+            "describedBy": "https://www.ttb.gov/glossary",
+            "description": "Current tax rates for alcohol beverages, tobacco products, firearms and ammunition and information on filing taxes with TTB.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.ttb.gov/tax-audit/tax-and-fee-rates",
                     "describedBy": "https://www.ttb.gov/glossary",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.ttb.gov/tax-audit/tax-and-fee-rates",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Tax Rates",
-            "description": "Current tax rates for alcohol beverages, tobacco products, firearms and ammunition and information on filing taxes with TTB.",
+            "identifier": "015-TTB-45",
             "keyword": [
                 "Tax",
                 "taxes",
@@ -11377,94 +11384,93 @@
                 "revolver",
                 "TTB"
             ],
+            "landingPage": "https://www.ttb.gov/tax-audit/tax-and-fee-rates",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2023-07-24",
+            "programCode": [
+                "015:026"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "TTB",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TTB",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TTB"
-                },
-                "name": "TTB"
-            },
-            "contactPoint": {
-                "fn": "Mason, Quinton",
-                "hasEmail": "mailto:ttbfoia@ttb.gov"
+            "title": "Tax Rates"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:13"
             ],
-            "programCode": [
-                "015:026"
-            ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "describedBy": "https://www.ttb.gov/glossary",
-            "landingPage": "https://www.ttb.gov/tax-audit/tax-and-fee-rates"
+            "contactPoint": {
+                "fn": "Mason, Quinton",
+                "hasEmail": "mailto:ttbfoia@ttb.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TTB-47",
+            "description": "Schedule for annual, quarterly, semi-monthly, and FAET filers.   List of due dates for export documentation for industry members with approved export variances to maintain records on premises.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.ttb.gov/tax-audit/excise-tax-and-export-due-dates",
                     "downloadURL": "https://www.ttb.gov/tax-audit/excise-tax-and-export-due-dates",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Tax Returns and Reports Due Dates",
-            "description": "Schedule for annual, quarterly, semi-monthly, and FAET filers.   List of due dates for export documentation for industry members with approved export variances to maintain records on premises.",
+            "identifier": "015-TTB-47",
             "keyword": [
                 "excise",
                 "tax",
                 "export"
             ],
+            "landingPage": "https://www.ttb.gov/tax-audit/excise-tax-and-export-due-dates",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2023-01-20",
+            "programCode": [
+                "015:026"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "TTB",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TTB",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TTB"
-                },
-                "name": "TTB"
-            },
-            "contactPoint": {
-                "fn": "Mason, Quinton",
-                "hasEmail": "mailto:ttbfoia@ttb.gov"
+            "title": "Tax Returns and Reports Due Dates"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:13"
             ],
-            "programCode": [
-                "015:026"
-            ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "https://www.ttb.gov/tax-audit/excise-tax-and-export-due-dates"
+            "contactPoint": {
+                "fn": "Mason, Quinton",
+                "hasEmail": "mailto:ttbfoia@ttb.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TTB-48",
+            "description": "References for methods used in tobacco tax classification.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.ttb.gov/scientific-services-division/tobacco-methods",
                     "downloadURL": "https://www.ttb.gov/scientific-services-division/tobacco-methods",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "Tobacco Methods",
-            "description": "References for methods used in tobacco tax classification.",
+            "identifier": "015-TTB-48",
             "keyword": [
                 "Tobacco",
                 "cigarettes",
@@ -11476,49 +11482,50 @@
                 "analytical methods",
                 "TTB"
             ],
+            "landingPage": "https://www.ttb.gov/scientific-services-division/tobacco-methods",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2021-10-08",
+            "programCode": [
+                "015:026"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "TTB",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TTB",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TTB"
-                },
-                "name": "TTB"
-            },
-            "contactPoint": {
-                "fn": "Mason, Quinton",
-                "hasEmail": "mailto:ttbfoia@ttb.gov"
+            "title": "Tobacco Methods"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:13"
             ],
-            "programCode": [
-                "015:026"
-            ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "https://www.ttb.gov/scientific-services-division/tobacco-methods"
+            "contactPoint": {
+                "fn": "Mason, Quinton",
+                "hasEmail": "mailto:ttbfoia@ttb.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TTB-49",
+            "describedBy": "https://www.ttb.gov/glossary",
+            "description": "Monthly statistical reports on tobacco products production and operations. Data for Tobacco Statistical Release is derived directly from the Report \u2013 Manufacturer of Tobacco Products or Cigarette Papers and Tubes Form 5210.5.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.ttb.gov/tobacco/tobacco-statistics",
                     "describedBy": "https://www.ttb.gov/glossary",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.ttb.gov/tobacco/tobacco-statistics",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "Tobacco Products Production and Operations Reports",
-            "description": "Monthly statistical reports on tobacco products production and operations. Data for Tobacco Statistical Release is derived directly from the Report \u2013 Manufacturer of Tobacco Products or Cigarette Papers and Tubes Form 5210.5.",
+            "identifier": "015-TTB-49",
             "keyword": [
                 "tobacco",
                 "cigarettes",
@@ -11529,138 +11536,137 @@
                 "export",
                 "TTB"
             ],
+            "landingPage": "https://www.ttb.gov/tobacco/tobacco-statistics",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2023-12-08",
+            "programCode": [
+                "015:026"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "TTB",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TTB",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TTB"
-                },
-                "name": "TTB"
-            },
-            "contactPoint": {
-                "fn": "Mason, Quinton",
-                "hasEmail": "mailto:ttbfoia@ttb.gov"
+            "title": "Tobacco Products Production and Operations Reports"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:13"
             ],
-            "programCode": [
-                "015:026"
-            ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "describedBy": "https://www.ttb.gov/glossary",
-            "landingPage": "https://www.ttb.gov/tobacco/tobacco-statistics"
+            "contactPoint": {
+                "fn": "Mason, Quinton",
+                "hasEmail": "mailto:ttbfoia@ttb.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TTB-50",
+            "description": "Statistics relating to the use of Pay.gov.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.ttb.gov/epayment",
                     "downloadURL": "https://www.ttb.gov/epayment",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "TTB and Pay.gov Customer Support",
-            "description": "Statistics relating to the use of Pay.gov.",
+            "identifier": "015-TTB-50",
             "keyword": [
                 "statistics",
                 "pay.gov"
             ],
+            "landingPage": "https://www.ttb.gov/epayment",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2023-12-08",
+            "programCode": [
+                "015:026"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "TTB",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TTB",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TTB"
-                },
-                "name": "TTB"
-            },
-            "contactPoint": {
-                "fn": "Mason, Quinton",
-                "hasEmail": "mailto:ttbfoia@ttb.gov"
+            "title": "TTB and Pay.gov Customer Support"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "015:13"
             ],
-            "programCode": [
-                "015:026"
-            ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "https://www.ttb.gov/epayment"
+            "contactPoint": {
+                "fn": "Mason, Quinton",
+                "hasEmail": "mailto:ttbfoia@ttb.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TTB-51",
+            "description": "Reports on TTB\u2019s  performance and financial information regarding its programs and operations to its customers and stakeholders.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.ttb.gov/about-ttb/plans-and-reports-annual-reports",
                     "downloadURL": "https://www.ttb.gov/about-ttb/plans-and-reports-annual-reports",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "title": "TTB Annual Reports",
-            "description": "Reports on TTB\u2019s  performance and financial information regarding its programs and operations to its customers and stakeholders.",
+            "identifier": "015-TTB-51",
             "keyword": [
                 "financial",
                 "budget"
             ],
+            "landingPage": "https://www.ttb.gov/about-ttb/plans-and-reports-annual-reports",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2023-12-08",
+            "programCode": [
+                "015:005"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "TTB",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TTB",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TTB"
-                },
-                "name": "TTB"
-            },
-            "contactPoint": {
-                "fn": "Mason, Quinton",
-                "hasEmail": "mailto:ttbfoia@ttb.gov"
+            "title": "TTB Annual Reports"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:13"
             ],
-            "programCode": [
-                "015:005"
-            ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "https://www.ttb.gov/about-ttb/plans-and-reports-annual-reports"
+            "contactPoint": {
+                "fn": "Mason, Quinton",
+                "hasEmail": "mailto:ttbfoia@ttb.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TTB-52",
+            "description": "Worksheets for calculating items 9 and 10, simple mixtures and filtrations, extracts, and dietary supplements on TTB Form 5154.1.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.ttb.gov/scientific-services-division/dbmenu2sub3",
                     "downloadURL": "https://www.ttb.gov/scientific-services-division/dbmenu2sub3",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "TTB Form 5154.1 Worksheets",
-            "description": "Worksheets for calculating items 9 and 10, simple mixtures and filtrations, extracts, and dietary supplements on TTB Form 5154.1.",
+            "identifier": "015-TTB-52",
             "keyword": [
                 "Dietary supplements",
                 "flavors",
@@ -11671,47 +11677,47 @@
                 "filtrations",
                 "TTB"
             ],
+            "landingPage": "https://www.ttb.gov/scientific-services-division/dbmenu2sub3",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2021-06-10",
+            "programCode": [
+                "015:027"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "TTB",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TTB",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TTB"
-                },
-                "name": "TTB"
-            },
-            "contactPoint": {
-                "fn": "Mason, Quinton",
-                "hasEmail": "mailto:ttbfoia@ttb.gov"
+            "title": "TTB Form 5154.1 Worksheets"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:13"
             ],
-            "programCode": [
-                "015:027"
-            ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "https://www.ttb.gov/scientific-services-division/dbmenu2sub3"
+            "contactPoint": {
+                "fn": "Mason, Quinton",
+                "hasEmail": "mailto:ttbfoia@ttb.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TTB-53",
+            "description": "TTB periodically participates in industry conferences and seminars to provide training or relevant TTB-related information. We also occasionally hold our own training events, such as webinars or seminars. We\u2019re sharing those presentations here for everyone\u2019s benefit. Choose from the topics below to see a listing of related presentations.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.ttb.gov/main-pages/presentations",
                     "downloadURL": "https://www.ttb.gov/main-pages/presentations",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "TTB Presentations",
-            "description": "TTB periodically participates in industry conferences and seminars to provide training or relevant TTB-related information. We also occasionally hold our own training events, such as webinars or seminars. We\u2019re sharing those presentations here for everyone\u2019s benefit. Choose from the topics below to see a listing of related presentations.",
+            "identifier": "015-TTB-53",
             "keyword": [
                 "wine",
                 "cider",
@@ -11726,47 +11732,47 @@
                 "spirits",
                 "trade_practices"
             ],
+            "landingPage": "https://www.ttb.gov/main-pages/presentations",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2023-05-17",
+            "programCode": [
+                "015:026"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "TTB",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TTB",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
-                        "name": "Department of the Treasury"
-                    },
-                    "name": "TTB"
-                },
-                "name": "TTB"
+                        "name": "Department of the Treasury"
+                    }
+                }
             },
-            "contactPoint": {
-                "fn": "Mason, Quinton",
-                "hasEmail": "mailto:ttbfoia@ttb.gov"
+            "title": "TTB Presentations"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:13"
             ],
-            "programCode": [
-                "015:026"
-            ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "https://www.ttb.gov/main-pages/presentations"
+            "contactPoint": {
+                "fn": "Mason, Quinton",
+                "hasEmail": "mailto:ttbfoia@ttb.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TTB-54",
+            "description": "Locate and view the approved, expired, surrendered, or revoked Certificate of Label Approval (COLA), via the COLA Public Registry.   The URL needs to be followed by the command: ?action=publicDisplaySearchBasic&ttbid=XXXXXXXXXXXXXX, where XXXXXXXXXXXXXX is the 14 character value for the COLA's TTB ID.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.ttbonline.gov/colasonline/publicSearchColasBasic.do",
                     "downloadURL": "https://www.ttbonline.gov/colasonline/publicSearchColasBasic.do",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "TTB Public COLA Registry \u2013 View the details of a specific Certificate of Label Approval (COLA)",
-            "description": "Locate and view the approved, expired, surrendered, or revoked Certificate of Label Approval (COLA), via the COLA Public Registry.   The URL needs to be followed by the command: ?action=publicDisplaySearchBasic&ttbid=XXXXXXXXXXXXXX, where XXXXXXXXXXXXXX is the 14 character value for the COLA's TTB ID.",
+            "identifier": "015-TTB-54",
             "keyword": [
                 "COLAs Online",
                 "COLA Public Registry",
@@ -11778,50 +11784,50 @@
                 "FOIA",
                 "TTB"
             ],
+            "landingPage": "https://www.ttbonline.gov/colasonline/publicSearchColasBasic.do",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2023-12-08",
+            "programCode": [
+                "015:027"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "TTB",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TTB",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TTB"
-                },
-                "name": "TTB"
-            },
-            "contactPoint": {
-                "fn": "Mason, Quinton",
-                "hasEmail": "mailto:ttbfoia@ttb.gov"
+            "references": [
+                "https://www.ttb.gov/images/pdfs/labeling_colas-docs/display-cola-detail-through-public-cola-registry.pdf"
+            ],
+            "title": "TTB Public COLA Registry \u2013 View the details of a specific Certificate of Label Approval (COLA)"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "015:13"
             ],
-            "programCode": [
-                "015:027"
-            ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "https://www.ttbonline.gov/colasonline/publicSearchColasBasic.do",
-            "references": [
-                "https://www.ttb.gov/images/pdfs/labeling_colas-docs/display-cola-detail-through-public-cola-registry.pdf"
-            ]
+            "contactPoint": {
+                "fn": "Mason, Quinton",
+                "hasEmail": "mailto:ttbfoia@ttb.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TTB-55",
+            "description": "Locate, view and download the details associated with approved, expired, surrendered, or revoked Certificate of Label Approvals (COLAs), via the COLA Public Registry.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.ttbonline.gov/colasonline/publicSearchColasBasic.do",
                     "downloadURL": "https://www.ttbonline.gov/colasonline/publicSearchColasBasic.do",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "irregular",
-            "title": "TTB Public COLA Registry Search and Download \u2013 Extract data about COLAs that meet specified search criteria",
-            "description": "Locate, view and download the details associated with approved, expired, surrendered, or revoked Certificate of Label Approvals (COLAs), via the COLA Public Registry.",
+            "identifier": "015-TTB-55",
             "keyword": [
                 "COLAs Online",
                 "COLA Public Registry",
@@ -11833,273 +11839,273 @@
                 "FOIA",
                 "TTB"
             ],
+            "landingPage": "https://www.ttbonline.gov/colasonline/publicSearchColasBasic.do",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2014-02-06",
+            "programCode": [
+                "015:027"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "TTB",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TTB",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TTB"
-                },
-                "name": "TTB"
-            },
-            "contactPoint": {
-                "fn": "Mason, Quinton",
-                "hasEmail": "mailto:ttbfoia@ttb.gov"
+            "references": [
+                "https://www.ttb.gov/images/pdfs/labeling_colas-docs/save-search-results-in-public-cola-registry.pdf"
+            ],
+            "title": "TTB Public COLA Registry Search and Download \u2013 Extract data about COLAs that meet specified search criteria"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:13"
             ],
-            "programCode": [
-                "015:027"
-            ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "landingPage": "https://www.ttbonline.gov/colasonline/publicSearchColasBasic.do",
-            "references": [
-                "https://www.ttb.gov/images/pdfs/labeling_colas-docs/save-search-results-in-public-cola-registry.pdf"
-            ]
+            "contactPoint": {
+                "fn": "Mason, Quinton",
+                "hasEmail": "mailto:ttbfoia@ttb.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-TTB-56",
+            "describedBy": "https://www.ttb.gov/glossary",
+            "description": "Data for Wine Statistical Releases is derived directly from the Report of Wine Premises Operations Form 5120.17. This form must be filed with TTB 15 days after the close of the period. The Wine Statistical Release report is generated approximately 45 days after the due date.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.ttb.gov/wine/wine-statistics",
                     "describedBy": "https://www.ttb.gov/glossary",
                     "describedByType": "text/html",
                     "downloadURL": "https://www.ttb.gov/wine/wine-statistics",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "Wine Statistics",
-            "description": "Data for Wine Statistical Releases is derived directly from the Report of Wine Premises Operations Form 5120.17. This form must be filed with TTB 15 days after the close of the period. The Wine Statistical Release report is generated approximately 45 days after the due date.",
+            "identifier": "015-TTB-56",
             "keyword": [
                 "TTB",
                 "wine",
                 "statistical",
                 "form5120.17"
             ],
+            "landingPage": "https://www.ttb.gov/wine/wine-statistics",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "modified": "2023-12-08",
+            "programCode": [
+                "015:026"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "TTB",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "TTB",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "TTB"
-                },
-                "name": "TTB"
-            },
-            "contactPoint": {
-                "fn": "Mason, Quinton",
-                "hasEmail": "mailto:ttbfoia@ttb.gov"
+            "title": "Wine Statistics"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
-                "015:13"
-            ],
-            "programCode": [
-                "015:026"
+                "015:25"
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "describedBy": "https://www.ttb.gov/glossary",
-            "landingPage": "https://www.ttb.gov/wine/wine-statistics"
+            "contactPoint": {
+                "fn": "Thomas Samuelsen",
+                "hasEmail": "mailto:Thomas.Samuelsen@usmint.treas.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-USMint-0001",
+            "description": "Sales totals by month are updated every weekday by 5 p.m. (ET). Mintage is updated annually. Programs tracked in this report include: American Eagle, American Buffalo, and America the Beautiful Silver Five Ounce Coin",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usmint.gov/bullion-sales",
                     "downloadURL": "https://www.usmint.gov/bullion-sales",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1D",
-            "title": "Bullion Sales and Mintage\u00a0Figures",
-            "description": "Sales totals by month are updated every weekday by 5 p.m. (ET). Mintage is updated annually. Programs tracked in this report include: American Eagle, American Buffalo, and America the Beautiful Silver Five Ounce Coin",
+            "identifier": "015-USMint-0001",
             "keyword": [
                 "Bullion Sales",
                 "Bullion Mintage\u00a0Figures"
             ],
+            "landingPage": "https://www.usmint.gov/bullion-sales",
             "modified": "2023-12-08",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "United States Mint. Sales and Marketing (SAM) Department",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "USMint",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "USMint"
-                },
-                "name": "United States Mint. Sales and Marketing (SAM) Department"
-            },
-            "contactPoint": {
-                "fn": "Thomas Samuelsen",
-                "hasEmail": "mailto:Thomas.Samuelsen@usmint.treas.gov"
+            "title": "Bullion Sales and Mintage\u00a0Figures"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "015:25"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "landingPage": "https://www.usmint.gov/bullion-sales"
+            "contactPoint": {
+                "fn": "Thomas Samuelsen",
+                "hasEmail": "mailto:Thomas.Samuelsen@usmint.treas.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-USMint-0002",
+            "description": "Production figures for circulating coins by denomination manufactured in Denver and Philadelphia. Updated monthly. Data includes active and inactive programs. Programs tracked in this report include: America the Beautiful Quarters, Presidential $1 Coins, District of Columbia and U.S. Territories Quarters, 50 State Quarters, Westward Journey Nickel Series. Presidential $1 Coins, Native American $1 Coins, and Kennedy Half Dollar Coins are currently only minted for numismatic products. Coins minted for numismatic bags, rolls, and boxes are produced in the circulating departments and may be shown in circulating totals",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usmint.gov/circulating-coins-production",
                     "downloadURL": "https://www.usmint.gov/circulating-coins-production",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
-            "title": "Circulating Coins Production Figures",
-            "description": "Production figures for circulating coins by denomination manufactured in Denver and Philadelphia. Updated monthly. Data includes active and inactive programs. Programs tracked in this report include: America the Beautiful Quarters, Presidential $1 Coins, District of Columbia and U.S. Territories Quarters, 50 State Quarters, Westward Journey Nickel Series. Presidential $1 Coins, Native American $1 Coins, and Kennedy Half Dollar Coins are currently only minted for numismatic products. Coins minted for numismatic bags, rolls, and boxes are produced in the circulating departments and may be shown in circulating totals",
+            "identifier": "015-USMint-0002",
             "keyword": [
                 "Circulating Coins Production Figures"
             ],
+            "landingPage": "https://www.usmint.gov/circulating-coins-production",
             "modified": "2023-12-08",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "United States Mint, Sales and Marketing (SAM) Department",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "USMint",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "USMint"
-                },
-                "name": "United States Mint, Sales and Marketing (SAM) Department"
-            },
-            "contactPoint": {
-                "fn": "Thomas Samuelsen",
-                "hasEmail": "mailto:Thomas.Samuelsen@usmint.treas.gov"
+            "title": "Circulating Coins Production Figures"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "015:25"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "landingPage": "https://www.usmint.gov/circulating-coins-production"
+            "contactPoint": {
+                "fn": "Thomas Samuelsen",
+                "hasEmail": "mailto:Thomas.Samuelsen@usmint.treas.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-USMint-0003",
+            "description": "The cumulative total of net sales demand for numismatic products reported from the launch of each product through the report date. Updated weekly by 5 p.m. (ET) Tuesdays. These figures should not be considered final and are subject to change as audited. Products are classified by program category. Some products may contain multiple coins that could fall under various categories",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usmint.gov/cumulative-sales-figures/",
                     "downloadURL": "https://www.usmint.gov/cumulative-sales-figures/",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1W",
-            "title": "Cumulative Numismatic Sales Figures",
-            "description": "The cumulative total of net sales demand for numismatic products reported from the launch of each product through the report date. Updated weekly by 5 p.m. (ET) Tuesdays. These figures should not be considered final and are subject to change as audited. Products are classified by program category. Some products may contain multiple coins that could fall under various categories",
+            "identifier": "015-USMint-0003",
             "keyword": [
                 "Cumulative Numismatic Sales Figures"
             ],
+            "landingPage": "https://www.usmint.gov/cumulative-sales-figures/",
             "modified": "2023-12-08",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "United States Mint, Sales and Marketing (SAM) Department",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "USMint",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "USMint"
-                },
-                "name": "United States Mint, Sales and Marketing (SAM) Department"
-            },
-            "contactPoint": {
-                "fn": "Thomas Samuelsen",
-                "hasEmail": "mailto:Thomas.Samuelsen@usmint.treas.gov"
+            "title": "Cumulative Numismatic Sales Figures"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "015:25"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "landingPage": "https://www.usmint.gov/cumulative-sales-figures/"
+            "contactPoint": {
+                "fn": "Thomas Samuelsen",
+                "hasEmail": "mailto:Thomas.Samuelsen@usmint.treas.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-USMint-0004",
+            "description": "Annual sales figures for numismatic precious metal products. Updated annually after sales have been audited and finalized. Programs tracked in this report include American Eagle and American Buffalo.",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usmint.gov/precious-metal-products",
                     "downloadURL": "https://www.usmint.gov/precious-metal-products",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "title": "Numismatic Precious Metal Products Sales Figures",
-            "description": "Annual sales figures for numismatic precious metal products. Updated annually after sales have been audited and finalized. Programs tracked in this report include American Eagle and American Buffalo.",
+            "identifier": "015-USMint-0004",
             "keyword": [
                 "Numismatic Precious Metal Products Sales Figures"
             ],
+            "landingPage": "https://www.usmint.gov/precious-metal-products",
             "modified": "2023-12-08",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "United States Mint, Sales and Marketing (SAM) Department",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "USMint",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "USMint"
-                },
-                "name": "United States Mint, Sales and Marketing (SAM) Department"
-            },
-            "contactPoint": {
-                "fn": "Thomas Samuelsen",
-                "hasEmail": "mailto:Thomas.Samuelsen@usmint.treas.gov"
+            "title": "Numismatic Precious Metal Products Sales Figures"
         },
+        {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "015:25"
             ],
-            "programCode": [
-                "015:000"
-            ],
-            "landingPage": "https://www.usmint.gov/precious-metal-products"
+            "contactPoint": {
+                "fn": "David Lean",
+                "hasEmail": "mailto:david.lean@usmint.treas.gov"
             },
-        {
-            "@type": "dcat:Dataset",
-            "identifier": "015-USMint-0005",
+            "description": "Complete audited financial and program report",
             "distribution": [
                 {
+                    "@type": "dcat:Distribution",
                     "accessURL": "https://www.usmint.gov/about/reports",
                     "downloadURL": "https://www.usmint.gov/about/reports",
-                    "mediaType": "text/html",
-                    "@type": "dcat:Distribution"
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "title": "United States Mint Annual Reports",
-            "description": "Complete audited financial and program report",
+            "identifier": "015-USMint-0005",
             "keyword": [
                 "Audited Financial Statements",
                 "MD&A",
@@ -12108,31 +12114,25 @@
                 "Bullion Sales",
                 "Circulating Coin Sales"
             ],
+            "landingPage": "https://www.usmint.gov/about/reports",
             "modified": "2023-12-08",
+            "programCode": [
+                "015:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
+                "name": "United States Mint, Financial Department (CFO)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
+                    "name": "USMint",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Department of the Treasury"
+                    }
+                }
             },
-                    "name": "USMint"
-                },
-                "name": "United States Mint, Financial Department (CFO)"
-            },
-            "contactPoint": {
-                "fn": "David Lean",
-                "hasEmail": "mailto:david.lean@usmint.treas.gov"
-            },
-            "accessLevel": "public",
-            "bureauCode": [
-                "015:25"
-            ],
-            "programCode": [
-                "015:000"
-            ],
-            "landingPage": "https://www.usmint.gov/about/reports"
+            "title": "United States Mint Annual Reports"
         }
-    ]
+    ],
+    "describedBy": "https://project-open-data.cio.gov/v1.1/schema/catalog.json"
 }
```

