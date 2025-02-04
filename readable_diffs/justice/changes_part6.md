# Change History for justice.json (Part 6)

### Changes from acf49f0 to dd2190f (Part 6/22)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
-            "description": "This collection contains information on federal criminal\r\ncases sentenced under the Sentencing Guidelines and Policy Statements\r\nof the Sentencing Reform Act of 1984. The data files include all cases\r\nreceived by the United States Sentencing Commission that had\r\nsentencing dates between October 1, 2004, and September 30, 2005, and\r\nwere assessed as constitutional. Constitutionality compares each\r\ncase's sentencing date, circuit, district, and judge to provide\r\nuniformity in reporting the cases. In 1999, the United States\r\nSentencing Commission added more variables from its databases to this\r\ncollection, so the data are now provided in two files. Part 1, Main\r\nData, includes the most important variables for each case, such as\r\ndefendant's age, criminal history points, armed criminal status, case\r\ndisposition, sentence, and fines applied. Part 2, Supplemental Data,\r\ncontains additional variables involving multiple guideline computation\r\nand count-based statutes. For a more detailed discussion of the two\r\nfiles, users should consult the codebook.",
-            "modified": "2014-06-25T14:31:24",
-            "accessLevel": "public",
-            "identifier": "2189",
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
+            "title": "Monitoring of Federal Criminal Convictions and Sentences: Appeals Data, 2004"
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
+            "description": "This collection contains information on federal criminal\r\ncases sentenced under the Sentencing Guidelines and Policy Statements\r\nof the Sentencing Reform Act of 1984. The data files include all cases\r\nreceived by the United States Sentencing Commission that had\r\nsentencing dates between October 1, 2004, and September 30, 2005, and\r\nwere assessed as constitutional. Constitutionality compares each\r\ncase's sentencing date, circuit, district, and judge to provide\r\nuniformity in reporting the cases. In 1999, the United States\r\nSentencing Commission added more variables from its databases to this\r\ncollection, so the data are now provided in two files. Part 1, Main\r\nData, includes the most important variables for each case, such as\r\ndefendant's age, criminal history points, armed criminal status, case\r\ndisposition, sentence, and fines applied. Part 2, Supplemental Data,\r\ncontains additional variables involving multiple guideline computation\r\nand count-based statutes. For a more detailed discussion of the two\r\nfiles, users should consult the codebook.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR04630.v2",
+                    "title": "Monitoring of Federal Criminal Sentences, [United States], 2005"
+                }
+            ],
+            "identifier": "2189",
+            "isPartOf": "2180",
+            "issued": "2007-03-20T00:00:00",
             "keyword": [
                 "convictions (law)",
                 "criminal histories",
@@ -49865,55 +49859,55 @@
                 "sentencing",
                 "sentencing guidelines"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2014-06-25T14:31:24",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2180",
-            "dataQuality": false,
-            "issued": "2007-03-20T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR04630.v2",
-                    "title": "Monitoring of Federal Criminal Sentences, [United States], 2005"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Organizations Convicted in Federal Criminal Courts, 2003",
-            "description": "These data, collected to assist in the development of\r\nsentencing guidelines, describe offense and sentencing characteristics\r\nfor organizations sentenced in federal district courts in 2003. The\r\nUnited States Sentencing Commission's primary function is to inform\r\nfederal courts of sentencing policies and practices that include\r\nguidelines prescribing the appropriate form and severity of punishment\r\nfor offenders convicted of federal crimes. Court-related variables\r\ninclude primary offense type, pecuniary offense loss and gain, dates\r\nof disposition and sentencing, method of determination of guilt,\r\nnumber of counts pled and charged, and dates and types of sentencing\r\nand restitution. Defendant organization variables include ownership\r\nstructure, number of owners and employees, highest level of corporate\r\nknowledge of the criminal offense, highest level of corporate\r\nindictment and conviction for participation in the criminal offense,\r\nannual revenue, equity and financial status, whether it was a criminal\r\norganization, duration of criminal activity, and risk to national\r\nsecurity. Organizational defendants data, 2003, covers fiscal year\r\nOctober 1, 2002, through September 30, 2003.",
-            "modified": "2014-06-27T14:37:35",
-            "accessLevel": "public",
-            "identifier": "2190",
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
+            "title": "Monitoring of Federal Criminal Sentences, [United States], 2005"
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
-            "keyword": [
+            "dataQuality": false,
+            "description": "These data, collected to assist in the development of\r\nsentencing guidelines, describe offense and sentencing characteristics\r\nfor organizations sentenced in federal district courts in 2003. The\r\nUnited States Sentencing Commission's primary function is to inform\r\nfederal courts of sentencing policies and practices that include\r\nguidelines prescribing the appropriate form and severity of punishment\r\nfor offenders convicted of federal crimes. Court-related variables\r\ninclude primary offense type, pecuniary offense loss and gain, dates\r\nof disposition and sentencing, method of determination of guilt,\r\nnumber of counts pled and charged, and dates and types of sentencing\r\nand restitution. Defendant organization variables include ownership\r\nstructure, number of owners and employees, highest level of corporate\r\nknowledge of the criminal offense, highest level of corporate\r\nindictment and conviction for participation in the criminal offense,\r\nannual revenue, equity and financial status, whether it was a criminal\r\norganization, duration of criminal activity, and risk to national\r\nsecurity. Organizational defendants data, 2003, covers fiscal year\r\nOctober 1, 2002, through September 30, 2003.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR04631.v2",
+                    "title": "Organizations Convicted in Federal Criminal Courts, 2003"
+                }
+            ],
+            "identifier": "2190",
+            "isPartOf": "2427",
+            "issued": "2007-03-12T00:00:00",
+            "keyword": [
                 "convictions (law)",
                 "corporate crime",
                 "corporate sentencing",
@@ -49928,54 +49922,53 @@
                 "sentencing",
                 "sentencing guidelines"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2014-06-27T14:37:35",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2427",
-            "dataQuality": false,
-            "issued": "2007-03-12T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR04631.v2",
-                    "title": "Organizations Convicted in Federal Criminal Courts, 2003"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Mandatory Drug Offender Processing Data, 1987: New York",
-            "description": "The National Consortium for Assessing Drug Control\r\n Initiatives, funded by the Bureau of Justice Assistance and\r\n coordinated by the Criminal Justice Statistics Association, collected\r\n drug offender processing data from the state of New York. The purpose\r\n of the project was to track adult drug offenders from the point of\r\n entry into the criminal justice system (typically by arrest) through\r\n final court disposition, regardless of whether the offender was\r\n released without trial, acquitted, or convicted. These data allow\r\n researchers to examine how the criminal justice system processes drug\r\n offenders, to measure the changing volume of drug offenders moving\r\n through the different segments of the criminal justice system, to\r\n calculate processing time intervals between major decision-making\r\n events, and to assess the changing structure of the drug offender\r\n population. For purposes of this project, a drug offender was defined\r\n as any person who had been charged with a felony drug offense. The\r\n data are structured into six segments pertaining to (1) record\r\n identification, (2) the offender (date of birth, sex, race, and ethnic\r\n origin), (3) arrest information (date of arrest, age at arrest, arrest\r\n charge code), (4) prosecution information (filed offense code and\r\n level, prosecution disposition and date), (5) court disposition\r\n information (disposition offense and level, court disposition, final\r\n disposition date, final pleading, type of trial), and (6) sentencing\r\n information (sentence and sentence date, sentence minimum and\r\n maximum). Also included are elapsed time variables. The unit of\r\nanalysis is the felony drug offender.",
-            "modified": "1997-08-25T00:00:00",
-            "accessLevel": "public",
-            "identifier": "2191",
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
+            "title": "Organizations Convicted in Federal Criminal Courts, 2003"
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
+            "description": "The National Consortium for Assessing Drug Control\r\n Initiatives, funded by the Bureau of Justice Assistance and\r\n coordinated by the Criminal Justice Statistics Association, collected\r\n drug offender processing data from the state of New York. The purpose\r\n of the project was to track adult drug offenders from the point of\r\n entry into the criminal justice system (typically by arrest) through\r\n final court disposition, regardless of whether the offender was\r\n released without trial, acquitted, or convicted. These data allow\r\n researchers to examine how the criminal justice system processes drug\r\n offenders, to measure the changing volume of drug offenders moving\r\n through the different segments of the criminal justice system, to\r\n calculate processing time intervals between major decision-making\r\n events, and to assess the changing structure of the drug offender\r\n population. For purposes of this project, a drug offender was defined\r\n as any person who had been charged with a felony drug offense. The\r\n data are structured into six segments pertaining to (1) record\r\n identification, (2) the offender (date of birth, sex, race, and ethnic\r\n origin), (3) arrest information (date of arrest, age at arrest, arrest\r\n charge code), (4) prosecution information (filed offense code and\r\n level, prosecution disposition and date), (5) court disposition\r\n information (disposition offense and level, court disposition, final\r\n disposition date, final pleading, type of trial), and (6) sentencing\r\n information (sentence and sentence date, sentence minimum and\r\n maximum). Also included are elapsed time variables. The unit of\r\nanalysis is the felony drug offender.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR09565.v1",
+                    "title": "Mandatory Drug Offender Processing Data, 1987: New York"
+                }
+            ],
+            "identifier": "2191",
+            "issued": "1992-03-04T00:00:00",
             "keyword": [
                 "adults",
                 "arrests",
@@ -49986,53 +49979,54 @@
                 "prosecution",
                 "sentencing"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "1997-08-25T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "1992-03-04T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR09565.v1",
-                    "title": "Mandatory Drug Offender Processing Data, 1987: New York"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "United Nations World Crime Surveys:  First Survey, 1970-1975 and Second Survey, 1975-1980",
-            "description": "The United Nations began its World Crime Surveys in 1978. \r\n The first survey collected statistics on a small range of offenses and \r\n on the criminal justice process for the years 1970-1975. The second \r\n survey collected data on a wide range of offenses, offenders, and \r\n criminal justice process data for the years 1975-1980. Several factors \r\n make these two collections difficult to use in combination. Some 25 \r\n percent of those countries responding to the first survey did not \r\n respond to the second and, similarly, some 30 percent of those \r\n responding to the second survey did not respond to the first. In \r\n addition, many questions asked in the second survey were not asked in \r\n the first survey. This data collection represents the efforts of the \r\n investigators to combine, revise, and recheck the data of the first two \r\n surveys. The data are divided into two parts. Part 1 comprises all data \r\n on offenses and on some criminal justice personnel. Crime data are \r\n entered for 1970 through 1980. In most cases 1975 is entered twice, \r\n since both surveys collected data for this year. Part 2 includes data \r\n on offenders, prosecutions, convictions, and prisons. Data are entered \r\nfor 1970 through 1980, for every even year.",
-            "modified": "2006-01-12T00:00:00",
-            "accessLevel": "public",
-            "identifier": "2192",
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
+            "title": "Mandatory Drug Offender Processing Data, 1987: New York"
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
+            "description": "The United Nations began its World Crime Surveys in 1978. \r\n The first survey collected statistics on a small range of offenses and \r\n on the criminal justice process for the years 1970-1975. The second \r\n survey collected data on a wide range of offenses, offenders, and \r\n criminal justice process data for the years 1975-1980. Several factors \r\n make these two collections difficult to use in combination. Some 25 \r\n percent of those countries responding to the first survey did not \r\n respond to the second and, similarly, some 30 percent of those \r\n responding to the second survey did not respond to the first. In \r\n addition, many questions asked in the second survey were not asked in \r\n the first survey. This data collection represents the efforts of the \r\n investigators to combine, revise, and recheck the data of the first two \r\n surveys. The data are divided into two parts. Part 1 comprises all data \r\n on offenses and on some criminal justice personnel. Crime data are \r\n entered for 1970 through 1980. In most cases 1975 is entered twice, \r\n since both surveys collected data for this year. Part 2 includes data \r\n on offenders, prosecutions, convictions, and prisons. Data are entered \r\nfor 1970 through 1980, for every even year.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR09571.v1",
+                    "title": "United Nations World Crime Surveys:  First Survey, 1970-1975 and Second Survey, 1975-1980"
+                }
+            ],
+            "identifier": "2192",
+            "isPartOf": "2437",
+            "issued": "1991-10-23T00:00:00",
             "keyword": [
                 "United Nations",
                 "convictions (law)",
@@ -50050,54 +50044,54 @@
                 "persecution",
                 "trends"
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
-            "isPartOf": "2437",
-            "dataQuality": false,
-            "issued": "1991-10-23T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR09571.v1",
-                    "title": "United Nations World Crime Surveys:  First Survey, 1970-1975 and Second Survey, 1975-1980"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data [United States]:  Offenses Known and Clearances by Arrest in All Cities with Populations Over 250,000, 1989",
-            "description": "Since 1930, the Federal Bureau of Investigation has\r\n compiled the Uniform Crime Reports (UCR) to serve as periodic\r\n nationwide assessments of reported crime not available elsewhere in\r\n the criminal justice system. Each year, this information is reported\r\n in four types of files: (1) Offenses Known and Clearances by Arrest,\r\n (2) Property Stolen and Recovered, (3) Supplementary Homicide Reports\r\n (SHR), and (4) Police Employee (LEOKA) data. This collection contains\r\n Offenses Known and Clearances by Arrest data and includes monthly\r\n information on the number of Crime Index offenses reported, the number\r\n of offenses cleared by arrest or other means, and the number of adults\r\n and juveniles arrested in cities with populations over 250,000. The\r\n counts include all reports of Index Crimes (excluding arson) received\r\n from victims, from officers who discovered infractions, or from other\r\nsources.",
-            "modified": "2005-11-04T00:00:00",
-            "accessLevel": "public",
-            "identifier": "2193",
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
+            "title": "United Nations World Crime Surveys:  First Survey, 1970-1975 and Second Survey, 1975-1980"
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
+            "description": "Since 1930, the Federal Bureau of Investigation has\r\n compiled the Uniform Crime Reports (UCR) to serve as periodic\r\n nationwide assessments of reported crime not available elsewhere in\r\n the criminal justice system. Each year, this information is reported\r\n in four types of files: (1) Offenses Known and Clearances by Arrest,\r\n (2) Property Stolen and Recovered, (3) Supplementary Homicide Reports\r\n (SHR), and (4) Police Employee (LEOKA) data. This collection contains\r\n Offenses Known and Clearances by Arrest data and includes monthly\r\n information on the number of Crime Index offenses reported, the number\r\n of offenses cleared by arrest or other means, and the number of adults\r\n and juveniles arrested in cities with populations over 250,000. The\r\n counts include all reports of Index Crimes (excluding arson) received\r\n from victims, from officers who discovered infractions, or from other\r\nsources.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR09572.v1",
+                    "title": "Uniform Crime Reporting Program Data [United States]:  Offenses Known and Clearances by Arrest in All Cities with Populations Over 250,000, 1989"
+                }
+            ],
+            "identifier": "2193",
+            "isPartOf": "2167",
+            "issued": "1991-10-23T00:00:00",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrest records",
@@ -50108,54 +50102,54 @@
                 "law enforcement",
                 "offenses"
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
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "1991-10-23T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR09572.v1",
-                    "title": "Uniform Crime Reporting Program Data [United States]:  Offenses Known and Clearances by Arrest in All Cities with Populations Over 250,000, 1989"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data [United States]:  County-Level Detailed Arrest and Offense Data, 1989",
-            "description": "The files in this collection contain counts of arrests and\r\n offenses for Part 1 and Part 2 offenses: murder, rape, robbery,\r\n assault, burglary, larceny, auto theft, arson, forgery, fraud,\r\n embezzlement, vandalism, weapons violations, sex offenses, drug and\r\n alcohol abuse violations, gambling, vagrancy, curfew violations, and\r\nrunaways. County populations are also reported.",
-            "modified": "2006-01-12T00:00:00",
-            "accessLevel": "public",
-            "identifier": "2194",
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
+            "title": "Uniform Crime Reporting Program Data [United States]:  Offenses Known and Clearances by Arrest in All Cities with Populations Over 250,000, 1989"
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
+            "description": "The files in this collection contain counts of arrests and\r\n offenses for Part 1 and Part 2 offenses: murder, rape, robbery,\r\n assault, burglary, larceny, auto theft, arson, forgery, fraud,\r\n embezzlement, vandalism, weapons violations, sex offenses, drug and\r\n alcohol abuse violations, gambling, vagrancy, curfew violations, and\r\nrunaways. County populations are also reported.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR09573.v1",
+                    "title": "Uniform Crime Reporting Program Data [United States]:  County-Level Detailed Arrest and Offense Data, 1989"
+                }
+            ],
+            "identifier": "2194",
+            "isPartOf": "2167",
+            "issued": "1992-01-10T00:00:00",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -50179,54 +50173,54 @@
                 "sex offenses",
                 "vandalism"
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
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "1992-01-10T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR09573.v1",
-                    "title": "Uniform Crime Reporting Program Data [United States]:  County-Level Detailed Arrest and Offense Data, 1989"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reports [United States]:  Supplementary Homicide Reports, 1976-1998",
-            "description": "These data provide incident-level information on criminal\r\n homicides including location, circumstances, and method of offense, as\r\n well as demographic characteristics of victims and perpetrators and\r\n the relationship between the two. The data were provided monthly to\r\n the Federal Bureau of Investigation (FBI) by local law enforcement\r\nagencies participating in the FBI's Uniform Crime Reporting Program.",
-            "modified": "2006-03-30T00:00:00",
-            "accessLevel": "public",
-            "identifier": "2195",
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
+            "title": "Uniform Crime Reporting Program Data [United States]:  County-Level Detailed Arrest and Offense Data, 1989"
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
+            "description": "These data provide incident-level information on criminal\r\n homicides including location, circumstances, and method of offense, as\r\n well as demographic characteristics of victims and perpetrators and\r\n the relationship between the two. The data were provided monthly to\r\n the Federal Bureau of Investigation (FBI) by local law enforcement\r\nagencies participating in the FBI's Uniform Crime Reporting Program.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR03000.v1",
+                    "title": "Uniform Crime Reports [United States]:  Supplementary Homicide Reports, 1976-1998"
+                }
+            ],
+            "identifier": "2195",
+            "isPartOf": "2167",
+            "issued": "2000-09-11T00:00:00",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -50239,54 +50233,54 @@
                 "offenses",
                 "victims"
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
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2000-09-11T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR03000.v1",
-                    "title": "Uniform Crime Reports [United States]:  Supplementary Homicide Reports, 1976-1998"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Firearm Injury Surveillance Study, 1993-2000: [United States]",
-            "description": "These data were collected using the National Electronic\r\nInjury Surveillance System (NEISS), the primary data system of the\r\nUnited States Consumer Product Safety Commission (CPSC). CPSC began\r\noperating NEISS in 1972 to monitor product-related injuries treated in\r\nUnited States hospital emergency departments (EDs). In June 1992, the\r\nNational Center for Injury Prevention and Control (NCIPC), within the\r\nCenters for Disease Control and Prevention, established an interagency\r\nagreement with CPSC to begin collecting data on nonfatal\r\nfirearm-related injuries to monitor the incidence and characteristics\r\nof persons with nonfatal firearm-related injuries treated in United\r\nStates hospital EDs over time. This dataset represents all nonfatal\r\nfirearm-related injuries (i.e., injuries associated with\r\npowder-charged guns) and all nonfatal BB and pellet gun-related\r\ninjuries reported through NEISS from 1993 through 2000. The cases\r\nconsist of initial ED visits for treatment of the injuries. Cases were\r\nreported even if the patients subsequently died. Secondary visits and\r\ntransfers from other hospitals were excluded. Information is available\r\non injury diagnosis, firearm type, use of drugs or alcohol, criminal\r\nincident, and locale of the incident. Demographic information includes\r\nage, sex, and race of the injured person.",
-            "modified": "2005-11-04T00:00:00",
-            "accessLevel": "public",
-            "identifier": "2196",
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
+            "title": "Uniform Crime Reports [United States]:  Supplementary Homicide Reports, 1976-1998"
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
+            "description": "These data were collected using the National Electronic\r\nInjury Surveillance System (NEISS), the primary data system of the\r\nUnited States Consumer Product Safety Commission (CPSC). CPSC began\r\noperating NEISS in 1972 to monitor product-related injuries treated in\r\nUnited States hospital emergency departments (EDs). In June 1992, the\r\nNational Center for Injury Prevention and Control (NCIPC), within the\r\nCenters for Disease Control and Prevention, established an interagency\r\nagreement with CPSC to begin collecting data on nonfatal\r\nfirearm-related injuries to monitor the incidence and characteristics\r\nof persons with nonfatal firearm-related injuries treated in United\r\nStates hospital EDs over time. This dataset represents all nonfatal\r\nfirearm-related injuries (i.e., injuries associated with\r\npowder-charged guns) and all nonfatal BB and pellet gun-related\r\ninjuries reported through NEISS from 1993 through 2000. The cases\r\nconsist of initial ED visits for treatment of the injuries. Cases were\r\nreported even if the patients subsequently died. Secondary visits and\r\ntransfers from other hospitals were excluded. Information is available\r\non injury diagnosis, firearm type, use of drugs or alcohol, criminal\r\nincident, and locale of the incident. Demographic information includes\r\nage, sex, and race of the injured person.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR03018.v4",
+                    "title": "Firearm Injury Surveillance Study, 1993-2000: [United States]"
+                }
+            ],
+            "identifier": "2196",
+            "isPartOf": "2438",
+            "issued": "2000-09-11T00:00:00",
             "keyword": [
                 "accidents",
                 "firearms",
@@ -50297,54 +50291,53 @@
                 "public health",
                 "public safety"
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
-            "isPartOf": "2438",
-            "dataQuality": false,
-            "issued": "2000-09-11T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR03018.v4",
-                    "title": "Firearm Injury Surveillance Study, 1993-2000: [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Augmented Federal Probation, Sentencing, and Supervision Information System, 1985 ",
-            "description": "The United States Sentencing Commission, established by the \r\n 98th Congress, is an independent agency in the judicial branch of \r\n government. The Commission recommends guidelines prescribing the \r\n appropriate form and severity of punishment for offenders convicted of \r\n federal crimes. These data were collected to determine whether \r\n sentencing disparities existed and whether the guidelines were \r\n adequate. Basic information in the collection includes a description of \r\n the offense, characterization of the defendant's background and \r\n criminal record, method of disposition of the case, and sentence \r\n imposed. Felony and misdemeanor cases are included while petty offense \r\n cases are excluded. Three types of additional information were used to \r\n augment the existing data: (1) more detailed offense and offender \r\n characteristics identified by the United States Sentencing Commission \r\n but coded by federal probation officers, (2) actual time served in \r\n prison from the SENTRY data file of the United States Bureau of \r\n Prisons, and (3) information necessary to estimate prospective release \r\n dates from the hearing files of the United States Parole Commission. \r\nThe unit of analysis is the defendant.",
-            "modified": "2006-01-12T00:00:00",
-            "accessLevel": "public",
-            "identifier": "2197",
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
+            "title": "Firearm Injury Surveillance Study, 1993-2000: [United States]"
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
+            "description": "The United States Sentencing Commission, established by the \r\n 98th Congress, is an independent agency in the judicial branch of \r\n government. The Commission recommends guidelines prescribing the \r\n appropriate form and severity of punishment for offenders convicted of \r\n federal crimes. These data were collected to determine whether \r\n sentencing disparities existed and whether the guidelines were \r\n adequate. Basic information in the collection includes a description of \r\n the offense, characterization of the defendant's background and \r\n criminal record, method of disposition of the case, and sentence \r\n imposed. Felony and misdemeanor cases are included while petty offense \r\n cases are excluded. Three types of additional information were used to \r\n augment the existing data: (1) more detailed offense and offender \r\n characteristics identified by the United States Sentencing Commission \r\n but coded by federal probation officers, (2) actual time served in \r\n prison from the SENTRY data file of the United States Bureau of \r\n Prisons, and (3) information necessary to estimate prospective release \r\n dates from the hearing files of the United States Parole Commission. \r\nThe unit of analysis is the defendant.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR09664.v2",
+                    "title": "Augmented Federal Probation, Sentencing, and Supervision Information System, 1985 "
+                }
+            ],
+            "identifier": "2197",
+            "issued": "1992-01-10T00:00:00",
             "keyword": [
                 "criminal histories",
                 "disposition (legal)",
@@ -50356,53 +50349,53 @@
                 "sentencing",
                 "sentencing guidelines"
             ],
-            "bureauCode": [
-                "011:21"
-            ],
-            "programCode": [
-                "011:061"
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "1992-01-10T00:00:00",
             "language": [
                 "eng"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR09664.v2",
-                    "title": "Augmented Federal Probation, Sentencing, and Supervision Information System, 1985 "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Criminal Justice Outcomes of Male Offenders in 14 Jurisdictions in the United States, 1985-1988",
-            "description": "This data collection provides information on multiple \r\n prosecutions for individual offenders. The data are intended for use in \r\n the exploration and description of relationships among the various \r\n elements of the adjudication process (characteristics of the offender \r\n and offense and decisions made by various actors in the prosecution and \r\n sentencing of the offenders). The sampled incidents were drawn from two \r\n types of offenses: residential burglary and armed robbery. The \r\n collection includes only those incidents involving male offenders who \r\n were previously unknown to their victims and who were facing \r\n adjudication in adult court. The data collection instrument probed five \r\n areas for each offender and incident sampled: A. Related Incidents \r\n (information to identify all other incidents for which processing \r\n overlapped that of the sampled incident), B. Incident Description \r\n (information about the criminal incident itself, such as date and \r\n location of the incident, date of arrest, victims, weapons, \r\n accomplices, witnesses, and evidence), C. Adjudication Process \r\n (information such as bond amount, legal representation, adjudication \r\n events and outcomes, date of sentencing, and type and length of \r\n incarceration), D. Defendant (information about the defendant himself, \r\n including date of birth, race/descent, and employment status), and E. \r\n Prior Record (information about the defendant's record, such as his age \r\n at first arrest and first incarceration, the number of times he was \r\nincarcerated, and history of drug and/or alcohol abuse).",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "modified": "2006-01-12T00:00:00",
-            "accessLevel": "public",
-            "identifier": "2198",
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
+            "title": "Augmented Federal Probation, Sentencing, and Supervision Information System, 1985 "
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
+            "description": "This data collection provides information on multiple \r\n prosecutions for individual offenders. The data are intended for use in \r\n the exploration and description of relationships among the various \r\n elements of the adjudication process (characteristics of the offender \r\n and offense and decisions made by various actors in the prosecution and \r\n sentencing of the offenders). The sampled incidents were drawn from two \r\n types of offenses: residential burglary and armed robbery. The \r\n collection includes only those incidents involving male offenders who \r\n were previously unknown to their victims and who were facing \r\n adjudication in adult court. The data collection instrument probed five \r\n areas for each offender and incident sampled: A. Related Incidents \r\n (information to identify all other incidents for which processing \r\n overlapped that of the sampled incident), B. Incident Description \r\n (information about the criminal incident itself, such as date and \r\n location of the incident, date of arrest, victims, weapons, \r\n accomplices, witnesses, and evidence), C. Adjudication Process \r\n (information such as bond amount, legal representation, adjudication \r\n events and outcomes, date of sentencing, and type and length of \r\n incarceration), D. Defendant (information about the defendant himself, \r\n including date of birth, race/descent, and employment status), and E. \r\n Prior Record (information about the defendant's record, such as his age \r\n at first arrest and first incarceration, the number of times he was \r\nincarcerated, and history of drug and/or alcohol abuse).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR09671.v1",
+                    "title": "Criminal Justice Outcomes of Male Offenders in 14 Jurisdictions in the United States, 1985-1988"
+                }
+            ],
+            "identifier": "2198",
+            "issued": "1993-04-09T00:00:00",
             "keyword": [
                 "armed robbery",
                 "arrests",
@@ -50413,53 +50406,53 @@
                 "prosecution",
                 "sentencing"
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
-            "dataQuality": false,
-            "issued": "1993-04-09T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR09671.v1",
-                    "title": "Criminal Justice Outcomes of Male Offenders in 14 Jurisdictions in the United States, 1985-1988"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Survey of Judges and Court Practitioners, 1991  ",
-            "description": "The United States Sentencing Commission, established by the\r\n 98th Congress, is an independent agency in the judicial branch of\r\n government. The Commission's primary function is to institute\r\n guidelines that prescribe the appropriate form and severity of\r\n punishment for offenders convicted of federal crimes. This survey was\r\n developed in response to issues that arose during site visits\r\n conducted in conjunction with an implementation study of sentencing\r\n guidelines and was intended to supplement the information obtained in\r\n the more extensive site visit interviews. Topics include the impact of\r\n the plea agreement, departures by the court, mandatory minimum\r\n sentences, the general issue of unwarranted sentencing disparity, and\r\n whether this disparity had increased, decreased, or stayed about the\r\nsame since the sentencing guidelines were imposed in 1987.",
-            "modified": "2000-10-27T00:00:00",
-            "accessLevel": "public",
-            "identifier": "2199",
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
+            "title": "Criminal Justice Outcomes of Male Offenders in 14 Jurisdictions in the United States, 1985-1988"
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
+            "description": "The United States Sentencing Commission, established by the\r\n 98th Congress, is an independent agency in the judicial branch of\r\n government. The Commission's primary function is to institute\r\n guidelines that prescribe the appropriate form and severity of\r\n punishment for offenders convicted of federal crimes. This survey was\r\n developed in response to issues that arose during site visits\r\n conducted in conjunction with an implementation study of sentencing\r\n guidelines and was intended to supplement the information obtained in\r\n the more extensive site visit interviews. Topics include the impact of\r\n the plea agreement, departures by the court, mandatory minimum\r\n sentences, the general issue of unwarranted sentencing disparity, and\r\n whether this disparity had increased, decreased, or stayed about the\r\nsame since the sentencing guidelines were imposed in 1987.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR09837.v1",
+                    "title": "National Survey of Judges and Court Practitioners, 1991  "
+                }
+            ],
+            "identifier": "2199",
+            "issued": "1993-04-09T00:00:00",
             "keyword": [
                 "convictions (law)",
                 "courts",
@@ -50473,53 +50466,53 @@
                 "sentencing",
                 "sentencing guidelines"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2000-10-27T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "1993-04-09T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR09837.v1",
-                    "title": "National Survey of Judges and Court Practitioners, 1991  "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Prosecutorial Discretion and Plea Bargaining in Federal Criminal Courts in the United States, 1983-1990  ",
-            "description": "The primary purpose of this data collection was to study\r\n whether prosecutorial behavior was affected by the implementation of\r\n federal criminal sentencing guidelines in 1987. Monthly time series\r\n data were constructed on a number of prosecutorial outcomes,\r\n representing either discrete decision steps in the processing of\r\n criminal cases or the characteristics of cases that passed through the\r\n system. Variables include disposition year and month, number of matters\r\n initiated, number of cases filed, declined, and dismissed, number of\r\n convictions by trial, by jury, and by bench trial, number of guilty\r\n pleas, ratio of guilty pleas to cases resolved, and ratio of trials to\r\n cases resolved. The collection also provides a series of dichotomous\r\n variables to assess the impact of various events on prosecutorial\r\n outcomes over time. These events include the Anti-Drug Abuse Act of\r\n 1986 (effective November 1986), implementation of the sentencing\r\n guidelines (November 1987), Anti-Drug Abuse Act of 1988 (November\r\n 1988), United States Supreme Court's decision in the Minstretta case\r\n affirming the constitutionality of the sentencing guidelines (January\r\n 1989), and Attorney General Thornburgh's memo outlining Justice\r\nDepartment policy on charging and prosecution (March 1989).",
-            "modified": "2000-06-05T00:00:00",
-            "accessLevel": "public",
-            "identifier": "2200",
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
+            "title": "National Survey of Judges and Court Practitioners, 1991  "
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
+            "description": "The primary purpose of this data collection was to study\r\n whether prosecutorial behavior was affected by the implementation of\r\n federal criminal sentencing guidelines in 1987. Monthly time series\r\n data were constructed on a number of prosecutorial outcomes,\r\n representing either discrete decision steps in the processing of\r\n criminal cases or the characteristics of cases that passed through the\r\n system. Variables include disposition year and month, number of matters\r\n initiated, number of cases filed, declined, and dismissed, number of\r\n convictions by trial, by jury, and by bench trial, number of guilty\r\n pleas, ratio of guilty pleas to cases resolved, and ratio of trials to\r\n cases resolved. The collection also provides a series of dichotomous\r\n variables to assess the impact of various events on prosecutorial\r\n outcomes over time. These events include the Anti-Drug Abuse Act of\r\n 1986 (effective November 1986), implementation of the sentencing\r\n guidelines (November 1987), Anti-Drug Abuse Act of 1988 (November\r\n 1988), United States Supreme Court's decision in the Minstretta case\r\n affirming the constitutionality of the sentencing guidelines (January\r\n 1989), and Attorney General Thornburgh's memo outlining Justice\r\nDepartment policy on charging and prosecution (March 1989).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR09844.v1",
+                    "title": "Prosecutorial Discretion and Plea Bargaining in Federal Criminal Courts in the United States, 1983-1990  "
+                }
+            ],
+            "identifier": "2200",
+            "issued": "1993-04-09T00:00:00",
             "keyword": [
                 "case dismissal",
                 "case processing",
@@ -50533,53 +50526,53 @@
                 "prosecution",
                 "sentencing"
             ],
-            "bureauCode": [
-                "011:21"
-            ],
-            "programCode": [
-                "011:061"
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "1993-04-09T00:00:00",
             "language": [
                 "eng"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR09844.v1",
-                    "title": "Prosecutorial Discretion and Plea Bargaining in Federal Criminal Courts in the United States, 1983-1990  "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Impact of Sentencing Guidelines on the Use of Incarceration in Federal Criminal Courts in the United States, 1984-1990  ",
-            "description": "The primary purpose of this data collection was to examine\r\n the impact of the implementation of sentencing guidelines on the rate\r\n of incarcerative and nonincarcerative sentences imposed and on the\r\n average length of expected time to be served in incarceration for all\r\n offenses as well as for select groups of offenses. The measure of\r\n sentence length, \"expected time to be served,\" was used to allow for\r\n assumed good time and parole reductions. This term represents the\r\n amount of time an offender can expect to spend in prison at the time\r\n of sentencing, a roughly equivalent standard that can be measured\r\n before and after the implementation of federal criminal sentencing\r\n guidelines in 1987. Three broad offense categories were studied: drug\r\n offenses, robbery, and economic crimes. Drug offenses include a wide\r\n range of illegal activities involving marijuana, heroin, and\r\n cocaine. Robbery includes bank and postal robbery (both armed and\r\n unarmed) as well as other types of robbery offenses that appear less\r\n frequently in the federal system, such as carrying a firearm during\r\n the commission of a robbery. Economic offenses include fraud (bank,\r\n postal, and other), embezzlement (bank, postal, and other), and tax\r\n evasion. Other monthly data are provided on the number of prison and\r\nprobation sentences for all offenses and by offense categories.",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "modified": "2000-06-05T00:00:00",
-            "accessLevel": "public",
-            "identifier": "2201",
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
+            "title": "Prosecutorial Discretion and Plea Bargaining in Federal Criminal Courts in the United States, 1983-1990  "
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
+            "description": "The primary purpose of this data collection was to examine\r\n the impact of the implementation of sentencing guidelines on the rate\r\n of incarcerative and nonincarcerative sentences imposed and on the\r\n average length of expected time to be served in incarceration for all\r\n offenses as well as for select groups of offenses. The measure of\r\n sentence length, \"expected time to be served,\" was used to allow for\r\n assumed good time and parole reductions. This term represents the\r\n amount of time an offender can expect to spend in prison at the time\r\n of sentencing, a roughly equivalent standard that can be measured\r\n before and after the implementation of federal criminal sentencing\r\n guidelines in 1987. Three broad offense categories were studied: drug\r\n offenses, robbery, and economic crimes. Drug offenses include a wide\r\n range of illegal activities involving marijuana, heroin, and\r\n cocaine. Robbery includes bank and postal robbery (both armed and\r\n unarmed) as well as other types of robbery offenses that appear less\r\n frequently in the federal system, such as carrying a firearm during\r\n the commission of a robbery. Economic offenses include fraud (bank,\r\n postal, and other), embezzlement (bank, postal, and other), and tax\r\n evasion. Other monthly data are provided on the number of prison and\r\nprobation sentences for all offenses and by offense categories.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR09845.v1",
+                    "title": "Impact of Sentencing Guidelines on the Use of Incarceration in Federal Criminal Courts in the United States, 1984-1990  "
+                }
+            ],
+            "identifier": "2201",
+            "issued": "1993-04-09T00:00:00",
             "keyword": [
                 "courts",
                 "drug law offenses",
@@ -50592,53 +50585,54 @@
                 "sentencing guidelines",
                 "tax evasion"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2000-06-05T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "1993-04-09T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR09845.v1",
-                    "title": "Impact of Sentencing Guidelines on the Use of Incarceration in Federal Criminal Courts in the United States, 1984-1990  "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data [United States]: County-Level Detailed Arrest and Offense Data, 1990",
-            "description": "This data collection contains counts of arrests and offenses \r\n for Part I offenses (murder, rape, robbery, assault, burglary, larceny, \r\n auto theft, and arson) and Part II offenses (forgery, fraud, \r\n embezzlement, vandalism, weapons violations, sex offenses, drug and \r\n alcohol abuse violations, gambling, vagrancy, curfew violations, and \r\n runaways). Two sets of county populations are reported: one for total \r\n county population and the other for counties reporting six months or \r\nmore of data.",
-            "modified": "2006-01-12T00:00:00",
-            "accessLevel": "public",
-            "identifier": "2202",
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
+            "title": "Impact of Sentencing Guidelines on the Use of Incarceration in Federal Criminal Courts in the United States, 1984-1990  "
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
+            "description": "This data collection contains counts of arrests and offenses \r\n for Part I offenses (murder, rape, robbery, assault, burglary, larceny, \r\n auto theft, and arson) and Part II offenses (forgery, fraud, \r\n embezzlement, vandalism, weapons violations, sex offenses, drug and \r\n alcohol abuse violations, gambling, vagrancy, curfew violations, and \r\n runaways). Two sets of county populations are reported: one for total \r\n county population and the other for counties reporting six months or \r\nmore of data.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR09785.v1",
+                    "title": "Uniform Crime Reporting Program Data [United States]: County-Level Detailed Arrest and Offense Data, 1990"
+                }
+            ],
+            "identifier": "2202",
+            "isPartOf": "2167",
+            "issued": "1993-05-13T00:00:00",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -50662,108 +50656,108 @@
                 "sex offenses",
                 "vandalism"
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
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "1993-05-13T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR09785.v1",
-                    "title": "Uniform Crime Reporting Program Data [United States]: County-Level Detailed Arrest and Offense Data, 1990"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Offenders Released From Prison, 2006",
-            "description": "The data contain records of sentenced offenders released from the custody of the Bureau of Prisons (BOP) during fiscal year 2006. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. Records of offenders who exit federal prison temporarily, such as for transit to another location, to serve a weekend sentence, or for health care, are not included in the exiting cohort. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2014-03-10T21:54:29",
-            "accessLevel": "restricted public",
-            "identifier": "2203",
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
+            "title": "Uniform Crime Reporting Program Data [United States]: County-Level Detailed Arrest and Offense Data, 1990"
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
+            "description": "The data contain records of sentenced offenders released from the custody of the Bureau of Prisons (BOP) during fiscal year 2006. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. Records of offenders who exit federal prison temporarily, such as for transit to another location, to serve a weekend sentence, or for health care, are not included in the exiting cohort. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24219.v3",
+                    "title": "Federal Justice Statistics Program: Offenders Released From Prison, 2006"
+                }
+            ],
+            "identifier": "2203",
+            "isPartOf": "2174",
+            "issued": "2009-02-06T08:50:24",
             "keyword": [
                 "correctional system",
                 "offenders",
                 "prisons"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2014-03-10T21:54:29",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-06T08:50:24",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24219.v3",
-                    "title": "Federal Justice Statistics Program: Offenders Released From Prison, 2006"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reports [United States]: Supplementary Homicide Reports With Multiple Imputation, Cumulative Files 1976-2007",
-            "description": "These data provide incident-level information on criminal\r\nhomicides including location, circumstances, and method of offense, as\r\nwell as demographic characteristics of victims and perpetrators and\r\nthe relationship between the two. To adjust for unit missingness, a\r\nmultiple imputation approach and a weighting scheme were adopted,\r\nresulting in a fully-imputed SHR cumulative database of criminal\r\nhomicides for the years 1976-2007. Unlike other versions of the SHR\r\nfiles, these are limited to incidents of murder and non-negligent\r\nmanslaughter, excluding justifiable homicides, negligent manslaughter\r\nand homicides related to the September 11, 2001, terrorist attacks.",
-            "modified": "2009-02-24T09:16:15",
-            "accessLevel": "public",
-            "identifier": "2204",
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
+            "title": "Federal Justice Statistics Program: Offenders Released From Prison, 2006"
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
+            "description": "These data provide incident-level information on criminal\r\nhomicides including location, circumstances, and method of offense, as\r\nwell as demographic characteristics of victims and perpetrators and\r\nthe relationship between the two. To adjust for unit missingness, a\r\nmultiple imputation approach and a weighting scheme were adopted,\r\nresulting in a fully-imputed SHR cumulative database of criminal\r\nhomicides for the years 1976-2007. Unlike other versions of the SHR\r\nfiles, these are limited to incidents of murder and non-negligent\r\nmanslaughter, excluding justifiable homicides, negligent manslaughter\r\nand homicides related to the September 11, 2001, terrorist attacks.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24801.v1",
+                    "title": "Uniform Crime Reports [United States]: Supplementary Homicide Reports With Multiple Imputation, Cumulative Files 1976-2007"
+                }
+            ],
+            "identifier": "2204",
+            "isPartOf": "2167",
+            "issued": "2009-02-24T09:16:15",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -50776,54 +50770,54 @@
                 "offenses",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2009-02-24T09:16:15",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2009-02-24T09:16:15",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24801.v1",
-                    "title": "Uniform Crime Reports [United States]: Supplementary Homicide Reports With Multiple Imputation, Cumulative Files 1976-2007"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Court Cases: Integrated Data Base, 2008",
-            "description": "The purpose of this data collection is to provide an official public record of the business of the federal courts. The data originate from district and appellate court offices throughout the United States. Information was obtained at two points in the life of a case: filing and termination. The termination data contain information on both filing and terminations, while the pending data contain only filing information.",
-            "modified": "2015-08-24T12:09:56",
-            "accessLevel": "restricted public",
-            "identifier": "2205",
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
+            "title": "Uniform Crime Reports [United States]: Supplementary Homicide Reports With Multiple Imputation, Cumulative Files 1976-2007"
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
+            "description": "The purpose of this data collection is to provide an official public record of the business of the federal courts. The data originate from district and appellate court offices throughout the United States. Information was obtained at two points in the life of a case: filing and termination. The termination data contain information on both filing and terminations, while the pending data contain only filing information.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR25002.v6",
+                    "title": "Federal Court Cases: Integrated Data Base, 2008"
+                }
+            ],
+            "identifier": "2205",
+            "isPartOf": "2173",
+            "issued": "2009-04-03T11:07:26",
             "keyword": [
                 "administration",
                 "appellate courts",
@@ -50842,55 +50836,55 @@
                 "trial courts",
                 "trial procedures"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2015-08-24T12:09:56",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2173",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-04-03T11:07:26",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR25002.v6",
-                    "title": "Federal Court Cases: Integrated Data Base, 2008"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data [United States]: Offenses Known and Clearances by Arrest, 2007",
-            "description": "Since 1930, the Federal Bureau of Investigation has\r\ncompiled the Uniform Crime Reports (UCR) to serve as periodic\r\nnationwide assessments of reported crimes not available elsewhere in\r\nthe criminal justice system. Law enforcement agencies contribute\r\nreports either directly or through their state reporting programs.\r\nEach year, summary data are reported in four types of files: (1)\r\nOffenses Known and Clearances by Arrest, (2) Property Stolen and\r\nRecovered, (3) Supplementary Homicide Reports (SHR), and (4) Police\r\nEmployee (LEOKA) Data. The Offenses Known and Clearances by Arrest\r\ndata files include monthly data on the number of Crime Index offenses\r\nreported and the number of offenses cleared by arrest or other means.\r\nThe counts include all reports of Index crimes (excluding arson)\r\nreceived from victims, officers who discovered infractions, or other\r\nsources.",
-            "modified": "2009-08-21T10:39:29",
-            "accessLevel": "public",
-            "identifier": "2206",
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
+            "title": "Federal Court Cases: Integrated Data Base, 2008"
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
+            "description": "Since 1930, the Federal Bureau of Investigation has\r\ncompiled the Uniform Crime Reports (UCR) to serve as periodic\r\nnationwide assessments of reported crimes not available elsewhere in\r\nthe criminal justice system. Law enforcement agencies contribute\r\nreports either directly or through their state reporting programs.\r\nEach year, summary data are reported in four types of files: (1)\r\nOffenses Known and Clearances by Arrest, (2) Property Stolen and\r\nRecovered, (3) Supplementary Homicide Reports (SHR), and (4) Police\r\nEmployee (LEOKA) Data. The Offenses Known and Clearances by Arrest\r\ndata files include monthly data on the number of Crime Index offenses\r\nreported and the number of offenses cleared by arrest or other means.\r\nThe counts include all reports of Index crimes (excluding arson)\r\nreceived from victims, officers who discovered infractions, or other\r\nsources.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR25101.v2",
+                    "title": "Uniform Crime Reporting Program Data [United States]: Offenses Known and Clearances by Arrest, 2007"
+                }
+            ],
+            "identifier": "2206",
+            "isPartOf": "2167",
+            "issued": "2009-05-29T08:55:53",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -50900,54 +50894,54 @@
                 "law enforcement",
                 "offenses"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2009-08-21T10:39:29",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2009-05-29T08:55:53",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR25101.v2",
-                    "title": "Uniform Crime Reporting Program Data [United States]: Offenses Known and Clearances by Arrest, 2007"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data [United States]: Property Stolen and Recovered, 2007",
-            "description": "Since 1930, the Federal Bureau of Investigation has compiled the Uniform Crime Reports (UCR) to serve as periodic nationwide assessments of reported crimes not available elsewhere in the criminal justice system. Law enforcement agencies contribute reports either directly or through their state reporting programs. Each year, this information is reported in four types of files: (1) Offenses Known and Clearances by Arrest, (2) Property Stolen and Recovered, (3) Supplementary Homicide Reports (SHR), and (4) Police Employee (LEOKA) Data. The Property Stolen and Recovered data are collected on a monthly basis by all UCR contributing agencies. These data, aggregated at the agency level, report on the nature of the crime, the monetary value of the property stolen, and the type of property stolen. Similar information regarding recovered property is also included in the data.",
-            "modified": "2016-02-29T10:36:22",
-            "accessLevel": "public",
-            "identifier": "2207",
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
+            "title": "Uniform Crime Reporting Program Data [United States]: Offenses Known and Clearances by Arrest, 2007"
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
+            "description": "Since 1930, the Federal Bureau of Investigation has compiled the Uniform Crime Reports (UCR) to serve as periodic nationwide assessments of reported crimes not available elsewhere in the criminal justice system. Law enforcement agencies contribute reports either directly or through their state reporting programs. Each year, this information is reported in four types of files: (1) Offenses Known and Clearances by Arrest, (2) Property Stolen and Recovered, (3) Supplementary Homicide Reports (SHR), and (4) Police Employee (LEOKA) Data. The Property Stolen and Recovered data are collected on a monthly basis by all UCR contributing agencies. These data, aggregated at the agency level, report on the nature of the crime, the monetary value of the property stolen, and the type of property stolen. Similar information regarding recovered property is also included in the data.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR25102.v1",
+                    "title": "Uniform Crime Reporting Program Data [United States]: Property Stolen and Recovered, 2007"
+                }
+            ],
+            "identifier": "2207",
+            "isPartOf": "2167",
+            "issued": "2016-02-29T10:36:22",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -50962,54 +50956,54 @@
                 "stolen property",
                 "stolen property recovery"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2016-02-29T10:36:22",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2016-02-29T10:36:22",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR25102.v1",
-                    "title": "Uniform Crime Reporting Program Data [United States]: Property Stolen and Recovered, 2007"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data [United States]: Supplementary Homicide Reports, 2007",
-            "description": "Since 1930, the Federal Bureau of Investigation has compiled the Uniform Crime Reports (UCR) to serve as a periodic nationwide assessment of reported crimes not available elsewhere in the criminal justice system. Each year, this information is reported in four types of files: (1) Offenses Known and Clearances by Arrest, (2) Property Stolen and Recovered, (3) Supplementary Homicide Reports (SHR), and (4) Police Employee (LEOKA) Data. The Supplementary Homicide Reports provide incident-based information on criminal homicides reported to the police. These homicides consist of murders, non-negligent manslaughter, and justifiable homicides. The data, provided monthly by UCR agencies, contain information describing the victim of the homicide, the offender, and the relationship between victim and offender.",
-            "modified": "2009-06-10T08:52:15",
-            "accessLevel": "public",
-            "identifier": "2208",
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
+            "title": "Uniform Crime Reporting Program Data [United States]: Property Stolen and Recovered, 2007"
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
+            "description": "Since 1930, the Federal Bureau of Investigation has compiled the Uniform Crime Reports (UCR) to serve as a periodic nationwide assessment of reported crimes not available elsewhere in the criminal justice system. Each year, this information is reported in four types of files: (1) Offenses Known and Clearances by Arrest, (2) Property Stolen and Recovered, (3) Supplementary Homicide Reports (SHR), and (4) Police Employee (LEOKA) Data. The Supplementary Homicide Reports provide incident-based information on criminal homicides reported to the police. These homicides consist of murders, non-negligent manslaughter, and justifiable homicides. The data, provided monthly by UCR agencies, contain information describing the victim of the homicide, the offender, and the relationship between victim and offender.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR25103.v1",
+                    "title": "Uniform Crime Reporting Program Data [United States]: Supplementary Homicide Reports, 2007"
+                }
+            ],
+            "identifier": "2208",
+            "isPartOf": "2167",
+            "issued": "2009-06-10T08:52:15",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -51023,59 +51017,59 @@
                 "offenses",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2009-06-10T08:52:15",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2009-06-10T08:52:15",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR25103.v1",
-                    "title": "Uniform Crime Reporting Program Data [United States]: Supplementary Homicide Reports, 2007"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data [United States]: Police Employee (LEOKA) Data, 2007",
-            "description": "Since 1930, the Federal Bureau of Investigation has compiled the Uniform Crime Reports (UCR) to serve as a periodic nationwide assessment of reported crimes not available elsewhere in the criminal justice system. Each year, this information is reported in four types of files: (1) Offenses Known and Clearances by Arrest, (2) Property Stolen and Recovered, (3) Supplementary Homicide Reports (SHR), and (4) Police Employee (LEOKA) Data. The Police Employee (LEOKA) Data provide information about law enforcement officers killed or assaulted (hence the acronym, LEOKA) in the line of duty. The variables created from the LEOKA forms provide in-depth information on the circumstances surrounding killings or assaults, including type of call answered, type of weapon used, and type of patrol the officers were on.",
-            "modified": "2009-04-14T10:02:09",
-            "accessLevel": "public",
-            "identifier": "2209",
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
+            "title": "Uniform Crime Reporting Program Data [United States]: Supplementary Homicide Reports, 2007"
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
-            "keyword": [
-                "Uniform Crime Reports",
-                "arrests",
-                "assaults on police",
-                "crime rates",
+            "dataQuality": false,
+            "description": "Since 1930, the Federal Bureau of Investigation has compiled the Uniform Crime Reports (UCR) to serve as a periodic nationwide assessment of reported crimes not available elsewhere in the criminal justice system. Each year, this information is reported in four types of files: (1) Offenses Known and Clearances by Arrest, (2) Property Stolen and Recovered, (3) Supplementary Homicide Reports (SHR), and (4) Police Employee (LEOKA) Data. The Police Employee (LEOKA) Data provide information about law enforcement officers killed or assaulted (hence the acronym, LEOKA) in the line of duty. The variables created from the LEOKA forms provide in-depth information on the circumstances surrounding killings or assaults, including type of call answered, type of weapon used, and type of patrol the officers were on.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR25104.v1",
+                    "title": "Uniform Crime Reporting Program Data [United States]: Police Employee (LEOKA) Data, 2007"
+                }
+            ],
+            "identifier": "2209",
+            "isPartOf": "2167",
+            "issued": "2009-04-14T10:02:09",
+            "keyword": [
+                "Uniform Crime Reports",
+                "arrests",
+                "assaults on police",
+                "crime rates",
                 "crime reporting",
                 "crime statistics",
                 "law enforcement",
@@ -51083,54 +51077,54 @@
                 "police deaths",
                 "police officers"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2009-04-14T10:02:09",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2009-04-14T10:02:09",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR25104.v1",
-                    "title": "Uniform Crime Reporting Program Data [United States]: Police Employee (LEOKA) Data, 2007"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, Summarized Yearly, 2007",
-            "description": "These data provide information on the number of arrests\r\nreported to the Federal Bureau of Investigation's Uniform Crime\r\nReporting (UCR) Program each year by police agencies in the United\r\nStates. These arrest reports provide data on 43 offenses including\r\nviolent crime, drug use, gambling, and larceny. The data received by\r\nICPSR were structured as a hierarchical file containing, per reporting\r\npolice agency: an agency header record, and 1 to 43 detail offense\r\nrecords containing the counts of arrests by age, sex, and race for a\r\nparticular offense. ICPSR restructured the original data to logical\r\nrecord length format with the agency header record variables copied\r\nonto the detail records. Consequently, each record contains arrest\r\ncounts for a particular agency-offense.",
-            "modified": "2009-09-28T19:25:41",
-            "accessLevel": "public",
-            "identifier": "2210",
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
+            "title": "Uniform Crime Reporting Program Data [United States]: Police Employee (LEOKA) Data, 2007"
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
+            "description": "These data provide information on the number of arrests\r\nreported to the Federal Bureau of Investigation's Uniform Crime\r\nReporting (UCR) Program each year by police agencies in the United\r\nStates. These arrest reports provide data on 43 offenses including\r\nviolent crime, drug use, gambling, and larceny. The data received by\r\nICPSR were structured as a hierarchical file containing, per reporting\r\npolice agency: an agency header record, and 1 to 43 detail offense\r\nrecords containing the counts of arrests by age, sex, and race for a\r\nparticular offense. ICPSR restructured the original data to logical\r\nrecord length format with the agency header record variables copied\r\nonto the detail records. Consequently, each record contains arrest\r\ncounts for a particular agency-offense.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR25106.v1",
+                    "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, Summarized Yearly, 2007"
+                }
+            ],
+            "identifier": "2210",
+            "isPartOf": "2167",
+            "issued": "2009-09-28T19:25:41",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrest records",
@@ -51146,54 +51140,54 @@
                 "offenses",
                 "violent crime"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2009-09-28T19:25:41",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2009-09-28T19:25:41",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR25106.v1",
-                    "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, Summarized Yearly, 2007"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data [United States]: Hate Crime Data, 2007 [Record-Type Files]",
-            "description": "In response to a growing concern about hate crimes, the\r\nUnited States Congress enacted the Hate Crime Statistics Act of\r\n1990. The Act requires the attorney general to establish guidelines\r\nand collect, as part of the Uniform Crime Reporting (UCR) Program,\r\ndata \"about crimes that manifest evidence of prejudice based on race,\r\nreligion, sexual orientation, or ethnicity, including where\r\nappropriate the crimes of murder and non-negligent manslaughter,\r\nforcible rape, aggravated assault, simple assault, intimidation,\r\narson, and destruction, damage or vandalism of property.\" Hate crime\r\ndata collection was required by the Act to begin in calendar year 1990\r\nand to continue for four successive years. In September 1994, the\r\nViolent Crime Control and Law Enforcement Act amended the Hate Crime\r\nStatistics Act to add disabilities, both physical and mental, as\r\nfactors that could be considered a basis for hate crimes. Although the\r\nAct originally mandated data collection for five years, the Church\r\nArson Prevention Act of 1996 amended the collection duration \"for each\r\ncalendar year,\" making hate crime statistics a permanent addition to\r\nthe UCR program. As with the other UCR data, law enforcement agencies\r\ncontribute reports either directly or through their state reporting\r\nprograms. Information contained in the data includes number of victims\r\nand offenders involved in each hate crime incident, type of victims,\r\nbias motivation, offense type, and location type.",
-            "modified": "2009-06-10T08:44:44",
-            "accessLevel": "public",
-            "identifier": "2211",
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
+            "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, Summarized Yearly, 2007"
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
+            "description": "In response to a growing concern about hate crimes, the\r\nUnited States Congress enacted the Hate Crime Statistics Act of\r\n1990. The Act requires the attorney general to establish guidelines\r\nand collect, as part of the Uniform Crime Reporting (UCR) Program,\r\ndata \"about crimes that manifest evidence of prejudice based on race,\r\nreligion, sexual orientation, or ethnicity, including where\r\nappropriate the crimes of murder and non-negligent manslaughter,\r\nforcible rape, aggravated assault, simple assault, intimidation,\r\narson, and destruction, damage or vandalism of property.\" Hate crime\r\ndata collection was required by the Act to begin in calendar year 1990\r\nand to continue for four successive years. In September 1994, the\r\nViolent Crime Control and Law Enforcement Act amended the Hate Crime\r\nStatistics Act to add disabilities, both physical and mental, as\r\nfactors that could be considered a basis for hate crimes. Although the\r\nAct originally mandated data collection for five years, the Church\r\nArson Prevention Act of 1996 amended the collection duration \"for each\r\ncalendar year,\" making hate crime statistics a permanent addition to\r\nthe UCR program. As with the other UCR data, law enforcement agencies\r\ncontribute reports either directly or through their state reporting\r\nprograms. Information contained in the data includes number of victims\r\nand offenders involved in each hate crime incident, type of victims,\r\nbias motivation, offense type, and location type.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR25107.v1",
+                    "title": "Uniform Crime Reporting Program Data [United States]: Hate Crime Data, 2007 [Record-Type Files]"
+                }
+            ],
+            "identifier": "2211",
+            "isPartOf": "2167",
+            "issued": "2009-06-10T08:44:44",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -51212,54 +51206,54 @@
                 "religion",
                 "violence"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2009-06-10T08:44:44",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2009-06-10T08:44:44",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR25107.v1",
-                    "title": "Uniform Crime Reporting Program Data [United States]: Hate Crime Data, 2007 [Record-Type Files]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, 2007",
-            "description": "These data provide information on the number of arrests\r\nreported to the Federal Bureau of Investigation's Uniform Crime\r\nReporting (UCR) Program each year by police agencies in the United\r\nStates. These arrest reports provide data on 43 offenses including\r\nviolent crime, drug use, gambling, and larceny. The data received by\r\nICPSR were structured as a hierarchical file containing (per reporting\r\npolice agency) an agency header record, 1 to 12 monthly header\r\nrecords, and 1 to 43 detail offense records containing the counts of\r\narrests by age, sex, and race for a particular offense. ICPSR\r\nrestructured the original data to a rectangular format.",
-            "modified": "2009-06-10T08:36:10",
-            "accessLevel": "public",
-            "identifier": "2212",
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
+            "title": "Uniform Crime Reporting Program Data [United States]: Hate Crime Data, 2007 [Record-Type Files]"
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
+            "description": "These data provide information on the number of arrests\r\nreported to the Federal Bureau of Investigation's Uniform Crime\r\nReporting (UCR) Program each year by police agencies in the United\r\nStates. These arrest reports provide data on 43 offenses including\r\nviolent crime, drug use, gambling, and larceny. The data received by\r\nICPSR were structured as a hierarchical file containing (per reporting\r\npolice agency) an agency header record, 1 to 12 monthly header\r\nrecords, and 1 to 43 detail offense records containing the counts of\r\narrests by age, sex, and race for a particular offense. ICPSR\r\nrestructured the original data to a rectangular format.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR25108.v1",
+                    "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, 2007"
+                }
+            ],
+            "identifier": "2212",
+            "isPartOf": "2167",
+            "issued": "2009-06-10T08:36:10",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -51284,54 +51278,54 @@
                 "vandalism",
                 "weapons"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2009-06-10T08:36:10",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2009-06-10T08:36:10",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR25108.v1",
-                    "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, 2007"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Incident-Based Reporting System, 1991",
-            "description": "The National Incident-Based Reporting System (NIBRS) is a\r\npart of the Uniform Crime Reporting Program (UCR), administered by the\r\nFederal Bureau of Investigation (FBI). In the late 1970s, the law\r\nenforcement community called for a thorough evaluative study of the\r\nUCR with the objective of recommending an expanded and enhanced UCR\r\nprogram to meet law enforcement needs into the 21st century. The FBI\r\nfully concurred with the need for an updated program to meet\r\ncontemporary needs and provided its support, formulating a\r\ncomprehensive redesign effort. Following a multiyear study, a\r\n\"Blueprint for the Future of the Uniform Crime Reporting Program\" was\r\ndeveloped. Using the \"Blueprint\" and in consultation with local and\r\nstate law enforcement executives, the FBI formulated new guidelines\r\nfor the Uniform Crime Reports. The National Incident-Based Reporting\r\nSystem (NIBRS) is being implemented to meet these guidelines. NIBRS\r\ndata are archived at ICPSR as 13 separate data files, which may be\r\nmerged by using linkage variables. The data focus on a variety of\r\naspects of a crime incident. Part 4, Administrative Segment, offers\r\ndata on the incident itself (date and time). Each crime incident is\r\ndelineated by one administrative segment record. Also provided are\r\nPart 5, Offense Segment (offense type, location, weapon use, and bias\r\nmotivation), Part 6, Property Segment (type of property loss, property\r\ndescription, property value, drug type and quantity), Part 7, Victim\r\nSegment (age, sex, race, ethnicity, and injuries), Part 8, Offender\r\nSegment (age, sex, and race), and Part 9, Arrestee Segment (arrest\r\ndate, age, sex, race, and weapon use). The Batch Header Segment (Parts\r\n1-3) separates and identifies individual police agencies by\r\nOriginating Agency Identifier (ORI). Batch Header information, which\r\nis contained on three records for each ORI, includes agency name,\r\ngeographic location, and population of the area. Part 10, Group B\r\nArrest Report Segment, includes arrestee data for Group B\r\ncrimes. Window Segments files (Parts 11-13) pertain to incidents for\r\nwhich the complete Group A Incident Report was not submitted to the\r\nFBI. In general, a Window Segment record will be generated if the\r\nincident occurred prior to January 1 of the previous year or if the\r\nincident occurred prior to when the agency started NIBRS reporting. As\r\nwith UCR, participation in NIBRS is voluntary on the part of law\r\nenforcement agencies. The data are not a representative sample of\r\ncrime in the United States. For 1991, four states, fully or partially\r\nparticipating in NIBRS, were included in the dataset.",
-            "modified": "2009-07-27T08:42:22",
-            "accessLevel": "public",
-            "identifier": "2213",
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
+            "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, 2007"
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
+            "description": "The National Incident-Based Reporting System (NIBRS) is a\r\npart of the Uniform Crime Reporting Program (UCR), administered by the\r\nFederal Bureau of Investigation (FBI). In the late 1970s, the law\r\nenforcement community called for a thorough evaluative study of the\r\nUCR with the objective of recommending an expanded and enhanced UCR\r\nprogram to meet law enforcement needs into the 21st century. The FBI\r\nfully concurred with the need for an updated program to meet\r\ncontemporary needs and provided its support, formulating a\r\ncomprehensive redesign effort. Following a multiyear study, a\r\n\"Blueprint for the Future of the Uniform Crime Reporting Program\" was\r\ndeveloped. Using the \"Blueprint\" and in consultation with local and\r\nstate law enforcement executives, the FBI formulated new guidelines\r\nfor the Uniform Crime Reports. The National Incident-Based Reporting\r\nSystem (NIBRS) is being implemented to meet these guidelines. NIBRS\r\ndata are archived at ICPSR as 13 separate data files, which may be\r\nmerged by using linkage variables. The data focus on a variety of\r\naspects of a crime incident. Part 4, Administrative Segment, offers\r\ndata on the incident itself (date and time). Each crime incident is\r\ndelineated by one administrative segment record. Also provided are\r\nPart 5, Offense Segment (offense type, location, weapon use, and bias\r\nmotivation), Part 6, Property Segment (type of property loss, property\r\ndescription, property value, drug type and quantity), Part 7, Victim\r\nSegment (age, sex, race, ethnicity, and injuries), Part 8, Offender\r\nSegment (age, sex, and race), and Part 9, Arrestee Segment (arrest\r\ndate, age, sex, race, and weapon use). The Batch Header Segment (Parts\r\n1-3) separates and identifies individual police agencies by\r\nOriginating Agency Identifier (ORI). Batch Header information, which\r\nis contained on three records for each ORI, includes agency name,\r\ngeographic location, and population of the area. Part 10, Group B\r\nArrest Report Segment, includes arrestee data for Group B\r\ncrimes. Window Segments files (Parts 11-13) pertain to incidents for\r\nwhich the complete Group A Incident Report was not submitted to the\r\nFBI. In general, a Window Segment record will be generated if the\r\nincident occurred prior to January 1 of the previous year or if the\r\nincident occurred prior to when the agency started NIBRS reporting. As\r\nwith UCR, participation in NIBRS is voluntary on the part of law\r\nenforcement agencies. The data are not a representative sample of\r\ncrime in the United States. For 1991, four states, fully or partially\r\nparticipating in NIBRS, were included in the dataset.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR25109.v1",
+                    "title": "National Incident-Based Reporting System, 1991"
+                }
+            ],
+            "identifier": "2213",
+            "isPartOf": "2433",
+            "issued": "2009-07-27T08:42:22",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -51346,54 +51340,54 @@
                 "victims",
                 "violent crime"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2009-07-27T08:42:22",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2433",
-            "dataQuality": false,
-            "issued": "2009-07-27T08:42:22",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR25109.v1",
-                    "title": "National Incident-Based Reporting System, 1991"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Incident-Based Reporting System, 1992",
-            "description": "The National Incident-Based Reporting System (NIBRS) is a\r\npart of the Uniform Crime Reporting Program (UCR), administered by the\r\nFederal Bureau of Investigation (FBI). In the late 1970s, the law\r\nenforcement community called for a thorough evaluative study of the\r\nUCR with the objective of recommending an expanded and enhanced UCR\r\nprogram to meet law enforcement needs into the 21st century. The FBI\r\nfully concurred with the need for an updated program to meet\r\ncontemporary needs and provided its support, formulating a\r\ncomprehensive redesign effort. Following a multiyear study, a\r\n\"Blueprint for the Future of the Uniform Crime Reporting Program\" was\r\ndeveloped. Using the \"Blueprint\" and in consultation with local and\r\nstate law enforcement executives, the FBI formulated new guidelines\r\nfor the Uniform Crime Reports. The National Incident-Based Reporting\r\nSystem (NIBRS) is being implemented to meet these guidelines. NIBRS\r\ndata are archived at ICPSR as 13 separate data files, which may be\r\nmerged by using linkage variables. The data focus on a variety of\r\naspects of a crime incident. Part 4, Administrative Segment, offers\r\ndata on the incident itself (date and time). Each crime incident is\r\ndelineated by one administrative segment record. Also provided are\r\nPart 5, Offense Segment (offense type, location, weapon use, and bias\r\nmotivation), Part 6, Property Segment (type of property loss, property\r\ndescription, property value, drug type and quantity), Part 7, Victim\r\nSegment (age, sex, race, ethnicity, and injuries), Part 8, Offender\r\nSegment (age, sex, and race), and Part 9, Arrestee Segment (arrest\r\ndate, age, sex, race, and weapon use). The Batch Header Segment (Parts\r\n1-3) separates and identifies individual police agencies by\r\nOriginating Agency Identifier (ORI). Batch Header information, which\r\nis contained on three records for each ORI, includes agency name,\r\ngeographic location, and population of the area. Part 10, Group B\r\nArrest Report Segment, includes arrestee data for Group B\r\ncrimes. Window Segments files (Parts 11-13) pertain to incidents for\r\nwhich the complete Group A Incident Report was not submitted to the\r\nFBI. In general, a Window Segment record will be generated if the\r\nincident occurred prior to January 1 of the previous year or if the\r\nincident occurred prior to when the agency started NIBRS reporting. As\r\nwith UCR, participation in NIBRS is voluntary on the part of law\r\nenforcement agencies. The data are not a representative sample of\r\ncrime in the United States. For 1992, six states, fully or partially\r\nparticipating in NIBRS, were included in the dataset.",
-            "modified": "2009-07-27T09:01:33",
-            "accessLevel": "public",
-            "identifier": "2214",
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
+            "title": "National Incident-Based Reporting System, 1991"
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
+            "description": "The National Incident-Based Reporting System (NIBRS) is a\r\npart of the Uniform Crime Reporting Program (UCR), administered by the\r\nFederal Bureau of Investigation (FBI). In the late 1970s, the law\r\nenforcement community called for a thorough evaluative study of the\r\nUCR with the objective of recommending an expanded and enhanced UCR\r\nprogram to meet law enforcement needs into the 21st century. The FBI\r\nfully concurred with the need for an updated program to meet\r\ncontemporary needs and provided its support, formulating a\r\ncomprehensive redesign effort. Following a multiyear study, a\r\n\"Blueprint for the Future of the Uniform Crime Reporting Program\" was\r\ndeveloped. Using the \"Blueprint\" and in consultation with local and\r\nstate law enforcement executives, the FBI formulated new guidelines\r\nfor the Uniform Crime Reports. The National Incident-Based Reporting\r\nSystem (NIBRS) is being implemented to meet these guidelines. NIBRS\r\ndata are archived at ICPSR as 13 separate data files, which may be\r\nmerged by using linkage variables. The data focus on a variety of\r\naspects of a crime incident. Part 4, Administrative Segment, offers\r\ndata on the incident itself (date and time). Each crime incident is\r\ndelineated by one administrative segment record. Also provided are\r\nPart 5, Offense Segment (offense type, location, weapon use, and bias\r\nmotivation), Part 6, Property Segment (type of property loss, property\r\ndescription, property value, drug type and quantity), Part 7, Victim\r\nSegment (age, sex, race, ethnicity, and injuries), Part 8, Offender\r\nSegment (age, sex, and race), and Part 9, Arrestee Segment (arrest\r\ndate, age, sex, race, and weapon use). The Batch Header Segment (Parts\r\n1-3) separates and identifies individual police agencies by\r\nOriginating Agency Identifier (ORI). Batch Header information, which\r\nis contained on three records for each ORI, includes agency name,\r\ngeographic location, and population of the area. Part 10, Group B\r\nArrest Report Segment, includes arrestee data for Group B\r\ncrimes. Window Segments files (Parts 11-13) pertain to incidents for\r\nwhich the complete Group A Incident Report was not submitted to the\r\nFBI. In general, a Window Segment record will be generated if the\r\nincident occurred prior to January 1 of the previous year or if the\r\nincident occurred prior to when the agency started NIBRS reporting. As\r\nwith UCR, participation in NIBRS is voluntary on the part of law\r\nenforcement agencies. The data are not a representative sample of\r\ncrime in the United States. For 1992, six states, fully or partially\r\nparticipating in NIBRS, were included in the dataset.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR25110.v1",
+                    "title": "National Incident-Based Reporting System, 1992"
+                }
+            ],
+            "identifier": "2214",
+            "isPartOf": "2433",
+            "issued": "2009-07-27T09:01:33",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -51408,54 +51402,54 @@
                 "victims",
                 "violent crime"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2009-07-27T09:01:33",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2433",
-            "dataQuality": false,
-            "issued": "2009-07-27T09:01:33",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR25110.v1",
-                    "title": "National Incident-Based Reporting System, 1992"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Police-Public Contact Survey, 2011",
-            "description": "\r\nThe Police-Public Contact Survey (PPCS) provides detailed information on the nature and\r\ncharacteristics of face-to-face contacts between police and the public, including the\r\nreason for and outcome of the contact. The PPCS interviews a nationally representative\r\nsample of U.S. residents age 16 or older as a supplement to the National Crime\r\nVictimization Survey. To date, the PPCS has been conducted six times by BJS:\r\nThe first survey - described in the BJS publication Police Use of Force: Collection of National Data\r\n(NCJ 165040) - documented levels of contacts with police during 1996.\r\nThe second survey - described in Contacts between Police and the Public: Findings from the\r\n1999 National Survey (NCJ 184957) - recorded police-citizen contacts in 1999. These data are\r\narchived as POLICE-PUBLIC CONTACT SURVEY, 1999: [UNITED STATES] (ICPSR 3151).\r\nThe third survey - described in Contacts between Police and the Public: Findings from the\r\n2002 National Survey (NCJ 207845) - covered interactions between police and the public in\r\n2002. These data are archived as POLICE-PUBLIC CONTACT SURVEY, 2002: [UNITED STATES]\r\n(ICPSR 4273). \r\nThe fourth survey - described in the BJS publication Contacts between\r\nPolice and the Public, 2005 (NCJ 215243) - covered interactions between police and the\r\npublic in 2005. These data are archived as POLICE-PUBLIC CONTACT SURVEY, 2005: [UNITED\r\nSTATES] (ICPSR 020020).\r\nThe fifth survey - described in the BJS publication Contacts between Police and the\r\nPublic, 2008 (NCJ 234599) - covered interactions between police and the public in\r\n2008. These data are archived as POLICE-PUBLIC CONTACT SURVEY, 2008 (ICPSR 32022).\r\nThe sixth survey (split sample design due to instrument changes) - new instrument findings described in\r\ntwo publications: Police Behavior During Traffic and Street Stops, 2011 (NCJ 242937) and Requests for Police Assistance, 2011 (NCJ 242938) - covered interactions\r\nbetween police and publice and public perceptions of police in 2011. These data are archived as POLICE-PUBLIC CONTACT SURVEY, 2011 (ICPSR 34276).",
-            "modified": "2014-03-18T11:30:38",
-            "accessLevel": "public",
-            "identifier": "2215",
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
+            "title": "National Incident-Based Reporting System, 1992"
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
+            "description": "\r\nThe Police-Public Contact Survey (PPCS) provides detailed information on the nature and\r\ncharacteristics of face-to-face contacts between police and the public, including the\r\nreason for and outcome of the contact. The PPCS interviews a nationally representative\r\nsample of U.S. residents age 16 or older as a supplement to the National Crime\r\nVictimization Survey. To date, the PPCS has been conducted six times by BJS:\r\nThe first survey - described in the BJS publication Police Use of Force: Collection of National Data\r\n(NCJ 165040) - documented levels of contacts with police during 1996.\r\nThe second survey - described in Contacts between Police and the Public: Findings from the\r\n1999 National Survey (NCJ 184957) - recorded police-citizen contacts in 1999. These data are\r\narchived as POLICE-PUBLIC CONTACT SURVEY, 1999: [UNITED STATES] (ICPSR 3151).\r\nThe third survey - described in Contacts between Police and the Public: Findings from the\r\n2002 National Survey (NCJ 207845) - covered interactions between police and the public in\r\n2002. These data are archived as POLICE-PUBLIC CONTACT SURVEY, 2002: [UNITED STATES]\r\n(ICPSR 4273). \r\nThe fourth survey - described in the BJS publication Contacts between\r\nPolice and the Public, 2005 (NCJ 215243) - covered interactions between police and the\r\npublic in 2005. These data are archived as POLICE-PUBLIC CONTACT SURVEY, 2005: [UNITED\r\nSTATES] (ICPSR 020020).\r\nThe fifth survey - described in the BJS publication Contacts between Police and the\r\nPublic, 2008 (NCJ 234599) - covered interactions between police and the public in\r\n2008. These data are archived as POLICE-PUBLIC CONTACT SURVEY, 2008 (ICPSR 32022).\r\nThe sixth survey (split sample design due to instrument changes) - new instrument findings described in\r\ntwo publications: Police Behavior During Traffic and Street Stops, 2011 (NCJ 242937) and Requests for Police Assistance, 2011 (NCJ 242938) - covered interactions\r\nbetween police and publice and public perceptions of police in 2011. These data are archived as POLICE-PUBLIC CONTACT SURVEY, 2011 (ICPSR 34276).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR34276.v1",
+                    "title": "Police-Public Contact Survey, 2011"
+                }
+            ],
+            "identifier": "2215",
+            "isPartOf": "2432",
+            "issued": "2014-03-18T11:30:38",
             "keyword": [
                 "police citizen interactions",
                 "police community relations",
@@ -51464,54 +51458,54 @@
                 "public interest",
                 "public opinion"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2014-03-18T11:30:38",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2014-03-18T11:30:38",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR34276.v1",
-                    "title": "Police-Public Contact Survey, 2011"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Deaths in Custody Reporting Program: Local Jails, 2000 - 2013",
-            "description": "The Deaths in Custody Reporting Program (DCRP) is an annual data collection\r\nconducted by the Bureau of Justice Statistics (BJS). The DCRP began in 2000\r\nunder the Death in Custody Reporting Act of 2000 (P.L. 106-297). It is the\r\nonly national statistical collection that obtains detailed information\r\nabout deaths in adult correctional facilities. The DCRP collects data on\r\npersons dying in state prisons, local jails and in the process of\r\narrest. Each collection is a separate subcollection, but each is under the\r\numbrella of the DCRP collection. This deals with the local jails subcollection,\r\nwhich has a local jail facilities death file.\r\nThe jails portion of the Deaths in Custody Reporting Program began in 2000\r\nafter the passage of the Deaths in Custody Reporting Act of 2000 in October\r\nof 2000. The jails component of the DCRP collects data on inmate deaths\r\noccurring in local jail facilities while inmates are in\r\nthe physical custody of jail facility officials.",
-            "modified": "2016-08-31T11:12:55",
-            "accessLevel": "restricted public",
-            "identifier": "2216",
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
+            "title": "Police-Public Contact Survey, 2011"
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
+            "description": "The Deaths in Custody Reporting Program (DCRP) is an annual data collection\r\nconducted by the Bureau of Justice Statistics (BJS). The DCRP began in 2000\r\nunder the Death in Custody Reporting Act of 2000 (P.L. 106-297). It is the\r\nonly national statistical collection that obtains detailed information\r\nabout deaths in adult correctional facilities. The DCRP collects data on\r\npersons dying in state prisons, local jails and in the process of\r\narrest. Each collection is a separate subcollection, but each is under the\r\numbrella of the DCRP collection. This deals with the local jails subcollection,\r\nwhich has a local jail facilities death file.\r\nThe jails portion of the Deaths in Custody Reporting Program began in 2000\r\nafter the passage of the Deaths in Custody Reporting Act of 2000 in October\r\nof 2000. The jails component of the DCRP collects data on inmate deaths\r\noccurring in local jail facilities while inmates are in\r\nthe physical custody of jail facility officials.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR34286.v1",
+                    "title": "Deaths in Custody Reporting Program: Local Jails, 2000 - 2013"
+                }
+            ],
+            "identifier": "2216",
+            "isPartOf": "2441",
+            "issued": "2016-08-31T11:09:40",
             "keyword": [
                 "correctional facilities",
                 "corrections",
@@ -51519,55 +51513,55 @@
                 "homicide",
                 "suicide"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2016-08-31T11:12:55",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2441",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2016-08-31T11:09:40",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR34286.v1",
-                    "title": "Deaths in Custody Reporting Program: Local Jails, 2000 - 2013"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Law Enforcement Management and Administrative Statistics (LEMAS), 2016",
-            "description": "The Law Enforcement Management and Administrative Statistics (LEMAS) survey collects data from a nationally representative sample of general-purpose agencies (i.e., local and county police departments, sheriffs' offices, and primary state police agencies). The 2016 LEMAS sample design called for the survey questionnaire to be sent to 3,499 general purpose law enforcement agencies, including 2,640 local and county police departments, 810 sheriffs' offices, and the 49 primary state police departments (Hawaii does not have a primary state police agency). The design called for all agencies employing 100 or more full-time equivalent sworn personnel to be included with certainty (self-representing), and for smaller agencies to be sampled from strata based on number of full-time equivalent sworn officers and type of agency. A total of 28 local police departments were determined to be out-of-scope for the survey because they had closed, had less than one full-time equivalent sworn officer, had contracted out their services with another law enforcement agency, or only had special enforcement responsibilities. The final mail out total of 3,471 agencies included 2,612 local police departments, 810 sheriffs' offices, and the 49 state agencies.",
-            "modified": "2020-08-20T09:49:27",
-            "accessLevel": "public",
-            "identifier": "2217",
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
+            "title": "Deaths in Custody Reporting Program: Local Jails, 2000 - 2013"
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
+            "description": "The Law Enforcement Management and Administrative Statistics (LEMAS) survey collects data from a nationally representative sample of general-purpose agencies (i.e., local and county police departments, sheriffs' offices, and primary state police agencies). The 2016 LEMAS sample design called for the survey questionnaire to be sent to 3,499 general purpose law enforcement agencies, including 2,640 local and county police departments, 810 sheriffs' offices, and the 49 primary state police departments (Hawaii does not have a primary state police agency). The design called for all agencies employing 100 or more full-time equivalent sworn personnel to be included with certainty (self-representing), and for smaller agencies to be sampled from strata based on number of full-time equivalent sworn officers and type of agency. A total of 28 local police departments were determined to be out-of-scope for the survey because they had closed, had less than one full-time equivalent sworn officer, had contracted out their services with another law enforcement agency, or only had special enforcement responsibilities. The final mail out total of 3,471 agencies included 2,612 local police departments, 810 sheriffs' offices, and the 49 state agencies.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR37323.v1",
+                    "title": "Law Enforcement Management and Administrative Statistics (LEMAS), 2016"
+                }
+            ],
+            "identifier": "2217",
+            "isPartOf": "2430",
+            "issued": "2020-08-20T09:49:27",
             "keyword": [
                 "administration",
                 "budgets",
@@ -51583,109 +51577,109 @@
                 "wages and salaries",
                 "workers"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2020-08-20T09:49:27",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2430",
-            "dataQuality": false,
-            "issued": "2020-08-20T09:49:27",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR37323.v1",
-                    "title": "Law Enforcement Management and Administrative Statistics (LEMAS), 2016"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Offenders Released From Prison, 2015",
-            "description": "The data contain records of sentenced offenders released from the custody of the Bureau of Prisons (BOP) during fiscal year 2015. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. Records of offenders who exit federal prison temporarily, such as for transit to another location, to serve a weekend sentence, or for health care, are not included in the exiting cohort. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database as well as additional analysis variables. Variables containing identifying information (e.g., name, Social Security Number) were either removed, coarsened, or blanked in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, D.C.) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute through 2012. Data from 2013 and on were prepared by Abt Associates.",
-            "modified": "2019-09-23T13:06:27",
-            "accessLevel": "restricted public",
-            "identifier": "2218",
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
+            "title": "Law Enforcement Management and Administrative Statistics (LEMAS), 2016"
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
+            "description": "The data contain records of sentenced offenders released from the custody of the Bureau of Prisons (BOP) during fiscal year 2015. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. Records of offenders who exit federal prison temporarily, such as for transit to another location, to serve a weekend sentence, or for health care, are not included in the exiting cohort. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database as well as additional analysis variables. Variables containing identifying information (e.g., name, Social Security Number) were either removed, coarsened, or blanked in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, D.C.) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute through 2012. Data from 2013 and on were prepared by Abt Associates.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR37324.v1",
+                    "title": "Federal Justice Statistics Program: Offenders Released From Prison, 2015"
+                }
+            ],
+            "identifier": "2218",
+            "isPartOf": "2174",
+            "issued": "2019-09-23T13:04:10",
             "keyword": [
                 "correctional facilities",
                 "correctional system",
                 "inmate release plans",
                 "offenders"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2019-09-23T13:06:27",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2019-09-23T13:04:10",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR37324.v1",
-                    "title": "Federal Justice Statistics Program: Offenders Released From Prison, 2015"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court - Pending, 2015",
-            "description": "The data contain records of defendants in criminal cases filed in United States District Court before or during fiscal year 2015 and still pending as of year-end. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables. Variables containing identifying information (e.g., name, Social Security number) were either removed, coarsened, or blanked in order to protect the identities of individuals. These data are part of a series designed by Abt and the Bureau of Justice Statistics. Data and documentation were prepared by Abt.",
-            "modified": "2019-09-26T11:01:39",
-            "accessLevel": "restricted public",
-            "identifier": "2219",
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
+            "title": "Federal Justice Statistics Program: Offenders Released From Prison, 2015"
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
+            "description": "The data contain records of defendants in criminal cases filed in United States District Court before or during fiscal year 2015 and still pending as of year-end. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables. Variables containing identifying information (e.g., name, Social Security number) were either removed, coarsened, or blanked in order to protect the identities of individuals. These data are part of a series designed by Abt and the Bureau of Justice Statistics. Data and documentation were prepared by Abt.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR37334.v1",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court - Pending, 2015"
+                }
+            ],
+            "identifier": "2219",
+            "isPartOf": "2174",
+            "issued": "2019-09-26T10:59:27",
             "keyword": [
                 "administration",
                 "court cases",
@@ -51697,55 +51691,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2019-09-26T11:01:39",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2019-09-26T10:59:27",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR37334.v1",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court - Pending, 2015"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 2016",
-            "description": "The data contain records of criminal appeals cases filed in United States Courts of Appeals during fiscal year 2016. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. The data file contains variables from the original AOUSC files as well as additional analysis variables. Variables containing identifying information (e.g., name, Social Security number) were either removed, coarsened, or blanked in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute through 2012. Data from 2013 on were prepared by Abt Associates.",
-            "modified": "2019-12-19T09:24:15",
-            "accessLevel": "restricted public",
-            "identifier": "2220",
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court - Pending, 2015"
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
+            "description": "The data contain records of criminal appeals cases filed in United States Courts of Appeals during fiscal year 2016. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. The data file contains variables from the original AOUSC files as well as additional analysis variables. Variables containing identifying information (e.g., name, Social Security number) were either removed, coarsened, or blanked in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute through 2012. Data from 2013 on were prepared by Abt Associates.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR37340.v1",
+                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 2016"
+                }
+            ],
+            "identifier": "2220",
+            "isPartOf": "2174",
+            "issued": "2019-12-19T09:22:29",
             "keyword": [
                 "administration",
                 "appellate courts",
@@ -51756,55 +51750,55 @@
                 "judicial decisions",
                 "legal systems"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2019-12-19T09:24:15",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2019-12-19T09:22:29",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR37340.v1",
-                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 2016"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 2015",
-            "description": "The data contain records of arrests and bookings for federal offenses in the United States during fiscal year 2015. The data were constructed from the United States Marshals Service (USMS) Prisoner Tracking System database. Records include arrests made by federal law enforcement agencies (including the USMS), state and local agencies, and self-surrenders. Offenders arrested for federal offenses are transferred to the custody of the USMS for processing, transportation, and detention. The Prisoner Tracking System contains data on all offenders within the custody of the USMS. The data file contains variables from the original USMS files as well as additional analysis variables. Variables containing identifying information (e.g., name, Social Security number) were either removed, coarsened, or blanked in order to protect the identities of individuals. These data are part of a series designed by Abt and the Bureau of Justice Statistics. Data and documentation were prepared by Abt.",
-            "modified": "2019-09-24T10:07:41",
-            "accessLevel": "restricted public",
-            "identifier": "2221",
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
+            "title": "Federal Justice Statistics Program: Criminal Appeals Cases Filed in Courts of Appeals, 2016"
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
+            "description": "The data contain records of arrests and bookings for federal offenses in the United States during fiscal year 2015. The data were constructed from the United States Marshals Service (USMS) Prisoner Tracking System database. Records include arrests made by federal law enforcement agencies (including the USMS), state and local agencies, and self-surrenders. Offenders arrested for federal offenses are transferred to the custody of the USMS for processing, transportation, and detention. The Prisoner Tracking System contains data on all offenders within the custody of the USMS. The data file contains variables from the original USMS files as well as additional analysis variables. Variables containing identifying information (e.g., name, Social Security number) were either removed, coarsened, or blanked in order to protect the identities of individuals. These data are part of a series designed by Abt and the Bureau of Justice Statistics. Data and documentation were prepared by Abt.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR37342.v1",
+                    "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 2015"
+                }
+            ],
+            "identifier": "2221",
+            "isPartOf": "2174",
+            "issued": "2019-09-24T10:04:42",
             "keyword": [
                 "arrest records",
                 "arrests",
@@ -51812,55 +51806,55 @@
                 "federal prisoners",
                 "offenders"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2019-09-24T10:07:41",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2019-09-24T10:04:42",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR37342.v1",
-                    "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 2015"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals - Terminated, 2015",
-            "description": "The data contain records of criminal appeals cases terminated in United States Courts of Appeals during fiscal year 2015. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. Appeals may be terminated on the merits or on procedural grounds. Of those that are terminated on the merits, the district court ruling may be affirmed, reversed, remanded to criminal court, or dismissed. The data file contains variables from the original AOUSC files as well as additional analysis variables. Variables containing identifying information (e.g., name, Social Security number) were either removed, coarsened, or blanked in order to protect the identities of individuals.\r\nThese data are part of a series designed by the Urban Institute (Washington, D.C.) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute through 2012. Data from 2013 and on were prepared by Abt Associates.",
-            "modified": "2019-09-26T08:54:35",
-            "accessLevel": "restricted public",
-            "identifier": "2222",
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
+            "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 2015"
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
+            "description": "The data contain records of criminal appeals cases terminated in United States Courts of Appeals during fiscal year 2015. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. Appeals may be terminated on the merits or on procedural grounds. Of those that are terminated on the merits, the district court ruling may be affirmed, reversed, remanded to criminal court, or dismissed. The data file contains variables from the original AOUSC files as well as additional analysis variables. Variables containing identifying information (e.g., name, Social Security number) were either removed, coarsened, or blanked in order to protect the identities of individuals.\r\nThese data are part of a series designed by the Urban Institute (Washington, D.C.) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute through 2012. Data from 2013 and on were prepared by Abt Associates.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR37343.v1",
+                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals - Terminated, 2015"
+                }
+            ],
+            "identifier": "2222",
+            "isPartOf": "2174",
+            "issued": "2019-09-26T08:52:38",
             "keyword": [
                 "administration",
                 "appellate courts",
@@ -51871,55 +51865,55 @@
                 "judicial decisions",
                 "legal systems"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2019-09-26T08:54:35",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2019-09-26T08:52:38",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR37343.v1",
-                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals - Terminated, 2015"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Statutes for Counts of Convictions for Defendants Sentenced Under the Sentencing Reform Act, 2015",
-            "description": "These data contain records of statutes for each count of conviction for criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2015. The data are one of two supplementary files that should be used in conjunction with the primary analysis file, which contains records for all defendants sentenced under the guidelines. These data can be linked to the primary analysis file using the unique identifier variable USSCIDN. The number of records for a defendant in the current data corresponds to the total number of counts of conviction for that defendant, and that total is recorded in the NOCOUNT variable. As an example, if a defendant has five counts of conviction (NOCOUNT=5), he or she will have five records in the current data. As it is possible for defendants to have multiple statutes applying to a single count of conviction, up to three statutes (STA1-STA3) are recorded for each count of conviction. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. These data are part of a series designed by Abt and the Bureau of Justice Statistics. Data and documentation were prepared by Abt.",
-            "modified": "2019-09-24T10:36:26",
-            "accessLevel": "restricted public",
-            "identifier": "2223",
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
+            "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals - Terminated, 2015"
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
+            "description": "These data contain records of statutes for each count of conviction for criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2015. The data are one of two supplementary files that should be used in conjunction with the primary analysis file, which contains records for all defendants sentenced under the guidelines. These data can be linked to the primary analysis file using the unique identifier variable USSCIDN. The number of records for a defendant in the current data corresponds to the total number of counts of conviction for that defendant, and that total is recorded in the NOCOUNT variable. As an example, if a defendant has five counts of conviction (NOCOUNT=5), he or she will have five records in the current data. As it is possible for defendants to have multiple statutes applying to a single count of conviction, up to three statutes (STA1-STA3) are recorded for each count of conviction. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. These data are part of a series designed by Abt and the Bureau of Justice Statistics. Data and documentation were prepared by Abt.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR37344.v1",
+                    "title": "Federal Justice Statistics Program: Statutes for Counts of Convictions for Defendants Sentenced Under the Sentencing Reform Act, 2015"
+                }
+            ],
+            "identifier": "2223",
+            "isPartOf": "2174",
+            "issued": "2019-09-24T10:26:30",
             "keyword": [
                 "administration",
                 "court cases",
@@ -51931,55 +51925,55 @@
                 "sentencing guidelines",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2019-09-24T10:36:26",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2019-09-24T10:26:30",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR37344.v1",
-                    "title": "Federal Justice Statistics Program: Statutes for Counts of Convictions for Defendants Sentenced Under the Sentencing Reform Act, 2015"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Survey of Jails, 2017",
-            "description": "The Annual Survey of Jails (ASJ) is the only data collection effort that provides an annual source of data on local jails and jail inmates. Data on the size of the jail population and selected inmate characteristics are obtained every five to six years from the Census of Jails. In each of the years between the complete censuses, a sample survey of jails is conducted to estimate\r\nbaseline characteristics of the nation's jails and inmates housed in these jails. The 2017 Annual Survey of Jails is the 30th such survey in a series begun in 1982. The ASJ supplies data on characteristics of jails such as admissions and releases, growth in the number of jail facilities, changes in their rated capacities and level of occupancy, growth in the population supervised in the community, changes in methods of community supervision, and crowding issues. The ASJ also provides information on changes in the demographics of the jail population, supervision status of persons held, and a count of non-U.S. citizens in custody. The data presented in this study were collected in the Annual Survey of Jails, 2017. These data are used to track growth in the number of jails and the capacities nationally, changes in the demographics of the jail population and supervision status of persons held, the prevalence of crowding issues, and a count of non-U.S. citizens within the jail population. The data are intended for a variety of users, including Federal and State agencies, local officials in conjunction with jail administrators, researchers, planners, and the public. The reference date for the survey is June 30, 2017.",
-            "modified": "2019-10-10T10:16:18",
-            "accessLevel": "public",
-            "identifier": "2224",
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
+            "title": "Federal Justice Statistics Program: Statutes for Counts of Convictions for Defendants Sentenced Under the Sentencing Reform Act, 2015"
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
+            "description": "The Annual Survey of Jails (ASJ) is the only data collection effort that provides an annual source of data on local jails and jail inmates. Data on the size of the jail population and selected inmate characteristics are obtained every five to six years from the Census of Jails. In each of the years between the complete censuses, a sample survey of jails is conducted to estimate\r\nbaseline characteristics of the nation's jails and inmates housed in these jails. The 2017 Annual Survey of Jails is the 30th such survey in a series begun in 1982. The ASJ supplies data on characteristics of jails such as admissions and releases, growth in the number of jail facilities, changes in their rated capacities and level of occupancy, growth in the population supervised in the community, changes in methods of community supervision, and crowding issues. The ASJ also provides information on changes in the demographics of the jail population, supervision status of persons held, and a count of non-U.S. citizens in custody. The data presented in this study were collected in the Annual Survey of Jails, 2017. These data are used to track growth in the number of jails and the capacities nationally, changes in the demographics of the jail population and supervision status of persons held, the prevalence of crowding issues, and a count of non-U.S. citizens within the jail population. The data are intended for a variety of users, including Federal and State agencies, local officials in conjunction with jail administrators, researchers, planners, and the public. The reference date for the survey is June 30, 2017.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR37373.v1",
+                    "title": "Annual Survey of Jails, 2017"
+                }
+            ],
+            "identifier": "2224",
+            "isPartOf": "2586",
+            "issued": "2019-10-10T10:16:18",
             "keyword": [
                 "correctional facilities",
                 "correctional system",
@@ -51989,54 +51983,54 @@
                 "population characteristics",
                 "probation"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2019-10-10T10:16:18",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2586",
-            "dataQuality": false,
-            "issued": "2019-10-10T10:16:18",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR37373.v1",
-                    "title": "Annual Survey of Jails, 2017"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 2015",
-            "description": "The data contain records of suspects in federal criminal matters received by United States attorneys or filed before the United States magistrates during fiscal year 2015. These data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables. Variables containing identifying information (e.g., name, Social Security Number) were either removed, coarsened, or blanked in order to protect the identities of individuals. These data are part of a series designed by Abt and the Bureau of Justice Statistics. Data and documentation were prepared by Abt.",
-            "modified": "2019-09-25T11:15:42",
-            "accessLevel": "restricted public",
-            "identifier": "2225",
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
+            "title": "Annual Survey of Jails, 2017"
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
+            "description": "The data contain records of suspects in federal criminal matters received by United States attorneys or filed before the United States magistrates during fiscal year 2015. These data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables. Variables containing identifying information (e.g., name, Social Security Number) were either removed, coarsened, or blanked in order to protect the identities of individuals. These data are part of a series designed by Abt and the Bureau of Justice Statistics. Data and documentation were prepared by Abt.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR37374.v1",
+                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 2015"
+                }
+            ],
+            "identifier": "2225",
+            "isPartOf": "2174",
+            "issued": "2019-09-25T11:13:56",
             "keyword": [
                 "defendants",
                 "federal courts",
@@ -52044,55 +52038,55 @@
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2019-09-25T11:15:42",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2019-09-25T11:13:56",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR37374.v1",
-                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 2015"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2015",
-            "description": "The data contain records of suspects in federal criminal matters concluded by United States attorneys or United States magistrates during fiscal year 2015. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables. Variables containing identifying information (e.g., name, Social Security Number) were either removed, coarsened, or blanked in order to protect the identities of individuals. These data are part of a series designed by Abt and the Bureau of Justice Statistics. Data and documentation were prepared by Abt.",
-            "modified": "2019-09-25T11:04:30",
-            "accessLevel": "restricted public",
-            "identifier": "2226",
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
+            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 2015"
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
+            "description": "The data contain records of suspects in federal criminal matters concluded by United States attorneys or United States magistrates during fiscal year 2015. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables. Variables containing identifying information (e.g., name, Social Security Number) were either removed, coarsened, or blanked in order to protect the identities of individuals. These data are part of a series designed by Abt and the Bureau of Justice Statistics. Data and documentation were prepared by Abt.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR37376.v1",
+                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2015"
+                }
+            ],
+            "identifier": "2226",
+            "isPartOf": "2174",
+            "issued": "2019-09-25T11:02:05",
             "keyword": [
                 "defendants",
                 "federal courts",
@@ -52100,55 +52094,55 @@
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2019-09-25T11:04:30",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2019-09-25T11:02:05",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR37376.v1",
-                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2015"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court - Terminated, 2015",
-            "description": "The data contain records of defendants in criminal cases terminated in United States District Court during fiscal year 2015. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables. Variables containing identifying information (e.g., name, Social Security number) were either removed, coarsened, or blanked in order to protect the identities of individuals. These data are part of a series designed by Abt and the Bureau of Justice Statistics. Data and documentation were prepared by Abt.",
-            "modified": "2019-09-26T16:05:16",
-            "accessLevel": "restricted public",
-            "identifier": "2227",
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
+            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2015"
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
+            "description": "The data contain records of defendants in criminal cases terminated in United States District Court during fiscal year 2015. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables. Variables containing identifying information (e.g., name, Social Security number) were either removed, coarsened, or blanked in order to protect the identities of individuals. These data are part of a series designed by Abt and the Bureau of Justice Statistics. Data and documentation were prepared by Abt.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR37377.v1",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court - Terminated, 2015"
+                }
+            ],
+            "identifier": "2227",
+            "isPartOf": "2174",
+            "issued": "2019-09-26T15:59:46",
             "keyword": [
                 "administration",
                 "court cases",
@@ -52160,163 +52154,163 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2019-09-26T16:05:16",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2019-09-26T15:59:46",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR37377.v1",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court - Terminated, 2015"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Offenders Released From Prison, 2010",
-            "description": "The data contain records of sentenced offenders released from the custody of the Bureau of Prisons (BOP) during fiscal year 2010. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. Records of offenders who exit federal prison temporarily, such as for transit to another location, to serve a weekend sentence, or for health care, are not included in the exiting cohort. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2014-03-11T12:07:37",
-            "accessLevel": "restricted public",
-            "identifier": "2228",
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court - Terminated, 2015"
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
+            "description": "The data contain records of sentenced offenders released from the custody of the Bureau of Prisons (BOP) during fiscal year 2010. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. Records of offenders who exit federal prison temporarily, such as for transit to another location, to serve a weekend sentence, or for health care, are not included in the exiting cohort. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR34328.v2",
+                    "title": "Federal Justice Statistics Program: Offenders Released From Prison, 2010"
+                }
+            ],
+            "identifier": "2228",
+            "isPartOf": "2174",
+            "issued": "2013-01-07T10:30:46",
             "keyword": [
                 "correctional system",
                 "offenders",
                 "prisons"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2014-03-11T12:07:37",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2013-01-07T10:30:46",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR34328.v2",
-                    "title": "Federal Justice Statistics Program: Offenders Released From Prison, 2010"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 2010",
-            "description": "The data contain records of sentenced offenders in the custody of the Bureau of Prisons (BOP) at year-end of fiscal year 2010. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2014-03-11T12:13:06",
-            "accessLevel": "restricted public",
-            "identifier": "2229",
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
+            "title": "Federal Justice Statistics Program: Offenders Released From Prison, 2010"
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
+            "description": "The data contain records of sentenced offenders in the custody of the Bureau of Prisons (BOP) at year-end of fiscal year 2010. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR34329.v2",
+                    "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 2010"
+                }
+            ],
+            "identifier": "2229",
+            "isPartOf": "2174",
+            "issued": "2013-01-07T13:30:42",
             "keyword": [
                 "correctional system",
                 "offenders",
                 "prisons"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2014-03-11T12:13:06",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2013-01-07T13:30:42",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR34329.v2",
-                    "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 2010"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data [United States]:  Offenses Known and Clearances by Arrest, 1999    ",
-            "description": "Since 1930, the Federal Bureau of Investigation has\r\n compiled the Uniform Crime Reports (UCR) to serve as periodic\r\n nationwide assessments of reported crimes not available elsewhere in\r\n the criminal justice system. Law enforcement agencies contribute\r\n reports either directly or through their state reporting\r\n programs. Each year, summary data are reported in four types of files:\r\n (1) Offenses Known and Clearances by Arrest, (2) Property Stolen and\r\n Recovered, (3) Supplementary Homicide Reports (SHR), and (4) Police\r\n Employee (LEOKA) Data. The Offenses Known and Clearances by Arrest\r\n data files include monthly data on the number of Crime Index offenses\r\n reported and the number of offenses cleared by arrest or other\r\n means. The counts include all reports of Index Crimes (excluding\r\n arson) received from victims, officers who discovered infractions, or\r\nother sources.",
-            "modified": "2005-11-04T00:00:00",
-            "accessLevel": "public",
-            "identifier": "2230",
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
+            "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 2010"
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
+            "description": "Since 1930, the Federal Bureau of Investigation has\r\n compiled the Uniform Crime Reports (UCR) to serve as periodic\r\n nationwide assessments of reported crimes not available elsewhere in\r\n the criminal justice system. Law enforcement agencies contribute\r\n reports either directly or through their state reporting\r\n programs. Each year, summary data are reported in four types of files:\r\n (1) Offenses Known and Clearances by Arrest, (2) Property Stolen and\r\n Recovered, (3) Supplementary Homicide Reports (SHR), and (4) Police\r\n Employee (LEOKA) Data. The Offenses Known and Clearances by Arrest\r\n data files include monthly data on the number of Crime Index offenses\r\n reported and the number of offenses cleared by arrest or other\r\n means. The counts include all reports of Index Crimes (excluding\r\n arson) received from victims, officers who discovered infractions, or\r\nother sources.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR03158.v2",
+                    "title": "Uniform Crime Reporting Program Data [United States]:  Offenses Known and Clearances by Arrest, 1999    "
+                }
+            ],
+            "identifier": "2230",
+            "isPartOf": "2167",
+            "issued": "2001-05-09T00:00:00",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrest records",
@@ -52327,54 +52321,54 @@
                 "law enforcement",
                 "offenses"
             ],
-            "bureauCode": [
-                "011:21"
-            ],
-            "programCode": [
-                "011:061"
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2001-05-09T00:00:00",
             "language": [
                 "eng"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR03158.v2",
-                    "title": "Uniform Crime Reporting Program Data [United States]:  Offenses Known and Clearances by Arrest, 1999    "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data [United States]: Supplementary Homicide Reports, 1999",
-            "description": "Since 1930, the Federal Bureau of Investigation has\r\ncompiled the Uniform Crime Reports (UCR) to serve as a periodic\r\nnationwide assessment of reported crimes not available elsewhere in\r\nthe criminal justice system. Each year, participating law enforcement\r\nagencies contribute reports either directly or through their state\r\nreporting programs. Summary data are provided in four types of files:\r\n(1) Offenses Known and Clearances by Arrest, (2) Property Stolen and\r\nRecovered, (3) Supplementary Homicide Reports (SHR), and (4) Police\r\nEmployee (LEOKA) Data. The Supplementary Homicide Reports provide\r\nincident-based information on criminal homicides reported to the\r\npolice. These homicides consist of murders, non-negligent\r\nmanslaughter, and justifiable homicides. The data, provided monthly by\r\nUCR agencies, contain information describing the victim of each\r\nhomicide, the offender, and the relationship between victim and\r\noffender.",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "modified": "2005-11-04T00:00:00",
-            "accessLevel": "public",
-            "identifier": "2231",
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
+            "title": "Uniform Crime Reporting Program Data [United States]:  Offenses Known and Clearances by Arrest, 1999    "
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
+            "description": "Since 1930, the Federal Bureau of Investigation has\r\ncompiled the Uniform Crime Reports (UCR) to serve as a periodic\r\nnationwide assessment of reported crimes not available elsewhere in\r\nthe criminal justice system. Each year, participating law enforcement\r\nagencies contribute reports either directly or through their state\r\nreporting programs. Summary data are provided in four types of files:\r\n(1) Offenses Known and Clearances by Arrest, (2) Property Stolen and\r\nRecovered, (3) Supplementary Homicide Reports (SHR), and (4) Police\r\nEmployee (LEOKA) Data. The Supplementary Homicide Reports provide\r\nincident-based information on criminal homicides reported to the\r\npolice. These homicides consist of murders, non-negligent\r\nmanslaughter, and justifiable homicides. The data, provided monthly by\r\nUCR agencies, contain information describing the victim of each\r\nhomicide, the offender, and the relationship between victim and\r\noffender.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR03162.v1",
+                    "title": "Uniform Crime Reporting Program Data [United States]: Supplementary Homicide Reports, 1999"
+                }
+            ],
+            "identifier": "2231",
+            "isPartOf": "2167",
+            "issued": "2001-05-18T00:00:00",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -52388,54 +52382,54 @@
                 "offenses",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
-            ],
-            "programCode": [
-                "011:061"
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2001-05-18T00:00:00",
             "language": [
                 "eng"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR03162.v1",
-                    "title": "Uniform Crime Reporting Program Data [United States]: Supplementary Homicide Reports, 1999"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data [United States]:  Property Stolen and Recovered, 1999 ",
-            "description": "Since 1930, the Federal Bureau of Investigation has\r\n compiled the Uniform Crime Reports (UCR) to serve as periodic\r\n nationwide assessments of reported crimes not available elsewhere in\r\n the criminal justice system. Law enforcement agencies contribute\r\n reports either directly or through their state reporting\r\n programs. Each year, this information is reported in four types of\r\n files: (1) Offenses Known and Clearances by Arrest, (2) Property\r\n Stolen and Recovered, (3) Supplementary Homicide Reports (SHR), and\r\n (4) Police Employee (LEOKA) Data. The Property Stolen and Recovered\r\n data are collected on a monthly basis by all UCR contributing\r\n agencies. These data, aggregated at the agency level, report on the\r\n nature of the crime, the monetary value of the property stolen, and\r\n the type of property stolen. Similar information regarding recovered\r\nproperty is also included in the data.",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "modified": "2005-11-04T00:00:00",
-            "accessLevel": "public",
-            "identifier": "2232",
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
+            "title": "Uniform Crime Reporting Program Data [United States]: Supplementary Homicide Reports, 1999"
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
+            "description": "Since 1930, the Federal Bureau of Investigation has\r\n compiled the Uniform Crime Reports (UCR) to serve as periodic\r\n nationwide assessments of reported crimes not available elsewhere in\r\n the criminal justice system. Law enforcement agencies contribute\r\n reports either directly or through their state reporting\r\n programs. Each year, this information is reported in four types of\r\n files: (1) Offenses Known and Clearances by Arrest, (2) Property\r\n Stolen and Recovered, (3) Supplementary Homicide Reports (SHR), and\r\n (4) Police Employee (LEOKA) Data. The Property Stolen and Recovered\r\n data are collected on a monthly basis by all UCR contributing\r\n agencies. These data, aggregated at the agency level, report on the\r\n nature of the crime, the monetary value of the property stolen, and\r\n the type of property stolen. Similar information regarding recovered\r\nproperty is also included in the data.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR03164.v1",
+                    "title": "Uniform Crime Reporting Program Data [United States]:  Property Stolen and Recovered, 1999 "
+                }
+            ],
+            "identifier": "2232",
+            "isPartOf": "2167",
+            "issued": "2001-05-29T00:00:00",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -52450,54 +52444,54 @@
                 "stolen property",
                 "stolen property recovery"
             ],
-            "bureauCode": [
-                "011:21"
-            ],
-            "programCode": [
-                "011:061"
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2001-05-29T00:00:00",
             "language": [
                 "eng"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR03164.v1",
-                    "title": "Uniform Crime Reporting Program Data [United States]:  Property Stolen and Recovered, 1999 "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data [United States]:  Police Employee (LEOKA) Data, 1999    ",
-            "description": "Since 1930, the Federal Bureau of Investigation has\r\n compiled the Uniform Crime Reports (UCR) to serve as a periodic\r\n nationwide assessment of reported crimes not available elsewhere in\r\n the criminal justice system. Each year, this information is reported\r\n in four types of files: (1) Offenses Known and Clearances by Arrest,\r\n (2) Property Stolen and Recovered, (3) Supplementary Homicide Reports\r\n (SHR), and (4) Police Employee (LEOKA) Data. The Police Employee\r\n (LEOKA) Data provide information about law enforcement officers killed\r\n or assaulted (hence the acronym, LEOKA) in the line of duty. The\r\n variables created from the LEOKA forms provide in-depth information on\r\n the circumstances surrounding killings or assaults, including type of\r\n call answered, type of weapon used, and type of patrol the officers\r\nwere on.",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "modified": "2005-11-04T00:00:00",
-            "accessLevel": "public",
-            "identifier": "2233",
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
+            "title": "Uniform Crime Reporting Program Data [United States]:  Property Stolen and Recovered, 1999 "
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
+            "description": "Since 1930, the Federal Bureau of Investigation has\r\n compiled the Uniform Crime Reports (UCR) to serve as a periodic\r\n nationwide assessment of reported crimes not available elsewhere in\r\n the criminal justice system. Each year, this information is reported\r\n in four types of files: (1) Offenses Known and Clearances by Arrest,\r\n (2) Property Stolen and Recovered, (3) Supplementary Homicide Reports\r\n (SHR), and (4) Police Employee (LEOKA) Data. The Police Employee\r\n (LEOKA) Data provide information about law enforcement officers killed\r\n or assaulted (hence the acronym, LEOKA) in the line of duty. The\r\n variables created from the LEOKA forms provide in-depth information on\r\n the circumstances surrounding killings or assaults, including type of\r\n call answered, type of weapon used, and type of patrol the officers\r\nwere on.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR03165.v1",
+                    "title": "Uniform Crime Reporting Program Data [United States]:  Police Employee (LEOKA) Data, 1999    "
+                }
+            ],
+            "identifier": "2233",
+            "isPartOf": "2167",
+            "issued": "2001-06-29T00:00:00",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -52510,54 +52504,53 @@
                 "police deaths",
                 "police officers"
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
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2001-06-29T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR03165.v1",
-                    "title": "Uniform Crime Reporting Program Data [United States]:  Police Employee (LEOKA) Data, 1999    "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Multi-User Database on the Attributes of United States Appeals Court Judges, 1801-2000",
-            "description": "This project orignally was undertaken to compile a definitive\r\ndatabase on the personal, social, economic, career, and political\r\nattributes of judges who served on the United States Courts of Appeals from\r\n1801 to 1994 - it has now been updated to include information through the year 2000. The database includes conventional social background\r\nvariables such as appointing president, religion, political party\r\naffiliation, education, and prior experience. In addition, unique items are\r\nprovided: the temporal sequence of prior career experiences, the\r\ntiming of and reason for leaving the bench, gender, race and ethnicity,\r\nposition numbering analogous to the scheme used for the Supreme Court,\r\nAmerican Bar Association rating, and net worth (for judges who began\r\nservice on the bench after 1978). The second objective of this project\r\nwas to merge\r\nthese data with a multi-user database on United States Courts of Appeals decisions\r\nthat is headed by Donald Songer and funded by the National Science\r\nFoundation. That database includes a unique identification number\r\nfor each judge participating in a particular decision. The combined\r\ndatabases\r\nshould enable scholars to explore: (1) intra- and inter-circuit fluctuation\r\nin the distribution of social background characteristics, (2) generational\r\nand presidential cohort variation in these attributes, and (3) state\r\nand partisan control of seats. The collection also facilitates the\r\nconstruction of models that examine the effects of personal attributes on\r\ndecision-making, while controlling for the conditions above.",
-            "modified": "2009-02-03T14:51:36",
-            "accessLevel": "restricted public",
-            "identifier": "2234",
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
+            "title": "Uniform Crime Reporting Program Data [United States]:  Police Employee (LEOKA) Data, 1999    "
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
+            "description": "This project orignally was undertaken to compile a definitive\r\ndatabase on the personal, social, economic, career, and political\r\nattributes of judges who served on the United States Courts of Appeals from\r\n1801 to 1994 - it has now been updated to include information through the year 2000. The database includes conventional social background\r\nvariables such as appointing president, religion, political party\r\naffiliation, education, and prior experience. In addition, unique items are\r\nprovided: the temporal sequence of prior career experiences, the\r\ntiming of and reason for leaving the bench, gender, race and ethnicity,\r\nposition numbering analogous to the scheme used for the Supreme Court,\r\nAmerican Bar Association rating, and net worth (for judges who began\r\nservice on the bench after 1978). The second objective of this project\r\nwas to merge\r\nthese data with a multi-user database on United States Courts of Appeals decisions\r\nthat is headed by Donald Songer and funded by the National Science\r\nFoundation. That database includes a unique identification number\r\nfor each judge participating in a particular decision. The combined\r\ndatabases\r\nshould enable scholars to explore: (1) intra- and inter-circuit fluctuation\r\nin the distribution of social background characteristics, (2) generational\r\nand presidential cohort variation in these attributes, and (3) state\r\nand partisan control of seats. The collection also facilitates the\r\nconstruction of models that examine the effects of personal attributes on\r\ndecision-making, while controlling for the conditions above.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR06796.v2",
+                    "title": "Multi-User Database on the Attributes of United States Appeals Court Judges, 1801-2000"
+                }
+            ],
+            "identifier": "2234",
+            "issued": "1997-01-09T00:00:00",
             "keyword": [
                 "appellate courts",
                 "biographical data",
@@ -52572,54 +52565,55 @@
                 "religious behavior",
                 "social history"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2009-02-03T14:51:36",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "1997-01-09T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR06796.v2",
-                    "title": "Multi-User Database on the Attributes of United States Appeals Court Judges, 1801-2000"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data [United States]:  County-Level Detailed Arrest and Offense Data, 1995",
-            "description": "This data collection contains county-level counts of\r\n arrests and offenses for Part I offenses (murder, rape, robbery,\r\n aggravated assault, burglary, larceny, auto theft, and arson) and Part\r\n II offenses (forgery, fraud, embezzlement, vandalism, weapons\r\n violations, sex offenses, drug and alcohol abuse violations, gambling,\r\nvagrancy, curfew violations, and runaways).",
-            "modified": "2006-03-30T00:00:00",
-            "accessLevel": "public",
-            "identifier": "2235",
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
+            "title": "Multi-User Database on the Attributes of United States Appeals Court Judges, 1801-2000"
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
+            "description": "This data collection contains county-level counts of\r\n arrests and offenses for Part I offenses (murder, rape, robbery,\r\n aggravated assault, burglary, larceny, auto theft, and arson) and Part\r\n II offenses (forgery, fraud, embezzlement, vandalism, weapons\r\n violations, sex offenses, drug and alcohol abuse violations, gambling,\r\nvagrancy, curfew violations, and runaways).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR06850.v2",
+                    "title": "Uniform Crime Reporting Program Data [United States]:  County-Level Detailed Arrest and Offense Data, 1995"
+                }
+            ],
+            "identifier": "2235",
+            "isPartOf": "2167",
+            "issued": "1997-05-30T00:00:00",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -52643,54 +52637,54 @@
                 "sex offenses",
                 "vandalism"
             ],
-            "bureauCode": [
-                "011:21"
-            ],
-            "programCode": [
-                "011:061"
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "1997-05-30T00:00:00",
             "language": [
                 "eng"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR06850.v2",
-                    "title": "Uniform Crime Reporting Program Data [United States]:  County-Level Detailed Arrest and Offense Data, 1995"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "United Nations World Crime Surveys:  Fourth Survey, 1986-1990",
-            "description": "The Fourth United Nations Survey, covering the years\r\n1986-1990, was designed to increase knowledge regarding the incidence\r\nof reported crime and the structure of criminal justice systems, as a\r\nbasis for improving the international exchange of information. The\r\nmain objectives of the survey were to determine which data are\r\ngenerally available in national databases and to provide an instrument\r\nfor strengthening cooperation among member states of the United Nations\r\nby putting the review and analysis of national crime-related data in a\r\nbroader context. Variables describe combined police and\r\nprosecution expenditure by year and by country, number of police\r\npersonnel by gender, total number of homicides by country and by city,\r\nnumber of assaults, rapes, robberies, thefts, burglaries, frauds, and\r\nembezzlements, amount of drug crime, number of people formally charged with\r\ncrime, age of suspects, number and gender of prosecutors,\r\nnumber of individuals prosecuted and the types of crimes prosecuted for, gender\r\nand age of individuals prosecuted, types of courts, number of\r\nindividuals convicted and acquitted, numbers sentenced to capital\r\npunishment and to various other punishments, number of convictions\r\non various charges, number of individuals sentenced and in detention,\r\nnumber of prisoners, sentence lengths, and prison demographics.",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "modified": "2006-03-30T00:00:00",
-            "accessLevel": "public",
-            "identifier": "2236",
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
+            "title": "Uniform Crime Reporting Program Data [United States]:  County-Level Detailed Arrest and Offense Data, 1995"
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
+            "description": "The Fourth United Nations Survey, covering the years\r\n1986-1990, was designed to increase knowledge regarding the incidence\r\nof reported crime and the structure of criminal justice systems, as a\r\nbasis for improving the international exchange of information. The\r\nmain objectives of the survey were to determine which data are\r\ngenerally available in national databases and to provide an instrument\r\nfor strengthening cooperation among member states of the United Nations\r\nby putting the review and analysis of national crime-related data in a\r\nbroader context. Variables describe combined police and\r\nprosecution expenditure by year and by country, number of police\r\npersonnel by gender, total number of homicides by country and by city,\r\nnumber of assaults, rapes, robberies, thefts, burglaries, frauds, and\r\nembezzlements, amount of drug crime, number of people formally charged with\r\ncrime, age of suspects, number and gender of prosecutors,\r\nnumber of individuals prosecuted and the types of crimes prosecuted for, gender\r\nand age of individuals prosecuted, types of courts, number of\r\nindividuals convicted and acquitted, numbers sentenced to capital\r\npunishment and to various other punishments, number of convictions\r\non various charges, number of individuals sentenced and in detention,\r\nnumber of prisoners, sentence lengths, and prison demographics.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR06945.v1",
+                    "title": "United Nations World Crime Surveys:  Fourth Survey, 1986-1990"
+                }
+            ],
+            "identifier": "2236",
+            "isPartOf": "2437",
+            "issued": "1997-09-11T00:00:00",
             "keyword": [
                 "United Nations",
                 "acquittals",
@@ -52726,54 +52720,54 @@
                 "sentencing",
                 "trends"
             ],
-            "bureauCode": [
-                "011:21"
-            ],
-            "programCode": [
-                "011:061"
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2437",
-            "dataQuality": false,
-            "issued": "1997-09-11T00:00:00",
             "language": [
                 "eng"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR06945.v1",
-                    "title": "United Nations World Crime Surveys:  Fourth Survey, 1986-1990"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "United States Supreme Court Judicial Database, Phase II:  1953-1993",
-            "description": "The purpose of this data collection was to record\r\n information about the cases, litigants, amicus participants, and the\r\n opinions decided by the Supreme Court under the tenure of Chief\r\n Justices Earl Warren (1953-1969) and Warren Burger (1969-1986) and\r\n others through 1993. The approach of this study was to proceed\r\n deductively, rather than seek to infer values of a particular group of\r\n justices. This method allows the investigation of value conflicts that\r\n are not litigated, as well as the value conflicts represented in\r\n Supreme Court opinions. Opinions are coded on the basis of their\r\n literal content, and the data are organized around the opinions. There\r\n are eight types of opinions. Within each type, up to six topics are\r\n coded, and within each topic, up to two values are coded. There are\r\n three integrated parts to this study, each of which can be linked to\r\n the other files by specific variables. Part 1, Supreme Court Database,\r\n contains basic case attributes from UNITED STATES SUPREME COURT\r\n JUDICIAL DATABASE, 1953-1993 TERMS (ICPSR 9422) and the opinions given\r\n in the cases.  Part 2, Briefs, gives information on the filers and\r\n co-filers for cases in which amicus curie briefs were filed. Part 3,\r\n Groups, lists the litigants' names. The distinct aspects of the\r\n Court's decisions are covered by six types of variables in Part 1: (1)\r\n identification variables including case citation, docket number, unit\r\n of analysis, and number of records per unit of analysis, (2)\r\n background variables offering information on origin of case, source of\r\n case, reason for granting cert, parties to the case, direction of the\r\n lower court's decision, and manner in which the Court takes\r\n jurisdiction, (3) chronological variables covering date of term of\r\n court, chief justice, and natural court, (4) substantive variables\r\n including multiple legal provisions, authority for decision, issue,\r\n issue areas, and direction of decision, (5) outcome variables\r\n supplying information on form of decision, disposition of case,\r\n winning party, declaration of unconstitutionality, and multiple\r\n memorandum decisions, and (6) voting and opinion variables pertaining\r\n to the vote in the case and to the direction of the individual\r\njustices' votes.",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "modified": "2006-03-30T00:00:00",
-            "accessLevel": "public",
-            "identifier": "2237",
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
+            "title": "United Nations World Crime Surveys:  Fourth Survey, 1986-1990"
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
+            "description": "The purpose of this data collection was to record\r\n information about the cases, litigants, amicus participants, and the\r\n opinions decided by the Supreme Court under the tenure of Chief\r\n Justices Earl Warren (1953-1969) and Warren Burger (1969-1986) and\r\n others through 1993. The approach of this study was to proceed\r\n deductively, rather than seek to infer values of a particular group of\r\n justices. This method allows the investigation of value conflicts that\r\n are not litigated, as well as the value conflicts represented in\r\n Supreme Court opinions. Opinions are coded on the basis of their\r\n literal content, and the data are organized around the opinions. There\r\n are eight types of opinions. Within each type, up to six topics are\r\n coded, and within each topic, up to two values are coded. There are\r\n three integrated parts to this study, each of which can be linked to\r\n the other files by specific variables. Part 1, Supreme Court Database,\r\n contains basic case attributes from UNITED STATES SUPREME COURT\r\n JUDICIAL DATABASE, 1953-1993 TERMS (ICPSR 9422) and the opinions given\r\n in the cases.  Part 2, Briefs, gives information on the filers and\r\n co-filers for cases in which amicus curie briefs were filed. Part 3,\r\n Groups, lists the litigants' names. The distinct aspects of the\r\n Court's decisions are covered by six types of variables in Part 1: (1)\r\n identification variables including case citation, docket number, unit\r\n of analysis, and number of records per unit of analysis, (2)\r\n background variables offering information on origin of case, source of\r\n case, reason for granting cert, parties to the case, direction of the\r\n lower court's decision, and manner in which the Court takes\r\n jurisdiction, (3) chronological variables covering date of term of\r\n court, chief justice, and natural court, (4) substantive variables\r\n including multiple legal provisions, authority for decision, issue,\r\n issue areas, and direction of decision, (5) outcome variables\r\n supplying information on form of decision, disposition of case,\r\n winning party, declaration of unconstitutionality, and multiple\r\n memorandum decisions, and (6) voting and opinion variables pertaining\r\n to the vote in the case and to the direction of the individual\r\njustices' votes.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR06987.v1",
+                    "title": "United States Supreme Court Judicial Database, Phase II:  1953-1993"
+                }
+            ],
+            "identifier": "2237",
+            "isPartOf": "2428",
+            "issued": "1997-12-11T00:00:00",
             "keyword": [
                 "Supreme Court decisions",
                 "Supreme Court justices",
@@ -52786,54 +52780,54 @@
                 "legal history",
                 "twentieth century"
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
-            "isPartOf": "2428",
-            "dataQuality": false,
-            "issued": "1997-12-11T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR06987.v1",
-                    "title": "United States Supreme Court Judicial Database, Phase II:  1953-1993"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Court Cases, 1962-1964",
-            "description": "This study collected data from both civil and criminal\r\n federal cases tried in the fiscal years 1962-1963 and\r\n 1963-1964. Procedural, jurisdictional, and other legal information is\r\nprovided, including the disposition of each case.",
-            "modified": "2011-04-14T10:21:25",
-            "accessLevel": "public",
-            "identifier": "2238",
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
+            "title": "United States Supreme Court Judicial Database, Phase II:  1953-1993"
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
+            "description": "This study collected data from both civil and criminal\r\n federal cases tried in the fiscal years 1962-1963 and\r\n 1963-1964. Procedural, jurisdictional, and other legal information is\r\nprovided, including the disposition of each case.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR07245.v1",
+                    "title": "Federal Court Cases, 1962-1964"
+                }
+            ],
+            "identifier": "2238",
+            "isPartOf": "2173",
+            "issued": "1984-05-03T00:00:00",
             "keyword": [
                 "administration",
                 "appellate courts",
@@ -52852,54 +52846,54 @@
                 "trial courts",
                 "trial procedures"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-04-14T10:21:25",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2173",
-            "dataQuality": false,
-            "issued": "1984-05-03T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR07245.v1",
-                    "title": "Federal Court Cases, 1962-1964"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data: Arson, United States, 2011",
-            "description": "Since 1930, the Federal Bureau of Investigation has\r\ncompiled the Uniform Crime Reports (UCR) to serve as periodic\r\nnationwide assessments of reported crimes not available elsewhere in\r\nthe criminal justice system. Seven main classifications of crime were\r\nchosen to gauge fluctuations in the overall volume and rate of\r\ncrime. These seven classifications that eventually became known as the\r\nCrime Index included the violent crimes of murder and non-negligent\r\nmanslaughter, forcible rape, robbery, and aggravated assault, and the\r\nproperty crimes of burglary, larceny-theft, and motor vehicle theft.\r\nBy congressional mandate, arson was added as the eighth Index offense\r\nin 1979. Arson is defined as any willful or malicious burning or\r\nattempt to burn, with or without intent to defraud, a dwelling house,\r\npublic building, motor vehicle or aircraft, personal property of\r\nanother, etc. The arson data files include monthly data on the number\r\nof arson offenses reported and the number of offenses cleared by\r\narrest or other means. The counts include all reports of arson\r\nreceived from victims, officers who discovered infractions, or other\r\nsources.",
-            "modified": "2014-01-24T14:42:10",
-            "accessLevel": "public",
-            "identifier": "2239",
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
+            "title": "Federal Court Cases, 1962-1964"
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
+            "description": "Since 1930, the Federal Bureau of Investigation has\r\ncompiled the Uniform Crime Reports (UCR) to serve as periodic\r\nnationwide assessments of reported crimes not available elsewhere in\r\nthe criminal justice system. Seven main classifications of crime were\r\nchosen to gauge fluctuations in the overall volume and rate of\r\ncrime. These seven classifications that eventually became known as the\r\nCrime Index included the violent crimes of murder and non-negligent\r\nmanslaughter, forcible rape, robbery, and aggravated assault, and the\r\nproperty crimes of burglary, larceny-theft, and motor vehicle theft.\r\nBy congressional mandate, arson was added as the eighth Index offense\r\nin 1979. Arson is defined as any willful or malicious burning or\r\nattempt to burn, with or without intent to defraud, a dwelling house,\r\npublic building, motor vehicle or aircraft, personal property of\r\nanother, etc. The arson data files include monthly data on the number\r\nof arson offenses reported and the number of offenses cleared by\r\narrest or other means. The counts include all reports of arson\r\nreceived from victims, officers who discovered infractions, or other\r\nsources.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR34579.v1",
+                    "title": "Uniform Crime Reporting Program Data: Arson, United States, 2011"
+                }
+            ],
+            "identifier": "2239",
+            "isPartOf": "2167",
+            "issued": "2014-01-24T14:42:10",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -52910,54 +52904,54 @@
                 "law enforcement",
                 "offenses"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2014-01-24T14:42:10",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2014-01-24T14:42:10",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR34579.v1",
-                    "title": "Uniform Crime Reporting Program Data: Arson, United States, 2011"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data: Arrests by Age, Sex, and Race, United States, 2011",
-            "description": "These data provide information on the number of arrests reported to the Federal Bureau of Investigation's (FBI) Uniform Crime Reporting (UCR) Program each month by police agencies in the United States. Although not as well known as the ''Crimes Known to the Police'' data drawn from the Uniform Crime Report's Return A form, the arrest reports by age, sex, and race provide valuable data on 43 offenses including violent, drug, gambling, and larceny crimes. The data received by ICPSR were structured as a hierarchical file containing (per reporting police agency) an agency header record, and 1 to 12 monthly header reports, and 1 to 43 detail offense records containing the counts of arrests by age, sex, and race for a particular offense. ICPSR restructured the original data to a rectangular format.",
-            "modified": "2013-07-17T13:56:22",
-            "accessLevel": "public",
-            "identifier": "2240",
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
+            "title": "Uniform Crime Reporting Program Data: Arson, United States, 2011"
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
+            "description": "These data provide information on the number of arrests reported to the Federal Bureau of Investigation's (FBI) Uniform Crime Reporting (UCR) Program each month by police agencies in the United States. Although not as well known as the ''Crimes Known to the Police'' data drawn from the Uniform Crime Report's Return A form, the arrest reports by age, sex, and race provide valuable data on 43 offenses including violent, drug, gambling, and larceny crimes. The data received by ICPSR were structured as a hierarchical file containing (per reporting police agency) an agency header record, and 1 to 12 monthly header reports, and 1 to 43 detail offense records containing the counts of arrests by age, sex, and race for a particular offense. ICPSR restructured the original data to a rectangular format.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR34580.v1",
+                    "title": "Uniform Crime Reporting Program Data: Arrests by Age, Sex, and Race, United States, 2011"
+                }
+            ],
+            "identifier": "2240",
+            "isPartOf": "2167",
+            "issued": "2013-07-17T13:56:22",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -52982,54 +52976,54 @@
                 "vandalism",
                 "weapons"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-07-17T13:56:22",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2013-07-17T13:56:22",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR34580.v1",
-                    "title": "Uniform Crime Reporting Program Data: Arrests by Age, Sex, and Race, United States, 2011"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data: Arrests by Age, Sex, and Race, Summarized Yearly, United States, 2011",
-            "description": "These data provide information on the number of arrests\r\nreported to the Federal Bureau of Investigation's Uniform Crime\r\nReporting (UCR) Program each year by police agencies in the United\r\nStates. These arrest reports provide data on 43 offenses including\r\nviolent crime, drug use, gambling, and larceny. The data received by\r\nICPSR were structured as a hierarchical file containing, per reporting\r\npolice agency: an agency header record, and 1 to 43 detail offense\r\nrecords containing the counts of arrests by age, sex, and race for a\r\nparticular offense. ICPSR restructured the original data to logical\r\nrecord length format with the agency header record variables copied\r\nonto the detail records. Consequently, each record contains arrest\r\ncounts for a particular agency-offense.",
-            "modified": "2013-07-17T13:51:12",
-            "accessLevel": "public",
-            "identifier": "2241",
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
+            "title": "Uniform Crime Reporting Program Data: Arrests by Age, Sex, and Race, United States, 2011"
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
+            "description": "These data provide information on the number of arrests\r\nreported to the Federal Bureau of Investigation's Uniform Crime\r\nReporting (UCR) Program each year by police agencies in the United\r\nStates. These arrest reports provide data on 43 offenses including\r\nviolent crime, drug use, gambling, and larceny. The data received by\r\nICPSR were structured as a hierarchical file containing, per reporting\r\npolice agency: an agency header record, and 1 to 43 detail offense\r\nrecords containing the counts of arrests by age, sex, and race for a\r\nparticular offense. ICPSR restructured the original data to logical\r\nrecord length format with the agency header record variables copied\r\nonto the detail records. Consequently, each record contains arrest\r\ncounts for a particular agency-offense.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR34581.v1",
+                    "title": "Uniform Crime Reporting Program Data: Arrests by Age, Sex, and Race, Summarized Yearly, United States, 2011"
+                }
+            ],
+            "identifier": "2241",
+            "isPartOf": "2167",
+            "issued": "2013-07-17T13:51:12",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrest records",
@@ -53045,54 +53039,54 @@
                 "offenses",
                 "violent crime"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-07-17T13:51:12",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2013-07-17T13:51:12",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR34581.v1",
-                    "title": "Uniform Crime Reporting Program Data: Arrests by Age, Sex, and Race, Summarized Yearly, United States, 2011"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data: Hate Crime Data, 2011 [Record-Type Files]",
-            "description": "In response to a growing concern about hate crimes, the\r\nUnited States Congress enacted the Hate Crime Statistics Act of\r\n1990. The Act requires the attorney general to establish guidelines\r\nand collect, as part of the Uniform Crime Reporting (UCR) Program,\r\ndata \"about crimes that manifest evidence of prejudice based on race,\r\nreligion, sexual orientation, or ethnicity, including where\r\nappropriate the crimes of murder and non-negligent manslaughter,\r\nforcible rape, aggravated assault, simple assault, intimidation,\r\narson, and destruction, damage or vandalism of property.\" Hate crime\r\ndata collection was required by the Act to begin in calendar year 1990\r\nand to continue for four successive years. In September 1994, the\r\nViolent Crime Control and Law Enforcement Act amended the Hate Crime\r\nStatistics Act to add disabilities, both physical and mental, as\r\nfactors that could be considered a basis for hate crimes. Although the\r\nAct originally mandated data collection for five years, the Church\r\nArson Prevention Act of 1996 amended the collection duration \"for each\r\ncalendar year,\" making hate crime statistics a permanent addition to\r\nthe UCR program. As with the other UCR data, law enforcement agencies\r\ncontribute reports either directly or through their state reporting\r\nprograms. Information contained in the data includes number of victims\r\nand offenders involved in each hate crime incident, type of victims,\r\nbias motivation, offense type, and location type.",
-            "modified": "2013-07-17T11:03:44",
-            "accessLevel": "public",
-            "identifier": "2242",
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
+            "title": "Uniform Crime Reporting Program Data: Arrests by Age, Sex, and Race, Summarized Yearly, United States, 2011"
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
+            "description": "In response to a growing concern about hate crimes, the\r\nUnited States Congress enacted the Hate Crime Statistics Act of\r\n1990. The Act requires the attorney general to establish guidelines\r\nand collect, as part of the Uniform Crime Reporting (UCR) Program,\r\ndata \"about crimes that manifest evidence of prejudice based on race,\r\nreligion, sexual orientation, or ethnicity, including where\r\nappropriate the crimes of murder and non-negligent manslaughter,\r\nforcible rape, aggravated assault, simple assault, intimidation,\r\narson, and destruction, damage or vandalism of property.\" Hate crime\r\ndata collection was required by the Act to begin in calendar year 1990\r\nand to continue for four successive years. In September 1994, the\r\nViolent Crime Control and Law Enforcement Act amended the Hate Crime\r\nStatistics Act to add disabilities, both physical and mental, as\r\nfactors that could be considered a basis for hate crimes. Although the\r\nAct originally mandated data collection for five years, the Church\r\nArson Prevention Act of 1996 amended the collection duration \"for each\r\ncalendar year,\" making hate crime statistics a permanent addition to\r\nthe UCR program. As with the other UCR data, law enforcement agencies\r\ncontribute reports either directly or through their state reporting\r\nprograms. Information contained in the data includes number of victims\r\nand offenders involved in each hate crime incident, type of victims,\r\nbias motivation, offense type, and location type.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR34583.v1",
+                    "title": "Uniform Crime Reporting Program Data: Hate Crime Data, 2011 [Record-Type Files]"
+                }
+            ],
+            "identifier": "2242",
+            "isPartOf": "2167",
+            "issued": "2013-07-17T11:03:44",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -53111,54 +53105,54 @@
                 "religion",
                 "violence"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-07-17T11:03:44",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2013-07-17T11:03:44",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR34583.v1",
-                    "title": "Uniform Crime Reporting Program Data: Hate Crime Data, 2011 [Record-Type Files]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data: Police Employee (LEOKA) Data, 2011",
-            "description": "The Uniform Crime Reporting Program Data, Police Employee Data, 2011 file contains monthly data on felonious or accidental killings and assaults upon United States law enforcement officers acting in the line of duty. The Federal Bureau of Investigation (FBI) assembled the data and processed them from UCR Master Police Employee (LEOKA) data tapes.\r\nEach agency record included in the file includes the following summary variables: state code, population group code, geographic division, Metropolitan Statistical Area code, and agency name. These variables afford considerable flexibility in creating subsets or aggregations of the data.\r\nSince 1930, the Federal Bureau of Investigation has compiled the Uniform Crime Reports (UCR) to serve as a periodic nationwide assessment of reported crimes not available elsewhere in the criminal justice system. Each year, this information is reported in four types of files: (1) Offenses Known and Clearances by Arrest, (2) Property Stolen and Recovered, (3) Supplementary Homicide Reports (SHR), and (4) Police Employee (LEOKA) Data. The Police Employee (LEOKA) Data provide information about law enforcement officers killed or assaulted (hence the acronym, LEOKA) in the line of duty. The variables created from the LEOKA forms provide in-depth information on the circumstances surrounding killings or assaults, including type of call answered, type of weapon used, and type of patrol the officers were on.",
-            "modified": "2013-05-02T15:26:14",
-            "accessLevel": "public",
-            "identifier": "2243",
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
+            "title": "Uniform Crime Reporting Program Data: Hate Crime Data, 2011 [Record-Type Files]"
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
+            "description": "The Uniform Crime Reporting Program Data, Police Employee Data, 2011 file contains monthly data on felonious or accidental killings and assaults upon United States law enforcement officers acting in the line of duty. The Federal Bureau of Investigation (FBI) assembled the data and processed them from UCR Master Police Employee (LEOKA) data tapes.\r\nEach agency record included in the file includes the following summary variables: state code, population group code, geographic division, Metropolitan Statistical Area code, and agency name. These variables afford considerable flexibility in creating subsets or aggregations of the data.\r\nSince 1930, the Federal Bureau of Investigation has compiled the Uniform Crime Reports (UCR) to serve as a periodic nationwide assessment of reported crimes not available elsewhere in the criminal justice system. Each year, this information is reported in four types of files: (1) Offenses Known and Clearances by Arrest, (2) Property Stolen and Recovered, (3) Supplementary Homicide Reports (SHR), and (4) Police Employee (LEOKA) Data. The Police Employee (LEOKA) Data provide information about law enforcement officers killed or assaulted (hence the acronym, LEOKA) in the line of duty. The variables created from the LEOKA forms provide in-depth information on the circumstances surrounding killings or assaults, including type of call answered, type of weapon used, and type of patrol the officers were on.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR34584.v1",
+                    "title": "Uniform Crime Reporting Program Data: Police Employee (LEOKA) Data, 2011"
+                }
+            ],
+            "identifier": "2243",
+            "isPartOf": "2167",
+            "issued": "2013-05-02T15:26:14",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -53171,54 +53165,54 @@
                 "police deaths",
                 "police officers"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-05-02T15:26:14",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2013-05-02T15:26:14",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR34584.v1",
-                    "title": "Uniform Crime Reporting Program Data: Police Employee (LEOKA) Data, 2011"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data: National Incident-Based Reporting System, 2011",
-            "description": "The National Incident-Based Reporting System (NIBRS) is a\r\npart of the Uniform Crime Reporting Program (UCR), administered by the\r\nFederal Bureau of Investigation (FBI). In the late 1970s, the law\r\nenforcement community called for a thorough evaluative study of the\r\nUCR with the objective of recommending an expanded and enhanced UCR\r\nprogram to meet law enforcement needs into the 21st century. The FBI\r\nfully concurred with the need for an updated program to meet\r\ncontemporary needs and provided its support, formulating a\r\ncomprehensive redesign effort. Following a multiyear study, a\r\n\"Blueprint for the Future of the Uniform Crime Reporting Program\" was\r\ndeveloped. Using the \"Blueprint,\" and in consultation with local and\r\nstate law enforcement executives, the FBI formulated new guidelines\r\nfor the Uniform Crime Reports. The National Incident-Based Reporting\r\nSystem (NIBRS) was implemented to meet these guidelines. NIBRS data\r\nare archived at ICPSR as 13 separate data files per year, which may be\r\nmerged by using linkage variables. The data focus on a variety of\r\naspects of a crime incident. Part 4, Administrative Segment, offers\r\ndata on the incident itself (date and time). Each crime incident is\r\ndelineated by one administrative segment record. Also provided are\r\nPart 5, Offense Segment (offense type, location, weapon use, and bias\r\nmotivation), Part 6, Property Segment (type of property loss, property\r\ndescription, property value, drug type and quantity), Part 7, Victim\r\nSegment (age, sex, race, ethnicity, and injuries), Part 8, Offender\r\nSegment (age, sex, and race), and Part 9, Arrestee Segment (arrest\r\ndate, age, sex, race, and weapon use). The Batch Header Segment (Parts\r\n1-3) separates and identifies individual police agencies by\r\nOriginating Agency Identifier (ORI). Batch Header information, which\r\nis contained on three records for each ORI, includes agency name,\r\ngeographic location, and population of the area. Part 10, Group B\r\nArrest Report Segment, includes arrestee data for Group B crimes.\r\nWindow Segments files (Parts 11-13) pertain to incidents for which the\r\ncomplete Group A Incident Report was not submitted to the FBI. In\r\ngeneral, a Window Segment record will be generated if the incident\r\noccurred prior to January 1 of the previous year or if the incident\r\noccurred prior to when the agency started NIBRS reporting. As with the\r\nUCR, participation in NIBRS is voluntary on the part of law\r\nenforcement agencies. The data are not a representative sample of\r\ncrime in the United States.",
-            "modified": "2013-09-05T14:04:39",
-            "accessLevel": "public",
-            "identifier": "2244",
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
+            "title": "Uniform Crime Reporting Program Data: Police Employee (LEOKA) Data, 2011"
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
+            "description": "The National Incident-Based Reporting System (NIBRS) is a\r\npart of the Uniform Crime Reporting Program (UCR), administered by the\r\nFederal Bureau of Investigation (FBI). In the late 1970s, the law\r\nenforcement community called for a thorough evaluative study of the\r\nUCR with the objective of recommending an expanded and enhanced UCR\r\nprogram to meet law enforcement needs into the 21st century. The FBI\r\nfully concurred with the need for an updated program to meet\r\ncontemporary needs and provided its support, formulating a\r\ncomprehensive redesign effort. Following a multiyear study, a\r\n\"Blueprint for the Future of the Uniform Crime Reporting Program\" was\r\ndeveloped. Using the \"Blueprint,\" and in consultation with local and\r\nstate law enforcement executives, the FBI formulated new guidelines\r\nfor the Uniform Crime Reports. The National Incident-Based Reporting\r\nSystem (NIBRS) was implemented to meet these guidelines. NIBRS data\r\nare archived at ICPSR as 13 separate data files per year, which may be\r\nmerged by using linkage variables. The data focus on a variety of\r\naspects of a crime incident. Part 4, Administrative Segment, offers\r\ndata on the incident itself (date and time). Each crime incident is\r\ndelineated by one administrative segment record. Also provided are\r\nPart 5, Offense Segment (offense type, location, weapon use, and bias\r\nmotivation), Part 6, Property Segment (type of property loss, property\r\ndescription, property value, drug type and quantity), Part 7, Victim\r\nSegment (age, sex, race, ethnicity, and injuries), Part 8, Offender\r\nSegment (age, sex, and race), and Part 9, Arrestee Segment (arrest\r\ndate, age, sex, race, and weapon use). The Batch Header Segment (Parts\r\n1-3) separates and identifies individual police agencies by\r\nOriginating Agency Identifier (ORI). Batch Header information, which\r\nis contained on three records for each ORI, includes agency name,\r\ngeographic location, and population of the area. Part 10, Group B\r\nArrest Report Segment, includes arrestee data for Group B crimes.\r\nWindow Segments files (Parts 11-13) pertain to incidents for which the\r\ncomplete Group A Incident Report was not submitted to the FBI. In\r\ngeneral, a Window Segment record will be generated if the incident\r\noccurred prior to January 1 of the previous year or if the incident\r\noccurred prior to when the agency started NIBRS reporting. As with the\r\nUCR, participation in NIBRS is voluntary on the part of law\r\nenforcement agencies. The data are not a representative sample of\r\ncrime in the United States.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR34585.v1",
+                    "title": "Uniform Crime Reporting Program Data: National Incident-Based Reporting System, 2011"
+                }
+            ],
+            "identifier": "2244",
+            "isPartOf": "2433",
+            "issued": "2013-09-05T14:04:39",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -53233,54 +53227,54 @@
                 "victims",
                 "violent crime"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-09-05T14:04:39",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2433",
-            "dataQuality": false,
-            "issued": "2013-09-05T14:04:39",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR34585.v1",
-                    "title": "Uniform Crime Reporting Program Data: National Incident-Based Reporting System, 2011"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data: Offenses Known and Clearances by Arrest, 2011",
-            "description": "The UNIFORM CRIME REPORTING PROGRAM DATA: OFFENSES KNOWN AND CLEARANCES BY ARREST, 2011 dataset is a compilation of offenses reported to law enforcement agencies in the United States. Due to the vast number of categories of crime committed in the United States, the FBI has limited the type of crimes included in this compilation to those crimes which people are most likely to report to police and those crimes which occur frequently enough to be analyzed across time. Crimes included are criminal homicide, forcible rape, robbery, aggravated assault, burglary, larceny-theft, and motor vehicle theft.\r\nMuch information about these crimes is provided in this dataset. The number of times an offense has been reported, the number of reported offenses that have been cleared by arrests, and the number of cleared offenses which involved offenders under the age of 18 are the major items of information collected.",
-            "modified": "2013-04-26T10:36:55",
-            "accessLevel": "public",
-            "identifier": "2245",
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
+            "title": "Uniform Crime Reporting Program Data: National Incident-Based Reporting System, 2011"
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
+            "description": "The UNIFORM CRIME REPORTING PROGRAM DATA: OFFENSES KNOWN AND CLEARANCES BY ARREST, 2011 dataset is a compilation of offenses reported to law enforcement agencies in the United States. Due to the vast number of categories of crime committed in the United States, the FBI has limited the type of crimes included in this compilation to those crimes which people are most likely to report to police and those crimes which occur frequently enough to be analyzed across time. Crimes included are criminal homicide, forcible rape, robbery, aggravated assault, burglary, larceny-theft, and motor vehicle theft.\r\nMuch information about these crimes is provided in this dataset. The number of times an offense has been reported, the number of reported offenses that have been cleared by arrests, and the number of cleared offenses which involved offenders under the age of 18 are the major items of information collected.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR34586.v1",
+                    "title": "Uniform Crime Reporting Program Data: Offenses Known and Clearances by Arrest, 2011"
+                }
+            ],
+            "identifier": "2245",
+            "isPartOf": "2167",
+            "issued": "2013-04-26T10:36:55",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -53290,54 +53284,54 @@
                 "law enforcement",
                 "offenses"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-04-26T10:36:55",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2013-04-26T10:36:55",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR34586.v1",
-                    "title": "Uniform Crime Reporting Program Data: Offenses Known and Clearances by Arrest, 2011"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data: Property Stolen and Recovered, 2011",
-            "description": "The UNIFORM CRIME REPORTING PROGRAM DATA: PROPERTY STOLEN AND RECOVERED,\r\n2011 file (also known as the Supplement to Return A) is collected at the agency level and includes detailed monthly data on the nature of crime and the value and type of property stolen and recovered incident to each crime. The Return A Supplement requires that a value be established for property stolen and recovered in each Crime Index category except aggravated assault. It is designed to record the value of property stolen and recovered in the following eleven classifications: Currency/notes, Jewelry and Precious Metals, Clothing and Furs, Locally Stolen Motor Vehicles, Office Equipment, Televisions/Radios, Firearms, Household Goods, Consumable Goods, Livestock, and Miscellaneous. The determination of the value of property stolen is an obligation of the investigating officer, and such information is essential to assure the completeness of a law enforcement investigative report on stolen property. The data were originally assembled by the Federal Bureau of Investigation (FBI) from reports submitted by agencies participating in the UCR. The ICPSR file was processed from Return A Supplement files provided by the FBI.",
-            "modified": "2013-08-06T11:10:46",
-            "accessLevel": "public",
-            "identifier": "2246",
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
+            "title": "Uniform Crime Reporting Program Data: Offenses Known and Clearances by Arrest, 2011"
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
+            "description": "The UNIFORM CRIME REPORTING PROGRAM DATA: PROPERTY STOLEN AND RECOVERED,\r\n2011 file (also known as the Supplement to Return A) is collected at the agency level and includes detailed monthly data on the nature of crime and the value and type of property stolen and recovered incident to each crime. The Return A Supplement requires that a value be established for property stolen and recovered in each Crime Index category except aggravated assault. It is designed to record the value of property stolen and recovered in the following eleven classifications: Currency/notes, Jewelry and Precious Metals, Clothing and Furs, Locally Stolen Motor Vehicles, Office Equipment, Televisions/Radios, Firearms, Household Goods, Consumable Goods, Livestock, and Miscellaneous. The determination of the value of property stolen is an obligation of the investigating officer, and such information is essential to assure the completeness of a law enforcement investigative report on stolen property. The data were originally assembled by the Federal Bureau of Investigation (FBI) from reports submitted by agencies participating in the UCR. The ICPSR file was processed from Return A Supplement files provided by the FBI.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR34587.v1",
+                    "title": "Uniform Crime Reporting Program Data: Property Stolen and Recovered, 2011"
+                }
+            ],
+            "identifier": "2246",
+            "isPartOf": "2167",
+            "issued": "2013-08-06T11:10:46",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -53352,54 +53346,54 @@
                 "stolen property",
                 "stolen property recovery"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-08-06T11:10:46",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2013-08-06T11:10:46",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR34587.v1",
-                    "title": "Uniform Crime Reporting Program Data: Property Stolen and Recovered, 2011"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data: Supplementary Homicide Reports, 2011",
-            "description": "The UNIFORM CRIME REPORTING PROGRAM DATA: SUPPLEMENTARY HOMICIDE REPORTS, 2011 (SHR) provide detailed information on criminal homicides reported to the police. These homicides consist of murders; non-negligent killings also called non-negligent manslaughter; and justifiable homicides. UCR Program contributors compile and submit their crime data by one of two means: either directly to the FBI or through their State UCR Programs. State UCR Programs frequently impose mandatory reporting requirements which have been effective in increasing both the number of reporting agencies as well as the number and accuracy of each participating agency's reports. Each agency may be identified by its numeric state code, alpha-numeric agency (\"ORI\") code, jurisdiction population, and population group. In addition, each homicide incident is identified by month of occurrence and situation type, allowing flexibility in creating aggregations and subsets.",
-            "modified": "2013-04-26T10:36:19",
-            "accessLevel": "public",
-            "identifier": "2247",
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
+            "title": "Uniform Crime Reporting Program Data: Property Stolen and Recovered, 2011"
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
+            "description": "The UNIFORM CRIME REPORTING PROGRAM DATA: SUPPLEMENTARY HOMICIDE REPORTS, 2011 (SHR) provide detailed information on criminal homicides reported to the police. These homicides consist of murders; non-negligent killings also called non-negligent manslaughter; and justifiable homicides. UCR Program contributors compile and submit their crime data by one of two means: either directly to the FBI or through their State UCR Programs. State UCR Programs frequently impose mandatory reporting requirements which have been effective in increasing both the number of reporting agencies as well as the number and accuracy of each participating agency's reports. Each agency may be identified by its numeric state code, alpha-numeric agency (\"ORI\") code, jurisdiction population, and population group. In addition, each homicide incident is identified by month of occurrence and situation type, allowing flexibility in creating aggregations and subsets.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR34588.v1",
+                    "title": "Uniform Crime Reporting Program Data: Supplementary Homicide Reports, 2011"
+                }
+            ],
+            "identifier": "2247",
+            "isPartOf": "2167",
+            "issued": "2013-04-26T10:36:19",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -53412,54 +53406,54 @@
                 "offenses",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-04-26T10:36:19",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2013-04-26T10:36:19",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR34588.v1",
-                    "title": "Uniform Crime Reporting Program Data: Supplementary Homicide Reports, 2011"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Electronic Injury Surveillance System All Injury Program, 2010",
-            "description": "Beginning in July 2000, the National Center for Injury\r\nPrevention and Control (NCIPC), and Centers for Disease Control and\r\nPrevention (CDC), in collaboration with the United States Consumer\r\nProduct Safety Commission (CPSC), expanded the National Electronic\r\nInjury Surveillance System (NEISS) to collect data on all types and\r\ncauses of injuries treated in a representative sample of United States\r\nhospitals with emergency departments (ED). This system is called the\r\nNEISS-All Injury Program (NEISS-AIP). The NEISS-AIP is designed to\r\nprovide national incidence estimates of all types and external causes\r\nof nonfatal injuries and poisonings treated in United States hospital\r\nEDs. Data on injury-related visits are being obtained from a national\r\nsample of 66 out of 100 NEISS hospitals that were selected as a\r\nstratified probability sample of hospitals in the United States and\r\nits territories with a minimum of 6 beds and a 24-hour ED. The\r\nsample includes separate strata for very large, large, medium, and\r\nsmall hospitals, defined by the number of annual ED visits per\r\nhospital, and children's hospitals. The scope of reporting goes beyond\r\nroutine reporting of injuries associated with consumer-related\r\nproducts in CPSC's jurisdiction to include all injuries and\r\npoisonings. The data can be used to (1) measure the magnitude and\r\ndistribution of nonfatal injuries in the United States, (2) monitor\r\nunintentional and violence-related nonfatal injuries over time, (3)\r\nidentify emerging injury problems, (4) identify specific cases for\r\nfollow-up investigations of particular injury-related problems, and\r\n(5) set national priorities. A fundamental principle of this expansion\r\neffort is that preliminary surveillance data will be made available in\r\na timely manner to a number of different federal agencies with unique\r\nand overlapping public health responsibilities and concerns. Also,\r\nannually, the final edited data are released as public use data files\r\nfor use by other public health professionals and researchers. NEISS-AIP data on nonfatal injuries were collected from January through December each year except the year 2000 when data were collected from July through December (ICPSR 3582). NEISS AIP is providing data on approximately over 500,000 cases annually. Data obtained on each case include age, race/ethnicity, gender, principal diagnosis, primary body part affected, consumer products involved, disposition at ED discharge (i.e., hospitalized, transferred, treated and released, observation, died), locale where the injury occurred, work-relatedness, and a narrative description of the injury circumstances. Also, major categories of external cause of injury (e.g., motor vehicle, falls, cut/pierce, poisoning, fire/burn) and of intent of injury (e.g., unintentional, assault, intentional self-harm, legal intervention) are being coded for each case in a manner consistent with the International Classification of Diseases, Ninth Revision, Clinical Modification (ICD-9-CM) coding rules and guidelines. NEISS has been managed and operated by the United States Consumer Product Safety Commission since 1972 and is used by the Commission for identifying and monitoring consumer product-related injuries and for assessing risk to all United States residents. These product-related injury data are used for educating consumers about hazardous products and for identifying injury-related cases used in detailed studies of specific products and associated hazard patterns. These studies set the stage for developing both voluntary and mandatory safety standards. Since the early 1980s, CPSC has assisted other federal agencies by using NEISS to collect injury- related data of special interest to them. In 1990, an interagency agreement was established between NCIPC and CPSC to (1) collect NEISS data on nonfatal firearm-related injuries for the CDC Firearm Injury Surveillance Study; (2) publish NEISS data on a variety of injury-related topics, such as in-line skating, firearms, BB and pellet guns, bicycles, boat propellers, personal water craft, and playground injuries; and (3) to address common concerns. CPSC also uses NEISS to collect data on work-related injuries for the National Institute of Occupational Safety and Health (NIOSH), CDC. In 1997, the interagency agreement was modified to conduct the three-month NEISS All Injury Pilot Study at 21 NEISS hospitals (see Quinlan KP, Thompson MP, Annest JL, et al. Expanding the National Electronic Injury Surveillance System to Monitor All Nonfatal Injuries Treated in US Hospital Emergency Departments. Annals Emerg. Med. 1999;34:637-643.) This study demonstrated the feasibility of expanding NEISS to collect data on all injuries. National estimates based on this study indicated product-related injuries that fall into CPSC's jurisdiction accounted for approximately 50 percent of injuries treated in U.S. hospital EDs. The study also indicated that NEISS is a cost-effective system for capturing data on all injuries treated in U.S. hospital EDs. The NEISS-AIP provides an excellent data source for monitoring national estimates of nonfatal injuries over time. Analysis and dissemination of these surveillance data through the ICPSR, and Internet publications will help support NCIPC's mission of reducing all types and causes of injuries in the United States, as well as assist other federal agencies with responsibilities for injury prevention and control.",
-            "modified": "2013-06-07T14:26:20",
-            "accessLevel": "public",
-            "identifier": "2248",
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
+            "title": "Uniform Crime Reporting Program Data: Supplementary Homicide Reports, 2011"
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
+            "description": "Beginning in July 2000, the National Center for Injury\r\nPrevention and Control (NCIPC), and Centers for Disease Control and\r\nPrevention (CDC), in collaboration with the United States Consumer\r\nProduct Safety Commission (CPSC), expanded the National Electronic\r\nInjury Surveillance System (NEISS) to collect data on all types and\r\ncauses of injuries treated in a representative sample of United States\r\nhospitals with emergency departments (ED). This system is called the\r\nNEISS-All Injury Program (NEISS-AIP). The NEISS-AIP is designed to\r\nprovide national incidence estimates of all types and external causes\r\nof nonfatal injuries and poisonings treated in United States hospital\r\nEDs. Data on injury-related visits are being obtained from a national\r\nsample of 66 out of 100 NEISS hospitals that were selected as a\r\nstratified probability sample of hospitals in the United States and\r\nits territories with a minimum of 6 beds and a 24-hour ED. The\r\nsample includes separate strata for very large, large, medium, and\r\nsmall hospitals, defined by the number of annual ED visits per\r\nhospital, and children's hospitals. The scope of reporting goes beyond\r\nroutine reporting of injuries associated with consumer-related\r\nproducts in CPSC's jurisdiction to include all injuries and\r\npoisonings. The data can be used to (1) measure the magnitude and\r\ndistribution of nonfatal injuries in the United States, (2) monitor\r\nunintentional and violence-related nonfatal injuries over time, (3)\r\nidentify emerging injury problems, (4) identify specific cases for\r\nfollow-up investigations of particular injury-related problems, and\r\n(5) set national priorities. A fundamental principle of this expansion\r\neffort is that preliminary surveillance data will be made available in\r\na timely manner to a number of different federal agencies with unique\r\nand overlapping public health responsibilities and concerns. Also,\r\nannually, the final edited data are released as public use data files\r\nfor use by other public health professionals and researchers. NEISS-AIP data on nonfatal injuries were collected from January through December each year except the year 2000 when data were collected from July through December (ICPSR 3582). NEISS AIP is providing data on approximately over 500,000 cases annually. Data obtained on each case include age, race/ethnicity, gender, principal diagnosis, primary body part affected, consumer products involved, disposition at ED discharge (i.e., hospitalized, transferred, treated and released, observation, died), locale where the injury occurred, work-relatedness, and a narrative description of the injury circumstances. Also, major categories of external cause of injury (e.g., motor vehicle, falls, cut/pierce, poisoning, fire/burn) and of intent of injury (e.g., unintentional, assault, intentional self-harm, legal intervention) are being coded for each case in a manner consistent with the International Classification of Diseases, Ninth Revision, Clinical Modification (ICD-9-CM) coding rules and guidelines. NEISS has been managed and operated by the United States Consumer Product Safety Commission since 1972 and is used by the Commission for identifying and monitoring consumer product-related injuries and for assessing risk to all United States residents. These product-related injury data are used for educating consumers about hazardous products and for identifying injury-related cases used in detailed studies of specific products and associated hazard patterns. These studies set the stage for developing both voluntary and mandatory safety standards. Since the early 1980s, CPSC has assisted other federal agencies by using NEISS to collect injury- related data of special interest to them. In 1990, an interagency agreement was established between NCIPC and CPSC to (1) collect NEISS data on nonfatal firearm-related injuries for the CDC Firearm Injury Surveillance Study; (2) publish NEISS data on a variety of injury-related topics, such as in-line skating, firearms, BB and pellet guns, bicycles, boat propellers, personal water craft, and playground injuries; and (3) to address common concerns. CPSC also uses NEISS to collect data on work-related injuries for the National Institute of Occupational Safety and Health (NIOSH), CDC. In 1997, the interagency agreement was modified to conduct the three-month NEISS All Injury Pilot Study at 21 NEISS hospitals (see Quinlan KP, Thompson MP, Annest JL, et al. Expanding the National Electronic Injury Surveillance System to Monitor All Nonfatal Injuries Treated in US Hospital Emergency Departments. Annals Emerg. Med. 1999;34:637-643.) This study demonstrated the feasibility of expanding NEISS to collect data on all injuries. National estimates based on this study indicated product-related injuries that fall into CPSC's jurisdiction accounted for approximately 50 percent of injuries treated in U.S. hospital EDs. The study also indicated that NEISS is a cost-effective system for capturing data on all injuries treated in U.S. hospital EDs. The NEISS-AIP provides an excellent data source for monitoring national estimates of nonfatal injuries over time. Analysis and dissemination of these surveillance data through the ICPSR, and Internet publications will help support NCIPC's mission of reducing all types and causes of injuries in the United States, as well as assist other federal agencies with responsibilities for injury prevention and control.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR34640.v2",
+                    "title": "National Electronic Injury Surveillance System All Injury Program, 2010"
+                }
+            ],
+            "identifier": "2248",
+            "isPartOf": "2438",
+            "issued": "2013-06-04T15:02:25",
             "keyword": [
                 "accidents",
                 "medical care",
@@ -53469,329 +53463,329 @@
                 "public health",
                 "public safety"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-06-07T14:26:20",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2438",
-            "dataQuality": false,
-            "issued": "2013-06-04T15:02:25",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR34640.v2",
-                    "title": "National Electronic Injury Surveillance System All Injury Program, 2010"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Deaths in Custody Reporting Program: Non-standardized Jail Data, 2008",
-            "description": "The Deaths in Custody Reporting Program (DCRP) is an annual data collection conducted by the Bureau of Justice Statistics (BJS). The DCRP began in 2000 under the Death in Custody Reporting Act of 2000 (P.L. 106-297). It is the only national statistical collection that obtains detailed information about deaths in adult correctional facilities. The DCRP collects data on persons dying in state prisons, local jails and in the process of arrest. Each collection is a separate subcollection, but each is under the umbrella of the DCRP collection. The DCRP collects inmate death records from each of the nation's 50 state prison systems and approximately 2,800 local jail jurisdictions. In addition, this program collects records of all deaths occurring during the process of arrest. Data are collected directly from state and local law enforcement agencies.\r\nDeath records include information on decedent personal characteristics (age, race or Hispanic origin, and sex), decedent criminal background (legal status, offense type, and time served), and the death itself (date, time, location, and cause of death, as well as information on the autopsy and medical treatment provided for any illness or disease).\r\nThis data collection represents a single year of DCRP Jails data. The variable names and coding, while similar to other years, have not been standardized across years. The concatenated multi-year versions of the DCRP Jails population data have been edited to correct outliers and other data anomalies. Researchers are encouraged to use the concatenated multi-year data for final jail population data.",
-            "modified": "2016-08-31T10:52:28",
-            "accessLevel": "restricted public",
-            "identifier": "2249",
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
+            "title": "National Electronic Injury Surveillance System All Injury Program, 2010"
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
+            "description": "The Deaths in Custody Reporting Program (DCRP) is an annual data collection conducted by the Bureau of Justice Statistics (BJS). The DCRP began in 2000 under the Death in Custody Reporting Act of 2000 (P.L. 106-297). It is the only national statistical collection that obtains detailed information about deaths in adult correctional facilities. The DCRP collects data on persons dying in state prisons, local jails and in the process of arrest. Each collection is a separate subcollection, but each is under the umbrella of the DCRP collection. The DCRP collects inmate death records from each of the nation's 50 state prison systems and approximately 2,800 local jail jurisdictions. In addition, this program collects records of all deaths occurring during the process of arrest. Data are collected directly from state and local law enforcement agencies.\r\nDeath records include information on decedent personal characteristics (age, race or Hispanic origin, and sex), decedent criminal background (legal status, offense type, and time served), and the death itself (date, time, location, and cause of death, as well as information on the autopsy and medical treatment provided for any illness or disease).\r\nThis data collection represents a single year of DCRP Jails data. The variable names and coding, while similar to other years, have not been standardized across years. The concatenated multi-year versions of the DCRP Jails population data have been edited to correct outliers and other data anomalies. Researchers are encouraged to use the concatenated multi-year data for final jail population data.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR36300.v1",
+                    "title": "Deaths in Custody Reporting Program: Non-standardized Jail Data, 2008"
+                }
+            ],
+            "identifier": "2249",
+            "isPartOf": "2441",
+            "issued": "2016-08-31T10:50:07",
             "keyword": [
                 "correctional facilities",
                 "corrections",
                 "death",
                 "jails"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2016-08-31T10:52:28",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2441",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2016-08-31T10:50:07",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR36300.v1",
-                    "title": "Deaths in Custody Reporting Program: Non-standardized Jail Data, 2008"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Deaths in Custody Reporting Program: Non-standardized Jail Data, 2009",
-            "description": "The Deaths in Custody Reporting Program (DCRP) is an annual data collection conducted by the Bureau of Justice Statistics (BJS). The DCRP began in 2000 under the Death in Custody Reporting Act of 2000 (P.L. 106-297). It is the only national statistical collection that obtains detailed information about deaths in adult correctional facilities. The DCRP collects data on persons dying in state prisons, local jails and in the process of arrest. Each collection is a separate subcollection, but each is under the umbrella of the DCRP collection. The DCRP collects inmate death records from each of the nation's 50 state prison systems and approximately 2,800 local jail jurisdictions. In addition, this program collects records of all deaths occurring during the process of arrest. Data are collected directly from state and local law enforcement agencies.\r\nDeath records include information on decedent personal characteristics (age, race or Hispanic origin, and sex), decedent criminal background (legal status, offense type, and time served), and the death itself (date, time, location, and cause of death, as well as information on the autopsy and medical treatment provided for any illness or disease).\r\nThis data collection represents a single year of DCRP Jails data. The variable names and coding, while similar to other years, have not been standardized across years. The concatenated multi-year versions of the DCRP Jails population data have been edited to correct outliers and other data anomalies. Researchers are encouraged to use the concatenated multi-year data for final jail population data.",
-            "modified": "2016-08-31T10:56:45",
-            "accessLevel": "restricted public",
-            "identifier": "2250",
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
+            "title": "Deaths in Custody Reporting Program: Non-standardized Jail Data, 2008"
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
+            "description": "The Deaths in Custody Reporting Program (DCRP) is an annual data collection conducted by the Bureau of Justice Statistics (BJS). The DCRP began in 2000 under the Death in Custody Reporting Act of 2000 (P.L. 106-297). It is the only national statistical collection that obtains detailed information about deaths in adult correctional facilities. The DCRP collects data on persons dying in state prisons, local jails and in the process of arrest. Each collection is a separate subcollection, but each is under the umbrella of the DCRP collection. The DCRP collects inmate death records from each of the nation's 50 state prison systems and approximately 2,800 local jail jurisdictions. In addition, this program collects records of all deaths occurring during the process of arrest. Data are collected directly from state and local law enforcement agencies.\r\nDeath records include information on decedent personal characteristics (age, race or Hispanic origin, and sex), decedent criminal background (legal status, offense type, and time served), and the death itself (date, time, location, and cause of death, as well as information on the autopsy and medical treatment provided for any illness or disease).\r\nThis data collection represents a single year of DCRP Jails data. The variable names and coding, while similar to other years, have not been standardized across years. The concatenated multi-year versions of the DCRP Jails population data have been edited to correct outliers and other data anomalies. Researchers are encouraged to use the concatenated multi-year data for final jail population data.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR36301.v1",
+                    "title": "Deaths in Custody Reporting Program: Non-standardized Jail Data, 2009"
+                }
+            ],
+            "identifier": "2250",
+            "isPartOf": "2441",
+            "issued": "2016-08-31T10:54:13",
             "keyword": [
                 "correctional facilities",
                 "corrections",
                 "death",
                 "jails"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2016-08-31T10:56:45",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2441",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2016-08-31T10:54:13",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR36301.v1",
-                    "title": "Deaths in Custody Reporting Program: Non-standardized Jail Data, 2009"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Deaths in Custody Reporting Program: Non-standardized Jail Data, 2010",
-            "description": "The Deaths in Custody Reporting Program (DCRP) is an annual data collection conducted by the Bureau of Justice Statistics (BJS). The DCRP began in 2000 under the Death in Custody Reporting Act of 2000 (P.L. 106-297). It is the only national statistical collection that obtains detailed information about deaths in adult correctional facilities. The DCRP collects data on persons dying in state prisons, local jails and in the process of arrest. Each collection is a separate subcollection, but each is under the umbrella of the DCRP collection. The DCRP collects inmate death records from each of the nation's 50 state prison systems and approximately 2,800 local jail jurisdictions. In addition, this program collects records of all deaths occurring during the process of arrest. Data are collected directly from state and local law enforcement agencies.\r\nDeath records include information on decedent personal characteristics (age, race or Hispanic origin, and sex), decedent criminal background (legal status, offense type, and time served), and the death itself (date, time, location, and cause of death, as well as information on the autopsy and medical treatment provided for any illness or disease).\r\nThis data collection represents a single year of DCRP Jails data. The variable names and coding, while similar to other years, have not been standardized across years. The concatenated multi-year versions of the DCRP Jails population data have been edited to correct outliers and other data anomalies. Researchers are encouraged to use the concatenated multi-year data for final jail population data.",
-            "modified": "2016-08-31T11:01:05",
-            "accessLevel": "restricted public",
-            "identifier": "2251",
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
+            "title": "Deaths in Custody Reporting Program: Non-standardized Jail Data, 2009"
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
+            "description": "The Deaths in Custody Reporting Program (DCRP) is an annual data collection conducted by the Bureau of Justice Statistics (BJS). The DCRP began in 2000 under the Death in Custody Reporting Act of 2000 (P.L. 106-297). It is the only national statistical collection that obtains detailed information about deaths in adult correctional facilities. The DCRP collects data on persons dying in state prisons, local jails and in the process of arrest. Each collection is a separate subcollection, but each is under the umbrella of the DCRP collection. The DCRP collects inmate death records from each of the nation's 50 state prison systems and approximately 2,800 local jail jurisdictions. In addition, this program collects records of all deaths occurring during the process of arrest. Data are collected directly from state and local law enforcement agencies.\r\nDeath records include information on decedent personal characteristics (age, race or Hispanic origin, and sex), decedent criminal background (legal status, offense type, and time served), and the death itself (date, time, location, and cause of death, as well as information on the autopsy and medical treatment provided for any illness or disease).\r\nThis data collection represents a single year of DCRP Jails data. The variable names and coding, while similar to other years, have not been standardized across years. The concatenated multi-year versions of the DCRP Jails population data have been edited to correct outliers and other data anomalies. Researchers are encouraged to use the concatenated multi-year data for final jail population data.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR36302.v1",
+                    "title": "Deaths in Custody Reporting Program: Non-standardized Jail Data, 2010"
+                }
+            ],
+            "identifier": "2251",
+            "isPartOf": "2441",
+            "issued": "2016-08-31T10:58:42",
             "keyword": [
                 "correctional facilities",
                 "corrections",
                 "death",
                 "jails"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2016-08-31T11:01:05",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2441",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2016-08-31T10:58:42",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR36302.v1",
-                    "title": "Deaths in Custody Reporting Program: Non-standardized Jail Data, 2010"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Deaths in Custody Reporting Program: Non-standardized Jail Data, 2011",
-            "description": "The Deaths in Custody Reporting Program (DCRP) is an annual data collection conducted by the Bureau of Justice Statistics (BJS). The DCRP began in 2000 under the Death in Custody Reporting Act of 2000 (P.L. 106-297). It is the only national statistical collection that obtains detailed information about deaths in adult correctional facilities. The DCRP collects data on persons dying in state prisons, local jails and in the process of arrest. Each collection is a separate subcollection, but each is under the umbrella of the DCRP collection. The DCRP collects inmate death records from each of the nation's 50 state prison systems and approximately 2,800 local jail jurisdictions. In addition, this program collects records of all deaths occurring during the process of arrest. Data are collected directly from state and local law enforcement agencies.\r\nDeath records include information on decedent personal characteristics (age, race or Hispanic origin, and sex), decedent criminal background (legal status, offense type, and time served), and the death itself (date, time, location, and cause of death, as well as information on the autopsy and medical treatment provided for any illness or disease).\r\nThis data collection represents a single year of DCRP Jails data. The variable names and coding, while similar to other years, have not been standardized across years. The concatenated multi-year versions of the DCRP Jails population data have been edited to correct outliers and other data anomalies. Researchers are encouraged to use the concatenated multi-year data for final jail population data.",
-            "modified": "2016-08-31T11:05:59",
-            "accessLevel": "restricted public",
-            "identifier": "2252",
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
+            "title": "Deaths in Custody Reporting Program: Non-standardized Jail Data, 2010"
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
+            "description": "The Deaths in Custody Reporting Program (DCRP) is an annual data collection conducted by the Bureau of Justice Statistics (BJS). The DCRP began in 2000 under the Death in Custody Reporting Act of 2000 (P.L. 106-297). It is the only national statistical collection that obtains detailed information about deaths in adult correctional facilities. The DCRP collects data on persons dying in state prisons, local jails and in the process of arrest. Each collection is a separate subcollection, but each is under the umbrella of the DCRP collection. The DCRP collects inmate death records from each of the nation's 50 state prison systems and approximately 2,800 local jail jurisdictions. In addition, this program collects records of all deaths occurring during the process of arrest. Data are collected directly from state and local law enforcement agencies.\r\nDeath records include information on decedent personal characteristics (age, race or Hispanic origin, and sex), decedent criminal background (legal status, offense type, and time served), and the death itself (date, time, location, and cause of death, as well as information on the autopsy and medical treatment provided for any illness or disease).\r\nThis data collection represents a single year of DCRP Jails data. The variable names and coding, while similar to other years, have not been standardized across years. The concatenated multi-year versions of the DCRP Jails population data have been edited to correct outliers and other data anomalies. Researchers are encouraged to use the concatenated multi-year data for final jail population data.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR36303.v1",
+                    "title": "Deaths in Custody Reporting Program: Non-standardized Jail Data, 2011"
+                }
+            ],
+            "identifier": "2252",
+            "isPartOf": "2441",
+            "issued": "2016-08-31T11:04:03",
             "keyword": [
                 "correctional facilities",
                 "corrections",
                 "death",
                 "jails"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2016-08-31T11:05:59",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2441",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2016-08-31T11:04:03",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR36303.v1",
-                    "title": "Deaths in Custody Reporting Program: Non-standardized Jail Data, 2011"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Deaths in Custody Reporting Program: Non-standardized Jail Data, 2012",
-            "description": "The Deaths in Custody Reporting Program (DCRP) is an annual data collection conducted by the Bureau of Justice Statistics (BJS). The DCRP began in 2000 under the Death in Custody Reporting Act of 2000 (P.L. 106-297). It is the only national statistical collection that obtains detailed information about deaths in adult correctional facilities. The DCRP collects data on persons dying in state prisons, local jails and in the process of arrest. Each collection is a separate subcollection, but each is under the umbrella of the DCRP collection. The DCRP collects inmate death records from each of the nation's 50 state prison systems and approximately 2,800 local jail jurisdictions. In addition, this program collects records of all deaths occurring during the process of arrest. Data are collected directly from state and local law enforcement agencies.\r\nDeath records include information on decedent personal characteristics (age, race or Hispanic origin, and sex), decedent criminal background (legal status, offense type, and time served), and the death itself (date, time, location, and cause of death, as well as information on the autopsy and medical treatment provided for any illness or disease).\r\nThis data collection represents a single year of DCRP Jails data. The variable names and coding, while similar to other years, have not been standardized across years. The concatenated multi-year versions of the DCRP Jails population data have been edited to correct outliers and other data anomalies. Researchers are encouraged to use the concatenated multi-year data for final jail population data.",
-            "modified": "2016-08-31T11:10:56",
-            "accessLevel": "restricted public",
-            "identifier": "2253",
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
+            "title": "Deaths in Custody Reporting Program: Non-standardized Jail Data, 2011"
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
+            "description": "The Deaths in Custody Reporting Program (DCRP) is an annual data collection conducted by the Bureau of Justice Statistics (BJS). The DCRP began in 2000 under the Death in Custody Reporting Act of 2000 (P.L. 106-297). It is the only national statistical collection that obtains detailed information about deaths in adult correctional facilities. The DCRP collects data on persons dying in state prisons, local jails and in the process of arrest. Each collection is a separate subcollection, but each is under the umbrella of the DCRP collection. The DCRP collects inmate death records from each of the nation's 50 state prison systems and approximately 2,800 local jail jurisdictions. In addition, this program collects records of all deaths occurring during the process of arrest. Data are collected directly from state and local law enforcement agencies.\r\nDeath records include information on decedent personal characteristics (age, race or Hispanic origin, and sex), decedent criminal background (legal status, offense type, and time served), and the death itself (date, time, location, and cause of death, as well as information on the autopsy and medical treatment provided for any illness or disease).\r\nThis data collection represents a single year of DCRP Jails data. The variable names and coding, while similar to other years, have not been standardized across years. The concatenated multi-year versions of the DCRP Jails population data have been edited to correct outliers and other data anomalies. Researchers are encouraged to use the concatenated multi-year data for final jail population data.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR36304.v1",
+                    "title": "Deaths in Custody Reporting Program: Non-standardized Jail Data, 2012"
+                }
+            ],
+            "identifier": "2253",
+            "isPartOf": "2441",
+            "issued": "2016-08-31T11:08:09",
             "keyword": [
                 "correctional facilities",
                 "corrections",
                 "death",
                 "jails"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2016-08-31T11:10:56",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2441",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2016-08-31T11:08:09",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR36304.v1",
-                    "title": "Deaths in Custody Reporting Program: Non-standardized Jail Data, 2012"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Parole Survey, 2014",
-            "description": "The 2014 Annual Parole Survey provides a count of the total number of persons supervised in the community on January 1 and December 31, 2014, and a count of the number entering and leaving supervision during the year. The survey also provides counts of the number of parolees by certain characteristics, such as gender, race and Hispanic or Latino origin, supervision status, and type of offense. This survey covers all 50 states, the District of Columbia, and the Federal System.",
-            "modified": "2015-12-02T08:40:54",
-            "accessLevel": "public",
-            "identifier": "2254",
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
+            "title": "Deaths in Custody Reporting Program: Non-standardized Jail Data, 2012"
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
+            "description": "The 2014 Annual Parole Survey provides a count of the total number of persons supervised in the community on January 1 and December 31, 2014, and a count of the number entering and leaving supervision during the year. The survey also provides counts of the number of parolees by certain characteristics, such as gender, race and Hispanic or Latino origin, supervision status, and type of offense. This survey covers all 50 states, the District of Columbia, and the Federal System.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR36320.v1",
+                    "title": "Annual Parole Survey, 2014"
+                }
+            ],
+            "identifier": "2254",
+            "isPartOf": "2631",
+            "issued": "2015-12-02T08:40:54",
             "keyword": [
                 "criminal justice system",
                 "offenses",
@@ -53799,54 +53793,54 @@
                 "parolees",
                 "sentencing"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2015-12-02T08:40:54",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2631",
-            "dataQuality": false,
-            "issued": "2015-12-02T08:40:54",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR36320.v1",
-                    "title": "Annual Parole Survey, 2014"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals - Terminated, 2013",
-            "description": "The data contain records of criminal appeals cases terminated in United States Courts of Appeals during fiscal year 2013. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. Appeals may be terminated on the merits or on procedural grounds. Of those that are terminated on the merits, the district court ruling may be affirmed, reversed, remanded to criminal court, or dismissed. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by Abt and the Bureau of Justice Statistics. Data and documentation were prepared by Abt.",
-            "modified": "2016-02-22T10:17:17",
-            "accessLevel": "restricted public",
-            "identifier": "2255",
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
+            "title": "Annual Parole Survey, 2014"
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
+            "description": "The data contain records of criminal appeals cases terminated in United States Courts of Appeals during fiscal year 2013. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. Appeals may be terminated on the merits or on procedural grounds. Of those that are terminated on the merits, the district court ruling may be affirmed, reversed, remanded to criminal court, or dismissed. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by Abt and the Bureau of Justice Statistics. Data and documentation were prepared by Abt.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR36323.v1",
+                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals - Terminated, 2013"
+                }
+            ],
+            "identifier": "2255",
+            "isPartOf": "2174",
+            "issued": "2016-02-17T09:27:06",
             "keyword": [
                 "administration",
                 "appellate courts",
@@ -53857,55 +53851,55 @@
                 "judicial decisions",
                 "legal systems"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2016-02-22T10:17:17",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2016-02-17T09:27:06",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR36323.v1",
-                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals - Terminated, 2013"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2013",
-            "description": "The data contain records of defendants in criminal cases filed in United States District Court during fiscal year 2013. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by Abt and the Bureau of Justice Statistics. Data and documentation were prepared by Abt.",
-            "modified": "2016-02-22T10:55:19",
-            "accessLevel": "restricted public",
-            "identifier": "2256",
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
+            "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals - Terminated, 2013"
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
+            "description": "The data contain records of defendants in criminal cases filed in United States District Court during fiscal year 2013. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by Abt and the Bureau of Justice Statistics. Data and documentation were prepared by Abt.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR36324.v1",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2013"
+                }
+            ],
+            "identifier": "2256",
+            "isPartOf": "2174",
+            "issued": "2016-02-17T09:29:54",
             "keyword": [
                 "administration",
                 "court cases",
@@ -53917,55 +53911,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2016-02-22T10:55:19",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2016-02-17T09:29:54",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR36324.v1",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2013"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court - Pending, 2013",
-            "description": "The data contain records of defendants in criminal cases filed in United States District Court before or during fiscal year 2013 and still pending as of year-end. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by Abt and the Bureau of Justice Statistics. Data and documentation were prepared by Abt.",
-            "modified": "2016-02-22T11:25:19",
-            "accessLevel": "restricted public",
-            "identifier": "2257",
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2013"
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
+            "description": "The data contain records of defendants in criminal cases filed in United States District Court before or during fiscal year 2013 and still pending as of year-end. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by Abt and the Bureau of Justice Statistics. Data and documentation were prepared by Abt.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR36326.v1",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court - Pending, 2013"
+                }
+            ],
+            "identifier": "2257",
+            "isPartOf": "2174",
+            "issued": "2016-02-17T09:32:49",
             "keyword": [
                 "administration",
                 "court cases",
@@ -53977,55 +53971,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2016-02-22T11:25:19",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2016-02-17T09:32:49",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR36326.v1",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court - Pending, 2013"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court - Terminated, 2013",
-            "description": "The data contain records of defendants in criminal cases terminated in United States District Court during fiscal year 2013. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by Abt and the Bureau of Justice Statistics. Data and documentation were prepared by Abt.",
-            "modified": "2016-02-22T12:18:06",
-            "accessLevel": "restricted public",
-            "identifier": "2258",
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court - Pending, 2013"
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
+            "description": "The data contain records of defendants in criminal cases terminated in United States District Court during fiscal year 2013. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by Abt and the Bureau of Justice Statistics. Data and documentation were prepared by Abt.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR36327.v1",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court - Terminated, 2013"
+                }
+            ],
+            "identifier": "2258",
+            "isPartOf": "2174",
+            "issued": "2016-02-17T09:35:28",
             "keyword": [
                 "administration",
                 "court cases",
@@ -54037,55 +54031,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2016-02-22T12:18:06",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2016-02-17T09:35:28",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR36327.v1",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court - Terminated, 2013"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2013",
-            "description": "The data contain records of sentenced offenders committed to the custody of the Bureau of Prisons (BOP) during fiscal year 2013. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by Abt and the Bureau of Justice Statistics. Data and documentation were prepared by Abt.",
-            "modified": "2016-02-22T14:01:46",
-            "accessLevel": "restricted public",
-            "identifier": "2259",
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court - Terminated, 2013"
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
+            "description": "The data contain records of sentenced offenders committed to the custody of the Bureau of Prisons (BOP) during fiscal year 2013. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by Abt and the Bureau of Justice Statistics. Data and documentation were prepared by Abt.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR36328.v1",
+                    "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2013"
+                }
+            ],
+            "identifier": "2259",
+            "isPartOf": "2174",
+            "issued": "2016-02-17T09:39:31",
             "keyword": [
                 "correctional facilities",
                 "correctional system",
@@ -54093,55 +54087,55 @@
                 "offenders",
                 "sentencing"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2016-02-22T14:01:46",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2016-02-17T09:39:31",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR36328.v1",
-                    "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2013"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Firearm Injury Surveillance Study, 1993-2002: [United States]",
-            "description": "These data were collected using the National Electronic\r\nInjury Surveillance System (NEISS), the primary data system of the\r\nUnited States Consumer Product Safety Commission (CPSC). CPSC began\r\noperating NEISS in 1972 to monitor product-related injuries treated in\r\nUnited States hospital emergency departments (EDs). In June 1992, the\r\nNational Center for Injury Prevention and Control (NCIPC), within the\r\nCenters for Disease Control and Prevention, established an interagency\r\nagreement with CPSC to begin collecting data on nonfatal firearm-related\r\ninjuries to monitor the incidence and characteristics of persons with\r\nnonfatal firearm-related injuries treated in United States hospital EDs\r\nover time. This dataset represents all nonfatal firearm-related injuries\r\n(i.e., injuries associated with powder-charged guns) and all nonfatal BB\r\nand pellet gun-related injuries reported through NEISS from 1993 through\r\n2002. The cases consist of initial ED visits for treatment of the\r\ninjuries. Cases were reported even if the patients subsequently died.\r\nSecondary visits and transfers from other hospitals were excluded.\r\nInformation is available on injury diagnosis, firearm type, use of drugs\r\nor alcohol, criminal incident, and locale of the incident. Demographic\r\ninformation includes age, sex, and race of the injured person.",
-            "modified": "2005-11-04T00:00:00",
-            "accessLevel": "public",
-            "identifier": "2260",
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
+            "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2013"
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
+            "description": "These data were collected using the National Electronic\r\nInjury Surveillance System (NEISS), the primary data system of the\r\nUnited States Consumer Product Safety Commission (CPSC). CPSC began\r\noperating NEISS in 1972 to monitor product-related injuries treated in\r\nUnited States hospital emergency departments (EDs). In June 1992, the\r\nNational Center for Injury Prevention and Control (NCIPC), within the\r\nCenters for Disease Control and Prevention, established an interagency\r\nagreement with CPSC to begin collecting data on nonfatal firearm-related\r\ninjuries to monitor the incidence and characteristics of persons with\r\nnonfatal firearm-related injuries treated in United States hospital EDs\r\nover time. This dataset represents all nonfatal firearm-related injuries\r\n(i.e., injuries associated with powder-charged guns) and all nonfatal BB\r\nand pellet gun-related injuries reported through NEISS from 1993 through\r\n2002. The cases consist of initial ED visits for treatment of the\r\ninjuries. Cases were reported even if the patients subsequently died.\r\nSecondary visits and transfers from other hospitals were excluded.\r\nInformation is available on injury diagnosis, firearm type, use of drugs\r\nor alcohol, criminal incident, and locale of the incident. Demographic\r\ninformation includes age, sex, and race of the injured person.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR04083.v1",
+                    "title": "Firearm Injury Surveillance Study, 1993-2002: [United States]"
+                }
+            ],
+            "identifier": "2260",
+            "isPartOf": "2438",
+            "issued": "2004-09-16T00:00:00",
             "keyword": [
                 "accidents",
                 "firearms",
@@ -54152,54 +54146,54 @@
                 "public health",
                 "public safety"
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
-            "isPartOf": "2438",
-            "dataQuality": false,
-            "issued": "2004-09-16T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR04083.v1",
-                    "title": "Firearm Injury Surveillance Study, 1993-2002: [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Electronic Injury Surveillance System All Injury Program, 2002    ",
-            "description": "Beginning in July 2000, the National Center for Injury\r\nPrevention and Control (NCIPC), Centers for Disease Control and\r\nPrevention (CDC), in collaboration with the United States Consumer\r\nProduct Safety Commission (CPSC), expanded the National Electronic\r\nInjury Surveillance System (NEISS) to collect data on all types and\r\ncauses of injuries treated in a representative sample of United States\r\nhospitals with emergency departments (ED). This system is called the\r\nNEISS All Injury Program (NEISS AIP). The NEISS AIP is designed to\r\nprovide national incidence estimates of all types and external causes\r\nof nonfatal injuries and poisonings treated in U.S. hospital EDs. Data\r\non injury-related visits are being obtained from a national sample of\r\n66 out of 100 NEISS hospitals, which were selected as a stratified\r\nprobability sample of hospitals in the United States and its\r\nterritories with a minimum of six beds and a 24-hour ED. The sample\r\nincludes separate strata for very large, large, medium, and small\r\nhospitals, defined by the number of annual ED visits per hospital, and\r\nchildren's hospitals. The scope of reporting goes beyond routine\r\nreporting of injuries associated with consumer-related products in\r\nCPSC's jurisdiction to include all injuries and poisonings. The data\r\ncan be used to (1) measure the magnitude and distribution of nonfatal\r\ninjuries in the United States, (2) monitor unintentional and\r\nviolence-related nonfatal injuries over time, (3) identify emerging\r\ninjury problems, (4) identify specific cases for follow-up\r\ninvestigations of particular injury-related problems, and (5) set\r\nnational priorities. A fundamental principle of this expansion effort\r\nis that preliminary surveillance data will be made available in a\r\ntimely manner to a number of different federal agencies with unique\r\nand overlapping public health responsibilities and concerns. Also,\r\nannually, the final edited data are released as public use data files\r\nfor use by other public health professionals and researchers. NEISS-AIP data on nonfatal injuries were collected from January through December each year except the year 2000 when data were collected from July through December (ICPSR 3582).NEISS AIP is providing data on approximately over 500,000 cases annually. Data obtained on each case include age, race/ethnicity, gender, principal diagnosis, primary body part affected, consumer products involved, disposition at ED discharge (i.e., hospitalized, transferred, treated and released, observation, died), locale where the injury occurred, work-relatedness, and a narrative description of the injury circumstances. Also, major categories of external cause of injury (e.g., motor vehicle, falls, cut/pierce, poisoning, fire/burn) and of intent of injury (e.g., unintentional, assault, intentional self-harm, legal intervention) are being coded for each case in a manner consistent with the International Classification of Diseases, Ninth Revision, Clinical Modification (ICD-9-CM) coding rules and guidelines. NEISS has been managed and operated by the United States Consumer Product Safety Commission since 1972 and is used by the Commission for identifying and monitoring consumer product-related injuries and for assessing risk to all United States residents. These product-related injury data are used for educating consumers about hazardous products and for identifying injury-related cases used in detailed studies of specific products and associated hazard patterns. These studies set the stage for developing both voluntary and mandatory safety standards.\r\nSince the early 1980s, CPSC has assisted other federal agencies by using NEISS to collect injury- related data of special interest to them. In 1990, an interagency agreement was established between NCIPC and CPSC to (1) collect NEISS data on nonfatal firearm-related injuries for the CDC Firearm Injury Surveillance Study; (2) publish NEISS data on a variety of injury-related topics, such as in-line skating, firearms, BB and pellet guns, bicycles, boat propellers, personal water craft, and playground injuries; and (3) to address common concerns. CPSC also uses NEISS to collect data on work-related injuries for the National Institute of Occupational Safety and Health (NIOSH), CDC. In 1997, the interagency agreement was modified to conduct the three-month NEISS All Injury Pilot Study at 21 NEISS hospitals (see Quinlan KP, Thompson MP, Annest JL, et al. Expanding the National Electronic Injury Surveillance System to Monitor All Nonfatal Injuries Treated in US Hospital Emergency Departments. Annals Emerg. Med. 1999;34:637-643.) This study demonstrated the feasibility of expanding NEISS to collect data on all injuries. National estimates based on this study indicated product-related injuries that fall into CPSC's jurisdiction accounted for approximately 50 percent of injuries treated in U.S. hospital EDs. The study also indicated that NEISS is a cost-effective system for capturing data on all injuries treated in U.S. hospital EDs. The NEISS-AIP provides an excellent data source for monitoring national estimates of nonfatal injuries over time. Analysis and dissemination of these surveillance data through the ICPSR, and Internet publications will help support NCIPC's mission of reducing all types and causes of injuries in the United States, as well as assist other federal agencies with responsibilities for injury prevention and control.",
-            "modified": "2004-10-01T00:00:00",
-            "accessLevel": "public",
-            "identifier": "2261",
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
+            "title": "Firearm Injury Surveillance Study, 1993-2002: [United States]"
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
+            "description": "Beginning in July 2000, the National Center for Injury\r\nPrevention and Control (NCIPC), Centers for Disease Control and\r\nPrevention (CDC), in collaboration with the United States Consumer\r\nProduct Safety Commission (CPSC), expanded the National Electronic\r\nInjury Surveillance System (NEISS) to collect data on all types and\r\ncauses of injuries treated in a representative sample of United States\r\nhospitals with emergency departments (ED). This system is called the\r\nNEISS All Injury Program (NEISS AIP). The NEISS AIP is designed to\r\nprovide national incidence estimates of all types and external causes\r\nof nonfatal injuries and poisonings treated in U.S. hospital EDs. Data\r\non injury-related visits are being obtained from a national sample of\r\n66 out of 100 NEISS hospitals, which were selected as a stratified\r\nprobability sample of hospitals in the United States and its\r\nterritories with a minimum of six beds and a 24-hour ED. The sample\r\nincludes separate strata for very large, large, medium, and small\r\nhospitals, defined by the number of annual ED visits per hospital, and\r\nchildren's hospitals. The scope of reporting goes beyond routine\r\nreporting of injuries associated with consumer-related products in\r\nCPSC's jurisdiction to include all injuries and poisonings. The data\r\ncan be used to (1) measure the magnitude and distribution of nonfatal\r\ninjuries in the United States, (2) monitor unintentional and\r\nviolence-related nonfatal injuries over time, (3) identify emerging\r\ninjury problems, (4) identify specific cases for follow-up\r\ninvestigations of particular injury-related problems, and (5) set\r\nnational priorities. A fundamental principle of this expansion effort\r\nis that preliminary surveillance data will be made available in a\r\ntimely manner to a number of different federal agencies with unique\r\nand overlapping public health responsibilities and concerns. Also,\r\nannually, the final edited data are released as public use data files\r\nfor use by other public health professionals and researchers. NEISS-AIP data on nonfatal injuries were collected from January through December each year except the year 2000 when data were collected from July through December (ICPSR 3582).NEISS AIP is providing data on approximately over 500,000 cases annually. Data obtained on each case include age, race/ethnicity, gender, principal diagnosis, primary body part affected, consumer products involved, disposition at ED discharge (i.e., hospitalized, transferred, treated and released, observation, died), locale where the injury occurred, work-relatedness, and a narrative description of the injury circumstances. Also, major categories of external cause of injury (e.g., motor vehicle, falls, cut/pierce, poisoning, fire/burn) and of intent of injury (e.g., unintentional, assault, intentional self-harm, legal intervention) are being coded for each case in a manner consistent with the International Classification of Diseases, Ninth Revision, Clinical Modification (ICD-9-CM) coding rules and guidelines. NEISS has been managed and operated by the United States Consumer Product Safety Commission since 1972 and is used by the Commission for identifying and monitoring consumer product-related injuries and for assessing risk to all United States residents. These product-related injury data are used for educating consumers about hazardous products and for identifying injury-related cases used in detailed studies of specific products and associated hazard patterns. These studies set the stage for developing both voluntary and mandatory safety standards.\r\nSince the early 1980s, CPSC has assisted other federal agencies by using NEISS to collect injury- related data of special interest to them. In 1990, an interagency agreement was established between NCIPC and CPSC to (1) collect NEISS data on nonfatal firearm-related injuries for the CDC Firearm Injury Surveillance Study; (2) publish NEISS data on a variety of injury-related topics, such as in-line skating, firearms, BB and pellet guns, bicycles, boat propellers, personal water craft, and playground injuries; and (3) to address common concerns. CPSC also uses NEISS to collect data on work-related injuries for the National Institute of Occupational Safety and Health (NIOSH), CDC. In 1997, the interagency agreement was modified to conduct the three-month NEISS All Injury Pilot Study at 21 NEISS hospitals (see Quinlan KP, Thompson MP, Annest JL, et al. Expanding the National Electronic Injury Surveillance System to Monitor All Nonfatal Injuries Treated in US Hospital Emergency Departments. Annals Emerg. Med. 1999;34:637-643.) This study demonstrated the feasibility of expanding NEISS to collect data on all injuries. National estimates based on this study indicated product-related injuries that fall into CPSC's jurisdiction accounted for approximately 50 percent of injuries treated in U.S. hospital EDs. The study also indicated that NEISS is a cost-effective system for capturing data on all injuries treated in U.S. hospital EDs. The NEISS-AIP provides an excellent data source for monitoring national estimates of nonfatal injuries over time. Analysis and dissemination of these surveillance data through the ICPSR, and Internet publications will help support NCIPC's mission of reducing all types and causes of injuries in the United States, as well as assist other federal agencies with responsibilities for injury prevention and control.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR04085.v1",
+                    "title": "National Electronic Injury Surveillance System All Injury Program, 2002    "
+                }
+            ],
+            "identifier": "2261",
+            "isPartOf": "2438",
+            "issued": "2004-10-01T00:00:00",
             "keyword": [
                 "accidents",
                 "medical care",
@@ -54209,54 +54203,54 @@
                 "public health",
                 "public safety"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2004-10-01T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2438",
-            "dataQuality": false,
-            "issued": "2004-10-01T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR04085.v1",
-                    "title": "National Electronic Injury Surveillance System All Injury Program, 2002    "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Court Cases: Integrated Data Base Bankruptcy Petitions, 1998",
-            "description": "The purpose of this data collection is to provide an\r\nofficial public record of the business of the federal bankruptcy\r\ncourts. The data includes all petitions filed under the Bankruptcy\r\nCode in the U.S. Bankruptcy Courts on or after October 1, 1993, and any\r\npetitions filed before October 1, 1993, that were still pending on that\r\ndate. The records are organized according to the fiscal year of\r\ntermination with cases still pending at the end included in a separate\r\npending data set. For the bankruptcy data, the unit of analysis is a\r\nsingle case.",
-            "modified": "2011-04-12T10:14:00",
-            "accessLevel": "restricted public",
-            "identifier": "2262",
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
+            "title": "National Electronic Injury Surveillance System All Injury Program, 2002    "
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
+            "description": "The purpose of this data collection is to provide an\r\nofficial public record of the business of the federal bankruptcy\r\ncourts. The data includes all petitions filed under the Bankruptcy\r\nCode in the U.S. Bankruptcy Courts on or after October 1, 1993, and any\r\npetitions filed before October 1, 1993, that were still pending on that\r\ndate. The records are organized according to the fiscal year of\r\ntermination with cases still pending at the end included in a separate\r\npending data set. For the bankruptcy data, the unit of analysis is a\r\nsingle case.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR04086.v1",
+                    "title": "Federal Court Cases: Integrated Data Base Bankruptcy Petitions, 1998"
+                }
+            ],
+            "identifier": "2262",
+            "isPartOf": "2173",
+            "issued": "2004-11-17T00:00:00",
             "keyword": [
                 "administration",
                 "appellate courts",
@@ -54274,55 +54268,55 @@
                 "trial courts",
                 "trial procedures"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-04-12T10:14:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2173",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2004-11-17T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR04086.v1",
-                    "title": "Federal Court Cases: Integrated Data Base Bankruptcy Petitions, 1998"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Court Cases:  Integrated Data Base Bankruptcy Petitions, 1999",
-            "description": "The purpose of this data collection is to provide an\r\nofficial public record of the business of the federal bankruptcy\r\ncourts. The data includes all petitions filed under the Bankruptcy\r\nCode in the U.S. Bankruptcy Courts on or after October 1, 1993, and\r\nany petitions filed before October 1, 1993, that were still pending on\r\nthat date. The records are organized according to the fiscal year of\r\ntermination with cases still pending at the end included in a separate\r\npending data set. For the bankruptcy data, the unit of analysis is a\r\nsingle case.",
-            "modified": "2011-04-12T11:15:20",
-            "accessLevel": "restricted public",
-            "identifier": "2263",
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
+            "title": "Federal Court Cases: Integrated Data Base Bankruptcy Petitions, 1998"
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
+            "description": "The purpose of this data collection is to provide an\r\nofficial public record of the business of the federal bankruptcy\r\ncourts. The data includes all petitions filed under the Bankruptcy\r\nCode in the U.S. Bankruptcy Courts on or after October 1, 1993, and\r\nany petitions filed before October 1, 1993, that were still pending on\r\nthat date. The records are organized according to the fiscal year of\r\ntermination with cases still pending at the end included in a separate\r\npending data set. For the bankruptcy data, the unit of analysis is a\r\nsingle case.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR04088.v1",
+                    "title": "Federal Court Cases:  Integrated Data Base Bankruptcy Petitions, 1999"
+                }
+            ],
+            "identifier": "2263",
+            "isPartOf": "2173",
+            "issued": "2004-11-17T00:00:00",
             "keyword": [
                 "administration",
                 "appellate courts",
@@ -54341,55 +54335,55 @@
                 "trial courts",
                 "trial procedures"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-04-12T11:15:20",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2173",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2004-11-17T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR04088.v1",
-                    "title": "Federal Court Cases:  Integrated Data Base Bankruptcy Petitions, 1999"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Monitoring of Federal Criminal Convictions and Sentences:  Appeals Data, 2002  ",
-            "description": "This collection contains appellate information from the 12\r\ncircuit courts of appeals of the United States. From the Clerk of the\r\nCourt of each court of appeals, the United States Sentencing\r\nCommission compiled the final opinions and orders, both published and\r\nunpublished, in all criminal appeals for the time period surveyed. The\r\nCommission also collected habeas corpus decisions even though they are\r\ntechnically civil matters, because such cases often involve sentencing\r\nissues. Both the \"case\" and the \"defendant\" are used in this\r\ncollection as units of analysis. Each \"case\" comprises individual\r\nrecords representing all codefendants participating in a consolidated\r\nappeal. Each defendant's record comprises the sentencing-related\r\nissues corresponding to that particular defendant.",
-            "modified": "2014-06-27T14:20:08",
-            "accessLevel": "public",
-            "identifier": "2264",
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
+            "title": "Federal Court Cases:  Integrated Data Base Bankruptcy Petitions, 1999"
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
+            "description": "This collection contains appellate information from the 12\r\ncircuit courts of appeals of the United States. From the Clerk of the\r\nCourt of each court of appeals, the United States Sentencing\r\nCommission compiled the final opinions and orders, both published and\r\nunpublished, in all criminal appeals for the time period surveyed. The\r\nCommission also collected habeas corpus decisions even though they are\r\ntechnically civil matters, because such cases often involve sentencing\r\nissues. Both the \"case\" and the \"defendant\" are used in this\r\ncollection as units of analysis. Each \"case\" comprises individual\r\nrecords representing all codefendants participating in a consolidated\r\nappeal. Each defendant's record comprises the sentencing-related\r\nissues corresponding to that particular defendant.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR04108.v1",
+                    "title": "Monitoring of Federal Criminal Convictions and Sentences:  Appeals Data, 2002  "
+                }
+            ],
+            "identifier": "2264",
+            "isPartOf": "2175",
+            "issued": "2005-01-19T00:00:00",
             "keyword": [
                 "appeal procedures",
                 "appellate courts",
@@ -54404,54 +54398,54 @@
                 "sentence review",
                 "sentencing"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2014-06-27T14:20:08",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2175",
-            "dataQuality": false,
-            "issued": "2005-01-19T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR04108.v1",
-                    "title": "Monitoring of Federal Criminal Convictions and Sentences:  Appeals Data, 2002  "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Organizations Convicted in Federal Criminal Courts, 2002",
-            "description": "These data, collected to assist in the development of\r\n sentencing guidelines, describe offense and sentencing characteristics\r\n for organizations sentenced in federal district courts in 2002. The\r\n United States Sentencing Commission's primary function is to inform\r\n federal courts of sentencing policies and practices that include\r\n guidelines prescribing the appropriate form and severity of punishment\r\n for offenders convicted of federal crimes. Court-related variables\r\n include primary offense type, pecuniary offense loss and gain, dates\r\n of disposition and sentencing, method of determination of guilt,\r\n number of counts pled and charged, and dates and types of sentencing\r\n and restitution. Defendant organization variables include ownership\r\n structure, number of owners and employees, highest level of corporate\r\n knowledge of the criminal offense, highest level of corporate\r\n indictment and conviction for participation in the criminal offense,\r\n annual revenue, equity and financial status, whether it was a criminal\r\n organization, duration of criminal activity, and risk to national\r\n security. Organizational Defendants Data, 2002, covers fiscal year\r\nOctober 1, 2001, through September 30, 2002.",
-            "modified": "2014-06-27T14:36:33",
-            "accessLevel": "public",
-            "identifier": "2265",
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
+            "title": "Monitoring of Federal Criminal Convictions and Sentences:  Appeals Data, 2002  "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "011:21"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "These data, collected to assist in the development of\r\n sentencing guidelines, describe offense and sentencing characteristics\r\n for organizations sentenced in federal district courts in 2002. The\r\n United States Sentencing Commission's primary function is to inform\r\n federal courts of sentencing policies and practices that include\r\n guidelines prescribing the appropriate form and severity of punishment\r\n for offenders convicted of federal crimes. Court-related variables\r\n include primary offense type, pecuniary offense loss and gain, dates\r\n of disposition and sentencing, method of determination of guilt,\r\n number of counts pled and charged, and dates and types of sentencing\r\n and restitution. Defendant organization variables include ownership\r\n structure, number of owners and employees, highest level of corporate\r\n knowledge of the criminal offense, highest level of corporate\r\n indictment and conviction for participation in the criminal offense,\r\n annual revenue, equity and financial status, whether it was a criminal\r\n organization, duration of criminal activity, and risk to national\r\n security. Organizational Defendants Data, 2002, covers fiscal year\r\nOctober 1, 2001, through September 30, 2002.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR04109.v1",
+                    "title": "Organizations Convicted in Federal Criminal Courts, 2002"
+                }
+            ],
+            "identifier": "2265",
+            "isPartOf": "2427",
+            "issued": "2004-12-08T00:00:00",
             "keyword": [
                 "convictions (law)",
                 "corporate crime",
@@ -54467,54 +54461,54 @@
                 "sentencing",
                 "sentencing guidelines"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2014-06-27T14:36:33",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2427",
-            "dataQuality": false,
-            "issued": "2004-12-08T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR04109.v1",
-                    "title": "Organizations Convicted in Federal Criminal Courts, 2002"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Court Cases:  Integrated Data Base, 2002        ",
-            "description": "The purpose of this data collection is to provide an\r\nofficial public record of the business of the federal courts. The data\r\noriginate from district and appellate court offices throughout the\r\nUnited States. Information was obtained at two points in the life of a\r\ncase: filing and termination. The termination data contain information\r\non both filing and terminations, while the pending data contain only\r\nfiling information.",
-            "modified": "2015-09-18T16:21:48",
-            "accessLevel": "restricted public",
-            "identifier": "2266",
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
+            "title": "Organizations Convicted in Federal Criminal Courts, 2002"
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
+            "description": "The purpose of this data collection is to provide an\r\nofficial public record of the business of the federal courts. The data\r\noriginate from district and appellate court offices throughout the\r\nUnited States. Information was obtained at two points in the life of a\r\ncase: filing and termination. The termination data contain information\r\non both filing and terminations, while the pending data contain only\r\nfiling information.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR04059.v3",
+                    "title": "Federal Court Cases:  Integrated Data Base, 2002        "
+                }
+            ],
+            "identifier": "2266",
+            "isPartOf": "2173",
+            "issued": "2004-10-08T00:00:00",
             "keyword": [
                 "administration",
                 "appellate courts",
@@ -54533,55 +54527,55 @@
                 "trial courts",
                 "trial procedures"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2015-09-18T16:21:48",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2173",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2004-10-08T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR04059.v3",
-                    "title": "Federal Court Cases:  Integrated Data Base, 2002        "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Incident-Based Reporting System, 2002",
-            "description": "The National Incident-Based Reporting System (NIBRS) is a\r\n part of the Uniform Crime Reporting Program (UCR), administered by the\r\n Federal Bureau of Investigation (FBI). In the late 1970s, the law\r\n enforcement community called for a thorough evaluative study of the\r\n UCR with the objective of recommending an expanded and enhanced UCR\r\n program to meet law enforcement needs into the 21st century. The FBI\r\n fully concurred with the need for an updated program to meet\r\n contemporary needs and provided its support, formulating a\r\n comprehensive redesign effort. Following a multiyear study, a\r\n \"Blueprint for the Future of the Uniform Crime Reporting Program\" was\r\n developed. Using the \"Blueprint\" and in consultation with local and\r\n state law enforcement executives, the FBI formulated new guidelines\r\n for the Uniform Crime Reports. The National Incident-Based Reporting\r\n System (NIBRS) is being implemented to meet these guidelines. NIBRS\r\n data are archived at ICPSR as 13 separate data files per year, which\r\n may be merged by using linkage variables. The data focus on a variety\r\n of aspects of a crime incident. Part 4, Administrative Segment, offers\r\n data on the incident itself (date and time). Each crime incident is\r\n delineated by one administrative segment record. Also provided are\r\n Part 5, Offense Segment (offense type, location, weapon use, and bias\r\n motivation), Part 6, Property Segment (type of property loss, property\r\n description, property value, drug type and quantity), Part 7, Victim\r\n Segment (age, sex, race, ethnicity, and injuries), Part 8, Offender\r\n Segment (age, sex, and race), and Part 9, Arrestee Segment (arrest\r\n date, age, sex, race, and weapon use). The Batch Header Segment (Parts\r\n 1-3) separates and identifies individual police agencies by\r\n Originating Agency Identifier (ORI). Batch Header information, which\r\n is contained on three records for each ORI, includes agency name,\r\n geographic location, and population of the area. Part 10, Group B\r\n Arrest Report Segment, includes arrestee data for Group B crimes.\r\n Window Segments files (Parts 11-13) pertain to incidents for which the\r\n complete Group A Incident Report was not submitted to the FBI. In\r\n general, a Window Segment record will be generated if the incident\r\n occurred prior to January 1 of the previous year or if the incident\r\n occurred prior to when the agency started NIBRS reporting. As with\r\n UCR, participation in NIBRS is voluntary on the part of law\r\n enforcement agencies. The data are not a representative sample of\r\n crime in the United States. For 2002, 23 states, fully or partially\r\nparticipating in NIBRS, were included in the dataset.",
-            "modified": "2007-03-15T00:00:00",
-            "accessLevel": "public",
-            "identifier": "2267",
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
+            "title": "Federal Court Cases:  Integrated Data Base, 2002        "
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
+            "description": "The National Incident-Based Reporting System (NIBRS) is a\r\n part of the Uniform Crime Reporting Program (UCR), administered by the\r\n Federal Bureau of Investigation (FBI). In the late 1970s, the law\r\n enforcement community called for a thorough evaluative study of the\r\n UCR with the objective of recommending an expanded and enhanced UCR\r\n program to meet law enforcement needs into the 21st century. The FBI\r\n fully concurred with the need for an updated program to meet\r\n contemporary needs and provided its support, formulating a\r\n comprehensive redesign effort. Following a multiyear study, a\r\n \"Blueprint for the Future of the Uniform Crime Reporting Program\" was\r\n developed. Using the \"Blueprint\" and in consultation with local and\r\n state law enforcement executives, the FBI formulated new guidelines\r\n for the Uniform Crime Reports. The National Incident-Based Reporting\r\n System (NIBRS) is being implemented to meet these guidelines. NIBRS\r\n data are archived at ICPSR as 13 separate data files per year, which\r\n may be merged by using linkage variables. The data focus on a variety\r\n of aspects of a crime incident. Part 4, Administrative Segment, offers\r\n data on the incident itself (date and time). Each crime incident is\r\n delineated by one administrative segment record. Also provided are\r\n Part 5, Offense Segment (offense type, location, weapon use, and bias\r\n motivation), Part 6, Property Segment (type of property loss, property\r\n description, property value, drug type and quantity), Part 7, Victim\r\n Segment (age, sex, race, ethnicity, and injuries), Part 8, Offender\r\n Segment (age, sex, and race), and Part 9, Arrestee Segment (arrest\r\n date, age, sex, race, and weapon use). The Batch Header Segment (Parts\r\n 1-3) separates and identifies individual police agencies by\r\n Originating Agency Identifier (ORI). Batch Header information, which\r\n is contained on three records for each ORI, includes agency name,\r\n geographic location, and population of the area. Part 10, Group B\r\n Arrest Report Segment, includes arrestee data for Group B crimes.\r\n Window Segments files (Parts 11-13) pertain to incidents for which the\r\n complete Group A Incident Report was not submitted to the FBI. In\r\n general, a Window Segment record will be generated if the incident\r\n occurred prior to January 1 of the previous year or if the incident\r\n occurred prior to when the agency started NIBRS reporting. As with\r\n UCR, participation in NIBRS is voluntary on the part of law\r\n enforcement agencies. The data are not a representative sample of\r\n crime in the United States. For 2002, 23 states, fully or partially\r\nparticipating in NIBRS, were included in the dataset.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR04066.v2",
+                    "title": "National Incident-Based Reporting System, 2002"
+                }
+            ],
+            "identifier": "2267",
+            "isPartOf": "2433",
+            "issued": "2004-10-18T00:00:00",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -54596,54 +54590,54 @@
                 "victims",
                 "violent crime"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2007-03-15T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2433",
-            "dataQuality": false,
-            "issued": "2004-10-18T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR04066.v2",
-                    "title": "National Incident-Based Reporting System, 2002"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data [United States]:  Property Stolen and Recovered, 2002  ",
-            "description": "Since 1930, the Federal Bureau of Investigation has\r\n compiled the Uniform Crime Reports (UCR) to serve as periodic\r\n nationwide assessments of reported crimes not available elsewhere in\r\n the criminal justice system. Law enforcement agencies contribute\r\n reports either directly or through their state reporting programs.\r\n Each year, this information is reported in four types of files: (1)\r\n Offenses Known and Clearances by Arrest, (2) Property Stolen and\r\n Recovered, (3) Supplementary Homicide Reports (SHR), and (4) Police\r\n Employee (LEOKA) Data. The Property Stolen and Recovered data are\r\n collected on a monthly basis by all UCR contributing agencies. These\r\n data, aggregated at the agency level, report on the nature of the\r\n crime, the monetary value of the property stolen, and the type of\r\n property stolen. Similar information regarding recovered property is\r\nalso included in the data.",
-            "modified": "2005-11-04T00:00:00",
-            "accessLevel": "public",
-            "identifier": "2268",
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
+            "title": "National Incident-Based Reporting System, 2002"
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
+            "description": "Since 1930, the Federal Bureau of Investigation has\r\n compiled the Uniform Crime Reports (UCR) to serve as periodic\r\n nationwide assessments of reported crimes not available elsewhere in\r\n the criminal justice system. Law enforcement agencies contribute\r\n reports either directly or through their state reporting programs.\r\n Each year, this information is reported in four types of files: (1)\r\n Offenses Known and Clearances by Arrest, (2) Property Stolen and\r\n Recovered, (3) Supplementary Homicide Reports (SHR), and (4) Police\r\n Employee (LEOKA) Data. The Property Stolen and Recovered data are\r\n collected on a monthly basis by all UCR contributing agencies. These\r\n data, aggregated at the agency level, report on the nature of the\r\n crime, the monetary value of the property stolen, and the type of\r\n property stolen. Similar information regarding recovered property is\r\nalso included in the data.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR04067.v1",
+                    "title": "Uniform Crime Reporting Program Data [United States]:  Property Stolen and Recovered, 2002  "
+                }
+            ],
+            "identifier": "2268",
+            "isPartOf": "2167",
+            "issued": "2004-09-02T00:00:00",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -54658,54 +54652,54 @@
                 "stolen property",
                 "stolen property recovery"
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
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2004-09-02T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR04067.v1",
-                    "title": "Uniform Crime Reporting Program Data [United States]:  Property Stolen and Recovered, 2002  "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, Summarized Yearly, 2002",
-            "description": "These data provide information on the number of arrests\r\nreported to the Federal Bureau of Investigation's Uniform Crime\r\nReporting (UCR) Program each year by police agencies in the United\r\nStates. These arrest reports provide data on 43 offenses including\r\nviolent crime, drug use, gambling, and larceny. The data received by\r\nICPSR were structured as a hierarchical file containing, per reporting\r\npolice agency: an agency header record, and 1 to 43 detail offense\r\nrecords containing the counts of arrests by age, sex, and race for a\r\nparticular offense. ICPSR restructured the original data to logical\r\nrecord length format with the agency header record variables copied\r\nonto the detail records. Consequently, each record contains arrest\r\ncounts for a particular agency-offense.",
-            "modified": "2009-09-28T18:55:04",
-            "accessLevel": "public",
-            "identifier": "2269",
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
+            "title": "Uniform Crime Reporting Program Data [United States]:  Property Stolen and Recovered, 2002  "
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
+            "description": "These data provide information on the number of arrests\r\nreported to the Federal Bureau of Investigation's Uniform Crime\r\nReporting (UCR) Program each year by police agencies in the United\r\nStates. These arrest reports provide data on 43 offenses including\r\nviolent crime, drug use, gambling, and larceny. The data received by\r\nICPSR were structured as a hierarchical file containing, per reporting\r\npolice agency: an agency header record, and 1 to 43 detail offense\r\nrecords containing the counts of arrests by age, sex, and race for a\r\nparticular offense. ICPSR restructured the original data to logical\r\nrecord length format with the agency header record variables copied\r\nonto the detail records. Consequently, each record contains arrest\r\ncounts for a particular agency-offense.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR04068.v2",
+                    "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, Summarized Yearly, 2002"
+                }
+            ],
+            "identifier": "2269",
+            "isPartOf": "2167",
+            "issued": "2004-08-26T00:00:00",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrest records",
@@ -54721,54 +54715,53 @@
                 "offenses",
                 "violent crime"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2009-09-28T18:55:04",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2004-08-26T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR04068.v2",
-                    "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, Summarized Yearly, 2002"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Police Departments, Arrests and Crime in the United States, 1860-1920",
-            "description": "These data on 19th- and early 20th-century police department\r\nand arrest behavior were collected between 1975 and 1978 for a study of\r\npolice and crime in the United States. Raw and aggregated time-series\r\ndata are presented in Parts 1 and 3 on 23 American cities for most\r\nyears during the period 1860-1920. The data were drawn from annual\r\nreports of police departments found in the Library of Congress or in\r\nnewspapers and legislative reports located elsewhere. Variables in Part\r\n1, for which the city is the unit of analysis, include arrests for\r\ndrunkenness, conditional offenses and homicides, persons dismissed or\r\nheld, police personnel, and population. Part 3 aggregates the data by\r\nyear and reports some of these variables on a per capita basis, using a\r\nlinear interpolation from the last decennial census to estimate\r\npopulation. Part 2 contains data for 267 United States cities for the\r\nperiod 1880-1890 and was generated from the 1880 federal census volume,\r\nREPORT ON THE DEFECTIVE, DEPENDENT, AND DELINQUENT CLASSES, published\r\nin 1888, and from the 1890 federal census volume, SOCIAL STATISTICS OF\r\nCITIES. Information includes police personnel and expenditures,\r\narrests, persons held overnight, trains entering town, and population.",
-            "modified": "2006-01-12T00:00:00",
-            "accessLevel": "public",
-            "identifier": "2270",
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
+            "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, Summarized Yearly, 2002"
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
+            "description": "These data on 19th- and early 20th-century police department\r\nand arrest behavior were collected between 1975 and 1978 for a study of\r\npolice and crime in the United States. Raw and aggregated time-series\r\ndata are presented in Parts 1 and 3 on 23 American cities for most\r\nyears during the period 1860-1920. The data were drawn from annual\r\nreports of police departments found in the Library of Congress or in\r\nnewspapers and legislative reports located elsewhere. Variables in Part\r\n1, for which the city is the unit of analysis, include arrests for\r\ndrunkenness, conditional offenses and homicides, persons dismissed or\r\nheld, police personnel, and population. Part 3 aggregates the data by\r\nyear and reports some of these variables on a per capita basis, using a\r\nlinear interpolation from the last decennial census to estimate\r\npopulation. Part 2 contains data for 267 United States cities for the\r\nperiod 1880-1890 and was generated from the 1880 federal census volume,\r\nREPORT ON THE DEFECTIVE, DEPENDENT, AND DELINQUENT CLASSES, published\r\nin 1888, and from the 1890 federal census volume, SOCIAL STATISTICS OF\r\nCITIES. Information includes police personnel and expenditures,\r\narrests, persons held overnight, trains entering town, and population.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR07708.v2",
+                    "title": "Police Departments, Arrests and Crime in the United States, 1860-1920"
+                }
+            ],
+            "identifier": "2270",
+            "issued": "1984-03-18T00:00:00",
             "keyword": [
                 "United States",
                 "arrests",
@@ -54778,53 +54771,54 @@
                 "police activity",
                 "police chiefs"
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
-            "dataQuality": false,
-            "issued": "1984-03-18T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR07708.v2",
-                    "title": "Police Departments, Arrests and Crime in the United States, 1860-1920"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reports, 1958-1969, and County and City Data Books, 1962, 1967, 1972:  Merged Data",
-            "description": "This dataset includes selected variables and cases from the\r\n Federal Bureau of Investigation's Uniform Crime Reports, 1958-1969,\r\n and the County and City Data Books for 1962, 1967, and 1972. Data are\r\n reported for all United States cities with a population of 75,000 or\r\n more in 1960. Data from the Uniform Crime Reports include for each year\r\n the number of homicides, forcible rapes, robberies, aggravated assaults,\r\n burglaries, larcenies over 50 dollars, and auto thefts. Also included is the\r\n Total Crime Index, which is the simple sum of all the crimes listed\r\n above. Selected variables describing population characteristics and\r\n city finances were taken from the 1962, 1967, and 1972 County and\r\nCity Data Books.",
-            "modified": "2005-11-04T00:00:00",
-            "accessLevel": "public",
-            "identifier": "2271",
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
+            "title": "Police Departments, Arrests and Crime in the United States, 1860-1920"
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
+            "description": "This dataset includes selected variables and cases from the\r\n Federal Bureau of Investigation's Uniform Crime Reports, 1958-1969,\r\n and the County and City Data Books for 1962, 1967, and 1972. Data are\r\n reported for all United States cities with a population of 75,000 or\r\n more in 1960. Data from the Uniform Crime Reports include for each year\r\n the number of homicides, forcible rapes, robberies, aggravated assaults,\r\n burglaries, larcenies over 50 dollars, and auto thefts. Also included is the\r\n Total Crime Index, which is the simple sum of all the crimes listed\r\n above. Selected variables describing population characteristics and\r\n city finances were taken from the 1962, 1967, and 1972 County and\r\nCity Data Books.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR07715.v1",
+                    "title": "Uniform Crime Reports, 1958-1969, and County and City Data Books, 1962, 1967, 1972:  Merged Data"
+                }
+            ],
+            "identifier": "2271",
+            "isPartOf": "2167",
+            "issued": "1984-03-18T00:00:00",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -54843,54 +54837,54 @@
                 "robbery",
                 "weapons offenses"
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
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "1984-03-18T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR07715.v1",
-                    "title": "Uniform Crime Reports, 1958-1969, and County and City Data Books, 1962, 1967, 1972:  Merged Data"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Court Cases: Integrated Data Base Bankruptcy Petitions, 2005",
-            "description": "The purpose of this data collection is to provide an\r\nofficial public record of the business of the federal bankruptcy\r\ncourts. The data include all petitions filed under the Bankruptcy Code\r\nin the United States Bankruptcy Courts on or after October 1, 2005, that were terminated in the 2005 fiscal year. For the bankruptcy data, the unit of analysis is a single case.",
-            "modified": "2011-03-08T09:42:05",
-            "accessLevel": "restricted public",
-            "identifier": "2272",
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
+            "title": "Uniform Crime Reports, 1958-1969, and County and City Data Books, 1962, 1967, 1972:  Merged Data"
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
+            "description": "The purpose of this data collection is to provide an\r\nofficial public record of the business of the federal bankruptcy\r\ncourts. The data include all petitions filed under the Bankruptcy Code\r\nin the United States Bankruptcy Courts on or after October 1, 2005, that were terminated in the 2005 fiscal year. For the bankruptcy data, the unit of analysis is a single case.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR23080.v2",
+                    "title": "Federal Court Cases: Integrated Data Base Bankruptcy Petitions, 2005"
+                }
+            ],
+            "identifier": "2272",
+            "isPartOf": "2173",
+            "issued": "2008-12-10T15:12:39",
             "keyword": [
                 "administration",
                 "appellate courts",
@@ -54908,55 +54902,55 @@
                 "trial courts",
                 "trial procedures"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T09:42:05",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2173",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2008-12-10T15:12:39",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR23080.v2",
-                    "title": "Federal Court Cases: Integrated Data Base Bankruptcy Petitions, 2005"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Court Cases: Integrated Data Base Bankruptcy Petitions, 2006",
-            "description": "The purpose of this data collection is to provide an official public record of the business of the federal bankruptcy courts. The data include all petitions filed under the Bankruptcy Code in the United States Bankruptcy Courts on or after October 1, 2006, that were terminated in the 2006 fiscal year. For the bankruptcy data, the unit of analysis is a single case.",
-            "modified": "2011-03-08T09:42:38",
-            "accessLevel": "restricted public",
-            "identifier": "2273",
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
+            "title": "Federal Court Cases: Integrated Data Base Bankruptcy Petitions, 2005"
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
+            "description": "The purpose of this data collection is to provide an official public record of the business of the federal bankruptcy courts. The data include all petitions filed under the Bankruptcy Code in the United States Bankruptcy Courts on or after October 1, 2006, that were terminated in the 2006 fiscal year. For the bankruptcy data, the unit of analysis is a single case.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR23081.v2",
+                    "title": "Federal Court Cases: Integrated Data Base Bankruptcy Petitions, 2006"
+                }
+            ],
+            "identifier": "2273",
+            "isPartOf": "2173",
+            "issued": "2008-12-10T15:18:01",
             "keyword": [
                 "administration",
                 "appellate courts",
@@ -54974,55 +54968,55 @@
                 "trial courts",
                 "trial procedures"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T09:42:38",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2173",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2008-12-10T15:18:01",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR23081.v2",
-                    "title": "Federal Court Cases: Integrated Data Base Bankruptcy Petitions, 2006"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Court Cases: Integrated Data Base Bankruptcy Petitions, 2007",
-            "description": "The purpose of this data collection is to provide an official public record\r\nof the business of the federal bankruptcy courts. The data include all\r\npetitions filed under the Bankruptcy Code in the United States Bankruptcy\r\nCourts on or after October 1, 2006, and any petitions filed before October 1, 2006, that were still pending on that date. The records are organized according to the fiscal year of termination with cases still pending at the end included in a separate pending dataset. The records in Part 1, Terminations Data, 2007, include cases that terminated in the year 2007. The records in Part 2, Pending Data, 2007, include cases that were still pending as of October 1, 2007. For the bankruptcy data, the unit of analysis is a single case.",
-            "modified": "2011-03-08T09:44:33",
-            "accessLevel": "restricted public",
-            "identifier": "2274",
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
+            "title": "Federal Court Cases: Integrated Data Base Bankruptcy Petitions, 2006"
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
+            "description": "The purpose of this data collection is to provide an official public record\r\nof the business of the federal bankruptcy courts. The data include all\r\npetitions filed under the Bankruptcy Code in the United States Bankruptcy\r\nCourts on or after October 1, 2006, and any petitions filed before October 1, 2006, that were still pending on that date. The records are organized according to the fiscal year of termination with cases still pending at the end included in a separate pending dataset. The records in Part 1, Terminations Data, 2007, include cases that terminated in the year 2007. The records in Part 2, Pending Data, 2007, include cases that were still pending as of October 1, 2007. For the bankruptcy data, the unit of analysis is a single case.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR23082.v2",
+                    "title": "Federal Court Cases: Integrated Data Base Bankruptcy Petitions, 2007"
+                }
+            ],
+            "identifier": "2274",
+            "isPartOf": "2173",
+            "issued": "2008-12-17T14:58:27",
             "keyword": [
                 "administration",
                 "appellate courts",
@@ -55040,55 +55034,55 @@
                 "trial courts",
                 "trial procedures"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T09:44:33",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2173",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2008-12-17T14:58:27",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR23082.v2",
-                    "title": "Federal Court Cases: Integrated Data Base Bankruptcy Petitions, 2007"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, 1980",
-            "description": "These data provide information on the number of arrests\r\nreported to the Federal Bureau of Investigation's Uniform Crime\r\nReporting (UCR) Program each year by police agencies in the United\r\nStates. These arrest reports provide data on 43 offenses including\r\nviolent crime, drug use, gambling, and larceny. The data received by\r\nICPSR were structured as a hierarchical file containing (per reporting\r\npolice agency) an agency header record, 1 to 12 monthly header\r\nrecords, and 1 to 43 detail offense records containing the counts of\r\narrests by age, sex, and race for a particular offense. ICPSR\r\nrestructured the original data to a rectangular format.",
-            "modified": "2009-02-13T15:09:03",
-            "accessLevel": "public",
-            "identifier": "2275",
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
+            "title": "Federal Court Cases: Integrated Data Base Bankruptcy Petitions, 2007"
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
+            "description": "These data provide information on the number of arrests\r\nreported to the Federal Bureau of Investigation's Uniform Crime\r\nReporting (UCR) Program each year by police agencies in the United\r\nStates. These arrest reports provide data on 43 offenses including\r\nviolent crime, drug use, gambling, and larceny. The data received by\r\nICPSR were structured as a hierarchical file containing (per reporting\r\npolice agency) an agency header record, 1 to 12 monthly header\r\nrecords, and 1 to 43 detail offense records containing the counts of\r\narrests by age, sex, and race for a particular offense. ICPSR\r\nrestructured the original data to a rectangular format.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR23320.v1",
+                    "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, 1980"
+                }
+            ],
+            "identifier": "2275",
+            "isPartOf": "2167",
+            "issued": "2009-02-13T15:09:03",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -55113,54 +55107,54 @@
                 "vandalism",
                 "weapons"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2009-02-13T15:09:03",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2009-02-13T15:09:03",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR23320.v1",
-                    "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, 1980"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, Summarized Yearly, 1980",
-            "description": "These data provide information on the number of arrests\r\nreported to the Federal Bureau of Investigation's Uniform Crime\r\nReporting (UCR) Program each year by police agencies in the United\r\nStates. These arrest reports provide data on 43 offenses including\r\nviolent crime, drug use, gambling, and larceny. The data received by\r\nICPSR were structured as a hierarchical file containing, per reporting\r\npolice agency: an agency header record, and 1 to 43 detail offense\r\nrecords containing the counts of arrests by age, sex, and race for a\r\nparticular offense. ICPSR restructured the original data to logical\r\nrecord length format with the agency header record variables copied\r\nonto the detail records. Consequently, each record contains arrest\r\ncounts for a particular agency-offense.",
-            "modified": "2009-09-21T17:39:24",
-            "accessLevel": "public",
-            "identifier": "2276",
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
+            "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, 1980"
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
+            "description": "These data provide information on the number of arrests\r\nreported to the Federal Bureau of Investigation's Uniform Crime\r\nReporting (UCR) Program each year by police agencies in the United\r\nStates. These arrest reports provide data on 43 offenses including\r\nviolent crime, drug use, gambling, and larceny. The data received by\r\nICPSR were structured as a hierarchical file containing, per reporting\r\npolice agency: an agency header record, and 1 to 43 detail offense\r\nrecords containing the counts of arrests by age, sex, and race for a\r\nparticular offense. ICPSR restructured the original data to logical\r\nrecord length format with the agency header record variables copied\r\nonto the detail records. Consequently, each record contains arrest\r\ncounts for a particular agency-offense.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR23321.v1",
+                    "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, Summarized Yearly, 1980"
+                }
+            ],
+            "identifier": "2276",
+            "isPartOf": "2167",
+            "issued": "2009-09-21T17:39:24",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrest records",
@@ -55176,54 +55170,54 @@
                 "offenses",
                 "violent crime"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2009-09-21T17:39:24",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2009-09-21T17:39:24",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR23321.v1",
-                    "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, Summarized Yearly, 1980"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, 1981",
-            "description": "These data provide information on the number of arrests\r\nreported to the Federal Bureau of Investigation's Uniform Crime\r\nReporting (UCR) Program each year by police agencies in the United\r\nStates. These arrest reports provide data on 43 offenses including\r\nviolent crime, drug use, gambling, and larceny. The data received by\r\nICPSR were structured as a hierarchical file containing (per reporting\r\npolice agency) an agency header record, 1 to 12 monthly header\r\nrecords, and 1 to 43 detail offense records containing the counts of\r\narrests by age, sex, and race for a particular offense. ICPSR\r\nrestructured the original data to a rectangular format.",
-            "modified": "2009-02-26T17:04:09",
-            "accessLevel": "public",
-            "identifier": "2277",
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
+            "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, Summarized Yearly, 1980"
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
+            "description": "These data provide information on the number of arrests\r\nreported to the Federal Bureau of Investigation's Uniform Crime\r\nReporting (UCR) Program each year by police agencies in the United\r\nStates. These arrest reports provide data on 43 offenses including\r\nviolent crime, drug use, gambling, and larceny. The data received by\r\nICPSR were structured as a hierarchical file containing (per reporting\r\npolice agency) an agency header record, 1 to 12 monthly header\r\nrecords, and 1 to 43 detail offense records containing the counts of\r\narrests by age, sex, and race for a particular offense. ICPSR\r\nrestructured the original data to a rectangular format.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR23322.v1",
+                    "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, 1981"
+                }
+            ],
+            "identifier": "2277",
+            "isPartOf": "2167",
+            "issued": "2009-02-26T17:04:09",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -55248,54 +55242,54 @@
                 "vandalism",
                 "weapons"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2009-02-26T17:04:09",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2009-02-26T17:04:09",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR23322.v1",
-                    "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, 1981"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, Summarized Yearly, 1981",
-            "description": "These data provide information on the number of arrests\r\nreported to the Federal Bureau of Investigation's Uniform Crime\r\nReporting (UCR) Program each year by police agencies in the United\r\nStates. These arrest reports provide data on 43 offenses including\r\nviolent crime, drug use, gambling, and larceny. The data received by\r\nICPSR were structured as a hierarchical file containing, per reporting\r\npolice agency: an agency header record, and 1 to 43 detail offense\r\nrecords containing the counts of arrests by age, sex, and race for a\r\nparticular offense. ICPSR restructured the original data to logical\r\nrecord length format with the agency header record variables copied\r\nonto the detail records. Consequently, each record contains arrest\r\ncounts for a particular agency-offense.",
-            "modified": "2009-09-21T17:42:47",
-            "accessLevel": "public",
-            "identifier": "2278",
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
+            "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, 1981"
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
+            "description": "These data provide information on the number of arrests\r\nreported to the Federal Bureau of Investigation's Uniform Crime\r\nReporting (UCR) Program each year by police agencies in the United\r\nStates. These arrest reports provide data on 43 offenses including\r\nviolent crime, drug use, gambling, and larceny. The data received by\r\nICPSR were structured as a hierarchical file containing, per reporting\r\npolice agency: an agency header record, and 1 to 43 detail offense\r\nrecords containing the counts of arrests by age, sex, and race for a\r\nparticular offense. ICPSR restructured the original data to logical\r\nrecord length format with the agency header record variables copied\r\nonto the detail records. Consequently, each record contains arrest\r\ncounts for a particular agency-offense.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR23323.v1",
+                    "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, Summarized Yearly, 1981"
+                }
+            ],
+            "identifier": "2278",
+            "isPartOf": "2167",
+            "issued": "2009-09-21T17:42:47",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrest records",
@@ -55311,54 +55305,54 @@
                 "offenses",
                 "violent crime"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2009-09-21T17:42:47",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2009-09-21T17:42:47",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR23323.v1",
-                    "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, Summarized Yearly, 1981"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, 1982",
-            "description": "These data provide information on the number of arrests\r\nreported to the Federal Bureau of Investigation's Uniform Crime\r\nReporting (UCR) Program each year by police agencies in the United\r\nStates. These arrest reports provide data on 43 offenses including\r\nviolent crime, drug use, gambling, and larceny. The data received by\r\nICPSR were structured as a hierarchical file containing (per reporting\r\npolice agency) an agency header record, 1 to 12 monthly header\r\nrecords, and 1 to 43 detail offense records containing the counts of\r\narrests by age, sex, and race for a particular offense. ICPSR\r\nrestructured the original data to a rectangular format.",
-            "modified": "2009-02-26T17:04:56",
-            "accessLevel": "public",
-            "identifier": "2279",
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
+            "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, Summarized Yearly, 1981"
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
+            "description": "These data provide information on the number of arrests\r\nreported to the Federal Bureau of Investigation's Uniform Crime\r\nReporting (UCR) Program each year by police agencies in the United\r\nStates. These arrest reports provide data on 43 offenses including\r\nviolent crime, drug use, gambling, and larceny. The data received by\r\nICPSR were structured as a hierarchical file containing (per reporting\r\npolice agency) an agency header record, 1 to 12 monthly header\r\nrecords, and 1 to 43 detail offense records containing the counts of\r\narrests by age, sex, and race for a particular offense. ICPSR\r\nrestructured the original data to a rectangular format.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR23324.v1",
+                    "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, 1982"
+                }
+            ],
+            "identifier": "2279",
+            "isPartOf": "2167",
+            "issued": "2009-02-26T17:04:56",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -55383,54 +55377,54 @@
                 "vandalism",
                 "weapons"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2009-02-26T17:04:56",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2009-02-26T17:04:56",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR23324.v1",
-                    "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, 1982"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, Summarized Yearly, 1982",
-            "description": "These data provide information on the number of arrests\r\nreported to the Federal Bureau of Investigation's Uniform Crime\r\nReporting (UCR) Program each year by police agencies in the United\r\nStates. These arrest reports provide data on 43 offenses including\r\nviolent crime, drug use, gambling, and larceny. The data received by\r\nICPSR were structured as a hierarchical file containing, per reporting\r\npolice agency: an agency header record, and 1 to 43 detail offense\r\nrecords containing the counts of arrests by age, sex, and race for a\r\nparticular offense. ICPSR restructured the original data to logical\r\nrecord length format with the agency header record variables copied\r\nonto the detail records. Consequently, each record contains arrest\r\ncounts for a particular agency-offense.",
-            "modified": "2009-09-21T17:45:35",
-            "accessLevel": "public",
-            "identifier": "2280",
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
+            "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, 1982"
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
+            "description": "These data provide information on the number of arrests\r\nreported to the Federal Bureau of Investigation's Uniform Crime\r\nReporting (UCR) Program each year by police agencies in the United\r\nStates. These arrest reports provide data on 43 offenses including\r\nviolent crime, drug use, gambling, and larceny. The data received by\r\nICPSR were structured as a hierarchical file containing, per reporting\r\npolice agency: an agency header record, and 1 to 43 detail offense\r\nrecords containing the counts of arrests by age, sex, and race for a\r\nparticular offense. ICPSR restructured the original data to logical\r\nrecord length format with the agency header record variables copied\r\nonto the detail records. Consequently, each record contains arrest\r\ncounts for a particular agency-offense.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR23325.v1",
+                    "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, Summarized Yearly, 1982"
+                }
+            ],
+            "identifier": "2280",
+            "isPartOf": "2167",
+            "issued": "2009-09-21T17:45:35",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrest records",
@@ -55446,54 +55440,54 @@
                 "offenses",
                 "violent crime"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2009-09-21T17:45:35",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2009-09-21T17:45:35",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR23325.v1",
-                    "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, Summarized Yearly, 1982"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data: Arrests by Age, Sex, and Race, United States, 1983",
-            "description": "These data provide information on the number of arrests\r\nreported to the Federal Bureau of Investigation's (FBI) Uniform Crime\r\nReporting (UCR) Program each year by police agencies in the United\r\nStates. Although not as well known as the \"Crimes Known to the Police\" data drawn from the Uniform crime report's Return A form, the arrest reports by age, sex, and race provide valuable data on 43 offenses including violent, drug, gambling, and larceny crimes.",
-            "modified": "2014-10-16T08:19:07",
-            "accessLevel": "public",
-            "identifier": "2281",
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
+            "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, Summarized Yearly, 1982"
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
+            "description": "These data provide information on the number of arrests\r\nreported to the Federal Bureau of Investigation's (FBI) Uniform Crime\r\nReporting (UCR) Program each year by police agencies in the United\r\nStates. Although not as well known as the \"Crimes Known to the Police\" data drawn from the Uniform crime report's Return A form, the arrest reports by age, sex, and race provide valuable data on 43 offenses including violent, drug, gambling, and larceny crimes.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR23326.v2",
+                    "title": "Uniform Crime Reporting Program Data: Arrests by Age, Sex, and Race, United States, 1983"
+                }
+            ],
+            "identifier": "2281",
+            "isPartOf": "2167",
+            "issued": "2009-02-26T17:13:56",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -55518,54 +55512,54 @@
                 "vandalism",
                 "weapons"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2014-10-16T08:19:07",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2009-02-26T17:13:56",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR23326.v2",
-                    "title": "Uniform Crime Reporting Program Data: Arrests by Age, Sex, and Race, United States, 1983"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, Summarized Yearly, 1983",
-            "description": "These data provide information on the number of arrests\r\nreported to the Federal Bureau of Investigation's Uniform Crime\r\nReporting (UCR) Program each year by police agencies in the United\r\nStates. These arrest reports provide data on 43 offenses including\r\nviolent crime, drug use, gambling, and larceny. The data received by\r\nICPSR were structured as a hierarchical file containing, per reporting\r\npolice agency: an agency header record, and 1 to 43 detail offense\r\nrecords containing the counts of arrests by age, sex, and race for a\r\nparticular offense. ICPSR restructured the original data to logical\r\nrecord length format with the agency header record variables copied\r\nonto the detail records. Consequently, each record contains arrest\r\ncounts for a particular agency-offense.",
-            "modified": "2009-09-21T17:48:20",
-            "accessLevel": "public",
-            "identifier": "2282",
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
+            "title": "Uniform Crime Reporting Program Data: Arrests by Age, Sex, and Race, United States, 1983"
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
+            "description": "These data provide information on the number of arrests\r\nreported to the Federal Bureau of Investigation's Uniform Crime\r\nReporting (UCR) Program each year by police agencies in the United\r\nStates. These arrest reports provide data on 43 offenses including\r\nviolent crime, drug use, gambling, and larceny. The data received by\r\nICPSR were structured as a hierarchical file containing, per reporting\r\npolice agency: an agency header record, and 1 to 43 detail offense\r\nrecords containing the counts of arrests by age, sex, and race for a\r\nparticular offense. ICPSR restructured the original data to logical\r\nrecord length format with the agency header record variables copied\r\nonto the detail records. Consequently, each record contains arrest\r\ncounts for a particular agency-offense.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR23327.v1",
+                    "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, Summarized Yearly, 1983"
+                }
+            ],
+            "identifier": "2282",
+            "isPartOf": "2167",
+            "issued": "2009-09-21T17:48:20",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrest records",
@@ -55581,54 +55575,54 @@
                 "offenses",
                 "violent crime"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2009-09-21T17:48:20",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2009-09-21T17:48:20",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR23327.v1",
-                    "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, Summarized Yearly, 1983"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, 1984",
-            "description": "These data provide information on the number of arrests\r\nreported to the Federal Bureau of Investigation's Uniform Crime\r\nReporting (UCR) Program each year by police agencies in the United\r\nStates. These arrest reports provide data on 43 offenses including\r\nviolent crime, drug use, gambling, and larceny. The data received by\r\nICPSR were structured as a hierarchical file containing (per reporting\r\npolice agency) an agency header record, 1 to 12 monthly header\r\nrecords, and 1 to 43 detail offense records containing the counts of\r\narrests by age, sex, and race for a particular offense. ICPSR\r\nrestructured the original data to a rectangular format.",
-            "modified": "2014-03-05T13:20:26",
-            "accessLevel": "public",
-            "identifier": "2283",
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
+            "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, Summarized Yearly, 1983"
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
+            "description": "These data provide information on the number of arrests\r\nreported to the Federal Bureau of Investigation's Uniform Crime\r\nReporting (UCR) Program each year by police agencies in the United\r\nStates. These arrest reports provide data on 43 offenses including\r\nviolent crime, drug use, gambling, and larceny. The data received by\r\nICPSR were structured as a hierarchical file containing (per reporting\r\npolice agency) an agency header record, 1 to 12 monthly header\r\nrecords, and 1 to 43 detail offense records containing the counts of\r\narrests by age, sex, and race for a particular offense. ICPSR\r\nrestructured the original data to a rectangular format.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR23328.v1",
+                    "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, 1984"
+                }
+            ],
+            "identifier": "2283",
+            "isPartOf": "2167",
+            "issued": "2014-03-05T13:20:26",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -55653,54 +55647,54 @@
                 "vandalism",
                 "weapons"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2014-03-05T13:20:26",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2014-03-05T13:20:26",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR23328.v1",
-                    "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, 1984"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, Summarized Yearly, 1984",
-            "description": "These data provide information on the number of arrests\r\nreported to the Federal Bureau of Investigation's Uniform Crime\r\nReporting (UCR) Program each year by police agencies in the United\r\nStates. These arrest reports provide data on 43 offenses including\r\nviolent crime, drug use, gambling, and larceny. The data received by\r\nICPSR were structured as a hierarchical file containing, per reporting\r\npolice agency: an agency header record, and 1 to 43 detail offense\r\nrecords containing the counts of arrests by age, sex, and race for a\r\nparticular offense. ICPSR restructured the original data to logical\r\nrecord length format with the agency header record variables copied\r\nonto the detail records. Consequently, each record contains arrest\r\ncounts for a particular agency-offense.",
-            "modified": "2009-09-21T17:51:10",
-            "accessLevel": "public",
-            "identifier": "2284",
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
+            "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, 1984"
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
+            "description": "These data provide information on the number of arrests\r\nreported to the Federal Bureau of Investigation's Uniform Crime\r\nReporting (UCR) Program each year by police agencies in the United\r\nStates. These arrest reports provide data on 43 offenses including\r\nviolent crime, drug use, gambling, and larceny. The data received by\r\nICPSR were structured as a hierarchical file containing, per reporting\r\npolice agency: an agency header record, and 1 to 43 detail offense\r\nrecords containing the counts of arrests by age, sex, and race for a\r\nparticular offense. ICPSR restructured the original data to logical\r\nrecord length format with the agency header record variables copied\r\nonto the detail records. Consequently, each record contains arrest\r\ncounts for a particular agency-offense.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR23329.v1",
+                    "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, Summarized Yearly, 1984"
+                }
+            ],
+            "identifier": "2284",
+            "isPartOf": "2167",
+            "issued": "2009-09-21T17:51:10",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrest records",
@@ -55716,54 +55710,54 @@
                 "offenses",
                 "violent crime"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2009-09-21T17:51:10",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2009-09-21T17:51:10",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR23329.v1",
-                    "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, Summarized Yearly, 1984"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data [United States]: County-Level Detailed Arrest and Offense Data, 2006",
-            "description": "This data collection contains county-level counts of\r\narrests and offenses for Part I offenses (murder, rape, robbery,\r\naggravated assault, burglary, larceny, auto theft, and arson) and\r\ncounts of arrests for Part II offenses (forgery, fraud, embezzlement,\r\nvandalism, weapons violations, sex offenses, drug and alcohol abuse\r\nviolations, gambling, vagrancy, curfew violations, and runaways).",
-            "modified": "2008-12-12T10:19:24",
-            "accessLevel": "public",
-            "identifier": "2285",
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
+            "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, Summarized Yearly, 1984"
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
+                    "accessURL": "https://doi.org/10.3886/ICPSR23780.v1",
+                    "title": "Uniform Crime Reporting Program Data [United States]: County-Level Detailed Arrest and Offense Data, 2006"
+                }
+            ],
+            "identifier": "2285",
+            "isPartOf": "2167",
+            "issued": "2008-12-12T10:19:24",
             "keyword": [
                 "Uniform Crime Reports",
                 "aggravated assault",
@@ -55792,54 +55786,54 @@
                 "vandalism",
                 "weapons offenses"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-12-12T10:19:24",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2008-12-12T10:19:24",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR23780.v1",
-                    "title": "Uniform Crime Reporting Program Data [United States]: County-Level Detailed Arrest and Offense Data, 2006"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data [United States]: Hate Crime Data, 2001 [Record-Type Files]",
-            "description": "In response to a growing concern about hate crimes, the\r\nUnited States Congress enacted the Hate Crime Statistics Act of\r\n1990. The Act requires the attorney general to establish guidelines\r\nand collect, as part of the Uniform Crime Reporting (UCR) Program,\r\ndata \"about crimes that manifest evidence of prejudice based on race,\r\nreligion, sexual orientation, or ethnicity, including where\r\nappropriate the crimes of murder and non-negligent manslaughter,\r\nforcible rape, aggravated assault, simple assault, intimidation,\r\narson, and destruction, damage or vandalism of property.\" Hate crime\r\ndata collection was required by the Act to begin in calendar year 1990\r\nand to continue for four successive years. In September 1994, the\r\nViolent Crime Control and Law Enforcement Act amended the Hate Crime\r\nStatistics Act to add disabilities, both physical and mental, as\r\nfactors that could be considered a basis for hate crimes. Although the\r\nAct originally mandated data collection for five years, the Church\r\nArson Prevention Act of 1996 amended the collection duration \"for each\r\ncalendar year,\" making hate crime statistics a permanent addition to\r\nthe UCR program. As with the other UCR data, law enforcement agencies\r\ncontribute reports either directly or through their state reporting\r\nprograms. Information contained in the data includes number of victims\r\nand offenders involved in each hate crime incident, type of victims,\r\nbias motivation, offense type, and location type.",
-            "modified": "2008-11-14T15:38:17",
-            "accessLevel": "public",
-            "identifier": "2286",
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
+            "title": "Uniform Crime Reporting Program Data [United States]: County-Level Detailed Arrest and Offense Data, 2006"
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
+            "description": "In response to a growing concern about hate crimes, the\r\nUnited States Congress enacted the Hate Crime Statistics Act of\r\n1990. The Act requires the attorney general to establish guidelines\r\nand collect, as part of the Uniform Crime Reporting (UCR) Program,\r\ndata \"about crimes that manifest evidence of prejudice based on race,\r\nreligion, sexual orientation, or ethnicity, including where\r\nappropriate the crimes of murder and non-negligent manslaughter,\r\nforcible rape, aggravated assault, simple assault, intimidation,\r\narson, and destruction, damage or vandalism of property.\" Hate crime\r\ndata collection was required by the Act to begin in calendar year 1990\r\nand to continue for four successive years. In September 1994, the\r\nViolent Crime Control and Law Enforcement Act amended the Hate Crime\r\nStatistics Act to add disabilities, both physical and mental, as\r\nfactors that could be considered a basis for hate crimes. Although the\r\nAct originally mandated data collection for five years, the Church\r\nArson Prevention Act of 1996 amended the collection duration \"for each\r\ncalendar year,\" making hate crime statistics a permanent addition to\r\nthe UCR program. As with the other UCR data, law enforcement agencies\r\ncontribute reports either directly or through their state reporting\r\nprograms. Information contained in the data includes number of victims\r\nand offenders involved in each hate crime incident, type of victims,\r\nbias motivation, offense type, and location type.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR23781.v1",
+                    "title": "Uniform Crime Reporting Program Data [United States]: Hate Crime Data, 2001 [Record-Type Files]"
+                }
+            ],
+            "identifier": "2286",
+            "isPartOf": "2167",
+            "issued": "2008-11-14T15:38:17",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -55858,54 +55852,54 @@
                 "religion",
                 "violence"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-11-14T15:38:17",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2008-11-14T15:38:17",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR23781.v1",
-                    "title": "Uniform Crime Reporting Program Data [United States]: Hate Crime Data, 2001 [Record-Type Files]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data [United States]: Hate Crime Data, 2000 [Record-Type Files]",
-            "description": "In response to a growing concern about hate crimes, the\r\nUnited States Congress enacted the Hate Crime Statistics Act of\r\n1990. The Act requires the attorney general to establish guidelines\r\nand collect, as part of the Uniform Crime Reporting (UCR) Program,\r\ndata \"about crimes that manifest evidence of prejudice based on race,\r\nreligion, sexual orientation, or ethnicity, including where\r\nappropriate the crimes of murder and non-negligent manslaughter,\r\nforcible rape, aggravated assault, simple assault, intimidation,\r\narson, and destruction, damage or vandalism of property.\" Hate crime\r\ndata collection was required by the Act to begin in calendar year 1990\r\nand to continue for four successive years. In September 1994, the\r\nViolent Crime Control and Law Enforcement Act amended the Hate Crime\r\nStatistics Act to add disabilities, both physical and mental, as\r\nfactors that could be considered a basis for hate crimes. Although the\r\nAct originally mandated data collection for five years, the Church\r\nArson Prevention Act of 1996 amended the collection duration \"for each\r\ncalendar year,\" making hate crime statistics a permanent addition to\r\nthe UCR program. As with the other UCR data, law enforcement agencies\r\ncontribute reports either directly or through their state reporting\r\nprograms. Information contained in the data includes number of victims\r\nand offenders involved in each hate crime incident, type of victims,\r\nbias motivation, offense type, and location type.",
-            "modified": "2008-11-14T15:35:08",
-            "accessLevel": "public",
-            "identifier": "2287",
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
+            "title": "Uniform Crime Reporting Program Data [United States]: Hate Crime Data, 2001 [Record-Type Files]"
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
+            "description": "In response to a growing concern about hate crimes, the\r\nUnited States Congress enacted the Hate Crime Statistics Act of\r\n1990. The Act requires the attorney general to establish guidelines\r\nand collect, as part of the Uniform Crime Reporting (UCR) Program,\r\ndata \"about crimes that manifest evidence of prejudice based on race,\r\nreligion, sexual orientation, or ethnicity, including where\r\nappropriate the crimes of murder and non-negligent manslaughter,\r\nforcible rape, aggravated assault, simple assault, intimidation,\r\narson, and destruction, damage or vandalism of property.\" Hate crime\r\ndata collection was required by the Act to begin in calendar year 1990\r\nand to continue for four successive years. In September 1994, the\r\nViolent Crime Control and Law Enforcement Act amended the Hate Crime\r\nStatistics Act to add disabilities, both physical and mental, as\r\nfactors that could be considered a basis for hate crimes. Although the\r\nAct originally mandated data collection for five years, the Church\r\nArson Prevention Act of 1996 amended the collection duration \"for each\r\ncalendar year,\" making hate crime statistics a permanent addition to\r\nthe UCR program. As with the other UCR data, law enforcement agencies\r\ncontribute reports either directly or through their state reporting\r\nprograms. Information contained in the data includes number of victims\r\nand offenders involved in each hate crime incident, type of victims,\r\nbias motivation, offense type, and location type.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR23783.v1",
+                    "title": "Uniform Crime Reporting Program Data [United States]: Hate Crime Data, 2000 [Record-Type Files]"
+                }
+            ],
+            "identifier": "2287",
+            "isPartOf": "2167",
+            "issued": "2008-11-14T15:35:08",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -55924,54 +55918,54 @@
                 "religion",
                 "violence"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-11-14T15:35:08",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2008-11-14T15:35:08",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR23783.v1",
-                    "title": "Uniform Crime Reporting Program Data [United States]: Hate Crime Data, 2000 [Record-Type Files]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data [United States]: Hate Crime Data, 1999 [Record-Type Files]",
-            "description": "In response to a growing concern about hate crimes, the\r\nUnited States Congress enacted the Hate Crime Statistics Act of\r\n1990. The Act requires the attorney general to establish guidelines\r\nand collect, as part of the Uniform Crime Reporting (UCR) Program,\r\ndata \"about crimes that manifest evidence of prejudice based on race,\r\nreligion, sexual orientation, or ethnicity, including where\r\nappropriate the crimes of murder and non-negligent manslaughter,\r\nforcible rape, aggravated assault, simple assault, intimidation,\r\narson, and destruction, damage or vandalism of property.\" Hate crime\r\ndata collection was required by the Act to begin in calendar year 1990\r\nand to continue for four successive years. In September 1994, the\r\nViolent Crime Control and Law Enforcement Act amended the Hate Crime\r\nStatistics Act to add disabilities, both physical and mental, as\r\nfactors that could be considered a basis for hate crimes. Although the\r\nAct originally mandated data collection for five years, the Church\r\nArson Prevention Act of 1996 amended the collection duration \"for each\r\ncalendar year,\" making hate crime statistics a permanent addition to\r\nthe UCR program. As with the other UCR data, law enforcement agencies\r\ncontribute reports either directly or through their state reporting\r\nprograms. Information contained in the data includes number of victims\r\nand offenders involved in each hate crime incident, type of victims,\r\nbias motivation, offense type, and location type.",
-            "modified": "2008-11-18T09:41:24",
-            "accessLevel": "public",
-            "identifier": "2288",
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
+            "title": "Uniform Crime Reporting Program Data [United States]: Hate Crime Data, 2000 [Record-Type Files]"
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
+            "description": "In response to a growing concern about hate crimes, the\r\nUnited States Congress enacted the Hate Crime Statistics Act of\r\n1990. The Act requires the attorney general to establish guidelines\r\nand collect, as part of the Uniform Crime Reporting (UCR) Program,\r\ndata \"about crimes that manifest evidence of prejudice based on race,\r\nreligion, sexual orientation, or ethnicity, including where\r\nappropriate the crimes of murder and non-negligent manslaughter,\r\nforcible rape, aggravated assault, simple assault, intimidation,\r\narson, and destruction, damage or vandalism of property.\" Hate crime\r\ndata collection was required by the Act to begin in calendar year 1990\r\nand to continue for four successive years. In September 1994, the\r\nViolent Crime Control and Law Enforcement Act amended the Hate Crime\r\nStatistics Act to add disabilities, both physical and mental, as\r\nfactors that could be considered a basis for hate crimes. Although the\r\nAct originally mandated data collection for five years, the Church\r\nArson Prevention Act of 1996 amended the collection duration \"for each\r\ncalendar year,\" making hate crime statistics a permanent addition to\r\nthe UCR program. As with the other UCR data, law enforcement agencies\r\ncontribute reports either directly or through their state reporting\r\nprograms. Information contained in the data includes number of victims\r\nand offenders involved in each hate crime incident, type of victims,\r\nbias motivation, offense type, and location type.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR23800.v1",
+                    "title": "Uniform Crime Reporting Program Data [United States]: Hate Crime Data, 1999 [Record-Type Files]"
+                }
+            ],
+            "identifier": "2288",
+            "isPartOf": "2167",
+            "issued": "2008-11-18T09:41:24",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -55990,54 +55984,54 @@
                 "religion",
                 "violence"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-11-18T09:41:24",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2008-11-18T09:41:24",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR23800.v1",
-                    "title": "Uniform Crime Reporting Program Data [United States]: Hate Crime Data, 1999 [Record-Type Files]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data [United States]: Hate Crime Data, 1998 [Record-Type Files]",
-            "description": "In response to a growing concern about hate crimes, the\r\nUnited States Congress enacted the Hate Crime Statistics Act of\r\n1990. The Act requires the attorney general to establish guidelines\r\nand collect, as part of the Uniform Crime Reporting (UCR) Program,\r\ndata \"about crimes that manifest evidence of prejudice based on race,\r\nreligion, sexual orientation, or ethnicity, including where\r\nappropriate the crimes of murder and non-negligent manslaughter,\r\nforcible rape, aggravated assault, simple assault, intimidation,\r\narson, and destruction, damage or vandalism of property.\" Hate crime\r\ndata collection was required by the Act to begin in calendar year 1990\r\nand to continue for four successive years. In September 1994, the\r\nViolent Crime Control and Law Enforcement Act amended the Hate Crime\r\nStatistics Act to add disabilities, both physical and mental, as\r\nfactors that could be considered a basis for hate crimes. Although the\r\nAct originally mandated data collection for five years, the Church\r\nArson Prevention Act of 1996 amended the collection duration \"for each\r\ncalendar year,\" making hate crime statistics a permanent addition to\r\nthe UCR program. As with the other UCR data, law enforcement agencies\r\ncontribute reports either directly or through their state reporting\r\nprograms. Information contained in the data includes number of victims\r\nand offenders involved in each hate crime incident, type of victims,\r\nbias motivation, offense type, and location type.",
-            "modified": "2008-11-18T09:38:28",
-            "accessLevel": "public",
-            "identifier": "2289",
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
+            "title": "Uniform Crime Reporting Program Data [United States]: Hate Crime Data, 1999 [Record-Type Files]"
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
+            "description": "In response to a growing concern about hate crimes, the\r\nUnited States Congress enacted the Hate Crime Statistics Act of\r\n1990. The Act requires the attorney general to establish guidelines\r\nand collect, as part of the Uniform Crime Reporting (UCR) Program,\r\ndata \"about crimes that manifest evidence of prejudice based on race,\r\nreligion, sexual orientation, or ethnicity, including where\r\nappropriate the crimes of murder and non-negligent manslaughter,\r\nforcible rape, aggravated assault, simple assault, intimidation,\r\narson, and destruction, damage or vandalism of property.\" Hate crime\r\ndata collection was required by the Act to begin in calendar year 1990\r\nand to continue for four successive years. In September 1994, the\r\nViolent Crime Control and Law Enforcement Act amended the Hate Crime\r\nStatistics Act to add disabilities, both physical and mental, as\r\nfactors that could be considered a basis for hate crimes. Although the\r\nAct originally mandated data collection for five years, the Church\r\nArson Prevention Act of 1996 amended the collection duration \"for each\r\ncalendar year,\" making hate crime statistics a permanent addition to\r\nthe UCR program. As with the other UCR data, law enforcement agencies\r\ncontribute reports either directly or through their state reporting\r\nprograms. Information contained in the data includes number of victims\r\nand offenders involved in each hate crime incident, type of victims,\r\nbias motivation, offense type, and location type.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR23821.v1",
+                    "title": "Uniform Crime Reporting Program Data [United States]: Hate Crime Data, 1998 [Record-Type Files]"
+                }
+            ],
+            "identifier": "2289",
+            "isPartOf": "2167",
+            "issued": "2008-11-18T09:38:28",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -56056,54 +56050,54 @@
                 "religion",
                 "violence"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-11-18T09:38:28",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2008-11-18T09:38:28",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR23821.v1",
-                    "title": "Uniform Crime Reporting Program Data [United States]: Hate Crime Data, 1998 [Record-Type Files]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data [United States]: Hate Crime Data, 1997 [Record-Type Files]",
-            "description": "In response to a growing concern about hate crimes, the\r\nUnited States Congress enacted the Hate Crime Statistics Act of\r\n1990. The Act requires the attorney general to establish guidelines\r\nand collect, as part of the Uniform Crime Reporting (UCR) Program,\r\ndata \"about crimes that manifest evidence of prejudice based on race,\r\nreligion, sexual orientation, or ethnicity, including where\r\nappropriate the crimes of murder and non-negligent manslaughter,\r\nforcible rape, aggravated assault, simple assault, intimidation,\r\narson, and destruction, damage or vandalism of property.\" Hate crime\r\ndata collection was required by the Act to begin in calendar year 1990\r\nand to continue for four successive years. In September 1994, the\r\nViolent Crime Control and Law Enforcement Act amended the Hate Crime\r\nStatistics Act to add disabilities, both physical and mental, as\r\nfactors that could be considered a basis for hate crimes. Although the\r\nAct originally mandated data collection for five years, the Church\r\nArson Prevention Act of 1996 amended the collection duration \"for each\r\ncalendar year,\" making hate crime statistics a permanent addition to\r\nthe UCR program. As with the other UCR data, law enforcement agencies\r\ncontribute reports either directly or through their state reporting\r\nprograms. Information contained in the data includes number of victims\r\nand offenders involved in each hate crime incident, type of victims,\r\nbias motivation, offense type, and location type.",
-            "modified": "2008-11-18T09:35:28",
-            "accessLevel": "public",
-            "identifier": "2290",
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
+            "title": "Uniform Crime Reporting Program Data [United States]: Hate Crime Data, 1998 [Record-Type Files]"
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
+            "description": "In response to a growing concern about hate crimes, the\r\nUnited States Congress enacted the Hate Crime Statistics Act of\r\n1990. The Act requires the attorney general to establish guidelines\r\nand collect, as part of the Uniform Crime Reporting (UCR) Program,\r\ndata \"about crimes that manifest evidence of prejudice based on race,\r\nreligion, sexual orientation, or ethnicity, including where\r\nappropriate the crimes of murder and non-negligent manslaughter,\r\nforcible rape, aggravated assault, simple assault, intimidation,\r\narson, and destruction, damage or vandalism of property.\" Hate crime\r\ndata collection was required by the Act to begin in calendar year 1990\r\nand to continue for four successive years. In September 1994, the\r\nViolent Crime Control and Law Enforcement Act amended the Hate Crime\r\nStatistics Act to add disabilities, both physical and mental, as\r\nfactors that could be considered a basis for hate crimes. Although the\r\nAct originally mandated data collection for five years, the Church\r\nArson Prevention Act of 1996 amended the collection duration \"for each\r\ncalendar year,\" making hate crime statistics a permanent addition to\r\nthe UCR program. As with the other UCR data, law enforcement agencies\r\ncontribute reports either directly or through their state reporting\r\nprograms. Information contained in the data includes number of victims\r\nand offenders involved in each hate crime incident, type of victims,\r\nbias motivation, offense type, and location type.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR23840.v1",
+                    "title": "Uniform Crime Reporting Program Data [United States]: Hate Crime Data, 1997 [Record-Type Files]"
+                }
+            ],
+            "identifier": "2290",
+            "isPartOf": "2167",
+            "issued": "2008-11-18T09:35:28",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -56122,54 +56116,54 @@
                 "religion",
                 "violence"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-11-18T09:35:28",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2008-11-18T09:35:28",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR23840.v1",
-                    "title": "Uniform Crime Reporting Program Data [United States]: Hate Crime Data, 1997 [Record-Type Files]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data [United States]: Hate Crime Data, 1996 [Record-Type Files]",
-            "description": "In response to a growing concern about hate crimes, the\r\nUnited States Congress enacted the Hate Crime Statistics Act of\r\n1990. The Act requires the attorney general to establish guidelines\r\nand collect, as part of the Uniform Crime Reporting (UCR) Program,\r\ndata \"about crimes that manifest evidence of prejudice based on race,\r\nreligion, sexual orientation, or ethnicity, including where\r\nappropriate the crimes of murder and non-negligent manslaughter,\r\nforcible rape, aggravated assault, simple assault, intimidation,\r\narson, and destruction, damage or vandalism of property.\" Hate crime\r\ndata collection was required by the Act to begin in calendar year 1990\r\nand to continue for four successive years. In September 1994, the\r\nViolent Crime Control and Law Enforcement Act amended the Hate Crime\r\nStatistics Act to add disabilities, both physical and mental, as\r\nfactors that could be considered a basis for hate crimes. Although the\r\nAct originally mandated data collection for five years, the Church\r\nArson Prevention Act of 1996 amended the collection duration \"for each\r\ncalendar year,\" making hate crime statistics a permanent addition to\r\nthe UCR program. As with the other UCR data, law enforcement agencies\r\ncontribute reports either directly or through their state reporting\r\nprograms. Information contained in the data includes number of victims\r\nand offenders involved in each hate crime incident, type of victims,\r\nbias motivation, offense type, and location type.",
-            "modified": "2008-11-18T09:28:37",
-            "accessLevel": "public",
-            "identifier": "2291",
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
+            "title": "Uniform Crime Reporting Program Data [United States]: Hate Crime Data, 1997 [Record-Type Files]"
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
+            "description": "In response to a growing concern about hate crimes, the\r\nUnited States Congress enacted the Hate Crime Statistics Act of\r\n1990. The Act requires the attorney general to establish guidelines\r\nand collect, as part of the Uniform Crime Reporting (UCR) Program,\r\ndata \"about crimes that manifest evidence of prejudice based on race,\r\nreligion, sexual orientation, or ethnicity, including where\r\nappropriate the crimes of murder and non-negligent manslaughter,\r\nforcible rape, aggravated assault, simple assault, intimidation,\r\narson, and destruction, damage or vandalism of property.\" Hate crime\r\ndata collection was required by the Act to begin in calendar year 1990\r\nand to continue for four successive years. In September 1994, the\r\nViolent Crime Control and Law Enforcement Act amended the Hate Crime\r\nStatistics Act to add disabilities, both physical and mental, as\r\nfactors that could be considered a basis for hate crimes. Although the\r\nAct originally mandated data collection for five years, the Church\r\nArson Prevention Act of 1996 amended the collection duration \"for each\r\ncalendar year,\" making hate crime statistics a permanent addition to\r\nthe UCR program. As with the other UCR data, law enforcement agencies\r\ncontribute reports either directly or through their state reporting\r\nprograms. Information contained in the data includes number of victims\r\nand offenders involved in each hate crime incident, type of victims,\r\nbias motivation, offense type, and location type.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR23841.v1",
+                    "title": "Uniform Crime Reporting Program Data [United States]: Hate Crime Data, 1996 [Record-Type Files]"
+                }
+            ],
+            "identifier": "2291",
+            "isPartOf": "2167",
+            "issued": "2008-11-18T09:28:37",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -56188,54 +56182,53 @@
                 "religion",
                 "violence"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-11-18T09:28:37",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2008-11-18T09:28:37",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR23841.v1",
-                    "title": "Uniform Crime Reporting Program Data [United States]: Hate Crime Data, 1996 [Record-Type Files]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Executions in the United States, 1608-1940: The ESPY File -- Summary Data of Executions Collected by M. Watt Espy Between 1986 and 1996",
-            "description": "This collection consists of four summary variables based on new data collected by M. Watt Espy between 1986 and 1996 after he corrected and updated the data in 1992. See the related collection, EXECUTIONS IN THE UNITED STATES, 1608-2002: THE ESPY FILE (ICPSR 8451). The summary variables consist of the ethnicity of the executed, the state, territory, district or colony of execution, the decade of execution, and the geographical region of execution. They were complete as of March 1, 1996.",
-            "modified": "2008-12-12T08:18:31",
-            "accessLevel": "public",
-            "identifier": "2292",
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
+            "title": "Uniform Crime Reporting Program Data [United States]: Hate Crime Data, 1996 [Record-Type Files]"
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
+            "description": "This collection consists of four summary variables based on new data collected by M. Watt Espy between 1986 and 1996 after he corrected and updated the data in 1992. See the related collection, EXECUTIONS IN THE UNITED STATES, 1608-2002: THE ESPY FILE (ICPSR 8451). The summary variables consist of the ethnicity of the executed, the state, territory, district or colony of execution, the decade of execution, and the geographical region of execution. They were complete as of March 1, 1996.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR23900.v1",
+                    "title": "Executions in the United States, 1608-1940: The ESPY File -- Summary Data of Executions Collected by M. Watt Espy Between 1986 and 1996"
+                }
+            ],
+            "identifier": "2292",
+            "issued": "2008-12-12T08:18:31",
             "keyword": [
                 "capital punishment",
                 "crime",
@@ -56245,53 +56238,54 @@
                 "offenders",
                 "offenses"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-12-12T08:18:31",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "dataQuality": false,
-            "issued": "2008-12-12T08:18:31",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR23900.v1",
-                    "title": "Executions in the United States, 1608-1940: The ESPY File -- Summary Data of Executions Collected by M. Watt Espy Between 1986 and 1996"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data [United States]: Hate Crime Data, 1995 [Record-Type Files]",
-            "description": "In response to a growing concern about hate crimes, the\r\nUnited States Congress enacted the Hate Crime Statistics Act of\r\n1990. The Act requires the attorney general to establish guidelines\r\nand collect, as part of the Uniform Crime Reporting (UCR) Program,\r\ndata \"about crimes that manifest evidence of prejudice based on race,\r\nreligion, sexual orientation, or ethnicity, including where\r\nappropriate the crimes of murder and non-negligent manslaughter,\r\nforcible rape, aggravated assault, simple assault, intimidation,\r\narson, and destruction, damage or vandalism of property.\" Hate crime\r\ndata collection was required by the Act to begin in calendar year 1990\r\nand to continue for four successive years. In September 1994, the\r\nViolent Crime Control and Law Enforcement Act amended the Hate Crime\r\nStatistics Act to add disabilities, both physical and mental, as\r\nfactors that could be considered a basis for hate crimes. Although the\r\nAct originally mandated data collection for five years, the Church\r\nArson Prevention Act of 1996 amended the collection duration \"for each\r\ncalendar year,\" making hate crime statistics a permanent addition to\r\nthe UCR program. As with the other UCR data, law enforcement agencies\r\ncontribute reports either directly or through their state reporting\r\nprograms. Information contained in the data includes number of victims\r\nand offenders involved in each hate crime incident, type of victims,\r\nbias motivation, offense type, and location type.",
-            "modified": "2008-12-23T09:44:43",
-            "accessLevel": "public",
-            "identifier": "2293",
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
+            "title": "Executions in the United States, 1608-1940: The ESPY File -- Summary Data of Executions Collected by M. Watt Espy Between 1986 and 1996"
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
+            "description": "In response to a growing concern about hate crimes, the\r\nUnited States Congress enacted the Hate Crime Statistics Act of\r\n1990. The Act requires the attorney general to establish guidelines\r\nand collect, as part of the Uniform Crime Reporting (UCR) Program,\r\ndata \"about crimes that manifest evidence of prejudice based on race,\r\nreligion, sexual orientation, or ethnicity, including where\r\nappropriate the crimes of murder and non-negligent manslaughter,\r\nforcible rape, aggravated assault, simple assault, intimidation,\r\narson, and destruction, damage or vandalism of property.\" Hate crime\r\ndata collection was required by the Act to begin in calendar year 1990\r\nand to continue for four successive years. In September 1994, the\r\nViolent Crime Control and Law Enforcement Act amended the Hate Crime\r\nStatistics Act to add disabilities, both physical and mental, as\r\nfactors that could be considered a basis for hate crimes. Although the\r\nAct originally mandated data collection for five years, the Church\r\nArson Prevention Act of 1996 amended the collection duration \"for each\r\ncalendar year,\" making hate crime statistics a permanent addition to\r\nthe UCR program. As with the other UCR data, law enforcement agencies\r\ncontribute reports either directly or through their state reporting\r\nprograms. Information contained in the data includes number of victims\r\nand offenders involved in each hate crime incident, type of victims,\r\nbias motivation, offense type, and location type.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR23940.v1",
+                    "title": "Uniform Crime Reporting Program Data [United States]: Hate Crime Data, 1995 [Record-Type Files]"
+                }
+            ],
+            "identifier": "2293",
+            "isPartOf": "2167",
+            "issued": "2008-12-23T09:44:43",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -56310,54 +56304,54 @@
                 "religion",
                 "violence"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-12-23T09:44:43",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2008-12-23T09:44:43",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR23940.v1",
-                    "title": "Uniform Crime Reporting Program Data [United States]: Hate Crime Data, 1995 [Record-Type Files]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data [United States]: Hate Crime Data, 1994 [Record-Type Files]",
-            "description": "In response to a growing concern about hate crimes, the\r\nUnited States Congress enacted the Hate Crime Statistics Act of\r\n1990. The Act requires the attorney general to establish guidelines\r\nand collect, as part of the Uniform Crime Reporting (UCR) Program,\r\ndata \"about crimes that manifest evidence of prejudice based on race,\r\nreligion, sexual orientation, or ethnicity, including where\r\nappropriate the crimes of murder and non-negligent manslaughter,\r\nforcible rape, aggravated assault, simple assault, intimidation,\r\narson, and destruction, damage or vandalism of property.\" Hate crime\r\ndata collection was required by the Act to begin in calendar year 1990\r\nand to continue for four successive years. In September 1994, the\r\nViolent Crime Control and Law Enforcement Act amended the Hate Crime\r\nStatistics Act to add disabilities, both physical and mental, as\r\nfactors that could be considered a basis for hate crimes. Although the\r\nAct originally mandated data collection for five years, the Church\r\nArson Prevention Act of 1996 amended the collection duration \"for each\r\ncalendar year,\" making hate crime statistics a permanent addition to\r\nthe UCR program. As with the other UCR data, law enforcement agencies\r\ncontribute reports either directly or through their state reporting\r\nprograms. Information contained in the data includes number of victims\r\nand offenders involved in each hate crime incident, type of victims,\r\nbias motivation, offense type, and location type.",
-            "modified": "2008-12-23T09:41:57",
-            "accessLevel": "public",
-            "identifier": "2294",
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
+            "title": "Uniform Crime Reporting Program Data [United States]: Hate Crime Data, 1995 [Record-Type Files]"
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
+            "description": "In response to a growing concern about hate crimes, the\r\nUnited States Congress enacted the Hate Crime Statistics Act of\r\n1990. The Act requires the attorney general to establish guidelines\r\nand collect, as part of the Uniform Crime Reporting (UCR) Program,\r\ndata \"about crimes that manifest evidence of prejudice based on race,\r\nreligion, sexual orientation, or ethnicity, including where\r\nappropriate the crimes of murder and non-negligent manslaughter,\r\nforcible rape, aggravated assault, simple assault, intimidation,\r\narson, and destruction, damage or vandalism of property.\" Hate crime\r\ndata collection was required by the Act to begin in calendar year 1990\r\nand to continue for four successive years. In September 1994, the\r\nViolent Crime Control and Law Enforcement Act amended the Hate Crime\r\nStatistics Act to add disabilities, both physical and mental, as\r\nfactors that could be considered a basis for hate crimes. Although the\r\nAct originally mandated data collection for five years, the Church\r\nArson Prevention Act of 1996 amended the collection duration \"for each\r\ncalendar year,\" making hate crime statistics a permanent addition to\r\nthe UCR program. As with the other UCR data, law enforcement agencies\r\ncontribute reports either directly or through their state reporting\r\nprograms. Information contained in the data includes number of victims\r\nand offenders involved in each hate crime incident, type of victims,\r\nbias motivation, offense type, and location type.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR23960.v1",
+                    "title": "Uniform Crime Reporting Program Data [United States]: Hate Crime Data, 1994 [Record-Type Files]"
+                }
+            ],
+            "identifier": "2294",
+            "isPartOf": "2167",
+            "issued": "2008-12-23T09:41:57",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -56376,54 +56370,54 @@
                 "religion",
                 "violence"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2008-12-23T09:41:57",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2008-12-23T09:41:57",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR23960.v1",
-                    "title": "Uniform Crime Reporting Program Data [United States]: Hate Crime Data, 1994 [Record-Type Files]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data: Arrests by Age, Sex, and Race, United States, 2009",
-            "description": "These data provide information on the number of arrests\r\nreported to the Federal Bureau of Investigation's Uniform Crime\r\nReporting (UCR) Program each year by police agencies in the United\r\nStates. These arrest reports provide data on 43 offenses including\r\nviolent crime, drug use, gambling, and larceny. The data received by\r\nICPSR were structured as a hierarchical file containing (per reporting\r\npolice agency) an agency header record, 1 to 12 monthly header\r\nrecords, and 1 to 43 detail offense records containing the counts of\r\narrests by age, sex, and race for a particular offense. ICPSR\r\nrestructured the original data to a rectangular format.",
-            "modified": "2011-09-30T14:31:06",
-            "accessLevel": "public",
-            "identifier": "2295",
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
+            "title": "Uniform Crime Reporting Program Data [United States]: Hate Crime Data, 1994 [Record-Type Files]"
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
+            "description": "These data provide information on the number of arrests\r\nreported to the Federal Bureau of Investigation's Uniform Crime\r\nReporting (UCR) Program each year by police agencies in the United\r\nStates. These arrest reports provide data on 43 offenses including\r\nviolent crime, drug use, gambling, and larceny. The data received by\r\nICPSR were structured as a hierarchical file containing (per reporting\r\npolice agency) an agency header record, 1 to 12 monthly header\r\nrecords, and 1 to 43 detail offense records containing the counts of\r\narrests by age, sex, and race for a particular offense. ICPSR\r\nrestructured the original data to a rectangular format.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR30761.v1",
+                    "title": "Uniform Crime Reporting Program Data: Arrests by Age, Sex, and Race, United States, 2009"
+                }
+            ],
+            "identifier": "2295",
+            "isPartOf": "2167",
+            "issued": "2011-09-30T14:31:06",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -56448,54 +56442,54 @@
                 "vandalism",
                 "weapons"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-09-30T14:31:06",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2011-09-30T14:31:06",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR30761.v1",
-                    "title": "Uniform Crime Reporting Program Data: Arrests by Age, Sex, and Race, United States, 2009"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data: Arrests by Age, Sex, and Race, Summarized Yearly, United States, 2009",
-            "description": "These data provide information on the number of arrests\r\nreported to the Federal Bureau of Investigation's Uniform Crime\r\nReporting (UCR) Program each year by police agencies in the United\r\nStates. These arrest reports provide data on 43 offenses including\r\nviolent crime, drug use, gambling, and larceny. The data received by\r\nICPSR were structured as a hierarchical file containing, per reporting\r\npolice agency: an agency header record, and 1 to 43 detail offense\r\nrecords containing the counts of arrests by age, sex, and race for a\r\nparticular offense. ICPSR restructured the original data to logical\r\nrecord length format with the agency header record variables copied\r\nonto the detail records. Consequently, each record contains arrest\r\ncounts for a particular agency-offense.",
-            "modified": "2011-09-30T14:36:38",
-            "accessLevel": "public",
-            "identifier": "2296",
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
+            "title": "Uniform Crime Reporting Program Data: Arrests by Age, Sex, and Race, United States, 2009"
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
+            "description": "These data provide information on the number of arrests\r\nreported to the Federal Bureau of Investigation's Uniform Crime\r\nReporting (UCR) Program each year by police agencies in the United\r\nStates. These arrest reports provide data on 43 offenses including\r\nviolent crime, drug use, gambling, and larceny. The data received by\r\nICPSR were structured as a hierarchical file containing, per reporting\r\npolice agency: an agency header record, and 1 to 43 detail offense\r\nrecords containing the counts of arrests by age, sex, and race for a\r\nparticular offense. ICPSR restructured the original data to logical\r\nrecord length format with the agency header record variables copied\r\nonto the detail records. Consequently, each record contains arrest\r\ncounts for a particular agency-offense.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR30762.v1",
+                    "title": "Uniform Crime Reporting Program Data: Arrests by Age, Sex, and Race, Summarized Yearly, United States, 2009"
+                }
+            ],
+            "identifier": "2296",
+            "isPartOf": "2167",
+            "issued": "2011-09-30T14:36:38",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrest records",
@@ -56511,54 +56505,54 @@
                 "offenses",
                 "violent crime"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-09-30T14:36:38",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2011-09-30T14:36:38",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR30762.v1",
-                    "title": "Uniform Crime Reporting Program Data: Arrests by Age, Sex, and Race, Summarized Yearly, United States, 2009"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data: County-Level Detailed Arrest and Offense Data, United States, 2009",
-            "description": "This data collection contains county-level counts of\r\narrests and offenses for Part I offenses (murder, rape, robbery,\r\naggravated assault, burglary, larceny, auto theft, and arson) and\r\ncounts of arrests for Part II offenses (forgery, fraud, embezzlement,\r\nvandalism, weapons violations, sex offenses, drug and alcohol abuse\r\nviolations, gambling, vagrancy, curfew violations, and runaways).",
-            "modified": "2014-06-16T14:03:22",
-            "accessLevel": "public",
-            "identifier": "2297",
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
+            "title": "Uniform Crime Reporting Program Data: Arrests by Age, Sex, and Race, Summarized Yearly, United States, 2009"
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
+                    "accessURL": "https://doi.org/10.3886/ICPSR30763.v2",
+                    "title": "Uniform Crime Reporting Program Data: County-Level Detailed Arrest and Offense Data, United States, 2009"
+                }
+            ],
+            "identifier": "2297",
+            "isPartOf": "2167",
+            "issued": "2012-01-23T11:44:27",
             "keyword": [
                 "Uniform Crime Reports",
                 "aggravated assault",
@@ -56588,54 +56582,54 @@
                 "vandalism",
                 "weapons offenses"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2014-06-16T14:03:22",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2012-01-23T11:44:27",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR30763.v2",
-                    "title": "Uniform Crime Reporting Program Data: County-Level Detailed Arrest and Offense Data, United States, 2009"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data: Hate Crime Data, 2009 [Record-Type Files]",
-            "description": "In response to a growing concern about hate crimes, the\r\nUnited States Congress enacted the Hate Crime Statistics Act of\r\n1990. The Act requires the attorney general to establish guidelines\r\nand collect, as part of the Uniform Crime Reporting (UCR) Program,\r\ndata \"about crimes that manifest evidence of prejudice based on race,\r\nreligion, sexual orientation, or ethnicity, including where\r\nappropriate the crimes of murder and non-negligent manslaughter,\r\nforcible rape, aggravated assault, simple assault, intimidation,\r\narson, and destruction, damage or vandalism of property.\" Hate crime\r\ndata collection was required by the Act to begin in calendar year 1990\r\nand to continue for four successive years. In September 1994, the\r\nViolent Crime Control and Law Enforcement Act amended the Hate Crime\r\nStatistics Act to add disabilities, both physical and mental, as\r\nfactors that could be considered a basis for hate crimes. Although the\r\nAct originally mandated data collection for five years, the Church\r\nArson Prevention Act of 1996 amended the collection duration \"for each\r\ncalendar year,\" making hate crime statistics a permanent addition to\r\nthe UCR program. As with the other UCR data, law enforcement agencies\r\ncontribute reports either directly or through their state reporting\r\nprograms. Information contained in the data includes number of victims\r\nand offenders involved in each hate crime incident, type of victims,\r\nbias motivation, offense type, and location type.",
-            "modified": "2011-09-30T14:49:49",
-            "accessLevel": "public",
-            "identifier": "2298",
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
+            "title": "Uniform Crime Reporting Program Data: County-Level Detailed Arrest and Offense Data, United States, 2009"
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
+            "description": "In response to a growing concern about hate crimes, the\r\nUnited States Congress enacted the Hate Crime Statistics Act of\r\n1990. The Act requires the attorney general to establish guidelines\r\nand collect, as part of the Uniform Crime Reporting (UCR) Program,\r\ndata \"about crimes that manifest evidence of prejudice based on race,\r\nreligion, sexual orientation, or ethnicity, including where\r\nappropriate the crimes of murder and non-negligent manslaughter,\r\nforcible rape, aggravated assault, simple assault, intimidation,\r\narson, and destruction, damage or vandalism of property.\" Hate crime\r\ndata collection was required by the Act to begin in calendar year 1990\r\nand to continue for four successive years. In September 1994, the\r\nViolent Crime Control and Law Enforcement Act amended the Hate Crime\r\nStatistics Act to add disabilities, both physical and mental, as\r\nfactors that could be considered a basis for hate crimes. Although the\r\nAct originally mandated data collection for five years, the Church\r\nArson Prevention Act of 1996 amended the collection duration \"for each\r\ncalendar year,\" making hate crime statistics a permanent addition to\r\nthe UCR program. As with the other UCR data, law enforcement agencies\r\ncontribute reports either directly or through their state reporting\r\nprograms. Information contained in the data includes number of victims\r\nand offenders involved in each hate crime incident, type of victims,\r\nbias motivation, offense type, and location type.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR30764.v1",
+                    "title": "Uniform Crime Reporting Program Data: Hate Crime Data, 2009 [Record-Type Files]"
+                }
+            ],
+            "identifier": "2298",
+            "isPartOf": "2167",
+            "issued": "2011-09-30T14:49:49",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -56654,54 +56648,54 @@
                 "religion",
                 "violence"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-09-30T14:49:49",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2011-09-30T14:49:49",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR30764.v1",
-                    "title": "Uniform Crime Reporting Program Data: Hate Crime Data, 2009 [Record-Type Files]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data [United States]: Police Employee (LEOKA) Data, 2009",
-            "description": "Since 1930, the Federal Bureau of Investigation has compiled the Uniform Crime Reports (UCR) to serve as a periodic nationwide assessment of reported crimes not available elsewhere in the criminal justice system. Each year, this information is reported in four types of files: (1) Offenses Known and Clearances by Arrest, (2) Property Stolen and Recovered, (3) Supplementary Homicide Reports (SHR), and (4) Police Employee (LEOKA) Data. The Police Employee (LEOKA) Data provide information about law enforcement officers killed or assaulted (hence the acronym, LEOKA) in the line of duty. The variables created from the LEOKA forms provide in-depth information on the circumstances surrounding killings or assaults, including type of call answered, type of weapon used, and type of patrol the officers were on.",
-            "modified": "2011-07-27T14:07:33",
-            "accessLevel": "public",
-            "identifier": "2299",
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
+            "title": "Uniform Crime Reporting Program Data: Hate Crime Data, 2009 [Record-Type Files]"
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
+            "description": "Since 1930, the Federal Bureau of Investigation has compiled the Uniform Crime Reports (UCR) to serve as a periodic nationwide assessment of reported crimes not available elsewhere in the criminal justice system. Each year, this information is reported in four types of files: (1) Offenses Known and Clearances by Arrest, (2) Property Stolen and Recovered, (3) Supplementary Homicide Reports (SHR), and (4) Police Employee (LEOKA) Data. The Police Employee (LEOKA) Data provide information about law enforcement officers killed or assaulted (hence the acronym, LEOKA) in the line of duty. The variables created from the LEOKA forms provide in-depth information on the circumstances surrounding killings or assaults, including type of call answered, type of weapon used, and type of patrol the officers were on.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR30765.v1",
+                    "title": "Uniform Crime Reporting Program Data [United States]: Police Employee (LEOKA) Data, 2009"
+                }
+            ],
+            "identifier": "2299",
+            "isPartOf": "2167",
+            "issued": "2011-07-27T14:07:33",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -56714,54 +56708,54 @@
                 "police deaths",
                 "police officers"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-07-27T14:07:33",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2011-07-27T14:07:33",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR30765.v1",
-                    "title": "Uniform Crime Reporting Program Data [United States]: Police Employee (LEOKA) Data, 2009"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data: Offenses Known and Clearances by Arrest, 2009",
-            "description": "Since 1930, the Federal Bureau of Investigation has\r\ncompiled the Uniform Crime Reports (UCR) to serve as periodic\r\nnationwide assessments of reported crimes not available elsewhere in\r\nthe criminal justice system. Law enforcement agencies contribute\r\nreports either directly or through their state reporting programs.\r\nEach year, summary data are reported in four types of files: (1)\r\nOffenses Known and Clearances by Arrest, (2) Property Stolen and\r\nRecovered, (3) Supplementary Homicide Reports (SHR), and (4) Police\r\nEmployee (LEOKA) Data. The Offenses Known and Clearances by Arrest\r\ndata files include monthly data on the number of Crime Index offenses\r\nreported and the number of offenses cleared by arrest or other means.\r\nThe counts include all reports of Index crimes (excluding arson)\r\nreceived from victims, officers who discovered infractions, or other\r\nsources.",
-            "modified": "2011-09-30T14:54:34",
-            "accessLevel": "public",
-            "identifier": "2300",
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
+            "title": "Uniform Crime Reporting Program Data [United States]: Police Employee (LEOKA) Data, 2009"
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
+            "description": "Since 1930, the Federal Bureau of Investigation has\r\ncompiled the Uniform Crime Reports (UCR) to serve as periodic\r\nnationwide assessments of reported crimes not available elsewhere in\r\nthe criminal justice system. Law enforcement agencies contribute\r\nreports either directly or through their state reporting programs.\r\nEach year, summary data are reported in four types of files: (1)\r\nOffenses Known and Clearances by Arrest, (2) Property Stolen and\r\nRecovered, (3) Supplementary Homicide Reports (SHR), and (4) Police\r\nEmployee (LEOKA) Data. The Offenses Known and Clearances by Arrest\r\ndata files include monthly data on the number of Crime Index offenses\r\nreported and the number of offenses cleared by arrest or other means.\r\nThe counts include all reports of Index crimes (excluding arson)\r\nreceived from victims, officers who discovered infractions, or other\r\nsources.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR30766.v1",
+                    "title": "Uniform Crime Reporting Program Data: Offenses Known and Clearances by Arrest, 2009"
+                }
+            ],
+            "identifier": "2300",
+            "isPartOf": "2167",
+            "issued": "2011-09-30T14:54:34",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -56771,54 +56765,54 @@
                 "law enforcement",
                 "offenses"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-09-30T14:54:34",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2011-09-30T14:54:34",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR30766.v1",
-                    "title": "Uniform Crime Reporting Program Data: Offenses Known and Clearances by Arrest, 2009"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data: Supplementary Homicide Reports, 2009",
-            "description": "Since 1930, the Federal Bureau of Investigation has compiled the Uniform Crime Reports (UCR) to serve as a periodic nationwide assessment of reported crimes not available elsewhere in the criminal justice system. Each year, this information is reported in four types of files: (1) Offenses Known and Clearances by Arrest, (2) Property Stolen and Recovered, (3) Supplementary Homicide Reports (SHR), and (4) Police Employee (LEOKA) Data. The Supplementary Homicide Reports provide incident-based information on criminal homicides reported to the police. These homicides consist of murders, non-negligent manslaughter, and justifiable homicides. The data, provided monthly by UCR agencies, contain information describing the victim of the homicide, the offender, and the relationship between victim and offender.",
-            "modified": "2011-08-04T09:14:17",
-            "accessLevel": "public",
-            "identifier": "2301",
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
+            "title": "Uniform Crime Reporting Program Data: Offenses Known and Clearances by Arrest, 2009"
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
+            "description": "Since 1930, the Federal Bureau of Investigation has compiled the Uniform Crime Reports (UCR) to serve as a periodic nationwide assessment of reported crimes not available elsewhere in the criminal justice system. Each year, this information is reported in four types of files: (1) Offenses Known and Clearances by Arrest, (2) Property Stolen and Recovered, (3) Supplementary Homicide Reports (SHR), and (4) Police Employee (LEOKA) Data. The Supplementary Homicide Reports provide incident-based information on criminal homicides reported to the police. These homicides consist of murders, non-negligent manslaughter, and justifiable homicides. The data, provided monthly by UCR agencies, contain information describing the victim of the homicide, the offender, and the relationship between victim and offender.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR30767.v1",
+                    "title": "Uniform Crime Reporting Program Data: Supplementary Homicide Reports, 2009"
+                }
+            ],
+            "identifier": "2301",
+            "isPartOf": "2167",
+            "issued": "2011-08-04T09:14:17",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -56832,54 +56826,54 @@
                 "offenses",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-08-04T09:14:17",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2011-08-04T09:14:17",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR30767.v1",
-                    "title": "Uniform Crime Reporting Program Data: Supplementary Homicide Reports, 2009"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data: Arson, United States, 2009",
-            "description": "Since 1930, the Federal Bureau of Investigation has\r\ncompiled the Uniform Crime Reports (UCR) to serve as periodic\r\nnationwide assessments of reported crimes not available elsewhere in\r\nthe criminal justice system. Seven main classifications of crime were\r\nchosen to gauge fluctuations in the overall volume and rate of\r\ncrime. These seven classifications that eventually became known as the\r\nCrime Index included the violent crimes of murder and non-negligent\r\nmanslaughter, forcible rape, robbery, and aggravated assault, and the\r\nproperty crimes of burglary, larceny-theft, and motor vehicle theft.\r\nBy congressional mandate, arson was added as the eighth Index offense\r\nin 1979. Arson is defined as any willful or malicious burning or\r\nattempt to burn, with or without intent to defraud, a dwelling house,\r\npublic building, motor vehicle or aircraft, personal property of\r\nanother, etc. The arson data files include monthly data on the number\r\nof arson offenses reported and the number of offenses cleared by\r\narrest or other means. The counts include all reports of arson\r\nreceived from victims, officers who discovered infractions, or other\r\nsources.",
-            "modified": "2014-02-06T11:38:58",
-            "accessLevel": "public",
-            "identifier": "2302",
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
+            "title": "Uniform Crime Reporting Program Data: Supplementary Homicide Reports, 2009"
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
+            "description": "Since 1930, the Federal Bureau of Investigation has\r\ncompiled the Uniform Crime Reports (UCR) to serve as periodic\r\nnationwide assessments of reported crimes not available elsewhere in\r\nthe criminal justice system. Seven main classifications of crime were\r\nchosen to gauge fluctuations in the overall volume and rate of\r\ncrime. These seven classifications that eventually became known as the\r\nCrime Index included the violent crimes of murder and non-negligent\r\nmanslaughter, forcible rape, robbery, and aggravated assault, and the\r\nproperty crimes of burglary, larceny-theft, and motor vehicle theft.\r\nBy congressional mandate, arson was added as the eighth Index offense\r\nin 1979. Arson is defined as any willful or malicious burning or\r\nattempt to burn, with or without intent to defraud, a dwelling house,\r\npublic building, motor vehicle or aircraft, personal property of\r\nanother, etc. The arson data files include monthly data on the number\r\nof arson offenses reported and the number of offenses cleared by\r\narrest or other means. The counts include all reports of arson\r\nreceived from victims, officers who discovered infractions, or other\r\nsources.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR30768.v1",
+                    "title": "Uniform Crime Reporting Program Data: Arson, United States, 2009"
+                }
+            ],
+            "identifier": "2302",
+            "isPartOf": "2167",
+            "issued": "2014-02-06T11:38:58",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -56890,54 +56884,54 @@
                 "law enforcement",
                 "offenses"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2014-02-06T11:38:58",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2014-02-06T11:38:58",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR30768.v1",
-                    "title": "Uniform Crime Reporting Program Data: Arson, United States, 2009"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data: Property Stolen and Recovered, 2009",
-            "description": "The UNIFORM CRIME REPORTING PROGRAM DATA: PROPERTY STOLEN AND RECOVERED,\r\n2009 file (also known as the Supplement to Return A) is collected at the agency level and includes detailed monthly data on the nature of crime and the value and type of property stolen and recovered incident to each crime. The Return A Supplement requires that a value be established for property stolen and recovered in each Crime Index category except aggravated assault. It is designed to record the value of property stolen and recovered in the following eleven classifications: Currency/notes, Jewelry and Precious Metals, Clothing and Furs, Locally Stolen Motor Vehicles, Office Equipment, Televisions/Radios, Firearms, Household Goods, Consumable Goods, Livestock, and Miscellaneous. The determination of the value of property stolen is an obligation of the investigating officer, and such information is essential to assure the completeness of a law enforcement investigative report on stolen property. The data were originally assembled by the Federal Bureau of Investigation (FBI) from reports submitted by agencies participating in the UCR. The ICPSR file was processed from Return A Supplement files provided by the FBI.",
-            "modified": "2014-02-28T11:01:36",
-            "accessLevel": "public",
-            "identifier": "2303",
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
+            "title": "Uniform Crime Reporting Program Data: Arson, United States, 2009"
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
+            "description": "The UNIFORM CRIME REPORTING PROGRAM DATA: PROPERTY STOLEN AND RECOVERED,\r\n2009 file (also known as the Supplement to Return A) is collected at the agency level and includes detailed monthly data on the nature of crime and the value and type of property stolen and recovered incident to each crime. The Return A Supplement requires that a value be established for property stolen and recovered in each Crime Index category except aggravated assault. It is designed to record the value of property stolen and recovered in the following eleven classifications: Currency/notes, Jewelry and Precious Metals, Clothing and Furs, Locally Stolen Motor Vehicles, Office Equipment, Televisions/Radios, Firearms, Household Goods, Consumable Goods, Livestock, and Miscellaneous. The determination of the value of property stolen is an obligation of the investigating officer, and such information is essential to assure the completeness of a law enforcement investigative report on stolen property. The data were originally assembled by the Federal Bureau of Investigation (FBI) from reports submitted by agencies participating in the UCR. The ICPSR file was processed from Return A Supplement files provided by the FBI.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR30769.v1",
+                    "title": "Uniform Crime Reporting Program Data: Property Stolen and Recovered, 2009"
+                }
+            ],
+            "identifier": "2303",
+            "isPartOf": "2167",
+            "issued": "2014-02-28T11:01:36",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -56952,54 +56946,54 @@
                 "stolen property",
                 "stolen property recovery"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2014-02-28T11:01:36",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2014-02-28T11:01:36",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR30769.v1",
-                    "title": "Uniform Crime Reporting Program Data: Property Stolen and Recovered, 2009"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Monitoring of Federal Criminal Sentences, [United States], 2011-2012",
-            "description": "This collection contains information on federal criminal cases sentenced under the Sentencing Guidelines and Policy Statements of the Sentencing Reform Act of 1984. The data files include all cases received by the United States Sentencing Commission that had sentencing dates between October 1, 2011, and September 30, 2012, and were assessed as constitutional. Constitutionality compares each case's sentencing date, circuit, district, and judge to provide uniformity in reporting the cases. In 1999, the United States Sentencing Commission added more variables from its databases to this collection, so the data are now provided in two files. Several variables iterate to include multiple occurrences of the same event. Part 1, Main Data, includes all noniterating variables plus the highest occurrences of each iterating variable. Part 2, Supplementary Data, includes the remaining iterations.",
-            "modified": "2014-11-25T11:42:37",
-            "accessLevel": "public",
-            "identifier": "2304",
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
+            "title": "Uniform Crime Reporting Program Data: Property Stolen and Recovered, 2009"
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
+            "description": "This collection contains information on federal criminal cases sentenced under the Sentencing Guidelines and Policy Statements of the Sentencing Reform Act of 1984. The data files include all cases received by the United States Sentencing Commission that had sentencing dates between October 1, 2011, and September 30, 2012, and were assessed as constitutional. Constitutionality compares each case's sentencing date, circuit, district, and judge to provide uniformity in reporting the cases. In 1999, the United States Sentencing Commission added more variables from its databases to this collection, so the data are now provided in two files. Several variables iterate to include multiple occurrences of the same event. Part 1, Main Data, includes all noniterating variables plus the highest occurrences of each iterating variable. Part 2, Supplementary Data, includes the remaining iterations.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR35342.v1",
+                    "title": "Monitoring of Federal Criminal Sentences, [United States], 2011-2012"
+                }
+            ],
+            "identifier": "2304",
+            "isPartOf": "2180",
+            "issued": "2014-11-25T11:42:37",
             "keyword": [
                 "convictions (law)",
                 "criminal histories",
@@ -57010,54 +57004,54 @@
                 "sentencing",
                 "sentencing guidelines"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2014-11-25T11:42:37",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2180",
-            "dataQuality": false,
-            "issued": "2014-11-25T11:42:37",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR35342.v1",
-                    "title": "Monitoring of Federal Criminal Sentences, [United States], 2011-2012"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Monitoring of Federal Criminal Convictions and Sentences: Appeals Data, 2012",
-            "description": "This collection contains appellate information from the 12\r\ncircuit courts of appeals of the United States. From the Clerk of the\r\nCourt of each court of appeals, the United States Sentencing\r\nCommission compiled the final opinions and orders, both published and\r\nunpublished, in all criminal appeals for the time period surveyed. The\r\nCommission also collected habeas corpus decisions even though they are\r\ntechnically civil matters, because such cases often involve sentencing\r\nissues. Both the \"case\" and the \"defendant\" are used in this\r\ncollection as units of analysis. Each case comprises individual\r\nrecords representing all codefendants participating in a consolidated\r\nappeal. Each defendant's record comprises the sentencing-related\r\nissues corresponding to that particular defendant.",
-            "modified": "2014-12-03T10:28:36",
-            "accessLevel": "public",
-            "identifier": "2305",
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
+            "title": "Monitoring of Federal Criminal Sentences, [United States], 2011-2012"
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
+            "description": "This collection contains appellate information from the 12\r\ncircuit courts of appeals of the United States. From the Clerk of the\r\nCourt of each court of appeals, the United States Sentencing\r\nCommission compiled the final opinions and orders, both published and\r\nunpublished, in all criminal appeals for the time period surveyed. The\r\nCommission also collected habeas corpus decisions even though they are\r\ntechnically civil matters, because such cases often involve sentencing\r\nissues. Both the \"case\" and the \"defendant\" are used in this\r\ncollection as units of analysis. Each case comprises individual\r\nrecords representing all codefendants participating in a consolidated\r\nappeal. Each defendant's record comprises the sentencing-related\r\nissues corresponding to that particular defendant.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR35343.v1",
+                    "title": "Monitoring of Federal Criminal Convictions and Sentences: Appeals Data, 2012"
+                }
+            ],
+            "identifier": "2305",
+            "isPartOf": "2175",
+            "issued": "2014-12-03T10:28:36",
             "keyword": [
                 "appeal procedures",
                 "appellate courts",
@@ -57073,54 +57067,54 @@
                 "sentence review",
                 "sentencing"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2014-12-03T10:28:36",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2175",
-            "dataQuality": false,
-            "issued": "2014-12-03T10:28:36",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR35343.v1",
-                    "title": "Monitoring of Federal Criminal Convictions and Sentences: Appeals Data, 2012"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Organizations Convicted in Federal Criminal Courts, 2012",
-            "description": "These data, collected to assist in the development of\r\nsentencing guidelines, describe offense and sentencing characteristics\r\nfor organizations sentenced in federal district courts in 2012. The\r\nUnited States Sentencing Commission's primary function is to inform\r\nfederal courts of sentencing policies and practices that include\r\nguidelines prescribing the appropriate form and severity of punishment\r\nfor offenders convicted of federal crimes. Court-related variables\r\ninclude primary offense type, pecuniary offense loss and gain, dates\r\nof disposition and sentencing, method of determination of guilt,\r\nnumber of counts pled and charged, and dates and types of sentencing\r\nand restitution. Defendant organization variables include ownership\r\nstructure, number of owners and employees, highest level of corporate\r\nknowledge of the criminal offense, highest level of corporate\r\nindictment and conviction for participation in the criminal offense,\r\nannual revenue, equity and financial status, whether it was a criminal\r\norganization, duration of criminal activity, and risk to national\r\nsecurity. Organizational defendants data, 2012, covers fiscal year\r\nOctober 1, 2011, through September 30, 2012.",
-            "modified": "2014-11-25T12:04:49",
-            "accessLevel": "public",
-            "identifier": "2306",
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
+            "title": "Monitoring of Federal Criminal Convictions and Sentences: Appeals Data, 2012"
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
+            "description": "These data, collected to assist in the development of\r\nsentencing guidelines, describe offense and sentencing characteristics\r\nfor organizations sentenced in federal district courts in 2012. The\r\nUnited States Sentencing Commission's primary function is to inform\r\nfederal courts of sentencing policies and practices that include\r\nguidelines prescribing the appropriate form and severity of punishment\r\nfor offenders convicted of federal crimes. Court-related variables\r\ninclude primary offense type, pecuniary offense loss and gain, dates\r\nof disposition and sentencing, method of determination of guilt,\r\nnumber of counts pled and charged, and dates and types of sentencing\r\nand restitution. Defendant organization variables include ownership\r\nstructure, number of owners and employees, highest level of corporate\r\nknowledge of the criminal offense, highest level of corporate\r\nindictment and conviction for participation in the criminal offense,\r\nannual revenue, equity and financial status, whether it was a criminal\r\norganization, duration of criminal activity, and risk to national\r\nsecurity. Organizational defendants data, 2012, covers fiscal year\r\nOctober 1, 2011, through September 30, 2012.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR35344.v1",
+                    "title": "Organizations Convicted in Federal Criminal Courts, 2012"
+                }
+            ],
+            "identifier": "2306",
+            "isPartOf": "2427",
+            "issued": "2014-11-25T12:04:49",
             "keyword": [
                 "convictions (law)",
                 "corporate crime",
@@ -57136,54 +57130,54 @@
                 "sentencing",
                 "sentencing guidelines"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2014-11-25T12:04:49",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2427",
-            "dataQuality": false,
-            "issued": "2014-11-25T12:04:49",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR35344.v1",
-                    "title": "Organizations Convicted in Federal Criminal Courts, 2012"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Monitoring of Federal Criminal Sentences, [United States], 2012-2013",
-            "description": "This collection contains information on federal criminal cases sentenced under the Sentencing Guidelines and Policy Statements of the Sentencing Reform Act of 1984. The data files include all cases received by the United States Sentencing Commission that had sentencing dates between October 1, 2012, and September 30, 2013, and were assessed as constitutional. Constitutionality compares each case's sentencing date, circuit, district, and judge to provide uniformity in reporting the cases. In 1999, the United States Sentencing Commission added more variables from its databases to this collection, so the data are now provided in two files. Several variables iterate to include multiple occurrences of the same event. Part 1, Main Data, includes all noniterating variables plus the highest occurrences of each iterating variable. Part 2, Supplementary Data, includes the remaining iterations.",
-            "modified": "2014-11-25T11:55:56",
-            "accessLevel": "public",
-            "identifier": "2307",
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
+            "title": "Organizations Convicted in Federal Criminal Courts, 2012"
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
+            "description": "This collection contains information on federal criminal cases sentenced under the Sentencing Guidelines and Policy Statements of the Sentencing Reform Act of 1984. The data files include all cases received by the United States Sentencing Commission that had sentencing dates between October 1, 2012, and September 30, 2013, and were assessed as constitutional. Constitutionality compares each case's sentencing date, circuit, district, and judge to provide uniformity in reporting the cases. In 1999, the United States Sentencing Commission added more variables from its databases to this collection, so the data are now provided in two files. Several variables iterate to include multiple occurrences of the same event. Part 1, Main Data, includes all noniterating variables plus the highest occurrences of each iterating variable. Part 2, Supplementary Data, includes the remaining iterations.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR35345.v1",
+                    "title": "Monitoring of Federal Criminal Sentences, [United States], 2012-2013"
+                }
+            ],
+            "identifier": "2307",
+            "isPartOf": "2180",
+            "issued": "2014-11-25T11:55:56",
             "keyword": [
                 "convictions (law)",
                 "criminal histories",
@@ -57194,54 +57188,54 @@
                 "sentencing",
                 "sentencing guidelines"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2014-11-25T11:55:56",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2180",
-            "dataQuality": false,
-            "issued": "2014-11-25T11:55:56",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR35345.v1",
-                    "title": "Monitoring of Federal Criminal Sentences, [United States], 2012-2013"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Monitoring of Federal Criminal Convictions and Sentences: Appeals Data, 2013",
-            "description": "This collection contains appellate information from the 12\r\ncircuit courts of appeals of the United States. From the Clerk of the\r\nCourt of each court of appeals, the United States Sentencing\r\nCommission compiled the final opinions and orders, both published and\r\nunpublished, in all criminal appeals for the time period surveyed. The\r\nCommission also collected habeas corpus decisions even though they are\r\ntechnically civil matters, because such cases often involve sentencing\r\nissues. Both the \"case\" and the \"defendant\" are used in this\r\ncollection as units of analysis. Each case comprises individual\r\nrecords representing all codefendants participating in a consolidated\r\nappeal. Each defendant's record comprises the sentencing-related\r\nissues corresponding to that particular defendant.",
-            "modified": "2014-12-03T10:31:44",
-            "accessLevel": "public",
-            "identifier": "2308",
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
+            "title": "Monitoring of Federal Criminal Sentences, [United States], 2012-2013"
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
+            "description": "This collection contains appellate information from the 12\r\ncircuit courts of appeals of the United States. From the Clerk of the\r\nCourt of each court of appeals, the United States Sentencing\r\nCommission compiled the final opinions and orders, both published and\r\nunpublished, in all criminal appeals for the time period surveyed. The\r\nCommission also collected habeas corpus decisions even though they are\r\ntechnically civil matters, because such cases often involve sentencing\r\nissues. Both the \"case\" and the \"defendant\" are used in this\r\ncollection as units of analysis. Each case comprises individual\r\nrecords representing all codefendants participating in a consolidated\r\nappeal. Each defendant's record comprises the sentencing-related\r\nissues corresponding to that particular defendant.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR35346.v1",
+                    "title": "Monitoring of Federal Criminal Convictions and Sentences: Appeals Data, 2013"
+                }
+            ],
+            "identifier": "2308",
+            "isPartOf": "2175",
+            "issued": "2014-12-03T10:31:44",
             "keyword": [
                 "appeal procedures",
                 "appellate courts",
@@ -57257,54 +57251,54 @@
                 "sentence review",
                 "sentencing"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2014-12-03T10:31:44",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2175",
-            "dataQuality": false,
-            "issued": "2014-12-03T10:31:44",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR35346.v1",
-                    "title": "Monitoring of Federal Criminal Convictions and Sentences: Appeals Data, 2013"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Organizations Convicted in Federal Criminal Courts, 2013",
-            "description": "These data, collected to assist in the development of\r\nsentencing guidelines, describe offense and sentencing characteristics\r\nfor organizations sentenced in federal district courts in 2013. The\r\nUnited States Sentencing Commission's primary function is to inform\r\nfederal courts of sentencing policies and practices that include\r\nguidelines prescribing the appropriate form and severity of punishment\r\nfor offenders convicted of federal crimes. Court-related variables\r\ninclude primary offense type, pecuniary offense loss and gain, dates\r\nof disposition and sentencing, method of determination of guilt,\r\nnumber of counts pled and charged, and dates and types of sentencing\r\nand restitution. Defendant organization variables include ownership\r\nstructure, number of owners and employees, highest level of corporate\r\nknowledge of the criminal offense, highest level of corporate\r\nindictment and conviction for participation in the criminal offense,\r\nannual revenue, equity and financial status, whether it was a criminal\r\norganization, duration of criminal activity, and risk to national\r\nsecurity. Organizational defendants data, 2013, covers fiscal year\r\nOctober 1, 2012, through September 30, 2013.",
-            "modified": "2014-12-03T10:34:23",
-            "accessLevel": "public",
-            "identifier": "2309",
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
+            "title": "Monitoring of Federal Criminal Convictions and Sentences: Appeals Data, 2013"
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
+            "description": "These data, collected to assist in the development of\r\nsentencing guidelines, describe offense and sentencing characteristics\r\nfor organizations sentenced in federal district courts in 2013. The\r\nUnited States Sentencing Commission's primary function is to inform\r\nfederal courts of sentencing policies and practices that include\r\nguidelines prescribing the appropriate form and severity of punishment\r\nfor offenders convicted of federal crimes. Court-related variables\r\ninclude primary offense type, pecuniary offense loss and gain, dates\r\nof disposition and sentencing, method of determination of guilt,\r\nnumber of counts pled and charged, and dates and types of sentencing\r\nand restitution. Defendant organization variables include ownership\r\nstructure, number of owners and employees, highest level of corporate\r\nknowledge of the criminal offense, highest level of corporate\r\nindictment and conviction for participation in the criminal offense,\r\nannual revenue, equity and financial status, whether it was a criminal\r\norganization, duration of criminal activity, and risk to national\r\nsecurity. Organizational defendants data, 2013, covers fiscal year\r\nOctober 1, 2012, through September 30, 2013.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR35347.v1",
+                    "title": "Organizations Convicted in Federal Criminal Courts, 2013"
+                }
+            ],
+            "identifier": "2309",
+            "isPartOf": "2427",
+            "issued": "2014-12-03T10:34:23",
             "keyword": [
                 "convictions (law)",
                 "corporate crime",
@@ -57320,54 +57314,54 @@
                 "sentencing",
                 "sentencing guidelines"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2014-12-03T10:34:23",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2427",
-            "dataQuality": false,
-            "issued": "2014-12-03T10:34:23",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR35347.v1",
-                    "title": "Organizations Convicted in Federal Criminal Courts, 2013"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data: Arson, United States, 1983",
-            "description": "Since 1930, the Federal Bureau of Investigation has\r\ncompiled the Uniform Crime Reports (UCR) to serve as periodic\r\nnationwide assessments of reported crimes not available elsewhere in\r\nthe criminal justice system. Seven main classifications of crime were\r\nchosen to gauge fluctuations in the overall volume and rate of\r\ncrime. These seven classifications that eventually became known as the\r\nCrime Index included the violent crimes of murder and non-negligent\r\nmanslaughter, forcible rape, robbery, and aggravated assault, and the\r\nproperty crimes of burglary, larceny-theft, and motor vehicle theft.\r\nBy congressional mandate, arson was added as the eighth Index offense\r\nin 1979. Arson is defined as any willful or malicious burning or\r\nattempt to burn, with or without intent to defraud, a dwelling house,\r\npublic building, motor vehicle or aircraft, personal property of\r\nanother, etc. The arson data files include monthly data on the number\r\nof arson offenses reported and the number of offenses cleared by\r\narrest or other means. The counts include all reports of arson\r\nreceived from victims, officers who discovered infractions, or other\r\nsources.",
-            "modified": "2014-11-11T12:34:51",
-            "accessLevel": "public",
-            "identifier": "2310",
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
+            "title": "Organizations Convicted in Federal Criminal Courts, 2013"
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
+            "description": "Since 1930, the Federal Bureau of Investigation has\r\ncompiled the Uniform Crime Reports (UCR) to serve as periodic\r\nnationwide assessments of reported crimes not available elsewhere in\r\nthe criminal justice system. Seven main classifications of crime were\r\nchosen to gauge fluctuations in the overall volume and rate of\r\ncrime. These seven classifications that eventually became known as the\r\nCrime Index included the violent crimes of murder and non-negligent\r\nmanslaughter, forcible rape, robbery, and aggravated assault, and the\r\nproperty crimes of burglary, larceny-theft, and motor vehicle theft.\r\nBy congressional mandate, arson was added as the eighth Index offense\r\nin 1979. Arson is defined as any willful or malicious burning or\r\nattempt to burn, with or without intent to defraud, a dwelling house,\r\npublic building, motor vehicle or aircraft, personal property of\r\nanother, etc. The arson data files include monthly data on the number\r\nof arson offenses reported and the number of offenses cleared by\r\narrest or other means. The counts include all reports of arson\r\nreceived from victims, officers who discovered infractions, or other\r\nsources.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR35483.v1",
+                    "title": "Uniform Crime Reporting Program Data: Arson, United States, 1983"
+                }
+            ],
+            "identifier": "2310",
+            "isPartOf": "2167",
+            "issued": "2014-11-11T12:34:51",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -57378,109 +57372,109 @@
                 "law enforcement",
                 "offenses"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2014-11-11T12:34:51",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2014-11-11T12:34:51",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR35483.v1",
-                    "title": "Uniform Crime Reporting Program Data: Arson, United States, 1983"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 2012",
-            "description": "The data contain records of defendants in federal criminal cases filed in United States District Court during fiscal year 2012. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2015-02-04T16:34:52",
-            "accessLevel": "restricted public",
-            "identifier": "2311",
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
+            "title": "Uniform Crime Reporting Program Data: Arson, United States, 1983"
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
+            "description": "The data contain records of defendants in federal criminal cases filed in United States District Court during fiscal year 2012. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR35489.v1",
+                    "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 2012"
+                }
+            ],
+            "identifier": "2311",
+            "isPartOf": "2174",
+            "issued": "2015-02-04T16:33:27",
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
+            "modified": "2015-02-04T16:34:52",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2015-02-04T16:33:27",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR35489.v1",
-                    "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 2012"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2012",
-            "description": "The data contain records of defendants in criminal cases filed in United States District Court during fiscal year 2012. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2015-02-04T15:32:36",
-            "accessLevel": "restricted public",
-            "identifier": "2312",
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
+            "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 2012"
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
+            "description": "The data contain records of defendants in criminal cases filed in United States District Court during fiscal year 2012. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR35490.v1",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2012"
+                }
+            ],
+            "identifier": "2312",
+            "isPartOf": "2174",
+            "issued": "2015-02-04T15:30:35",
             "keyword": [
                 "administration",
                 "court cases",
@@ -57492,55 +57486,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2015-02-04T15:32:36",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2015-02-04T15:30:35",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR35490.v1",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2012"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 2012",
-            "description": "The data contain records of defendants in criminal cases filed in United States District Court before or during fiscal year 2012 and still pending as of year-end. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2015-02-04T15:40:36",
-            "accessLevel": "restricted public",
-            "identifier": "2313",
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2012"
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
+            "description": "The data contain records of defendants in criminal cases filed in United States District Court before or during fiscal year 2012 and still pending as of year-end. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR35491.v1",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 2012"
+                }
+            ],
+            "identifier": "2313",
+            "isPartOf": "2174",
+            "issued": "2015-02-04T15:38:48",
             "keyword": [
                 "administration",
                 "court cases",
@@ -57552,55 +57546,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2015-02-04T15:40:36",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2015-02-04T15:38:48",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR35491.v1",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 2012"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 2012",
-            "description": "The data contain records of defendants in criminal cases terminated in United States District Court during fiscal year 2012. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2015-02-04T15:50:58",
-            "accessLevel": "restricted public",
-            "identifier": "2314",
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 2012"
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
+            "description": "The data contain records of defendants in criminal cases terminated in United States District Court during fiscal year 2012. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR35492.v1",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 2012"
+                }
+            ],
+            "identifier": "2314",
+            "isPartOf": "2174",
+            "issued": "2015-02-04T15:43:48",
             "keyword": [
                 "administration",
                 "court cases",
@@ -57612,330 +57606,330 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2015-02-04T15:50:58",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2015-02-04T15:43:48",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR35492.v1",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 2012"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2012",
-            "description": "The data contain records of sentenced offenders committed to the custody of the Bureau of Prisons (BOP) during fiscal year 2012. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2015-02-04T15:57:15",
-            "accessLevel": "restricted public",
-            "identifier": "2315",
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 2012"
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
+            "description": "The data contain records of sentenced offenders committed to the custody of the Bureau of Prisons (BOP) during fiscal year 2012. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR35493.v1",
+                    "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2012"
+                }
+            ],
+            "identifier": "2315",
+            "isPartOf": "2174",
+            "issued": "2015-02-04T15:54:50",
             "keyword": [
                 "correctional facilities",
                 "correctional system",
                 "imprisonment",
                 "offenders"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2015-02-04T15:57:15",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2015-02-04T15:54:50",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR35493.v1",
-                    "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2012"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Offenders Released From Prison, 2012",
-            "description": "The data contain records of sentenced offenders released from the custody of the Bureau of Prisons (BOP) during fiscal year 2012. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. Records of offenders who exit federal prison temporarily, such as for transit to another location, to serve a weekend sentence, or for health care, are not included in the exiting cohort. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2015-02-04T16:02:41",
-            "accessLevel": "restricted public",
-            "identifier": "2316",
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
+            "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2012"
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
+            "description": "The data contain records of sentenced offenders released from the custody of the Bureau of Prisons (BOP) during fiscal year 2012. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. Records of offenders who exit federal prison temporarily, such as for transit to another location, to serve a weekend sentence, or for health care, are not included in the exiting cohort. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR35494.v1",
+                    "title": "Federal Justice Statistics Program: Offenders Released From Prison, 2012"
+                }
+            ],
+            "identifier": "2316",
+            "isPartOf": "2174",
+            "issued": "2015-02-04T16:00:27",
             "keyword": [
                 "correctional facilities",
                 "correctional system",
                 "inmate release plans",
                 "offenders"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2015-02-04T16:02:41",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2015-02-04T16:00:27",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR35494.v1",
-                    "title": "Federal Justice Statistics Program: Offenders Released From Prison, 2012"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 2012",
-            "description": "The data contain records of sentenced offenders in the custody of the Bureau of Prisons (BOP) at year-end of fiscal year 2012. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2015-02-04T16:10:54",
-            "accessLevel": "restricted public",
-            "identifier": "2317",
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
+            "title": "Federal Justice Statistics Program: Offenders Released From Prison, 2012"
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
+            "description": "The data contain records of sentenced offenders in the custody of the Bureau of Prisons (BOP) at year-end of fiscal year 2012. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR35495.v1",
+                    "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 2012"
+                }
+            ],
+            "identifier": "2317",
+            "isPartOf": "2174",
+            "issued": "2015-02-04T16:08:27",
             "keyword": [
                 "correctional facilities",
                 "correctional system",
                 "offenders",
                 "prison inmates"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2015-02-04T16:10:54",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2015-02-04T16:08:27",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR35495.v1",
-                    "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 2012"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 2012",
-            "description": "The data contain records of charges filed against defendants whose cases were filed by United States attorneys in United States district court during fiscal year 2012. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2015-02-04T16:16:00",
-            "accessLevel": "restricted public",
-            "identifier": "2318",
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
+            "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 2012"
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
+            "description": "The data contain records of charges filed against defendants whose cases were filed by United States attorneys in United States district court during fiscal year 2012. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR35496.v1",
+                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 2012"
+                }
+            ],
+            "identifier": "2318",
+            "isPartOf": "2174",
+            "issued": "2015-02-04T16:14:36",
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
+            "modified": "2015-02-04T16:16:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2015-02-04T16:14:36",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR35496.v1",
-                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 2012"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 2012",
-            "description": "The data contain records of charges filed against defendants whose cases were terminated by United States attorneys in United States district court during fiscal year 2012. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2015-02-04T16:20:22",
-            "accessLevel": "restricted public",
-            "identifier": "2319",
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
+            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 2012"
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
+            "description": "The data contain records of charges filed against defendants whose cases were terminated by United States attorneys in United States district court during fiscal year 2012. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR35497.v1",
+                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 2012"
+                }
+            ],
+            "identifier": "2319",
+            "isPartOf": "2174",
+            "issued": "2015-02-04T16:18:58",
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
+            "modified": "2015-02-04T16:20:22",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2015-02-04T16:18:58",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR35497.v1",
-                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 2012"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2012",
-            "description": "The data contain records of suspects in federal criminal matters concluded by United States attorneys or United States magistrates during fiscal year 2012. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.2-1.5. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2015-02-04T16:26:04",
-            "accessLevel": "restricted public",
-            "identifier": "2320",
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
+            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court -- Terminated, 2012"
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
+            "description": "The data contain records of suspects in federal criminal matters concluded by United States attorneys or United States magistrates during fiscal year 2012. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.2-1.5. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR35498.v1",
+                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2012"
+                }
+            ],
+            "identifier": "2320",
+            "isPartOf": "2174",
+            "issued": "2015-02-04T16:24:27",
             "keyword": [
                 "defendants",
                 "federal courts",
@@ -57943,110 +57937,110 @@
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2015-02-04T16:26:04",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2015-02-04T16:24:27",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR35498.v1",
-                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2012"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 2012",
-            "description": "The data contain records of defendants in federal criminal cases terminated in United States District Court during fiscal year 2012. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2015-02-04T16:30:37",
-            "accessLevel": "restricted public",
-            "identifier": "2321",
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
+            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2012"
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
+            "description": "The data contain records of defendants in federal criminal cases terminated in United States District Court during fiscal year 2012. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR35499.v1",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 2012"
+                }
+            ],
+            "identifier": "2321",
+            "isPartOf": "2174",
+            "issued": "2015-02-04T16:29:19",
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
+            "modified": "2015-02-04T16:30:37",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2015-02-04T16:29:19",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR35499.v1",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 2012"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data: Arrests by Age, Sex, and Race, Summarized Yearly, United States, 2014",
-            "description": "These data provide information on the number of arrests\r\nreported to the Federal Bureau of Investigation's Uniform Crime\r\nReporting (UCR) Program each year by police agencies in the United\r\nStates. These arrest reports provide data on 43 offenses including\r\nviolent crime, drug use, gambling, and larceny. The data received by\r\nICPSR were structured as a hierarchical file containing, per reporting\r\npolice agency: an agency header record, and 1 to 43 detail offense\r\nrecords containing the counts of arrests by age, sex, and race for a\r\nparticular offense. ICPSR restructured the original data to logical\r\nrecord length format with the agency header record variables copied\r\nonto the detail records. Consequently, each record contains arrest\r\ncounts for a particular agency-offense.",
-            "modified": "2016-03-09T12:21:55",
-            "accessLevel": "public",
-            "identifier": "2322",
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 2012"
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
+            "description": "These data provide information on the number of arrests\r\nreported to the Federal Bureau of Investigation's Uniform Crime\r\nReporting (UCR) Program each year by police agencies in the United\r\nStates. These arrest reports provide data on 43 offenses including\r\nviolent crime, drug use, gambling, and larceny. The data received by\r\nICPSR were structured as a hierarchical file containing, per reporting\r\npolice agency: an agency header record, and 1 to 43 detail offense\r\nrecords containing the counts of arrests by age, sex, and race for a\r\nparticular offense. ICPSR restructured the original data to logical\r\nrecord length format with the agency header record variables copied\r\nonto the detail records. Consequently, each record contains arrest\r\ncounts for a particular agency-offense.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR36400.v1",
+                    "title": "Uniform Crime Reporting Program Data: Arrests by Age, Sex, and Race, Summarized Yearly, United States, 2014"
+                }
+            ],
+            "identifier": "2322",
+            "isPartOf": "2167",
+            "issued": "2016-03-09T12:21:55",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrest records",
@@ -58062,54 +58056,54 @@
                 "offenses",
                 "violent crime"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2016-03-09T12:21:55",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2016-03-09T12:21:55",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR36400.v1",
-                    "title": "Uniform Crime Reporting Program Data: Arrests by Age, Sex, and Race, Summarized Yearly, United States, 2014"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Corrections Reporting Program, 1991-2014: Selected Variables",
-            "description": "The National Corrections Reporting Program (NCRP) compiles offender-level data on admissions and releases from state and federal prisons and post-confinement community supervision. The data are used to monitor the nation's correctional population and address specific policy questions related to recidivism, prisoner reentry, and trends in demographic characteristics of the incarcerated and community supervision populations. The Bureau of Justice Statistics (BJS) has administered the NCRP since 1983. Abt Associates has served as the NCRP data collection agent since October 2010.\r\nThis version of the NCRP contains selected variables making it suitable for public release.",
-            "modified": "2016-09-07T09:43:22",
-            "accessLevel": "public",
-            "identifier": "2323",
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
+            "title": "Uniform Crime Reporting Program Data: Arrests by Age, Sex, and Race, Summarized Yearly, United States, 2014"
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
+            "description": "The National Corrections Reporting Program (NCRP) compiles offender-level data on admissions and releases from state and federal prisons and post-confinement community supervision. The data are used to monitor the nation's correctional population and address specific policy questions related to recidivism, prisoner reentry, and trends in demographic characteristics of the incarcerated and community supervision populations. The Bureau of Justice Statistics (BJS) has administered the NCRP since 1983. Abt Associates has served as the NCRP data collection agent since October 2010.\r\nThis version of the NCRP contains selected variables making it suitable for public release.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR36404.v2",
+                    "title": "National Corrections Reporting Program, 1991-2014: Selected Variables"
+                }
+            ],
+            "identifier": "2323",
+            "isPartOf": "2589",
+            "issued": "2016-04-13T11:33:43",
             "keyword": [
                 "correctional facilities",
                 "correctional facilities (juveniles)",
@@ -58126,54 +58120,54 @@
                 "probation",
                 "state correctional facilities"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2016-09-07T09:43:22",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2589",
-            "dataQuality": false,
-            "issued": "2016-04-13T11:33:43",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR36404.v2",
-                    "title": "National Corrections Reporting Program, 1991-2014: Selected Variables"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Incident-Based Reporting System, 2014: Extract Files",
-            "description": "The National Incident-Based Reporting System (NIBRS) is a\r\npart of the Uniform Crime Reporting Program (UCR), administered by the\r\nFederal Bureau of Investigation (FBI). The extract files version of\r\nNIBRS was created to simplify working with NIBRS data. Data management\r\nissues with NIBRS are significant, especially when two or more segment\r\nlevels are being merged. These issues require skills separate from\r\ndata analysis. NIBRS data as formatted by the FBI are stored in a\r\nsingle file. These data are organized by various segment levels\r\n(record types). There are six main segment levels: administrative,\r\noffense, property, victim, offender, and arrestee. Each segment level\r\nhas a different length and layout. There are other segment levels that\r\noccur with less frequency than the six main levels. Significant\r\ncomputing resources are necessary to work with the data in its\r\nsingle-file format. In addition, the user must be sophisticated in\r\nworking with data in complex file types. For these reasons and the\r\ndesire to facilitate the use of NIBRS data, ICPSR created the extract\r\nfiles. The data are not a representative sample of crime in the United\r\nStates.",
-            "modified": "2018-10-03T14:24:04",
-            "accessLevel": "public",
-            "identifier": "2324",
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
+            "title": "National Corrections Reporting Program, 1991-2014: Selected Variables"
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
+                    "accessURL": "https://doi.org/10.3886/ICPSR36421.v2",
+                    "title": "National Incident-Based Reporting System, 2014: Extract Files"
+                }
+            ],
+            "identifier": "2324",
+            "isPartOf": "2433",
+            "issued": "2016-04-01T12:47:24",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -58188,54 +58182,54 @@
                 "victims",
                 "violent crime"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2018-10-03T14:24:04",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2433",
-            "dataQuality": false,
-            "issued": "2016-04-01T12:47:24",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR36421.v2",
-                    "title": "National Incident-Based Reporting System, 2014: Extract Files"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Deaths in Custody Reporting Program: State Prisons, 2001 - 2013",
-            "description": "The Deaths in Custody Reporting Program (DCRP) is an annual data collection\r\nconducted by the Bureau of Justice Statistics (BJS). The DCRP began in 2000\r\nunder the Death in Custody Reporting Act of 2000 (P.L. 106-297). It is the\r\nonly national statistical collection that obtains detailed information\r\nabout deaths in adult correctional facilities. The DCRP collects data on\r\npersons dying in state prisons, local jails and in the process of\r\narrest. Each collection is a separate subcollection, but each is under the\r\numbrella of the DCRP collection. This deals with the prison subcollection,\r\nwhich has a prison death file.\r\nThe prison portion of the Deaths in Custody Reporting Program began in 2001\r\nafter the passage of the Deaths in Custody Reporting Act of 2000 in October\r\nof 2000. The prison component of the DCRP collects data on inmate deaths\r\noccurring in the 50 state departments of corrections while inmates are in\r\nthe physical custody of prison officials.",
-            "modified": "2016-08-31T11:07:25",
-            "accessLevel": "restricted public",
-            "identifier": "2325",
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
+            "title": "National Incident-Based Reporting System, 2014: Extract Files"
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
+                    "accessURL": "https://doi.org/10.3886/ICPSR36435.v1",
+                    "title": "Deaths in Custody Reporting Program: State Prisons, 2001 - 2013"
+                }
+            ],
+            "identifier": "2325",
+            "isPartOf": "2441",
+            "issued": "2016-08-31T11:04:56",
             "keyword": [
                 "correctional facilities",
                 "corrections",
@@ -58243,55 +58237,55 @@
                 "homicide",
                 "suicide"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2016-08-31T11:07:25",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2441",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2016-08-31T11:04:56",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR36435.v1",
-                    "title": "Deaths in Custody Reporting Program: State Prisons, 2001 - 2013"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Victimization Survey, [United States], 2015",
-            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a nationally-representative sample of residential addresses since 1973. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, motor vehicle theft, and vandalism. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations. This version of the NCVS, referred to as the collection year, contains records from interviews conducted in the 12 months of the given year.",
-            "modified": "2020-07-23T16:26:44",
-            "accessLevel": "public",
-            "identifier": "2326",
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
+            "title": "Deaths in Custody Reporting Program: State Prisons, 2001 - 2013"
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
+            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a nationally-representative sample of residential addresses since 1973. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, motor vehicle theft, and vandalism. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations. This version of the NCVS, referred to as the collection year, contains records from interviews conducted in the 12 months of the given year.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR36448.v2",
+                    "title": "National Crime Victimization Survey, [United States], 2015"
+                }
+            ],
+            "identifier": "2326",
+            "isPartOf": "2432",
+            "issued": "2016-10-20T09:18:33",
             "keyword": [
                 "assault",
                 "auto theft",
@@ -58312,54 +58306,54 @@
                 "victimization",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2020-07-23T16:26:44",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2016-10-20T09:18:33",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR36448.v2",
-                    "title": "National Crime Victimization Survey, [United States], 2015"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Victimization Survey, Concatenated File, 1992-2015",
-            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a nationally-representative sample of residential addresses since 1973. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, motor vehicle theft, and vandalism. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations. \r\nThis dataset represents the concatenated version of the NCVS on a collection year basis for 1992-2015.  A collection year contains records from interviews conducted in the 12 months of the given year.  Under the collection year format, victimizations are counted in the year the interview is conducted, regardless of the year when the crime incident occurred.\r\nFor additional information, please see the documentation for the data from the most current year of the NCVS, ICPSR Study 36142.",
-            "modified": "2016-10-20T10:17:13",
-            "accessLevel": "public",
-            "identifier": "2327",
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
+            "title": "National Crime Victimization Survey, [United States], 2015"
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
+            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a nationally-representative sample of residential addresses since 1973. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, motor vehicle theft, and vandalism. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations. \r\nThis dataset represents the concatenated version of the NCVS on a collection year basis for 1992-2015.  A collection year contains records from interviews conducted in the 12 months of the given year.  Under the collection year format, victimizations are counted in the year the interview is conducted, regardless of the year when the crime incident occurred.\r\nFor additional information, please see the documentation for the data from the most current year of the NCVS, ICPSR Study 36142.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR36456.v1",
+                    "title": "National Crime Victimization Survey, Concatenated File, 1992-2015"
+                }
+            ],
+            "identifier": "2327",
+            "isPartOf": "2432",
+            "issued": "2016-10-20T10:17:13",
             "keyword": [
                 "assault",
                 "auto theft",
@@ -58380,108 +58374,108 @@
                 "victimization",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2016-10-20T10:17:13",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2016-10-20T10:17:13",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR36456.v1",
-                    "title": "National Crime Victimization Survey, Concatenated File, 1992-2015"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Survey of State Court Criminal Appeals, 2010",
-            "description": "State appellate courts were created to detect and correct errors in trial\r\ncourt decisions and provide fair, consistent, and timely resolutions to all\r\nappeals.  The Survey of State Court Criminal Appeals, 2010 (SSCCA) data\r\nwere collected from a nationally representative sample of all criminal\r\nappeals disposed in all 143 state appellate courts in 2010.  The data\r\ninclude state court criminal appeals, resolution of appeals, and time to\r\nresolution.",
-            "modified": "2016-07-05T17:26:45",
-            "accessLevel": "restricted public",
-            "identifier": "2328",
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
+            "title": "National Crime Victimization Survey, Concatenated File, 1992-2015"
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
+            "description": "State appellate courts were created to detect and correct errors in trial\r\ncourt decisions and provide fair, consistent, and timely resolutions to all\r\nappeals.  The Survey of State Court Criminal Appeals, 2010 (SSCCA) data\r\nwere collected from a nationally representative sample of all criminal\r\nappeals disposed in all 143 state appellate courts in 2010.  The data\r\ninclude state court criminal appeals, resolution of appeals, and time to\r\nresolution.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR36465.v1",
+                    "title": "Survey of State Court Criminal Appeals, 2010"
+                }
+            ],
+            "identifier": "2328",
+            "isPartOf": "2179",
+            "issued": "2016-07-05T17:21:44",
             "keyword": [
                 "appellate courts",
                 "criminal courts",
                 "offenses"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2016-07-05T17:26:45",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2179",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2016-07-05T17:21:44",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR36465.v1",
-                    "title": "Survey of State Court Criminal Appeals, 2010"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Court Cases: Integrated Data Base Bankruptcy Petitions, 2008",
-            "description": "In 2008, the Administrative Office of the United States Courts (AOUSC) began implementing the NewSTATS (New Streamline Timely Access to Statistics) Project with respect to bankruptcy data. The project's goals were to modernize the system for collecting, processing, analyzing, and reporting statistics of the federal court system. Based on the records for bankruptcy cases in NewSTATS, a data base for internal use in the Research Division of the Federal Judicial Center has been created. That data base is the Bankruptcy Petition NewSTATS Snapshots [BPNS] Data Base.",
-            "modified": "2017-01-05T10:02:48",
-            "accessLevel": "restricted public",
-            "identifier": "2329",
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
+            "title": "Survey of State Court Criminal Appeals, 2010"
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
+            "description": "In 2008, the Administrative Office of the United States Courts (AOUSC) began implementing the NewSTATS (New Streamline Timely Access to Statistics) Project with respect to bankruptcy data. The project's goals were to modernize the system for collecting, processing, analyzing, and reporting statistics of the federal court system. Based on the records for bankruptcy cases in NewSTATS, a data base for internal use in the Research Division of the Federal Judicial Center has been created. That data base is the Bankruptcy Petition NewSTATS Snapshots [BPNS] Data Base.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR36468.v1",
+                    "title": "Federal Court Cases: Integrated Data Base Bankruptcy Petitions, 2008"
+                }
+            ],
+            "identifier": "2329",
+            "isPartOf": "2173",
+            "issued": "2016-08-08T17:01:48",
             "keyword": [
                 "administration",
                 "appellate courts",
@@ -58499,55 +58493,55 @@
                 "trial courts",
                 "trial procedures"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2017-01-05T10:02:48",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2173",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2016-08-08T17:01:48",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR36468.v1",
-                    "title": "Federal Court Cases: Integrated Data Base Bankruptcy Petitions, 2008"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Court Cases: Integrated Data Base Bankruptcy Petitions, 2009",
-            "description": "In 2008, the Administrative Office of the United States Courts (AOUSC) began implementing the NewSTATS (New Streamline Timely Access to Statistics) Project with respect to bankruptcy data. The project's goals were to modernize the system for collecting, processing, analyzing, and reporting statistics of the federal court system. Based on the records for bankruptcy cases in NewSTATS, a data base for internal use in the Research Division of the Federal Judicial Center has been created. That data base is the Bankruptcy Petition NewSTATS Snapshots [BPNS] Data Base.",
-            "modified": "2017-01-05T10:18:49",
-            "accessLevel": "restricted public",
-            "identifier": "2330",
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
+            "title": "Federal Court Cases: Integrated Data Base Bankruptcy Petitions, 2008"
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
+            "description": "In 2008, the Administrative Office of the United States Courts (AOUSC) began implementing the NewSTATS (New Streamline Timely Access to Statistics) Project with respect to bankruptcy data. The project's goals were to modernize the system for collecting, processing, analyzing, and reporting statistics of the federal court system. Based on the records for bankruptcy cases in NewSTATS, a data base for internal use in the Research Division of the Federal Judicial Center has been created. That data base is the Bankruptcy Petition NewSTATS Snapshots [BPNS] Data Base.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR36483.v1",
+                    "title": "Federal Court Cases: Integrated Data Base Bankruptcy Petitions, 2009"
+                }
+            ],
+            "identifier": "2330",
+            "isPartOf": "2173",
+            "issued": "2016-08-08T17:15:27",
             "keyword": [
                 "administration",
                 "appellate courts",
@@ -58565,55 +58559,55 @@
                 "trial courts",
                 "trial procedures"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2017-01-05T10:18:49",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2173",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2016-08-08T17:15:27",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR36483.v1",
-                    "title": "Federal Court Cases: Integrated Data Base Bankruptcy Petitions, 2009"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Court Cases: Integrated Data Base Bankruptcy Petitions, 2010",
-            "description": "In 2008, the Administrative Office of the United States Courts (AOUSC) began implementing the NewSTATS (New Streamline Timely Access to Statistics) Project with respect to bankruptcy data. The project's goals were to modernize the system for collecting, processing, analyzing, and reporting statistics of the federal court system. Based on the records for bankruptcy cases in NewSTATS, a data base for internal use in the Research Division of the Federal Judicial Center has been created. That data base is the Bankruptcy Petition NewSTATS Snapshots [BPNS] Data Base.",
-            "modified": "2017-01-05T10:25:47",
-            "accessLevel": "restricted public",
-            "identifier": "2331",
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
+            "title": "Federal Court Cases: Integrated Data Base Bankruptcy Petitions, 2009"
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
+            "description": "In 2008, the Administrative Office of the United States Courts (AOUSC) began implementing the NewSTATS (New Streamline Timely Access to Statistics) Project with respect to bankruptcy data. The project's goals were to modernize the system for collecting, processing, analyzing, and reporting statistics of the federal court system. Based on the records for bankruptcy cases in NewSTATS, a data base for internal use in the Research Division of the Federal Judicial Center has been created. That data base is the Bankruptcy Petition NewSTATS Snapshots [BPNS] Data Base.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR36484.v1",
+                    "title": "Federal Court Cases: Integrated Data Base Bankruptcy Petitions, 2010"
+                }
+            ],
+            "identifier": "2331",
+            "isPartOf": "2173",
+            "issued": "2016-08-08T17:43:29",
             "keyword": [
                 "administration",
                 "appellate courts",
@@ -58631,55 +58625,55 @@
                 "trial courts",
                 "trial procedures"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2017-01-05T10:25:47",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2173",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2016-08-08T17:43:29",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR36484.v1",
-                    "title": "Federal Court Cases: Integrated Data Base Bankruptcy Petitions, 2010"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Court Cases: Integrated Data Base Bankruptcy Petitions, 2011",
-            "description": "In 2008, the Administrative Office of the United States Courts (AOUSC) began implementing the NewSTATS (New Streamline Timely Access to Statistics) Project with respect to bankruptcy data. The project's goals were to modernize the system for collecting, processing, analyzing, and reporting statistics of the federal court system. Based on the records for bankruptcy cases in NewSTATS, a data base for internal use in the Research Division of the Federal Judicial Center has been created. That data base is the Bankruptcy Petition NewSTATS Snapshots [BPNS] Data Base.",
-            "modified": "2017-01-05T10:37:28",
-            "accessLevel": "restricted public",
-            "identifier": "2332",
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
+            "title": "Federal Court Cases: Integrated Data Base Bankruptcy Petitions, 2010"
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
+            "description": "In 2008, the Administrative Office of the United States Courts (AOUSC) began implementing the NewSTATS (New Streamline Timely Access to Statistics) Project with respect to bankruptcy data. The project's goals were to modernize the system for collecting, processing, analyzing, and reporting statistics of the federal court system. Based on the records for bankruptcy cases in NewSTATS, a data base for internal use in the Research Division of the Federal Judicial Center has been created. That data base is the Bankruptcy Petition NewSTATS Snapshots [BPNS] Data Base.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR36485.v1",
+                    "title": "Federal Court Cases: Integrated Data Base Bankruptcy Petitions, 2011"
+                }
+            ],
+            "identifier": "2332",
+            "isPartOf": "2173",
+            "issued": "2016-08-08T17:59:47",
             "keyword": [
                 "administration",
                 "appellate courts",
@@ -58697,55 +58691,55 @@
                 "trial courts",
                 "trial procedures"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2017-01-05T10:37:28",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2173",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2016-08-08T17:59:47",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR36485.v1",
-                    "title": "Federal Court Cases: Integrated Data Base Bankruptcy Petitions, 2011"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Court Cases: Integrated Data Base Bankruptcy Petitions, 2012",
-            "description": "In 2008, the Administrative Office of the United States Courts (AOUSC) began implementing the NewSTATS (New Streamline Timely Access to Statistics) Project with respect to bankruptcy data. The project's goals were to modernize the system for collecting, processing, analyzing, and reporting statistics of the federal court system. Based on the records for bankruptcy cases in NewSTATS, a data base for internal use in the Research Division of the Federal Judicial Center has been created. That data base is the Bankruptcy Petition NewSTATS Snapshots [BPNS] Data Base.",
-            "modified": "2017-01-05T10:51:22",
-            "accessLevel": "restricted public",
-            "identifier": "2333",
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
+            "title": "Federal Court Cases: Integrated Data Base Bankruptcy Petitions, 2011"
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
+            "description": "In 2008, the Administrative Office of the United States Courts (AOUSC) began implementing the NewSTATS (New Streamline Timely Access to Statistics) Project with respect to bankruptcy data. The project's goals were to modernize the system for collecting, processing, analyzing, and reporting statistics of the federal court system. Based on the records for bankruptcy cases in NewSTATS, a data base for internal use in the Research Division of the Federal Judicial Center has been created. That data base is the Bankruptcy Petition NewSTATS Snapshots [BPNS] Data Base.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR36486.v1",
+                    "title": "Federal Court Cases: Integrated Data Base Bankruptcy Petitions, 2012"
+                }
+            ],
+            "identifier": "2333",
+            "isPartOf": "2173",
+            "issued": "2016-08-08T18:15:31",
             "keyword": [
                 "administration",
                 "appellate courts",
@@ -58763,55 +58757,55 @@
                 "trial courts",
                 "trial procedures"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2017-01-05T10:51:22",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2173",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2016-08-08T18:15:31",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR36486.v1",
-                    "title": "Federal Court Cases: Integrated Data Base Bankruptcy Petitions, 2012"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Court Cases: Integrated Data Base Bankruptcy Petitions, 2013",
-            "description": "In 2008, the Administrative Office of the United States Courts (AOUSC) began implementing the NewSTATS (New Streamline Timely Access to Statistics) Project with respect to bankruptcy data. The project's goals were to modernize the system for collecting, processing, analyzing, and reporting statistics of the federal court system. Based on the records for bankruptcy cases in NewSTATS, a data base for internal use in the Research Division of the Federal Judicial Center has been created. That data base is the Bankruptcy Petition NewSTATS Snapshots [BPNS] Data Base.",
-            "modified": "2017-01-05T11:05:11",
-            "accessLevel": "restricted public",
-            "identifier": "2334",
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
+            "title": "Federal Court Cases: Integrated Data Base Bankruptcy Petitions, 2012"
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
+            "description": "In 2008, the Administrative Office of the United States Courts (AOUSC) began implementing the NewSTATS (New Streamline Timely Access to Statistics) Project with respect to bankruptcy data. The project's goals were to modernize the system for collecting, processing, analyzing, and reporting statistics of the federal court system. Based on the records for bankruptcy cases in NewSTATS, a data base for internal use in the Research Division of the Federal Judicial Center has been created. That data base is the Bankruptcy Petition NewSTATS Snapshots [BPNS] Data Base.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR36487.v1",
+                    "title": "Federal Court Cases: Integrated Data Base Bankruptcy Petitions, 2013"
+                }
+            ],
+            "identifier": "2334",
+            "isPartOf": "2173",
+            "issued": "2016-08-09T10:22:28",
             "keyword": [
                 "administration",
                 "appellate courts",
@@ -58829,55 +58823,55 @@
                 "trial courts",
                 "trial procedures"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2017-01-05T11:05:11",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2173",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2016-08-09T10:22:28",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR36487.v1",
-                    "title": "Federal Court Cases: Integrated Data Base Bankruptcy Petitions, 2013"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court - Pending, 2016",
-            "description": "The data contain records of defendants in criminal cases filed in United States District Court before or during fiscal year 2016 and still pending as of year-end. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables. Variables containing identifying information (e.g., name, Social Security number) were either removed, coarsened, or blanked in order to protect the identities of individuals. These data are part of a series designed by Abt and the Bureau of Justice Statistics. Data and documentation were prepared by Abt.",
-            "modified": "2019-12-19T11:24:55",
-            "accessLevel": "restricted public",
-            "identifier": "2335",
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
+            "title": "Federal Court Cases: Integrated Data Base Bankruptcy Petitions, 2013"
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
+            "description": "The data contain records of defendants in criminal cases filed in United States District Court before or during fiscal year 2016 and still pending as of year-end. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables. Variables containing identifying information (e.g., name, Social Security number) were either removed, coarsened, or blanked in order to protect the identities of individuals. These data are part of a series designed by Abt and the Bureau of Justice Statistics. Data and documentation were prepared by Abt.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR37389.v1",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court - Pending, 2016"
+                }
+            ],
+            "identifier": "2335",
+            "isPartOf": "2174",
+            "issued": "2019-12-19T11:21:39",
             "keyword": [
                 "administration",
                 "court cases",
@@ -58889,110 +58883,110 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2019-12-19T11:24:55",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2019-12-19T11:21:39",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR37389.v1",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court - Pending, 2016"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court - Terminated, 2015",
-            "description": "The data contain records of charges filed against defendants whose cases were terminated by United States attorneys in United States district court during fiscal year 2015. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables. Variables containing identifying information (e.g., name, Social Security Number) were either removed, coarsened, or blanked in order to protect the identities of individuals. These data are part of a series designed by Abt and the Bureau of Justice Statistics. Data and documentation were prepared by Abt.",
-            "modified": "2019-09-25T10:15:34",
-            "accessLevel": "restricted public",
-            "identifier": "2336",
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court - Pending, 2016"
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
+            "description": "The data contain records of charges filed against defendants whose cases were terminated by United States attorneys in United States district court during fiscal year 2015. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables. Variables containing identifying information (e.g., name, Social Security Number) were either removed, coarsened, or blanked in order to protect the identities of individuals. These data are part of a series designed by Abt and the Bureau of Justice Statistics. Data and documentation were prepared by Abt.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR37390.v1",
+                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court - Terminated, 2015"
+                }
+            ],
+            "identifier": "2336",
+            "isPartOf": "2174",
+            "issued": "2019-09-25T10:13:43",
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
+            "modified": "2019-09-25T10:15:34",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2019-09-25T10:13:43",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR37390.v1",
-                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court - Terminated, 2015"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals - Terminated, 2016",
-            "description": "The data contain records of criminal appeals cases terminated in United States Courts of Appeals during fiscal year 2016. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. Appeals may be terminated on the merits or on procedural grounds. Of those that are terminated on the merits, the district court ruling may be affirmed, reversed, remanded to criminal court, or dismissed. The data file contains variables from the original AOUSC files as well as additional analysis variables. Variables containing identifying information (e.g., name, Social Security number) were either removed, coarsened, or blanked in order to protect the identities of individuals. These data are part of a series designed by Abt and the Bureau of Justice Statistics. Data and documentation were prepared by Abt.",
-            "modified": "2019-12-19T09:41:45",
-            "accessLevel": "restricted public",
-            "identifier": "2337",
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
+            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court - Terminated, 2015"
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
+            "description": "The data contain records of criminal appeals cases terminated in United States Courts of Appeals during fiscal year 2016. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. Appeals may be terminated on the merits or on procedural grounds. Of those that are terminated on the merits, the district court ruling may be affirmed, reversed, remanded to criminal court, or dismissed. The data file contains variables from the original AOUSC files as well as additional analysis variables. Variables containing identifying information (e.g., name, Social Security number) were either removed, coarsened, or blanked in order to protect the identities of individuals. These data are part of a series designed by Abt and the Bureau of Justice Statistics. Data and documentation were prepared by Abt.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR37391.v1",
+                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals - Terminated, 2016"
+                }
+            ],
+            "identifier": "2337",
+            "isPartOf": "2174",
+            "issued": "2019-12-19T09:39:49",
             "keyword": [
                 "administration",
                 "appellate courts",
@@ -59003,55 +58997,55 @@
                 "judicial decisions",
                 "legal systems"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2019-12-19T09:41:45",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2019-12-19T09:39:49",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR37391.v1",
-                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals - Terminated, 2016"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Survey of Jails, 2018",
-            "description": "The Annual Survey of Jails (ASJ) is the only data collection effort that provides an annual source of data on local jails and jail inmates. Data on the size of the jail population and selected inmate characteristics are obtained every five to six years from the Census of Jails. In each of the years between the complete censuses, a sample survey of jails is conducted to estimate\r\nbaseline characteristics of the nation's jails and inmates housed in these jails. The 2018 Annual Survey of Jails is the 31st such survey in a series begun in 1982. The ASJ supplies data on characteristics of jails such as admissions and releases, growth in the number of jail facilities, changes in their rated capacities and level of occupancy, growth in the population supervised in the community, changes in methods of community supervision, and crowding issues. The ASJ also provides information on changes in the demographics of the jail population, supervision status of persons held, and a count of non-U.S. citizens in custody. The data presented in this study were collected in the Annual Survey of Jails, 2018. These data are used to track growth in the number of jails and the capacities nationally, changes in the demographics of the jail population and supervision status of persons held, the prevalence of crowding issues, and a count of non-U.S. citizens within the jail population. The data are intended for a variety of users, including Federal and State agencies, local officials in conjunction with jail administrators, researchers, planners, and the public. The reference date for the survey is June 29, 2018.",
-            "modified": "2020-04-23T09:19:18",
-            "accessLevel": "public",
-            "identifier": "2338",
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
+            "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals - Terminated, 2016"
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
+            "description": "The Annual Survey of Jails (ASJ) is the only data collection effort that provides an annual source of data on local jails and jail inmates. Data on the size of the jail population and selected inmate characteristics are obtained every five to six years from the Census of Jails. In each of the years between the complete censuses, a sample survey of jails is conducted to estimate\r\nbaseline characteristics of the nation's jails and inmates housed in these jails. The 2018 Annual Survey of Jails is the 31st such survey in a series begun in 1982. The ASJ supplies data on characteristics of jails such as admissions and releases, growth in the number of jail facilities, changes in their rated capacities and level of occupancy, growth in the population supervised in the community, changes in methods of community supervision, and crowding issues. The ASJ also provides information on changes in the demographics of the jail population, supervision status of persons held, and a count of non-U.S. citizens in custody. The data presented in this study were collected in the Annual Survey of Jails, 2018. These data are used to track growth in the number of jails and the capacities nationally, changes in the demographics of the jail population and supervision status of persons held, the prevalence of crowding issues, and a count of non-U.S. citizens within the jail population. The data are intended for a variety of users, including Federal and State agencies, local officials in conjunction with jail administrators, researchers, planners, and the public. The reference date for the survey is June 29, 2018.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR37392.v1",
+                    "title": "Annual Survey of Jails, 2018"
+                }
+            ],
+            "identifier": "2338",
+            "isPartOf": "2586",
+            "issued": "2020-04-23T09:19:18",
             "keyword": [
                 "correctional facilities",
                 "correctional system",
@@ -59061,54 +59055,54 @@
                 "population characteristics",
                 "probation"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2020-04-23T09:19:18",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2586",
-            "dataQuality": false,
-            "issued": "2020-04-23T09:19:18",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR37392.v1",
-                    "title": "Annual Survey of Jails, 2018"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court - Terminated, 2016",
-            "description": "The data contain records of defendants in criminal cases terminated in United States District Court during fiscal year 2016. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables. Variables containing identifying information (e.g., name, Social Security number) were either removed, coarsened, or blanked in order to protect the identities of individuals. These data are part of a series designed by Abt and the Bureau of Justice Statistics. Data and documentation were prepared by Abt.",
-            "modified": "2019-12-19T11:14:37",
-            "accessLevel": "restricted public",
-            "identifier": "2339",
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
+            "title": "Annual Survey of Jails, 2018"
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
+            "description": "The data contain records of defendants in criminal cases terminated in United States District Court during fiscal year 2016. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables. Variables containing identifying information (e.g., name, Social Security number) were either removed, coarsened, or blanked in order to protect the identities of individuals. These data are part of a series designed by Abt and the Bureau of Justice Statistics. Data and documentation were prepared by Abt.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR37393.v1",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court - Terminated, 2016"
+                }
+            ],
+            "identifier": "2339",
+            "isPartOf": "2174",
+            "issued": "2019-12-19T11:10:22",
             "keyword": [
                 "administration",
                 "court cases",
@@ -59120,55 +59114,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2019-12-19T11:14:37",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2019-12-19T11:10:22",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR37393.v1",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court - Terminated, 2016"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2016",
-            "description": "The data contain records of defendants in criminal cases filed in United States District Court during fiscal year 2016. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables. Variables containing identifying information (e.g., name, Social Security number) were either removed, coarsened, or blanked in order to protect the identities of individuals. These data are part of a series designed by Abt and the Bureau of Justice Statistics. Data and documentation were prepared by Abt.",
-            "modified": "2019-12-19T10:18:02",
-            "accessLevel": "restricted public",
-            "identifier": "2340",
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court - Terminated, 2016"
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
+            "description": "The data contain records of defendants in criminal cases filed in United States District Court during fiscal year 2016. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables. Variables containing identifying information (e.g., name, Social Security number) were either removed, coarsened, or blanked in order to protect the identities of individuals. These data are part of a series designed by Abt and the Bureau of Justice Statistics. Data and documentation were prepared by Abt.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR37399.v1",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2016"
+                }
+            ],
+            "identifier": "2340",
+            "isPartOf": "2174",
+            "issued": "2019-12-19T10:11:51",
             "keyword": [
                 "administration",
                 "court cases",
@@ -59180,55 +59174,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2019-12-19T10:18:02",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2019-12-19T10:11:51",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR37399.v1",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2016"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2016",
-            "description": "The data contain records of sentenced offenders committed to the custody of the Bureau of Prisons (BOP) during fiscal year 2016. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database as well as additional analysis variables. Variables containing identifying information (e.g., name, Social Security Number) were either removed, coarsened, or blanked in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, D.C.) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute through 2012. Data from 2013 and on were prepared by Abt Associates.",
-            "modified": "2019-12-16T13:31:30",
-            "accessLevel": "restricted public",
-            "identifier": "2341",
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2016"
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
+            "description": "The data contain records of sentenced offenders committed to the custody of the Bureau of Prisons (BOP) during fiscal year 2016. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database as well as additional analysis variables. Variables containing identifying information (e.g., name, Social Security Number) were either removed, coarsened, or blanked in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, D.C.) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute through 2012. Data from 2013 and on were prepared by Abt Associates.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR37400.v1",
+                    "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2016"
+                }
+            ],
+            "identifier": "2341",
+            "isPartOf": "2174",
+            "issued": "2019-12-16T13:24:31",
             "keyword": [
                 "correctional facilities",
                 "correctional system",
@@ -59236,55 +59230,55 @@
                 "offenders",
                 "sentencing"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2019-12-16T13:31:30",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2019-12-16T13:24:31",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR37400.v1",
-                    "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2016"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 2016",
-            "description": "The data contain records of arrests and bookings for federal offenses in the United States during fiscal year 2016. The data were constructed from the United States Marshals Service (USMS) Prisoner Tracking System database. Records include arrests made by federal law enforcement agencies (including the USMS), state and local agencies, and self-surrenders. Offenders arrested for federal offenses are transferred to the custody of the USMS for processing, transportation, and detention. The Prisoner Tracking System contains data on all offenders within the custody of the USMS. The data file contains variables from the original USMS files as well as additional analysis variables. Variables containing identifying information (e.g., name, Social Security number) were either removed, coarsened, or blanked in order to protect the identities of individuals. These data are part of a series designed by Abt and the Bureau of Justice Statistics. Data and documentation were prepared by Abt.",
-            "modified": "2019-12-17T10:12:42",
-            "accessLevel": "restricted public",
-            "identifier": "2342",
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
+            "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2016"
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
+            "description": "The data contain records of arrests and bookings for federal offenses in the United States during fiscal year 2016. The data were constructed from the United States Marshals Service (USMS) Prisoner Tracking System database. Records include arrests made by federal law enforcement agencies (including the USMS), state and local agencies, and self-surrenders. Offenders arrested for federal offenses are transferred to the custody of the USMS for processing, transportation, and detention. The Prisoner Tracking System contains data on all offenders within the custody of the USMS. The data file contains variables from the original USMS files as well as additional analysis variables. Variables containing identifying information (e.g., name, Social Security number) were either removed, coarsened, or blanked in order to protect the identities of individuals. These data are part of a series designed by Abt and the Bureau of Justice Statistics. Data and documentation were prepared by Abt.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR37409.v1",
+                    "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 2016"
+                }
+            ],
+            "identifier": "2342",
+            "isPartOf": "2174",
+            "issued": "2019-12-17T10:10:47",
             "keyword": [
                 "arrest records",
                 "arrests",
@@ -59292,275 +59286,275 @@
                 "federal prisoners",
                 "offenders"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2019-12-17T10:12:42",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2019-12-17T10:10:47",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR37409.v1",
-                    "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 2016"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Offenders Released From Prison, 2016",
-            "description": "The data contain records of sentenced offenders released from the custody of the Bureau of Prisons (BOP) during fiscal year 2016. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. Records of offenders who exit federal prison temporarily, such as for transit to another location, to serve a weekend sentence, or for health care, are not included in the exiting cohort. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database as well as additional analysis variables. Variables containing identifying information (e.g., name, Social Security Number) were either removed, coarsened, or blanked in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, D.C.) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute through 2012. Data from 2013 and on were prepared by Abt Associates.",
-            "modified": "2019-12-16T13:51:06",
-            "accessLevel": "restricted public",
-            "identifier": "2343",
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
+            "title": "Federal Justice Statistics Program: Arrests and Bookings for Federal Offenses, 2016"
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
+            "description": "The data contain records of sentenced offenders released from the custody of the Bureau of Prisons (BOP) during fiscal year 2016. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. Records of offenders who exit federal prison temporarily, such as for transit to another location, to serve a weekend sentence, or for health care, are not included in the exiting cohort. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database as well as additional analysis variables. Variables containing identifying information (e.g., name, Social Security Number) were either removed, coarsened, or blanked in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, D.C.) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute through 2012. Data from 2013 and on were prepared by Abt Associates.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR37410.v1",
+                    "title": "Federal Justice Statistics Program: Offenders Released From Prison, 2016"
+                }
+            ],
+            "identifier": "2343",
+            "isPartOf": "2174",
+            "issued": "2019-12-16T12:16:38",
             "keyword": [
                 "correctional facilities",
                 "correctional system",
                 "inmate release plans",
                 "offenders"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2019-12-16T13:51:06",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2019-12-16T12:16:38",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR37410.v1",
-                    "title": "Federal Justice Statistics Program: Offenders Released From Prison, 2016"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 2016",
-            "description": "The data contain records of sentenced offenders in the custody of the Bureau of Prisons (BOP) at year-end of fiscal year 2016. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database as well as additional analysis variables. Variables containing identifying information (e.g., name, Social Security Number) were either removed, coarsened, or blanked in order to protect the identities of individuals. These data are part of a series designed by Abt and the Bureau of Justice Statistics. Data and documentation were prepared by Abt.",
-            "modified": "2019-12-16T10:15:59",
-            "accessLevel": "restricted public",
-            "identifier": "2344",
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
+            "title": "Federal Justice Statistics Program: Offenders Released From Prison, 2016"
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
+            "description": "The data contain records of sentenced offenders in the custody of the Bureau of Prisons (BOP) at year-end of fiscal year 2016. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database as well as additional analysis variables. Variables containing identifying information (e.g., name, Social Security Number) were either removed, coarsened, or blanked in order to protect the identities of individuals. These data are part of a series designed by Abt and the Bureau of Justice Statistics. Data and documentation were prepared by Abt.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR37412.v1",
+                    "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 2016"
+                }
+            ],
+            "identifier": "2344",
+            "isPartOf": "2174",
+            "issued": "2019-12-16T10:13:36",
             "keyword": [
                 "correctional facilities",
                 "correctional system",
                 "offenders",
                 "prison inmates"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2019-12-16T10:15:59",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2019-12-16T10:13:36",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR37412.v1",
-                    "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 2016"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 2016",
-            "description": "The data contain records of charges filed against defendants whose cases were filed by United States attorneys in United States district court during fiscal year 2016. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables. Variables containing identifying information (e.g., name, Social Security Number) were either removed, coarsened, or blanked in order to protect the identities of individuals. These data are part of a series designed by Abt and the Bureau of Justice Statistics. Data and documentation were prepared by Abt.",
-            "modified": "2019-12-18T14:12:14",
-            "accessLevel": "restricted public",
-            "identifier": "2345",
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
+            "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 2016"
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
+            "description": "The data contain records of charges filed against defendants whose cases were filed by United States attorneys in United States district court during fiscal year 2016. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables. Variables containing identifying information (e.g., name, Social Security Number) were either removed, coarsened, or blanked in order to protect the identities of individuals. These data are part of a series designed by Abt and the Bureau of Justice Statistics. Data and documentation were prepared by Abt.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR37413.v1",
+                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 2016"
+                }
+            ],
+            "identifier": "2345",
+            "isPartOf": "2174",
+            "issued": "2019-12-18T14:08:47",
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
+            "modified": "2019-12-18T14:12:14",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2019-12-18T14:08:47",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR37413.v1",
-                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 2016"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court - Terminated, 2016",
-            "description": "The data contain records of charges filed against defendants whose cases were terminated by United States attorneys in United States district court during fiscal year 2016. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables. Variables containing identifying information (e.g., name, Social Security Number) were either removed, coarsened, or blanked in order to protect the identities of individuals. These data are part of a series designed by Abt and the Bureau of Justice Statistics. Data and documentation were prepared by Abt.",
-            "modified": "2019-12-18T14:26:23",
-            "accessLevel": "restricted public",
-            "identifier": "2346",
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
+            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court, 2016"
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
+            "description": "The data contain records of charges filed against defendants whose cases were terminated by United States attorneys in United States district court during fiscal year 2016. The data are charge-level records, and more than one charge may be filed against a single defendant. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central Charge file. The charge-level data may be linked to defendant-level data (extracted from the EOUSA Central System file) through the CS_SEQ variable, and it should be noted that some defendants may not have any charges other than the lead charge appearing on the defendant-level record. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables. Variables containing identifying information (e.g., name, Social Security Number) were either removed, coarsened, or blanked in order to protect the identities of individuals. These data are part of a series designed by Abt and the Bureau of Justice Statistics. Data and documentation were prepared by Abt.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR37414.v1",
+                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court - Terminated, 2016"
+                }
+            ],
+            "identifier": "2346",
+            "isPartOf": "2174",
+            "issued": "2019-12-18T14:23:10",
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
+            "modified": "2019-12-18T14:26:23",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2019-12-18T14:23:10",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR37414.v1",
-                    "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court - Terminated, 2016"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Statutes for Counts of Convictions for Defendants Sentenced Under the Sentencing Reform Act, 2016",
-            "description": "These data contain records of statutes for each count of conviction for criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2016. The data are one of two supplementary files that should be used in conjunction with the primary analysis file, which contains records for all defendants sentenced under the guidelines. These data can be linked to the primary analysis file using the unique identifier variable USSCIDN. The number of records for a defendant in the current data corresponds to the total number of counts of conviction for that defendant, and that total is recorded in the NOCOUNT variable. As an example, if a defendant has five counts of conviction (NOCOUNT=5), he or she will have five records in the current data. As it is possible for defendants to have multiple statutes applying to a single count of conviction, up to three statutes (STA1-STA3) are recorded for each count of conviction. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. These data are part of a series designed by Abt and the Bureau of Justice Statistics. Data and documentation were prepared by Abt.",
-            "modified": "2019-12-17T11:25:24",
-            "accessLevel": "restricted public",
-            "identifier": "2347",
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
+            "title": "Federal Justice Statistics Program: Charges Filed Against Defendants in Criminal Cases in District Court - Terminated, 2016"
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
+            "description": "These data contain records of statutes for each count of conviction for criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2016. The data are one of two supplementary files that should be used in conjunction with the primary analysis file, which contains records for all defendants sentenced under the guidelines. These data can be linked to the primary analysis file using the unique identifier variable USSCIDN. The number of records for a defendant in the current data corresponds to the total number of counts of conviction for that defendant, and that total is recorded in the NOCOUNT variable. As an example, if a defendant has five counts of conviction (NOCOUNT=5), he or she will have five records in the current data. As it is possible for defendants to have multiple statutes applying to a single count of conviction, up to three statutes (STA1-STA3) are recorded for each count of conviction. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. These data are part of a series designed by Abt and the Bureau of Justice Statistics. Data and documentation were prepared by Abt.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR37417.v1",
+                    "title": "Federal Justice Statistics Program: Statutes for Counts of Convictions for Defendants Sentenced Under the Sentencing Reform Act, 2016"
+                }
+            ],
+            "identifier": "2347",
+            "isPartOf": "2174",
+            "issued": "2019-12-17T11:21:09",
             "keyword": [
                 "administration",
                 "court cases",
@@ -59572,55 +59566,55 @@
                 "sentencing guidelines",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2019-12-17T11:25:24",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2019-12-17T11:21:09",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR37417.v1",
-                    "title": "Federal Justice Statistics Program: Statutes for Counts of Convictions for Defendants Sentenced Under the Sentencing Reform Act, 2016"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 2016",
-            "description": "These data contain records of criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2016. It is estimated that over 90 percent of felony defendants in the federal criminal justice system are sentenced pursuant to the SRA of 1984. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. The Standardized Research Data File consists of variables from the Monitoring Department's database, which is limited to those defendants whose records have been furnished to the USSC by United States district courts and United States magistrates, as well as variables created by the OPA specifically for research purposes. The data include variables from the Judgement and Conviction (J and C) order submitted by the court, background and guideline information collected from the Presentencing Report (PSR), and the report on sentencing hearing in the Statement of Reasons (SOR). These data contain detailed information such as the guideline base offense level, offense level adjustments, criminal history, departure status, statement of reasons given for departure, and basic demographic information. These data are the primary analysis file and include only statute, guideline computation, and adjustment variables for the most serious offense of conviction. These data are part of a series designed by Abt and the Bureau of Justice Statistics. Data and documentation were prepared by Abt.",
-            "modified": "2019-12-17T14:43:12",
-            "accessLevel": "restricted public",
-            "identifier": "2348",
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
+            "title": "Federal Justice Statistics Program: Statutes for Counts of Convictions for Defendants Sentenced Under the Sentencing Reform Act, 2016"
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
+            "description": "These data contain records of criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2016. It is estimated that over 90 percent of felony defendants in the federal criminal justice system are sentenced pursuant to the SRA of 1984. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. The Standardized Research Data File consists of variables from the Monitoring Department's database, which is limited to those defendants whose records have been furnished to the USSC by United States district courts and United States magistrates, as well as variables created by the OPA specifically for research purposes. The data include variables from the Judgement and Conviction (J and C) order submitted by the court, background and guideline information collected from the Presentencing Report (PSR), and the report on sentencing hearing in the Statement of Reasons (SOR). These data contain detailed information such as the guideline base offense level, offense level adjustments, criminal history, departure status, statement of reasons given for departure, and basic demographic information. These data are the primary analysis file and include only statute, guideline computation, and adjustment variables for the most serious offense of conviction. These data are part of a series designed by Abt and the Bureau of Justice Statistics. Data and documentation were prepared by Abt.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR37418.v1",
+                    "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 2016"
+                }
+            ],
+            "identifier": "2348",
+            "isPartOf": "2174",
+            "issued": "2019-12-17T14:39:44",
             "keyword": [
                 "administration",
                 "court cases",
@@ -59632,55 +59626,55 @@
                 "sentencing guidelines",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2019-12-17T14:43:12",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2019-12-17T14:39:44",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR37418.v1",
-                    "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 2016"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 2016",
-            "description": "The data contain records of suspects in federal criminal matters received by United States attorneys or filed before the United States magistrates during fiscal year 2016. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables. Variables containing identifying information (e.g., name, Social Security Number) were either removed, coarsened, or blanked in order to protect the identities of individuals. These data are part of a series designed by Abt and the Bureau of Justice Statistics. Data and documentation were prepared by Abt.",
-            "modified": "2019-12-18T11:59:57",
-            "accessLevel": "restricted public",
-            "identifier": "2349",
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
+            "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 2016"
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
+            "description": "The data contain records of suspects in federal criminal matters received by United States attorneys or filed before the United States magistrates during fiscal year 2016. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables. Variables containing identifying information (e.g., name, Social Security Number) were either removed, coarsened, or blanked in order to protect the identities of individuals. These data are part of a series designed by Abt and the Bureau of Justice Statistics. Data and documentation were prepared by Abt.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR37424.v1",
+                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 2016"
+                }
+            ],
+            "identifier": "2349",
+            "isPartOf": "2174",
+            "issued": "2019-12-18T11:37:30",
             "keyword": [
                 "defendants",
                 "federal courts",
@@ -59688,165 +59682,165 @@
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2019-12-18T11:59:57",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2019-12-18T11:37:30",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR37424.v1",
-                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 2016"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 2016",
-            "description": "The data contain records of defendants in federal criminal cases filed in United States District Court during fiscal year 2016. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables. Variables containing identifying information (e.g., name, Social Security Number) were either removed, coarsened, or blanked in order to protect the identities of individuals. These data are part of a series designed by Abt and the Bureau of Justice Statistics. Data and documentation were prepared by Abt.",
-            "modified": "2019-12-18T11:07:34",
-            "accessLevel": "restricted public",
-            "identifier": "2350",
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
+            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 2016"
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
+            "description": "The data contain records of defendants in federal criminal cases filed in United States District Court during fiscal year 2016. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables. Variables containing identifying information (e.g., name, Social Security Number) were either removed, coarsened, or blanked in order to protect the identities of individuals. These data are part of a series designed by Abt and the Bureau of Justice Statistics. Data and documentation were prepared by Abt.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR37430.v1",
+                    "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 2016"
+                }
+            ],
+            "identifier": "2350",
+            "isPartOf": "2174",
+            "issued": "2019-12-18T11:04:35",
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
+            "modified": "2019-12-18T11:07:34",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2019-12-18T11:04:35",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR37430.v1",
-                    "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 2016"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases - Terminated, 2016",
-            "description": "The data contain records of defendants in federal criminal cases terminated in United States District Court during fiscal year 2016. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables. Variables containing identifying information (e.g., name, Social Security Number) were either removed, coarsened, or blanked in order to protect the identities of individuals. These data are part of a series designed by Abt and the Bureau of Justice Statistics. Data and documentation were prepared by Abt.",
-            "modified": "2019-12-18T12:22:51",
-            "accessLevel": "restricted public",
-            "identifier": "2351",
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
+            "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 2016"
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
+            "description": "The data contain records of defendants in federal criminal cases terminated in United States District Court during fiscal year 2016. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables. Variables containing identifying information (e.g., name, Social Security Number) were either removed, coarsened, or blanked in order to protect the identities of individuals. These data are part of a series designed by Abt and the Bureau of Justice Statistics. Data and documentation were prepared by Abt.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR37433.v1",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases - Terminated, 2016"
+                }
+            ],
+            "identifier": "2351",
+            "isPartOf": "2174",
+            "issued": "2019-12-18T12:20:17",
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
+            "modified": "2019-12-18T12:22:51",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2019-12-18T12:20:17",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR37433.v1",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases - Terminated, 2016"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2016",
-            "description": "The data contain records of suspects in federal criminal matters concluded by United States attorneys or United States magistrates during fiscal year 2016. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables. Variables containing identifying information (e.g., name, Social Security Number) were either removed, coarsened, or blanked in order to protect the identities of individuals. These data are part of a series designed by Abt and the Bureau of Justice Statistics. Data and documentation were prepared by Abt.",
-            "modified": "2019-12-18T11:24:29",
-            "accessLevel": "restricted public",
-            "identifier": "2352",
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases - Terminated, 2016"
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
+            "description": "The data contain records of suspects in federal criminal matters concluded by United States attorneys or United States magistrates during fiscal year 2016. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central Charge and Central System data contain variables from the original EOUSA files as well as additional analysis variables. Variables containing identifying information (e.g., name, Social Security Number) were either removed, coarsened, or blanked in order to protect the identities of individuals. These data are part of a series designed by Abt and the Bureau of Justice Statistics. Data and documentation were prepared by Abt.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR37440.v1",
+                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2016"
+                }
+            ],
+            "identifier": "2352",
+            "isPartOf": "2174",
+            "issued": "2019-12-18T11:21:32",
             "keyword": [
                 "defendants",
                 "federal courts",
@@ -59854,55 +59848,55 @@
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2019-12-18T11:24:29",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2019-12-18T11:21:32",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR37440.v1",
-                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2016"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Parole Survey, 2016",
-            "description": "The 2016 Annual Parole Survey provides a count of the total number of persons supervised in the community on January 1 and December 31, 2016, and a count of the number entering and leaving supervision during the year. The survey also provides counts of the number of parolees by certain characteristics, such as gender, race and Hispanic or Latino origin, supervision status, and type of offense. This survey covers all 50 states, the District of Columbia, and the Federal System.",
-            "modified": "2020-04-30T14:40:25",
-            "accessLevel": "public",
-            "identifier": "2353",
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
+            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2016"
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
+            "description": "The 2016 Annual Parole Survey provides a count of the total number of persons supervised in the community on January 1 and December 31, 2016, and a count of the number entering and leaving supervision during the year. The survey also provides counts of the number of parolees by certain characteristics, such as gender, race and Hispanic or Latino origin, supervision status, and type of offense. This survey covers all 50 states, the District of Columbia, and the Federal System.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR37441.v1",
+                    "title": "Annual Parole Survey, 2016"
+                }
+            ],
+            "identifier": "2353",
+            "isPartOf": "2631",
+            "issued": "2020-04-30T14:40:25",
             "keyword": [
                 "criminal justice system",
                 "offenses",
@@ -59910,54 +59904,54 @@
                 "parolees",
                 "sentencing"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2020-04-30T14:40:25",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2631",
-            "dataQuality": false,
-            "issued": "2020-04-30T14:40:25",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR37441.v1",
-                    "title": "Annual Parole Survey, 2016"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Probation Survey, 2016",
-            "description": "The 2016 Annual Probation Survey provides a count of the total number of persons supervised on probation on January 1 and December 31, 2016, and a count of the number of persons entering and exiting probation supervision during 2016. The survey also provides counts of the number of probationers by certain characteristics, such as gender, race, Hispanic or Latino origin, offense, and supervision status. The survey covers all 50 states, the District of Columbia, and the federal system.",
-            "modified": "2020-04-30T14:57:54",
-            "accessLevel": "public",
-            "identifier": "2354",
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
+            "title": "Annual Parole Survey, 2016"
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
+            "description": "The 2016 Annual Probation Survey provides a count of the total number of persons supervised on probation on January 1 and December 31, 2016, and a count of the number of persons entering and exiting probation supervision during 2016. The survey also provides counts of the number of probationers by certain characteristics, such as gender, race, Hispanic or Latino origin, offense, and supervision status. The survey covers all 50 states, the District of Columbia, and the federal system.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR37459.v1",
+                    "title": "Annual Probation Survey, 2016"
+                }
+            ],
+            "identifier": "2354",
+            "isPartOf": "2444",
+            "issued": "2020-04-30T14:57:54",
             "keyword": [
                 "criminal justice system",
                 "offenses",
@@ -59965,107 +59959,106 @@
                 "probationers",
                 "sentencing"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2020-04-30T14:57:54",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2444",
-            "dataQuality": false,
-            "issued": "2020-04-30T14:57:54",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR37459.v1",
-                    "title": "Annual Probation Survey, 2016"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Census of Victim Service Providers, [United States], 2017",
-            "description": "The purpose of the National Census of Victim Service Providers (NCVSP) is to describe the field of organizations or programs that are dedicated to serving victims of crime or abuse. The NCVSP collects characteristics about victim service providers (VSPs) over the past year, including the structure of the organization, the services the organization provided to victims, the availability of a hotline/helpline for victims, the types of crimes for which victims received services, the number of staff providing victim services, and current issues of concern to victim service providers. The information is intended for use by policymakers, practitioners at the Federal, state and local levels, academic researchers, and special interest groups to inform decisions related to victim services and the organizations that provide these services. The NCVSP also provides descriptive information about the full universe of organizations that provide crime victim services that can be used to develop representative samples for the National Survey of Victim Service Providers (NSVSP) and other VSP surveys.",
-            "modified": "2020-02-27T10:58:23",
-            "accessLevel": "public",
-            "identifier": "2355",
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
+            "title": "Annual Probation Survey, 2016"
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
+            "description": "The purpose of the National Census of Victim Service Providers (NCVSP) is to describe the field of organizations or programs that are dedicated to serving victims of crime or abuse. The NCVSP collects characteristics about victim service providers (VSPs) over the past year, including the structure of the organization, the services the organization provided to victims, the availability of a hotline/helpline for victims, the types of crimes for which victims received services, the number of staff providing victim services, and current issues of concern to victim service providers. The information is intended for use by policymakers, practitioners at the Federal, state and local levels, academic researchers, and special interest groups to inform decisions related to victim services and the organizations that provide these services. The NCVSP also provides descriptive information about the full universe of organizations that provide crime victim services that can be used to develop representative samples for the National Survey of Victim Service Providers (NSVSP) and other VSP surveys.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR37518.v1",
+                    "title": "National Census of Victim Service Providers, [United States], 2017"
+                }
+            ],
+            "identifier": "2355",
+            "issued": "2020-02-27T10:58:23",
             "keyword": [
                 "abuse",
                 "crime",
                 "victim services",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2020-02-27T10:58:23",
```

