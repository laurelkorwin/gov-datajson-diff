# Change History for justice.json (Part 2)

### Changes from acf49f0 to dd2190f (Part 2/22)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
+            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a nationally-representative sample of residential addresses since 1973. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, motor vehicle theft, and vandalism. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations. This version of the NCVS, referred to as the collection year, contains records from interviews conducted in the 12 months of the given year.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR34650.v2",
+                    "title": "National Crime Victimization Survey, [United States], 2012"
+                }
+            ],
+            "identifier": "223",
+            "isPartOf": "2432",
+            "issued": "2013-10-28T11:19:55",
             "keyword": [
                 "assault",
                 "auto theft",
@@ -11231,106 +11225,106 @@
                 "victimization",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-01-26T11:15:48",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2013-10-28T11:19:55",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR34650.v2",
-                    "title": "National Crime Victimization Survey, [United States], 2012"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Victimization Survey: Identity Theft Supplement, 2008",
-            "description": "The primary purpose of the Identity Theft Supplement is to obtain additional information about identity theft-related victimizations so that policymakers, academic researchers, practitioners at the Federal, state and local levels, and special interest groups who are concerned with identity theft can make informed decisions concerning policies and programs. Responses are linked to the NCVS survey instrument responses for a more complete understanding of the individual's circumstances.",
-            "modified": "2012-02-17T14:35:35",
-            "accessLevel": "public",
-            "identifier": "224",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
-                "hasEmail": "mailto:askbjs@usdoj.gov"
+            "title": "National Crime Victimization Survey, [United States], 2012"
         },
-            "keyword": [
-                "identity theft",
-                "theft"
-            ],
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "bureauCode": [
                 "011:21"
             ],
-            "programCode": [
-                "011:061"
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
+                "hasEmail": "mailto:askbjs@usdoj.gov"
+            },
             "dataQuality": false,
-            "issued": "2012-02-17T14:35:35",
-            "language": [
-                "eng"
-            ],
+            "description": "The primary purpose of the Identity Theft Supplement is to obtain additional information about identity theft-related victimizations so that policymakers, academic researchers, practitioners at the Federal, state and local levels, and special interest groups who are concerned with identity theft can make informed decisions concerning policies and programs. Responses are linked to the NCVS survey instrument responses for a more complete understanding of the individual's circumstances.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://doi.org/10.3886/ICPSR26362.v1",
                     "title": "National Crime Victimization Survey: Identity Theft Supplement, 2008"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Victimization Survey: Identity Theft Supplement, 2012",
-            "description": "The primary purpose of the Identity Theft Supplement is to obtain additional information about identity theft-related victimizations so that policymakers, academic researchers, practitioners at the Federal, state and local levels, and special interest groups who are concerned with identity theft can make informed decisions concerning policies and programs. Responses are linked to the NCVS survey instrument responses for a more complete understanding of the individual's circumstances.",
-            "modified": "2017-01-31T13:40:23",
-            "accessLevel": "public",
-            "identifier": "225",
+            ],
+            "identifier": "224",
+            "isPartOf": "2432",
+            "issued": "2012-02-17T14:35:35",
+            "keyword": [
+                "identity theft",
+                "theft"
+            ],
+            "language": [
+                "eng"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2012-02-17T14:35:35",
+            "programCode": [
+                "011:061"
+            ],
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Victimization Survey: Identity Theft Supplement, 2008"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The primary purpose of the Identity Theft Supplement is to obtain additional information about identity theft-related victimizations so that policymakers, academic researchers, practitioners at the Federal, state and local levels, and special interest groups who are concerned with identity theft can make informed decisions concerning policies and programs. Responses are linked to the NCVS survey instrument responses for a more complete understanding of the individual's circumstances.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR34735.v1",
+                    "title": "National Crime Victimization Survey: Identity Theft Supplement, 2012"
+                }
+            ],
+            "identifier": "225",
+            "isPartOf": "2432",
+            "issued": "2014-02-20T16:02:01",
             "keyword": [
                 "crime",
                 "crime rates",
@@ -11341,54 +11335,54 @@
                 "victimization",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2017-01-31T13:40:23",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2014-02-20T16:02:01",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR34735.v1",
-                    "title": "National Crime Victimization Survey: Identity Theft Supplement, 2012"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Victimization Survey: MSA Data, 1979-2004",
-            "description": "The National Crime Victimization Survey (NCVS), previously\r\n the National Crime Survey (NCS), has been collecting data on personal\r\n and household victimization through an ongoing survey of a\r\n nationally-representative sample of residential addresses since 1973.\r\n The survey is administered by the United States Census Bureau (under\r\n the United States Department of Commerce) on behalf of the Bureau of\r\n Justice Statistics (under the United States Department of Justice).\r\n Occasionally there have been extract or supplement files created from\r\n the NCVS and NCS data series. This extract contains two data files, a\r\n weighted person-based file, and a weighted incident-based file, which\r\n contain the \"core\" counties within the top 40 National Crime\r\n Victimization Survey Metropolitan Statistical Areas (MSAs). Core\r\n counties within these MSAs are defined as those self-representing\r\n primary sampling units that are common to the MSA definitions\r\n determined by the Office of Management and Budget for the 1970-based,\r\n 1980-based, and 1990-based sample designs. Each MSA is comprised of\r\n only the core counties and not all counties within the MSA. The\r\n person-based file contains select household and person variables for\r\n all people in NCVS-interviewed households in the core counties of the\r\n 40 largest MSAs from January 1979 through December 2004. The\r\n incident-based file contains select household, person, and incident\r\n variables for persons who reported a violent crime within any of the\r\n core counties of the 40 largest MSAs from January 1979 through\r\n December 2004. Household, person, and incident information for persons\r\n reporting non-violent crime are excluded from this file. The 40\r\n largest MSAs were determined based on the number of household\r\ninterviews in an MSA.",
-            "modified": "2007-01-15T00:00:00",
-            "accessLevel": "public",
-            "identifier": "226",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Victimization Survey: Identity Theft Supplement, 2012"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Crime Victimization Survey (NCVS), previously\r\n the National Crime Survey (NCS), has been collecting data on personal\r\n and household victimization through an ongoing survey of a\r\n nationally-representative sample of residential addresses since 1973.\r\n The survey is administered by the United States Census Bureau (under\r\n the United States Department of Commerce) on behalf of the Bureau of\r\n Justice Statistics (under the United States Department of Justice).\r\n Occasionally there have been extract or supplement files created from\r\n the NCVS and NCS data series. This extract contains two data files, a\r\n weighted person-based file, and a weighted incident-based file, which\r\n contain the \"core\" counties within the top 40 National Crime\r\n Victimization Survey Metropolitan Statistical Areas (MSAs). Core\r\n counties within these MSAs are defined as those self-representing\r\n primary sampling units that are common to the MSA definitions\r\n determined by the Office of Management and Budget for the 1970-based,\r\n 1980-based, and 1990-based sample designs. Each MSA is comprised of\r\n only the core counties and not all counties within the MSA. The\r\n person-based file contains select household and person variables for\r\n all people in NCVS-interviewed households in the core counties of the\r\n 40 largest MSAs from January 1979 through December 2004. The\r\n incident-based file contains select household, person, and incident\r\n variables for persons who reported a violent crime within any of the\r\n core counties of the 40 largest MSAs from January 1979 through\r\n December 2004. Household, person, and incident information for persons\r\n reporting non-violent crime are excluded from this file. The 40\r\n largest MSAs were determined based on the number of household\r\ninterviews in an MSA.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR04576.v1",
+                    "title": "National Crime Victimization Survey: MSA Data, 1979-2004"
+                }
+            ],
+            "identifier": "226",
+            "isPartOf": "2432",
+            "issued": "2007-01-15T00:00:00",
             "keyword": [
                 "assault",
                 "auto theft",
@@ -11409,54 +11403,54 @@
                 "victimization",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2007-01-15T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2007-01-15T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR04576.v1",
-                    "title": "National Crime Victimization Survey: MSA Data, 1979-2004"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Victimization Survey:  School Crime Supplement, 1995 ",
-            "description": "This supplement to the National Crime Victimization Surveys\r\n (formerly the National Crime Surveys)\r\n was designed to collect data on crime victimization in schools in the\r\n United States. Student respondents were asked a series of questions\r\n to determine their school attendance in the last six months. Other\r\n questions concerning schools were posed, including type of school,\r\n distance from home, and general attendance and monitoring\r\n policies. The data present information on the response of the school\r\n to student violation of rules, accessibility of drugs, and violence in\r\n school, including types of violence and student reaction. Other\r\n variables cover general violent crimes, personal larceny crimes, and\r\n household crimes and offer information on date, time, and place of\r\n crime. Demographic characteristics of household members such as age,\r\n sex, race, education, employment, median family income, and marital\r\nstatus are provided.",
-            "modified": "1998-04-06T00:00:00",
-            "accessLevel": "public",
-            "identifier": "227",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Victimization Survey: MSA Data, 1979-2004"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This supplement to the National Crime Victimization Surveys\r\n (formerly the National Crime Surveys)\r\n was designed to collect data on crime victimization in schools in the\r\n United States. Student respondents were asked a series of questions\r\n to determine their school attendance in the last six months. Other\r\n questions concerning schools were posed, including type of school,\r\n distance from home, and general attendance and monitoring\r\n policies. The data present information on the response of the school\r\n to student violation of rules, accessibility of drugs, and violence in\r\n school, including types of violence and student reaction. Other\r\n variables cover general violent crimes, personal larceny crimes, and\r\n household crimes and offer information on date, time, and place of\r\n crime. Demographic characteristics of household members such as age,\r\n sex, race, education, employment, median family income, and marital\r\nstatus are provided.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR06739.v1",
+                    "title": "National Crime Victimization Survey:  School Crime Supplement, 1995 "
+                }
+            ],
+            "identifier": "227",
+            "isPartOf": "2432",
+            "issued": "1998-04-06T00:00:00",
             "keyword": [
                 "crime",
                 "crime in schools",
@@ -11480,54 +11474,54 @@
                 "victimization",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "1998-04-06T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "1998-04-06T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR06739.v1",
-                    "title": "National Crime Victimization Survey:  School Crime Supplement, 1995 "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Victimization Survey: School Crime Supplement, 1999",
-            "description": "This supplement to the National Crime Victimization Survey\r\n(formerly the National Crime Surveys) was designed to collect data on\r\ncrime victimization in schools in the United States. Student\r\nrespondents were asked a series of questions to determine their school\r\nattendance in the last six months. Other questions concerning schools\r\nwere posed, including preventive measures employed by schools,\r\nstudents' participation in after-school activities, students'\r\nperception of school rules and enforcement of these rules, the\r\npresence of weapons, drugs, alcohol, and gangs in school, student\r\nbullying, hate-related incidents, and attitudinal questions relating\r\nto the fear of victimization at school. Other variables cover general\r\nviolent crimes, personal larceny crimes, and household crimes and\r\noffer information on date, time, and place of crime. Demographic\r\ncharacteristics of household members such as age, sex, race,\r\neducation, employment, median family income, and marital status are\r\nprovided.",
-            "modified": "2001-09-20T00:00:00",
-            "accessLevel": "public",
-            "identifier": "228",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Victimization Survey:  School Crime Supplement, 1995 "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This supplement to the National Crime Victimization Survey\r\n(formerly the National Crime Surveys) was designed to collect data on\r\ncrime victimization in schools in the United States. Student\r\nrespondents were asked a series of questions to determine their school\r\nattendance in the last six months. Other questions concerning schools\r\nwere posed, including preventive measures employed by schools,\r\nstudents' participation in after-school activities, students'\r\nperception of school rules and enforcement of these rules, the\r\npresence of weapons, drugs, alcohol, and gangs in school, student\r\nbullying, hate-related incidents, and attitudinal questions relating\r\nto the fear of victimization at school. Other variables cover general\r\nviolent crimes, personal larceny crimes, and household crimes and\r\noffer information on date, time, and place of crime. Demographic\r\ncharacteristics of household members such as age, sex, race,\r\neducation, employment, median family income, and marital status are\r\nprovided.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR03137.v1",
+                    "title": "National Crime Victimization Survey: School Crime Supplement, 1999"
+                }
+            ],
+            "identifier": "228",
+            "isPartOf": "2432",
+            "issued": "2001-06-27T00:00:00",
             "keyword": [
                 "crime",
                 "crime in schools",
@@ -11551,54 +11545,54 @@
                 "victimization",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2001-09-20T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2001-06-27T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR03137.v1",
-                    "title": "National Crime Victimization Survey: School Crime Supplement, 1999"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Victimization Survey: School Crime Supplement, 2001",
-            "description": "This supplement to the National Crime Victimization Survey\r\n(formerly the National Crime Surveys) was designed to collect data on\r\ncrime victimization in schools in the United States. Student\r\nrespondents were asked a series of questions to determine their school\r\nattendance in the last six months. Other questions concerning schools\r\nwere posed, including preventive measures employed by schools,\r\nstudents' participation in after-school activities, students'\r\nperception of school rules and enforcement of these rules, the\r\npresence of weapons, drugs, alcohol, and gangs in schools, student\r\nbullying, hate-related incidents, and attitudinal questions relating\r\nto the fear of victimization at school. Other variables cover general\r\nviolent crimes, personal larceny crimes, and household crimes and\r\noffer information on date, time, and place of crime. Demographic\r\ncharacteristics of household members such as age, sex, race,\r\neducation, employment, median family income, and marital status are\r\nprovided.",
-            "modified": "2002-09-19T00:00:00",
-            "accessLevel": "public",
-            "identifier": "229",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Victimization Survey: School Crime Supplement, 1999"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This supplement to the National Crime Victimization Survey\r\n(formerly the National Crime Surveys) was designed to collect data on\r\ncrime victimization in schools in the United States. Student\r\nrespondents were asked a series of questions to determine their school\r\nattendance in the last six months. Other questions concerning schools\r\nwere posed, including preventive measures employed by schools,\r\nstudents' participation in after-school activities, students'\r\nperception of school rules and enforcement of these rules, the\r\npresence of weapons, drugs, alcohol, and gangs in schools, student\r\nbullying, hate-related incidents, and attitudinal questions relating\r\nto the fear of victimization at school. Other variables cover general\r\nviolent crimes, personal larceny crimes, and household crimes and\r\noffer information on date, time, and place of crime. Demographic\r\ncharacteristics of household members such as age, sex, race,\r\neducation, employment, median family income, and marital status are\r\nprovided.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR03477.v1",
+                    "title": "National Crime Victimization Survey: School Crime Supplement, 2001"
+                }
+            ],
+            "identifier": "229",
+            "isPartOf": "2432",
+            "issued": "2002-09-19T00:00:00",
             "keyword": [
                 "crime",
                 "crime in schools",
@@ -11622,54 +11616,54 @@
                 "victimization",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2002-09-19T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2002-09-19T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR03477.v1",
-                    "title": "National Crime Victimization Survey: School Crime Supplement, 2001"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Victimization Survey: School Crime Supplement, 2003",
-            "description": "This supplement to the National Crime Victimization Survey\r\n (formerly the National Crime Surveys) was designed to collect data on\r\n crime victimization in schools in the United States. Student\r\n respondents were asked a series of questions to determine their school\r\n attendance in the last six months. Other questions concerning schools\r\n were posed, including preventive measures employed by schools,\r\n students' participation in after-school activities, students'\r\n perception of school rules and enforcement of these rules, the\r\n presence of weapons, drugs, alcohol, and gangs in schools, student\r\n bullying, hate-related incidents, and attitudinal questions relating\r\n to the fear of victimization at school. Other variables cover general\r\n violent crimes, personal larceny crimes, and household crimes and\r\n offer information on date, time, and place of crime. Demographic\r\n characteristics of household members such as age, sex, race,\r\n education, employment, median family income, and marital status are\r\nprovided.",
-            "modified": "2005-07-29T00:00:00",
-            "accessLevel": "public",
-            "identifier": "230",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Victimization Survey: School Crime Supplement, 2001"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This supplement to the National Crime Victimization Survey\r\n (formerly the National Crime Surveys) was designed to collect data on\r\n crime victimization in schools in the United States. Student\r\n respondents were asked a series of questions to determine their school\r\n attendance in the last six months. Other questions concerning schools\r\n were posed, including preventive measures employed by schools,\r\n students' participation in after-school activities, students'\r\n perception of school rules and enforcement of these rules, the\r\n presence of weapons, drugs, alcohol, and gangs in schools, student\r\n bullying, hate-related incidents, and attitudinal questions relating\r\n to the fear of victimization at school. Other variables cover general\r\n violent crimes, personal larceny crimes, and household crimes and\r\n offer information on date, time, and place of crime. Demographic\r\n characteristics of household members such as age, sex, race,\r\n education, employment, median family income, and marital status are\r\nprovided.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR04182.v1",
+                    "title": "National Crime Victimization Survey: School Crime Supplement, 2003"
+                }
+            ],
+            "identifier": "230",
+            "isPartOf": "2432",
+            "issued": "2005-07-29T00:00:00",
             "keyword": [
                 "crime",
                 "crime in schools",
@@ -11694,54 +11688,54 @@
                 "victimization",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2005-07-29T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2005-07-29T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR04182.v1",
-                    "title": "National Crime Victimization Survey: School Crime Supplement, 2003"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Victimization Survey: School Crime Supplement, 2005",
-            "description": "This supplement to the National Crime Victimization Survey\r\n (formerly the National Crime Surveys) was designed to collect data on\r\n crime victimization in schools in the United States. Student\r\n respondents were asked a series of questions to determine their school\r\n attendance in the last six months. Other questions concerning schools\r\n were posed including preventive measures employed by schools,\r\n students' participation in after-school activities, students'\r\n perception of school rules and enforcement of these rules, the\r\n presence of weapons, drugs, alcohol, and gangs in schools, student\r\n bullying, hate-related incidents, and attitudinal questions relating\r\n to the fear of victimization at school. Other variables cover general\r\n violent crimes, personal larceny crimes, and household crimes and\r\n offer information on date, time, and place of crime. Demographic\r\n characteristics of household members such as age, sex, race,\r\n education, employment, household income, and marital status are\r\nprovided.",
-            "modified": "2008-04-30T09:32:16",
-            "accessLevel": "public",
-            "identifier": "231",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Victimization Survey: School Crime Supplement, 2003"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This supplement to the National Crime Victimization Survey\r\n (formerly the National Crime Surveys) was designed to collect data on\r\n crime victimization in schools in the United States. Student\r\n respondents were asked a series of questions to determine their school\r\n attendance in the last six months. Other questions concerning schools\r\n were posed including preventive measures employed by schools,\r\n students' participation in after-school activities, students'\r\n perception of school rules and enforcement of these rules, the\r\n presence of weapons, drugs, alcohol, and gangs in schools, student\r\n bullying, hate-related incidents, and attitudinal questions relating\r\n to the fear of victimization at school. Other variables cover general\r\n violent crimes, personal larceny crimes, and household crimes and\r\n offer information on date, time, and place of crime. Demographic\r\n characteristics of household members such as age, sex, race,\r\n education, employment, household income, and marital status are\r\nprovided.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR04429.v2",
+                    "title": "National Crime Victimization Survey: School Crime Supplement, 2005"
+                }
+            ],
+            "identifier": "231",
+            "isPartOf": "2432",
+            "issued": "2006-12-04T00:00:00",
             "keyword": [
                 "crime",
                 "crime in schools",
@@ -11765,54 +11759,54 @@
                 "victimization",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-04-30T09:32:16",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2006-12-04T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR04429.v2",
-                    "title": "National Crime Victimization Survey: School Crime Supplement, 2005"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Victimization Survey: School Crime Supplement, 2007",
-            "description": "The primary purpose of the School Crime Supplement (SCS) is to obtain additional information about school-related victimizations so that policymakers, academic researchers, practitioners at the federal, state and local levels, and special interest groups who are concerned with crime in schools can make informed decisions concerning policies and programs. The SCS asks questions related to students' experiences with, and perceptions of crime and safety at school, including preventive measures employed by schools, students' participation in after school activities, students' perception of school rules and enforcement of these rules, the presence of weapons, drugs, alcohol, and gangs in school,\r\nstudent bullying, hate-related incidents, and attitudinal questions relating to the fear of victimization at school. These responses are linked to the National Crime Victimization Survey (NCVS) survey instrument responses for a more complete understanding of the individual student's circumstances.",
-            "modified": "2009-03-26T10:59:02",
-            "accessLevel": "public",
-            "identifier": "232",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Victimization Survey: School Crime Supplement, 2005"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The primary purpose of the School Crime Supplement (SCS) is to obtain additional information about school-related victimizations so that policymakers, academic researchers, practitioners at the federal, state and local levels, and special interest groups who are concerned with crime in schools can make informed decisions concerning policies and programs. The SCS asks questions related to students' experiences with, and perceptions of crime and safety at school, including preventive measures employed by schools, students' participation in after school activities, students' perception of school rules and enforcement of these rules, the presence of weapons, drugs, alcohol, and gangs in school,\r\nstudent bullying, hate-related incidents, and attitudinal questions relating to the fear of victimization at school. These responses are linked to the National Crime Victimization Survey (NCVS) survey instrument responses for a more complete understanding of the individual student's circumstances.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR23041.v1",
+                    "title": "National Crime Victimization Survey: School Crime Supplement, 2007"
+                }
+            ],
+            "identifier": "232",
+            "isPartOf": "2432",
+            "issued": "2009-03-26T10:59:02",
             "keyword": [
                 "crime",
                 "crime in schools",
@@ -11836,54 +11830,54 @@
                 "victimization",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2009-03-26T10:59:02",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2009-03-26T10:59:02",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR23041.v1",
-                    "title": "National Crime Victimization Survey: School Crime Supplement, 2007"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Victimization Survey: School Crime Supplement, 2009",
-            "description": "The primary purpose of the School Crime Supplement (SCS) is to obtain additional information about school-related victimizations so that policymakers; academic researchers; practitioners at the federal, state, and local levels; and special interest groups who are concerned with crime in schools can make informed decisions concerning policies and programs. The SCS asks questions related to students' experiences with, and perceptions of crime and safety at school, including preventive measures employed by schools; students' participation in after school activities; students' perception of school rules and enforcement of these rules; the presence of weapons, drugs, alcohol, and gangs in school;\r\nstudent bullying; hate-related incidents; and attitudinal questions relating to the fear of victimization at school. These responses are linked to the National Crime Victimization Survey (NCVS) survey instrument responses for a more complete understanding of the individual student's circumstances.",
-            "modified": "2011-01-21T09:24:37",
-            "accessLevel": "public",
-            "identifier": "233",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Victimization Survey: School Crime Supplement, 2007"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The primary purpose of the School Crime Supplement (SCS) is to obtain additional information about school-related victimizations so that policymakers; academic researchers; practitioners at the federal, state, and local levels; and special interest groups who are concerned with crime in schools can make informed decisions concerning policies and programs. The SCS asks questions related to students' experiences with, and perceptions of crime and safety at school, including preventive measures employed by schools; students' participation in after school activities; students' perception of school rules and enforcement of these rules; the presence of weapons, drugs, alcohol, and gangs in school;\r\nstudent bullying; hate-related incidents; and attitudinal questions relating to the fear of victimization at school. These responses are linked to the National Crime Victimization Survey (NCVS) survey instrument responses for a more complete understanding of the individual student's circumstances.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR28201.v1",
+                    "title": "National Crime Victimization Survey: School Crime Supplement, 2009"
+                }
+            ],
+            "identifier": "233",
+            "isPartOf": "2432",
+            "issued": "2011-01-21T09:24:37",
             "keyword": [
                 "crime",
                 "crime in schools",
@@ -11907,54 +11901,54 @@
                 "victimization",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-01-21T09:24:37",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2011-01-21T09:24:37",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR28201.v1",
-                    "title": "National Crime Victimization Survey: School Crime Supplement, 2009"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Victimization Survey: School Crime Supplement, 2011",
-            "description": "The primary purpose of the School Crime Supplement (SCS) is to obtain additional information about school-related victimizations so that policymakers; academic researchers; practitioners at the federal, state, and local levels; and special interest groups who are concerned with crime in schools can make informed decisions concerning policies and programs. The SCS asks questions related to students' experiences with, and perceptions of crime and safety at school, including preventive measures employed by schools; students' participation in after school activities; students' perception of school rules and enforcement of these rules; the presence of weapons, drugs, alcohol, and gangs in school;\r\nstudent bullying; hate-related incidents; and attitudinal questions relating to the fear of victimization at school. These responses are linked to the National Crime Victimization Survey (NCVS) survey instrument responses for a more complete understanding of the individual student's circumstances.",
-            "modified": "2013-03-26T10:44:31",
-            "accessLevel": "public",
-            "identifier": "234",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Victimization Survey: School Crime Supplement, 2009"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The primary purpose of the School Crime Supplement (SCS) is to obtain additional information about school-related victimizations so that policymakers; academic researchers; practitioners at the federal, state, and local levels; and special interest groups who are concerned with crime in schools can make informed decisions concerning policies and programs. The SCS asks questions related to students' experiences with, and perceptions of crime and safety at school, including preventive measures employed by schools; students' participation in after school activities; students' perception of school rules and enforcement of these rules; the presence of weapons, drugs, alcohol, and gangs in school;\r\nstudent bullying; hate-related incidents; and attitudinal questions relating to the fear of victimization at school. These responses are linked to the National Crime Victimization Survey (NCVS) survey instrument responses for a more complete understanding of the individual student's circumstances.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR33081.v1",
+                    "title": "National Crime Victimization Survey: School Crime Supplement, 2011"
+                }
+            ],
+            "identifier": "234",
+            "isPartOf": "2432",
+            "issued": "2013-03-26T10:44:31",
             "keyword": [
                 "crime",
                 "crime in schools",
@@ -11978,54 +11972,54 @@
                 "victimization",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-03-26T10:44:31",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2013-03-26T10:44:31",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR33081.v1",
-                    "title": "National Crime Victimization Survey: School Crime Supplement, 2011"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Victimization Survey: Stalking Victimization Supplement, 2006",
-            "description": "The Supplemental Victimization Survey (SVS) was designed to measure\r\nthe prevalence, characteristics, and consequences of nonfatal stalking\r\nso that policymakers, academic researchers, practitioners at the\r\nfederal, state and local levels, and advocates could make informed\r\ndecisions concerning policies and programs. The SVS asks questions\r\nrelated to victims' experiences of unwanted contact or harassing\r\nbehavior on two or more occasions during the previous 12 months. The\r\nsurvey provides information about the following dimensions of stalking\r\nbehavior: relationship of the perpetrator to victim; onset, duration,\r\nand desistance; other crimes and injuries committed against the victim\r\nin conjunction with stalking; victim response; criminal justice\r\nresponse; and cost to victim.  These responses are linked to the National\r\nCrime Victimization Survey (NCVS)\r\nsurvey instrument responses for a more complete understanding of the\r\nstalking victim's circumstances.\r\nThe 2006 SVS was a one-time\r\nsupplement to the annual NCVS to obtain specific information about\r\nstalking victimization on a national level.  This supplement was\r\nsponsored by the Office of Violence Against Women (OVW) in the\r\nUnited States Department of Justice.  Since the SVS is a supplement to the\r\nNCVS, it is conducted under the authority of Title 42, United States\r\nCode, Section 3732. Only Census employees sworn to preserve\r\nconfidentiality may see the completed questionnaires.",
-            "modified": "2009-01-16T11:21:20",
-            "accessLevel": "public",
-            "identifier": "235",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Victimization Survey: School Crime Supplement, 2011"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The Supplemental Victimization Survey (SVS) was designed to measure\r\nthe prevalence, characteristics, and consequences of nonfatal stalking\r\nso that policymakers, academic researchers, practitioners at the\r\nfederal, state and local levels, and advocates could make informed\r\ndecisions concerning policies and programs. The SVS asks questions\r\nrelated to victims' experiences of unwanted contact or harassing\r\nbehavior on two or more occasions during the previous 12 months. The\r\nsurvey provides information about the following dimensions of stalking\r\nbehavior: relationship of the perpetrator to victim; onset, duration,\r\nand desistance; other crimes and injuries committed against the victim\r\nin conjunction with stalking; victim response; criminal justice\r\nresponse; and cost to victim.  These responses are linked to the National\r\nCrime Victimization Survey (NCVS)\r\nsurvey instrument responses for a more complete understanding of the\r\nstalking victim's circumstances.\r\nThe 2006 SVS was a one-time\r\nsupplement to the annual NCVS to obtain specific information about\r\nstalking victimization on a national level.  This supplement was\r\nsponsored by the Office of Violence Against Women (OVW) in the\r\nUnited States Department of Justice.  Since the SVS is a supplement to the\r\nNCVS, it is conducted under the authority of Title 42, United States\r\nCode, Section 3732. Only Census employees sworn to preserve\r\nconfidentiality may see the completed questionnaires.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR20080.v1",
+                    "title": "National Crime Victimization Survey: Stalking Victimization Supplement, 2006"
+                }
+            ],
+            "identifier": "235",
+            "isPartOf": "2432",
+            "issued": "2009-01-15T17:23:29",
             "keyword": [
                 "crime",
                 "crime rates",
@@ -12035,54 +12029,54 @@
                 "victimization",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2009-01-16T11:21:20",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2009-01-15T17:23:29",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR20080.v1",
-                    "title": "National Crime Victimization Survey: Stalking Victimization Supplement, 2006"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Victimization Survey: Unbounded Data, 1999",
-            "description": "The National Crime Victimization Survey: Unbounded Data\r\n (also referred to as the All Rotations Data) are now being made\r\n available to the public for analytic use. These data differ from the\r\n \"regular\" National Crime Victimization Survey (NCVS) data in that they\r\n contain the first interview with respondents. The National Crime\r\n Victimization Survey Series, previously called the National Crime\r\n Surveys (NCS), has been collecting data on personal and household\r\n victimization through an ongoing survey of a nationally-representative\r\n sample of residential addresses since 1973. The NCVS was designed with\r\n four primary objectives: (1) to develop detailed information about the\r\n victims and consequences of crime, (2) to estimate the number and\r\n types of crimes not reported to the police, (3) to provide uniform\r\n measures of selected types of crimes, and (4) to permit comparisons\r\n over time and types of areas. The survey categorizes crimes as\r\n \"personal\" or \"property.\" Personal crimes include rape and sexual\r\n attack, robbery, aggravated and simple assault, and\r\n purse-snatching/pocket-picking, while property crimes include\r\n burglary, theft, motor vehicle theft, and vandalism. Each respondent\r\n is asked a series of screen questions designed to determine whether\r\n she or he was victimized during the six-month period preceding the\r\n first day of the month of the interview. A \"household respondent\" is\r\n also asked to report on crimes against the household as a whole (e.g.,\r\n burglary, motor vehicle theft). The data include type of crime, month,\r\n time, and location of the crime, relationship between victim and\r\n offender, characteristics of the offender, self-protective actions\r\n taken by the victim during the incident and results of those actions,\r\n consequences of the victimization, type of property lost, whether the\r\n crime was reported to police and reasons for reporting or not\r\n reporting, and offender use of weapons, drugs, and alcohol. Basic\r\n demographic information such as age, race, gender, and income is also\r\ncollected to enable analysis of crime by various subpopulations.",
-            "modified": "2006-06-23T00:00:00",
-            "accessLevel": "public",
-            "identifier": "236",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Victimization Survey: Stalking Victimization Supplement, 2006"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Crime Victimization Survey: Unbounded Data\r\n (also referred to as the All Rotations Data) are now being made\r\n available to the public for analytic use. These data differ from the\r\n \"regular\" National Crime Victimization Survey (NCVS) data in that they\r\n contain the first interview with respondents. The National Crime\r\n Victimization Survey Series, previously called the National Crime\r\n Surveys (NCS), has been collecting data on personal and household\r\n victimization through an ongoing survey of a nationally-representative\r\n sample of residential addresses since 1973. The NCVS was designed with\r\n four primary objectives: (1) to develop detailed information about the\r\n victims and consequences of crime, (2) to estimate the number and\r\n types of crimes not reported to the police, (3) to provide uniform\r\n measures of selected types of crimes, and (4) to permit comparisons\r\n over time and types of areas. The survey categorizes crimes as\r\n \"personal\" or \"property.\" Personal crimes include rape and sexual\r\n attack, robbery, aggravated and simple assault, and\r\n purse-snatching/pocket-picking, while property crimes include\r\n burglary, theft, motor vehicle theft, and vandalism. Each respondent\r\n is asked a series of screen questions designed to determine whether\r\n she or he was victimized during the six-month period preceding the\r\n first day of the month of the interview. A \"household respondent\" is\r\n also asked to report on crimes against the household as a whole (e.g.,\r\n burglary, motor vehicle theft). The data include type of crime, month,\r\n time, and location of the crime, relationship between victim and\r\n offender, characteristics of the offender, self-protective actions\r\n taken by the victim during the incident and results of those actions,\r\n consequences of the victimization, type of property lost, whether the\r\n crime was reported to police and reasons for reporting or not\r\n reporting, and offender use of weapons, drugs, and alcohol. Basic\r\n demographic information such as age, race, gender, and income is also\r\ncollected to enable analysis of crime by various subpopulations.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR04444.v1",
+                    "title": "National Crime Victimization Survey: Unbounded Data, 1999"
+                }
+            ],
+            "identifier": "236",
+            "isPartOf": "2432",
+            "issued": "2006-06-23T00:00:00",
             "keyword": [
                 "assault",
                 "auto theft",
@@ -12103,54 +12097,54 @@
                 "victimization",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
-            ],
-            "programCode": [
-                "011:061"
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2006-06-23T00:00:00",
             "language": [
                 "eng"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR04444.v1",
-                    "title": "National Crime Victimization Survey: Unbounded Data, 1999"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Victimization Survey: Unbounded Data, 2000",
-            "description": "The National Crime Victimization Survey: Unbounded Data\r\n (also referred to as the All Rotations Data) are now being made\r\n available to the public for analytic use. These data differ from the\r\n \"regular\" National Crime Victimization Survey (NCVS) data in that they\r\n contain the first interview with respondents. The National Crime\r\n Victimization Survey Series, previously called the National Crime\r\n Surveys (NCS), has been collecting data on personal and household\r\n victimization through an ongoing survey of a nationally-representative\r\n sample of residential addresses since 1973. The NCVS was designed with\r\n four primary objectives: (1) to develop detailed information about the\r\n victims and consequences of crime, (2) to estimate the number and\r\n types of crimes not reported to the police, (3) to provide uniform\r\n measures of selected types of crimes, and (4) to permit comparisons\r\n over time and types of areas. The survey categorizes crimes as\r\n \"personal\" or \"property.\" Personal crimes include rape and sexual\r\n attack, robbery, aggravated and simple assault, and\r\n purse-snatching/pocket-picking, while property crimes include\r\n burglary, theft, motor vehicle theft, and vandalism. Each respondent\r\n is asked a series of screen questions designed to determine whether\r\n she or he was victimized during the six-month period preceding the\r\n first day of the month of the interview. A \"household respondent\" is\r\n also asked to report on crimes against the household as a whole (e.g.,\r\n burglary, motor vehicle theft). The data include type of crime, month,\r\n time, and location of the crime, relationship between victim and\r\n offender, characteristics of the offender, self-protective actions\r\n taken by the victim during the incident and results of those actions,\r\n consequences of the victimization, type of property lost, whether the\r\n crime was reported to police and reasons for reporting or not\r\n reporting, and offender use of weapons, drugs, and alcohol. Basic\r\n demographic information such as age, race, gender, and income is also\r\ncollected to enable analysis of crime by various subpopulations.",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "modified": "2006-06-23T00:00:00",
-            "accessLevel": "public",
-            "identifier": "237",
+            "programCode": [
+                "011:061"
+            ],
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Victimization Survey: Unbounded Data, 1999"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Crime Victimization Survey: Unbounded Data\r\n (also referred to as the All Rotations Data) are now being made\r\n available to the public for analytic use. These data differ from the\r\n \"regular\" National Crime Victimization Survey (NCVS) data in that they\r\n contain the first interview with respondents. The National Crime\r\n Victimization Survey Series, previously called the National Crime\r\n Surveys (NCS), has been collecting data on personal and household\r\n victimization through an ongoing survey of a nationally-representative\r\n sample of residential addresses since 1973. The NCVS was designed with\r\n four primary objectives: (1) to develop detailed information about the\r\n victims and consequences of crime, (2) to estimate the number and\r\n types of crimes not reported to the police, (3) to provide uniform\r\n measures of selected types of crimes, and (4) to permit comparisons\r\n over time and types of areas. The survey categorizes crimes as\r\n \"personal\" or \"property.\" Personal crimes include rape and sexual\r\n attack, robbery, aggravated and simple assault, and\r\n purse-snatching/pocket-picking, while property crimes include\r\n burglary, theft, motor vehicle theft, and vandalism. Each respondent\r\n is asked a series of screen questions designed to determine whether\r\n she or he was victimized during the six-month period preceding the\r\n first day of the month of the interview. A \"household respondent\" is\r\n also asked to report on crimes against the household as a whole (e.g.,\r\n burglary, motor vehicle theft). The data include type of crime, month,\r\n time, and location of the crime, relationship between victim and\r\n offender, characteristics of the offender, self-protective actions\r\n taken by the victim during the incident and results of those actions,\r\n consequences of the victimization, type of property lost, whether the\r\n crime was reported to police and reasons for reporting or not\r\n reporting, and offender use of weapons, drugs, and alcohol. Basic\r\n demographic information such as age, race, gender, and income is also\r\ncollected to enable analysis of crime by various subpopulations.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR04445.v1",
+                    "title": "National Crime Victimization Survey: Unbounded Data, 2000"
+                }
+            ],
+            "identifier": "237",
+            "isPartOf": "2432",
+            "issued": "2006-06-23T00:00:00",
             "keyword": [
                 "assault",
                 "auto theft",
@@ -12171,54 +12165,54 @@
                 "victimization",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
-            ],
-            "programCode": [
-                "011:061"
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2006-06-23T00:00:00",
             "language": [
                 "eng"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR04445.v1",
-                    "title": "National Crime Victimization Survey: Unbounded Data, 2000"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Victimization Survey: Unbounded Data, 2001",
-            "description": "The National Crime Victimization Survey: Unbounded Data\r\n (also referred to as the All Rotations Data) are now being made\r\n available to the public for analytic use. These data differ from the\r\n \"regular\" National Crime Victimization Survey (NCVS) data in that they\r\n contain the first interview with respondents. The National Crime\r\n Victimization Survey Series, previously called the National Crime\r\n Surveys (NCS), has been collecting data on personal and household\r\n victimization through an ongoing survey of a nationally-representative\r\n sample of residential addresses since 1973. The NCVS was designed with\r\n four primary objectives: (1) to develop detailed information about the\r\n victims and consequences of crime, (2) to estimate the number and\r\n types of crimes not reported to the police, (3) to provide uniform\r\n measures of selected types of crimes, and (4) to permit comparisons\r\n over time and types of areas. The survey categorizes crimes as\r\n \"personal\" or \"property.\" Personal crimes include rape and sexual\r\n attack, robbery, aggravated and simple assault, and\r\n purse-snatching/pocket-picking, while property crimes include\r\n burglary, theft, motor vehicle theft, and vandalism. Each respondent\r\n is asked a series of screen questions designed to determine whether\r\n she or he was victimized during the six-month period preceding the\r\n first day of the month of the interview. A \"household respondent\" is\r\n also asked to report on crimes against the household as a whole (e.g.,\r\n burglary, motor vehicle theft). The data include type of crime, month,\r\n time, and location of the crime, relationship between victim and\r\n offender, characteristics of the offender, self-protective actions\r\n taken by the victim during the incident and results of those actions,\r\n consequences of the victimization, type of property lost, whether the\r\n crime was reported to police and reasons for reporting or not\r\n reporting, and offender use of weapons, drugs, and alcohol. Basic\r\n demographic information such as age, race, gender, and income is also\r\ncollected to enable analysis of crime by various subpopulations.",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "modified": "2006-06-23T00:00:00",
-            "accessLevel": "public",
-            "identifier": "238",
+            "programCode": [
+                "011:061"
+            ],
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Victimization Survey: Unbounded Data, 2000"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Crime Victimization Survey: Unbounded Data\r\n (also referred to as the All Rotations Data) are now being made\r\n available to the public for analytic use. These data differ from the\r\n \"regular\" National Crime Victimization Survey (NCVS) data in that they\r\n contain the first interview with respondents. The National Crime\r\n Victimization Survey Series, previously called the National Crime\r\n Surveys (NCS), has been collecting data on personal and household\r\n victimization through an ongoing survey of a nationally-representative\r\n sample of residential addresses since 1973. The NCVS was designed with\r\n four primary objectives: (1) to develop detailed information about the\r\n victims and consequences of crime, (2) to estimate the number and\r\n types of crimes not reported to the police, (3) to provide uniform\r\n measures of selected types of crimes, and (4) to permit comparisons\r\n over time and types of areas. The survey categorizes crimes as\r\n \"personal\" or \"property.\" Personal crimes include rape and sexual\r\n attack, robbery, aggravated and simple assault, and\r\n purse-snatching/pocket-picking, while property crimes include\r\n burglary, theft, motor vehicle theft, and vandalism. Each respondent\r\n is asked a series of screen questions designed to determine whether\r\n she or he was victimized during the six-month period preceding the\r\n first day of the month of the interview. A \"household respondent\" is\r\n also asked to report on crimes against the household as a whole (e.g.,\r\n burglary, motor vehicle theft). The data include type of crime, month,\r\n time, and location of the crime, relationship between victim and\r\n offender, characteristics of the offender, self-protective actions\r\n taken by the victim during the incident and results of those actions,\r\n consequences of the victimization, type of property lost, whether the\r\n crime was reported to police and reasons for reporting or not\r\n reporting, and offender use of weapons, drugs, and alcohol. Basic\r\n demographic information such as age, race, gender, and income is also\r\ncollected to enable analysis of crime by various subpopulations.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR04446.v1",
+                    "title": "National Crime Victimization Survey: Unbounded Data, 2001"
+                }
+            ],
+            "identifier": "238",
+            "isPartOf": "2432",
+            "issued": "2006-06-23T00:00:00",
             "keyword": [
                 "assault",
                 "auto theft",
@@ -12239,54 +12233,54 @@
                 "victimization",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2006-06-23T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2006-06-23T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR04446.v1",
-                    "title": "National Crime Victimization Survey: Unbounded Data, 2001"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Victimization Survey: Unbounded Data, 2002",
-            "description": "The National Crime Victimization Survey: Unbounded Data\r\n(also referred to as the All Rotations Data) are now being made\r\navailable to the public for analytic use. These data differ from the\r\n\"regular\" National Crime Victimization Survey (NCVS) data in that they\r\ncontain the first interview with respondents. The National Crime\r\nVictimization Survey Series, previously called the National Crime\r\nSurveys (NCS), has been collecting data on personal and household\r\nvictimization through an ongoing survey of a nationally-representative\r\nsample of residential addresses since 1973. The NCVS was designed with\r\nfour primary objectives: (1) to develop detailed information about the\r\nvictims and consequences of crime, (2) to estimate the number and\r\ntypes of crimes not reported to the police, (3) to provide uniform\r\nmeasures of selected types of crimes, and (4) to permit comparisons\r\nover time and types of areas. The survey categorizes crimes as\r\n\"personal\" or \"property.\" Personal crimes include rape and sexual\r\nattack, robbery, aggravated and simple assault, and\r\npurse-snatching/pocket-picking, while property crimes include\r\nburglary, theft, motor vehicle theft, and vandalism. Each respondent\r\nis asked a series of screen questions designed to determine whether\r\nshe or he was victimized during the six-month period preceding the\r\nfirst day of the month of the interview. A \"household respondent\" is\r\nalso asked to report on crimes against the household as a whole (e.g.,\r\nburglary, motor vehicle theft). The data include type of crime, month,\r\ntime, and location of the crime, relationship between victim and\r\noffender, characteristics of the offender, self-protective actions\r\ntaken by the victim during the incident and results of those actions,\r\nconsequences of the victimization, type of property lost, whether the\r\ncrime was reported to police and reasons for reporting or not\r\nreporting, and offender use of weapons, drugs, and alcohol. Basic\r\ndemographic information such as age, race, gender, and income is also\r\ncollected to enable analysis of crime by various subpopulations.",
-            "modified": "2006-06-22T00:00:00",
-            "accessLevel": "public",
-            "identifier": "239",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Victimization Survey: Unbounded Data, 2001"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Crime Victimization Survey: Unbounded Data\r\n(also referred to as the All Rotations Data) are now being made\r\navailable to the public for analytic use. These data differ from the\r\n\"regular\" National Crime Victimization Survey (NCVS) data in that they\r\ncontain the first interview with respondents. The National Crime\r\nVictimization Survey Series, previously called the National Crime\r\nSurveys (NCS), has been collecting data on personal and household\r\nvictimization through an ongoing survey of a nationally-representative\r\nsample of residential addresses since 1973. The NCVS was designed with\r\nfour primary objectives: (1) to develop detailed information about the\r\nvictims and consequences of crime, (2) to estimate the number and\r\ntypes of crimes not reported to the police, (3) to provide uniform\r\nmeasures of selected types of crimes, and (4) to permit comparisons\r\nover time and types of areas. The survey categorizes crimes as\r\n\"personal\" or \"property.\" Personal crimes include rape and sexual\r\nattack, robbery, aggravated and simple assault, and\r\npurse-snatching/pocket-picking, while property crimes include\r\nburglary, theft, motor vehicle theft, and vandalism. Each respondent\r\nis asked a series of screen questions designed to determine whether\r\nshe or he was victimized during the six-month period preceding the\r\nfirst day of the month of the interview. A \"household respondent\" is\r\nalso asked to report on crimes against the household as a whole (e.g.,\r\nburglary, motor vehicle theft). The data include type of crime, month,\r\ntime, and location of the crime, relationship between victim and\r\noffender, characteristics of the offender, self-protective actions\r\ntaken by the victim during the incident and results of those actions,\r\nconsequences of the victimization, type of property lost, whether the\r\ncrime was reported to police and reasons for reporting or not\r\nreporting, and offender use of weapons, drugs, and alcohol. Basic\r\ndemographic information such as age, race, gender, and income is also\r\ncollected to enable analysis of crime by various subpopulations.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR04447.v1",
+                    "title": "National Crime Victimization Survey: Unbounded Data, 2002"
+                }
+            ],
+            "identifier": "239",
+            "isPartOf": "2432",
+            "issued": "2006-06-22T00:00:00",
             "keyword": [
                 "assault",
                 "auto theft",
@@ -12307,54 +12301,54 @@
                 "victimization",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
-            ],
-            "programCode": [
-                "011:061"
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2006-06-22T00:00:00",
             "language": [
                 "eng"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR04447.v1",
-                    "title": "National Crime Victimization Survey: Unbounded Data, 2002"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Victimization Survey: Unbounded Data, 2003",
-            "description": "The National Crime Victimization Survey: Unbounded Data\r\n (also referred to as the All Rotations Data) are now being made\r\n available to the public for analytic use. These data differ from the\r\n \"regular\" National Crime Victimization Survey (NCVS) data in that they\r\n contain the first interview with respondents. The National Crime\r\n Victimization Survey Series, previously called the National Crime\r\n Surveys (NCS), has been collecting data on personal and household\r\n victimization through an ongoing survey of a nationally-representative\r\n sample of residential addresses since 1973. The NCVS was designed with\r\n four primary objectives: (1) to develop detailed information about the\r\n victims and consequences of crime, (2) to estimate the number and\r\n types of crimes not reported to the police, (3) to provide uniform\r\n measures of selected types of crimes, and (4) to permit comparisons\r\n over time and types of areas. The survey categorizes crimes as\r\n \"personal\" or \"property.\" Personal crimes include rape and sexual\r\n attack, robbery, aggravated and simple assault, and\r\n purse-snatching/pocket-picking, while property crimes include\r\n burglary, theft, motor vehicle theft, and vandalism. Each respondent\r\n is asked a series of screen questions designed to determine whether\r\n she or he was victimized during the six-month period preceding the\r\n first day of the month of the interview. A \"household respondent\" is\r\n also asked to report on crimes against the household as a whole (e.g.,\r\n burglary, motor vehicle theft). The data include type of crime, month,\r\n time, and location of the crime, relationship between victim and\r\n offender, characteristics of the offender, self-protective actions\r\n taken by the victim during the incident and results of those actions,\r\n consequences of the victimization, type of property lost, whether the\r\n crime was reported to police and reasons for reporting or not\r\n reporting, and offender use of weapons, drugs, and alcohol. Basic\r\n demographic information such as age, race, gender, and income is also\r\ncollected to enable analysis of crime by various subpopulations.",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "modified": "2006-06-22T00:00:00",
-            "accessLevel": "public",
-            "identifier": "240",
+            "programCode": [
+                "011:061"
+            ],
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Victimization Survey: Unbounded Data, 2002"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Crime Victimization Survey: Unbounded Data\r\n (also referred to as the All Rotations Data) are now being made\r\n available to the public for analytic use. These data differ from the\r\n \"regular\" National Crime Victimization Survey (NCVS) data in that they\r\n contain the first interview with respondents. The National Crime\r\n Victimization Survey Series, previously called the National Crime\r\n Surveys (NCS), has been collecting data on personal and household\r\n victimization through an ongoing survey of a nationally-representative\r\n sample of residential addresses since 1973. The NCVS was designed with\r\n four primary objectives: (1) to develop detailed information about the\r\n victims and consequences of crime, (2) to estimate the number and\r\n types of crimes not reported to the police, (3) to provide uniform\r\n measures of selected types of crimes, and (4) to permit comparisons\r\n over time and types of areas. The survey categorizes crimes as\r\n \"personal\" or \"property.\" Personal crimes include rape and sexual\r\n attack, robbery, aggravated and simple assault, and\r\n purse-snatching/pocket-picking, while property crimes include\r\n burglary, theft, motor vehicle theft, and vandalism. Each respondent\r\n is asked a series of screen questions designed to determine whether\r\n she or he was victimized during the six-month period preceding the\r\n first day of the month of the interview. A \"household respondent\" is\r\n also asked to report on crimes against the household as a whole (e.g.,\r\n burglary, motor vehicle theft). The data include type of crime, month,\r\n time, and location of the crime, relationship between victim and\r\n offender, characteristics of the offender, self-protective actions\r\n taken by the victim during the incident and results of those actions,\r\n consequences of the victimization, type of property lost, whether the\r\n crime was reported to police and reasons for reporting or not\r\n reporting, and offender use of weapons, drugs, and alcohol. Basic\r\n demographic information such as age, race, gender, and income is also\r\ncollected to enable analysis of crime by various subpopulations.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR04448.v1",
+                    "title": "National Crime Victimization Survey: Unbounded Data, 2003"
+                }
+            ],
+            "identifier": "240",
+            "isPartOf": "2432",
+            "issued": "2006-06-22T00:00:00",
             "keyword": [
                 "assault",
                 "auto theft",
@@ -12375,54 +12369,54 @@
                 "victimization",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2006-06-22T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2006-06-22T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR04448.v1",
-                    "title": "National Crime Victimization Survey: Unbounded Data, 2003"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Victimization Survey: Unbounded Data, 2004",
-            "description": "The National Crime Victimization Survey: Unbounded Data\r\n (also referred to as the All Rotations Data) are now being made\r\n available to the public for analytic use. These data differ from the\r\n \"regular\" National Crime Victimization Survey (NCVS) data in that they\r\n contain the first interview with respondents. The National Crime\r\n Victimization Survey Series, previously called the National Crime\r\n Surveys (NCS), has been collecting data on personal and household\r\n victimization through an ongoing survey of a nationally-representative\r\n sample of residential addresses since 1973. The NCVS was designed with\r\n four primary objectives: (1) to develop detailed information about the\r\n victims and consequences of crime, (2) to estimate the number and\r\n types of crimes not reported to the police, (3) to provide uniform\r\n measures of selected types of crimes, and (4) to permit comparisons\r\n over time and types of areas. The survey categorizes crimes as\r\n \"personal\" or \"property.\" Personal crimes include rape and sexual\r\n attack, robbery, aggravated and simple assault, and\r\n purse-snatching/pocket-picking, while property crimes include\r\n burglary, theft, motor vehicle theft, and vandalism. Each respondent\r\n is asked a series of screen questions designed to determine whether\r\n she or he was victimized during the six-month period preceding the\r\n first day of the month of the interview. A \"household respondent\" is\r\n also asked to report on crimes against the household as a whole (e.g.,\r\n burglary, motor vehicle theft). The data include type of crime, month,\r\n time, and location of the crime, relationship between victim and\r\n offender, characteristics of the offender, self-protective actions\r\n taken by the victim during the incident and results of those actions,\r\n consequences of the victimization, type of property lost, whether the\r\n crime was reported to police and reasons for reporting or not\r\n reporting, and offender use of weapons, drugs, and alcohol. Basic\r\n demographic information such as age, race, gender, and income is also\r\ncollected to enable analysis of crime by various subpopulations.",
-            "modified": "2007-05-03T00:00:00",
-            "accessLevel": "public",
-            "identifier": "241",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Victimization Survey: Unbounded Data, 2003"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Crime Victimization Survey: Unbounded Data\r\n (also referred to as the All Rotations Data) are now being made\r\n available to the public for analytic use. These data differ from the\r\n \"regular\" National Crime Victimization Survey (NCVS) data in that they\r\n contain the first interview with respondents. The National Crime\r\n Victimization Survey Series, previously called the National Crime\r\n Surveys (NCS), has been collecting data on personal and household\r\n victimization through an ongoing survey of a nationally-representative\r\n sample of residential addresses since 1973. The NCVS was designed with\r\n four primary objectives: (1) to develop detailed information about the\r\n victims and consequences of crime, (2) to estimate the number and\r\n types of crimes not reported to the police, (3) to provide uniform\r\n measures of selected types of crimes, and (4) to permit comparisons\r\n over time and types of areas. The survey categorizes crimes as\r\n \"personal\" or \"property.\" Personal crimes include rape and sexual\r\n attack, robbery, aggravated and simple assault, and\r\n purse-snatching/pocket-picking, while property crimes include\r\n burglary, theft, motor vehicle theft, and vandalism. Each respondent\r\n is asked a series of screen questions designed to determine whether\r\n she or he was victimized during the six-month period preceding the\r\n first day of the month of the interview. A \"household respondent\" is\r\n also asked to report on crimes against the household as a whole (e.g.,\r\n burglary, motor vehicle theft). The data include type of crime, month,\r\n time, and location of the crime, relationship between victim and\r\n offender, characteristics of the offender, self-protective actions\r\n taken by the victim during the incident and results of those actions,\r\n consequences of the victimization, type of property lost, whether the\r\n crime was reported to police and reasons for reporting or not\r\n reporting, and offender use of weapons, drugs, and alcohol. Basic\r\n demographic information such as age, race, gender, and income is also\r\ncollected to enable analysis of crime by various subpopulations.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR04449.v2",
+                    "title": "National Crime Victimization Survey: Unbounded Data, 2004"
+                }
+            ],
+            "identifier": "241",
+            "isPartOf": "2432",
+            "issued": "2006-06-22T00:00:00",
             "keyword": [
                 "assault",
                 "auto theft",
@@ -12443,54 +12437,54 @@
                 "victimization",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2007-05-03T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2006-06-22T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR04449.v2",
-                    "title": "National Crime Victimization Survey: Unbounded Data, 2004"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Victimization Survey: Unbounded Data, 2005 [Record-Type Files]",
-            "description": "The National Crime Victimization Survey: Unbounded Data\r\n(also referred to as the All Rotations Data) are now being made\r\navailable to the public for analytic use. These data differ from the\r\n\"regular\" National Crime Victimization Survey (NCVS) data in that they\r\ncontain the first interview with respondents. The National Crime\r\nVictimization Survey Series, previously called the National Crime\r\nSurveys (NCS), has been collecting data on personal and household\r\nvictimization through an ongoing survey of a nationally-representative\r\nsample of residential addresses since 1973. The NCVS was designed with\r\nfour primary objectives: (1) to develop detailed information about the\r\nvictims and consequences of crime, (2) to estimate the number and\r\ntypes of crimes not reported to the police, (3) to provide uniform\r\nmeasures of selected types of crimes, and (4) to permit comparisons\r\nover time and types of areas. The survey categorizes crimes as\r\n\"personal\" or \"property.\" Personal crimes include rape and sexual\r\nattack, robbery, aggravated and simple assault, and\r\npurse-snatching/pocket-picking, while property crimes include\r\nburglary, theft, motor vehicle theft, and vandalism. Each respondent\r\nis asked a series of screen questions designed to determine whether\r\nshe or he was victimized during the six-month period preceding the\r\nfirst day of the month of the interview. A \"household respondent\" is\r\nalso asked to report on crimes against the household as a whole (e.g.,\r\nburglary, motor vehicle theft). The data include type of crime, month,\r\ntime, and location of the crime, relationship between victim and\r\noffender, characteristics of the offender, self-protective actions\r\ntaken by the victim during the incident and results of those actions,\r\nconsequences of the victimization, type of property lost, whether the\r\ncrime was reported to police and reasons for reporting or not\r\nreporting, and offender use of weapons, drugs, and alcohol. Basic\r\ndemographic information such as age, race, gender, and income is also\r\ncollected to enable analysis of crime by various subpopulations.",
-            "modified": "2011-06-03T09:47:06",
-            "accessLevel": "public",
-            "identifier": "242",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Victimization Survey: Unbounded Data, 2004"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Crime Victimization Survey: Unbounded Data\r\n(also referred to as the All Rotations Data) are now being made\r\navailable to the public for analytic use. These data differ from the\r\n\"regular\" National Crime Victimization Survey (NCVS) data in that they\r\ncontain the first interview with respondents. The National Crime\r\nVictimization Survey Series, previously called the National Crime\r\nSurveys (NCS), has been collecting data on personal and household\r\nvictimization through an ongoing survey of a nationally-representative\r\nsample of residential addresses since 1973. The NCVS was designed with\r\nfour primary objectives: (1) to develop detailed information about the\r\nvictims and consequences of crime, (2) to estimate the number and\r\ntypes of crimes not reported to the police, (3) to provide uniform\r\nmeasures of selected types of crimes, and (4) to permit comparisons\r\nover time and types of areas. The survey categorizes crimes as\r\n\"personal\" or \"property.\" Personal crimes include rape and sexual\r\nattack, robbery, aggravated and simple assault, and\r\npurse-snatching/pocket-picking, while property crimes include\r\nburglary, theft, motor vehicle theft, and vandalism. Each respondent\r\nis asked a series of screen questions designed to determine whether\r\nshe or he was victimized during the six-month period preceding the\r\nfirst day of the month of the interview. A \"household respondent\" is\r\nalso asked to report on crimes against the household as a whole (e.g.,\r\nburglary, motor vehicle theft). The data include type of crime, month,\r\ntime, and location of the crime, relationship between victim and\r\noffender, characteristics of the offender, self-protective actions\r\ntaken by the victim during the incident and results of those actions,\r\nconsequences of the victimization, type of property lost, whether the\r\ncrime was reported to police and reasons for reporting or not\r\nreporting, and offender use of weapons, drugs, and alcohol. Basic\r\ndemographic information such as age, race, gender, and income is also\r\ncollected to enable analysis of crime by various subpopulations.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR22341.v1",
+                    "title": "National Crime Victimization Survey: Unbounded Data, 2005 [Record-Type Files]"
+                }
+            ],
+            "identifier": "242",
+            "isPartOf": "2432",
+            "issued": "2011-06-03T09:47:06",
             "keyword": [
                 "assault",
                 "auto theft",
@@ -12511,54 +12505,54 @@
                 "victimization",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-06-03T09:47:06",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2011-06-03T09:47:06",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR22341.v1",
-                    "title": "National Crime Victimization Survey: Unbounded Data, 2005 [Record-Type Files]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Victimization Survey: Unbounded Data, 2006 [Record-Type Files]",
-            "description": "The National Crime Victimization Survey: Unbounded Data\r\n(also referred to as the All Rotations Data) are now being made\r\navailable to the public for analytic use. These data differ from the\r\n\"regular\" National Crime Victimization Survey (NCVS) data in that they\r\ncontain the first interview with respondents. The National Crime\r\nVictimization Survey Series, previously called the National Crime\r\nSurveys (NCS), has been collecting data on personal and household\r\nvictimization through an ongoing survey of a nationally-representative\r\nsample of residential addresses since 1973. The NCVS was designed with\r\nfour primary objectives: (1) to develop detailed information about the\r\nvictims and consequences of crime, (2) to estimate the number and\r\ntypes of crimes not reported to the police, (3) to provide uniform\r\nmeasures of selected types of crimes, and (4) to permit comparisons\r\nover time and types of areas. The survey categorizes crimes as\r\n\"personal\" or \"property.\" Personal crimes include rape and sexual\r\nattack, robbery, aggravated and simple assault, and\r\npurse-snatching/pocket-picking, while property crimes include\r\nburglary, theft, motor vehicle theft, and vandalism. Each respondent\r\nis asked a series of screen questions designed to determine whether\r\nshe or he was victimized during the six-month period preceding the\r\nfirst day of the month of the interview. A \"household respondent\" is\r\nalso asked to report on crimes against the household as a whole (e.g.,\r\nburglary, motor vehicle theft). The data include type of crime, month,\r\ntime, and location of the crime, relationship between victim and\r\noffender, characteristics of the offender, self-protective actions\r\ntaken by the victim during the incident and results of those actions,\r\nconsequences of the victimization, type of property lost, whether the\r\ncrime was reported to police and reasons for reporting or not\r\nreporting, and offender use of weapons, drugs, and alcohol. Basic\r\ndemographic information such as age, race, gender, and income is also\r\ncollected to enable analysis of crime by various subpopulations.",
-            "modified": "2011-06-03T10:19:56",
-            "accessLevel": "public",
-            "identifier": "243",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Victimization Survey: Unbounded Data, 2005 [Record-Type Files]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Crime Victimization Survey: Unbounded Data\r\n(also referred to as the All Rotations Data) are now being made\r\navailable to the public for analytic use. These data differ from the\r\n\"regular\" National Crime Victimization Survey (NCVS) data in that they\r\ncontain the first interview with respondents. The National Crime\r\nVictimization Survey Series, previously called the National Crime\r\nSurveys (NCS), has been collecting data on personal and household\r\nvictimization through an ongoing survey of a nationally-representative\r\nsample of residential addresses since 1973. The NCVS was designed with\r\nfour primary objectives: (1) to develop detailed information about the\r\nvictims and consequences of crime, (2) to estimate the number and\r\ntypes of crimes not reported to the police, (3) to provide uniform\r\nmeasures of selected types of crimes, and (4) to permit comparisons\r\nover time and types of areas. The survey categorizes crimes as\r\n\"personal\" or \"property.\" Personal crimes include rape and sexual\r\nattack, robbery, aggravated and simple assault, and\r\npurse-snatching/pocket-picking, while property crimes include\r\nburglary, theft, motor vehicle theft, and vandalism. Each respondent\r\nis asked a series of screen questions designed to determine whether\r\nshe or he was victimized during the six-month period preceding the\r\nfirst day of the month of the interview. A \"household respondent\" is\r\nalso asked to report on crimes against the household as a whole (e.g.,\r\nburglary, motor vehicle theft). The data include type of crime, month,\r\ntime, and location of the crime, relationship between victim and\r\noffender, characteristics of the offender, self-protective actions\r\ntaken by the victim during the incident and results of those actions,\r\nconsequences of the victimization, type of property lost, whether the\r\ncrime was reported to police and reasons for reporting or not\r\nreporting, and offender use of weapons, drugs, and alcohol. Basic\r\ndemographic information such as age, race, gender, and income is also\r\ncollected to enable analysis of crime by various subpopulations.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24644.v1",
+                    "title": "National Crime Victimization Survey: Unbounded Data, 2006 [Record-Type Files]"
+                }
+            ],
+            "identifier": "243",
+            "isPartOf": "2432",
+            "issued": "2011-06-03T10:10:19",
             "keyword": [
                 "assault",
                 "auto theft",
@@ -12579,54 +12573,54 @@
                 "victimization",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-06-03T10:19:56",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2011-06-03T10:10:19",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24644.v1",
-                    "title": "National Crime Victimization Survey: Unbounded Data, 2006 [Record-Type Files]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Incident-Based Reporting System, 2011: Extract Files",
-            "description": "The National Incident-Based Reporting System (NIBRS) is a\r\npart of the Uniform Crime Reporting Program (UCR), administered by the\r\nFederal Bureau of Investigation (FBI). The extract files version of\r\nNIBRS was created to simplify working with NIBRS data. Data management\r\nissues with NIBRS are significant, especially when two or more segment\r\nlevels are being merged. These issues require skills separate from\r\ndata analysis. NIBRS data as formatted by the FBI are stored in a\r\nsingle file. These data are organized by various segment levels\r\n(record types). There are six main segment levels: administrative,\r\noffense, property, victim, offender, and arrestee. Each segment level\r\nhas a different length and layout. There are other segment levels that\r\noccur with less frequency than the six main levels. Significant\r\ncomputing resources are necessary to work with the data in its\r\nsingle-file format. In addition, the user must be sophisticated in\r\nworking with data in complex file types. For these reasons and the\r\ndesire to facilitate the use of NIBRS data, ICPSR created the extract\r\nfiles. The data are not a representative sample of crime in the United\r\nStates.",
-            "modified": "2018-10-15T15:59:31",
-            "accessLevel": "public",
-            "identifier": "244",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Victimization Survey: Unbounded Data, 2006 [Record-Type Files]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Incident-Based Reporting System (NIBRS) is a\r\npart of the Uniform Crime Reporting Program (UCR), administered by the\r\nFederal Bureau of Investigation (FBI). The extract files version of\r\nNIBRS was created to simplify working with NIBRS data. Data management\r\nissues with NIBRS are significant, especially when two or more segment\r\nlevels are being merged. These issues require skills separate from\r\ndata analysis. NIBRS data as formatted by the FBI are stored in a\r\nsingle file. These data are organized by various segment levels\r\n(record types). There are six main segment levels: administrative,\r\noffense, property, victim, offender, and arrestee. Each segment level\r\nhas a different length and layout. There are other segment levels that\r\noccur with less frequency than the six main levels. Significant\r\ncomputing resources are necessary to work with the data in its\r\nsingle-file format. In addition, the user must be sophisticated in\r\nworking with data in complex file types. For these reasons and the\r\ndesire to facilitate the use of NIBRS data, ICPSR created the extract\r\nfiles. The data are not a representative sample of crime in the United\r\nStates.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR34603.v2",
+                    "title": "National Incident-Based Reporting System, 2011: Extract Files"
+                }
+            ],
+            "identifier": "244",
+            "isPartOf": "2433",
+            "issued": "2014-01-03T15:41:48",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -12641,54 +12635,54 @@
                 "victims",
                 "violent crime"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2018-10-15T15:59:31",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2433",
-            "dataQuality": false,
-            "issued": "2014-01-03T15:41:48",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR34603.v2",
-                    "title": "National Incident-Based Reporting System, 2011: Extract Files"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Jail Census, 1970",
-            "description": "This census provides information on county and municipal \r\n jails facilities in the United States and their administration. For\r\n all jails, the data \r\n include number of prisoners and their reason for being held, age and \r\n sex of prisoners, maximum sentence that could be served in the \r\n facility, facility capacity and age, types of security available, and \r\n operating expenditures. For jails in counties and municipalities with\r\n populations of 25,000 or more, data are supplied on quarterly jail \r\n population, age of cells, and availability of service facilities and \r\nprograms for inmates.",
-            "modified": "2005-11-04T00:00:00",
-            "accessLevel": "public",
-            "identifier": "245",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Incident-Based Reporting System, 2011: Extract Files"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This census provides information on county and municipal \r\n jails facilities in the United States and their administration. For\r\n all jails, the data \r\n include number of prisoners and their reason for being held, age and \r\n sex of prisoners, maximum sentence that could be served in the \r\n facility, facility capacity and age, types of security available, and \r\n operating expenditures. For jails in counties and municipalities with\r\n populations of 25,000 or more, data are supplied on quarterly jail \r\n population, age of cells, and availability of service facilities and \r\nprograms for inmates.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR07641.v2",
+                    "title": "National Jail Census, 1970"
+                }
+            ],
+            "identifier": "245",
+            "isPartOf": "2169",
+            "issued": "1984-03-18T00:00:00",
             "keyword": [
                 "census data",
                 "correctional facilities",
@@ -12700,54 +12694,54 @@
                 "jail inmates",
                 "jails"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2005-11-04T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2169",
-            "dataQuality": false,
-            "issued": "1984-03-18T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR07641.v2",
-                    "title": "National Jail Census, 1970"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Jail Census, 1972",
-            "description": "The purpose of this census was to provide information on \r\n jails throughout the United States. Information is supplied on the \r\n number of inmates held, types of accommodations, number of different \r\n types of staff personnel, procedures for segregating certain types of \r\ninmates, and selected programs and services.",
-            "modified": "1994-02-18T00:00:00",
-            "accessLevel": "public",
-            "identifier": "246",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Jail Census, 1970"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The purpose of this census was to provide information on \r\n jails throughout the United States. Information is supplied on the \r\n number of inmates held, types of accommodations, number of different \r\n types of staff personnel, procedures for segregating certain types of \r\ninmates, and selected programs and services.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR07638.v2",
+                    "title": "National Jail Census, 1972"
+                }
+            ],
+            "identifier": "246",
+            "isPartOf": "2169",
+            "issued": "1984-03-18T00:00:00",
             "keyword": [
                 "census data",
                 "correctional facilities",
@@ -12759,54 +12753,54 @@
                 "jail inmates",
                 "jails"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "1994-02-18T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2169",
-            "dataQuality": false,
-            "issued": "1984-03-18T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR07638.v2",
-                    "title": "National Jail Census, 1972"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Jail Census, 1978",
-            "description": "The National Jail Census was conducted in early 1978 by the\r\n United States Census Bureau for the Bureau of Justice Statistics. The\r\n census was taken of all locally administered county and municipal\r\n jails with the authority to hold prisoners for more than 48 hours.\r\n Data are presented for jails in 45 states. Excluded are\r\n Connecticut, Delaware, Hawaii, Rhode Island, and Vermont. Information\r\n includes jail population by legal status, age and sex of prisoners,\r\n maximum sentence, admissions and releases, available services,\r\nstructure and capacity, expenditure, and employment.",
-            "modified": "2005-11-04T00:00:00",
-            "accessLevel": "public",
-            "identifier": "247",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Jail Census, 1972"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Jail Census was conducted in early 1978 by the\r\n United States Census Bureau for the Bureau of Justice Statistics. The\r\n census was taken of all locally administered county and municipal\r\n jails with the authority to hold prisoners for more than 48 hours.\r\n Data are presented for jails in 45 states. Excluded are\r\n Connecticut, Delaware, Hawaii, Rhode Island, and Vermont. Information\r\n includes jail population by legal status, age and sex of prisoners,\r\n maximum sentence, admissions and releases, available services,\r\nstructure and capacity, expenditure, and employment.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR07737.v4",
+                    "title": "National Jail Census, 1978"
+                }
+            ],
+            "identifier": "247",
+            "isPartOf": "2169",
+            "issued": "1984-03-18T00:00:00",
             "keyword": [
                 "census data",
                 "correctional facilities",
@@ -12818,54 +12812,54 @@
                 "jail inmates",
                 "jails"
             ],
-            "bureauCode": [
-                "011:21"
-            ],
-            "programCode": [
-                "011:061"
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2169",
-            "dataQuality": false,
-            "issued": "1984-03-18T00:00:00",
             "language": [
                 "eng"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR07737.v4",
-                    "title": "National Jail Census, 1978"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Jail Census, 1983",
-            "description": "The National Jail Census was conducted by the United States\r\nBureau of the Census for the Bureau of Justice Statistics. The census was\r\ntaken of all locally administered county and municipal jails with the\r\nauthority to hold prisoners for more than 48 hours. Data are presented\r\nfor 3,338 jails in 45 states. Excluded are Connecticut, Delaware,\r\nHawaii, Rhode Island, and Vermont. Information includes jail\r\npopulation by legal status, age and sex of prisoners, maximum\r\nsentence, admissions and releases, available services, structure and\r\ncapacity, expenditure, and employment.",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "modified": "2005-11-04T00:00:00",
-            "accessLevel": "public",
-            "identifier": "248",
+            "programCode": [
+                "011:061"
+            ],
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Jail Census, 1978"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Jail Census was conducted by the United States\r\nBureau of the Census for the Bureau of Justice Statistics. The census was\r\ntaken of all locally administered county and municipal jails with the\r\nauthority to hold prisoners for more than 48 hours. Data are presented\r\nfor 3,338 jails in 45 states. Excluded are Connecticut, Delaware,\r\nHawaii, Rhode Island, and Vermont. Information includes jail\r\npopulation by legal status, age and sex of prisoners, maximum\r\nsentence, admissions and releases, available services, structure and\r\ncapacity, expenditure, and employment.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR08203.v1",
+                    "title": "National Jail Census, 1983"
+                }
+            ],
+            "identifier": "248",
+            "isPartOf": "2169",
+            "issued": "1985-01-11T00:00:00",
             "keyword": [
                 "census data",
                 "correctional facilities",
@@ -12877,54 +12871,54 @@
                 "jail inmates",
                 "jails"
             ],
-            "bureauCode": [
-                "011:21"
-            ],
-            "programCode": [
-                "011:061"
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2169",
-            "dataQuality": false,
-            "issued": "1985-01-11T00:00:00",
             "language": [
                 "eng"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR08203.v1",
-                    "title": "National Jail Census, 1983"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Jail Census, 1988",
-            "description": "NATIONAL JAIL CENSUS, 1988, is the fifth in a series of\r\n data collection efforts aimed at studying the nation's locally\r\n administered jails. For purposes of this data collection, a jail was\r\n defined as a confinement facility intended for holding adults (and in\r\n some cases juveniles) pending adjudication or having sentences of a\r\n year or less. Jails were further defined as being administered and\r\n staffed by municipal or county employees. Also included in this\r\n collection were six jails privately operated under contract for local\r\n governments. Excluded from the census were federal or\r\n state-administered facilities, including the combined jail-prison\r\n systems in Alaska, Connecticut, Delaware, Hawaii, Rhode Island, and\r\n Vermont. The mailing list used for the census was derived from data\r\n gathered from the AMERICAN CORRECTIONAL ASSOCIATION DIRECTORY OF\r\n JUSTICE AGENCIES, publications such as AMERICAN JAILS, telephone calls\r\n to large metropolitan jail systems (e.g., New York City), state jail\r\n inspection bureaus, and newspaper articles. Following the initial\r\n mailout to 3,448 facilities, 44 jails were added and 176 deleted\r\n according to the criteria for inclusion, leaving a total of 3,316\r\n facilities in 44 states. Variables include information on jail\r\n population by legal status, age and sex of prisoners, maximum\r\n sentence, admissions and releases, available services, structure and\r\ncapacity, expenditure, and employment.",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "modified": "2005-11-04T00:00:00",
-            "accessLevel": "public",
-            "identifier": "249",
+            "programCode": [
+                "011:061"
+            ],
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Jail Census, 1983"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "NATIONAL JAIL CENSUS, 1988, is the fifth in a series of\r\n data collection efforts aimed at studying the nation's locally\r\n administered jails. For purposes of this data collection, a jail was\r\n defined as a confinement facility intended for holding adults (and in\r\n some cases juveniles) pending adjudication or having sentences of a\r\n year or less. Jails were further defined as being administered and\r\n staffed by municipal or county employees. Also included in this\r\n collection were six jails privately operated under contract for local\r\n governments. Excluded from the census were federal or\r\n state-administered facilities, including the combined jail-prison\r\n systems in Alaska, Connecticut, Delaware, Hawaii, Rhode Island, and\r\n Vermont. The mailing list used for the census was derived from data\r\n gathered from the AMERICAN CORRECTIONAL ASSOCIATION DIRECTORY OF\r\n JUSTICE AGENCIES, publications such as AMERICAN JAILS, telephone calls\r\n to large metropolitan jail systems (e.g., New York City), state jail\r\n inspection bureaus, and newspaper articles. Following the initial\r\n mailout to 3,448 facilities, 44 jails were added and 176 deleted\r\n according to the criteria for inclusion, leaving a total of 3,316\r\n facilities in 44 states. Variables include information on jail\r\n population by legal status, age and sex of prisoners, maximum\r\n sentence, admissions and releases, available services, structure and\r\ncapacity, expenditure, and employment.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR09256.v2",
+                    "title": "National Jail Census, 1988"
+                }
+            ],
+            "identifier": "249",
+            "isPartOf": "2169",
+            "issued": "1990-03-02T00:00:00",
             "keyword": [
                 "census data",
                 "correctional facilities",
@@ -12936,54 +12930,54 @@
                 "jail inmates",
                 "jails"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2005-11-04T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2169",
-            "dataQuality": false,
-            "issued": "1990-03-02T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR09256.v2",
-                    "title": "National Jail Census, 1988"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Jail Census, 1993",
-            "description": "This data collection is part of a series of data collection \r\n efforts aimed at studying the nation's locally administered jails. The \r\n 1993 census included all locally administered confinement facilities \r\n (3,287) that held inmates beyond arraignment and were staffed by \r\n municipal or county employees. The census also included 17 jails that \r\n were privately operated under contract for local governments and seven \r\n facilities maintained by the Federal Bureau of Prisons and functioning \r\n as jails. For purposes of this data collection, a local jail was \r\n defined as a confinement facility intended for holding adults, and in \r\n some cases juveniles pending adjudication or having sentences of a year \r\n or less. Jails were further defined as being administered by a local \r\n law enforcement agency. Variables include information on jail \r\n population by legal status, age, and sex of prisoners, maximum \r\n sentence, admissions and releases, available services and programs, \r\n structure and capacity, facility age and use of space, expenditure, \r\n employment, staff information, and health issues, which include \r\nstatistics on drugs, AIDS, and tuberculosis.",
-            "modified": "1996-07-13T00:00:00",
-            "accessLevel": "public",
-            "identifier": "250",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Jail Census, 1988"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This data collection is part of a series of data collection \r\n efforts aimed at studying the nation's locally administered jails. The \r\n 1993 census included all locally administered confinement facilities \r\n (3,287) that held inmates beyond arraignment and were staffed by \r\n municipal or county employees. The census also included 17 jails that \r\n were privately operated under contract for local governments and seven \r\n facilities maintained by the Federal Bureau of Prisons and functioning \r\n as jails. For purposes of this data collection, a local jail was \r\n defined as a confinement facility intended for holding adults, and in \r\n some cases juveniles pending adjudication or having sentences of a year \r\n or less. Jails were further defined as being administered by a local \r\n law enforcement agency. Variables include information on jail \r\n population by legal status, age, and sex of prisoners, maximum \r\n sentence, admissions and releases, available services and programs, \r\n structure and capacity, facility age and use of space, expenditure, \r\n employment, staff information, and health issues, which include \r\nstatistics on drugs, AIDS, and tuberculosis.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR06648.v1",
+                    "title": "National Jail Census, 1993"
+                }
+            ],
+            "identifier": "250",
+            "isPartOf": "2169",
+            "issued": "1996-07-13T00:00:00",
             "keyword": [
                 "census data",
                 "correctional facilities",
@@ -12995,54 +12989,54 @@
                 "jail inmates",
                 "jails"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "1996-07-13T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2169",
-            "dataQuality": false,
-            "issued": "1996-07-13T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR06648.v1",
-                    "title": "National Jail Census, 1993"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Justice Agency List, 1980",
-            "description": "The National Justice Agency List is a master name and\r\naddress file created and maintained by the United States Bureau of the\r\nCensus for the Bureau of Justice Statistics. The file was first\r\ncreated in 1970, and the Census Bureau has continued to maintain and\r\nexpand the file. The master file contains information for ten separate\r\nsectors: prosecution and civil attorneys, public defenders, law\r\nenforcement, courts, probation and parole, juvenile corrections, local\r\nadult corrections, state adult corrections, other justice agencies,\r\nand federal and Indian tribal agencies. ICPSR has separated the master\r\nfile into ten subfiles, corresponding to the ten sectors in the master\r\nfile. Each file has variables containing the names and addresses of\r\nagencies in that sector and information relevant only to the agencies\r\nwithin the sector. Court (Part 1) variables include court structure,\r\ntype of jurisdiction, and the location of court records. State Adult\r\nCorrectional Facilities (Part 2) variables include type of\r\ninstitution, agency employment size, sex of inmates, and funding\r\ncode. Public Defender Agencies (Part 3) variables include type of\r\nagency, type of cases handled, agency employment size, and funding\r\ncode. Probation and Parole Agencies (Part 4) variables include type of\r\nsystem, agency client caseload, agency employment size, and funding\r\ncode. \"Other\" Agencies (Part 5) variables include type of services\r\nand agency employment size. Local Jails (Part 6) variables include sex\r\nof inmates, number of female inmates, inmate population, and funding\r\ncode. Prosecution and Civil Attorney Agencies (Part 7) variables\r\ninclude type of agency, types of cases prosecuted, agency employment\r\nsize, number of attorneys, and funding code. Federal and Indian Tribal\r\nAgencies (Part 8) variables include type of justice sector, employment\r\nsize, and funding code. Law Enforcement Agencies (Part 9) variables\r\ninclude type of agency, employment size, and number of sworn police.\r\nJuvenile Detention and Correctional Facilities (Part 10) variables\r\ninclude type of facility, sex of residents, resident population, and\r\nemployment size.",
-            "modified": "2005-11-04T00:00:00",
-            "accessLevel": "public",
-            "identifier": "251",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Jail Census, 1993"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Justice Agency List is a master name and\r\naddress file created and maintained by the United States Bureau of the\r\nCensus for the Bureau of Justice Statistics. The file was first\r\ncreated in 1970, and the Census Bureau has continued to maintain and\r\nexpand the file. The master file contains information for ten separate\r\nsectors: prosecution and civil attorneys, public defenders, law\r\nenforcement, courts, probation and parole, juvenile corrections, local\r\nadult corrections, state adult corrections, other justice agencies,\r\nand federal and Indian tribal agencies. ICPSR has separated the master\r\nfile into ten subfiles, corresponding to the ten sectors in the master\r\nfile. Each file has variables containing the names and addresses of\r\nagencies in that sector and information relevant only to the agencies\r\nwithin the sector. Court (Part 1) variables include court structure,\r\ntype of jurisdiction, and the location of court records. State Adult\r\nCorrectional Facilities (Part 2) variables include type of\r\ninstitution, agency employment size, sex of inmates, and funding\r\ncode. Public Defender Agencies (Part 3) variables include type of\r\nagency, type of cases handled, agency employment size, and funding\r\ncode. Probation and Parole Agencies (Part 4) variables include type of\r\nsystem, agency client caseload, agency employment size, and funding\r\ncode. \"Other\" Agencies (Part 5) variables include type of services\r\nand agency employment size. Local Jails (Part 6) variables include sex\r\nof inmates, number of female inmates, inmate population, and funding\r\ncode. Prosecution and Civil Attorney Agencies (Part 7) variables\r\ninclude type of agency, types of cases prosecuted, agency employment\r\nsize, number of attorneys, and funding code. Federal and Indian Tribal\r\nAgencies (Part 8) variables include type of justice sector, employment\r\nsize, and funding code. Law Enforcement Agencies (Part 9) variables\r\ninclude type of agency, employment size, and number of sworn police.\r\nJuvenile Detention and Correctional Facilities (Part 10) variables\r\ninclude type of facility, sex of residents, resident population, and\r\nemployment size.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR07858.v2",
+                    "title": "National Justice Agency List, 1980"
+                }
+            ],
+            "identifier": "251",
+            "isPartOf": "2166",
+            "issued": "1984-03-18T00:00:00",
             "keyword": [
                 "census data",
                 "correctional facilities (adults)",
@@ -13059,54 +13053,54 @@
                 "state correctional facilities",
                 "state government"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2005-11-04T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2166",
-            "dataQuality": false,
-            "issued": "1984-03-18T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR07858.v2",
-                    "title": "National Justice Agency List, 1980"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Justice Agency List, 1985 ",
-            "description": "The National Justice Agency List, 1985 is a master name and\r\naddress file created and maintained by the Bureau of the Census for the\r\nBureau of Justice Statistics. The file contains information on the\r\nfollowing topics: prosecution and civil attorneys, public defenders,\r\nlaw enforcement, courts, probation and parole, juvenile corrections,\r\nlocal adult corrections, federal relations with American Indians, and\r\nother justice issues.",
-            "modified": "1992-02-16T00:00:00",
-            "accessLevel": "public",
-            "identifier": "252",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Justice Agency List, 1980"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Justice Agency List, 1985 is a master name and\r\naddress file created and maintained by the Bureau of the Census for the\r\nBureau of Justice Statistics. The file contains information on the\r\nfollowing topics: prosecution and civil attorneys, public defenders,\r\nlaw enforcement, courts, probation and parole, juvenile corrections,\r\nlocal adult corrections, federal relations with American Indians, and\r\nother justice issues.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR08489.v1",
+                    "title": "National Justice Agency List, 1985 "
+                }
+            ],
+            "identifier": "252",
+            "isPartOf": "2166",
+            "issued": "1986-08-18T00:00:00",
             "keyword": [
                 "census data",
                 "government agencies",
@@ -13114,54 +13108,54 @@
                 "local government",
                 "state government"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "1992-02-16T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2166",
-            "dataQuality": false,
-            "issued": "1986-08-18T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR08489.v1",
-                    "title": "National Justice Agency List, 1985 "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Justice Agency List, 1986   ",
-            "description": "The National Justice Agency List is a master name and\r\naddress file created and maintained by the Bureau of the Census for\r\nthe Bureau of Justice Statistics. The file also contains information\r\non the following topics: prosecution and civil attorneys, public\r\ndefenders, law enforcement, courts, probation and parole, juvenile\r\ncorrections, local adult corrections, federal relations with American\r\nIndians, and other justice issues.",
-            "modified": "2005-11-04T00:00:00",
-            "accessLevel": "public",
-            "identifier": "253",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Justice Agency List, 1985 "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Justice Agency List is a master name and\r\naddress file created and maintained by the Bureau of the Census for\r\nthe Bureau of Justice Statistics. The file also contains information\r\non the following topics: prosecution and civil attorneys, public\r\ndefenders, law enforcement, courts, probation and parole, juvenile\r\ncorrections, local adult corrections, federal relations with American\r\nIndians, and other justice issues.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR08692.v1",
+                    "title": "National Justice Agency List, 1986   "
+                }
+            ],
+            "identifier": "253",
+            "isPartOf": "2166",
+            "issued": "1987-10-12T00:00:00",
             "keyword": [
                 "census data",
                 "government agencies",
@@ -13169,54 +13163,54 @@
                 "local government",
                 "state government"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2005-11-04T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2166",
-            "dataQuality": false,
-            "issued": "1987-10-12T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR08692.v1",
-                    "title": "National Justice Agency List, 1986   "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Justice Agency List, 1987",
-            "description": "The National Justice Agency List, 1987 is a master name and\r\naddress file created and maintained by the Bureau of the Census for the\r\nBureau of Justice Statistics. The file contains information for the\r\nfollowing topics: public defenders, law enforcement, courts, probation\r\nenforcement, probation and parole, juvenile corrections, local adult\r\ncorrections, state adult corrections, federal adult corrections, and\r\nother justice agencies. Variables include name of the agency, address,\r\nstate and region identification, telephone number, FIPS code,\r\npopulation, total workload, and number of professional and total\r\nemployees.",
-            "modified": "2005-02-11T00:00:00",
-            "accessLevel": "public",
-            "identifier": "254",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Justice Agency List, 1986   "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Justice Agency List, 1987 is a master name and\r\naddress file created and maintained by the Bureau of the Census for the\r\nBureau of Justice Statistics. The file contains information for the\r\nfollowing topics: public defenders, law enforcement, courts, probation\r\nenforcement, probation and parole, juvenile corrections, local adult\r\ncorrections, state adult corrections, federal adult corrections, and\r\nother justice agencies. Variables include name of the agency, address,\r\nstate and region identification, telephone number, FIPS code,\r\npopulation, total workload, and number of professional and total\r\nemployees.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR09482.v1",
+                    "title": "National Justice Agency List, 1987"
+                }
+            ],
+            "identifier": "254",
+            "isPartOf": "2166",
+            "issued": "1991-03-05T00:00:00",
             "keyword": [
                 "census data",
                 "government agencies",
@@ -13224,54 +13218,54 @@
                 "local government",
                 "state government"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2005-02-11T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2166",
-            "dataQuality": false,
-            "issued": "1991-03-05T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR09482.v1",
-                    "title": "National Justice Agency List, 1987"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Justice Agency List, 1992",
-            "description": "The National Justice Agency List is a master name and\r\naddress file created and maintained by the Bureau of the Census for the\r\nBureau of Justice Statistics. The file contains information for the\r\nfollowing government justice agencies: law enforcement agencies,\r\njuvenile correctional facilities, local jails, state correctional\r\nfacilities, and federal prisons. Variables include name of agency,\r\naddress, state and region identification, telephone number, FIPS code,\r\npopulation, total workload, and number of professional and total\r\nemployees.",
-            "modified": "1994-05-20T00:00:00",
-            "accessLevel": "public",
-            "identifier": "255",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Justice Agency List, 1987"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Justice Agency List is a master name and\r\naddress file created and maintained by the Bureau of the Census for the\r\nBureau of Justice Statistics. The file contains information for the\r\nfollowing government justice agencies: law enforcement agencies,\r\njuvenile correctional facilities, local jails, state correctional\r\nfacilities, and federal prisons. Variables include name of agency,\r\naddress, state and region identification, telephone number, FIPS code,\r\npopulation, total workload, and number of professional and total\r\nemployees.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR06228.v1",
+                    "title": "National Justice Agency List, 1992"
+                }
+            ],
+            "identifier": "255",
+            "isPartOf": "2166",
+            "issued": "1994-05-20T00:00:00",
             "keyword": [
                 "census data",
                 "correctional facilities (juveniles)",
@@ -13283,54 +13277,54 @@
                 "state correctional facilities",
                 "state government"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "1994-05-20T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2166",
-            "dataQuality": false,
-            "issued": "1994-05-20T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR06228.v1",
-                    "title": "National Justice Agency List, 1992"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Justice Agency List, 1995   ",
-            "description": "The National Justice Agency List is a master name and\r\naddress file created and maintained by the Census Bureau for the\r\nBureau of Justice Statistics. The 1995 data provide information on 11\r\nseparate sectors of criminal justice agencies. Every sector file has\r\nvariables containing the names and addresses of agencies in that\r\nsector and information relevant only to the agencies within the\r\nsector. The following files comprise the collection: Part 1 -- Public\r\nDefender Agencies: Variables include type of agency and agency\r\nstructure. Part 2 -- Law Enforcement Agencies: Variables include type\r\nof agency and agency structure. Part 3 -- Courts: Variables include\r\ntype of agency and agency structure. Part 4 -- Probation and Parole\r\nAgencies: Variables include type of agency. Part 5 -- Juvenile\r\nDetention and Correctional Facilities: Variables include type of\r\nfacility, sex of residents, and resident population. Part 6 -- Local\r\nAdult Corrections Agencies: Variables include number of female\r\ninmates, number of male inmates, type of facility, and average daily\r\npopulation of inmates. Part 7 -- State Adult Correctional Facilities:\r\nVariables include type of institution, average daily population of\r\ninmates, and sex of inmates. Part 8 -- Federal Adult Correctional\r\nFacilities: Variables include type of facility, average daily\r\npopulation of inmates, and sex of inmates. Part 9 -- Other Justice\r\nAgencies: Variables include type of agency. Part 10 -- Prosecution and\r\nCivil Attorney Agencies: Variables include type of agency and agency\r\nstructure. Part 11 -- Federal and Indian Tribal Agencies: Variables\r\ninclude type of justice sector.",
-            "modified": "2006-01-12T00:00:00",
-            "accessLevel": "public",
-            "identifier": "256",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Justice Agency List, 1992"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Justice Agency List is a master name and\r\naddress file created and maintained by the Census Bureau for the\r\nBureau of Justice Statistics. The 1995 data provide information on 11\r\nseparate sectors of criminal justice agencies. Every sector file has\r\nvariables containing the names and addresses of agencies in that\r\nsector and information relevant only to the agencies within the\r\nsector. The following files comprise the collection: Part 1 -- Public\r\nDefender Agencies: Variables include type of agency and agency\r\nstructure. Part 2 -- Law Enforcement Agencies: Variables include type\r\nof agency and agency structure. Part 3 -- Courts: Variables include\r\ntype of agency and agency structure. Part 4 -- Probation and Parole\r\nAgencies: Variables include type of agency. Part 5 -- Juvenile\r\nDetention and Correctional Facilities: Variables include type of\r\nfacility, sex of residents, and resident population. Part 6 -- Local\r\nAdult Corrections Agencies: Variables include number of female\r\ninmates, number of male inmates, type of facility, and average daily\r\npopulation of inmates. Part 7 -- State Adult Correctional Facilities:\r\nVariables include type of institution, average daily population of\r\ninmates, and sex of inmates. Part 8 -- Federal Adult Correctional\r\nFacilities: Variables include type of facility, average daily\r\npopulation of inmates, and sex of inmates. Part 9 -- Other Justice\r\nAgencies: Variables include type of agency. Part 10 -- Prosecution and\r\nCivil Attorney Agencies: Variables include type of agency and agency\r\nstructure. Part 11 -- Federal and Indian Tribal Agencies: Variables\r\ninclude type of justice sector.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR06726.v1",
+                    "title": "National Justice Agency List, 1995   "
+                }
+            ],
+            "identifier": "256",
+            "isPartOf": "2166",
+            "issued": "1996-10-01T00:00:00",
             "keyword": [
                 "census data",
                 "government agencies",
@@ -13338,54 +13332,54 @@
                 "local government",
                 "state government"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2006-01-12T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2166",
-            "dataQuality": false,
-            "issued": "1996-10-01T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR06726.v1",
-                    "title": "National Justice Agency List, 1995   "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Prisoner Statistics, 1978-2011",
-            "description": "The National Prisoner Statistics (NPS) data collection began in 1926 in response to a congressional mandate to gather information on persons incarcerated in state and federal prisons. Originally under the auspices of the United States Census Bureau, the collection moved to the Bureau of Prisons in 1950, and then in 1971 to the National Criminal Justice Information and Statistics Service, the precursor to the Bureau of Justice Statistics (BJS) which was established in 1979.  Since 1979, the Census Bureau has been the NPS data collection agent.\r\nThe NPS is administered to 51 respondents. Before 2001, the District of Columbia was also a respondent, but responsibility for housing the District of Columbia's sentenced prisoners was transferred to the federal Bureau of Prisons, and by yearend 2001 the District of Columbia no longer operated a prison system.\r\nThe NPS provides an enumeration of persons in state and federal prisons and collects data on key characteristics of the nation's prison population.  NPS has been adapted over time to keep pace with the changing information needs of the public, researchers, and federal, state, and local governments.",
-            "modified": "2013-06-25T10:59:58",
-            "accessLevel": "public",
-            "identifier": "257",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Justice Agency List, 1995   "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Prisoner Statistics (NPS) data collection began in 1926 in response to a congressional mandate to gather information on persons incarcerated in state and federal prisons. Originally under the auspices of the United States Census Bureau, the collection moved to the Bureau of Prisons in 1950, and then in 1971 to the National Criminal Justice Information and Statistics Service, the precursor to the Bureau of Justice Statistics (BJS) which was established in 1979.  Since 1979, the Census Bureau has been the NPS data collection agent.\r\nThe NPS is administered to 51 respondents. Before 2001, the District of Columbia was also a respondent, but responsibility for housing the District of Columbia's sentenced prisoners was transferred to the federal Bureau of Prisons, and by yearend 2001 the District of Columbia no longer operated a prison system.\r\nThe NPS provides an enumeration of persons in state and federal prisons and collects data on key characteristics of the nation's prison population.  NPS has been adapted over time to keep pace with the changing information needs of the public, researchers, and federal, state, and local governments.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR34540.v1",
+                    "title": "National Prisoner Statistics, 1978-2011"
+                }
+            ],
+            "identifier": "257",
+            "isPartOf": "2633",
+            "issued": "2013-06-25T10:59:58",
             "keyword": [
                 "HIV",
                 "correctional system",
@@ -13395,54 +13389,54 @@
                 "prison inmates",
                 "state correctional facilities"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-06-25T10:59:58",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2633",
-            "dataQuality": false,
-            "issued": "2013-06-25T10:59:58",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR34540.v1",
-                    "title": "National Prisoner Statistics, 1978-2011"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Prosecutors Survey [Census], 2001",
-            "description": "The National Survey of Prosecutors is a survey of chief\r\nprosecutors in state court systems. It was previously conducted in\r\n1990, 1992, 1994, and 1996 (ICPSR 9579, 6273, 6785, 2433\r\nrespectively). For 2001, instead of a survey of chief prosecutors, a\r\ncensus of all 2,341 chief prosecutors who handled felony cases in state\r\ncourts of general jurisdiction was conducted. A chief prosecutor is an\r\nofficial, usually locally elected and typically with the title of\r\ndistrict attorney or county attorney, who is in charge of a\r\nprosecutorial district made up of one or more counties, and who\r\nconducts or supervises the prosecution of felony cases in a state\r\ncourt system. Prosecutors in courts of limited jurisdiction, such as\r\nmunicipal prosecutors, were not included in the survey. The census'\r\npurpose was to obtain detailed descriptive information on prosecutors'\r\noffices, as well as information on their policies and\r\npractices. Variables cover staffing, funding, special categories of\r\nfelony prosecutions, caseload, juvenile matters, work-related threats\r\nor assaults, the use of DNA evidence, and community-related\r\nactivities, such as involvement in neighborhood associations. The unit\r\nof analysis is the district office.",
-            "modified": "2005-11-04T00:00:00",
-            "accessLevel": "public",
-            "identifier": "258",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Prisoner Statistics, 1978-2011"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Survey of Prosecutors is a survey of chief\r\nprosecutors in state court systems. It was previously conducted in\r\n1990, 1992, 1994, and 1996 (ICPSR 9579, 6273, 6785, 2433\r\nrespectively). For 2001, instead of a survey of chief prosecutors, a\r\ncensus of all 2,341 chief prosecutors who handled felony cases in state\r\ncourts of general jurisdiction was conducted. A chief prosecutor is an\r\nofficial, usually locally elected and typically with the title of\r\ndistrict attorney or county attorney, who is in charge of a\r\nprosecutorial district made up of one or more counties, and who\r\nconducts or supervises the prosecution of felony cases in a state\r\ncourt system. Prosecutors in courts of limited jurisdiction, such as\r\nmunicipal prosecutors, were not included in the survey. The census'\r\npurpose was to obtain detailed descriptive information on prosecutors'\r\noffices, as well as information on their policies and\r\npractices. Variables cover staffing, funding, special categories of\r\nfelony prosecutions, caseload, juvenile matters, work-related threats\r\nor assaults, the use of DNA evidence, and community-related\r\nactivities, such as involvement in neighborhood associations. The unit\r\nof analysis is the district office.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR03418.v1",
+                    "title": "National Prosecutors Survey [Census], 2001"
+                }
+            ],
+            "identifier": "258",
+            "isPartOf": "2181",
+            "issued": "2002-07-03T00:00:00",
             "keyword": [
                 "attorneys",
                 "case processing",
@@ -13458,54 +13452,54 @@
                 "state courts",
                 "trial procedures"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2005-11-04T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2181",
-            "dataQuality": false,
-            "issued": "2002-07-03T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR03418.v1",
-                    "title": "National Prosecutors Survey [Census], 2001"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Prosecutors Survey [Census], 2007",
-            "description": "The 2007 Census of State Court Prosecutors marked\r\nthe second BJS survey of all prosecutors' offices in the\r\nUnited States. The first census, conducted in 2001,\r\nincluded the 2,341 offices in operation at that time.\r\nThe second census included the 2,330 state court\r\nprosecutors' offices operating in 2007. Neither census\r\nincluded offices of municipal attorneys or county\r\nattorneys, who primarily operate in courts of limited\r\njurisdiction.\r\nState court prosecutors serve in the executive\r\nbranch of state governments and handle felony\r\ncases in state courts of general jurisdiction. By law,\r\nthese prosecutors are afforded broad discretion in\r\ndetermining who is charged with an offense and\r\nwhether a case goes to trial. The chief prosecutor, also\r\nreferred to as the district attorney, county attorney,\r\ncommonwealth attorney, or state's attorney, represents\r\nthe state in criminal cases and is answerable to the\r\npublic as an elected or appointed public official.\r\nThe Office of the United States Attorney for the\r\nDistrict of Columbia is the only federal prosecutor\r\nincluded in the census. This unique office is\r\nresponsible for prosecution of serious local crimes\r\ncommitted in the District and also for prosecution of\r\nfederal cases, whether criminal or civil.",
-            "modified": "2012-05-14T09:19:59",
-            "accessLevel": "public",
-            "identifier": "259",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Prosecutors Survey [Census], 2001"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The 2007 Census of State Court Prosecutors marked\r\nthe second BJS survey of all prosecutors' offices in the\r\nUnited States. The first census, conducted in 2001,\r\nincluded the 2,341 offices in operation at that time.\r\nThe second census included the 2,330 state court\r\nprosecutors' offices operating in 2007. Neither census\r\nincluded offices of municipal attorneys or county\r\nattorneys, who primarily operate in courts of limited\r\njurisdiction.\r\nState court prosecutors serve in the executive\r\nbranch of state governments and handle felony\r\ncases in state courts of general jurisdiction. By law,\r\nthese prosecutors are afforded broad discretion in\r\ndetermining who is charged with an offense and\r\nwhether a case goes to trial. The chief prosecutor, also\r\nreferred to as the district attorney, county attorney,\r\ncommonwealth attorney, or state's attorney, represents\r\nthe state in criminal cases and is answerable to the\r\npublic as an elected or appointed public official.\r\nThe Office of the United States Attorney for the\r\nDistrict of Columbia is the only federal prosecutor\r\nincluded in the census. This unique office is\r\nresponsible for prosecution of serious local crimes\r\ncommitted in the District and also for prosecution of\r\nfederal cases, whether criminal or civil.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR33202.v1",
+                    "title": "National Prosecutors Survey [Census], 2007"
+                }
+            ],
+            "identifier": "259",
+            "isPartOf": "2181",
+            "issued": "2012-05-14T09:19:59",
             "keyword": [
                 "DNA fingerprinting",
                 "attorneys",
@@ -13528,54 +13522,54 @@
                 "trial procedures",
                 "victim services"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2012-05-14T09:19:59",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2181",
-            "dataQuality": false,
-            "issued": "2012-05-14T09:19:59",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR33202.v1",
-                    "title": "National Prosecutors Survey [Census], 2007"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Prosecutors Survey, 2005",
-            "description": "The National Survey of Prosecutors is a biennial survey of\r\nchief prosecutors in state court systems. A chief prosecutor is an\r\nofficial, usually locally elected and typically with the title of\r\ndistrict attorney or county attorney, who is in charge of a\r\nprosecutorial district made up of one or more counties, and who\r\nconducts or supervises the prosecution of felony cases in a state\r\ncourt system. Prosecutors in courts of limited jurisdiction, such as\r\nmunicipal prosecutors, were not included in the survey. The survey's\r\npurpose was to obtain detailed descriptive information on prosecutors'\r\noffices, as well as information on their policies and practices. The\r\ndata collection instrument was based on questions that were included\r\nin the NATIONAL PROSECUTORS SURVEY, 1994 (ICPSR 6785), and added\r\nqueries on topics of current concern. Variables cover staffing,\r\nworkload, funding, what type of computer access the office had,\r\nwhether the office was part of an integrated computerized system with\r\nother specific criminal agencies, the use of DNA evidence in plea\r\nnegotiations of felony trials, which laboratories performed these DNA\r\nanalyses, juvenile matters, and risks associated with the role of the\r\nprosecutor, such as threatening letters or calls, face-to-face\r\nassaults, or batter/assaults. The unit of analysis is the district\r\noffice.",
-            "modified": "2007-02-23T00:00:00",
-            "accessLevel": "public",
-            "identifier": "260",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Prosecutors Survey [Census], 2007"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Survey of Prosecutors is a biennial survey of\r\nchief prosecutors in state court systems. A chief prosecutor is an\r\nofficial, usually locally elected and typically with the title of\r\ndistrict attorney or county attorney, who is in charge of a\r\nprosecutorial district made up of one or more counties, and who\r\nconducts or supervises the prosecution of felony cases in a state\r\ncourt system. Prosecutors in courts of limited jurisdiction, such as\r\nmunicipal prosecutors, were not included in the survey. The survey's\r\npurpose was to obtain detailed descriptive information on prosecutors'\r\noffices, as well as information on their policies and practices. The\r\ndata collection instrument was based on questions that were included\r\nin the NATIONAL PROSECUTORS SURVEY, 1994 (ICPSR 6785), and added\r\nqueries on topics of current concern. Variables cover staffing,\r\nworkload, funding, what type of computer access the office had,\r\nwhether the office was part of an integrated computerized system with\r\nother specific criminal agencies, the use of DNA evidence in plea\r\nnegotiations of felony trials, which laboratories performed these DNA\r\nanalyses, juvenile matters, and risks associated with the role of the\r\nprosecutor, such as threatening letters or calls, face-to-face\r\nassaults, or batter/assaults. The unit of analysis is the district\r\noffice.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR04600.v1",
+                    "title": "National Prosecutors Survey, 2005"
+                }
+            ],
+            "identifier": "260",
+            "isPartOf": "2181",
+            "issued": "2007-01-17T00:00:00",
             "keyword": [
                 "DNA fingerprinting",
                 "attorneys",
@@ -13598,106 +13592,105 @@
                 "trial procedures",
                 "victim services"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2007-02-23T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2181",
-            "dataQuality": false,
-            "issued": "2007-01-17T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR04600.v1",
-                    "title": "National Prosecutors Survey, 2005"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Survey of Court Organization, 1971-1972",
-            "description": "The purpose of this study\r\nwas to document the existing organization of courts in the 50 states\r\nand the District of Columbia as of 1971-1972. The survey covers all\r\nappellate courts, courts of general jurisdiction, special courts, and\r\nother courts of limited jurisdiction. Excluded were justices of the\r\npeace and similar magistrates whose compensation is solely on a direct\r\nfee basis, and courts of limited or special jurisdiction located in\r\nmunicipalities or townships with a 1960 population of less than 1,000.\r\nThe data for courts include information on the organization of the\r\ncourt, geographic location, type of court, level of government\r\nadministering the court, number, types, and full- or part-time status\r\nof judicial and other personnel, method of appealing cases, location of\r\ncourt records, and types of statistics. Court subdivision variables cover\r\norganization of the courts, geographic location, type of\r\ncourt, level of government administering the court, types of\r\njurisdiction, percentage of judges' time spent on types of cases,\r\navailability of jury trials, and length of sentence and amounts of\r\nfines which may be imposed by the court.",
-            "modified": "2005-11-04T00:00:00",
-            "accessLevel": "public",
-            "identifier": "261",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Prosecutors Survey, 2005"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The purpose of this study\r\nwas to document the existing organization of courts in the 50 states\r\nand the District of Columbia as of 1971-1972. The survey covers all\r\nappellate courts, courts of general jurisdiction, special courts, and\r\nother courts of limited jurisdiction. Excluded were justices of the\r\npeace and similar magistrates whose compensation is solely on a direct\r\nfee basis, and courts of limited or special jurisdiction located in\r\nmunicipalities or townships with a 1960 population of less than 1,000.\r\nThe data for courts include information on the organization of the\r\ncourt, geographic location, type of court, level of government\r\nadministering the court, number, types, and full- or part-time status\r\nof judicial and other personnel, method of appealing cases, location of\r\ncourt records, and types of statistics. Court subdivision variables cover\r\norganization of the courts, geographic location, type of\r\ncourt, level of government administering the court, types of\r\njurisdiction, percentage of judges' time spent on types of cases,\r\navailability of jury trials, and length of sentence and amounts of\r\nfines which may be imposed by the court.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR07640.v1",
+                    "title": "National Survey of Court Organization, 1971-1972"
+                }
+            ],
+            "identifier": "261",
+            "issued": "1984-05-03T00:00:00",
             "keyword": [
                 "court cases",
                 "court system",
                 "criminal justice system"
             ],
-            "bureauCode": [
-                "011:21"
-            ],
-            "programCode": [
-                "011:061"
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "1984-05-03T00:00:00",
             "language": [
                 "eng"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR07640.v1",
-                    "title": "National Survey of Court Organization, 1971-1972"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Survey of DNA Crime Laboratories, 1998  ",
-            "description": "This study reports findings from a survey of publicly\r\n operated forensic crime labs that perform deoxyribonucleic acid (DNA)\r\n testing. The survey includes questions about each lab's budget,\r\n personnel, workload, and operating policies and procedures. Data were\r\n obtained from 108 out of 120 estimated known labs, including all\r\nstatewide labs.",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "modified": "2005-11-04T00:00:00",
-            "accessLevel": "public",
-            "identifier": "262",
+            "programCode": [
+                "011:061"
+            ],
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Survey of Court Organization, 1971-1972"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This study reports findings from a survey of publicly\r\n operated forensic crime labs that perform deoxyribonucleic acid (DNA)\r\n testing. The survey includes questions about each lab's budget,\r\n personnel, workload, and operating policies and procedures. Data were\r\n obtained from 108 out of 120 estimated known labs, including all\r\nstatewide labs.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR02879.v1",
+                    "title": "National Survey of DNA Crime Laboratories, 1998  "
+                }
+            ],
+            "identifier": "262",
+            "issued": "2000-11-02T00:00:00",
             "keyword": [
                 "DNA fingerprinting",
                 "crime laboratories",
@@ -13705,53 +13698,53 @@
                 "personnel",
                 "policies and procedures"
             ],
-            "bureauCode": [
-                "011:21"
-            ],
-            "programCode": [
-                "011:061"
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "2000-11-02T00:00:00",
             "language": [
                 "eng"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR02879.v1",
-                    "title": "National Survey of DNA Crime Laboratories, 1998  "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Survey of DNA Crime Laboratories, 2001  ",
-            "description": "This study contains data from a survey of publicly operated\r\n forensic crime labs that perform deoxyribonucleic acid (DNA)\r\n testing. The survey was a follow-up to the initial survey of DNA crime\r\n labs in 1998 (ICPSR study 2879). The survey included questions about\r\n each lab's budget, personnel, procedures, equipment, and workloads in\r\n terms of known subject cases, unknown subject cases, and convicted\r\n offender DNA samples. The survey was sent to 135 forensic laboratories,\r\n and 124 responses were received from individual public laboratories and\r\n headquarters for statewide forensic crime laboratory systems. The\r\n responses included 110 publicly funded forensic laboratories that\r\nperformed DNA testing in 47 states.",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "modified": "2005-11-04T00:00:00",
-            "accessLevel": "public",
-            "identifier": "263",
+            "programCode": [
+                "011:061"
+            ],
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Survey of DNA Crime Laboratories, 1998  "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This study contains data from a survey of publicly operated\r\n forensic crime labs that perform deoxyribonucleic acid (DNA)\r\n testing. The survey was a follow-up to the initial survey of DNA crime\r\n labs in 1998 (ICPSR study 2879). The survey included questions about\r\n each lab's budget, personnel, procedures, equipment, and workloads in\r\n terms of known subject cases, unknown subject cases, and convicted\r\n offender DNA samples. The survey was sent to 135 forensic laboratories,\r\n and 124 responses were received from individual public laboratories and\r\n headquarters for statewide forensic crime laboratory systems. The\r\n responses included 110 publicly funded forensic laboratories that\r\nperformed DNA testing in 47 states.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR03550.v1",
+                    "title": "National Survey of DNA Crime Laboratories, 2001  "
+                }
+            ],
+            "identifier": "263",
+            "issued": "2003-11-10T00:00:00",
             "keyword": [
                 "DNA fingerprinting",
                 "crime laboratories",
@@ -13760,53 +13753,53 @@
                 "personnel",
                 "policies and procedures"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2005-11-04T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "2003-11-10T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR03550.v1",
-                    "title": "National Survey of DNA Crime Laboratories, 2001  "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Survey of Indigent Defense Systems (NSIDS), 1999",
-            "description": "This survey collected nationwide data in order to: (1)\r\nidentify the number and characteristics of publicly financed indigent\r\ndefense systems and agencies in the United States, (2) measure how\r\nlegal services were provided to indigent criminal defendants in terms\r\nof caseloads, workloads, policies, and practices, and (3) describe the\r\ntypes of offenses handled by indigent defense system organizations.\r\nThe study was initially designed to permit measurable statistical\r\nestimates at the national level for each region of the United States,\r\nfor individual states, and for the 100 most populous counties,\r\nincluding the District of Columbia. However, due to resource and\r\nfinancial constraints, the study was scaled back to collect indigent\r\ncriminal defense data at the trial level for (1) the 100 most populous\r\ncounties, (2) 197 counties outside the 100 most populous counties, and\r\n(3) states that entirely funded indigent criminal defense services.",
-            "modified": "2006-01-18T00:00:00",
-            "accessLevel": "public",
-            "identifier": "264",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Survey of DNA Crime Laboratories, 2001  "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This survey collected nationwide data in order to: (1)\r\nidentify the number and characteristics of publicly financed indigent\r\ndefense systems and agencies in the United States, (2) measure how\r\nlegal services were provided to indigent criminal defendants in terms\r\nof caseloads, workloads, policies, and practices, and (3) describe the\r\ntypes of offenses handled by indigent defense system organizations.\r\nThe study was initially designed to permit measurable statistical\r\nestimates at the national level for each region of the United States,\r\nfor individual states, and for the 100 most populous counties,\r\nincluding the District of Columbia. However, due to resource and\r\nfinancial constraints, the study was scaled back to collect indigent\r\ncriminal defense data at the trial level for (1) the 100 most populous\r\ncounties, (2) 197 counties outside the 100 most populous counties, and\r\n(3) states that entirely funded indigent criminal defense services.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR03081.v1",
+                    "title": "National Survey of Indigent Defense Systems (NSIDS), 1999"
+                }
+            ],
+            "identifier": "264",
+            "issued": "2001-10-31T00:00:00",
             "keyword": [
                 "court cases",
                 "defendants",
@@ -13817,53 +13810,54 @@
                 "policies and procedures",
                 "public defenders"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2006-01-18T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "2001-10-31T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR03081.v1",
-                    "title": "National Survey of Indigent Defense Systems (NSIDS), 1999"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Survey of Jails: Jurisdiction-Level and Jail-Level Data, 1986",
-            "description": "This data collection provides annual data on jail\r\n populations across the nation and examines the \"spillover\" effect on\r\n local jails resulting from the dramatic growth in federal and state\r\n prison populations. These data permit an assessment of the demands\r\n placed on correctional resources. Information is available on the\r\n number of inmates by sex, race, adult or juvenile status, reason being\r\nheld, and cause of death.",
-            "modified": "2005-11-04T00:00:00",
-            "accessLevel": "public",
-            "identifier": "265",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Survey of Indigent Defense Systems (NSIDS), 1999"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This data collection provides annual data on jail\r\n populations across the nation and examines the \"spillover\" effect on\r\n local jails resulting from the dramatic growth in federal and state\r\n prison populations. These data permit an assessment of the demands\r\n placed on correctional resources. Information is available on the\r\n number of inmates by sex, race, adult or juvenile status, reason being\r\nheld, and cause of death.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR08871.v1",
+                    "title": "National Survey of Jails: Jurisdiction-Level and Jail-Level Data, 1986"
+                }
+            ],
+            "identifier": "265",
+            "isPartOf": "2586",
+            "issued": "1988-07-15T00:00:00",
             "keyword": [
                 "correctional facilities",
                 "correctional system",
@@ -13874,54 +13868,54 @@
                 "population characteristics",
                 "probation"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2005-11-04T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2586",
-            "dataQuality": false,
-            "issued": "1988-07-15T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR08871.v1",
-                    "title": "National Survey of Jails: Jurisdiction-Level and Jail-Level Data, 1986"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Offender Based Transaction Statistics (OBTS), 1990: Alabama, Alaska, California, Idaho, Minnesota, Missouri, Nebraska, New Jersey, New York, Pennsylvania, Vermont, and Virginia",
-            "description": "Offender Based Transaction Statistics (OBTS) studies are\r\n designed to collect information by tracking adult offenders from the\r\n point of entry into the criminal justice system (typically by arrest)\r\n through final disposition, regardless of whether the offender is\r\n convicted or acquitted. Information is provided on arrest, police\r\n action, prosecutor action, level of charges, charges filed by the\r\n prosecutor, type of counsel, pretrial status, type of trial, sentence\r\n type, and sentence length. This allows researchers to examine how the\r\n criminal justice system processes offenders, to measure the changing\r\n volume of offenders moving through the different segments of the\r\n criminal justice system, to calculate processing time intervals\r\n between major decision-making events, and to assess the changing\r\nstructure of the offender population.",
-            "modified": "2005-09-02T00:00:00",
-            "accessLevel": "public",
-            "identifier": "266",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Survey of Jails: Jurisdiction-Level and Jail-Level Data, 1986"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "Offender Based Transaction Statistics (OBTS) studies are\r\n designed to collect information by tracking adult offenders from the\r\n point of entry into the criminal justice system (typically by arrest)\r\n through final disposition, regardless of whether the offender is\r\n convicted or acquitted. Information is provided on arrest, police\r\n action, prosecutor action, level of charges, charges filed by the\r\n prosecutor, type of counsel, pretrial status, type of trial, sentence\r\n type, and sentence length. This allows researchers to examine how the\r\n criminal justice system processes offenders, to measure the changing\r\n volume of offenders moving through the different segments of the\r\n criminal justice system, to calculate processing time intervals\r\n between major decision-making events, and to assess the changing\r\nstructure of the offender population.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR06191.v2",
+                    "title": "Offender Based Transaction Statistics (OBTS), 1990: Alabama, Alaska, California, Idaho, Minnesota, Missouri, Nebraska, New Jersey, New York, Pennsylvania, Vermont, and Virginia"
+                }
+            ],
+            "identifier": "266",
+            "isPartOf": "2177",
+            "issued": "1994-03-10T00:00:00",
             "keyword": [
                 "adult offenders",
                 "arrests",
@@ -13932,54 +13926,53 @@
                 "prosecution",
                 "sentencing"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2005-09-02T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2177",
-            "dataQuality": false,
-            "issued": "1994-03-10T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR06191.v2",
-                    "title": "Offender Based Transaction Statistics (OBTS), 1990: Alabama, Alaska, California, Idaho, Minnesota, Missouri, Nebraska, New Jersey, New York, Pennsylvania, Vermont, and Virginia"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Police Use of Force Data, 1996: [United States]",
-            "description": "In 1996, the Bureau of Justice Statistics sponsored a\r\n pretest of a survey instrument designed to compile data on citizen\r\n contacts with police, including contacts in which police use force.\r\n The survey, which involved interviews (both face-to-face and by phone)\r\n carried out by the United States Census Bureau, was conducted as a\r\n special supplement to the National Crime Victimization Survey (NCVS),\r\n an ongoing household survey of the American public that elicits\r\n information concerning recent crime victimization\r\n experiences. Questions asked in the supplement covered reasons for\r\n contact with police officer(s), characteristics of the officer, weapons\r\n used by the officer, whether there were any injuries involved in the\r\n confrontation between the household member and the officer, whether\r\n drugs were involved in the incident, type of offense the respondent\r\n was charged with, and whether any citizen action was\r\ntaken. Demographic variables include race, sex, and age.",
-            "modified": "1998-01-13T00:00:00",
-            "accessLevel": "public",
-            "identifier": "267",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Offender Based Transaction Statistics (OBTS), 1990: Alabama, Alaska, California, Idaho, Minnesota, Missouri, Nebraska, New Jersey, New York, Pennsylvania, Vermont, and Virginia"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "In 1996, the Bureau of Justice Statistics sponsored a\r\n pretest of a survey instrument designed to compile data on citizen\r\n contacts with police, including contacts in which police use force.\r\n The survey, which involved interviews (both face-to-face and by phone)\r\n carried out by the United States Census Bureau, was conducted as a\r\n special supplement to the National Crime Victimization Survey (NCVS),\r\n an ongoing household survey of the American public that elicits\r\n information concerning recent crime victimization\r\n experiences. Questions asked in the supplement covered reasons for\r\n contact with police officer(s), characteristics of the officer, weapons\r\n used by the officer, whether there were any injuries involved in the\r\n confrontation between the household member and the officer, whether\r\n drugs were involved in the incident, type of offense the respondent\r\n was charged with, and whether any citizen action was\r\ntaken. Demographic variables include race, sex, and age.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR06999.v1",
+                    "title": "Police Use of Force Data, 1996: [United States]"
+                }
+            ],
+            "identifier": "267",
+            "issued": "1998-01-13T00:00:00",
             "keyword": [
                 "crime",
                 "police citizen interactions",
@@ -13988,53 +13981,54 @@
                 "public opinion",
                 "victimization"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "1998-01-13T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "1998-01-13T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR06999.v1",
-                    "title": "Police Use of Force Data, 1996: [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Police-Public Contact Survey, 1999:  [United States]    ",
-            "description": "This survey was undertaken to learn more about how often\r\n and under what circumstances police-public contact becomes\r\n problematic. The Bureau of Justice Statistics (BJS) initiated surveys\r\n of the public on their interactions with police in 1996 with the first\r\n Police-Public Contact Survey, a pretest among a nationally\r\n representative sample of 6,421 persons aged 12 or older. That initial\r\n version of the questionnaire revealed that about 20 percent of the\r\n public had direct, face-to-face contact with a police officer at least\r\n once during the year preceding the survey. At that time, the principal\r\n investigator estimated that about 1 in 500 residents, or about a half\r\n million people, who had an encounter with a police officer also\r\n experienced either a threat of force or the actual use of force by the\r\n officer. The current survey, an improved version of the 1996\r\n Police-Public Contact Survey, was fielded as a supplement to the\r\n National Crime Victimization Survey (ICPSR 6406) during the last six\r\n months of 1999. A national sample nearly 15 times as large as the\r\n pretest sample in 1996 was used. The 1999 survey yielded nearly\r\n identical estimates of the prevalence and nature of contacts between\r\n the public and the police. This survey, because of its much larger\r\n sample size, permits more extensive analysis of demographic\r\n differences in police contacts than the 1996 pretest. In addition, it\r\n added a new and more detailed set of questions about traffic stops by\r\n police, the most frequent reason given for contact with police.\r\n Variables in the dataset cover type of contact with police, including\r\n whether it was face-to-face, initiated by the police or the citizen,\r\n whether an injury to the officer or the citizen resulted from the\r\n contact, crimes reported, and police use of force. Demographic\r\n variables supplied for the citizens include gender, race, and Hispanic\r\norigin.",
-            "modified": "2001-06-18T00:00:00",
-            "accessLevel": "public",
-            "identifier": "268",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Police Use of Force Data, 1996: [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This survey was undertaken to learn more about how often\r\n and under what circumstances police-public contact becomes\r\n problematic. The Bureau of Justice Statistics (BJS) initiated surveys\r\n of the public on their interactions with police in 1996 with the first\r\n Police-Public Contact Survey, a pretest among a nationally\r\n representative sample of 6,421 persons aged 12 or older. That initial\r\n version of the questionnaire revealed that about 20 percent of the\r\n public had direct, face-to-face contact with a police officer at least\r\n once during the year preceding the survey. At that time, the principal\r\n investigator estimated that about 1 in 500 residents, or about a half\r\n million people, who had an encounter with a police officer also\r\n experienced either a threat of force or the actual use of force by the\r\n officer. The current survey, an improved version of the 1996\r\n Police-Public Contact Survey, was fielded as a supplement to the\r\n National Crime Victimization Survey (ICPSR 6406) during the last six\r\n months of 1999. A national sample nearly 15 times as large as the\r\n pretest sample in 1996 was used. The 1999 survey yielded nearly\r\n identical estimates of the prevalence and nature of contacts between\r\n the public and the police. This survey, because of its much larger\r\n sample size, permits more extensive analysis of demographic\r\n differences in police contacts than the 1996 pretest. In addition, it\r\n added a new and more detailed set of questions about traffic stops by\r\n police, the most frequent reason given for contact with police.\r\n Variables in the dataset cover type of contact with police, including\r\n whether it was face-to-face, initiated by the police or the citizen,\r\n whether an injury to the officer or the citizen resulted from the\r\n contact, crimes reported, and police use of force. Demographic\r\n variables supplied for the citizens include gender, race, and Hispanic\r\norigin.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR03151.v2",
+                    "title": "Police-Public Contact Survey, 1999:  [United States]    "
+                }
+            ],
+            "identifier": "268",
+            "isPartOf": "2432",
+            "issued": "2001-04-17T00:00:00",
             "keyword": [
                 "police citizen interactions",
                 "police community relations",
@@ -14043,54 +14037,54 @@
                 "public interest",
                 "public opinion"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2001-06-18T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2001-04-17T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR03151.v2",
-                    "title": "Police-Public Contact Survey, 1999:  [United States]    "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Police-Public Contact Survey, 2002 [United States]",
-            "description": "The Police-Public Contact Survey (PPCS), was designed by\r\n the Bureau of Justice Statistics (BJS) to document contacts between\r\n police and the public that culminated in police using force. The 2002\r\n survey was conducted as a supplement to the National Crime\r\n Victimization Survey (NCVS). To date, the PPCS has been conducted\r\n three times by BJS. The first survey -- described in the BJS\r\n publication, \"Police Use of Force: Collection of National Data\" (NCJ\r\n 165040) -- documented levels of contacts with police during 1996. The\r\n second survey -- described in \"Contacts Between Police and the Public:\r\n Findings from the 1999 National Survey\" (NCJ 184957) -- recorded\r\n police-citizen contacts in 1999. These data are archived in\r\n POLICE-PUBLIC CONTACT SURVEY, 1999: [UNITED STATES] (ICPSR 3151). The\r\n third survey -- described here under the title \"Contacts Between\r\n Police and the Public: Findings From the 2002 National Survey\" (NCJ\r\n 207845) -- covered interactions between police and the public in 2002.\r\nThe results of this survey are contained in this data collection.",
-            "modified": "2005-08-18T00:00:00",
-            "accessLevel": "public",
-            "identifier": "269",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Police-Public Contact Survey, 1999:  [United States]    "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The Police-Public Contact Survey (PPCS), was designed by\r\n the Bureau of Justice Statistics (BJS) to document contacts between\r\n police and the public that culminated in police using force. The 2002\r\n survey was conducted as a supplement to the National Crime\r\n Victimization Survey (NCVS). To date, the PPCS has been conducted\r\n three times by BJS. The first survey -- described in the BJS\r\n publication, \"Police Use of Force: Collection of National Data\" (NCJ\r\n 165040) -- documented levels of contacts with police during 1996. The\r\n second survey -- described in \"Contacts Between Police and the Public:\r\n Findings from the 1999 National Survey\" (NCJ 184957) -- recorded\r\n police-citizen contacts in 1999. These data are archived in\r\n POLICE-PUBLIC CONTACT SURVEY, 1999: [UNITED STATES] (ICPSR 3151). The\r\n third survey -- described here under the title \"Contacts Between\r\n Police and the Public: Findings From the 2002 National Survey\" (NCJ\r\n 207845) -- covered interactions between police and the public in 2002.\r\nThe results of this survey are contained in this data collection.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR04273.v1",
+                    "title": "Police-Public Contact Survey, 2002 [United States]"
+                }
+            ],
+            "identifier": "269",
+            "isPartOf": "2432",
+            "issued": "2005-07-14T00:00:00",
             "keyword": [
                 "police citizen interactions",
                 "police community relations",
@@ -14099,54 +14093,54 @@
                 "public interest",
                 "public opinion"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2005-08-18T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2005-07-14T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR04273.v1",
-                    "title": "Police-Public Contact Survey, 2002 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Police-Public Contact Survey, 2005 [United States]",
-            "description": "The Police-Public Contact Survey (PPCS), was designed by\r\n the Bureau of Justice Statistics (BJS) to document contacts between\r\n police and the public that culminated in police using force. The 2005\r\n survey was conducted as a supplement to the National Crime\r\n Victimization Survey (NCVS). To date, the PPCS has been conducted four\r\n times by BJS. The first survey -- described in the BJS publication,\r\n \"Police Use of Force: Collection of National Data\" (NCJ 165040) --\r\n documented levels of contacts with police during 1996. The second\r\n survey -- described in \"Contacts Between Police and the Public:\r\n Findings from the 1999 National Survey\" (NCJ 184957) -- recorded\r\n police-citizen contacts in 1999. These data are archived in\r\n POLICE-PUBLIC CONTACT SURVEY, 1999 (ICPSR 3151). The third survey --\r\n described in the BJS publication, \"Contacts Between Police and the\r\n Public, Findings from the 2002 National Survey\" (NCJ 207845) --\r\n recorded police-citizen contacts in 2002. These data are archived in\r\n POLICE-PUBLIC CONTACT SURVEY, 2002: [UNITED STATES] (ICPSR 4273). The\r\n fourth survey -- described in the BJS publication, \"Contacts Between\r\n Police and the Public, 2005\" (NCJ 215243) -- covered interactions\r\n between police and the public in 2005. The results of this survey are\r\ncontained in this data collection.",
-            "modified": "2008-05-06T14:37:19",
-            "accessLevel": "public",
-            "identifier": "270",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Police-Public Contact Survey, 2002 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The Police-Public Contact Survey (PPCS), was designed by\r\n the Bureau of Justice Statistics (BJS) to document contacts between\r\n police and the public that culminated in police using force. The 2005\r\n survey was conducted as a supplement to the National Crime\r\n Victimization Survey (NCVS). To date, the PPCS has been conducted four\r\n times by BJS. The first survey -- described in the BJS publication,\r\n \"Police Use of Force: Collection of National Data\" (NCJ 165040) --\r\n documented levels of contacts with police during 1996. The second\r\n survey -- described in \"Contacts Between Police and the Public:\r\n Findings from the 1999 National Survey\" (NCJ 184957) -- recorded\r\n police-citizen contacts in 1999. These data are archived in\r\n POLICE-PUBLIC CONTACT SURVEY, 1999 (ICPSR 3151). The third survey --\r\n described in the BJS publication, \"Contacts Between Police and the\r\n Public, Findings from the 2002 National Survey\" (NCJ 207845) --\r\n recorded police-citizen contacts in 2002. These data are archived in\r\n POLICE-PUBLIC CONTACT SURVEY, 2002: [UNITED STATES] (ICPSR 4273). The\r\n fourth survey -- described in the BJS publication, \"Contacts Between\r\n Police and the Public, 2005\" (NCJ 215243) -- covered interactions\r\n between police and the public in 2005. The results of this survey are\r\ncontained in this data collection.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR20020.v2",
+                    "title": "Police-Public Contact Survey, 2005 [United States]"
+                }
+            ],
+            "identifier": "270",
+            "isPartOf": "2432",
+            "issued": "2007-06-18T00:00:00",
             "keyword": [
                 "police citizen interactions",
                 "police community relations",
@@ -14155,54 +14149,54 @@
                 "public interest",
                 "public opinion"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-05-06T14:37:19",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2007-06-18T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR20020.v2",
-                    "title": "Police-Public Contact Survey, 2005 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Police-Public Contact Survey, 2008",
-            "description": "The Police-Public Contact Survey (PPCS) provides detailed information on the nature and characteristics of face-to-face contacts between police and the public, including the reason for and outcome of the contact. The PPCS interviews a nationally representative sample of United States residents aged 16 years or older as a supplement to the National Crime Victimization Survey. To date, the PPCS has been conducted five times by the Bureau of Justice Statistics (BJS):\r\n\r\nThe first survey -- described in the BJS publication Police Use of Force: Collection of National Data\r\n(NCJ 165040) -- documented levels of contacts with police during 1996.\r\nThe second survey -- described in Contacts between Police and the Public: Findings from the\r\n1999 National Survey (NCJ 184957) -- recorded police-citizen contacts in 1999. These data are\r\narchived as POLICE-PUBLIC CONTACT SURVEY, 1999: [UNITED STATES] (ICPSR 3151).\r\nThe third survey -- described in Contacts between Police and the Public: Findings from the 2002\r\nNational Survey (NCJ 207845) -- covered interactions between police and the public in 2002. These data are archived as POLICE-PUBLIC CONTACT SURVEY, 2002: [UNITED STATES] (ICPSR 4273).\r\nThe fourth survey -- described in the BJS publication, Contacts between Police and the Public, 2005 (NCJ 215243) -- covered interactions between police and the public in 2005. These data are archived as POLICE-PUBLIC CONTACT SURVEY, 2005: [UNITED STATES] (ICPSR 20020).\r\nThe fifth survey -- described in the BJS publication, Contacts between Police and the Public, 2008 (NCJ 234599) -- covered interactions between police and the public in 2008. These data are archived as POLICE-PUBLIC CONTACT SURVEY, 2008 (ICPSR 32022).",
-            "modified": "2011-10-05T13:42:19",
-            "accessLevel": "public",
-            "identifier": "271",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Police-Public Contact Survey, 2005 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The Police-Public Contact Survey (PPCS) provides detailed information on the nature and characteristics of face-to-face contacts between police and the public, including the reason for and outcome of the contact. The PPCS interviews a nationally representative sample of United States residents aged 16 years or older as a supplement to the National Crime Victimization Survey. To date, the PPCS has been conducted five times by the Bureau of Justice Statistics (BJS):\r\n\r\nThe first survey -- described in the BJS publication Police Use of Force: Collection of National Data\r\n(NCJ 165040) -- documented levels of contacts with police during 1996.\r\nThe second survey -- described in Contacts between Police and the Public: Findings from the\r\n1999 National Survey (NCJ 184957) -- recorded police-citizen contacts in 1999. These data are\r\narchived as POLICE-PUBLIC CONTACT SURVEY, 1999: [UNITED STATES] (ICPSR 3151).\r\nThe third survey -- described in Contacts between Police and the Public: Findings from the 2002\r\nNational Survey (NCJ 207845) -- covered interactions between police and the public in 2002. These data are archived as POLICE-PUBLIC CONTACT SURVEY, 2002: [UNITED STATES] (ICPSR 4273).\r\nThe fourth survey -- described in the BJS publication, Contacts between Police and the Public, 2005 (NCJ 215243) -- covered interactions between police and the public in 2005. These data are archived as POLICE-PUBLIC CONTACT SURVEY, 2005: [UNITED STATES] (ICPSR 20020).\r\nThe fifth survey -- described in the BJS publication, Contacts between Police and the Public, 2008 (NCJ 234599) -- covered interactions between police and the public in 2008. These data are archived as POLICE-PUBLIC CONTACT SURVEY, 2008 (ICPSR 32022).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR32022.v1",
+                    "title": "Police-Public Contact Survey, 2008"
+                }
+            ],
+            "identifier": "271",
+            "isPartOf": "2432",
+            "issued": "2011-10-05T13:42:19",
             "keyword": [
                 "police citizen interactions",
                 "police community relations",
@@ -14211,54 +14205,54 @@
                 "public interest",
                 "public opinion"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-10-05T13:42:19",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2011-10-05T13:42:19",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR32022.v1",
-                    "title": "Police-Public Contact Survey, 2008"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Prisoner Recidivism",
-            "description": "recidivism rates for persons released from state prisons with specific demographic, criminal history, and sentence attributes.",
-            "modified": "2005-01-01T00:00:00",
-            "accessLevel": "public",
-            "identifier": "272",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Police-Public Contact Survey, 2008"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "recidivism rates for persons released from state prisons with specific demographic, criminal history, and sentence attributes.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.bjs.gov/index.cfm?ty=datool&surl=/recidivism/index.cfm",
+                    "mediaType": "text/html",
+                    "title": "Prisoner Recidivism"
+                }
+            ],
+            "identifier": "272",
+            "issued": "2005-01-01T00:00:00",
             "keyword": [
                 "nonnegligent manslaughte",
                 "negligent manslaughter",
@@ -14269,160 +14263,159 @@
                 "Drug trafficking",
                 "Drug possession"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2005-01-01T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "2005-01-01T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://www.bjs.gov/index.cfm?ty=datool&surl=/recidivism/index.cfm",
-                    "mediaType": "text/html",
-                    "title": "Prisoner Recidivism"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Public Image of Courts, 1977: General Public Data",
-            "description": "This data collection and its companion study, PUBLIC IMAGE\r\nOF COURTS, 1977: SPECIAL PUBLICS DATA (ICPSR 7704), were undertaken to\r\nexplore attitudes toward\r\ncourts and justice. These surveys sought to measure perceptions of and\r\nexperiences with local, state, and federal courts as well as general\r\nattitudes toward the administration of justice and legal actors. The\r\ngeneral objectives of the studies were to (1) determine levels of public\r\nknowledge of courts, (2) test reactions to situations that might, or\r\nmight not, prompt recourse to courts, (3) determine the incidence,\r\nnature, and evaluations of court experience, (4) describe and account\r\nfor evaluations of court performance, (5) indicate attitudes toward\r\nlegal actors, and (6) indicate reactions to alternative means of dispute\r\nresolution. Two samples were drawn: a national sample of the general\r\npublic and a \"special publics\" sample of judges, lawyers, and\r\ncommunity leaders (ICPSR 7704). The 1,931 respondents in the general\r\npublic sample were interviewed in person by the National Consumer\r\nField Staff of Yankelovich, Skelly, and White, Inc.",
-            "modified": "1997-02-25T00:00:00",
-            "accessLevel": "public",
-            "identifier": "273",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Prisoner Recidivism"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This data collection and its companion study, PUBLIC IMAGE\r\nOF COURTS, 1977: SPECIAL PUBLICS DATA (ICPSR 7704), were undertaken to\r\nexplore attitudes toward\r\ncourts and justice. These surveys sought to measure perceptions of and\r\nexperiences with local, state, and federal courts as well as general\r\nattitudes toward the administration of justice and legal actors. The\r\ngeneral objectives of the studies were to (1) determine levels of public\r\nknowledge of courts, (2) test reactions to situations that might, or\r\nmight not, prompt recourse to courts, (3) determine the incidence,\r\nnature, and evaluations of court experience, (4) describe and account\r\nfor evaluations of court performance, (5) indicate attitudes toward\r\nlegal actors, and (6) indicate reactions to alternative means of dispute\r\nresolution. Two samples were drawn: a national sample of the general\r\npublic and a \"special publics\" sample of judges, lawyers, and\r\ncommunity leaders (ICPSR 7704). The 1,931 respondents in the general\r\npublic sample were interviewed in person by the National Consumer\r\nField Staff of Yankelovich, Skelly, and White, Inc.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR07703.v1",
+                    "title": "Public Image of Courts, 1977: General Public Data"
+                }
+            ],
+            "identifier": "273",
+            "issued": "1984-03-18T00:00:00",
             "keyword": [
                 "court system",
                 "judges",
                 "judicial process",
                 "justice"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "1997-02-25T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "1984-03-18T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR07703.v1",
-                    "title": "Public Image of Courts, 1977: General Public Data"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Public Image of Courts, 1977:  Special Publics Data",
-            "description": "This data collection and its companion study, PUBLIC\r\nIMAGE OF COURTS, 1977: GENERAL PUBLIC DATA (ICPSR 7703), were\r\nundertaken to explore attitudes toward courts and justice. These surveys\r\nsought to measure perceptions of and experiences\r\nwith local, state, and federal courts as well as general attitudes toward\r\nthe administration of justice and legal actors. The general objectives of\r\nthe studies were to (1) determine levels of public knowledge of courts,\r\n(2) test reactions to situations that might, or might not, prompt recourse\r\nto courts, (3) determine the incidence, nature, and evaluations of court\r\nexperience, (4) describe and account for evaluations of court performance,\r\n(5) indicate attitudes toward legal actors, and (6) indicate reactions to\r\nalternative means of dispute resolution. Two samples were drawn: a national\r\nsample of the general public (ICPSR 7703) and a \"special publics\" sample\r\nof judges, lawyers, and community leaders. The 1,112 respondents in the special\r\npublics sample were interviewed by a group of interviewers described\r\nas \"retired business executives specially trained to interview leadership\r\ngroups.\"",
-            "modified": "2005-11-04T00:00:00",
-            "accessLevel": "public",
-            "identifier": "274",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Public Image of Courts, 1977: General Public Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This data collection and its companion study, PUBLIC\r\nIMAGE OF COURTS, 1977: GENERAL PUBLIC DATA (ICPSR 7703), were\r\nundertaken to explore attitudes toward courts and justice. These surveys\r\nsought to measure perceptions of and experiences\r\nwith local, state, and federal courts as well as general attitudes toward\r\nthe administration of justice and legal actors. The general objectives of\r\nthe studies were to (1) determine levels of public knowledge of courts,\r\n(2) test reactions to situations that might, or might not, prompt recourse\r\nto courts, (3) determine the incidence, nature, and evaluations of court\r\nexperience, (4) describe and account for evaluations of court performance,\r\n(5) indicate attitudes toward legal actors, and (6) indicate reactions to\r\nalternative means of dispute resolution. Two samples were drawn: a national\r\nsample of the general public (ICPSR 7703) and a \"special publics\" sample\r\nof judges, lawyers, and community leaders. The 1,112 respondents in the special\r\npublics sample were interviewed by a group of interviewers described\r\nas \"retired business executives specially trained to interview leadership\r\ngroups.\"",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR07704.v1",
+                    "title": "Public Image of Courts, 1977:  Special Publics Data"
+                }
+            ],
+            "identifier": "274",
+            "issued": "1984-03-18T00:00:00",
             "keyword": [
                 "court system",
                 "judges",
                 "judicial process",
                 "justice"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2005-11-04T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "1984-03-18T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR07704.v1",
-                    "title": "Public Image of Courts, 1977:  Special Publics Data"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Race of Prisoners Admitted to State and Federal Institutions in the United States, 1926-1986   ",
-            "description": "This data collection includes tabulations of annual adult\r\n admissions to federal and state correctional institutions by\r\n race. Data are provided for the years 1926 to 1986 and include\r\n tabulations for prisons in each of the 50 states and the District of\r\n Columbia, as well as federal prison totals and United States\r\n totals. The figures were derived from a voluntary reporting program in\r\n which each state, the District of Columbia, and the Federal Bureau of\r\n Prisons reported summary and detailed statistics as a part of the\r\n National Prisoner Statistics series. Individual state and United\r\n States population figures according to racial categories also are\r\nprovided.",
-            "modified": "1999-10-04T00:00:00",
-            "accessLevel": "public",
-            "identifier": "275",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Public Image of Courts, 1977:  Special Publics Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This data collection includes tabulations of annual adult\r\n admissions to federal and state correctional institutions by\r\n race. Data are provided for the years 1926 to 1986 and include\r\n tabulations for prisons in each of the 50 states and the District of\r\n Columbia, as well as federal prison totals and United States\r\n totals. The figures were derived from a voluntary reporting program in\r\n which each state, the District of Columbia, and the Federal Bureau of\r\n Prisons reported summary and detailed statistics as a part of the\r\n National Prisoner Statistics series. Individual state and United\r\n States population figures according to racial categories also are\r\nprovided.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR09165.v1",
+                    "title": "Race of Prisoners Admitted to State and Federal Institutions in the United States, 1926-1986   "
+                }
+            ],
+            "identifier": "275",
+            "issued": "1991-05-03T00:00:00",
             "keyword": [
                 "correctional facilities",
                 "correctional facilities (adults)",
@@ -14431,53 +14424,53 @@
                 "race",
                 "state correctional facilities"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "1999-10-04T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "1991-05-03T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR09165.v1",
-                    "title": "Race of Prisoners Admitted to State and Federal Institutions in the United States, 1926-1986   "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Recidivism Among Young Parolees: a Study of Inmates Released from Prison in 22 States, 1978",
-            "description": "This study examines the criminal activities of a group of\r\nyoung offenders after their release from prison to parole supervision.\r\nPrevious studies have examined recidivism using arrests as the\r\nprincipal measure, whereas this study examines a variety of factors,\r\nincluding length of incarceration, age, sex, race, prior arrest\r\nrecord, prosecutions, length of time between parole and rearrest,\r\nparolees not prosecuted for new offenses but having their parole\r\nrevoked, rearrests in states other than the paroling states, and the\r\nnature and location of rearrest charges. Parolees in the 22 states\r\ncovered in this study account for 50 percent of all state prisoners\r\nparoled in the United States in 1978.",
-            "modified": "1997-05-30T00:00:00",
-            "accessLevel": "public",
-            "identifier": "276",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Race of Prisoners Admitted to State and Federal Institutions in the United States, 1926-1986   "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This study examines the criminal activities of a group of\r\nyoung offenders after their release from prison to parole supervision.\r\nPrevious studies have examined recidivism using arrests as the\r\nprincipal measure, whereas this study examines a variety of factors,\r\nincluding length of incarceration, age, sex, race, prior arrest\r\nrecord, prosecutions, length of time between parole and rearrest,\r\nparolees not prosecuted for new offenses but having their parole\r\nrevoked, rearrests in states other than the paroling states, and the\r\nnature and location of rearrest charges. Parolees in the 22 states\r\ncovered in this study account for 50 percent of all state prisoners\r\nparoled in the United States in 1978.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR08673.v2",
+                    "title": "Recidivism Among Young Parolees: a Study of Inmates Released from Prison in 22 States, 1978"
+                }
+            ],
+            "identifier": "276",
+            "issued": "1988-01-06T00:00:00",
             "keyword": [
                 "arrests",
                 "crime",
@@ -14485,53 +14478,53 @@
                 "demographic characteristics",
                 "parole systems"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "1997-05-30T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "1988-01-06T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR08673.v2",
-                    "title": "Recidivism Among Young Parolees: a Study of Inmates Released from Prison in 22 States, 1978"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Recidivism in the National Longitudinal Survey of Youth 1997 - Standalone Data (Rounds 1 to 13)",
-            "description": "The NLSY97 standalone data files are intended to be used by crime researchers for analyses without requiring supplementation from the main NLSY97 data set. The data contain age-based calendar year variables on arrests and incarcerations, self-reported criminal activity, substance use, demographic variables and relevant variables from other domains which are created using the NLSY97 data. The main NLSY97 data are available for public use and can be accessed online at the NLS Investigator Web site and at the NACJD Web site (as ICPSR 3959). Questionnaires, user guides and other documentation are available at the same links. The National Longitudinal Survey of Youth 1997 (NLSY97) was designed by the United States Department of Labor, comprising the National Longitudinal Survey (NLS) Series. Created to be representative of United States residents in 1997 who were born between the years of 1980 and 1984, the NLSY97 documents the\r\ntransition from school to work experienced by today's youths through\r\ndata collection from 1997. The majority of the oldest cohort members (age 16 as of December 31, 1996) were still in school during the first survey round and the\r\nyoungest respondents (age 12) had not yet entered the labor market.",
-            "modified": "2014-02-06T11:26:28",
-            "accessLevel": "public",
-            "identifier": "277",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Recidivism Among Young Parolees: a Study of Inmates Released from Prison in 22 States, 1978"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The NLSY97 standalone data files are intended to be used by crime researchers for analyses without requiring supplementation from the main NLSY97 data set. The data contain age-based calendar year variables on arrests and incarcerations, self-reported criminal activity, substance use, demographic variables and relevant variables from other domains which are created using the NLSY97 data. The main NLSY97 data are available for public use and can be accessed online at the NLS Investigator Web site and at the NACJD Web site (as ICPSR 3959). Questionnaires, user guides and other documentation are available at the same links. The National Longitudinal Survey of Youth 1997 (NLSY97) was designed by the United States Department of Labor, comprising the National Longitudinal Survey (NLS) Series. Created to be representative of United States residents in 1997 who were born between the years of 1980 and 1984, the NLSY97 documents the\r\ntransition from school to work experienced by today's youths through\r\ndata collection from 1997. The majority of the oldest cohort members (age 16 as of December 31, 1996) were still in school during the first survey round and the\r\nyoungest respondents (age 12) had not yet entered the labor market.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR34562.v1",
+                    "title": "Recidivism in the National Longitudinal Survey of Youth 1997 - Standalone Data (Rounds 1 to 13)"
+                }
+            ],
+            "identifier": "277",
+            "issued": "2014-02-06T11:26:28",
             "keyword": [
                 "alcohol",
                 "arrests",
@@ -14545,53 +14538,53 @@
                 "young adults",
                 "youths"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2014-02-06T11:26:28",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "2014-02-06T11:26:28",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR34562.v1",
-                    "title": "Recidivism in the National Longitudinal Survey of Youth 1997 - Standalone Data (Rounds 1 to 13)"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Recidivism of Felons on Probation, 1986-1989:  [United States]",
-            "description": "This data collection provides an overview of how probation \r\n cases are processed in 32 urban and suburban jurisdictions in the \r\n United States and gauges the extent to which variations in probation \r\n patterns exist between jurisdictions. Data were collected on offenders \r\n who were sentenced in 1986 and who committed one or more of the \r\n following types of offenses: homicide, rape, robbery, aggravated \r\n assault, burglary, larceny, drug trafficking, and other felony crimes. \r\n Probation history questionnaires were completed during the last half of \r\n 1989. Information is available on number of conviction charges, race, \r\n age, sex, marital status, educational level, and ethnicity of the \r\n probationer. In addition, data on drug and alcohol use and treatment, \r\nsentencing, restitution, and offenses are provided.",
-            "modified": "2005-11-04T00:00:00",
-            "accessLevel": "public",
-            "identifier": "278",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Recidivism in the National Longitudinal Survey of Youth 1997 - Standalone Data (Rounds 1 to 13)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This data collection provides an overview of how probation \r\n cases are processed in 32 urban and suburban jurisdictions in the \r\n United States and gauges the extent to which variations in probation \r\n patterns exist between jurisdictions. Data were collected on offenders \r\n who were sentenced in 1986 and who committed one or more of the \r\n following types of offenses: homicide, rape, robbery, aggravated \r\n assault, burglary, larceny, drug trafficking, and other felony crimes. \r\n Probation history questionnaires were completed during the last half of \r\n 1989. Information is available on number of conviction charges, race, \r\n age, sex, marital status, educational level, and ethnicity of the \r\n probationer. In addition, data on drug and alcohol use and treatment, \r\nsentencing, restitution, and offenses are provided.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR09574.v2",
+                    "title": "Recidivism of Felons on Probation, 1986-1989:  [United States]"
+                }
+            ],
+            "identifier": "278",
+            "issued": "1992-05-12T00:00:00",
             "keyword": [
                 "assault",
                 "burglary",
@@ -14607,106 +14600,106 @@
                 "suburbs",
                 "urban areas"
             ],
-            "bureauCode": [
-                "011:21"
-            ],
-            "programCode": [
-                "011:061"
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "1992-05-12T00:00:00",
             "language": [
                 "eng"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR09574.v2",
-                    "title": "Recidivism of Felons on Probation, 1986-1989:  [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "State and Local Probation and Parole Systems, 1976",
-            "description": "This study is a census of all state and local probation and\r\n parole systems. It was conducted in late 1976 by the United States\r\n Census Bureau for the Bureau of Justice Statistics. The data contain\r\n information on each agency, including jurisdiction, funding and\r\noperation, employment, and client caseload.",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "modified": "2005-11-04T00:00:00",
-            "accessLevel": "public",
-            "identifier": "279",
+            "programCode": [
+                "011:061"
+            ],
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Recidivism of Felons on Probation, 1986-1989:  [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This study is a census of all state and local probation and\r\n parole systems. It was conducted in late 1976 by the United States\r\n Census Bureau for the Bureau of Justice Statistics. The data contain\r\n information on each agency, including jurisdiction, funding and\r\noperation, employment, and client caseload.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR07673.v1",
+                    "title": "State and Local Probation and Parole Systems, 1976"
+                }
+            ],
+            "identifier": "279",
+            "issued": "1984-03-18T00:00:00",
             "keyword": [
                 "criminal justice system",
                 "jurisdiction",
                 "parole",
                 "probation"
             ],
-            "bureauCode": [
-                "011:21"
-            ],
-            "programCode": [
-                "011:061"
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "1984-03-18T00:00:00",
             "language": [
                 "eng"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR07673.v1",
-                    "title": "State and Local Probation and Parole Systems, 1976"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "State and Local Prosecution and Civil Attorney Systems, 1976",
-            "description": "The purpose of this data collection was to establish a\r\n current name and address listing of state and local government\r\n prosecution and civil attorney agencies and to obtain information\r\n about agency function, jurisdiction, employment, funding, and attorney\r\n compensation arrangements. The data for each agency include\r\n information for any identifiable local police prosecutors. Excluded\r\n from the study were private law firms that perform legal services\r\n periodically for a government and are compensated by retainers and\r\n fees. Variables cover agency functions and jurisdiction, agency\r\n funding, number and types of employees, compensation and employment\r\n restrictions for attorneys, agency's geographical jurisdiction, number\r\nof branch offices, and number of branch office employees.",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "modified": "2005-11-04T00:00:00",
-            "accessLevel": "public",
-            "identifier": "280",
+            "programCode": [
+                "011:061"
+            ],
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "State and Local Probation and Parole Systems, 1976"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The purpose of this data collection was to establish a\r\n current name and address listing of state and local government\r\n prosecution and civil attorney agencies and to obtain information\r\n about agency function, jurisdiction, employment, funding, and attorney\r\n compensation arrangements. The data for each agency include\r\n information for any identifiable local police prosecutors. Excluded\r\n from the study were private law firms that perform legal services\r\n periodically for a government and are compensated by retainers and\r\n fees. Variables cover agency functions and jurisdiction, agency\r\n funding, number and types of employees, compensation and employment\r\n restrictions for attorneys, agency's geographical jurisdiction, number\r\nof branch offices, and number of branch office employees.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR07674.v2",
+                    "title": "State and Local Prosecution and Civil Attorney Systems, 1976"
+                }
+            ],
+            "identifier": "280",
+            "issued": "1984-03-18T00:00:00",
             "keyword": [
                 "attorneys",
                 "databases",
@@ -14716,53 +14709,53 @@
                 "prosecuting attorneys",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2005-11-04T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "1984-03-18T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR07674.v2",
-                    "title": "State and Local Prosecution and Civil Attorney Systems, 1976"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Survey of Adults on Probation, 1995:  [United States]",
-            "description": "The 1995 Survey of Adults on Probation (SAP) was the first\r\n national survey to gather information on the individual\r\n characteristics of adult probationers. The SAP was a two-part\r\n nationally representative survey consisting of a records check based\r\n on probation office administrative records and personal interviews\r\n with probationers. The records check provided detailed information\r\n for 5,867 probationers on current offenses and sentences, criminal\r\n histories, levels of supervision and contacts, disciplinary hearings\r\n and outcomes, and demographic characteristics. Only adults with a\r\n formal sentence to probation who were not considered absconders were\r\n included in the records check. Excluded were persons supervised by a\r\n federal probation agency, those only on parole, persons on presentence\r\n or pretrial diversion, juveniles, and absconders. The records check\r\n forms were completed by a probation officer or by another person\r\n knowledgeable about probation office records. A subset of the\r\n population selected for the records check was selected for a personal\r\n interview, resulting in a total of 2,030 completed interviews. The\r\n personal interview sample excluded from the records check sample\r\n probationers not on active probation (defined as being required to\r\n make office visits at any interval), those incarcerated, and those in\r\n residential treatment. Respondents were asked about current\r\n offense(s) and supervision, criminal history, alcohol and drug use and\r\n treatment, mental health treatment, demographic characteristics, and a\r\n variety of socioeconomic characteristics such as employment, income,\r\n receipt of welfare, housing, number of children and child support, and\r\nliving conditions while growing up.",
-            "modified": "2006-03-30T00:00:00",
-            "accessLevel": "public",
-            "identifier": "281",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "State and Local Prosecution and Civil Attorney Systems, 1976"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The 1995 Survey of Adults on Probation (SAP) was the first\r\n national survey to gather information on the individual\r\n characteristics of adult probationers. The SAP was a two-part\r\n nationally representative survey consisting of a records check based\r\n on probation office administrative records and personal interviews\r\n with probationers. The records check provided detailed information\r\n for 5,867 probationers on current offenses and sentences, criminal\r\n histories, levels of supervision and contacts, disciplinary hearings\r\n and outcomes, and demographic characteristics. Only adults with a\r\n formal sentence to probation who were not considered absconders were\r\n included in the records check. Excluded were persons supervised by a\r\n federal probation agency, those only on parole, persons on presentence\r\n or pretrial diversion, juveniles, and absconders. The records check\r\n forms were completed by a probation officer or by another person\r\n knowledgeable about probation office records. A subset of the\r\n population selected for the records check was selected for a personal\r\n interview, resulting in a total of 2,030 completed interviews. The\r\n personal interview sample excluded from the records check sample\r\n probationers not on active probation (defined as being required to\r\n make office visits at any interval), those incarcerated, and those in\r\n residential treatment. Respondents were asked about current\r\n offense(s) and supervision, criminal history, alcohol and drug use and\r\n treatment, mental health treatment, demographic characteristics, and a\r\n variety of socioeconomic characteristics such as employment, income,\r\n receipt of welfare, housing, number of children and child support, and\r\nliving conditions while growing up.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR02039.v1",
+                    "title": "Survey of Adults on Probation, 1995:  [United States]"
+                }
+            ],
+            "identifier": "281",
+            "issued": "1999-08-18T00:00:00",
             "keyword": [
                 "arrest records",
                 "criminal histories",
@@ -14773,53 +14766,54 @@
                 "sentencing",
                 "supervised liberty"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2006-03-30T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "1999-08-18T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR02039.v1",
-                    "title": "Survey of Adults on Probation, 1995:  [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Survey of Campus Law Enforcement Agencies, 1995: [United States]",
-            "description": "In 1995, to determine the nature of law enforcement\r\nservices provided on campus, the Bureau of Justice Statistics (BJS)\r\nsurveyed four-year institutions of higher education in the United\r\nStates with 2,500 or more students. This survey describes nearly 600\r\nof these campus law enforcement agencies in terms of their personnel,\r\nexpenditures and pay, operations, equipment, computers and information\r\nsystems, policies, and special programs. The survey was based on the\r\nBJS Law Enforcement Management and Administrative Statistics (LEMAS)\r\nprogram, which collected similar data from a national sample of state\r\nand local law enforcement agencies.",
-            "modified": "2005-11-04T00:00:00",
-            "accessLevel": "public",
-            "identifier": "282",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Survey of Adults on Probation, 1995:  [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "In 1995, to determine the nature of law enforcement\r\nservices provided on campus, the Bureau of Justice Statistics (BJS)\r\nsurveyed four-year institutions of higher education in the United\r\nStates with 2,500 or more students. This survey describes nearly 600\r\nof these campus law enforcement agencies in terms of their personnel,\r\nexpenditures and pay, operations, equipment, computers and information\r\nsystems, policies, and special programs. The survey was based on the\r\nBJS Law Enforcement Management and Administrative Statistics (LEMAS)\r\nprogram, which collected similar data from a national sample of state\r\nand local law enforcement agencies.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR06846.v1",
+                    "title": "Survey of Campus Law Enforcement Agencies, 1995: [United States]"
+                }
+            ],
+            "identifier": "282",
+            "isPartOf": "2431",
+            "issued": "1997-05-16T00:00:00",
             "keyword": [
                 "administration",
                 "budgets",
@@ -14832,54 +14826,54 @@
                 "wages and salaries",
                 "workers"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2005-11-04T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2431",
-            "dataQuality": false,
-            "issued": "1997-05-16T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR06846.v1",
-                    "title": "Survey of Campus Law Enforcement Agencies, 1995: [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Survey of Campus Law Enforcement Agencies, 2004-2005:  [United States]",
-            "description": "This survey covered the 2004-2005 academic year and collected data from law enforcement agencies using sworn police officers and those using only non-sworn security officers. Agencies serving 4-year United States universities and colleges with a fall 2004 enrollment of 2,500 or more, and\r\nthose serving 2-year public colleges with a fall 2004\r\nenrollment of 10,000 or more were surveyed. United States military\r\nacademies and for-profit institutions were excluded. Data were collected in conjunction with the 2004 BJS Census of State and Local Law Enforcement Agencies. The survey instrument was patterned after the BJS Law\r\nEnforcement Management and Administrative Statistics\r\nsurvey. Data were collected describing campus law\r\nenforcement agencies, including personnel, expenditures\r\nand pay, operations, equipment, computers and information\r\nsystems, policies, and special programs. BJS conducted an earlier survey of campus law enforcement agencies, covering the 1994-1995 school year. Users can access the data collection from the ICPSR Web site (ICPSR 6846).",
-            "modified": "2010-03-09T16:06:17",
-            "accessLevel": "public",
-            "identifier": "283",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Survey of Campus Law Enforcement Agencies, 1995: [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This survey covered the 2004-2005 academic year and collected data from law enforcement agencies using sworn police officers and those using only non-sworn security officers. Agencies serving 4-year United States universities and colleges with a fall 2004 enrollment of 2,500 or more, and\r\nthose serving 2-year public colleges with a fall 2004\r\nenrollment of 10,000 or more were surveyed. United States military\r\nacademies and for-profit institutions were excluded. Data were collected in conjunction with the 2004 BJS Census of State and Local Law Enforcement Agencies. The survey instrument was patterned after the BJS Law\r\nEnforcement Management and Administrative Statistics\r\nsurvey. Data were collected describing campus law\r\nenforcement agencies, including personnel, expenditures\r\nand pay, operations, equipment, computers and information\r\nsystems, policies, and special programs. BJS conducted an earlier survey of campus law enforcement agencies, covering the 1994-1995 school year. Users can access the data collection from the ICPSR Web site (ICPSR 6846).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR27261.v1",
+                    "title": "Survey of Campus Law Enforcement Agencies, 2004-2005:  [United States]"
+                }
+            ],
+            "identifier": "283",
+            "isPartOf": "2431",
+            "issued": "2010-03-09T16:06:17",
             "keyword": [
                 "administration",
                 "budgets",
@@ -14892,54 +14886,54 @@
                 "wages and salaries",
                 "workers"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2010-03-09T16:06:17",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2431",
-            "dataQuality": false,
-            "issued": "2010-03-09T16:06:17",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR27261.v1",
-                    "title": "Survey of Campus Law Enforcement Agencies, 2004-2005:  [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Survey of Inmates in Local Jails, 1983:  [United States]",
-            "description": "This survey provides data on inmates' socioeconomic and\r\n demographic characteristics, previous military service, prior criminal\r\n history, jail activities, drug and alcohol use, health care, and\r\ncurrent offenses.",
-            "modified": "2005-11-04T00:00:00",
-            "accessLevel": "public",
-            "identifier": "284",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Survey of Campus Law Enforcement Agencies, 2004-2005:  [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This survey provides data on inmates' socioeconomic and\r\n demographic characteristics, previous military service, prior criminal\r\n history, jail activities, drug and alcohol use, health care, and\r\ncurrent offenses.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR08274.v1",
+                    "title": "Survey of Inmates in Local Jails, 1983:  [United States]"
+                }
+            ],
+            "identifier": "284",
+            "isPartOf": "2170",
+            "issued": "1985-10-09T00:00:00",
             "keyword": [
                 "correctional facilities",
                 "criminal histories",
@@ -14952,54 +14946,54 @@
                 "offenses",
                 "sentencing"
             ],
-            "bureauCode": [
-                "011:21"
-            ],
-            "programCode": [
-                "011:061"
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2170",
-            "dataQuality": false,
-            "issued": "1985-10-09T00:00:00",
             "language": [
                 "eng"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR08274.v1",
-                    "title": "Survey of Inmates in Local Jails, 1983:  [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Survey of Inmates in Local Jails, 1989:  [United States]",
-            "description": "This collection provides nationally representative data on\r\n persons held prior to trial and on convicted offenders serving\r\n sentences in local jails or awaiting transfer to state prisons. Data\r\n cover demographic characteristics of jail inmates (sex, race,\r\n ethnicity, Hispanic origin, employment), current offenses and\r\n sentences, characteristics of victims, criminal histories, jail\r\n activities and programs, prior drug and alcohol use and treatment, and\r\nhealth care services provided while in jail.",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "modified": "2005-11-04T00:00:00",
-            "accessLevel": "public",
-            "identifier": "285",
+            "programCode": [
+                "011:061"
+            ],
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Survey of Inmates in Local Jails, 1983:  [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This collection provides nationally representative data on\r\n persons held prior to trial and on convicted offenders serving\r\n sentences in local jails or awaiting transfer to state prisons. Data\r\n cover demographic characteristics of jail inmates (sex, race,\r\n ethnicity, Hispanic origin, employment), current offenses and\r\n sentences, characteristics of victims, criminal histories, jail\r\n activities and programs, prior drug and alcohol use and treatment, and\r\nhealth care services provided while in jail.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR09419.v1",
+                    "title": "Survey of Inmates in Local Jails, 1989:  [United States]"
+                }
+            ],
+            "identifier": "285",
+            "isPartOf": "2170",
+            "issued": "1991-10-23T00:00:00",
             "keyword": [
                 "correctional facilities",
                 "criminal histories",
@@ -15012,54 +15006,54 @@
                 "offenses",
                 "sentencing"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2005-11-04T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2170",
-            "dataQuality": false,
-            "issued": "1991-10-23T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR09419.v1",
-                    "title": "Survey of Inmates in Local Jails, 1989:  [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Survey of Inmates in Local Jails, 1996: [United States]",
-            "description": "This collection provides nationally representative data on\r\n persons held prior to trial and on convicted offenders serving\r\n sentences in local jails or awaiting transfer to state prisons. Data\r\n cover demographic characteristics of jail inmates (sex, race,\r\n ethnicity, Hispanic origin, employment), current offenses and\r\n sentences, detention status, trial, bail, characteristics of victims,\r\n criminal histories, incident characteristics, socioeconomic\r\n circumstances, jail conditions and activities, and prior drug and\r\n alcohol use and treatment. Part 1, Numeric Data, contains numeric data\r\n for all questions in the survey, while Part 2, Alphanumeric Data,\r\n consists of nonnumeric answers to the \"Other, Specify\" selection\r\navailable for some of the questions.",
-            "modified": "2006-03-30T00:00:00",
-            "accessLevel": "public",
-            "identifier": "286",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Survey of Inmates in Local Jails, 1989:  [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This collection provides nationally representative data on\r\n persons held prior to trial and on convicted offenders serving\r\n sentences in local jails or awaiting transfer to state prisons. Data\r\n cover demographic characteristics of jail inmates (sex, race,\r\n ethnicity, Hispanic origin, employment), current offenses and\r\n sentences, detention status, trial, bail, characteristics of victims,\r\n criminal histories, incident characteristics, socioeconomic\r\n circumstances, jail conditions and activities, and prior drug and\r\n alcohol use and treatment. Part 1, Numeric Data, contains numeric data\r\n for all questions in the survey, while Part 2, Alphanumeric Data,\r\n consists of nonnumeric answers to the \"Other, Specify\" selection\r\navailable for some of the questions.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR06858.v1",
+                    "title": "Survey of Inmates in Local Jails, 1996: [United States]"
+                }
+            ],
+            "identifier": "286",
+            "isPartOf": "2170",
+            "issued": "1999-06-02T00:00:00",
             "keyword": [
                 "correctional facilities",
                 "criminal histories",
@@ -15072,54 +15066,54 @@
                 "offenses",
                 "sentencing"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2006-03-30T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2170",
-            "dataQuality": false,
-            "issued": "1999-06-02T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR06858.v1",
-                    "title": "Survey of Inmates in Local Jails, 1996: [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Survey of Inmates of State Correctional Facilities and Census of State Adult Correctional Facilities, 1974",
-            "description": "The survey and census were part of a series of data \r\n collection efforts undertaken to assist policymakers in assessing and \r\n remedying deficiencies in the nation's correctional institutions. The \r\n survey was designed to provide information on social and economic \r\n characteristics of inmates, criminal and correctional background, court \r\n experience, and prison routine. The census gathered a wide range of \r\n information on all federal correctional facilities operating in 1974. \r\n The focus of the survey file is on the inmate, while the focus of the \r\ncensus file is on the facility.",
-            "modified": "1992-02-16T00:00:00",
-            "accessLevel": "public",
-            "identifier": "287",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Survey of Inmates in Local Jails, 1996: [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The survey and census were part of a series of data \r\n collection efforts undertaken to assist policymakers in assessing and \r\n remedying deficiencies in the nation's correctional institutions. The \r\n survey was designed to provide information on social and economic \r\n characteristics of inmates, criminal and correctional background, court \r\n experience, and prison routine. The census gathered a wide range of \r\n information on all federal correctional facilities operating in 1974. \r\n The focus of the survey file is on the inmate, while the focus of the \r\ncensus file is on the facility.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR07811.v3",
+                    "title": "Survey of Inmates of State Correctional Facilities and Census of State Adult Correctional Facilities, 1974"
+                }
+            ],
+            "identifier": "287",
+            "isPartOf": "2171",
+            "issued": "1984-03-18T00:00:00",
             "keyword": [
                 "correctional facilities",
                 "correctional facilities (adults)",
@@ -15142,54 +15136,54 @@
                 "substance abuse",
                 "treatment programs"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "1992-02-16T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2171",
-            "dataQuality": false,
-            "issued": "1984-03-18T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR07811.v3",
-                    "title": "Survey of Inmates of State Correctional Facilities and Census of State Adult Correctional Facilities, 1974"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Survey of Inmates of State Correctional Facilities, 1979",
-            "description": "The purpose of this survey was to obtain information on the\r\n characteristics of persons confined to prison and the circumstances\r\n and conditions of their confinement. The survey focuses on topics and\r\n issues that are of current and continuing concern to the correctional\r\n community and researchers. Information in the survey includes prison\r\n conditions such as staffing, space, and overcrowding, inmate rights and\r\n privileges, and rules and regulations concerning prison operation and\r\n inmate behavior. Additional data are provided on the presence of educational\r\n and vocational programs, drug and alcohol programs, medical treatment, and\r\nhealth care.",
-            "modified": "2005-11-04T00:00:00",
-            "accessLevel": "public",
-            "identifier": "288",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Survey of Inmates of State Correctional Facilities and Census of State Adult Correctional Facilities, 1974"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The purpose of this survey was to obtain information on the\r\n characteristics of persons confined to prison and the circumstances\r\n and conditions of their confinement. The survey focuses on topics and\r\n issues that are of current and continuing concern to the correctional\r\n community and researchers. Information in the survey includes prison\r\n conditions such as staffing, space, and overcrowding, inmate rights and\r\n privileges, and rules and regulations concerning prison operation and\r\n inmate behavior. Additional data are provided on the presence of educational\r\n and vocational programs, drug and alcohol programs, medical treatment, and\r\nhealth care.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR07856.v3",
+                    "title": "Survey of Inmates of State Correctional Facilities, 1979"
+                }
+            ],
+            "identifier": "288",
+            "isPartOf": "2171",
+            "issued": "1984-03-18T00:00:00",
             "keyword": [
                 "correctional facilities",
                 "correctional facilities (adults)",
@@ -15207,54 +15201,54 @@
                 "substance abuse",
                 "treatment programs"
             ],
-            "bureauCode": [
-                "011:21"
-            ],
-            "programCode": [
-                "011:061"
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2171",
-            "dataQuality": false,
-            "issued": "1984-03-18T00:00:00",
             "language": [
                 "eng"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR07856.v3",
-                    "title": "Survey of Inmates of State Correctional Facilities, 1979"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Survey of Inmates of State Correctional Facilities, 1986: [United States]",
-            "description": "This data collection provides information about topics and \r\n issues of concern in research and policy within the field of \r\n corrections. Chief among these are the characteristics of persons \r\n confined to state prisons, their current and past offenses, and the \r\n circumstances or conditions of their confinement. Also included is \r\n extensive information on inmates' drug and alcohol use, program \r\n participation, and the victims of the inmates' most recent offenses. \r\n This information, which is not available on a national basis from any \r\n other source, is intended to assist the criminal justice community and \r\nother researchers in analysis and evaluation of correctional issues.",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "modified": "2005-11-04T00:00:00",
-            "accessLevel": "public",
-            "identifier": "289",
+            "programCode": [
+                "011:061"
+            ],
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Survey of Inmates of State Correctional Facilities, 1979"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This data collection provides information about topics and \r\n issues of concern in research and policy within the field of \r\n corrections. Chief among these are the characteristics of persons \r\n confined to state prisons, their current and past offenses, and the \r\n circumstances or conditions of their confinement. Also included is \r\n extensive information on inmates' drug and alcohol use, program \r\n participation, and the victims of the inmates' most recent offenses. \r\n This information, which is not available on a national basis from any \r\n other source, is intended to assist the criminal justice community and \r\nother researchers in analysis and evaluation of correctional issues.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR08711.v2",
+                    "title": "Survey of Inmates of State Correctional Facilities, 1986: [United States]"
+                }
+            ],
+            "identifier": "289",
+            "isPartOf": "2171",
+            "issued": "1988-10-25T00:00:00",
             "keyword": [
                 "correctional facilities",
                 "correctional facilities (adults)",
@@ -15271,54 +15265,54 @@
                 "substance abuse",
                 "treatment programs"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2005-11-04T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2171",
-            "dataQuality": false,
-            "issued": "1988-10-25T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR08711.v2",
-                    "title": "Survey of Inmates of State Correctional Facilities, 1986: [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Survey of Inmates of State Correctional Facilities, 1991: [United States]",
-            "description": "This survey provides nationally representative data on\r\npersons held in state prisons and is similar to surveys conducted in\r\n1974 (ICPSR 7811), 1979 (ICPSR 7856), and 1986 (ICPSR 8711). The survey\r\nwas designed to provide information on individual characteristics of\r\nprison inmates, their current offenses and sentences, characteristics\r\nof victims, criminal histories, prior drug and alcohol use and\r\ntreatment, gun possession and use, gang membership, family background,\r\nand prison activities, programs, and services.",
-            "modified": "1993-10-11T00:00:00",
-            "accessLevel": "public",
-            "identifier": "290",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Survey of Inmates of State Correctional Facilities, 1986: [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This survey provides nationally representative data on\r\npersons held in state prisons and is similar to surveys conducted in\r\n1974 (ICPSR 7811), 1979 (ICPSR 7856), and 1986 (ICPSR 8711). The survey\r\nwas designed to provide information on individual characteristics of\r\nprison inmates, their current offenses and sentences, characteristics\r\nof victims, criminal histories, prior drug and alcohol use and\r\ntreatment, gun possession and use, gang membership, family background,\r\nand prison activities, programs, and services.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR06068.v1",
+                    "title": "Survey of Inmates of State Correctional Facilities, 1991: [United States]"
+                }
+            ],
+            "identifier": "290",
+            "isPartOf": "2171",
+            "issued": "1993-10-11T00:00:00",
             "keyword": [
                 "HIV",
                 "correctional facilities",
@@ -15336,54 +15330,54 @@
                 "substance abuse",
                 "treatment programs"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "1993-10-11T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2171",
-            "dataQuality": false,
-            "issued": "1993-10-11T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR06068.v1",
-                    "title": "Survey of Inmates of State Correctional Facilities, 1991: [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Survey of Jail Inmates, 1972",
-            "description": "This study is a follow-up to the National Jail Census, 1970. \r\n In addition to gathering more information concerning jails, the survey \r\n also collected demographic data, incarceration history, and legal \r\n status data from a sample of the inmates of local jails. The study \r\n includes basic demographic data, income and employment data, reason for \r\n incarceration, bail status, dates of admission and sentencing, length \r\nand type of sentence and previous incarceration history.",
-            "modified": "1992-02-16T00:00:00",
-            "accessLevel": "public",
-            "identifier": "291",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Survey of Inmates of State Correctional Facilities, 1991: [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This study is a follow-up to the National Jail Census, 1970. \r\n In addition to gathering more information concerning jails, the survey \r\n also collected demographic data, incarceration history, and legal \r\n status data from a sample of the inmates of local jails. The study \r\n includes basic demographic data, income and employment data, reason for \r\n incarceration, bail status, dates of admission and sentencing, length \r\nand type of sentence and previous incarceration history.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR07668.v2",
+                    "title": "Survey of Jail Inmates, 1972"
+                }
+            ],
+            "identifier": "291",
+            "isPartOf": "2170",
+            "issued": "1984-03-18T00:00:00",
             "keyword": [
                 "correctional facilities",
                 "criminal histories",
@@ -15396,54 +15390,54 @@
                 "offenses",
                 "sentencing"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "1992-02-16T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2170",
-            "dataQuality": false,
-            "issued": "1984-03-18T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR07668.v2",
-                    "title": "Survey of Jail Inmates, 1972"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Survey of Jail Inmates, 1978",
-            "description": "In February of 1978, locally operated jails were surveyed on\r\n a national scale. Of the more than 158,000 persons who were estimated\r\n to be held in these jails at that time, a sample of 5,247 inmates was\r\n drawn. Information was gathered regarding type of facility,\r\n availability of health care in the facility, personal and educational\r\n backgrounds, reasons for incarceration, sentencing, numbers of\r\noffenses, and inmate drug use.",
-            "modified": "2005-11-04T00:00:00",
-            "accessLevel": "public",
-            "identifier": "292",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Survey of Jail Inmates, 1972"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "In February of 1978, locally operated jails were surveyed on\r\n a national scale. Of the more than 158,000 persons who were estimated\r\n to be held in these jails at that time, a sample of 5,247 inmates was\r\n drawn. Information was gathered regarding type of facility,\r\n availability of health care in the facility, personal and educational\r\n backgrounds, reasons for incarceration, sentencing, numbers of\r\noffenses, and inmate drug use.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR07751.v5",
+                    "title": "Survey of Jail Inmates, 1978"
+                }
+            ],
+            "identifier": "292",
+            "isPartOf": "2170",
+            "issued": "1984-03-18T00:00:00",
             "keyword": [
                 "correctional facilities",
                 "criminal histories",
@@ -15456,54 +15450,53 @@
                 "offenses",
                 "sentencing"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2005-11-04T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2170",
-            "dataQuality": false,
-            "issued": "1984-03-18T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR07751.v5",
-                    "title": "Survey of Jail Inmates, 1978"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Survey of Youths in Custody, 1987:  [United States]",
-            "description": "This data collection, the first survey of youths confined to \r\n long-term, state-operated institutions, was undertaken to complement \r\n existing Children in Custody censuses. It also serves as a companion to \r\n the Surveys of State Prisons, allowing comparisons between adult and \r\n juvenile populations. The survey provides detailed information on the \r\n characteristics of youths held primarily in secure settings within the \r\n juvenile justice system. The data contain information on criminal \r\n histories, family situations, drug and alcohol use, and peer group \r\n activities. For youths committed for violent acts, data are available \r\non the victims of their crimes and on weapon use.",
-            "modified": "1995-03-31T00:00:00",
-            "accessLevel": "public",
-            "identifier": "293",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Survey of Jail Inmates, 1978"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This data collection, the first survey of youths confined to \r\n long-term, state-operated institutions, was undertaken to complement \r\n existing Children in Custody censuses. It also serves as a companion to \r\n the Surveys of State Prisons, allowing comparisons between adult and \r\n juvenile populations. The survey provides detailed information on the \r\n characteristics of youths held primarily in secure settings within the \r\n juvenile justice system. The data contain information on criminal \r\n histories, family situations, drug and alcohol use, and peer group \r\n activities. For youths committed for violent acts, data are available \r\non the victims of their crimes and on weapon use.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR08992.v3",
+                    "title": "Survey of Youths in Custody, 1987:  [United States]"
+                }
+            ],
+            "identifier": "293",
+            "issued": "1989-01-10T00:00:00",
             "keyword": [
                 "alcohol abuse",
                 "criminal histories",
@@ -15514,53 +15507,53 @@
                 "juvenile offenders",
                 "prisons"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "1995-03-31T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "1989-01-10T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR08992.v3",
-                    "title": "Survey of Youths in Custody, 1987:  [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Traffic Stop Data Collection Policies for State Police, 2004",
-            "description": "This collection contains survey data collected at the end\r\nof October 2004 from the 49 state law enforcement agencies in the\r\nUnited States that had traffic patrol responsibility. Information was\r\ngathered about their policies for recording race and ethnicity data\r\nfor persons in traffic stops, including the circumstances under which\r\ndemographic data should be collected for traffic-related stops and\r\nwhether such information should be stored in an electronically\r\naccessible format. The survey was not designed to obtain available\r\nagency databases containing traffic stop records.",
-            "modified": "2005-09-02T00:00:00",
-            "accessLevel": "public",
-            "identifier": "294",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Survey of Youths in Custody, 1987:  [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This collection contains survey data collected at the end\r\nof October 2004 from the 49 state law enforcement agencies in the\r\nUnited States that had traffic patrol responsibility. Information was\r\ngathered about their policies for recording race and ethnicity data\r\nfor persons in traffic stops, including the circumstances under which\r\ndemographic data should be collected for traffic-related stops and\r\nwhether such information should be stored in an electronically\r\naccessible format. The survey was not designed to obtain available\r\nagency databases containing traffic stop records.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR04288.v1",
+                    "title": "Traffic Stop Data Collection Policies for State Police, 2004"
+                }
+            ],
+            "identifier": "294",
+            "issued": "2005-09-02T00:00:00",
             "keyword": [
                 "ethnic identity",
                 "ethnicity",
@@ -15569,53 +15562,54 @@
                 "race",
                 "traffic offenses"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2005-09-02T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "2005-09-02T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR04288.v1",
-                    "title": "Traffic Stop Data Collection Policies for State Police, 2004"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data: County-Level Detailed Arrest and Offense Data, United States, 2011",
-            "description": "This data collection contains county-level counts of\r\narrests and offenses for Part I offenses (murder, rape, robbery,\r\naggravated assault, burglary, larceny, auto theft, and arson) and\r\ncounts of arrests for Part II offenses (forgery, fraud, embezzlement,\r\nvandalism, weapons violations, sex offenses, drug and alcohol abuse\r\nviolations, gambling, vagrancy, curfew violations, and runaways).",
-            "modified": "2014-06-13T10:56:16",
-            "accessLevel": "public",
-            "identifier": "295",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Traffic Stop Data Collection Policies for State Police, 2004"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This data collection contains county-level counts of\r\narrests and offenses for Part I offenses (murder, rape, robbery,\r\naggravated assault, burglary, larceny, auto theft, and arson) and\r\ncounts of arrests for Part II offenses (forgery, fraud, embezzlement,\r\nvandalism, weapons violations, sex offenses, drug and alcohol abuse\r\nviolations, gambling, vagrancy, curfew violations, and runaways).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR34582.v2",
+                    "title": "Uniform Crime Reporting Program Data: County-Level Detailed Arrest and Offense Data, United States, 2011"
+                }
+            ],
+            "identifier": "295",
+            "isPartOf": "2167",
+            "issued": "2013-12-18T10:35:31",
             "keyword": [
                 "Uniform Crime Reports",
                 "aggravated assault",
@@ -15644,54 +15638,54 @@
                 "vandalism",
                 "weapons offenses"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2014-06-13T10:56:16",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2013-12-18T10:35:31",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR34582.v2",
-                    "title": "Uniform Crime Reporting Program Data: County-Level Detailed Arrest and Offense Data, United States, 2011"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Capital Punishment in the United States, 1973-1987",
-            "description": "This data collection provides annual data on prisoners\r\n under a sentence of death and on prisoners whose sentences were\r\n commuted or vacated. The data furnish basic sociodemographic\r\n classifications including age, sex, race and ethnicity, marital status\r\n at time of imprisonment, level of education, and state and region of\r\n incarceration. Criminal history information includes prior felony\r\n convictions, prior convictions for criminal homicide, and legal status\r\n at the time of the capital offense. Additional information is provided\r\n on those inmates removed from death row by yearend 1986, inmates\r\n receiving a second capital punishment sentence in 1987, and inmates\r\nwho were executed.",
-            "modified": "2008-11-12T10:30:44",
-            "accessLevel": "restricted public",
-            "identifier": "749",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Uniform Crime Reporting Program Data: County-Level Detailed Arrest and Offense Data, United States, 2011"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This data collection provides annual data on prisoners\r\n under a sentence of death and on prisoners whose sentences were\r\n commuted or vacated. The data furnish basic sociodemographic\r\n classifications including age, sex, race and ethnicity, marital status\r\n at time of imprisonment, level of education, and state and region of\r\n incarceration. Criminal history information includes prior felony\r\n convictions, prior convictions for criminal homicide, and legal status\r\n at the time of the capital offense. Additional information is provided\r\n on those inmates removed from death row by yearend 1986, inmates\r\n receiving a second capital punishment sentence in 1987, and inmates\r\nwho were executed.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR09210.v1",
+                    "title": "Capital Punishment in the United States, 1973-1987"
+                }
+            ],
+            "identifier": "749",
+            "isPartOf": "2587",
+            "issued": "1989-09-26T00:00:00",
             "keyword": [
                 "capital punishment",
                 "commuted sentences",
@@ -15704,55 +15698,55 @@
                 "sentencing",
                 "states (USA)"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-11-12T10:30:44",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2587",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "1989-09-26T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR09210.v1",
-                    "title": "Capital Punishment in the United States, 1973-1987"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Capital Punishment in the United States, 1973-1988",
-            "description": "This data collection provides annual data on prisoners\r\n under a sentence of death and on those whose offense sentences were\r\n commuted or vacated. Information is available on basic\r\n sociodemographic characteristics such as age, sex, race and ethnicity,\r\n marital status at time of imprisonment, level of education, and state\r\n of incarceration. Criminal history data include prior felony\r\n convictions for criminal homicide and legal status at the time of the\r\n capital offense. Additional information is provided on those inmates\r\n removed from death row by yearend 1988 and those inmates who were\r\nexecuted.",
-            "modified": "2008-11-12T10:27:21",
-            "accessLevel": "restricted public",
-            "identifier": "750",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Capital Punishment in the United States, 1973-1987"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This data collection provides annual data on prisoners\r\n under a sentence of death and on those whose offense sentences were\r\n commuted or vacated. Information is available on basic\r\n sociodemographic characteristics such as age, sex, race and ethnicity,\r\n marital status at time of imprisonment, level of education, and state\r\n of incarceration. Criminal history data include prior felony\r\n convictions for criminal homicide and legal status at the time of the\r\n capital offense. Additional information is provided on those inmates\r\n removed from death row by yearend 1988 and those inmates who were\r\nexecuted.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR09337.v1",
+                    "title": "Capital Punishment in the United States, 1973-1988"
+                }
+            ],
+            "identifier": "750",
+            "isPartOf": "2587",
+            "issued": "1990-05-16T00:00:00",
             "keyword": [
                 "capital punishment",
                 "commuted sentences",
@@ -15765,55 +15759,55 @@
                 "sentencing",
                 "states (USA)"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-11-12T10:27:21",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2587",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "1990-05-16T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR09337.v1",
-                    "title": "Capital Punishment in the United States, 1973-1988"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Capital Punishment in the United States, 1973-1989",
-            "description": "This data collection provides annual data on prisoners under\r\na sentence of death and on those whose offense sentences were commuted\r\nor vacated during the period 1973-1989. Information is supplied on\r\nbasic sociodemographic characteristics such as age, sex, race and\r\nethnicity, marital status at time of imprisonment, level of education,\r\nand state of incarceration. Criminal history data include prior felony\r\nconvictions for criminal homicide and legal status at the time of the\r\ncapital offense. Additional information is available for those inmates\r\nremoved from death row by yearend 1989 and for those inmates who were\r\nexecuted.",
-            "modified": "2008-11-12T09:32:32",
-            "accessLevel": "restricted public",
-            "identifier": "751",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Capital Punishment in the United States, 1973-1988"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This data collection provides annual data on prisoners under\r\na sentence of death and on those whose offense sentences were commuted\r\nor vacated during the period 1973-1989. Information is supplied on\r\nbasic sociodemographic characteristics such as age, sex, race and\r\nethnicity, marital status at time of imprisonment, level of education,\r\nand state of incarceration. Criminal history data include prior felony\r\nconvictions for criminal homicide and legal status at the time of the\r\ncapital offense. Additional information is available for those inmates\r\nremoved from death row by yearend 1989 and for those inmates who were\r\nexecuted.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR09507.v2",
+                    "title": "Capital Punishment in the United States, 1973-1989"
+                }
+            ],
+            "identifier": "751",
+            "isPartOf": "2587",
+            "issued": "1991-03-05T00:00:00",
             "keyword": [
                 "capital punishment",
                 "commuted sentences",
@@ -15826,55 +15820,55 @@
                 "sentencing",
                 "states (USA)"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-11-12T09:32:32",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2587",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "1991-03-05T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR09507.v2",
-                    "title": "Capital Punishment in the United States, 1973-1989"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Capital Punishment in the United States, 1973-1990",
-            "description": "This data collection provides annual data on prisoners under \r\n a sentence of death and on those whose offense sentences were commuted \r\n or vacated during the period 1973-1990. Information is supplied for \r\n basic sociodemographic characteristics such as age, sex, race, \r\n ethnicity, marital status at time of imprisonment, level of education, \r\n and state of incarceration. Criminal history data include prior felony \r\n convictions for criminal homicide and legal status at the time of the \r\n capital offense. Additional information is available for those inmates \r\n removed from death row by yearend 1990 and for those inmates who were \r\nexecuted.",
-            "modified": "2008-11-12T10:24:55",
-            "accessLevel": "restricted public",
-            "identifier": "752",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Capital Punishment in the United States, 1973-1989"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This data collection provides annual data on prisoners under \r\n a sentence of death and on those whose offense sentences were commuted \r\n or vacated during the period 1973-1990. Information is supplied for \r\n basic sociodemographic characteristics such as age, sex, race, \r\n ethnicity, marital status at time of imprisonment, level of education, \r\n and state of incarceration. Criminal history data include prior felony \r\n convictions for criminal homicide and legal status at the time of the \r\n capital offense. Additional information is available for those inmates \r\n removed from death row by yearend 1990 and for those inmates who were \r\nexecuted.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR09819.v1",
+                    "title": "Capital Punishment in the United States, 1973-1990"
+                }
+            ],
+            "identifier": "752",
+            "isPartOf": "2587",
+            "issued": "1993-02-14T00:00:00",
             "keyword": [
                 "capital punishment",
                 "commuted sentences",
@@ -15887,116 +15881,55 @@
                 "sentencing",
                 "states (USA)"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-11-12T10:24:55",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2587",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "1993-02-14T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR09819.v1",
-                    "title": "Capital Punishment in the United States, 1973-1990"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Capital Punishment in the United States, 1973-1991",
-            "description": "This data collection provides annual data on prisoners under \r\n a sentence of death and on those whose offense sentences were commuted \r\n or vacated during the period 1973-1991. Information is supplied for \r\n basic sociodemographic characteristics such as age, sex, race, \r\n ethnicity, marital status at time of imprisonment, level of education, \r\n and state of incarceration. Criminal history data include prior felony \r\n convictions for criminal homicide and legal status at the time of the \r\n capital offense. Additional information is available for inmates \r\n removed from death row by yearend 1991 and for inmates who were \r\nexecuted.",
-            "modified": "2008-11-12T10:22:42",
-            "accessLevel": "restricted public",
-            "identifier": "753",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Capital Punishment in the United States, 1973-1990"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
-            "keyword": [
-                "capital punishment",
-                "commuted sentences",
-                "criminal histories",
-                "death row inmates",
-                "demographic characteristics",
-                "executions",
-                "felony offenses",
-                "prison inmates",
-                "sentencing",
-                "states (USA)"
-            ],
-            "bureauCode": [
-                "011:21"
-            ],
-            "programCode": [
-                "011:061"
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2587",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
             "dataQuality": false,
-            "issued": "1995-10-30T00:00:00",
-            "language": [
-                "eng"
-            ],
+            "description": "This data collection provides annual data on prisoners under \r\n a sentence of death and on those whose offense sentences were commuted \r\n or vacated during the period 1973-1991. Information is supplied for \r\n basic sociodemographic characteristics such as age, sex, race, \r\n ethnicity, marital status at time of imprisonment, level of education, \r\n and state of incarceration. Criminal history data include prior felony \r\n convictions for criminal homicide and legal status at the time of the \r\n capital offense. Additional information is available for inmates \r\n removed from death row by yearend 1991 and for inmates who were \r\nexecuted.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://doi.org/10.3886/ICPSR06514.v1",
                     "title": "Capital Punishment in the United States, 1973-1991"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Capital Punishment in the United States, 1973-1992",
-            "description": "This data collection provides annual data on prisoners under \r\n a sentence of death and on those whose offense sentences were commuted \r\n or vacated during the period 1973-1992. Information is supplied for \r\n basic sociodemographic characteristics such as age, sex, race, \r\n ethnicity, marital status at time of imprisonment, level of education, \r\n and state of incarceration. Criminal history data include prior felony \r\n convictions for criminal homicide and legal status at the time of the \r\n capital offense. Additional information is available for inmates \r\n removed from death row by yearend 1992 and for inmates who were \r\nexecuted.",
-            "modified": "2008-11-12T10:20:16",
-            "accessLevel": "restricted public",
-            "identifier": "754",
-            "publisher": {
-                "name": "Bureau of Justice Statistics",
-                "@type": "org:Organization",
-                "subOrganizationOf": {
-                    "id": 22,
-                    "acronym": "OJP",
-                    "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
-                    "parentOrganization": {
-                        "id": 10,
-                        "acronym": "DOJ",
-                        "name": "Department of Justice"
-                    }
-                }
-            },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
-                "hasEmail": "mailto:askbjs@usdoj.gov"
-            },
+            ],
+            "identifier": "753",
+            "isPartOf": "2587",
+            "issued": "1995-10-30T00:00:00",
             "keyword": [
                 "capital punishment",
                 "commuted sentences",
@@ -16009,55 +15942,55 @@
                 "sentencing",
                 "states (USA)"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-11-12T10:22:42",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2587",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "1995-10-30T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR06513.v1",
-                    "title": "Capital Punishment in the United States, 1973-1992"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Capital Punishment in the United States, 1973-1993",
-            "description": "This data collection provides annual data on prisoners under \r\n a sentence of death and on those whose offense sentences were commuted \r\n or vacated during the period 1973-1993. Information is supplied for \r\n basic sociodemographic characteristics such as age, sex, race, \r\n ethnicity, marital status at the time of imprisonment, level of \r\n education, and state of incarceration. Criminal history data include \r\n prior felony convictions for criminal homicide and legal status at the \r\n time of the capital offense. Additional information is available for \r\n inmates removed from death row by yearend 1993 and for inmates who were \r\nexecuted.",
-            "modified": "2008-11-12T10:17:31",
-            "accessLevel": "restricted public",
-            "identifier": "755",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Capital Punishment in the United States, 1973-1991"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This data collection provides annual data on prisoners under \r\n a sentence of death and on those whose offense sentences were commuted \r\n or vacated during the period 1973-1992. Information is supplied for \r\n basic sociodemographic characteristics such as age, sex, race, \r\n ethnicity, marital status at time of imprisonment, level of education, \r\n and state of incarceration. Criminal history data include prior felony \r\n convictions for criminal homicide and legal status at the time of the \r\n capital offense. Additional information is available for inmates \r\n removed from death row by yearend 1992 and for inmates who were \r\nexecuted.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR06513.v1",
+                    "title": "Capital Punishment in the United States, 1973-1992"
+                }
+            ],
+            "identifier": "754",
+            "isPartOf": "2587",
+            "issued": "1995-10-30T00:00:00",
             "keyword": [
                 "capital punishment",
                 "commuted sentences",
@@ -16070,55 +16003,55 @@
                 "sentencing",
                 "states (USA)"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-11-12T10:20:16",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2587",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "1995-10-30T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR06512.v1",
-                    "title": "Capital Punishment in the United States, 1973-1993"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Capital Punishment in the United States, 1973-1994  ",
-            "description": "This data collection provides annual data on prisoners under\r\na sentence of death and prisoners whose offense sentences were commuted\r\nor vacated during the period 1973-1994. Information is supplied for\r\nbasic sociodemographic characteristics such as age, sex, race,\r\nethnicity, marital status at the time of imprisonment, level of\r\neducation, and state of incarceration. Criminal history data include\r\nprior felony convictions for criminal homicide and legal status at the\r\ntime of the capital offense. Additional information is available for\r\ninmates removed from death row by yearend 1994 and for inmates who were\r\nexecuted.",
-            "modified": "2008-11-12T10:15:04",
-            "accessLevel": "restricted public",
-            "identifier": "756",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Capital Punishment in the United States, 1973-1992"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This data collection provides annual data on prisoners under \r\n a sentence of death and on those whose offense sentences were commuted \r\n or vacated during the period 1973-1993. Information is supplied for \r\n basic sociodemographic characteristics such as age, sex, race, \r\n ethnicity, marital status at the time of imprisonment, level of \r\n education, and state of incarceration. Criminal history data include \r\n prior felony convictions for criminal homicide and legal status at the \r\n time of the capital offense. Additional information is available for \r\n inmates removed from death row by yearend 1993 and for inmates who were \r\nexecuted.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR06512.v1",
+                    "title": "Capital Punishment in the United States, 1973-1993"
+                }
+            ],
+            "identifier": "755",
+            "isPartOf": "2587",
+            "issued": "1995-10-30T00:00:00",
             "keyword": [
                 "capital punishment",
                 "commuted sentences",
@@ -16131,55 +16064,55 @@
                 "sentencing",
                 "states (USA)"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-11-12T10:17:31",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2587",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "1997-10-13T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR06691.v1",
-                    "title": "Capital Punishment in the United States, 1973-1994  "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Capital Punishment in the United States, 1973-1995  ",
-            "description": "This data collection provides annual data on prisoners\r\nunder a sentence of death and prisoners whose offense sentences were\r\ncommuted or vacated during the period 1973-1995. Information is\r\nsupplied for basic sociodemographic characteristics such as age, sex,\r\nrace, ethnicity, marital status at the time of imprisonment, level of\r\neducation, and state of incarceration. Criminal history data include\r\nprior felony convictions for criminal homicide and legal status at the\r\ntime of the capital offense. Additional information is available for\r\ninmates removed from death row by yearend 1995 and for inmates who\r\nwere executed.",
-            "modified": "2008-11-12T10:05:26",
-            "accessLevel": "restricted public",
-            "identifier": "757",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Capital Punishment in the United States, 1973-1993"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This data collection provides annual data on prisoners under\r\na sentence of death and prisoners whose offense sentences were commuted\r\nor vacated during the period 1973-1994. Information is supplied for\r\nbasic sociodemographic characteristics such as age, sex, race,\r\nethnicity, marital status at the time of imprisonment, level of\r\neducation, and state of incarceration. Criminal history data include\r\nprior felony convictions for criminal homicide and legal status at the\r\ntime of the capital offense. Additional information is available for\r\ninmates removed from death row by yearend 1994 and for inmates who were\r\nexecuted.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR06691.v1",
+                    "title": "Capital Punishment in the United States, 1973-1994  "
+                }
+            ],
+            "identifier": "756",
+            "isPartOf": "2587",
+            "issued": "1997-10-13T00:00:00",
             "keyword": [
                 "capital punishment",
                 "commuted sentences",
@@ -16192,55 +16125,55 @@
                 "sentencing",
                 "states (USA)"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-11-12T10:15:04",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2587",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "1997-10-13T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR06956.v1",
-                    "title": "Capital Punishment in the United States, 1973-1995  "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Capital Punishment in the United States, 1973-1996  ",
-            "description": "This data collection provides annual data on prisoners\r\nunder a sentence of death and prisoners whose offense sentences were\r\ncommuted or vacated during the period 1973-1996. Information is\r\nsupplied for basic sociodemographic characteristics such as age, sex,\r\nrace, ethnicity, marital status at the time of imprisonment, level of\r\neducation, and state of incarceration. Criminal history data include\r\nprior felony convictions for criminal homicide and legal status at the\r\ntime of the capital offense. Additional information is available for\r\ninmates removed from death row by yearend 1996 and for inmates who\r\nwere executed.",
-            "modified": "2008-11-05T08:33:46",
-            "accessLevel": "restricted public",
-            "identifier": "758",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Capital Punishment in the United States, 1973-1994  "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This data collection provides annual data on prisoners\r\nunder a sentence of death and prisoners whose offense sentences were\r\ncommuted or vacated during the period 1973-1995. Information is\r\nsupplied for basic sociodemographic characteristics such as age, sex,\r\nrace, ethnicity, marital status at the time of imprisonment, level of\r\neducation, and state of incarceration. Criminal history data include\r\nprior felony convictions for criminal homicide and legal status at the\r\ntime of the capital offense. Additional information is available for\r\ninmates removed from death row by yearend 1995 and for inmates who\r\nwere executed.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR06956.v1",
+                    "title": "Capital Punishment in the United States, 1973-1995  "
+                }
+            ],
+            "identifier": "757",
+            "isPartOf": "2587",
+            "issued": "1997-10-13T00:00:00",
             "keyword": [
                 "capital punishment",
                 "commuted sentences",
@@ -16253,55 +16186,55 @@
                 "sentencing",
                 "states (USA)"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-11-12T10:05:26",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2587",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "1999-07-01T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR02736.v1",
-                    "title": "Capital Punishment in the United States, 1973-1996  "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Capital Punishment in the United States, 1973-1997",
-            "description": "This data collection provides annual data on prisoners\r\nunder a sentence of death and prisoners whose offense sentences were\r\ncommuted or vacated during the period 1973-1997. Information is\r\nsupplied for basic sociodemographic characteristics such as age, sex,\r\neducation, and state of incarceration. Criminal history data include\r\nprior felony convictions for criminal homicide and legal status at the\r\ntime of the capital offense. Additional information is available for\r\ninmates removed from death row by yearend 1997 and for inmates who\r\nwere executed.",
-            "modified": "2008-11-05T08:29:34",
-            "accessLevel": "restricted public",
-            "identifier": "759",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Capital Punishment in the United States, 1973-1995  "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This data collection provides annual data on prisoners\r\nunder a sentence of death and prisoners whose offense sentences were\r\ncommuted or vacated during the period 1973-1996. Information is\r\nsupplied for basic sociodemographic characteristics such as age, sex,\r\nrace, ethnicity, marital status at the time of imprisonment, level of\r\neducation, and state of incarceration. Criminal history data include\r\nprior felony convictions for criminal homicide and legal status at the\r\ntime of the capital offense. Additional information is available for\r\ninmates removed from death row by yearend 1996 and for inmates who\r\nwere executed.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR02736.v1",
+                    "title": "Capital Punishment in the United States, 1973-1996  "
+                }
+            ],
+            "identifier": "758",
+            "isPartOf": "2587",
+            "issued": "1999-07-01T00:00:00",
             "keyword": [
                 "capital punishment",
                 "commuted sentences",
@@ -16314,55 +16247,55 @@
                 "sentencing",
                 "states (USA)"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-11-05T08:33:46",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2587",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "1999-08-18T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR02737.v1",
-                    "title": "Capital Punishment in the United States, 1973-1997"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Capital Punishment in the United States, 1973-1998",
-            "description": "This data collection provides annual data on prisoners\r\nunder a sentence of death and prisoners whose offense sentences were\r\ncommuted or vacated during the period 1973-1998. Information is\r\nsupplied on basic sociodemographic characteristics such as age, sex,\r\neducation, and state of incarceration. Criminal history data include\r\nprior felony convictions for criminal homicide and legal status at the\r\ntime of the capital offense. Additional information is available for\r\ninmates removed from death row by yearend 1998 and for inmates who\r\nwere executed.",
-            "modified": "2008-11-05T08:25:42",
-            "accessLevel": "restricted public",
-            "identifier": "760",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Capital Punishment in the United States, 1973-1996  "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This data collection provides annual data on prisoners\r\nunder a sentence of death and prisoners whose offense sentences were\r\ncommuted or vacated during the period 1973-1997. Information is\r\nsupplied for basic sociodemographic characteristics such as age, sex,\r\neducation, and state of incarceration. Criminal history data include\r\nprior felony convictions for criminal homicide and legal status at the\r\ntime of the capital offense. Additional information is available for\r\ninmates removed from death row by yearend 1997 and for inmates who\r\nwere executed.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR02737.v1",
+                    "title": "Capital Punishment in the United States, 1973-1997"
+                }
+            ],
+            "identifier": "759",
+            "isPartOf": "2587",
+            "issued": "1999-08-18T00:00:00",
             "keyword": [
                 "capital punishment",
                 "commuted sentences",
@@ -16375,55 +16308,55 @@
                 "sentencing",
                 "states (USA)"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-11-05T08:29:34",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2587",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2000-09-11T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR02977.v1",
-                    "title": "Capital Punishment in the United States, 1973-1998"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Capital Punishment in the United States, 1973-1999",
-            "description": "This data collection provides annual data on prisoners\r\nunder a sentence of death and prisoners whose offense sentences were\r\ncommuted or vacated during the period 1973-1999. Information is\r\nsupplied for basic sociodemographic characteristics such as age, sex,\r\neducation, and state of incarceration. Criminal history data include\r\nprior felony convictions for criminal homicide and legal status at the\r\ntime of the capital offense. Additional information is available for\r\ninmates removed from death row by yearend 1999 and for inmates who\r\nwere executed.",
-            "modified": "2008-11-05T08:20:06",
-            "accessLevel": "restricted public",
-            "identifier": "761",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Capital Punishment in the United States, 1973-1997"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This data collection provides annual data on prisoners\r\nunder a sentence of death and prisoners whose offense sentences were\r\ncommuted or vacated during the period 1973-1998. Information is\r\nsupplied on basic sociodemographic characteristics such as age, sex,\r\neducation, and state of incarceration. Criminal history data include\r\nprior felony convictions for criminal homicide and legal status at the\r\ntime of the capital offense. Additional information is available for\r\ninmates removed from death row by yearend 1998 and for inmates who\r\nwere executed.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR02977.v1",
+                    "title": "Capital Punishment in the United States, 1973-1998"
+                }
+            ],
+            "identifier": "760",
+            "isPartOf": "2587",
+            "issued": "2000-09-11T00:00:00",
             "keyword": [
                 "capital punishment",
                 "commuted sentences",
@@ -16436,55 +16369,55 @@
                 "sentencing",
                 "states (USA)"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-11-05T08:25:42",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2587",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2001-07-26T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR03201.v1",
-                    "title": "Capital Punishment in the United States, 1973-1999"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Capital Punishment in the United States, 1973-2000",
-            "description": "This data collection provides annual data on prisoners\r\nunder a sentence of death and prisoners whose offense sentences were\r\ncommuted or vacated during the period 1973-2000. Information is\r\nsupplied for basic sociodemographic characteristics such as age, sex,\r\neducation, and state of incarceration. Criminal history data include\r\nprior felony convictions for criminal homicide and legal status at the\r\ntime of the capital offense. Additional information is available for\r\ninmates removed from death row by yearend 2000 and for inmates who\r\nwere executed.",
-            "modified": "2008-11-05T08:16:33",
-            "accessLevel": "restricted public",
-            "identifier": "762",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Capital Punishment in the United States, 1973-1998"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This data collection provides annual data on prisoners\r\nunder a sentence of death and prisoners whose offense sentences were\r\ncommuted or vacated during the period 1973-1999. Information is\r\nsupplied for basic sociodemographic characteristics such as age, sex,\r\neducation, and state of incarceration. Criminal history data include\r\nprior felony convictions for criminal homicide and legal status at the\r\ntime of the capital offense. Additional information is available for\r\ninmates removed from death row by yearend 1999 and for inmates who\r\nwere executed.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR03201.v1",
+                    "title": "Capital Punishment in the United States, 1973-1999"
+                }
+            ],
+            "identifier": "761",
+            "isPartOf": "2587",
+            "issued": "2001-07-26T00:00:00",
             "keyword": [
                 "capital punishment",
                 "commuted sentences",
@@ -16497,55 +16430,55 @@
                 "sentencing",
                 "states (USA)"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-11-05T08:20:06",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2587",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2003-02-28T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR03667.v1",
-                    "title": "Capital Punishment in the United States, 1973-2000"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Capital Punishment in the United States, 1973-2001",
-            "description": "This data collection provides annual data on prisoners under\r\na sentence of death and prisoners whose offense sentences were commuted\r\nor vacated during the period 1973-2001. Information is supplied for\r\nbasic sociodemographic characteristics such as age, sex, education, and\r\nstate of incarceration. Criminal history data include prior felony\r\nconvictions for criminal homicide and legal status at the time of the\r\ncapital offense. Additional information is available for inmates removed\r\nfrom death row by year-end 2001 and for inmates who were executed.",
-            "modified": "2008-11-05T08:11:39",
-            "accessLevel": "restricted public",
-            "identifier": "763",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Capital Punishment in the United States, 1973-1999"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This data collection provides annual data on prisoners\r\nunder a sentence of death and prisoners whose offense sentences were\r\ncommuted or vacated during the period 1973-2000. Information is\r\nsupplied for basic sociodemographic characteristics such as age, sex,\r\neducation, and state of incarceration. Criminal history data include\r\nprior felony convictions for criminal homicide and legal status at the\r\ntime of the capital offense. Additional information is available for\r\ninmates removed from death row by yearend 2000 and for inmates who\r\nwere executed.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR03667.v1",
+                    "title": "Capital Punishment in the United States, 1973-2000"
+                }
+            ],
+            "identifier": "762",
+            "isPartOf": "2587",
+            "issued": "2003-02-28T00:00:00",
             "keyword": [
                 "capital punishment",
                 "commuted sentences",
@@ -16558,55 +16491,55 @@
                 "sentencing",
                 "states (USA)"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-11-05T08:16:33",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2587",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2004-03-30T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR03947.v1",
-                    "title": "Capital Punishment in the United States, 1973-2001"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Capital Punishment in the United States, 1973-2002  ",
-            "description": "This data collection provides annual data on prisoners under\r\na sentence of death and prisoners whose offense sentences were commuted\r\nor vacated during the period 1973-2002. Information is supplied for\r\nbasic sociodemographic characteristics such as age, sex, education, and\r\nstate of incarceration. Criminal history data include prior felony\r\nconvictions for criminal homicide and legal status at the time of the\r\ncapital offense. Additional information is available for inmates removed\r\nfrom death row by year-end 2002 and for inmates who were executed.",
-            "modified": "2008-11-04T20:27:47",
-            "accessLevel": "restricted public",
-            "identifier": "764",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Capital Punishment in the United States, 1973-2000"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This data collection provides annual data on prisoners under\r\na sentence of death and prisoners whose offense sentences were commuted\r\nor vacated during the period 1973-2001. Information is supplied for\r\nbasic sociodemographic characteristics such as age, sex, education, and\r\nstate of incarceration. Criminal history data include prior felony\r\nconvictions for criminal homicide and legal status at the time of the\r\ncapital offense. Additional information is available for inmates removed\r\nfrom death row by year-end 2001 and for inmates who were executed.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR03947.v1",
+                    "title": "Capital Punishment in the United States, 1973-2001"
+                }
+            ],
+            "identifier": "763",
+            "isPartOf": "2587",
+            "issued": "2004-03-30T00:00:00",
             "keyword": [
                 "capital punishment",
                 "commuted sentences",
@@ -16619,55 +16552,55 @@
                 "sentencing",
                 "states (USA)"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-11-05T08:11:39",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2587",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2004-04-15T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR03958.v1",
-                    "title": "Capital Punishment in the United States, 1973-2002  "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Capital Punishment in the United States, 1973-2003",
-            "description": "This data collection provides annual data on prisoners\r\n under a sentence of death and prisoners whose offense sentences were\r\n commuted or vacated during the period 1973-2003. Information is\r\n supplied for basic sociodemographic characteristics such as age, sex,\r\n education, and state of incarceration. Criminal history data include\r\n prior felony convictions for criminal homicide and legal status at the\r\n time of the capital offense. Additional information is available for\r\n inmates removed from death row by year-end 2003 and for inmates who\r\nwere executed.",
-            "modified": "2008-11-04T20:11:35",
-            "accessLevel": "restricted public",
-            "identifier": "765",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Capital Punishment in the United States, 1973-2001"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This data collection provides annual data on prisoners under\r\na sentence of death and prisoners whose offense sentences were commuted\r\nor vacated during the period 1973-2002. Information is supplied for\r\nbasic sociodemographic characteristics such as age, sex, education, and\r\nstate of incarceration. Criminal history data include prior felony\r\nconvictions for criminal homicide and legal status at the time of the\r\ncapital offense. Additional information is available for inmates removed\r\nfrom death row by year-end 2002 and for inmates who were executed.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR03958.v1",
+                    "title": "Capital Punishment in the United States, 1973-2002  "
+                }
+            ],
+            "identifier": "764",
+            "isPartOf": "2587",
+            "issued": "2004-04-15T00:00:00",
             "keyword": [
                 "capital punishment",
                 "commuted sentences",
@@ -16680,55 +16613,55 @@
                 "sentencing",
                 "states (USA)"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-11-04T20:27:47",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2587",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2006-03-17T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR04404.v1",
-                    "title": "Capital Punishment in the United States, 1973-2003"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Capital Punishment in the United States, 1973-2004",
-            "description": "This data collection provides annual data on prisoners\r\n under a sentence of death and prisoners whose offense sentences were\r\n commuted or vacated during the period 1973-2004. Information is\r\n supplied for basic sociodemographic characteristics such as age, sex,\r\n education, and state of incarceration. Criminal history data include\r\n prior felony convictions for criminal homicide and legal status at the\r\n time of the capital offense. Additional information is available for\r\n inmates removed from death row by year-end 2004 and for inmates who\r\nwere executed.",
-            "modified": "2008-10-24T11:19:53",
-            "accessLevel": "restricted public",
-            "identifier": "766",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Capital Punishment in the United States, 1973-2002  "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This data collection provides annual data on prisoners\r\n under a sentence of death and prisoners whose offense sentences were\r\n commuted or vacated during the period 1973-2003. Information is\r\n supplied for basic sociodemographic characteristics such as age, sex,\r\n education, and state of incarceration. Criminal history data include\r\n prior felony convictions for criminal homicide and legal status at the\r\n time of the capital offense. Additional information is available for\r\n inmates removed from death row by year-end 2003 and for inmates who\r\nwere executed.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR04404.v1",
+                    "title": "Capital Punishment in the United States, 1973-2003"
+                }
+            ],
+            "identifier": "765",
+            "isPartOf": "2587",
+            "issued": "2006-03-17T00:00:00",
             "keyword": [
                 "capital punishment",
                 "commuted sentences",
@@ -16741,55 +16674,55 @@
                 "sentencing",
                 "states (USA)"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-11-04T20:11:35",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2587",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2006-04-05T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR04430.v1",
-                    "title": "Capital Punishment in the United States, 1973-2004"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Capital Punishment in the United States, 1973-2005",
-            "description": "This data collection provides annual data on prisoners\r\nunder a sentence of death and prisoners whose offense sentences were\r\ncommuted or vacated during the period 1973-2005. Information is\r\nsupplied for basic sociodemographic characteristics such as age, sex,\r\neducation, and state of incarceration. Criminal history data include\r\nprior felony convictions for criminal homicide and legal status at the\r\ntime of the capital offense. Additional information is available for\r\ninmates removed from death row by year-end 2005 and for inmates who\r\nwere executed.",
-            "modified": "2008-10-21T14:23:47",
-            "accessLevel": "restricted public",
-            "identifier": "767",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Capital Punishment in the United States, 1973-2003"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This data collection provides annual data on prisoners\r\n under a sentence of death and prisoners whose offense sentences were\r\n commuted or vacated during the period 1973-2004. Information is\r\n supplied for basic sociodemographic characteristics such as age, sex,\r\n education, and state of incarceration. Criminal history data include\r\n prior felony convictions for criminal homicide and legal status at the\r\n time of the capital offense. Additional information is available for\r\n inmates removed from death row by year-end 2004 and for inmates who\r\nwere executed.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR04430.v1",
+                    "title": "Capital Punishment in the United States, 1973-2004"
+                }
+            ],
+            "identifier": "766",
+            "isPartOf": "2587",
+            "issued": "2006-04-05T00:00:00",
             "keyword": [
                 "capital punishment",
                 "commuted sentences",
@@ -16802,55 +16735,55 @@
                 "sentencing",
                 "states (USA)"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-10-24T11:19:53",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2587",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2007-08-15T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR20580.v1",
-                    "title": "Capital Punishment in the United States, 1973-2005"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Capital Punishment in the United States, 1973-2006",
-            "description": "This data collection provides annual data on prisoners under a sentence of death and prisoners whose offense sentences were commuted or vacated during the period 1973-2005. Information is supplied for basic sociodemographic characteristics such as age, sex, education, and state of incarceration. Criminal history data include prior felony convictions for criminal homicide and legal status at the time of the capital offense. Additional information is available for inmates removed from death row by year-end 2006 and for inmates who were executed.",
-            "modified": "2008-10-06T11:49:03",
-            "accessLevel": "restricted public",
-            "identifier": "768",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Capital Punishment in the United States, 1973-2004"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This data collection provides annual data on prisoners\r\nunder a sentence of death and prisoners whose offense sentences were\r\ncommuted or vacated during the period 1973-2005. Information is\r\nsupplied for basic sociodemographic characteristics such as age, sex,\r\neducation, and state of incarceration. Criminal history data include\r\nprior felony convictions for criminal homicide and legal status at the\r\ntime of the capital offense. Additional information is available for\r\ninmates removed from death row by year-end 2005 and for inmates who\r\nwere executed.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR20580.v1",
+                    "title": "Capital Punishment in the United States, 1973-2005"
+                }
+            ],
+            "identifier": "767",
+            "isPartOf": "2587",
+            "issued": "2007-08-15T00:00:00",
             "keyword": [
                 "capital punishment",
                 "commuted sentences",
@@ -16863,55 +16796,55 @@
                 "sentencing",
                 "states (USA)"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-10-21T14:23:47",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2587",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2008-09-25T07:56:04",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR23360.v1",
-                    "title": "Capital Punishment in the United States, 1973-2006"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Capital Punishment in the United States, 1973-2007",
-            "description": "This data collection provides annual data on prisoners\r\nunder a sentence of death and prisoners whose offense sentences were\r\ncommuted or vacated during the period 1973-2007. Information is\r\nsupplied for basic sociodemographic characteristics such as age, sex,\r\neducation, and state of incarceration. Criminal history data include\r\nprior felony convictions for criminal homicide and legal status at the\r\ntime of the capital offense. Additional information is available for\r\ninmates removed from death row by year-end 2007 and for inmates who\r\nwere executed.",
-            "modified": "2009-03-11T10:01:44",
-            "accessLevel": "restricted public",
-            "identifier": "769",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Capital Punishment in the United States, 1973-2005"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This data collection provides annual data on prisoners under a sentence of death and prisoners whose offense sentences were commuted or vacated during the period 1973-2005. Information is supplied for basic sociodemographic characteristics such as age, sex, education, and state of incarceration. Criminal history data include prior felony convictions for criminal homicide and legal status at the time of the capital offense. Additional information is available for inmates removed from death row by year-end 2006 and for inmates who were executed.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR23360.v1",
+                    "title": "Capital Punishment in the United States, 1973-2006"
+                }
+            ],
+            "identifier": "768",
+            "isPartOf": "2587",
+            "issued": "2008-09-25T07:56:04",
             "keyword": [
                 "capital punishment",
                 "commuted sentences",
@@ -16924,55 +16857,55 @@
                 "sentencing",
                 "states (USA)"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-10-06T11:49:03",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2587",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-03-11T09:58:58",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24961.v1",
-                    "title": "Capital Punishment in the United States, 1973-2007"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Capital Punishment in the United States, 1973-2008",
-            "description": "This data collection provides annual data on prisoners\r\nunder a sentence of death and prisoners whose offense sentences were\r\ncommuted or vacated during the period 1973-2008. Information is\r\nsupplied for basic sociodemographic characteristics such as age, sex,\r\neducation, and state of incarceration. Criminal history data include\r\nprior felony convictions for criminal homicide and legal status at the\r\ntime of the capital offense. Additional information is available for\r\ninmates removed from death row by year-end 2008 and for inmates who\r\nwere executed.",
-            "modified": "2010-09-07T10:12:27",
-            "accessLevel": "restricted public",
-            "identifier": "770",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Capital Punishment in the United States, 1973-2006"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This data collection provides annual data on prisoners\r\nunder a sentence of death and prisoners whose offense sentences were\r\ncommuted or vacated during the period 1973-2007. Information is\r\nsupplied for basic sociodemographic characteristics such as age, sex,\r\neducation, and state of incarceration. Criminal history data include\r\nprior felony convictions for criminal homicide and legal status at the\r\ntime of the capital offense. Additional information is available for\r\ninmates removed from death row by year-end 2007 and for inmates who\r\nwere executed.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24961.v1",
+                    "title": "Capital Punishment in the United States, 1973-2007"
+                }
+            ],
+            "identifier": "769",
+            "isPartOf": "2587",
+            "issued": "2009-03-11T09:58:58",
             "keyword": [
                 "capital punishment",
                 "commuted sentences",
@@ -16985,55 +16918,55 @@
                 "sentencing",
                 "states (USA)"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2009-03-11T10:01:44",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2587",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2010-09-07T10:09:30",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR27982.v1",
-                    "title": "Capital Punishment in the United States, 1973-2008"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Capital Punishment in the United States, 1973-2009",
-            "description": "This data collection provides annual data on prisoners\r\nunder a sentence of death and prisoners whose offense sentences were\r\ncommuted or vacated during the period 1973-2009. Information is\r\nsupplied for basic sociodemographic characteristics such as age, sex,\r\neducation, and state of incarceration. Criminal history data include\r\nprior felony convictions for criminal homicide and legal status at the\r\ntime of the capital offense. Additional information is available for\r\ninmates removed from death row by year-end 2009 and for inmates who\r\nwere executed.",
-            "modified": "2011-12-08T12:00:54",
-            "accessLevel": "restricted public",
-            "identifier": "771",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Capital Punishment in the United States, 1973-2007"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This data collection provides annual data on prisoners\r\nunder a sentence of death and prisoners whose offense sentences were\r\ncommuted or vacated during the period 1973-2008. Information is\r\nsupplied for basic sociodemographic characteristics such as age, sex,\r\neducation, and state of incarceration. Criminal history data include\r\nprior felony convictions for criminal homicide and legal status at the\r\ntime of the capital offense. Additional information is available for\r\ninmates removed from death row by year-end 2008 and for inmates who\r\nwere executed.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR27982.v1",
+                    "title": "Capital Punishment in the United States, 1973-2008"
+                }
+            ],
+            "identifier": "770",
+            "isPartOf": "2587",
+            "issued": "2010-09-07T10:09:30",
             "keyword": [
                 "capital punishment",
                 "commuted sentences",
@@ -17046,55 +16979,116 @@
                 "sentencing",
                 "states (USA)"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2010-09-07T10:12:27",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2587",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
+                "subOrganizationOf": {
+                    "acronym": "OJP",
+                    "id": 22,
+                    "name": "Office of Justice Programs",
+                    "parentOrganization": {
+                        "acronym": "DOJ",
+                        "id": 10,
+                        "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
+                }
+            },
             "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2011-08-16T12:17:58",
-            "language": [
-                "eng"
+            "title": "Capital Punishment in the United States, 1973-2008"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
+                "hasEmail": "mailto:askbjs@usdoj.gov"
+            },
+            "dataQuality": false,
+            "description": "This data collection provides annual data on prisoners\r\nunder a sentence of death and prisoners whose offense sentences were\r\ncommuted or vacated during the period 1973-2009. Information is\r\nsupplied for basic sociodemographic characteristics such as age, sex,\r\neducation, and state of incarceration. Criminal history data include\r\nprior felony convictions for criminal homicide and legal status at the\r\ntime of the capital offense. Additional information is available for\r\ninmates removed from death row by year-end 2009 and for inmates who\r\nwere executed.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://doi.org/10.3886/ICPSR31443.v2",
                     "title": "Capital Punishment in the United States, 1973-2009"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Capital Punishment in the United States, 1973-2010",
-            "description": "CAPITAL PUNISHMENT IN THE UNITED STATES, 1973-2010 provides annual data on prisoners under a sentence of death, as well as those who had their sentences commuted or vacated and prisoners who were executed. This study examines basic sociodemographic classifications including age, sex, race and ethnicity, marital status at time of imprisonment, level of education, and State and region of incarceration. Criminal history information includes prior felony convictions and prior convictions for criminal homicide and the legal status at the time of the capital offense. Additional information is provided on those inmates removed from death row by yearend 2010.\r\nThe dataset consists of one part which contains 9,058 cases. The file provides information on inmates whose death sentences were removed in addition to information on those inmates who were executed. The file also gives information about inmates who received a second death sentence by yearend 2010 as well as inmates who were already on death row.",
-            "modified": "2020-11-17T11:44:04",
-            "accessLevel": "restricted public",
-            "identifier": "772",
+            ],
+            "identifier": "771",
+            "isPartOf": "2587",
+            "issued": "2011-08-16T12:17:58",
+            "keyword": [
+                "capital punishment",
+                "commuted sentences",
+                "criminal histories",
+                "death row inmates",
+                "demographic characteristics",
+                "executions",
+                "felony offenses",
+                "prison inmates",
+                "sentencing",
+                "states (USA)"
+            ],
+            "language": [
+                "eng"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-12-08T12:00:54",
+            "programCode": [
+                "011:061"
+            ],
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Capital Punishment in the United States, 1973-2009"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "CAPITAL PUNISHMENT IN THE UNITED STATES, 1973-2010 provides annual data on prisoners under a sentence of death, as well as those who had their sentences commuted or vacated and prisoners who were executed. This study examines basic sociodemographic classifications including age, sex, race and ethnicity, marital status at time of imprisonment, level of education, and State and region of incarceration. Criminal history information includes prior felony convictions and prior convictions for criminal homicide and the legal status at the time of the capital offense. Additional information is provided on those inmates removed from death row by yearend 2010.\r\nThe dataset consists of one part which contains 9,058 cases. The file provides information on inmates whose death sentences were removed in addition to information on those inmates who were executed. The file also gives information about inmates who received a second death sentence by yearend 2010 as well as inmates who were already on death row.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR34366.v2",
+                    "title": "Capital Punishment in the United States, 1973-2010"
+                }
+            ],
+            "identifier": "772",
+            "isPartOf": "2587",
+            "issued": "2012-11-28T11:15:41",
             "keyword": [
                 "capital punishment",
                 "commuted sentences",
@@ -17107,55 +17101,55 @@
                 "sentencing",
                 "states (USA)"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2020-11-17T11:44:04",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2587",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2012-11-28T11:15:41",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR34366.v2",
-                    "title": "Capital Punishment in the United States, 1973-2010"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Census of Medical Examiners' and Coroners' Offices, 2004",
-            "description": "The Census of Medical Examiners' and Coroners' Offices\r\n(MECO) is a compilation of data on the practices of these offices,\r\nwhich are responsible for medical-legal death investigations. The data\r\ncover information such as the prevalence of unidentified human remains\r\non record in medical examiners' and coroners' offices across the\r\ncountry, record-keeping practices, and final disposition practices\r\nsuch as burial, cremation, or other means. In addition, data were\r\ngathered on FTE employees, contractors, and annual budgets.",
-            "modified": "2011-04-19T16:38:49",
-            "accessLevel": "restricted public",
-            "identifier": "773",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Capital Punishment in the United States, 1973-2010"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The Census of Medical Examiners' and Coroners' Offices\r\n(MECO) is a compilation of data on the practices of these offices,\r\nwhich are responsible for medical-legal death investigations. The data\r\ncover information such as the prevalence of unidentified human remains\r\non record in medical examiners' and coroners' offices across the\r\ncountry, record-keeping practices, and final disposition practices\r\nsuch as burial, cremation, or other means. In addition, data were\r\ngathered on FTE employees, contractors, and annual budgets.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR20342.v3",
+                    "title": "Census of Medical Examiners' and Coroners' Offices, 2004"
+                }
+            ],
+            "identifier": "773",
+            "isPartOf": "2440",
+            "issued": "2007-07-26T00:00:00",
             "keyword": [
                 "autopsy",
                 "coroners",
@@ -17163,55 +17157,55 @@
                 "forensic medicine",
                 "victim identification"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-04-19T16:38:49",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2440",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2007-07-26T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR20342.v3",
-                    "title": "Census of Medical Examiners' and Coroners' Offices, 2004"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Civil Justice Survey of State Courts, 1992",
-            "description": "This survey is the first broad-based, systematic\r\nexamination of the nature of civil litigation in state general\r\njurisdiction trial courts. Data collection was carried out by the\r\nNational Center for State Courts with assistance from the National\r\nAssociation of Criminal Justice Planners and the United States Bureau\r\nof the Census. The data collection produced two datasets. Part 1,\r\nTort, Contract, and Real Property Rights Data, is a merged sample of\r\napproximately 30,000 tort, contract, and real property rights cases\r\ndisposed during the 12-month period ending June 30, 1992. Part 2,\r\nCivil Jury Cases Data, is a sample of about 6,500 jury trial cases\r\ndisposed over the same time period. Data collected include information\r\nabout litigants, case type, disposition type, processing time, case\r\noutcome, and award amounts for civil jury cases.",
-            "modified": "2011-11-02T16:16:27",
-            "accessLevel": "restricted public",
-            "identifier": "774",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Census of Medical Examiners' and Coroners' Offices, 2004"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This survey is the first broad-based, systematic\r\nexamination of the nature of civil litigation in state general\r\njurisdiction trial courts. Data collection was carried out by the\r\nNational Center for State Courts with assistance from the National\r\nAssociation of Criminal Justice Planners and the United States Bureau\r\nof the Census. The data collection produced two datasets. Part 1,\r\nTort, Contract, and Real Property Rights Data, is a merged sample of\r\napproximately 30,000 tort, contract, and real property rights cases\r\ndisposed during the 12-month period ending June 30, 1992. Part 2,\r\nCivil Jury Cases Data, is a sample of about 6,500 jury trial cases\r\ndisposed over the same time period. Data collected include information\r\nabout litigants, case type, disposition type, processing time, case\r\noutcome, and award amounts for civil jury cases.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR06587.v5",
+                    "title": "Civil Justice Survey of State Courts, 1992"
+                }
+            ],
+            "identifier": "774",
+            "isPartOf": "2172",
+            "issued": "1996-10-01T00:00:00",
             "keyword": [
                 "case processing",
                 "civil courts",
@@ -17222,55 +17216,55 @@
                 "lawsuits",
                 "state courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-11-02T16:16:27",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2172",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "1996-10-01T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR06587.v5",
-                    "title": "Civil Justice Survey of State Courts, 1992"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Civil Justice Survey of State Courts, 1996",
-            "description": "In 1996, the Bureau of Justice Statistics awarded a grant\r\nto the National Center for State Courts to gather detailed information\r\non tort, contract, and real property rights trial cases in 45\r\njurisdictions chosen to represent the 75 most populous counties in the\r\nnation. The result is this survey, which is a systematic examination\r\nof civil trial cases disposed in state general jurisdiction\r\ncourts. The study expands the 1992 civil jury study, CIVIL JUSTICE\r\nSURVEY OF STATE COURTS, 1992 (ICPSR 6587), by\r\nspecifically sampling bench and jury trial cases. Information gathered\r\nincludes the type of case, the presence of legal representation, the\r\ntype of litigation, the amount of compensatory damages awarded, the\r\namount of punitive damages awarded, and case processing time.",
-            "modified": "2011-11-02T16:12:20",
-            "accessLevel": "restricted public",
-            "identifier": "775",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Civil Justice Survey of State Courts, 1992"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "In 1996, the Bureau of Justice Statistics awarded a grant\r\nto the National Center for State Courts to gather detailed information\r\non tort, contract, and real property rights trial cases in 45\r\njurisdictions chosen to represent the 75 most populous counties in the\r\nnation. The result is this survey, which is a systematic examination\r\nof civil trial cases disposed in state general jurisdiction\r\ncourts. The study expands the 1992 civil jury study, CIVIL JUSTICE\r\nSURVEY OF STATE COURTS, 1992 (ICPSR 6587), by\r\nspecifically sampling bench and jury trial cases. Information gathered\r\nincludes the type of case, the presence of legal representation, the\r\ntype of litigation, the amount of compensatory damages awarded, the\r\namount of punitive damages awarded, and case processing time.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR02883.v4",
+                    "title": "Civil Justice Survey of State Courts, 1996"
+                }
+            ],
+            "identifier": "775",
+            "isPartOf": "2172",
+            "issued": "2000-09-18T00:00:00",
             "keyword": [
                 "case processing",
                 "civil courts",
@@ -17281,55 +17275,55 @@
                 "lawsuits",
                 "state courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-11-02T16:12:20",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2172",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2000-09-18T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR02883.v4",
-                    "title": "Civil Justice Survey of State Courts, 1996"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Civil Justice Survey of State Courts, 2001",
-            "description": "This data collection examined general civil cases (torts,\r\ncontracts, and real property) disposed of by bench or jury trial in\r\nthe nation's 75 most populous counties in 2001. Information reported\r\nincludes the type of case, types of plaintiffs and defendants, trial\r\nwinners, amount of total damages awarded, amount of punitive damages\r\nawarded, and case processing time. This is the third in a series of\r\ndata collections begun in 1992:  CIVIL JUSTICE SURVEY OF STATE COURTS,\r\n1992 (ICPSR 6587), and CIVIL JUSTICE SURVEY OF STATE\r\nCOURTS, 1996 (ICPSR 2883).",
-            "modified": "2011-11-03T09:25:59",
-            "accessLevel": "restricted public",
-            "identifier": "776",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Civil Justice Survey of State Courts, 1996"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This data collection examined general civil cases (torts,\r\ncontracts, and real property) disposed of by bench or jury trial in\r\nthe nation's 75 most populous counties in 2001. Information reported\r\nincludes the type of case, types of plaintiffs and defendants, trial\r\nwinners, amount of total damages awarded, amount of punitive damages\r\nawarded, and case processing time. This is the third in a series of\r\ndata collections begun in 1992:  CIVIL JUSTICE SURVEY OF STATE COURTS,\r\n1992 (ICPSR 6587), and CIVIL JUSTICE SURVEY OF STATE\r\nCOURTS, 1996 (ICPSR 2883).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR03957.v3",
+                    "title": "Civil Justice Survey of State Courts, 2001"
+                }
+            ],
+            "identifier": "776",
+            "isPartOf": "2172",
+            "issued": "2004-05-28T00:00:00",
             "keyword": [
                 "case processing",
                 "civil courts",
@@ -17340,55 +17334,55 @@
                 "lawsuits",
                 "state courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-11-03T09:25:59",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2172",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2004-05-28T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR03957.v3",
-                    "title": "Civil Justice Survey of State Courts, 2001"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Civil Justice Survey of State Courts, 2005 ",
-            "description": "The Civil Justice Survey of State Courts (CJSSC), 2005 is a systematic examination of general civil (that is, tort, contract, and real property) cases disposed of by bench or jury trial in a national sample of state courts of general jurisdiction in 2005. This study expands on the 1992, 1996, and 2001 CJSSC by collecting a nationally representative sample of bench and jury trials concluded in 156 urban, suburban, and rural counties. Prior iterations of the CJSSC focused on general civil cases concluded by bench or jury trial in a sample of the nation's 75 most populous counties. The 2005 CJSSC was designed and carried out by the National Center for State Courts. Westat designed the national sampling framework for this survey.\r\nThe data collection produced two datasets. The first contains information on general civil (tort, contract, and real property) cases disposed of by bench or jury trial in a national sample of counties in 2005. Detailed case level information was obtained on these trials, including types of civil cases litigated at trial, characteristics of litigants involved in trials, who wins in trials, compensatory award amounts, punitive damages, case processing times, and post-trial litigation. The other data file contains aggregate information on the number of general civil trial and nontrial dispositions that occurred in 2005 in CJSCC counties that had the capacity to provide these data.\r\nThis is the fourth in a series of data collections begun in 1992 [CIVIL JUSTICE SURVEY OF STATE COURTS, 1992 (ICPSR 6587), CIVIL JUSTICE SURVEY OF STATE COURTS, 1996 (ICPSR 2883), and CIVIL JUSTICE SURVEY OF STATE COURTS, 2001 (ICPSR 3957)].",
-            "modified": "2011-11-02T16:04:45",
-            "accessLevel": "restricted public",
-            "identifier": "777",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Civil Justice Survey of State Courts, 2001"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The Civil Justice Survey of State Courts (CJSSC), 2005 is a systematic examination of general civil (that is, tort, contract, and real property) cases disposed of by bench or jury trial in a national sample of state courts of general jurisdiction in 2005. This study expands on the 1992, 1996, and 2001 CJSSC by collecting a nationally representative sample of bench and jury trials concluded in 156 urban, suburban, and rural counties. Prior iterations of the CJSSC focused on general civil cases concluded by bench or jury trial in a sample of the nation's 75 most populous counties. The 2005 CJSSC was designed and carried out by the National Center for State Courts. Westat designed the national sampling framework for this survey.\r\nThe data collection produced two datasets. The first contains information on general civil (tort, contract, and real property) cases disposed of by bench or jury trial in a national sample of counties in 2005. Detailed case level information was obtained on these trials, including types of civil cases litigated at trial, characteristics of litigants involved in trials, who wins in trials, compensatory award amounts, punitive damages, case processing times, and post-trial litigation. The other data file contains aggregate information on the number of general civil trial and nontrial dispositions that occurred in 2005 in CJSCC counties that had the capacity to provide these data.\r\nThis is the fourth in a series of data collections begun in 1992 [CIVIL JUSTICE SURVEY OF STATE COURTS, 1992 (ICPSR 6587), CIVIL JUSTICE SURVEY OF STATE COURTS, 1996 (ICPSR 2883), and CIVIL JUSTICE SURVEY OF STATE COURTS, 2001 (ICPSR 3957)].",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR23862.v2",
+                    "title": "Civil Justice Survey of State Courts, 2005 "
+                }
+            ],
+            "identifier": "777",
+            "isPartOf": "2172",
+            "issued": "2009-01-14T14:45:17",
             "keyword": [
                 "case processing",
                 "civil courts",
@@ -17399,55 +17393,55 @@
                 "lawsuits",
                 "state courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-11-02T16:04:45",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2172",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-01-14T14:45:17",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR23862.v2",
-                    "title": "Civil Justice Survey of State Courts, 2005 "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Civil Justice Survey of Trials on Appeal, 2005",
-            "description": "The Bureau of Justice Statistics' (BJS) Civil Justice Survey\r\nof Trials on Appeal (CJSTA) was based on 26,950 general\r\ncivil (i.e., tort, contract, and real property) cases that were\r\ndisposed by bench or jury trial in 156 counties participating\r\nin the 2005 Civil Justice Survey of State Courts (ICPSR 23862).\r\nSubsequently, 3,970 of those cases were appealed to 84\r\nappellate courts in 35 states.\r\nThis data collection examines civil bench and jury trials\r\nconcluded in state trial courts in 2005 that were appealed\r\nto an intermediate appellate court or court of last resort.\r\nIt is the first report based on data collected in the Bureau\r\nof Justice Statistics' (BJS) Civil Justice Survey of Trials on\r\nAppeal (CJSTA). The CJSTA included information from\r\ncourt records on civil trials concluded in 2005 and tracked\r\nthe subsequent appeals from 2005 through March 2010.\r\nInformation collected included the types of civil cases\r\nappealed, appeals dismissed or withdrawn before being\r\ndecided on the merits, and appeals resulting in the trial\r\ncourt decision being reversed or affirmed. The time from the\r\nfiling of an appeal to final appellate court disposition was\r\nalso measured.",
-            "modified": "2012-01-10T15:50:17",
-            "accessLevel": "restricted public",
-            "identifier": "778",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Civil Justice Survey of State Courts, 2005 "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The Bureau of Justice Statistics' (BJS) Civil Justice Survey\r\nof Trials on Appeal (CJSTA) was based on 26,950 general\r\ncivil (i.e., tort, contract, and real property) cases that were\r\ndisposed by bench or jury trial in 156 counties participating\r\nin the 2005 Civil Justice Survey of State Courts (ICPSR 23862).\r\nSubsequently, 3,970 of those cases were appealed to 84\r\nappellate courts in 35 states.\r\nThis data collection examines civil bench and jury trials\r\nconcluded in state trial courts in 2005 that were appealed\r\nto an intermediate appellate court or court of last resort.\r\nIt is the first report based on data collected in the Bureau\r\nof Justice Statistics' (BJS) Civil Justice Survey of Trials on\r\nAppeal (CJSTA). The CJSTA included information from\r\ncourt records on civil trials concluded in 2005 and tracked\r\nthe subsequent appeals from 2005 through March 2010.\r\nInformation collected included the types of civil cases\r\nappealed, appeals dismissed or withdrawn before being\r\ndecided on the merits, and appeals resulting in the trial\r\ncourt decision being reversed or affirmed. The time from the\r\nfiling of an appeal to final appellate court disposition was\r\nalso measured.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR32501.v1",
+                    "title": "Civil Justice Survey of Trials on Appeal, 2005"
+                }
+            ],
+            "identifier": "778",
+            "isPartOf": "2172",
+            "issued": "2012-01-10T08:58:48",
             "keyword": [
                 "case processing",
                 "civil courts",
@@ -17458,55 +17452,55 @@
                 "lawsuits",
                 "state courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2012-01-10T15:50:17",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2172",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2012-01-10T08:58:48",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR32501.v1",
-                    "title": "Civil Justice Survey of Trials on Appeal, 2005"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Deaths in Custody Reporting Program: State Prisons 2001 - 2009",
-            "description": "The Deaths in Custody Reporting Program (DCRP) is an annual data collection\r\nconducted by the Bureau of Justice Statistics (BJS). The DCRP began in 2000\r\nunder the Death in Custody Reporting Act of 2000 (P.L. 106-297). It is the\r\nonly national statistical collection that obtains detailed information\r\nabout deaths in adult correctional facilities. The DCRP collects data on\r\npersons dying in state prisons, local jails and in the process of\r\narrest. Each collection is a separate subcollection, but each is under the\r\numbrella of the DCRP collection. This deals with the prison subcollection,\r\nwhich has a prison death file.\r\nThe prison portion of the Deaths in Custody Reporting Program began in 2001\r\nafter the passage of the Deaths in Custody Reporting Act of 2000 in October\r\nof 2000. The prison component of the DCRP collects data on inmate deaths\r\noccurring in the 50 state departments of corrections while inmates are in\r\nthe physical custody of prison officials.",
-            "modified": "2013-07-31T15:33:46",
-            "accessLevel": "restricted public",
-            "identifier": "779",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Civil Justice Survey of Trials on Appeal, 2005"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The Deaths in Custody Reporting Program (DCRP) is an annual data collection\r\nconducted by the Bureau of Justice Statistics (BJS). The DCRP began in 2000\r\nunder the Death in Custody Reporting Act of 2000 (P.L. 106-297). It is the\r\nonly national statistical collection that obtains detailed information\r\nabout deaths in adult correctional facilities. The DCRP collects data on\r\npersons dying in state prisons, local jails and in the process of\r\narrest. Each collection is a separate subcollection, but each is under the\r\numbrella of the DCRP collection. This deals with the prison subcollection,\r\nwhich has a prison death file.\r\nThe prison portion of the Deaths in Custody Reporting Program began in 2001\r\nafter the passage of the Deaths in Custody Reporting Act of 2000 in October\r\nof 2000. The prison component of the DCRP collects data on inmate deaths\r\noccurring in the 50 state departments of corrections while inmates are in\r\nthe physical custody of prison officials.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR34277.v1",
+                    "title": "Deaths in Custody Reporting Program: State Prisons 2001 - 2009"
+                }
+            ],
+            "identifier": "779",
+            "isPartOf": "2441",
+            "issued": "2013-07-31T14:54:37",
             "keyword": [
                 "correctional facilities",
                 "corrections",
@@ -17514,55 +17508,55 @@
                 "homicide",
                 "suicide"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-07-31T15:33:46",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2441",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2013-07-31T14:54:37",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR34277.v1",
-                    "title": "Deaths in Custody Reporting Program: State Prisons 2001 - 2009"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 1994 [United States]",
-            "description": "The data contain records of arrests and bookings for federal offenses in the United States during fiscal year 1994. The data were constructed from the United States Marshals Service (USMS) Prisoner Tracking System database. Records include arrests made by federal law enforcement agencies (including the USMS), state and local agencies, and self-surrenders. Offenders arrested for federal offenses are transferred to the custody of the USMS for processing, transportation, and detention. The Prisoner Tracking System contains data on all offenders within the custody of the USMS. The data file contains variables from the original USMS files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.1-1.3. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2015-06-16T13:03:00",
-            "accessLevel": "restricted public",
-            "identifier": "780",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Deaths in Custody Reporting Program: State Prisons 2001 - 2009"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of arrests and bookings for federal offenses in the United States during fiscal year 1994. The data were constructed from the United States Marshals Service (USMS) Prisoner Tracking System database. Records include arrests made by federal law enforcement agencies (including the USMS), state and local agencies, and self-surrenders. Offenders arrested for federal offenses are transferred to the custody of the USMS for processing, transportation, and detention. The Prisoner Tracking System contains data on all offenders within the custody of the USMS. The data file contains variables from the original USMS files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.1-1.3. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR23720.v3",
+                    "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 1994 [United States]"
+                }
+            ],
+            "identifier": "780",
+            "isPartOf": "2174",
+            "issued": "2009-02-09T13:15:28",
             "keyword": [
                 "arrest records",
                 "arrests",
@@ -17570,55 +17564,55 @@
                 "federal prisoners",
                 "offenders"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2015-06-16T13:03:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-09T13:15:28",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR23720.v3",
-                    "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 1994 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 1995 [United States]",
-            "description": "The data contain records of arrests and bookings for federal offenses in the United States during fiscal year 1995. The data were constructed from the United States Marshals Service (USMS) Prisoner Tracking System database. Records include arrests made by federal law enforcement agencies (including the USMS), state and local agencies, and self-surrenders. Offenders arrested for federal offenses are transferred to the custody of the USMS for processing, transportation, and detention. The Prisoner Tracking System contains data on all offenders within the custody of the USMS. The data file contains variables from the original USMS files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.1-1.3. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2015-06-16T13:24:44",
-            "accessLevel": "restricted public",
-            "identifier": "781",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 1994 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of arrests and bookings for federal offenses in the United States during fiscal year 1995. The data were constructed from the United States Marshals Service (USMS) Prisoner Tracking System database. Records include arrests made by federal law enforcement agencies (including the USMS), state and local agencies, and self-surrenders. Offenders arrested for federal offenses are transferred to the custody of the USMS for processing, transportation, and detention. The Prisoner Tracking System contains data on all offenders within the custody of the USMS. The data file contains variables from the original USMS files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.1-1.3. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24012.v3",
+                    "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 1995 [United States]"
+                }
+            ],
+            "identifier": "781",
+            "isPartOf": "2174",
+            "issued": "2009-02-09T13:18:04",
             "keyword": [
                 "arrest records",
                 "arrests",
@@ -17626,55 +17620,55 @@
                 "federal prisoners",
                 "offenders"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2015-06-16T13:24:44",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-09T13:18:04",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24012.v3",
-                    "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 1995 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 1996 [United States]",
-            "description": "The data contain records of arrests and bookings for federal offenses in the United States during fiscal year 1996. The data were constructed from the United States Marshals Service (USMS) Prisoner Tracking System database. Records include arrests made by federal law enforcement agencies (including the USMS), state and local agencies, and self-surrenders. Offenders arrested for federal offenses are transferred to the custody of the USMS for processing, transportation, and detention. The Prisoner Tracking System contains data on all offenders within the custody of the USMS. The data file contains variables from the original USMS files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.1-1.3. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2015-06-16T13:50:39",
-            "accessLevel": "restricted public",
-            "identifier": "782",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 1995 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of arrests and bookings for federal offenses in the United States during fiscal year 1996. The data were constructed from the United States Marshals Service (USMS) Prisoner Tracking System database. Records include arrests made by federal law enforcement agencies (including the USMS), state and local agencies, and self-surrenders. Offenders arrested for federal offenses are transferred to the custody of the USMS for processing, transportation, and detention. The Prisoner Tracking System contains data on all offenders within the custody of the USMS. The data file contains variables from the original USMS files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.1-1.3. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24031.v3",
+                    "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 1996 [United States]"
+                }
+            ],
+            "identifier": "782",
+            "isPartOf": "2174",
+            "issued": "2009-02-09T13:20:29",
             "keyword": [
                 "arrest records",
                 "arrests",
@@ -17682,55 +17676,55 @@
                 "federal prisoners",
                 "offenders"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2015-06-16T13:50:39",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-09T13:20:29",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24031.v3",
-                    "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 1996 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 1997 [United States]",
-            "description": "The data contain records of arrests and bookings for federal offenses in the United States during fiscal year 1997. The data were constructed from the United States Marshals Service (USMS) Prisoner Tracking System database. Records include arrests made by federal law enforcement agencies (including the USMS), state and local agencies, and self-surrenders. Offenders arrested for federal offenses are transferred to the custody of the USMS for processing, transportation, and detention. The Prisoner Tracking System contains data on all offenders within the custody of the USMS. The data file contains variables from the original USMS files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.1-1.3. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2015-06-15T13:06:08",
-            "accessLevel": "restricted public",
-            "identifier": "783",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 1996 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of arrests and bookings for federal offenses in the United States during fiscal year 1997. The data were constructed from the United States Marshals Service (USMS) Prisoner Tracking System database. Records include arrests made by federal law enforcement agencies (including the USMS), state and local agencies, and self-surrenders. Offenders arrested for federal offenses are transferred to the custody of the USMS for processing, transportation, and detention. The Prisoner Tracking System contains data on all offenders within the custody of the USMS. The data file contains variables from the original USMS files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.1-1.3. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24050.v3",
+                    "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 1997 [United States]"
+                }
+            ],
+            "identifier": "783",
+            "isPartOf": "2174",
+            "issued": "2009-02-09T13:28:52",
             "keyword": [
                 "arrest records",
                 "arrests",
@@ -17738,55 +17732,55 @@
                 "federal prisoners",
                 "offenders"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2015-06-15T13:06:08",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-09T13:28:52",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24050.v3",
-                    "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 1997 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 1998 [United States]",
-            "description": "The data contain records of arrests and bookings for federal offenses in the United States during fiscal year 1998. The data were constructed from the United States Marshals Service (USMS) Prisoner Tracking System database. Records include arrests made by federal law enforcement agencies (including the USMS), state and local agencies, and self-surrenders. Offenders arrested for federal offenses are transferred to the custody of the USMS for processing, transportation, and detention. The Prisoner Tracking System contains data on all offenders within the custody of the USMS. The data file contains variables from the original USMS files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.1-1.3. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2015-06-15T13:10:39",
-            "accessLevel": "restricted public",
-            "identifier": "784",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 1997 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of arrests and bookings for federal offenses in the United States during fiscal year 1998. The data were constructed from the United States Marshals Service (USMS) Prisoner Tracking System database. Records include arrests made by federal law enforcement agencies (including the USMS), state and local agencies, and self-surrenders. Offenders arrested for federal offenses are transferred to the custody of the USMS for processing, transportation, and detention. The Prisoner Tracking System contains data on all offenders within the custody of the USMS. The data file contains variables from the original USMS files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.1-1.3. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24069.v3",
+                    "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 1998 [United States]"
+                }
+            ],
+            "identifier": "784",
+            "isPartOf": "2174",
+            "issued": "2009-02-09T13:31:10",
             "keyword": [
                 "arrest records",
                 "arrests",
@@ -17794,55 +17788,55 @@
                 "federal prisoners",
                 "offenders"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2015-06-15T13:10:39",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-09T13:31:10",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24069.v3",
-                    "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 1998 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 1999 [United States]",
-            "description": "The data contain records of arrests and bookings for federal offenses in the United States during fiscal year 1999. The data were constructed from the United States Marshals Service (USMS) Prisoner Tracking System database. Records include arrests made by federal law enforcement agencies (including the USMS), state and local agencies, and self-surrenders. Offenders arrested for federal offenses are transferred to the custody of the USMS for processing, transportation, and detention. The Prisoner Tracking System contains data on all offenders within the custody of the USMS. The data file contains variables from the original USMS files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.1-1.3. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2015-06-15T13:37:26",
-            "accessLevel": "restricted public",
-            "identifier": "785",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 1998 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of arrests and bookings for federal offenses in the United States during fiscal year 1999. The data were constructed from the United States Marshals Service (USMS) Prisoner Tracking System database. Records include arrests made by federal law enforcement agencies (including the USMS), state and local agencies, and self-surrenders. Offenders arrested for federal offenses are transferred to the custody of the USMS for processing, transportation, and detention. The Prisoner Tracking System contains data on all offenders within the custody of the USMS. The data file contains variables from the original USMS files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.1-1.3. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24088.v3",
+                    "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 1999 [United States]"
+                }
+            ],
+            "identifier": "785",
+            "isPartOf": "2174",
+            "issued": "2009-02-09T13:34:19",
             "keyword": [
                 "arrest records",
                 "arrests",
@@ -17850,55 +17844,55 @@
                 "federal prisoners",
                 "offenders"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2015-06-15T13:37:26",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-09T13:34:19",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24088.v3",
-                    "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 1999 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 2000 [United States]",
-            "description": "The data contain records of arrests and bookings for federal offenses in the United States during fiscal year 2000. The data were constructed from the United States Marshals Service (USMS) Prisoner Tracking System database. Records include arrests made by federal law enforcement agencies (including the USMS), state and local agencies, and self-surrenders. Offenders arrested for federal offenses are transferred to the custody of the USMS for processing, transportation, and detention. The Prisoner Tracking System contains data on all offenders within the custody of the USMS. The data file contains variables from the original USMS files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.1-1.3. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2015-06-15T13:42:33",
-            "accessLevel": "restricted public",
-            "identifier": "786",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 1999 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of arrests and bookings for federal offenses in the United States during fiscal year 2000. The data were constructed from the United States Marshals Service (USMS) Prisoner Tracking System database. Records include arrests made by federal law enforcement agencies (including the USMS), state and local agencies, and self-surrenders. Offenders arrested for federal offenses are transferred to the custody of the USMS for processing, transportation, and detention. The Prisoner Tracking System contains data on all offenders within the custody of the USMS. The data file contains variables from the original USMS files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.1-1.3. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24107.v3",
+                    "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 2000 [United States]"
+                }
+            ],
+            "identifier": "786",
+            "isPartOf": "2174",
+            "issued": "2009-02-09T13:38:07",
             "keyword": [
                 "arrest records",
                 "arrests",
@@ -17906,55 +17900,55 @@
                 "federal prisoners",
                 "offenders"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2015-06-15T13:42:33",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-09T13:38:07",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24107.v3",
-                    "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 2000 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 2001 [United States]",
-            "description": "The data contain records of arrests and bookings for federal offenses in the United States during fiscal year 2001. The data were constructed from the United States Marshals Service (USMS) Prisoner Tracking System database. Records include arrests made by federal law enforcement agencies (including the USMS), state and local agencies, and self-surrenders. Offenders arrested for federal offenses are transferred to the custody of the USMS for processing, transportation, and detention. The Prisoner Tracking System contains data on all offenders within the custody of the USMS. The data file contains variables from the original USMS files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.1-1.3. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2015-06-15T13:47:30",
-            "accessLevel": "restricted public",
-            "identifier": "787",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 2000 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of arrests and bookings for federal offenses in the United States during fiscal year 2001. The data were constructed from the United States Marshals Service (USMS) Prisoner Tracking System database. Records include arrests made by federal law enforcement agencies (including the USMS), state and local agencies, and self-surrenders. Offenders arrested for federal offenses are transferred to the custody of the USMS for processing, transportation, and detention. The Prisoner Tracking System contains data on all offenders within the custody of the USMS. The data file contains variables from the original USMS files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.1-1.3. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24126.v3",
+                    "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 2001 [United States]"
+                }
+            ],
+            "identifier": "787",
+            "isPartOf": "2174",
+            "issued": "2009-02-09T13:41:59",
             "keyword": [
                 "arrest records",
                 "arrests",
@@ -17962,55 +17956,55 @@
                 "federal prisoners",
                 "offenders"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2015-06-15T13:47:30",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-09T13:41:59",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24126.v3",
-                    "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 2001 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 2002 [United States]",
-            "description": "The data contain records of arrests and bookings for federal offenses in the United States during fiscal year 2002. The data were constructed from the United States Marshals Service (USMS) Prisoner Tracking System database. Records include arrests made by federal law enforcement agencies (including the USMS), state and local agencies, and self-surrenders. Offenders arrested for federal offenses are transferred to the custody of the USMS for processing, transportation, and detention. The Prisoner Tracking System contains data on all offenders within the custody of the USMS. The data file contains variables from the original USMS files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.1-1.3. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2013-10-01T11:04:03",
-            "accessLevel": "restricted public",
-            "identifier": "788",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 2001 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of arrests and bookings for federal offenses in the United States during fiscal year 2002. The data were constructed from the United States Marshals Service (USMS) Prisoner Tracking System database. Records include arrests made by federal law enforcement agencies (including the USMS), state and local agencies, and self-surrenders. Offenders arrested for federal offenses are transferred to the custody of the USMS for processing, transportation, and detention. The Prisoner Tracking System contains data on all offenders within the custody of the USMS. The data file contains variables from the original USMS files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.1-1.3. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24145.v3",
+                    "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 2002 [United States]"
+                }
+            ],
+            "identifier": "788",
+            "isPartOf": "2174",
+            "issued": "2009-02-09T13:47:29",
             "keyword": [
                 "arrest records",
                 "arrests",
@@ -18018,111 +18012,111 @@
                 "federal prisoners",
                 "offenders"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-10-01T11:04:03",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-09T13:47:29",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24145.v3",
-                    "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 2002 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 2003 [United States]",
-            "description": "The data contain records of arrests and bookings for federal offenses in the United States during fiscal year 2003. The data were constructed from the United States Marshals Service (USMS) Prisoner Tracking System database. Records include arrests made by federal law enforcement agencies (including the USMS), state and local agencies, and self-surrenders. Offenders arrested for federal offenses are transferred to the custody of the USMS for processing, transportation, and detention. The Prisoner Tracking System contains data on all offenders within the custody of the USMS. The data file contains variables from the original USMS files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.1-1.3. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2013-09-24T10:17:41",
-            "accessLevel": "restricted public",
-            "identifier": "789",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 2002 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
-            "keyword": [
-                "arrest records",
-                "arrests",
-                "federal offenses",
-                "federal prisoners",
-                "offenders"
-            ],
-            "bureauCode": [
-                "011:21"
-            ],
-            "programCode": [
-                "011:061"
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
             "dataQuality": false,
-            "issued": "2009-02-09T13:51:58",
-            "language": [
-                "eng"
-            ],
+            "description": "The data contain records of arrests and bookings for federal offenses in the United States during fiscal year 2003. The data were constructed from the United States Marshals Service (USMS) Prisoner Tracking System database. Records include arrests made by federal law enforcement agencies (including the USMS), state and local agencies, and self-surrenders. Offenders arrested for federal offenses are transferred to the custody of the USMS for processing, transportation, and detention. The Prisoner Tracking System contains data on all offenders within the custody of the USMS. The data file contains variables from the original USMS files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.1-1.3. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://doi.org/10.3886/ICPSR24164.v3",
                     "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 2003 [United States]"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 2004 [United States]",
-            "description": "The data contain records of arrests and bookings for federal offenses in the United States during fiscal year 2004. The data were constructed from the United States Marshals Service (USMS) Prisoner Tracking System database. Records include arrests made by federal law enforcement agencies (including the USMS), state and local agencies, and self-surrenders. Offenders arrested for federal offenses are transferred to the custody of the USMS for processing, transportation, and detention. The Prisoner Tracking System contains data on all offenders within the custody of the USMS. The data file contains variables from the original USMS files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.1-1.3. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2013-09-19T12:08:48",
-            "accessLevel": "restricted public",
-            "identifier": "790",
+            ],
+            "identifier": "789",
+            "isPartOf": "2174",
+            "issued": "2009-02-09T13:51:58",
+            "keyword": [
+                "arrest records",
+                "arrests",
+                "federal offenses",
+                "federal prisoners",
+                "offenders"
+            ],
+            "language": [
+                "eng"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-09-24T10:17:41",
+            "programCode": [
+                "011:061"
+            ],
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 2003 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of arrests and bookings for federal offenses in the United States during fiscal year 2004. The data were constructed from the United States Marshals Service (USMS) Prisoner Tracking System database. Records include arrests made by federal law enforcement agencies (including the USMS), state and local agencies, and self-surrenders. Offenders arrested for federal offenses are transferred to the custody of the USMS for processing, transportation, and detention. The Prisoner Tracking System contains data on all offenders within the custody of the USMS. The data file contains variables from the original USMS files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.1-1.3. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24181.v3",
+                    "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 2004 [United States]"
+                }
+            ],
+            "identifier": "790",
+            "isPartOf": "2174",
+            "issued": "2009-02-09T13:55:09",
             "keyword": [
                 "arrest records",
                 "arrests",
@@ -18130,55 +18124,55 @@
                 "federal prisoners",
                 "offenders"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-09-19T12:08:48",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-09T13:55:09",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24181.v3",
-                    "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 2004 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 2005 [United States]",
-            "description": "The data contain records of arrests and bookings for federal offenses in the United States during fiscal year 2005. The data were constructed from the United States Marshals Service (USMS) Prisoner Tracking System database. Records include arrests made by federal law enforcement agencies (including the USMS), state and local agencies, and self-surrenders. Offenders arrested for federal offenses are transferred to the custody of the USMS for processing, transportation, and detention. The Prisoner Tracking System contains data on all offenders within the custody of the USMS. The data file contains variables from the original USMS files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.1-1.3. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2013-09-16T16:29:52",
-            "accessLevel": "restricted public",
-            "identifier": "791",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 2004 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of arrests and bookings for federal offenses in the United States during fiscal year 2005. The data were constructed from the United States Marshals Service (USMS) Prisoner Tracking System database. Records include arrests made by federal law enforcement agencies (including the USMS), state and local agencies, and self-surrenders. Offenders arrested for federal offenses are transferred to the custody of the USMS for processing, transportation, and detention. The Prisoner Tracking System contains data on all offenders within the custody of the USMS. The data file contains variables from the original USMS files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.1-1.3. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24199.v3",
+                    "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 2005 [United States]"
+                }
+            ],
+            "identifier": "791",
+            "isPartOf": "2174",
+            "issued": "2009-02-09T13:57:59",
             "keyword": [
                 "arrest records",
                 "arrests",
@@ -18186,55 +18180,55 @@
                 "federal prisoners",
                 "offenders"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-09-16T16:29:52",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-09T13:57:59",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24199.v3",
-                    "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 2005 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 2006 [United States]",
-            "description": "The data contain records of arrests and bookings for federal offenses in the United States during fiscal year 2006. The data were constructed from the United States Marshals Service (USMS) Prisoner Tracking System database. Records include arrests made by federal law enforcement agencies (including the USMS), state and local agencies, and self-surrenders. Offenders arrested for federal offenses are transferred to the custody of the USMS for processing, transportation, and detention. The Prisoner Tracking System contains data on all offenders within the custody of the USMS. The data file contains variables from the original USMS files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.1-1.3. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2013-09-13T15:45:08",
-            "accessLevel": "restricted public",
-            "identifier": "792",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 2005 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of arrests and bookings for federal offenses in the United States during fiscal year 2006. The data were constructed from the United States Marshals Service (USMS) Prisoner Tracking System database. Records include arrests made by federal law enforcement agencies (including the USMS), state and local agencies, and self-surrenders. Offenders arrested for federal offenses are transferred to the custody of the USMS for processing, transportation, and detention. The Prisoner Tracking System contains data on all offenders within the custody of the USMS. The data file contains variables from the original USMS files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.1-1.3. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24216.v3",
+                    "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 2006 [United States]"
+                }
+            ],
+            "identifier": "792",
+            "isPartOf": "2174",
+            "issued": "2009-02-09T14:00:25",
             "keyword": [
                 "arrest records",
                 "arrests",
@@ -18242,55 +18236,55 @@
                 "federal prisoners",
                 "offenders"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-09-13T15:45:08",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-09T14:00:25",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24216.v3",
-                    "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 2006 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 2007 [United States]",
-            "description": "The data contain records of arrests and bookings for federal offenses in the United States during fiscal year 2007. The data were constructed from the United States Marshals Service (USMS) Prisoner Tracking System database. Records include arrests made by federal law enforcement agencies (including the USMS), state and local agencies, and self-surrenders. Offenders arrested for federal offenses are transferred to the custody of the USMS for processing, transportation, and detention. The Prisoner Tracking System contains data on all offenders within the custody of the USMS. The data file contains variables from the original USMS files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.1-1.3. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2013-09-13T15:06:37",
-            "accessLevel": "restricted public",
-            "identifier": "793",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 2006 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of arrests and bookings for federal offenses in the United States during fiscal year 2007. The data were constructed from the United States Marshals Service (USMS) Prisoner Tracking System database. Records include arrests made by federal law enforcement agencies (including the USMS), state and local agencies, and self-surrenders. Offenders arrested for federal offenses are transferred to the custody of the USMS for processing, transportation, and detention. The Prisoner Tracking System contains data on all offenders within the custody of the USMS. The data file contains variables from the original USMS files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.1-1.3. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24231.v3",
+                    "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 2007 [United States]"
+                }
+            ],
+            "identifier": "793",
+            "isPartOf": "2174",
+            "issued": "2009-02-09T14:04:13",
             "keyword": [
                 "arrest records",
                 "arrests",
@@ -18298,55 +18292,55 @@
                 "federal prisoners",
                 "offenders"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-09-13T15:06:37",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-09T14:04:13",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24231.v3",
-                    "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 2007 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 2008 [United States]",
-            "description": "The data contain records of arrests and bookings for federal offenses in the United States during fiscal year 2008. The data were constructed from the United States Marshals Service (USMS) Prisoner Tracking System database. Records include arrests made by federal law enforcement agencies (including the USMS), state and local agencies, and self-surrenders. Offenders arrested for federal offenses are transferred to the custody of the USMS for processing, transportation, and detention. The Prisoner Tracking System contains data on all offenders within the custody of the USMS. The data file contains variables from the original USMS files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.1-1.3. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T12:14:38",
-            "accessLevel": "restricted public",
-            "identifier": "794",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 2007 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of arrests and bookings for federal offenses in the United States during fiscal year 2008. The data were constructed from the United States Marshals Service (USMS) Prisoner Tracking System database. Records include arrests made by federal law enforcement agencies (including the USMS), state and local agencies, and self-surrenders. Offenders arrested for federal offenses are transferred to the custody of the USMS for processing, transportation, and detention. The Prisoner Tracking System contains data on all offenders within the custody of the USMS. The data file contains variables from the original USMS files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.1-1.3. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR29428.v2",
+                    "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 2008 [United States]"
+                }
+            ],
+            "identifier": "794",
+            "isPartOf": "2174",
+            "issued": "2011-02-22T11:23:59",
             "keyword": [
                 "arrest records",
                 "arrests",
@@ -18354,55 +18348,55 @@
                 "federal prisoners",
                 "offenders"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T12:14:38",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2011-02-22T11:23:59",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR29428.v2",
-                    "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 2008 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 2009",
-            "description": "The data contain records of arrests and bookings for federal offenses in the United States during fiscal year 2009. The data were constructed from the United States Marshals Service (USMS) Prisoner Tracking System database. Records include arrests made by federal law enforcement agencies (including the USMS), state and local agencies, and self-surrenders. Offenders arrested for federal offenses are transferred to the custody of the USMS for processing, transportation, and detention. The Prisoner Tracking System contains data on all offenders within the custody of the USMS. The data file contains variables from the original USMS files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.1-1.3. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-07-22T17:31:11",
-            "accessLevel": "restricted public",
-            "identifier": "795",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 2008 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of arrests and bookings for federal offenses in the United States during fiscal year 2009. The data were constructed from the United States Marshals Service (USMS) Prisoner Tracking System database. Records include arrests made by federal law enforcement agencies (including the USMS), state and local agencies, and self-surrenders. Offenders arrested for federal offenses are transferred to the custody of the USMS for processing, transportation, and detention. The Prisoner Tracking System contains data on all offenders within the custody of the USMS. The data file contains variables from the original USMS files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.1-1.3. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR30794.v1",
+                    "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 2009"
+                }
+            ],
+            "identifier": "795",
+            "isPartOf": "2174",
+            "issued": "2011-06-06T09:07:43",
             "keyword": [
                 "arrest records",
                 "arrests",
@@ -18410,55 +18404,55 @@
                 "federal prisoners",
                 "offenders"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-07-22T17:31:11",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2011-06-06T09:07:43",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR30794.v1",
-                    "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 2009"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 2010",
-            "description": "The data contain records of arrests and bookings for federal offenses in the United States during fiscal year 2010. The data were constructed from the United States Marshals Service (USMS) Prisoner Tracking System database. Records include arrests made by federal law enforcement agencies (including the USMS), state and local agencies, and self-surrenders. Offenders arrested for federal offenses are transferred to the custody of the USMS for processing, transportation, and detention. The Prisoner Tracking System contains data on all offenders within the custody of the USMS. The data file contains variables from the original USMS files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.1-1.3. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2013-01-08T11:37:28",
-            "accessLevel": "restricted public",
-            "identifier": "796",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 2009"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of arrests and bookings for federal offenses in the United States during fiscal year 2010. The data were constructed from the United States Marshals Service (USMS) Prisoner Tracking System database. Records include arrests made by federal law enforcement agencies (including the USMS), state and local agencies, and self-surrenders. Offenders arrested for federal offenses are transferred to the custody of the USMS for processing, transportation, and detention. The Prisoner Tracking System contains data on all offenders within the custody of the USMS. The data file contains variables from the original USMS files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.1-1.3. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR34336.v1",
+                    "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 2010"
+                }
+            ],
+            "identifier": "796",
+            "isPartOf": "2174",
+            "issued": "2013-01-08T11:25:52",
             "keyword": [
                 "arrest records",
                 "arrests",
@@ -18466,1925 +18460,1925 @@
                 "federal prisoners",
                 "offenders"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-01-08T11:37:28",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2013-01-08T11:25:52",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR34336.v1",
-                    "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 2010"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 1994 [United States]",
-            "description": "The data contain records of charges filed against defendants whose cases were terminated by United States attorneys in United States district court during fiscal year 1994. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T09:47:36",
-            "accessLevel": "restricted public",
-            "identifier": "797",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 2010"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of charges filed against defendants whose cases were terminated by United States attorneys in United States district court during fiscal year 1994. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR23745.v2",
+                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 1994 [United States]"
+                }
+            ],
+            "identifier": "797",
+            "isPartOf": "2174",
+            "issued": "2009-02-13T14:29:57",
             "keyword": [
                 "defendants",
                 "district courts",
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T09:47:36",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-13T14:29:57",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR23745.v2",
-                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 1994 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 1995 [United States]",
-            "description": "The data contain records of charges filed against defendants whose cases were terminated by United States attorneys in United States district court during fiscal year 1995. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T09:59:21",
-            "accessLevel": "restricted public",
-            "identifier": "798",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 1994 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of charges filed against defendants whose cases were terminated by United States attorneys in United States district court during fiscal year 1995. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24010.v2",
+                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 1995 [United States]"
+                }
+            ],
+            "identifier": "798",
+            "isPartOf": "2174",
+            "issued": "2009-02-13T14:31:52",
             "keyword": [
                 "defendants",
                 "district courts",
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T09:59:21",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-13T14:31:52",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24010.v2",
-                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 1995 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 1996 [United States]",
-            "description": "The data contain records of charges filed against defendants whose cases were terminated by United States attorneys in United States district court during fiscal year 1996. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:09:34",
-            "accessLevel": "restricted public",
-            "identifier": "799",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 1995 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of charges filed against defendants whose cases were terminated by United States attorneys in United States district court during fiscal year 1996. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24029.v2",
+                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 1996 [United States]"
+                }
+            ],
+            "identifier": "799",
+            "isPartOf": "2174",
+            "issued": "2009-02-13T14:33:54",
             "keyword": [
                 "defendants",
                 "district courts",
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:09:34",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-13T14:33:54",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24029.v2",
-                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 1996 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 1997 [United States]",
-            "description": "The data contain records of charges filed against defendants whose cases were terminated by United States attorneys in United States district court during fiscal year 1997. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:20:23",
-            "accessLevel": "restricted public",
-            "identifier": "800",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 1996 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of charges filed against defendants whose cases were terminated by United States attorneys in United States district court during fiscal year 1997. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24048.v2",
+                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 1997 [United States]"
+                }
+            ],
+            "identifier": "800",
+            "isPartOf": "2174",
+            "issued": "2009-02-13T14:36:17",
             "keyword": [
                 "defendants",
                 "district courts",
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:20:23",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-13T14:36:17",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24048.v2",
-                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 1997 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 1998 [United States]",
-            "description": "The data contain records of charges filed against defendants whose cases were terminated by United States attorneys in United States district court during fiscal year 1998. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:31:00",
-            "accessLevel": "restricted public",
-            "identifier": "801",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 1997 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of charges filed against defendants whose cases were terminated by United States attorneys in United States district court during fiscal year 1998. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24067.v2",
+                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 1998 [United States]"
+                }
+            ],
+            "identifier": "801",
+            "isPartOf": "2174",
+            "issued": "2009-02-13T14:38:32",
             "keyword": [
                 "defendants",
                 "district courts",
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:31:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-13T14:38:32",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24067.v2",
-                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 1998 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 1999 [United States]",
-            "description": "The data contain records of charges filed against defendants whose cases were terminated by United States attorneys in United States district court during fiscal year 1999. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:41:59",
-            "accessLevel": "restricted public",
-            "identifier": "802",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 1998 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of charges filed against defendants whose cases were terminated by United States attorneys in United States district court during fiscal year 1999. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24086.v2",
+                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 1999 [United States]"
+                }
+            ],
+            "identifier": "802",
+            "isPartOf": "2174",
+            "issued": "2009-02-13T14:40:54",
             "keyword": [
                 "defendants",
                 "district courts",
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:41:59",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-13T14:40:54",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24086.v2",
-                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 1999 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 2000 [United States]",
-            "description": "The data contain records of charges filed against defendants whose cases were terminated by United States attorneys in United States district court during fiscal year 2000. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:52:44",
-            "accessLevel": "restricted public",
-            "identifier": "803",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 1999 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of charges filed against defendants whose cases were terminated by United States attorneys in United States district court during fiscal year 2000. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24105.v2",
+                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 2000 [United States]"
+                }
+            ],
+            "identifier": "803",
+            "isPartOf": "2174",
+            "issued": "2009-02-13T14:42:58",
             "keyword": [
                 "defendants",
                 "district courts",
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:52:44",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-13T14:42:58",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24105.v2",
-                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 2000 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 2001 [United States]",
-            "description": "The data contain records of charges filed against defendants whose cases were terminated by United States attorneys in United States district court during fiscal year 2001. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:03:41",
-            "accessLevel": "restricted public",
-            "identifier": "804",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 2000 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of charges filed against defendants whose cases were terminated by United States attorneys in United States district court during fiscal year 2001. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24124.v2",
+                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 2001 [United States]"
+                }
+            ],
+            "identifier": "804",
+            "isPartOf": "2174",
+            "issued": "2009-02-13T14:45:23",
             "keyword": [
                 "defendants",
                 "district courts",
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:03:41",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-13T14:45:23",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24124.v2",
-                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 2001 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 2002 [United States]",
-            "description": "The data contain records of charges filed against defendants whose cases were terminated by United States attorneys in United States district court during fiscal year 2002. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:14:28",
-            "accessLevel": "restricted public",
-            "identifier": "805",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 2001 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of charges filed against defendants whose cases were terminated by United States attorneys in United States district court during fiscal year 2002. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24143.v2",
+                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 2002 [United States]"
+                }
+            ],
+            "identifier": "805",
+            "isPartOf": "2174",
+            "issued": "2009-02-13T14:47:49",
             "keyword": [
                 "defendants",
                 "district courts",
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:14:28",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-13T14:47:49",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24143.v2",
-                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 2002 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 2003 [United States]",
-            "description": "The data contain records of charges filed against defendants whose cases were terminated by United States attorneys in United States district court during fiscal year 2003. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:25:16",
-            "accessLevel": "restricted public",
-            "identifier": "806",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 2002 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of charges filed against defendants whose cases were terminated by United States attorneys in United States district court during fiscal year 2003. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24162.v2",
+                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 2003 [United States]"
+                }
+            ],
+            "identifier": "806",
+            "isPartOf": "2174",
+            "issued": "2009-02-13T14:50:06",
             "keyword": [
                 "defendants",
                 "district courts",
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:25:16",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-13T14:50:06",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24162.v2",
-                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 2003 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 2004 [United States]",
-            "description": "The data contain records of charges filed against defendants whose cases were terminated by United States attorneys in United States district court during fiscal year 2004. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:34:50",
-            "accessLevel": "restricted public",
-            "identifier": "807",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
-                    }
+                    },
+                    "parentOrganizationID": 10
                 }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 2003 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of charges filed against defendants whose cases were terminated by United States attorneys in United States district court during fiscal year 2004. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24179.v2",
+                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 2004 [United States]"
+                }
+            ],
+            "identifier": "807",
+            "isPartOf": "2174",
+            "issued": "2009-02-13T14:52:36",
             "keyword": [
                 "defendants",
                 "district courts",
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
-            ],
-            "programCode": [
-                "011:061"
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-13T14:52:36",
             "language": [
                 "eng"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24179.v2",
-                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 2004 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 2005 [United States]",
-            "description": "The data contain records of charges filed against defendants whose cases were terminated by United States attorneys in United States district court during fiscal year 2005. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:44:25",
-            "accessLevel": "restricted public",
-            "identifier": "808",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:34:50",
+            "programCode": [
+                "011:061"
+            ],
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 2004 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of charges filed against defendants whose cases were terminated by United States attorneys in United States district court during fiscal year 2005. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24197.v2",
+                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 2005 [United States]"
+                }
+            ],
+            "identifier": "808",
+            "isPartOf": "2174",
+            "issued": "2009-02-13T14:55:13",
             "keyword": [
                 "defendants",
                 "district courts",
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:44:25",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-13T14:55:13",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24197.v2",
-                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 2005 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 2006 [United States]",
-            "description": "The data contain records of charges filed against defendants whose cases were terminated by United States attorneys in United States district court during fiscal year 2006. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:52:55",
-            "accessLevel": "restricted public",
-            "identifier": "809",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 2005 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of charges filed against defendants whose cases were terminated by United States attorneys in United States district court during fiscal year 2006. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24214.v2",
+                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 2006 [United States]"
+                }
+            ],
+            "identifier": "809",
+            "isPartOf": "2174",
+            "issued": "2009-02-13T14:57:24",
             "keyword": [
                 "defendants",
                 "district courts",
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:52:55",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-13T14:57:24",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24214.v2",
-                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 2006 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 2007 [United States]",
-            "description": "The data contain records of charges filed against defendants whose cases were terminated by United States attorneys in United States district court during fiscal year 2007. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T12:01:32",
-            "accessLevel": "restricted public",
-            "identifier": "810",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 2006 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of charges filed against defendants whose cases were terminated by United States attorneys in United States district court during fiscal year 2007. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24229.v2",
+                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 2007 [United States]"
+                }
+            ],
+            "identifier": "810",
+            "isPartOf": "2174",
+            "issued": "2009-02-19T10:45:19",
             "keyword": [
                 "defendants",
                 "district courts",
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T12:01:32",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-19T10:45:19",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24229.v2",
-                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 2007 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 2008 [United States]",
-            "description": "The data contain records of charges filed against defendants whose cases were terminated by United States attorneys in United States district court during fiscal year 2008. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T12:12:23",
-            "accessLevel": "restricted public",
-            "identifier": "811",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 2007 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of charges filed against defendants whose cases were terminated by United States attorneys in United States district court during fiscal year 2008. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR29423.v2",
+                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 2008 [United States]"
+                }
+            ],
+            "identifier": "811",
+            "isPartOf": "2174",
+            "issued": "2011-02-04T14:50:58",
             "keyword": [
                 "defendants",
                 "district courts",
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T12:12:23",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2011-02-04T14:50:58",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR29423.v2",
-                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 2008 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 2009",
-            "description": "The data contain records of charges filed against defendants whose cases were terminated by United States attorneys in United States district court during fiscal year 2009. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-06-03T17:38:41",
-            "accessLevel": "restricted public",
-            "identifier": "812",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 2008 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of charges filed against defendants whose cases were terminated by United States attorneys in United States district court during fiscal year 2009. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR30789.v1",
+                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 2009"
+                }
+            ],
+            "identifier": "812",
+            "isPartOf": "2174",
+            "issued": "2011-06-03T17:37:53",
             "keyword": [
                 "defendants",
                 "district courts",
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-06-03T17:38:41",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2011-06-03T17:37:53",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR30789.v1",
-                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 2009"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 2010",
-            "description": "The data contain records of charges filed against defendants whose cases were terminated by United States attorneys in United States district court during fiscal year 2010. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2013-01-07T14:02:52",
-            "accessLevel": "restricted public",
-            "identifier": "813",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 2009"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of charges filed against defendants whose cases were terminated by United States attorneys in United States district court during fiscal year 2010. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR34331.v1",
+                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 2010"
+                }
+            ],
+            "identifier": "813",
+            "isPartOf": "2174",
+            "issued": "2013-01-07T13:57:36",
             "keyword": [
                 "defendants",
                 "district courts",
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-01-07T14:02:52",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2013-01-07T13:57:36",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR34331.v1",
-                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 2010"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 1994 [United States]",
-            "description": "The data contain records of charges filed against defendants whose cases were filed by United States attorneys in United States district court during fiscal year 1994. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T09:47:04",
-            "accessLevel": "restricted public",
-            "identifier": "814",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 2010"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of charges filed against defendants whose cases were filed by United States attorneys in United States district court during fiscal year 1994. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR23744.v2",
+                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 1994 [United States]"
+                }
+            ],
+            "identifier": "814",
+            "isPartOf": "2174",
+            "issued": "2009-02-13T13:46:18",
             "keyword": [
                 "defendants",
                 "district courts",
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T09:47:04",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-13T13:46:18",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR23744.v2",
-                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 1994 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 1995 [United States]",
-            "description": "The data contain records of charges filed against defendants whose cases were filed by United States attorneys in United States district court during fiscal year 1995. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T09:58:48",
-            "accessLevel": "restricted public",
-            "identifier": "815",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 1994 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of charges filed against defendants whose cases were filed by United States attorneys in United States district court during fiscal year 1995. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24009.v2",
+                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 1995 [United States]"
+                }
+            ],
+            "identifier": "815",
+            "isPartOf": "2174",
+            "issued": "2009-02-13T13:48:24",
             "keyword": [
                 "defendants",
                 "district courts",
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T09:58:48",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-13T13:48:24",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24009.v2",
-                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 1995 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 1996 [United States]",
-            "description": "The data contain records of charges filed against defendants whose cases were filed by United States attorneys in United States district court during fiscal year 1996. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:09:02",
-            "accessLevel": "restricted public",
-            "identifier": "816",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 1995 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of charges filed against defendants whose cases were filed by United States attorneys in United States district court during fiscal year 1996. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24028.v2",
+                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 1996 [United States]"
+                }
+            ],
+            "identifier": "816",
+            "isPartOf": "2174",
+            "issued": "2009-02-13T13:50:35",
             "keyword": [
                 "defendants",
                 "district courts",
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:09:02",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-13T13:50:35",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24028.v2",
-                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 1996 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 1997 [United States]",
-            "description": "The data contain records of charges filed against defendants whose cases were filed by United States attorneys in United States district court during fiscal year 1997. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:19:49",
-            "accessLevel": "restricted public",
-            "identifier": "817",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 1996 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of charges filed against defendants whose cases were filed by United States attorneys in United States district court during fiscal year 1997. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24047.v2",
+                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 1997 [United States]"
+                }
+            ],
+            "identifier": "817",
+            "isPartOf": "2174",
+            "issued": "2009-02-13T14:04:44",
             "keyword": [
                 "defendants",
                 "district courts",
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:19:49",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-13T14:04:44",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24047.v2",
-                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 1997 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 1998 [United States]",
-            "description": "The data contain records of charges filed against defendants whose cases were filed by United States attorneys in United States district court during fiscal year 1998. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:30:27",
-            "accessLevel": "restricted public",
-            "identifier": "818",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 1997 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of charges filed against defendants whose cases were filed by United States attorneys in United States district court during fiscal year 1998. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24066.v2",
+                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 1998 [United States]"
+                }
+            ],
+            "identifier": "818",
+            "isPartOf": "2174",
+            "issued": "2009-02-13T14:06:55",
             "keyword": [
                 "defendants",
                 "district courts",
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:30:27",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-13T14:06:55",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24066.v2",
-                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 1998 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 1999 [United States]",
-            "description": "The data contain records of charges filed against defendants whose cases were filed by United States attorneys in United States district court during fiscal year 1999. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:41:18",
-            "accessLevel": "restricted public",
-            "identifier": "819",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 1998 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of charges filed against defendants whose cases were filed by United States attorneys in United States district court during fiscal year 1999. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24085.v2",
+                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 1999 [United States]"
+                }
+            ],
+            "identifier": "819",
+            "isPartOf": "2174",
+            "issued": "2009-02-13T14:08:51",
             "keyword": [
                 "defendants",
                 "district courts",
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:41:18",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-13T14:08:51",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24085.v2",
-                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 1999 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 2000 [United States]",
-            "description": "The data contain records of charges filed against defendants whose cases were filed by United States attorneys in United States district court during fiscal year 2000. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:52:10",
-            "accessLevel": "restricted public",
-            "identifier": "820",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 1999 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of charges filed against defendants whose cases were filed by United States attorneys in United States district court during fiscal year 2000. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24104.v2",
+                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 2000 [United States]"
+                }
+            ],
+            "identifier": "820",
+            "isPartOf": "2174",
+            "issued": "2009-02-13T14:11:21",
             "keyword": [
                 "defendants",
                 "district courts",
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:52:10",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-13T14:11:21",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24104.v2",
-                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 2000 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 2001 [United States]",
-            "description": "The data contain records of charges filed against defendants whose cases were filed by United States attorneys in United States district court during fiscal year 2001. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:03:05",
-            "accessLevel": "restricted public",
-            "identifier": "821",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 2000 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of charges filed against defendants whose cases were filed by United States attorneys in United States district court during fiscal year 2001. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24123.v2",
+                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 2001 [United States]"
+                }
+            ],
+            "identifier": "821",
+            "isPartOf": "2174",
+            "issued": "2009-02-13T14:13:24",
             "keyword": [
                 "defendants",
                 "district courts",
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:03:05",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-13T14:13:24",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24123.v2",
-                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 2001 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 2002 [United States]",
-            "description": "The data contain records of charges filed against defendants whose cases were filed by United States attorneys in United States district court during fiscal year 2002. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:13:50",
-            "accessLevel": "restricted public",
-            "identifier": "822",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 2001 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of charges filed against defendants whose cases were filed by United States attorneys in United States district court during fiscal year 2002. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24142.v2",
+                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 2002 [United States]"
+                }
+            ],
+            "identifier": "822",
+            "isPartOf": "2174",
+            "issued": "2009-02-13T14:16:15",
             "keyword": [
                 "defendants",
                 "district courts",
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:13:50",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-13T14:16:15",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24142.v2",
-                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 2002 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 2003 [United States]",
-            "description": "The data contain records of charges filed against defendants whose cases were filed by United States attorneys in United States district court during fiscal year 2003. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:24:42",
-            "accessLevel": "restricted public",
-            "identifier": "823",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 2002 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of charges filed against defendants whose cases were filed by United States attorneys in United States district court during fiscal year 2003. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24161.v2",
+                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 2003 [United States]"
+                }
+            ],
+            "identifier": "823",
+            "isPartOf": "2174",
+            "issued": "2009-02-13T14:18:24",
             "keyword": [
                 "defendants",
                 "district courts",
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:24:42",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-13T14:18:24",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24161.v2",
-                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 2003 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 2004 [United States]",
-            "description": "The data contain records of charges filed against defendants whose cases were filed by United States attorneys in United States district court during fiscal year 2004. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:34:16",
-            "accessLevel": "restricted public",
-            "identifier": "824",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 2003 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of charges filed against defendants whose cases were filed by United States attorneys in United States district court during fiscal year 2004. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24178.v2",
+                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 2004 [United States]"
+                }
+            ],
+            "identifier": "824",
+            "isPartOf": "2174",
+            "issued": "2009-02-13T14:20:39",
             "keyword": [
                 "defendants",
                 "district courts",
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:34:16",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-13T14:20:39",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24178.v2",
-                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 2004 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 2005 [United States]",
-            "description": "The data contain records of charges filed against defendants whose cases were filed by United States attorneys in United States district court during fiscal year 2005. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:43:51",
-            "accessLevel": "restricted public",
-            "identifier": "825",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 2004 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of charges filed against defendants whose cases were filed by United States attorneys in United States district court during fiscal year 2005. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24196.v2",
+                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 2005 [United States]"
+                }
+            ],
+            "identifier": "825",
+            "isPartOf": "2174",
+            "issued": "2009-02-13T14:22:45",
             "keyword": [
                 "defendants",
                 "district courts",
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:43:51",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-13T14:22:45",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24196.v2",
-                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 2005 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 2006 [United States]",
-            "description": "The data contain records of charges filed against defendants whose cases were filed by United States attorneys in United States district court during fiscal year 2006. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:52:19",
-            "accessLevel": "restricted public",
-            "identifier": "826",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 2005 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of charges filed against defendants whose cases were filed by United States attorneys in United States district court during fiscal year 2006. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24213.v2",
+                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 2006 [United States]"
+                }
+            ],
+            "identifier": "826",
+            "isPartOf": "2174",
+            "issued": "2009-02-13T14:27:36",
             "keyword": [
                 "defendants",
                 "district courts",
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:52:19",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-13T14:27:36",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24213.v2",
-                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 2006 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 2007 [United States]",
-            "description": "The data contain records of charges filed against defendants whose cases were filed by United States attorneys in United States district court during fiscal year 2007. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T12:25:13",
-            "accessLevel": "restricted public",
-            "identifier": "827",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 2006 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of charges filed against defendants whose cases were filed by United States attorneys in United States district court during fiscal year 2007. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24228.v2",
+                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 2007 [United States]"
+                }
+            ],
+            "identifier": "827",
+            "isPartOf": "2174",
+            "issued": "2009-02-19T10:42:07",
             "keyword": [
                 "defendants",
                 "district courts",
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T12:25:13",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-19T10:42:07",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24228.v2",
-                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 2007 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 2008 [United States]",
-            "description": "The data contain records of charges filed against defendants whose cases were filed by United States attorneys in United States district court during fiscal year 2008. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T12:11:49",
-            "accessLevel": "restricted public",
-            "identifier": "828",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 2007 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of charges filed against defendants whose cases were filed by United States attorneys in United States district court during fiscal year 2008. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR29421.v2",
+                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 2008 [United States]"
+                }
+            ],
+            "identifier": "828",
+            "isPartOf": "2174",
+            "issued": "2011-02-04T14:16:39",
             "keyword": [
                 "defendants",
                 "district courts",
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T12:11:49",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2011-02-04T14:16:39",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR29421.v2",
-                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 2008 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 2009",
-            "description": "The data contain records of charges filed against defendants whose cases were filed by United States attorneys in United States district court during fiscal year 2009. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-06-03T17:33:30",
-            "accessLevel": "restricted public",
-            "identifier": "829",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 2008 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of charges filed against defendants whose cases were filed by United States attorneys in United States district court during fiscal year 2009. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR30788.v1",
+                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 2009"
+                }
+            ],
+            "identifier": "829",
+            "isPartOf": "2174",
+            "issued": "2011-06-03T17:32:33",
             "keyword": [
                 "defendants",
                 "district courts",
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-06-03T17:33:30",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2011-06-03T17:32:33",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR30788.v1",
-                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 2009"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 2010",
-            "description": "The data contain records of charges filed against defendants whose cases were filed by United States attorneys in United States district court during fiscal year 2010. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2013-01-07T13:52:22",
-            "accessLevel": "restricted public",
-            "identifier": "830",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 2009"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of charges filed against defendants whose cases were filed by United States attorneys in United States district court during fiscal year 2010. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR34330.v1",
+                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 2010"
+                }
+            ],
+            "identifier": "830",
+            "isPartOf": "2174",
+            "issued": "2013-01-07T13:40:52",
             "keyword": [
                 "defendants",
                 "district courts",
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-01-07T13:52:22",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2013-01-07T13:40:52",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR34330.v1",
-                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 2010"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 1995 [United States]",
-            "description": "The data contain records of criminal appeals cases filed in United States Courts of Appeals during fiscal year 1995. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T09:52:42",
-            "accessLevel": "restricted public",
-            "identifier": "831",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 2010"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of criminal appeals cases filed in United States Courts of Appeals during fiscal year 1995. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR23768.v2",
+                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 1995 [United States]"
+                }
+            ],
+            "identifier": "831",
+            "isPartOf": "2174",
+            "issued": "2009-02-04T07:50:47",
             "keyword": [
                 "administration",
                 "appellate courts",
@@ -20395,55 +20389,55 @@
                 "judicial decisions",
                 "legal systems"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T09:52:42",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-04T07:50:47",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR23768.v2",
-                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 1995 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 1996 [United States]",
-            "description": "The data contain records of criminal appeals cases filed in United States Courts of Appeals during fiscal year 1996. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T09:55:30",
-            "accessLevel": "restricted public",
-            "identifier": "832",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 1995 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of criminal appeals cases filed in United States Courts of Appeals during fiscal year 1996. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24003.v2",
+                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 1996 [United States]"
+                }
+            ],
+            "identifier": "832",
+            "isPartOf": "2174",
+            "issued": "2009-02-04T07:54:53",
             "keyword": [
                 "administration",
                 "appellate courts",
@@ -20454,55 +20448,55 @@
                 "judicial decisions",
                 "legal systems"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T09:55:30",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-04T07:54:53",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24003.v2",
-                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 1996 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 1997 [United States]",
-            "description": "The data contain records of criminal appeals cases filed in United States Courts of Appeals during fiscal year 1997. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:05:51",
-            "accessLevel": "restricted public",
-            "identifier": "833",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 1996 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of criminal appeals cases filed in United States Courts of Appeals during fiscal year 1997. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24022.v2",
+                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 1997 [United States]"
+                }
+            ],
+            "identifier": "833",
+            "isPartOf": "2174",
+            "issued": "2009-02-04T07:57:11",
             "keyword": [
                 "administration",
                 "appellate courts",
@@ -20513,55 +20507,55 @@
                 "judicial decisions",
                 "legal systems"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:05:51",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-04T07:57:11",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24022.v2",
-                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 1997 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 1998 [United States]",
-            "description": "The data contain records of criminal appeals cases filed in United States Courts of Appeals during fiscal year 1998. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:16:28",
-            "accessLevel": "restricted public",
-            "identifier": "834",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 1997 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of criminal appeals cases filed in United States Courts of Appeals during fiscal year 1998. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24041.v2",
+                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 1998 [United States]"
+                }
+            ],
+            "identifier": "834",
+            "isPartOf": "2174",
+            "issued": "2009-02-04T09:15:44",
             "keyword": [
                 "administration",
                 "appellate courts",
@@ -20572,55 +20566,55 @@
                 "judicial decisions",
                 "legal systems"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:16:28",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-04T09:15:44",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24041.v2",
-                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 1998 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 1999 [United States]",
-            "description": "The data contain records of criminal appeals cases filed in United States Courts of Appeals during fiscal year 1999. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:27:01",
-            "accessLevel": "restricted public",
-            "identifier": "835",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 1998 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of criminal appeals cases filed in United States Courts of Appeals during fiscal year 1999. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24060.v2",
+                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 1999 [United States]"
+                }
+            ],
+            "identifier": "835",
+            "isPartOf": "2174",
+            "issued": "2009-02-04T08:01:16",
             "keyword": [
                 "administration",
                 "appellate courts",
@@ -20631,55 +20625,55 @@
                 "judicial decisions",
                 "legal systems"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:27:01",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-04T08:01:16",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24060.v2",
-                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 1999 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 2000 [United States]",
-            "description": "The data contain records of criminal appeals cases filed in United States Courts of Appeals during fiscal year 2000. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:37:51",
-            "accessLevel": "restricted public",
-            "identifier": "836",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 1999 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of criminal appeals cases filed in United States Courts of Appeals during fiscal year 2000. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24079.v2",
+                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 2000 [United States]"
+                }
+            ],
+            "identifier": "836",
+            "isPartOf": "2174",
+            "issued": "2009-02-04T08:03:51",
             "keyword": [
                 "administration",
                 "appellate courts",
@@ -20690,55 +20684,55 @@
                 "judicial decisions",
                 "legal systems"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:37:51",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-04T08:03:51",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24079.v2",
-                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 2000 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 2001 [United States]",
-            "description": "The data contain records of criminal appeals cases filed in United States Courts of Appeals during fiscal year 2001. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:48:46",
-            "accessLevel": "restricted public",
-            "identifier": "837",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 2000 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of criminal appeals cases filed in United States Courts of Appeals during fiscal year 2001. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24098.v2",
+                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 2001 [United States]"
+                }
+            ],
+            "identifier": "837",
+            "isPartOf": "2174",
+            "issued": "2009-02-04T08:06:07",
             "keyword": [
                 "administration",
                 "appellate courts",
@@ -20749,55 +20743,55 @@
                 "judicial decisions",
                 "legal systems"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:48:46",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-04T08:06:07",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24098.v2",
-                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 2001 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 2002 [United States]",
-            "description": "The data contain records of criminal appeals cases filed in United States Courts of Appeals during fiscal year 2002. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:59:40",
-            "accessLevel": "restricted public",
-            "identifier": "838",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 2001 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of criminal appeals cases filed in United States Courts of Appeals during fiscal year 2002. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24117.v2",
+                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 2002 [United States]"
+                }
+            ],
+            "identifier": "838",
+            "isPartOf": "2174",
+            "issued": "2009-02-04T08:08:36",
             "keyword": [
                 "administration",
                 "appellate courts",
@@ -20808,55 +20802,55 @@
                 "judicial decisions",
                 "legal systems"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:59:40",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-04T08:08:36",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24117.v2",
-                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 2002 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 2003 [United States]",
-            "description": "The data contain records of criminal appeals cases filed in United States Courts of Appeals during fiscal year 2003. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:10:31",
-            "accessLevel": "restricted public",
-            "identifier": "839",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 2002 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of criminal appeals cases filed in United States Courts of Appeals during fiscal year 2003. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24136.v2",
+                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 2003 [United States]"
+                }
+            ],
+            "identifier": "839",
+            "isPartOf": "2174",
+            "issued": "2009-02-04T08:11:20",
             "keyword": [
                 "administration",
                 "appellate courts",
@@ -20867,55 +20861,55 @@
                 "judicial decisions",
                 "legal systems"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:10:31",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-04T08:11:20",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24136.v2",
-                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 2003 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 2004 [United States]",
-            "description": "The data contain records of criminal appeals cases filed in United States Courts of Appeals during fiscal year 2004. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:21:30",
-            "accessLevel": "restricted public",
-            "identifier": "840",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 2003 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of criminal appeals cases filed in United States Courts of Appeals during fiscal year 2004. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24155.v2",
+                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 2004 [United States]"
+                }
+            ],
+            "identifier": "840",
+            "isPartOf": "2174",
+            "issued": "2009-02-04T08:14:29",
             "keyword": [
                 "administration",
                 "appellate courts",
@@ -20926,55 +20920,55 @@
                 "judicial decisions",
                 "legal systems"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:21:30",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-04T08:14:29",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24155.v2",
-                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 2004 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 2005 [United States]",
-            "description": "The data contain records of criminal appeals cases filed in United States Courts of Appeals during fiscal year 2005. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:30:54",
-            "accessLevel": "restricted public",
-            "identifier": "841",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 2004 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of criminal appeals cases filed in United States Courts of Appeals during fiscal year 2005. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24172.v2",
+                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 2005 [United States]"
+                }
+            ],
+            "identifier": "841",
+            "isPartOf": "2174",
+            "issued": "2009-02-04T08:17:43",
             "keyword": [
                 "administration",
                 "appellate courts",
@@ -20985,55 +20979,55 @@
                 "judicial decisions",
                 "legal systems"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:30:54",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-04T08:17:43",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24172.v2",
-                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 2005 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 2006 [United States]",
-            "description": "The data contain records of criminal appeals cases filed in United States Courts of Appeals during fiscal year 2006. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:40:30",
-            "accessLevel": "restricted public",
-            "identifier": "842",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 2005 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of criminal appeals cases filed in United States Courts of Appeals during fiscal year 2006. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24189.v2",
+                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 2006 [United States]"
+                }
+            ],
+            "identifier": "842",
+            "isPartOf": "2174",
+            "issued": "2009-02-04T08:20:49",
             "keyword": [
                 "administration",
                 "appellate courts",
@@ -21044,55 +21038,55 @@
                 "judicial decisions",
                 "legal systems"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:40:30",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-04T08:20:49",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24189.v2",
-                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 2006 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 2007",
-            "description": "The data contain records of criminal appeals cases filed in United States Courts of Appeals during fiscal year 2007. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-07-29T15:55:01",
-            "accessLevel": "restricted public",
-            "identifier": "843",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 2006 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of criminal appeals cases filed in United States Courts of Appeals during fiscal year 2007. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24207.v1",
+                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 2007"
+                }
+            ],
+            "identifier": "843",
+            "isPartOf": "2174",
+            "issued": "2011-07-29T15:53:44",
             "keyword": [
                 "administration",
                 "appellate courts",
@@ -21103,55 +21097,55 @@
                 "judicial decisions",
                 "legal systems"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-07-29T15:55:01",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2011-07-29T15:53:44",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24207.v1",
-                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 2007"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 1995 [United States]",
-            "description": "The data contain records of criminal appeals cases terminated in United States Courts of Appeals during fiscal year 1995. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. Appeals may be terminated on the merits or on procedural grounds. Of those that are terminated on the merits, the district court ruling may be affirmed, reversed, remanded to criminal court, or dismissed. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T09:53:15",
-            "accessLevel": "restricted public",
-            "identifier": "844",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 2007"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of criminal appeals cases terminated in United States Courts of Appeals during fiscal year 1995. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. Appeals may be terminated on the merits or on procedural grounds. Of those that are terminated on the merits, the district court ruling may be affirmed, reversed, remanded to criminal court, or dismissed. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR23769.v2",
+                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 1995 [United States]"
+                }
+            ],
+            "identifier": "844",
+            "isPartOf": "2174",
+            "issued": "2009-02-04T09:22:22",
             "keyword": [
                 "administration",
                 "appellate courts",
@@ -21162,55 +21156,55 @@
                 "judicial decisions",
                 "legal systems"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T09:53:15",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-04T09:22:22",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR23769.v2",
-                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 1995 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 1996 [United States]",
-            "description": "The data contain records of criminal appeals cases terminated in United States Courts of Appeals during fiscal year 1996. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. Appeals may be terminated on the merits or on procedural grounds. Of those that are terminated on the merits, the district court ruling may be affirmed, reversed, remanded to criminal court, or dismissed. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T09:56:04",
-            "accessLevel": "restricted public",
-            "identifier": "845",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 1995 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of criminal appeals cases terminated in United States Courts of Appeals during fiscal year 1996. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. Appeals may be terminated on the merits or on procedural grounds. Of those that are terminated on the merits, the district court ruling may be affirmed, reversed, remanded to criminal court, or dismissed. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24004.v2",
+                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 1996 [United States]"
+                }
+            ],
+            "identifier": "845",
+            "isPartOf": "2174",
+            "issued": "2009-02-04T09:25:51",
             "keyword": [
                 "administration",
                 "appellate courts",
@@ -21221,55 +21215,55 @@
                 "judicial decisions",
                 "legal systems"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T09:56:04",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-04T09:25:51",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24004.v2",
-                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 1996 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 1997 [United States]",
-            "description": "The data contain records of criminal appeals cases terminated in United States Courts of Appeals during fiscal year 1997. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. Appeals may be terminated on the merits or on procedural grounds. Of those that are terminated on the merits, the district court ruling may be affirmed, reversed, remanded to criminal court, or dismissed. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:06:23",
-            "accessLevel": "restricted public",
-            "identifier": "846",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 1996 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of criminal appeals cases terminated in United States Courts of Appeals during fiscal year 1997. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. Appeals may be terminated on the merits or on procedural grounds. Of those that are terminated on the merits, the district court ruling may be affirmed, reversed, remanded to criminal court, or dismissed. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24023.v2",
+                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 1997 [United States]"
+                }
+            ],
+            "identifier": "846",
+            "isPartOf": "2174",
+            "issued": "2009-02-04T09:29:08",
             "keyword": [
                 "administration",
                 "appellate courts",
@@ -21280,55 +21274,55 @@
                 "judicial decisions",
                 "legal systems"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:06:23",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-04T09:29:08",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24023.v2",
-                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 1997 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 1998 [United States]",
-            "description": "The data contain records of criminal appeals cases terminated in United States Courts of Appeals during fiscal year 1998. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. Appeals may be terminated on the merits or on procedural grounds. Of those that are terminated on the merits, the district court ruling may be affirmed, reversed, remanded to criminal court, or dismissed. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:17:02",
-            "accessLevel": "restricted public",
-            "identifier": "847",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
+            "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 1997 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
```

