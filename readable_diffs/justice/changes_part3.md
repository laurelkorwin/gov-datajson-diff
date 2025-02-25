# Change History for justice.json (Part 3)

### Changes from acf49f0 to dd2190f (Part 3/22)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
+            "description": "The data contain records of criminal appeals cases terminated in United States Courts of Appeals during fiscal year 1998. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. Appeals may be terminated on the merits or on procedural grounds. Of those that are terminated on the merits, the district court ruling may be affirmed, reversed, remanded to criminal court, or dismissed. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24042.v2",
+                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 1998 [United States]"
+                }
+            ],
+            "identifier": "847",
+            "isPartOf": "2174",
+            "issued": "2009-02-04T09:32:53",
             "keyword": [
                 "administration",
                 "appellate courts",
@@ -21339,55 +21333,55 @@
                 "judicial decisions",
                 "legal systems"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:17:02",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-04T09:32:53",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24042.v2",
-                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 1998 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 1999 [United States]",
-            "description": "The data contain records of criminal appeals cases terminated in United States Courts of Appeals during fiscal year 1999. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. Appeals may be terminated on the merits or on procedural grounds. Of those that are terminated on the merits, the district court ruling may be affirmed, reversed, remanded to criminal court, or dismissed. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:27:35",
-            "accessLevel": "restricted public",
-            "identifier": "848",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 1998 [United States]"
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
+            "description": "The data contain records of criminal appeals cases terminated in United States Courts of Appeals during fiscal year 1999. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. Appeals may be terminated on the merits or on procedural grounds. Of those that are terminated on the merits, the district court ruling may be affirmed, reversed, remanded to criminal court, or dismissed. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24061.v2",
+                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 1999 [United States]"
+                }
+            ],
+            "identifier": "848",
+            "isPartOf": "2174",
+            "issued": "2009-02-04T09:35:06",
             "keyword": [
                 "administration",
                 "appellate courts",
@@ -21398,55 +21392,55 @@
                 "judicial decisions",
                 "legal systems"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:27:35",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-04T09:35:06",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24061.v2",
-                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 1999 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 2000 [United States]",
-            "description": "The data contain records of criminal appeals cases terminated in United States Courts of Appeals during fiscal year 2000. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. Appeals may be terminated on the merits or on procedural grounds. Of those that are terminated on the merits, the district court ruling may be affirmed, reversed, remanded to criminal court, or dismissed. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:38:25",
-            "accessLevel": "restricted public",
-            "identifier": "849",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 1999 [United States]"
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
+            "description": "The data contain records of criminal appeals cases terminated in United States Courts of Appeals during fiscal year 2000. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. Appeals may be terminated on the merits or on procedural grounds. Of those that are terminated on the merits, the district court ruling may be affirmed, reversed, remanded to criminal court, or dismissed. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24080.v2",
+                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 2000 [United States]"
+                }
+            ],
+            "identifier": "849",
+            "isPartOf": "2174",
+            "issued": "2009-02-04T09:37:58",
             "keyword": [
                 "administration",
                 "appellate courts",
@@ -21457,55 +21451,55 @@
                 "judicial decisions",
                 "legal systems"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:38:25",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-04T09:37:58",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24080.v2",
-                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 2000 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 2001 [United States]",
-            "description": "The data contain records of criminal appeals cases terminated in United States Courts of Appeals during fiscal year 2001. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. Appeals may be terminated on the merits or on procedural grounds. Of those that are terminated on the merits, the district court ruling may be affirmed, reversed, remanded to criminal court, or dismissed. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:49:19",
-            "accessLevel": "restricted public",
-            "identifier": "850",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 2000 [United States]"
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
+            "description": "The data contain records of criminal appeals cases terminated in United States Courts of Appeals during fiscal year 2001. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. Appeals may be terminated on the merits or on procedural grounds. Of those that are terminated on the merits, the district court ruling may be affirmed, reversed, remanded to criminal court, or dismissed. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24099.v2",
+                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 2001 [United States]"
+                }
+            ],
+            "identifier": "850",
+            "isPartOf": "2174",
+            "issued": "2009-02-04T09:40:05",
             "keyword": [
                 "administration",
                 "appellate courts",
@@ -21516,55 +21510,55 @@
                 "judicial decisions",
                 "legal systems"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:49:19",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-04T09:40:05",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24099.v2",
-                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 2001 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 2002 [United States]",
-            "description": "The data contain records of criminal appeals cases terminated in United States Courts of Appeals during fiscal year 2002. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. Appeals may be terminated on the merits or on procedural grounds. Of those that are terminated on the merits, the district court ruling may be affirmed, reversed, remanded to criminal court, or dismissed. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:00:18",
-            "accessLevel": "restricted public",
-            "identifier": "851",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 2001 [United States]"
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
+            "description": "The data contain records of criminal appeals cases terminated in United States Courts of Appeals during fiscal year 2002. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. Appeals may be terminated on the merits or on procedural grounds. Of those that are terminated on the merits, the district court ruling may be affirmed, reversed, remanded to criminal court, or dismissed. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24118.v2",
+                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 2002 [United States]"
+                }
+            ],
+            "identifier": "851",
+            "isPartOf": "2174",
+            "issued": "2009-02-04T09:43:00",
             "keyword": [
                 "administration",
                 "appellate courts",
@@ -21575,55 +21569,55 @@
                 "judicial decisions",
                 "legal systems"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:00:18",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-04T09:43:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24118.v2",
-                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 2002 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 2003 [United States]",
-            "description": "The data contain records of criminal appeals cases terminated in United States Courts of Appeals during fiscal year 2003. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. Appeals may be terminated on the merits or on procedural grounds. Of those that are terminated on the merits, the district court ruling may be affirmed, reversed, remanded to criminal court, or dismissed. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:11:04",
-            "accessLevel": "restricted public",
-            "identifier": "852",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 2002 [United States]"
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
+            "description": "The data contain records of criminal appeals cases terminated in United States Courts of Appeals during fiscal year 2003. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. Appeals may be terminated on the merits or on procedural grounds. Of those that are terminated on the merits, the district court ruling may be affirmed, reversed, remanded to criminal court, or dismissed. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24137.v2",
+                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 2003 [United States]"
+                }
+            ],
+            "identifier": "852",
+            "isPartOf": "2174",
+            "issued": "2009-02-05T09:26:19",
             "keyword": [
                 "administration",
                 "appellate courts",
@@ -21634,55 +21628,55 @@
                 "judicial decisions",
                 "legal systems"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:11:04",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-05T09:26:19",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24137.v2",
-                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 2003 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 2004 [United States]",
-            "description": "The data contain records of criminal appeals cases terminated in United States Courts of Appeals during fiscal year 2004. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. Appeals may be terminated on the merits or on procedural grounds. Of those that are terminated on the merits, the district court ruling may be affirmed, reversed, remanded to criminal court, or dismissed. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:22:04",
-            "accessLevel": "restricted public",
-            "identifier": "853",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 2003 [United States]"
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
+            "description": "The data contain records of criminal appeals cases terminated in United States Courts of Appeals during fiscal year 2004. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. Appeals may be terminated on the merits or on procedural grounds. Of those that are terminated on the merits, the district court ruling may be affirmed, reversed, remanded to criminal court, or dismissed. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24156.v2",
+                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 2004 [United States]"
+                }
+            ],
+            "identifier": "853",
+            "isPartOf": "2174",
+            "issued": "2009-02-05T12:11:10",
             "keyword": [
                 "administration",
                 "appellate courts",
@@ -21693,55 +21687,55 @@
                 "judicial decisions",
                 "legal systems"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:22:04",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-05T12:11:10",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24156.v2",
-                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 2004 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 2005 [United States]",
-            "description": "The data contain records of criminal appeals cases terminated in United States Courts of Appeals during fiscal year 2005. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. Appeals may be terminated on the merits or on procedural grounds. Of those that are terminated on the merits, the district court ruling may be affirmed, reversed, remanded to criminal court, or dismissed. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:31:29",
-            "accessLevel": "restricted public",
-            "identifier": "854",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 2004 [United States]"
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
+            "description": "The data contain records of criminal appeals cases terminated in United States Courts of Appeals during fiscal year 2005. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. Appeals may be terminated on the merits or on procedural grounds. Of those that are terminated on the merits, the district court ruling may be affirmed, reversed, remanded to criminal court, or dismissed. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24173.v2",
+                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 2005 [United States]"
+                }
+            ],
+            "identifier": "854",
+            "isPartOf": "2174",
+            "issued": "2009-02-05T09:33:34",
             "keyword": [
                 "administration",
                 "appellate courts",
@@ -21752,55 +21746,55 @@
                 "judicial decisions",
                 "legal systems"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:31:29",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-05T09:33:34",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24173.v2",
-                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 2005 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 2006 [United States]",
-            "description": "The data contain records of criminal appeals cases terminated in United States Courts of Appeals during fiscal year 2006. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. Appeals may be terminated on the merits or on procedural grounds. Of those that are terminated on the merits, the district court ruling may be affirmed, reversed, remanded to criminal court, or dismissed. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:41:04",
-            "accessLevel": "restricted public",
-            "identifier": "855",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 2005 [United States]"
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
+            "description": "The data contain records of criminal appeals cases terminated in United States Courts of Appeals during fiscal year 2006. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. Appeals may be terminated on the merits or on procedural grounds. Of those that are terminated on the merits, the district court ruling may be affirmed, reversed, remanded to criminal court, or dismissed. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24191.v2",
+                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 2006 [United States]"
+                }
+            ],
+            "identifier": "855",
+            "isPartOf": "2174",
+            "issued": "2009-02-05T09:36:38",
             "keyword": [
                 "administration",
                 "appellate courts",
@@ -21811,55 +21805,55 @@
                 "judicial decisions",
                 "legal systems"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:41:04",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-05T09:36:38",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24191.v2",
-                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 2006 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 2007",
-            "description": "The data contain records of criminal appeals cases terminated in United States Courts of Appeals during fiscal year 2007. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. Appeals may be terminated on the merits or on procedural grounds. Of those that are terminated on the merits, the district court ruling may be affirmed, reversed, remanded to criminal court, or dismissed. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-07-29T16:01:44",
-            "accessLevel": "restricted public",
-            "identifier": "856",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 2006 [United States]"
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
+            "description": "The data contain records of criminal appeals cases terminated in United States Courts of Appeals during fiscal year 2007. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. Appeals may be terminated on the merits or on procedural grounds. Of those that are terminated on the merits, the district court ruling may be affirmed, reversed, remanded to criminal court, or dismissed. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24208.v1",
+                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 2007"
+                }
+            ],
+            "identifier": "856",
+            "isPartOf": "2174",
+            "issued": "2011-07-29T16:00:34",
             "keyword": [
                 "administration",
                 "appellate courts",
@@ -21870,55 +21864,55 @@
                 "judicial decisions",
                 "legal systems"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-07-29T16:01:44",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2011-07-29T16:00:34",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24208.v1",
-                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 2007"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 2008",
-            "description": "The data contain records of criminal appeals cases terminated in United States Courts of Appeals during fiscal year 2008. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. Appeals may be terminated on the merits or on procedural grounds. Of those that are terminated on the merits, the district court ruling may be affirmed, reversed, remanded to criminal court, or dismissed. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-07-29T16:11:26",
-            "accessLevel": "restricted public",
-            "identifier": "857",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 2007"
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
+            "description": "The data contain records of criminal appeals cases terminated in United States Courts of Appeals during fiscal year 2008. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. Appeals may be terminated on the merits or on procedural grounds. Of those that are terminated on the merits, the district court ruling may be affirmed, reversed, remanded to criminal court, or dismissed. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR26202.v1",
+                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 2008"
+                }
+            ],
+            "identifier": "857",
+            "isPartOf": "2174",
+            "issued": "2011-07-29T16:10:24",
             "keyword": [
                 "administration",
                 "appellate courts",
@@ -21929,55 +21923,55 @@
                 "judicial decisions",
                 "legal systems"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-07-29T16:11:26",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2011-07-29T16:10:24",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR26202.v1",
-                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 2008"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 2009 [United States]",
-            "description": "The data contain records of criminal appeals cases terminated in United States Courts of Appeals during fiscal year 2009. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. Appeals may be terminated on the merits or on procedural grounds. Of those that are terminated on the merits, the district court ruling may be affirmed, reversed, remanded to criminal court, or dismissed. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-06-06T09:59:53",
-            "accessLevel": "restricted public",
-            "identifier": "858",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 2008"
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
+            "description": "The data contain records of criminal appeals cases terminated in United States Courts of Appeals during fiscal year 2009. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. Appeals may be terminated on the merits or on procedural grounds. Of those that are terminated on the merits, the district court ruling may be affirmed, reversed, remanded to criminal court, or dismissed. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR31083.v1",
+                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 2009 [United States]"
+                }
+            ],
+            "identifier": "858",
+            "isPartOf": "2174",
+            "issued": "2011-06-06T09:59:04",
             "keyword": [
                 "administration",
                 "appellate courts",
@@ -21988,55 +21982,55 @@
                 "judicial decisions",
                 "legal systems"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-06-06T09:59:53",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2011-06-06T09:59:04",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR31083.v1",
-                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 2009 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 2010",
-            "description": "The data contain records of criminal appeals cases terminated in United States Courts of Appeals during fiscal year 2010. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. Appeals may be terminated on the merits or on procedural grounds. Of those that are terminated on the merits, the district court ruling may be affirmed, reversed, remanded to criminal court, or dismissed. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2013-01-07T09:22:37",
-            "accessLevel": "restricted public",
-            "identifier": "859",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 2009 [United States]"
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
+            "description": "The data contain records of criminal appeals cases terminated in United States Courts of Appeals during fiscal year 2010. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. Appeals may be terminated on the merits or on procedural grounds. Of those that are terminated on the merits, the district court ruling may be affirmed, reversed, remanded to criminal court, or dismissed. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR34323.v1",
+                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 2010"
+                }
+            ],
+            "identifier": "859",
+            "isPartOf": "2174",
+            "issued": "2013-01-07T09:07:39",
             "keyword": [
                 "administration",
                 "appellate courts",
@@ -22047,55 +22041,55 @@
                 "judicial decisions",
                 "legal systems"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-01-07T09:22:37",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2013-01-07T09:07:39",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR34323.v1",
-                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 2010"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals, 2008",
-            "description": "The data contain records of criminal appeals cases filed in United States Courts of Appeals during fiscal year 2008. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-07-29T16:06:17",
-            "accessLevel": "restricted public",
-            "identifier": "860",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals -- Terminated, 2010"
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
+            "description": "The data contain records of criminal appeals cases filed in United States Courts of Appeals during fiscal year 2008. The data were constructed from the Administrative Office of the United States Courts' (AOUSC) Court of Appeals file. These contain variables on the nature of the criminal appeal, the underlying offense, and the disposition of the appeal. An appeal can be filed by the government or the offender, and the appellant can appeal the sentence, the verdict, or both sentence and verdict. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 6.1-6.5. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR26201.v1",
+                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals, 2008"
+                }
+            ],
+            "identifier": "860",
+            "isPartOf": "2174",
+            "issued": "2011-07-29T16:05:13",
             "keyword": [
                 "administration",
                 "appellate courts",
@@ -22106,1925 +22100,1925 @@
                 "judicial decisions",
                 "legal systems"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-07-29T16:06:17",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2011-07-29T16:05:13",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR26201.v1",
-                    "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals, 2008"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 1995 [United States]",
-            "description": "The data contain records of defendants in federal criminal cases filed in United States District Court during fiscal year 1995. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T09:57:44",
-            "accessLevel": "restricted public",
-            "identifier": "861",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Criminal Appeals Cases in Courts of Appeals, 2008"
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
+            "description": "The data contain records of defendants in federal criminal cases filed in United States District Court during fiscal year 1995. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24007.v2",
+                    "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 1995 [United States]"
+                }
+            ],
+            "identifier": "861",
+            "isPartOf": "2174",
+            "issued": "2009-02-16T10:44:35",
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
+            "modified": "2011-03-08T09:57:44",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-16T10:44:35",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24007.v2",
-                    "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 1995 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 1996 [United States]",
-            "description": "The data contain records of defendants in federal criminal cases filed in United States District Court during fiscal year 1996. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:07:58",
-            "accessLevel": "restricted public",
-            "identifier": "862",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 1995 [United States]"
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
-                "defendants",
-                "district courts",
-                "offenses",
-                "prosecution"
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
-            "issued": "2009-02-16T10:47:18",
-            "language": [
-                "eng"
-            ],
+            "description": "The data contain records of defendants in federal criminal cases filed in United States District Court during fiscal year 1996. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://doi.org/10.3886/ICPSR24026.v2",
                     "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 1996 [United States]"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 1997 [United States]",
-            "description": "The data contain records of defendants in federal criminal cases filed in United States District Court during fiscal year 1997. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:18:42",
-            "accessLevel": "restricted public",
-            "identifier": "863",
+            ],
+            "identifier": "862",
+            "isPartOf": "2174",
+            "issued": "2009-02-16T10:47:18",
+            "keyword": [
+                "defendants",
+                "district courts",
+                "offenses",
+                "prosecution"
+            ],
+            "language": [
+                "eng"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:07:58",
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
+            "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 1996 [United States]"
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
+            "description": "The data contain records of defendants in federal criminal cases filed in United States District Court during fiscal year 1997. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24045.v2",
+                    "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 1997 [United States]"
+                }
+            ],
+            "identifier": "863",
+            "isPartOf": "2174",
+            "issued": "2009-02-16T10:49:22",
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
+            "modified": "2011-03-08T10:18:42",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-16T10:49:22",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24045.v2",
-                    "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 1997 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 1998 [United States]",
-            "description": "The data contain records of defendants in federal criminal cases filed in United States District Court during fiscal year 1998. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:29:18",
-            "accessLevel": "restricted public",
-            "identifier": "864",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 1997 [United States]"
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
+            "description": "The data contain records of defendants in federal criminal cases filed in United States District Court during fiscal year 1998. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24064.v2",
+                    "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 1998 [United States]"
+                }
+            ],
+            "identifier": "864",
+            "isPartOf": "2174",
+            "issued": "2009-02-16T10:51:45",
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
+            "modified": "2011-03-08T10:29:18",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-16T10:51:45",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24064.v2",
-                    "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 1998 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 1999 [United States]",
-            "description": "The data contain records of defendants in federal criminal cases filed in United States District Court during fiscal year 1999. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:40:07",
-            "accessLevel": "restricted public",
-            "identifier": "865",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 1998 [United States]"
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
+            "description": "The data contain records of defendants in federal criminal cases filed in United States District Court during fiscal year 1999. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24083.v2",
+                    "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 1999 [United States]"
+                }
+            ],
+            "identifier": "865",
+            "isPartOf": "2174",
+            "issued": "2009-02-16T10:53:46",
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
+            "modified": "2011-03-08T10:40:07",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-16T10:53:46",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24083.v2",
-                    "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 1999 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 2000 [United States]",
-            "description": "The data contain records of defendants in federal criminal cases filed in United States District Court during fiscal year 2000. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:51:03",
-            "accessLevel": "restricted public",
-            "identifier": "866",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 1999 [United States]"
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
+            "description": "The data contain records of defendants in federal criminal cases filed in United States District Court during fiscal year 2000. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24102.v2",
+                    "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 2000 [United States]"
+                }
+            ],
+            "identifier": "866",
+            "isPartOf": "2174",
+            "issued": "2009-02-16T10:55:49",
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
+            "modified": "2011-03-08T10:51:03",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-16T10:55:49",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24102.v2",
-                    "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 2000 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 2001 [United States]",
-            "description": "The data contain records of defendants in federal criminal cases filed in United States District Court during fiscal year 2001. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:01:59",
-            "accessLevel": "restricted public",
-            "identifier": "867",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 2000 [United States]"
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
+            "description": "The data contain records of defendants in federal criminal cases filed in United States District Court during fiscal year 2001. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24121.v2",
+                    "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 2001 [United States]"
+                }
+            ],
+            "identifier": "867",
+            "isPartOf": "2174",
+            "issued": "2009-02-16T10:57:51",
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
+            "modified": "2011-03-08T11:01:59",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-16T10:57:51",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24121.v2",
-                    "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 2001 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 2002 [United States]",
-            "description": "The data contain records of defendants in federal criminal cases filed in United States District Court during fiscal year 2002. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:12:44",
-            "accessLevel": "restricted public",
-            "identifier": "868",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 2001 [United States]"
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
+            "description": "The data contain records of defendants in federal criminal cases filed in United States District Court during fiscal year 2002. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24140.v2",
+                    "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 2002 [United States]"
+                }
+            ],
+            "identifier": "868",
+            "isPartOf": "2174",
+            "issued": "2009-02-16T11:00:12",
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
+            "modified": "2011-03-08T11:12:44",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-16T11:00:12",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24140.v2",
-                    "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 2002 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 2003 [United States]",
-            "description": "The data contain records of defendants in federal criminal cases filed in United States District Court during fiscal year 2003. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:23:45",
-            "accessLevel": "restricted public",
-            "identifier": "869",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 2002 [United States]"
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
+            "description": "The data contain records of defendants in federal criminal cases filed in United States District Court during fiscal year 2003. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24159.v2",
+                    "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 2003 [United States]"
+                }
+            ],
+            "identifier": "869",
+            "isPartOf": "2174",
+            "issued": "2009-02-16T11:02:24",
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
+            "modified": "2011-03-08T11:23:45",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-16T11:02:24",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24159.v2",
-                    "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 2003 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 2004 [United States]",
-            "description": "The data contain records of defendants in federal criminal cases filed in United States District Court during fiscal year 2004. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:33:09",
-            "accessLevel": "restricted public",
-            "identifier": "870",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 2003 [United States]"
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
+            "description": "The data contain records of defendants in federal criminal cases filed in United States District Court during fiscal year 2004. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24176.v2",
+                    "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 2004 [United States]"
+                }
+            ],
+            "identifier": "870",
+            "isPartOf": "2174",
+            "issued": "2009-02-16T11:04:25",
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
+            "modified": "2011-03-08T11:33:09",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-16T11:04:25",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24176.v2",
-                    "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 2004 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 2005 [United States]",
-            "description": "The data contain records of defendants in federal criminal cases filed in United States District Court during fiscal year 2005. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:42:44",
-            "accessLevel": "restricted public",
-            "identifier": "871",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 2004 [United States]"
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
+            "description": "The data contain records of defendants in federal criminal cases filed in United States District Court during fiscal year 2005. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24194.v2",
+                    "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 2005 [United States]"
+                }
+            ],
+            "identifier": "871",
+            "isPartOf": "2174",
+            "issued": "2009-02-16T11:06:30",
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
+            "modified": "2011-03-08T11:42:44",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-16T11:06:30",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24194.v2",
-                    "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 2005 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 2006 [United States]",
-            "description": "The data contain records of defendants in federal criminal cases filed in United States District Court during fiscal year 2006. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:51:10",
-            "accessLevel": "restricted public",
-            "identifier": "872",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 2005 [United States]"
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
+            "description": "The data contain records of defendants in federal criminal cases filed in United States District Court during fiscal year 2006. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24211.v2",
+                    "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 2006 [United States]"
+                }
+            ],
+            "identifier": "872",
+            "isPartOf": "2174",
+            "issued": "2009-02-16T11:08:37",
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
+            "modified": "2011-03-08T11:51:10",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-16T11:08:37",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24211.v2",
-                    "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 2006 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 2007 [United States]",
-            "description": "The data contain records of defendants in federal criminal cases filed in United States District Court during fiscal year 2007. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:59:58",
-            "accessLevel": "restricted public",
-            "identifier": "873",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 2006 [United States]"
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
+            "description": "The data contain records of defendants in federal criminal cases filed in United States District Court during fiscal year 2007. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24226.v2",
+                    "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 2007 [United States]"
+                }
+            ],
+            "identifier": "873",
+            "isPartOf": "2174",
+            "issued": "2009-02-19T10:36:53",
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
+            "modified": "2011-03-08T11:59:58",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-19T10:36:53",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24226.v2",
-                    "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 2007 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 2008 [United States]",
-            "description": "The data contain records of defendants in federal criminal cases filed in United States District Court during fiscal year 2008. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T12:13:31",
-            "accessLevel": "restricted public",
-            "identifier": "874",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 2007 [United States]"
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
+            "description": "The data contain records of defendants in federal criminal cases filed in United States District Court during fiscal year 2008. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR29426.v2",
+                    "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 2008 [United States]"
+                }
+            ],
+            "identifier": "874",
+            "isPartOf": "2174",
+            "issued": "2011-02-07T14:41:00",
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
+            "modified": "2011-03-08T12:13:31",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2011-02-07T14:41:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR29426.v2",
-                    "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 2008 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 2009",
-            "description": "The data contain records of defendants in federal criminal cases filed in United States District Court during fiscal year 2009. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-06-03T17:52:50",
-            "accessLevel": "restricted public",
-            "identifier": "875",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 2008 [United States]"
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
+            "description": "The data contain records of defendants in federal criminal cases filed in United States District Court during fiscal year 2009. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR30791.v1",
+                    "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 2009"
+                }
+            ],
+            "identifier": "875",
+            "isPartOf": "2174",
+            "issued": "2011-06-03T17:51:56",
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
+            "modified": "2011-06-03T17:52:50",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2011-06-03T17:51:56",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR30791.v1",
-                    "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 2009"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 2010",
-            "description": "The data contain records of defendants in federal criminal cases filed in United States District Court during fiscal year 2010. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2013-01-08T09:47:32",
-            "accessLevel": "restricted public",
-            "identifier": "876",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 2009"
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
+            "description": "The data contain records of defendants in federal criminal cases filed in United States District Court during fiscal year 2010. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR34333.v1",
+                    "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 2010"
+                }
+            ],
+            "identifier": "876",
+            "isPartOf": "2174",
+            "issued": "2013-01-08T09:41:06",
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
+            "modified": "2013-01-08T09:47:32",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2013-01-08T09:41:06",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR34333.v1",
-                    "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 2010"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Criminal Cases Filed in District Court, 1994 [United States]",
-            "description": "The data contain records of defendants in federal criminal cases filed in United States District Court during fiscal year 1994. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T09:45:54",
-            "accessLevel": "restricted public",
-            "identifier": "877",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants Charged in Criminal Cases Filed in District Court, 2010"
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
+            "description": "The data contain records of defendants in federal criminal cases filed in United States District Court during fiscal year 1994. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR23742.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Criminal Cases Filed in District Court, 1994 [United States]"
+                }
+            ],
+            "identifier": "877",
+            "isPartOf": "2174",
+            "issued": "2009-02-16T10:42:04",
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
+            "modified": "2011-03-08T09:45:54",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-16T10:42:04",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR23742.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Criminal Cases Filed in District Court, 1994 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 1994 [United States]",
-            "description": "The data contain records of defendants in federal criminal cases terminated in United States District Court during fiscal year 1994. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T09:46:30",
-            "accessLevel": "restricted public",
-            "identifier": "878",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Criminal Cases Filed in District Court, 1994 [United States]"
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
+            "description": "The data contain records of defendants in federal criminal cases terminated in United States District Court during fiscal year 1994. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR23743.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 1994 [United States]"
+                }
+            ],
+            "identifier": "878",
+            "isPartOf": "2174",
+            "issued": "2009-02-16T11:10:47",
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
+            "modified": "2011-03-08T09:46:30",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-16T11:10:47",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR23743.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 1994 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 1995 [United States]",
-            "description": "The data contain records of defendants in federal criminal cases terminated in United States District Court during fiscal year 1995. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T09:58:16",
-            "accessLevel": "restricted public",
-            "identifier": "879",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 1994 [United States]"
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
+            "description": "The data contain records of defendants in federal criminal cases terminated in United States District Court during fiscal year 1995. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24008.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 1995 [United States]"
+                }
+            ],
+            "identifier": "879",
+            "isPartOf": "2174",
+            "issued": "2009-02-16T11:12:57",
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
+            "modified": "2011-03-08T09:58:16",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-16T11:12:57",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24008.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 1995 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 1996 [United States]",
-            "description": "The data contain records of defendants in federal criminal cases terminated in United States District Court during fiscal year 1996. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:08:31",
-            "accessLevel": "restricted public",
-            "identifier": "880",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 1995 [United States]"
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
+            "description": "The data contain records of defendants in federal criminal cases terminated in United States District Court during fiscal year 1996. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24027.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 1996 [United States]"
+                }
+            ],
+            "identifier": "880",
+            "isPartOf": "2174",
+            "issued": "2009-02-16T11:15:01",
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
-            "issued": "2009-02-16T11:15:01",
             "language": [
                 "eng"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24027.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 1996 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 1997 [United States]",
-            "description": "The data contain records of defendants in federal criminal cases terminated in United States District Court during fiscal year 1997. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:19:15",
-            "accessLevel": "restricted public",
-            "identifier": "881",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:08:31",
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 1996 [United States]"
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
+            "description": "The data contain records of defendants in federal criminal cases terminated in United States District Court during fiscal year 1997. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24046.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 1997 [United States]"
+                }
+            ],
+            "identifier": "881",
+            "isPartOf": "2174",
+            "issued": "2009-02-16T11:17:04",
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
+            "modified": "2011-03-08T10:19:15",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-16T11:17:04",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24046.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 1997 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 1998 [United States]",
-            "description": "The data contain records of defendants in federal criminal cases terminated in United States District Court during fiscal year 1998. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:29:52",
-            "accessLevel": "restricted public",
-            "identifier": "882",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 1997 [United States]"
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
+            "description": "The data contain records of defendants in federal criminal cases terminated in United States District Court during fiscal year 1998. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24065.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 1998 [United States]"
+                }
+            ],
+            "identifier": "882",
+            "isPartOf": "2174",
+            "issued": "2009-02-16T11:19:06",
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
+            "modified": "2011-03-08T10:29:52",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-16T11:19:06",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24065.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 1998 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 1999 [United States]",
-            "description": "The data contain records of defendants in federal criminal cases terminated in United States District Court during fiscal year 1999. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:40:43",
-            "accessLevel": "restricted public",
-            "identifier": "883",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 1998 [United States]"
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
+            "description": "The data contain records of defendants in federal criminal cases terminated in United States District Court during fiscal year 1999. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24084.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 1999 [United States]"
+                }
+            ],
+            "identifier": "883",
+            "isPartOf": "2174",
+            "issued": "2009-02-16T11:21:17",
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
+            "modified": "2011-03-08T10:40:43",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-16T11:21:17",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24084.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 1999 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 2000 [United States]",
-            "description": "The data contain records of defendants in federal criminal cases terminated in United States District Court during fiscal year 2000. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:51:36",
-            "accessLevel": "restricted public",
-            "identifier": "884",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 1999 [United States]"
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
+            "description": "The data contain records of defendants in federal criminal cases terminated in United States District Court during fiscal year 2000. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24103.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 2000 [United States]"
+                }
+            ],
+            "identifier": "884",
+            "isPartOf": "2174",
+            "issued": "2009-02-16T11:23:22",
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
+            "modified": "2011-03-08T10:51:36",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-16T11:23:22",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24103.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 2000 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 2001 [United States]",
-            "description": "The data contain records of defendants in federal criminal cases terminated in United States District Court during fiscal year 2001. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:02:32",
-            "accessLevel": "restricted public",
-            "identifier": "885",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 2000 [United States]"
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
+            "description": "The data contain records of defendants in federal criminal cases terminated in United States District Court during fiscal year 2001. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24122.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 2001 [United States]"
+                }
+            ],
+            "identifier": "885",
+            "isPartOf": "2174",
+            "issued": "2009-02-16T11:25:29",
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
+            "modified": "2011-03-08T11:02:32",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-16T11:25:29",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24122.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 2001 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 2002 [United States]",
-            "description": "The data contain records of defendants in federal criminal cases terminated in United States District Court during fiscal year 2002. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:13:15",
-            "accessLevel": "restricted public",
-            "identifier": "886",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 2001 [United States]"
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
+            "description": "The data contain records of defendants in federal criminal cases terminated in United States District Court during fiscal year 2002. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24141.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 2002 [United States]"
+                }
+            ],
+            "identifier": "886",
+            "isPartOf": "2174",
+            "issued": "2009-02-16T11:27:32",
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
+            "modified": "2011-03-08T11:13:15",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-16T11:27:32",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24141.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 2002 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 2003 [United States]",
-            "description": "The data contain records of defendants in federal criminal cases terminated in United States District Court during fiscal year 2003. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T12:23:40",
-            "accessLevel": "restricted public",
-            "identifier": "887",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 2002 [United States]"
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
+            "description": "The data contain records of defendants in federal criminal cases terminated in United States District Court during fiscal year 2003. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24160.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 2003 [United States]"
+                }
+            ],
+            "identifier": "887",
+            "isPartOf": "2174",
+            "issued": "2009-02-16T11:29:34",
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
+            "modified": "2011-03-08T12:23:40",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-16T11:29:34",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24160.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 2003 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 2004 [United States]",
-            "description": "The data contain records of defendants in federal criminal cases terminated in United States District Court during fiscal year 2004. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:33:43",
-            "accessLevel": "restricted public",
-            "identifier": "888",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 2003 [United States]"
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
+            "description": "The data contain records of defendants in federal criminal cases terminated in United States District Court during fiscal year 2004. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24177.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 2004 [United States]"
+                }
+            ],
+            "identifier": "888",
+            "isPartOf": "2174",
+            "issued": "2009-02-16T11:31:37",
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
+            "modified": "2011-03-08T11:33:43",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-16T11:31:37",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24177.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 2004 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 2005 [United States]",
-            "description": "The data contain records of defendants in federal criminal cases terminated in United States District Court during fiscal year 2005. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:43:18",
-            "accessLevel": "restricted public",
-            "identifier": "889",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 2004 [United States]"
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
+            "description": "The data contain records of defendants in federal criminal cases terminated in United States District Court during fiscal year 2005. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24195.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 2005 [United States]"
+                }
+            ],
+            "identifier": "889",
+            "isPartOf": "2174",
+            "issued": "2009-02-16T11:33:45",
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
+            "modified": "2011-03-08T11:43:18",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-16T11:33:45",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24195.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 2005 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 2006 [United States]",
-            "description": "The data contain records of defendants in federal criminal cases terminated in United States District Court during fiscal year 2006. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:51:44",
-            "accessLevel": "restricted public",
-            "identifier": "890",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 2005 [United States]"
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
+            "description": "The data contain records of defendants in federal criminal cases terminated in United States District Court during fiscal year 2006. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24212.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 2006 [United States]"
+                }
+            ],
+            "identifier": "890",
+            "isPartOf": "2174",
+            "issued": "2009-02-16T11:35:49",
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
+            "modified": "2011-03-08T11:51:44",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-16T11:35:49",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24212.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 2006 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 2007 [United States]",
-            "description": "The data contain records of defendants in federal criminal cases terminated in United States District Court during fiscal year 2007. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T12:00:33",
-            "accessLevel": "restricted public",
-            "identifier": "891",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 2006 [United States]"
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
+            "description": "The data contain records of defendants in federal criminal cases terminated in United States District Court during fiscal year 2007. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24227.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 2007 [United States]"
+                }
+            ],
+            "identifier": "891",
+            "isPartOf": "2174",
+            "issued": "2009-02-19T15:04:32",
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
+            "modified": "2011-03-08T12:00:33",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-19T15:04:32",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24227.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 2007 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 2008 [United States]",
-            "description": "The data contain records of defendants in federal criminal cases terminated in United States District Court during fiscal year 2008. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T12:16:10",
-            "accessLevel": "restricted public",
-            "identifier": "892",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 2007 [United States]"
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
+            "description": "The data contain records of defendants in federal criminal cases terminated in United States District Court during fiscal year 2008. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR29433.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 2008 [United States]"
+                }
+            ],
+            "identifier": "892",
+            "isPartOf": "2174",
+            "issued": "2011-02-07T15:36:43",
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
+            "modified": "2011-03-08T12:16:10",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2011-02-07T15:36:43",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR29433.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 2008 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 2009",
-            "description": "The data contain records of defendants in federal criminal cases terminated in United States District Court during fiscal year 2009. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-06-03T17:57:21",
-            "accessLevel": "restricted public",
-            "identifier": "893",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 2008 [United States]"
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
+            "description": "The data contain records of defendants in federal criminal cases terminated in United States District Court during fiscal year 2009. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR30792.v1",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 2009"
+                }
+            ],
+            "identifier": "893",
+            "isPartOf": "2174",
+            "issued": "2011-06-03T17:56:30",
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
+            "modified": "2011-06-03T17:57:21",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2011-06-03T17:56:30",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR30792.v1",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 2009"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 2010",
-            "description": "The data contain records of defendants in federal criminal cases terminated in United States District Court during fiscal year 2010. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2013-01-08T10:29:48",
-            "accessLevel": "restricted public",
-            "identifier": "894",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 2009"
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
+            "description": "The data contain records of defendants in federal criminal cases terminated in United States District Court during fiscal year 2010. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR34334.v1",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 2010"
+                }
+            ],
+            "identifier": "894",
+            "isPartOf": "2174",
+            "issued": "2013-01-08T09:53:58",
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
+            "modified": "2013-01-08T10:29:48",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2013-01-08T09:53:58",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR34334.v1",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 2010"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 1994 [United States]",
-            "description": "The data contain records of defendants in criminal cases filed in United States District Court during fiscal year 1994. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF variables,\" that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T09:43:11",
-            "accessLevel": "restricted public",
-            "identifier": "895",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases -- Terminated, 2010"
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
+            "description": "The data contain records of defendants in criminal cases filed in United States District Court during fiscal year 1994. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF variables,\" that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR23660.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 1994 [United States]"
+                }
+            ],
+            "identifier": "895",
+            "isPartOf": "2174",
+            "issued": "2009-01-29T10:00:54",
             "keyword": [
                 "administration",
                 "court cases",
@@ -24035,55 +24029,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T09:43:11",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-01-29T10:00:54",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR23660.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 1994 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 1995 [United States]",
-            "description": "The data contain records of defendants in criminal cases filed in United States District Court during fiscal year 1995. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF variables,\" that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T09:53:49",
-            "accessLevel": "restricted public",
-            "identifier": "896",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 1994 [United States]"
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
+            "description": "The data contain records of defendants in criminal cases filed in United States District Court during fiscal year 1995. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF variables,\" that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24000.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 1995 [United States]"
+                }
+            ],
+            "identifier": "896",
+            "isPartOf": "2174",
+            "issued": "2009-01-29T10:05:05",
             "keyword": [
                 "administration",
                 "court cases",
@@ -24094,55 +24088,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T09:53:49",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-01-29T10:05:05",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24000.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 1995 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 1996 [United States]",
-            "description": "The data contain records of defendants in criminal cases filed in United States District Court during fiscal year 1996. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF variables,\" that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:04:15",
-            "accessLevel": "restricted public",
-            "identifier": "897",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 1995 [United States]"
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
+            "description": "The data contain records of defendants in criminal cases filed in United States District Court during fiscal year 1996. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF variables,\" that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24019.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 1996 [United States]"
+                }
+            ],
+            "identifier": "897",
+            "isPartOf": "2174",
+            "issued": "2009-01-29T10:09:46",
             "keyword": [
                 "administration",
                 "court cases",
@@ -24153,55 +24147,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:04:15",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-01-29T10:09:46",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24019.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 1996 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 1997 [United States]",
-            "description": "The data contain records of defendants in criminal cases filed in United States District Court during fiscal year 1997. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF variables,\" that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:14:45",
-            "accessLevel": "restricted public",
-            "identifier": "898",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 1996 [United States]"
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
+            "description": "The data contain records of defendants in criminal cases filed in United States District Court during fiscal year 1997. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF variables,\" that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24038.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 1997 [United States]"
+                }
+            ],
+            "identifier": "898",
+            "isPartOf": "2174",
+            "issued": "2009-01-29T10:15:18",
             "keyword": [
                 "administration",
                 "court cases",
@@ -24212,55 +24206,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:14:45",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-01-29T10:15:18",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24038.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 1997 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 1998 [United States]",
-            "description": "The data contain records of defendants in criminal cases filed in United States District Court during fiscal year 1998. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF variables,\" that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:25:16",
-            "accessLevel": "restricted public",
-            "identifier": "899",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 1997 [United States]"
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
+            "description": "The data contain records of defendants in criminal cases filed in United States District Court during fiscal year 1998. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF variables,\" that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24057.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 1998 [United States]"
+                }
+            ],
+            "identifier": "899",
+            "isPartOf": "2174",
+            "issued": "2009-01-29T10:19:00",
             "keyword": [
                 "administration",
                 "court cases",
@@ -24271,55 +24265,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:25:16",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-01-29T10:19:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24057.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 1998 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 1999 [United States]",
-            "description": "The data contain records of defendants in criminal cases filed in United States District Court during fiscal year 1999. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF variables,\" that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:36:08",
-            "accessLevel": "restricted public",
-            "identifier": "900",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 1998 [United States]"
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
+            "description": "The data contain records of defendants in criminal cases filed in United States District Court during fiscal year 1999. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF variables,\" that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24076.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 1999 [United States]"
+                }
+            ],
+            "identifier": "900",
+            "isPartOf": "2174",
+            "issued": "2009-01-29T10:23:18",
             "keyword": [
                 "administration",
                 "court cases",
@@ -24330,55 +24324,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:36:08",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-01-29T10:23:18",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24076.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 1999 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2000 [United States]",
-            "description": "The data contain records of defendants in criminal cases filed in United States District Court during fiscal year 2000. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF variables,\" that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:47:04",
-            "accessLevel": "restricted public",
-            "identifier": "901",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 1999 [United States]"
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
+            "description": "The data contain records of defendants in criminal cases filed in United States District Court during fiscal year 2000. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF variables,\" that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24095.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2000 [United States]"
+                }
+            ],
+            "identifier": "901",
+            "isPartOf": "2174",
+            "issued": "2009-01-29T10:26:22",
             "keyword": [
                 "administration",
                 "court cases",
@@ -24389,55 +24383,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:47:04",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-01-29T10:26:22",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24095.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2000 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2001 [United States]",
-            "description": "The data contain records of defendants in criminal cases filed in United States District Court during fiscal year 2001. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF variables,\" that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:57:56",
-            "accessLevel": "restricted public",
-            "identifier": "902",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2000 [United States]"
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
+            "description": "The data contain records of defendants in criminal cases filed in United States District Court during fiscal year 2001. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF variables,\" that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24114.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2001 [United States]"
+                }
+            ],
+            "identifier": "902",
+            "isPartOf": "2174",
+            "issued": "2009-01-29T10:29:42",
             "keyword": [
                 "administration",
                 "court cases",
@@ -24448,55 +24442,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:57:56",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-01-29T10:29:42",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24114.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2001 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2002 [United States]",
-            "description": "The data contain records of defendants in criminal cases filed in United States District Court during fiscal year 2002. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF variables,\" that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:08:49",
-            "accessLevel": "restricted public",
-            "identifier": "903",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2001 [United States]"
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
+            "description": "The data contain records of defendants in criminal cases filed in United States District Court during fiscal year 2002. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF variables,\" that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24133.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2002 [United States]"
+                }
+            ],
+            "identifier": "903",
+            "isPartOf": "2174",
+            "issued": "2009-01-29T10:33:29",
             "keyword": [
                 "administration",
                 "court cases",
@@ -24507,55 +24501,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:08:49",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-01-29T10:33:29",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24133.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2002 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2003 [United States]",
-            "description": "The data contain records of defendants in criminal cases filed in United States District Court during fiscal year 2003. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF variables,\" that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:19:48",
-            "accessLevel": "restricted public",
-            "identifier": "904",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2002 [United States]"
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
+            "description": "The data contain records of defendants in criminal cases filed in United States District Court during fiscal year 2003. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF variables,\" that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24152.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2003 [United States]"
+                }
+            ],
+            "identifier": "904",
+            "isPartOf": "2174",
+            "issued": "2009-01-29T10:36:56",
             "keyword": [
                 "administration",
                 "court cases",
@@ -24566,55 +24560,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:19:48",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-01-29T10:36:56",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24152.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2003 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2004 [United States]",
-            "description": "The data contain records of defendants in criminal cases filed in United States District Court during fiscal year 2004. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF variables,\" that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:29:11",
-            "accessLevel": "restricted public",
-            "identifier": "905",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2003 [United States]"
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
+            "description": "The data contain records of defendants in criminal cases filed in United States District Court during fiscal year 2004. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF variables,\" that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24169.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2004 [United States]"
+                }
+            ],
+            "identifier": "905",
+            "isPartOf": "2174",
+            "issued": "2009-01-29T10:41:08",
             "keyword": [
                 "administration",
                 "court cases",
@@ -24625,55 +24619,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:29:11",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-01-29T10:41:08",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24169.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2004 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2005 [United States]",
-            "description": "The data contain records of defendants in criminal cases filed in United States District Court during fiscal year 2005. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF variables,\" that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:38:48",
-            "accessLevel": "restricted public",
-            "identifier": "906",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2004 [United States]"
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
+            "description": "The data contain records of defendants in criminal cases filed in United States District Court during fiscal year 2005. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF variables,\" that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24186.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2005 [United States]"
+                }
+            ],
+            "identifier": "906",
+            "isPartOf": "2174",
+            "issued": "2009-01-29T10:44:19",
             "keyword": [
                 "administration",
                 "court cases",
@@ -24684,55 +24678,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:38:48",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-01-29T10:44:19",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24186.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2005 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2006 [United States]",
-            "description": "The data contain records of defendants in criminal cases filed in United States District Court during fiscal year 2006. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF variables,\" that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:48:21",
-            "accessLevel": "restricted public",
-            "identifier": "907",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2005 [United States]"
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
+            "description": "The data contain records of defendants in criminal cases filed in United States District Court during fiscal year 2006. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF variables,\" that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24204.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2006 [United States]"
+                }
+            ],
+            "identifier": "907",
+            "isPartOf": "2174",
+            "issued": "2009-01-29T10:48:43",
             "keyword": [
                 "administration",
                 "court cases",
@@ -24743,55 +24737,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:48:21",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-01-29T10:48:43",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24204.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2006 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2007 [United States]",
-            "description": "The data contain records of defendants in criminal cases filed in United States District Court during fiscal year 2007. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF variables,\" that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:57:02",
-            "accessLevel": "restricted public",
-            "identifier": "908",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2006 [United States]"
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
+            "description": "The data contain records of defendants in criminal cases filed in United States District Court during fiscal year 2007. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF variables,\" that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24221.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2007 [United States]"
+                }
+            ],
+            "identifier": "908",
+            "isPartOf": "2174",
+            "issued": "2009-02-23T14:22:28",
             "keyword": [
                 "administration",
                 "court cases",
@@ -24802,55 +24796,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:57:02",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-23T14:22:28",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24221.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2007 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2008 [United States]",
-            "description": "The data contain records of defendants in criminal cases filed in United States District Court during fiscal year 2008. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF variables,\" that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T12:09:33",
-            "accessLevel": "restricted public",
-            "identifier": "909",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2007 [United States]"
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
+            "description": "The data contain records of defendants in criminal cases filed in United States District Court during fiscal year 2008. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF variables,\" that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR29402.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2008 [United States]"
+                }
+            ],
+            "identifier": "909",
+            "isPartOf": "2174",
+            "issued": "2011-02-03T12:51:37",
             "keyword": [
                 "administration",
                 "court cases",
@@ -24861,55 +24855,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T12:09:33",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2011-02-03T12:51:37",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR29402.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2008 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2009",
-            "description": "The data contain records of defendants in criminal cases filed in United States District Court during fiscal year 2009. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-06-03T15:28:13",
-            "accessLevel": "restricted public",
-            "identifier": "910",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2008 [United States]"
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
+            "description": "The data contain records of defendants in criminal cases filed in United States District Court during fiscal year 2009. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR30781.v1",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2009"
+                }
+            ],
+            "identifier": "910",
+            "isPartOf": "2174",
+            "issued": "2011-06-03T15:27:08",
             "keyword": [
                 "administration",
                 "court cases",
@@ -24921,55 +24915,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-06-03T15:28:13",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2011-06-03T15:27:08",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR30781.v1",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2009"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2010",
-            "description": "The data contain records of defendants in criminal cases filed in United States District Court during fiscal year 2010. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2013-01-07T08:28:40",
-            "accessLevel": "restricted public",
-            "identifier": "911",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2009"
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
+            "description": "The data contain records of defendants in criminal cases filed in United States District Court during fiscal year 2010. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR34324.v1",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2010"
+                }
+            ],
+            "identifier": "911",
+            "isPartOf": "2174",
+            "issued": "2013-01-07T08:22:11",
             "keyword": [
                 "administration",
                 "court cases",
@@ -24981,55 +24975,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-01-07T08:28:40",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2013-01-07T08:22:11",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR34324.v1",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2010"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 1994 [United States]",
-            "description": "The data contain records of defendants in criminal cases filed in United States District Court before or during fiscal year 1994 and still pending as of year-end. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T09:48:46",
-            "accessLevel": "restricted public",
-            "identifier": "912",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases Filed in District Court, 2010"
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
+            "description": "The data contain records of defendants in criminal cases filed in United States District Court before or during fiscal year 1994 and still pending as of year-end. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR23761.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 1994 [United States]"
+                }
+            ],
+            "identifier": "912",
+            "isPartOf": "2174",
+            "issued": "2009-01-30T11:13:33",
             "keyword": [
                 "administration",
                 "court cases",
@@ -25040,55 +25034,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T09:48:46",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-01-30T11:13:33",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR23761.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 1994 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 1995 [United States]",
-            "description": "The data contain records of defendants in criminal cases filed in United States District Court before or during fiscal year 1995 and still pending as of year-end. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T09:54:56",
-            "accessLevel": "restricted public",
-            "identifier": "913",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 1994 [United States]"
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
+            "description": "The data contain records of defendants in criminal cases filed in United States District Court before or during fiscal year 1995 and still pending as of year-end. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24002.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 1995 [United States]"
+                }
+            ],
+            "identifier": "913",
+            "isPartOf": "2174",
+            "issued": "2009-01-29T15:03:47",
             "keyword": [
                 "administration",
                 "court cases",
@@ -25099,55 +25093,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T09:54:56",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-01-29T15:03:47",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24002.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 1995 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 1996 [United States]",
-            "description": "The data contain records of defendants in criminal cases filed in United States District Court before or during fiscal year 1996 and still pending as of year-end. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:05:19",
-            "accessLevel": "restricted public",
-            "identifier": "914",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 1995 [United States]"
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
+            "description": "The data contain records of defendants in criminal cases filed in United States District Court before or during fiscal year 1996 and still pending as of year-end. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24021.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 1996 [United States]"
+                }
+            ],
+            "identifier": "914",
+            "isPartOf": "2174",
+            "issued": "2009-01-29T15:07:06",
             "keyword": [
                 "administration",
                 "court cases",
@@ -25158,55 +25152,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:05:19",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-01-29T15:07:06",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24021.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 1996 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 1997 [United States]",
-            "description": "The data contain records of defendants in criminal cases filed in United States District Court before or during fiscal year 1997 and still pending as of year-end. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:15:54",
-            "accessLevel": "restricted public",
-            "identifier": "915",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 1996 [United States]"
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
+            "description": "The data contain records of defendants in criminal cases filed in United States District Court before or during fiscal year 1997 and still pending as of year-end. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24040.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 1997 [United States]"
+                }
+            ],
+            "identifier": "915",
+            "isPartOf": "2174",
+            "issued": "2009-01-29T15:09:49",
             "keyword": [
                 "administration",
                 "court cases",
@@ -25217,55 +25211,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:15:54",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-01-29T15:09:49",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24040.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 1997 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 1998 [United States]",
-            "description": "The data contain records of defendants in criminal cases filed in United States District Court before or during fiscal year 1998 and still pending as of year-end. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:26:24",
-            "accessLevel": "restricted public",
-            "identifier": "916",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 1997 [United States]"
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
+            "description": "The data contain records of defendants in criminal cases filed in United States District Court before or during fiscal year 1998 and still pending as of year-end. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24059.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 1998 [United States]"
+                }
+            ],
+            "identifier": "916",
+            "isPartOf": "2174",
+            "issued": "2009-01-29T15:13:22",
             "keyword": [
                 "administration",
                 "court cases",
@@ -25276,55 +25270,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:26:24",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-01-29T15:13:22",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24059.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 1998 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 1999 [United States]",
-            "description": "The data contain records of defendants in criminal cases filed in United States District Court before or during fiscal year 1999 and still pending as of year-end. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:37:17",
-            "accessLevel": "restricted public",
-            "identifier": "917",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 1998 [United States]"
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
+            "description": "The data contain records of defendants in criminal cases filed in United States District Court before or during fiscal year 1999 and still pending as of year-end. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24078.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 1999 [United States]"
+                }
+            ],
+            "identifier": "917",
+            "isPartOf": "2174",
+            "issued": "2009-01-29T15:16:40",
             "keyword": [
                 "administration",
                 "court cases",
@@ -25335,55 +25329,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:37:17",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-01-29T15:16:40",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24078.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 1999 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 2000 [United States]",
-            "description": "The data contain records of defendants in criminal cases filed in United States District Court before or during fiscal year 2000 and still pending as of year-end. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:48:12",
-            "accessLevel": "restricted public",
-            "identifier": "918",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 1999 [United States]"
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
+            "description": "The data contain records of defendants in criminal cases filed in United States District Court before or during fiscal year 2000 and still pending as of year-end. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24097.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 2000 [United States]"
+                }
+            ],
+            "identifier": "918",
+            "isPartOf": "2174",
+            "issued": "2009-01-29T15:20:56",
             "keyword": [
                 "administration",
                 "court cases",
@@ -25394,55 +25388,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:48:12",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-01-29T15:20:56",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24097.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 2000 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 2001 [United States]",
-            "description": "The data contain records of defendants in criminal cases filed in United States District Court before or during fiscal year 2001 and still pending as of year-end. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:59:04",
-            "accessLevel": "restricted public",
-            "identifier": "919",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 2000 [United States]"
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
+            "description": "The data contain records of defendants in criminal cases filed in United States District Court before or during fiscal year 2001 and still pending as of year-end. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24116.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 2001 [United States]"
+                }
+            ],
+            "identifier": "919",
+            "isPartOf": "2174",
+            "issued": "2009-01-29T15:24:33",
             "keyword": [
                 "administration",
                 "court cases",
@@ -25453,55 +25447,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:59:04",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-01-29T15:24:33",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24116.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 2001 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 2002 [United States]",
-            "description": "The data contain records of defendants in criminal cases filed in United States District Court before or during fiscal year 2002 and still pending as of year-end. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:09:57",
-            "accessLevel": "restricted public",
-            "identifier": "920",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 2001 [United States]"
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
+            "description": "The data contain records of defendants in criminal cases filed in United States District Court before or during fiscal year 2002 and still pending as of year-end. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24135.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 2002 [United States]"
+                }
+            ],
+            "identifier": "920",
+            "isPartOf": "2174",
+            "issued": "2009-01-29T15:32:15",
             "keyword": [
                 "administration",
                 "court cases",
@@ -25512,55 +25506,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:09:57",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-01-29T15:32:15",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24135.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 2002 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 2003 [United States]",
-            "description": "The data contain records of defendants in criminal cases filed in United States District Court before or during fiscal year 2003 and still pending as of year-end. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:20:56",
-            "accessLevel": "restricted public",
-            "identifier": "921",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 2002 [United States]"
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
+            "description": "The data contain records of defendants in criminal cases filed in United States District Court before or during fiscal year 2003 and still pending as of year-end. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24154.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 2003 [United States]"
+                }
+            ],
+            "identifier": "921",
+            "isPartOf": "2174",
+            "issued": "2009-01-29T15:36:40",
             "keyword": [
                 "administration",
                 "court cases",
@@ -25571,55 +25565,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:20:56",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-01-29T15:36:40",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24154.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 2003 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 2004 [United States]",
-            "description": "The data contain records of defendants in criminal cases filed in United States District Court before or during fiscal year 2004 and still pending as of year-end. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:30:20",
-            "accessLevel": "restricted public",
-            "identifier": "922",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 2003 [United States]"
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
+            "description": "The data contain records of defendants in criminal cases filed in United States District Court before or during fiscal year 2004 and still pending as of year-end. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24171.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 2004 [United States]"
+                }
+            ],
+            "identifier": "922",
+            "isPartOf": "2174",
+            "issued": "2009-01-30T10:25:57",
             "keyword": [
                 "administration",
                 "court cases",
@@ -25630,55 +25624,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:30:20",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-01-30T10:25:57",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24171.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 2004 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 2005 [United States]",
-            "description": "The data contain records of defendants in criminal cases filed in United States District Court before or during fiscal year 2005 and still pending as of year-end. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:39:57",
-            "accessLevel": "restricted public",
-            "identifier": "923",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 2004 [United States]"
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
+            "description": "The data contain records of defendants in criminal cases filed in United States District Court before or during fiscal year 2005 and still pending as of year-end. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24188.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 2005 [United States]"
+                }
+            ],
+            "identifier": "923",
+            "isPartOf": "2174",
+            "issued": "2009-01-30T10:31:34",
             "keyword": [
                 "administration",
                 "court cases",
@@ -25689,55 +25683,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:39:57",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-01-30T10:31:34",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24188.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 2005 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 2006 [United States]",
-            "description": "The data contain records of defendants in criminal cases filed in United States District Court before or during fiscal year 2006 and still pending as of year-end. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:49:29",
-            "accessLevel": "restricted public",
-            "identifier": "924",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 2005 [United States]"
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
+            "description": "The data contain records of defendants in criminal cases filed in United States District Court before or during fiscal year 2006 and still pending as of year-end. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24206.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 2006 [United States]"
+                }
+            ],
+            "identifier": "924",
+            "isPartOf": "2174",
+            "issued": "2009-01-29T15:41:52",
             "keyword": [
                 "administration",
                 "court cases",
@@ -25748,55 +25742,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:49:29",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-01-29T15:41:52",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24206.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 2006 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 2007 [United States]",
-            "description": "The data contain records of defendants in criminal cases filed in United States District Court before or during fiscal year 2007 and still pending as of year-end. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:58:13",
-            "accessLevel": "restricted public",
-            "identifier": "925",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 2006 [United States]"
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
+            "description": "The data contain records of defendants in criminal cases filed in United States District Court before or during fiscal year 2007 and still pending as of year-end. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24223.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 2007 [United States]"
+                }
+            ],
+            "identifier": "925",
+            "isPartOf": "2174",
+            "issued": "2009-02-23T14:28:34",
             "keyword": [
                 "administration",
                 "court cases",
@@ -25807,55 +25801,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:58:13",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-23T14:28:34",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24223.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 2007 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 2008 [United States]",
-            "description": "The data contain records of defendants in criminal cases filed in United States District Court before or during fiscal year 2008 and still pending as of year-end. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T12:10:07",
-            "accessLevel": "restricted public",
-            "identifier": "926",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 2007 [United States]"
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
+            "description": "The data contain records of defendants in criminal cases filed in United States District Court before or during fiscal year 2008 and still pending as of year-end. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR29403.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 2008 [United States]"
+                }
+            ],
+            "identifier": "926",
+            "isPartOf": "2174",
+            "issued": "2011-02-03T13:15:55",
             "keyword": [
                 "administration",
                 "court cases",
@@ -25866,55 +25860,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T12:10:07",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2011-02-03T13:15:55",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR29403.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 2008 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 2009",
-            "description": "The data contain records of defendants in criminal cases filed in United States District Court before or during fiscal year 2009 and still pending as of year-end. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-06-03T15:35:58",
-            "accessLevel": "restricted public",
-            "identifier": "927",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 2008 [United States]"
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
+            "description": "The data contain records of defendants in criminal cases filed in United States District Court before or during fiscal year 2009 and still pending as of year-end. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR30782.v1",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 2009"
+                }
+            ],
+            "identifier": "927",
+            "isPartOf": "2174",
+            "issued": "2011-06-03T15:34:53",
             "keyword": [
                 "administration",
                 "court cases",
@@ -25926,55 +25920,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-06-03T15:35:58",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2011-06-03T15:34:53",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR30782.v1",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 2009"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 2010",
-            "description": "The data contain records of defendants in criminal cases filed in United States District Court before or during fiscal year 2010 and still pending as of year-end. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2013-01-07T08:50:53",
-            "accessLevel": "restricted public",
-            "identifier": "928",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 2009"
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
+            "description": "The data contain records of defendants in criminal cases filed in United States District Court before or during fiscal year 2010 and still pending as of year-end. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR34325.v1",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 2010"
+                }
+            ],
+            "identifier": "928",
+            "isPartOf": "2174",
+            "issued": "2013-01-07T08:46:41",
             "keyword": [
                 "administration",
                 "court cases",
@@ -25986,55 +25980,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-01-07T08:50:53",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2013-01-07T08:46:41",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR34325.v1",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 2010"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 1994 [United States]",
-            "description": "The data contain records of defendants in criminal cases terminated in United States District Court during fiscal year 1994. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T09:48:11",
-            "accessLevel": "restricted public",
-            "identifier": "929",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Pending, 2010"
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
+            "description": "The data contain records of defendants in criminal cases terminated in United States District Court during fiscal year 1994. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR23760.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 1994 [United States]"
+                }
+            ],
+            "identifier": "929",
+            "isPartOf": "2174",
+            "issued": "2009-01-29T13:27:59",
             "keyword": [
                 "administration",
                 "court cases",
@@ -26045,55 +26039,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T09:48:11",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-01-29T13:27:59",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR23760.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 1994 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 1995 [United States]",
-            "description": "The data contain records of defendants in criminal cases terminated in United States District Court during fiscal year 1995. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T09:54:22",
-            "accessLevel": "restricted public",
-            "identifier": "930",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 1994 [United States]"
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
+            "description": "The data contain records of defendants in criminal cases terminated in United States District Court during fiscal year 1995. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24001.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 1995 [United States]"
+                }
+            ],
+            "identifier": "930",
+            "isPartOf": "2174",
+            "issued": "2009-01-29T13:31:51",
             "keyword": [
                 "administration",
                 "court cases",
@@ -26104,55 +26098,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T09:54:22",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-01-29T13:31:51",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24001.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 1995 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 1996 [United States]",
-            "description": "The data contain records of defendants in criminal cases terminated in United States District Court during fiscal year 1996. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:04:47",
-            "accessLevel": "restricted public",
-            "identifier": "931",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 1995 [United States]"
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
+            "description": "The data contain records of defendants in criminal cases terminated in United States District Court during fiscal year 1996. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24020.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 1996 [United States]"
+                }
+            ],
+            "identifier": "931",
+            "isPartOf": "2174",
+            "issued": "2009-01-29T13:36:02",
             "keyword": [
                 "administration",
                 "court cases",
@@ -26163,55 +26157,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:04:47",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-01-29T13:36:02",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24020.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 1996 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 1997 [United States]",
-            "description": "The data contain records of defendants in criminal cases terminated in United States District Court during fiscal year 1997. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:15:19",
-            "accessLevel": "restricted public",
-            "identifier": "932",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 1996 [United States]"
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
+            "description": "The data contain records of defendants in criminal cases terminated in United States District Court during fiscal year 1997. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24039.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 1997 [United States]"
+                }
+            ],
+            "identifier": "932",
+            "isPartOf": "2174",
+            "issued": "2009-01-29T13:39:17",
             "keyword": [
                 "administration",
                 "court cases",
@@ -26222,55 +26216,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:15:19",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-01-29T13:39:17",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24039.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 1997 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 1998 [United States]",
-            "description": "The data contain records of defendants in criminal cases terminated in United States District Court during fiscal year 1998. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:25:51",
-            "accessLevel": "restricted public",
-            "identifier": "933",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 1997 [United States]"
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
+            "description": "The data contain records of defendants in criminal cases terminated in United States District Court during fiscal year 1998. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24058.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 1998 [United States]"
+                }
+            ],
+            "identifier": "933",
+            "isPartOf": "2174",
+            "issued": "2009-01-29T13:43:47",
             "keyword": [
                 "administration",
                 "court cases",
@@ -26281,55 +26275,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:25:51",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-01-29T13:43:47",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24058.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 1998 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 1999 [United States]",
-            "description": "The data contain records of defendants in criminal cases terminated in United States District Court during fiscal year 1999. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:36:44",
-            "accessLevel": "restricted public",
-            "identifier": "934",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 1998 [United States]"
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
+            "description": "The data contain records of defendants in criminal cases terminated in United States District Court during fiscal year 1999. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24077.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 1999 [United States]"
+                }
+            ],
+            "identifier": "934",
+            "isPartOf": "2174",
+            "issued": "2009-01-29T13:47:25",
             "keyword": [
                 "administration",
                 "court cases",
@@ -26340,114 +26334,114 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:36:44",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-01-29T13:47:25",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24077.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 1999 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 2000 [United States]",
-            "description": "The data contain records of defendants in criminal cases terminated in United States District Court during fiscal year 2000. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:47:38",
-            "accessLevel": "restricted public",
-            "identifier": "935",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 1999 [United States]"
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
-                "administration",
-                "court cases",
-                "criminal law",
-                "defendants",
+            "dataQuality": false,
+            "description": "The data contain records of defendants in criminal cases terminated in United States District Court during fiscal year 2000. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24096.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 2000 [United States]"
+                }
+            ],
+            "identifier": "935",
+            "isPartOf": "2174",
+            "issued": "2009-01-29T13:50:42",
+            "keyword": [
+                "administration",
+                "court cases",
+                "criminal law",
+                "defendants",
                 "federal courts",
                 "judicial decisions",
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:47:38",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-01-29T13:50:42",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24096.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 2000 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 2001 [United States]",
-            "description": "The data contain records of defendants in criminal cases terminated in United States District Court during fiscal year 2001. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:58:30",
-            "accessLevel": "restricted public",
-            "identifier": "936",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 2000 [United States]"
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
+            "description": "The data contain records of defendants in criminal cases terminated in United States District Court during fiscal year 2001. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24115.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 2001 [United States]"
+                }
+            ],
+            "identifier": "936",
+            "isPartOf": "2174",
+            "issued": "2009-01-29T13:54:03",
             "keyword": [
                 "administration",
                 "court cases",
@@ -26458,55 +26452,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:58:30",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-01-29T13:54:03",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24115.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 2001 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 2002 [United States]",
-            "description": "The data contain records of defendants in criminal cases terminated in United States District Court during fiscal year 2002. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:09:23",
-            "accessLevel": "restricted public",
-            "identifier": "937",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 2001 [United States]"
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
+            "description": "The data contain records of defendants in criminal cases terminated in United States District Court during fiscal year 2002. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24134.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 2002 [United States]"
+                }
+            ],
+            "identifier": "937",
+            "isPartOf": "2174",
+            "issued": "2009-01-29T13:57:31",
             "keyword": [
                 "administration",
                 "court cases",
@@ -26517,55 +26511,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:09:23",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-01-29T13:57:31",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24134.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 2002 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 2003 [United States]",
-            "description": "The data contain records of defendants in criminal cases terminated in United States District Court during fiscal year 2003. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:20:22",
-            "accessLevel": "restricted public",
-            "identifier": "938",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 2002 [United States]"
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
+            "description": "The data contain records of defendants in criminal cases terminated in United States District Court during fiscal year 2003. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24153.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 2003 [United States]"
+                }
+            ],
+            "identifier": "938",
+            "isPartOf": "2174",
+            "issued": "2009-01-29T14:01:15",
             "keyword": [
                 "administration",
                 "court cases",
@@ -26576,55 +26570,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:20:22",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-01-29T14:01:15",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24153.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 2003 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 2004 [United States]",
-            "description": "The data contain records of defendants in criminal cases terminated in United States District Court during fiscal year 2004. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:29:45",
-            "accessLevel": "restricted public",
-            "identifier": "939",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 2003 [United States]"
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
+            "description": "The data contain records of defendants in criminal cases terminated in United States District Court during fiscal year 2004. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24170.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 2004 [United States]"
+                }
+            ],
+            "identifier": "939",
+            "isPartOf": "2174",
+            "issued": "2009-01-29T14:08:27",
             "keyword": [
                 "administration",
                 "court cases",
@@ -26635,55 +26629,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:29:45",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-01-29T14:08:27",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24170.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 2004 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 2005 [United States]",
-            "description": "The data contain records of defendants in criminal cases terminated in United States District Court during fiscal year 2005. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:39:22",
-            "accessLevel": "restricted public",
-            "identifier": "940",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 2004 [United States]"
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
+            "description": "The data contain records of defendants in criminal cases terminated in United States District Court during fiscal year 2005. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24187.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 2005 [United States]"
+                }
+            ],
+            "identifier": "940",
+            "isPartOf": "2174",
+            "issued": "2009-01-29T14:14:24",
             "keyword": [
                 "administration",
                 "court cases",
@@ -26694,55 +26688,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:39:22",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-01-29T14:14:24",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24187.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 2005 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 2006 [United States]",
-            "description": "The data contain records of defendants in criminal cases terminated in United States District Court during fiscal year 2006. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:48:55",
-            "accessLevel": "restricted public",
-            "identifier": "941",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 2005 [United States]"
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
+            "description": "The data contain records of defendants in criminal cases terminated in United States District Court during fiscal year 2006. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24205.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 2006 [United States]"
+                }
+            ],
+            "identifier": "941",
+            "isPartOf": "2174",
+            "issued": "2009-01-29T14:19:47",
             "keyword": [
                 "administration",
                 "court cases",
@@ -26753,55 +26747,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:48:55",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-01-29T14:19:47",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24205.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 2006 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 2007 [United States]",
-            "description": "The data contain records of defendants in criminal cases terminated in United States District Court during fiscal year 2007. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:57:38",
-            "accessLevel": "restricted public",
-            "identifier": "942",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 2006 [United States]"
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
+            "description": "The data contain records of defendants in criminal cases terminated in United States District Court during fiscal year 2007. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24222.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 2007 [United States]"
+                }
+            ],
+            "identifier": "942",
+            "isPartOf": "2174",
+            "issued": "2009-02-23T14:25:10",
             "keyword": [
                 "administration",
                 "court cases",
@@ -26812,55 +26806,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:57:38",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-23T14:25:10",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24222.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 2007 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 2008 [United States]",
-            "description": "The data contain records of defendants in criminal cases terminated in United States District Court during fiscal year 2008. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF variables,\" that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T12:08:24",
-            "accessLevel": "restricted public",
-            "identifier": "943",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 2007 [United States]"
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
+            "description": "The data contain records of defendants in criminal cases terminated in United States District Court during fiscal year 2008. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF variables,\" that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR29242.v2",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 2008 [United States]"
+                }
+            ],
+            "identifier": "943",
+            "isPartOf": "2174",
+            "issued": "2011-02-03T15:20:04",
             "keyword": [
                 "administration",
                 "court cases",
@@ -26871,55 +26865,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T12:08:24",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2011-02-03T15:20:04",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR29242.v2",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 2008 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 2009",
-            "description": "The data contain records of defendants in criminal cases terminated in United States District Court during fiscal year 2009. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-06-06T09:53:47",
-            "accessLevel": "restricted public",
-            "identifier": "944",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 2008 [United States]"
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
+            "description": "The data contain records of defendants in criminal cases terminated in United States District Court during fiscal year 2009. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR30784.v1",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 2009"
+                }
+            ],
+            "identifier": "944",
+            "isPartOf": "2174",
+            "issued": "2011-06-06T09:52:34",
             "keyword": [
                 "administration",
                 "court cases",
@@ -26931,55 +26925,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-06-06T09:53:47",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2011-06-06T09:52:34",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR30784.v1",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 2009"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 2010",
-            "description": "The data contain records of defendants in criminal cases terminated in United States District Court during fiscal year 2010. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2013-01-07T09:33:06",
-            "accessLevel": "restricted public",
-            "identifier": "945",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 2009"
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
+            "description": "The data contain records of defendants in criminal cases terminated in United States District Court during fiscal year 2010. The data were constructed from the Administrative Office of the United States District Courts' (AOUSC) criminal file. Defendants in criminal cases may be either individuals or corporations. There is one record for each defendant in each case filed. Included in the records are data from court proceedings and offense codes for up to five offenses charged at the time the case was filed. (The most serious charge at termination may differ from the most serious charge at case filing, due to plea bargaining or action of the judge or jury.) In a case with multiple charges against the defendant, a \"most serious\" offense charge is determined by a hierarchy of offenses based on statutory maximum penalties associated with the charges. The data file contains variables from the original AOUSC files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 4.1-4.5 and 5.1-5.6. Variables containing identifying information (e.g., name, Social Security number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR34326.v1",
+                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 2010"
+                }
+            ],
+            "identifier": "945",
+            "isPartOf": "2174",
+            "issued": "2013-01-07T09:29:10",
             "keyword": [
                 "administration",
                 "court cases",
@@ -26991,55 +26985,55 @@
                 "legal systems",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-01-07T09:33:06",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2013-01-07T09:29:10",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR34326.v1",
-                    "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 2010"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 1994 [United States]",
-            "description": "These data contain records of criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 1994. It is estimated that over 90 percent of felony defendants in the federal criminal justice system are sentenced pursuant to the SRA of 1984. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. The Standardized Research Data File consists of variables from the Monitoring Department's database, which is limited to those defendants whose records have been furnished to the USSC by United States district courts and United States magistrates, as well as variables created by the OPA specifically for research purposes. The data include variables from the Judgement and Conviction (J and C) order submitted by the court, background and guideline information collected from the Presentencing Report (PSR), and the report on sentencing hearing in the Statement of Reasons (SOR). These data contain detailed information such as the guideline base offense level, offense level adjustments, criminal history, departure status, statement of reasons given for departure, and basic demographic information. These data are the primary analysis file and include only statute, guideline computation, and adjustment variables for the most serious offense of conviction. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T09:49:19",
-            "accessLevel": "restricted public",
-            "identifier": "946",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants in Federal Criminal Cases in District Court -- Terminated, 2010"
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
+            "description": "These data contain records of criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 1994. It is estimated that over 90 percent of felony defendants in the federal criminal justice system are sentenced pursuant to the SRA of 1984. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. The Standardized Research Data File consists of variables from the Monitoring Department's database, which is limited to those defendants whose records have been furnished to the USSC by United States district courts and United States magistrates, as well as variables created by the OPA specifically for research purposes. The data include variables from the Judgement and Conviction (J and C) order submitted by the court, background and guideline information collected from the Presentencing Report (PSR), and the report on sentencing hearing in the Statement of Reasons (SOR). These data contain detailed information such as the guideline base offense level, offense level adjustments, criminal history, departure status, statement of reasons given for departure, and basic demographic information. These data are the primary analysis file and include only statute, guideline computation, and adjustment variables for the most serious offense of conviction. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR23762.v2",
+                    "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 1994 [United States]"
+                }
+            ],
+            "identifier": "946",
+            "isPartOf": "2174",
+            "issued": "2009-02-11T10:52:45",
             "keyword": [
                 "administration",
                 "court cases",
@@ -27051,55 +27045,55 @@
                 "sentencing guidelines",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T09:49:19",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-11T10:52:45",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR23762.v2",
-                    "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 1994 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 1995 [United States]",
-            "description": "These data contain records of criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 1995. It is estimated that over 90 percent of felony defendants in the federal criminal justice system are sentenced pursuant to the SRA of 1984. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. The Standardized Research Data File consists of variables from the Monitoring Department's database, which is limited to those defendants whose records have been furnished to the USSC by United States district courts and United States magistrates, as well as variables created by the OPA specifically for research purposes. The data include variables from the Judgement and Conviction (J and C) order submitted by the court, background and guideline information collected from the Presentencing Report (PSR), and the report on sentencing hearing in the Statement of Reasons (SOR). These data contain detailed information such as the guideline base offense level, offense level adjustments, criminal history, departure status, statement of reasons given for departure, and basic demographic information. These data are the primary analysis file and include only statute, guideline computation, and adjustment variables for the most serious offense of conviction. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:01:02",
-            "accessLevel": "restricted public",
-            "identifier": "947",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 1994 [United States]"
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
+            "description": "These data contain records of criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 1995. It is estimated that over 90 percent of felony defendants in the federal criminal justice system are sentenced pursuant to the SRA of 1984. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. The Standardized Research Data File consists of variables from the Monitoring Department's database, which is limited to those defendants whose records have been furnished to the USSC by United States district courts and United States magistrates, as well as variables created by the OPA specifically for research purposes. The data include variables from the Judgement and Conviction (J and C) order submitted by the court, background and guideline information collected from the Presentencing Report (PSR), and the report on sentencing hearing in the Statement of Reasons (SOR). These data contain detailed information such as the guideline base offense level, offense level adjustments, criminal history, departure status, statement of reasons given for departure, and basic demographic information. These data are the primary analysis file and include only statute, guideline computation, and adjustment variables for the most serious offense of conviction. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24013.v2",
+                    "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 1995 [United States]"
+                }
+            ],
+            "identifier": "947",
+            "isPartOf": "2174",
+            "issued": "2009-02-11T10:55:46",
             "keyword": [
                 "administration",
                 "court cases",
@@ -27111,55 +27105,55 @@
                 "sentencing guidelines",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:01:02",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-11T10:55:46",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24013.v2",
-                    "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 1995 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 1996 [United States]",
-            "description": "These data contain records of criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 1996. It is estimated that over 90 percent of felony defendants in the federal criminal justice system are sentenced pursuant to the SRA of 1984. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. The Standardized Research Data File consists of variables from the Monitoring Department's database, which is limited to those defendants whose records have been furnished to the USSC by United States district courts and United States magistrates, as well as variables created by the OPA specifically for research purposes. The data include variables from the Judgement and Conviction (J and C) order submitted by the court, background and guideline information collected from the Presentencing Report (PSR), and the report on sentencing hearing in the Statement of Reasons (SOR). These data contain detailed information such as the guideline base offense level, offense level adjustments, criminal history, departure status, statement of reasons given for departure, and basic demographic information. These data are the primary analysis file and include only statute, guideline computation, and adjustment variables for the most serious offense of conviction. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:11:14",
-            "accessLevel": "restricted public",
-            "identifier": "948",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 1995 [United States]"
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
+            "description": "These data contain records of criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 1996. It is estimated that over 90 percent of felony defendants in the federal criminal justice system are sentenced pursuant to the SRA of 1984. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. The Standardized Research Data File consists of variables from the Monitoring Department's database, which is limited to those defendants whose records have been furnished to the USSC by United States district courts and United States magistrates, as well as variables created by the OPA specifically for research purposes. The data include variables from the Judgement and Conviction (J and C) order submitted by the court, background and guideline information collected from the Presentencing Report (PSR), and the report on sentencing hearing in the Statement of Reasons (SOR). These data contain detailed information such as the guideline base offense level, offense level adjustments, criminal history, departure status, statement of reasons given for departure, and basic demographic information. These data are the primary analysis file and include only statute, guideline computation, and adjustment variables for the most serious offense of conviction. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24032.v2",
+                    "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 1996 [United States]"
+                }
+            ],
+            "identifier": "948",
+            "isPartOf": "2174",
+            "issued": "2009-02-11T10:59:53",
             "keyword": [
                 "administration",
                 "court cases",
@@ -27171,55 +27165,55 @@
                 "sentencing guidelines",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:11:14",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-11T10:59:53",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24032.v2",
-                    "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 1996 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 1997 [United States]",
-            "description": "These data contain records of criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 1997. It is estimated that over 90 percent of felony defendants in the federal criminal justice system are sentenced pursuant to the SRA of 1984. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. The Standardized Research Data File consists of variables from the Monitoring Department's database, which is limited to those defendants whose records have been furnished to the USSC by United States district courts and United States magistrates, as well as variables created by the OPA specifically for research purposes. The data include variables from the Judgement and Conviction (J and C) order submitted by the court, background and guideline information collected from the Presentencing Report (PSR), and the report on sentencing hearing in the Statement of Reasons (SOR). These data contain detailed information such as the guideline base offense level, offense level adjustments, criminal history, departure status, statement of reasons given for departure, and basic demographic information. These data are the primary analysis file and include only statute, guideline computation, and adjustment variables for the most serious offense of conviction. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:22:04",
-            "accessLevel": "restricted public",
-            "identifier": "949",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 1996 [United States]"
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
+            "description": "These data contain records of criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 1997. It is estimated that over 90 percent of felony defendants in the federal criminal justice system are sentenced pursuant to the SRA of 1984. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. The Standardized Research Data File consists of variables from the Monitoring Department's database, which is limited to those defendants whose records have been furnished to the USSC by United States district courts and United States magistrates, as well as variables created by the OPA specifically for research purposes. The data include variables from the Judgement and Conviction (J and C) order submitted by the court, background and guideline information collected from the Presentencing Report (PSR), and the report on sentencing hearing in the Statement of Reasons (SOR). These data contain detailed information such as the guideline base offense level, offense level adjustments, criminal history, departure status, statement of reasons given for departure, and basic demographic information. These data are the primary analysis file and include only statute, guideline computation, and adjustment variables for the most serious offense of conviction. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24051.v2",
+                    "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 1997 [United States]"
+                }
+            ],
+            "identifier": "949",
+            "isPartOf": "2174",
+            "issued": "2009-02-11T11:02:59",
             "keyword": [
                 "administration",
                 "court cases",
@@ -27231,55 +27225,55 @@
                 "sentencing guidelines",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:22:04",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-11T11:02:59",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24051.v2",
-                    "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 1997 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 1998 [United States]",
-            "description": "These data contain records of criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 1998. It is estimated that over 90 percent of felony defendants in the federal criminal justice system are sentenced pursuant to the SRA of 1984. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. The Standardized Research Data File consists of variables from the Monitoring Department's database, which is limited to those defendants whose records have been furnished to the USSC by United States district courts and United States magistrates, as well as variables created by the OPA specifically for research purposes. The data include variables from the Judgement and Conviction (J and C) order submitted by the court, background and guideline information collected from the Presentencing Report (PSR), and the report on sentencing hearing in the Statement of Reasons (SOR). These data contain detailed information such as the guideline base offense level, offense level adjustments, criminal history, departure status, statement of reasons given for departure, and basic demographic information. These data are the primary analysis file and include only statute, guideline computation, and adjustment variables for the most serious offense of conviction. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:32:45",
-            "accessLevel": "restricted public",
-            "identifier": "950",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 1997 [United States]"
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
+            "description": "These data contain records of criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 1998. It is estimated that over 90 percent of felony defendants in the federal criminal justice system are sentenced pursuant to the SRA of 1984. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. The Standardized Research Data File consists of variables from the Monitoring Department's database, which is limited to those defendants whose records have been furnished to the USSC by United States district courts and United States magistrates, as well as variables created by the OPA specifically for research purposes. The data include variables from the Judgement and Conviction (J and C) order submitted by the court, background and guideline information collected from the Presentencing Report (PSR), and the report on sentencing hearing in the Statement of Reasons (SOR). These data contain detailed information such as the guideline base offense level, offense level adjustments, criminal history, departure status, statement of reasons given for departure, and basic demographic information. These data are the primary analysis file and include only statute, guideline computation, and adjustment variables for the most serious offense of conviction. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24070.v2",
+                    "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 1998 [United States]"
+                }
+            ],
+            "identifier": "950",
+            "isPartOf": "2174",
+            "issued": "2009-02-11T11:06:47",
             "keyword": [
                 "administration",
                 "court cases",
@@ -27291,55 +27285,55 @@
                 "sentencing guidelines",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:32:45",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-11T11:06:47",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24070.v2",
-                    "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 1998 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 1999 [United States]",
-            "description": "These data contain records of criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 1999. It is estimated that over 90 percent of felony defendants in the federal criminal justice system are sentenced pursuant to the SRA of 1984. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. The Standardized Research Data File consists of variables from the Monitoring Department's database, which is limited to those defendants whose records have been furnished to the USSC by United States district courts and United States magistrates, as well as variables created by the OPA specifically for research purposes. The data include variables from the Judgement and Conviction (J and C) order submitted by the court, background and guideline information collected from the Presentencing Report (PSR), and the report on sentencing hearing in the Statement of Reasons (SOR). These data contain detailed information such as the guideline base offense level, offense level adjustments, criminal history, departure status, statement of reasons given for departure, and basic demographic information. These data are the primary analysis file and include only statute, guideline computation, and adjustment variables for the most serious offense of conviction. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:43:41",
-            "accessLevel": "restricted public",
-            "identifier": "951",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 1998 [United States]"
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
+            "description": "These data contain records of criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 1999. It is estimated that over 90 percent of felony defendants in the federal criminal justice system are sentenced pursuant to the SRA of 1984. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. The Standardized Research Data File consists of variables from the Monitoring Department's database, which is limited to those defendants whose records have been furnished to the USSC by United States district courts and United States magistrates, as well as variables created by the OPA specifically for research purposes. The data include variables from the Judgement and Conviction (J and C) order submitted by the court, background and guideline information collected from the Presentencing Report (PSR), and the report on sentencing hearing in the Statement of Reasons (SOR). These data contain detailed information such as the guideline base offense level, offense level adjustments, criminal history, departure status, statement of reasons given for departure, and basic demographic information. These data are the primary analysis file and include only statute, guideline computation, and adjustment variables for the most serious offense of conviction. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24089.v2",
+                    "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 1999 [United States]"
+                }
+            ],
+            "identifier": "951",
+            "isPartOf": "2174",
+            "issued": "2009-02-11T11:09:58",
             "keyword": [
                 "administration",
                 "court cases",
@@ -27351,55 +27345,55 @@
                 "sentencing guidelines",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:43:41",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-11T11:09:58",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24089.v2",
-                    "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 1999 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 2000 [United States]",
-            "description": "These data contain records of criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2000. It is estimated that over 90 percent of felony defendants in the federal criminal justice system are sentenced pursuant to the SRA of 1984. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. The Standardized Research Data File consists of variables from the Monitoring Department's database, which is limited to those defendants whose records have been furnished to the USSC by United States district courts and United States magistrates, as well as variables created by the OPA specifically for research purposes. The data include variables from the Judgement and Conviction (J and C) order submitted by the court, background and guideline information collected from the Presentencing Report (PSR), and the report on sentencing hearing in the Statement of Reasons (SOR). These data contain detailed information such as the guideline base offense level, offense level adjustments, criminal history, departure status, statement of reasons given for departure, and basic demographic information. These data are the primary analysis file and include only statute, guideline computation, and adjustment variables for the most serious offense of conviction. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:54:29",
-            "accessLevel": "restricted public",
-            "identifier": "952",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 1999 [United States]"
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
+            "description": "These data contain records of criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2000. It is estimated that over 90 percent of felony defendants in the federal criminal justice system are sentenced pursuant to the SRA of 1984. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. The Standardized Research Data File consists of variables from the Monitoring Department's database, which is limited to those defendants whose records have been furnished to the USSC by United States district courts and United States magistrates, as well as variables created by the OPA specifically for research purposes. The data include variables from the Judgement and Conviction (J and C) order submitted by the court, background and guideline information collected from the Presentencing Report (PSR), and the report on sentencing hearing in the Statement of Reasons (SOR). These data contain detailed information such as the guideline base offense level, offense level adjustments, criminal history, departure status, statement of reasons given for departure, and basic demographic information. These data are the primary analysis file and include only statute, guideline computation, and adjustment variables for the most serious offense of conviction. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24108.v2",
+                    "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 2000 [United States]"
+                }
+            ],
+            "identifier": "952",
+            "isPartOf": "2174",
+            "issued": "2009-02-11T11:13:30",
             "keyword": [
                 "administration",
                 "court cases",
@@ -27411,115 +27405,55 @@
                 "sentencing guidelines",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:54:29",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-11T11:13:30",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24108.v2",
-                    "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 2000 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 2001 [United States]",
-            "description": "These data contain records of criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2001. It is estimated that over 90 percent of felony defendants in the federal criminal justice system are sentenced pursuant to the SRA of 1984. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. The Standardized Research Data File consists of variables from the Monitoring Department's database, which is limited to those defendants whose records have been furnished to the USSC by United States district courts and United States magistrates, as well as variables created by the OPA specifically for research purposes. The data include variables from the Judgement and Conviction (J and C) order submitted by the court, background and guideline information collected from the Presentencing Report (PSR), and the report on sentencing hearing in the Statement of Reasons (SOR). These data contain detailed information such as the guideline base offense level, offense level adjustments, criminal history, departure status, statement of reasons given for departure, and basic demographic information. These data are the primary analysis file and include only statute, guideline computation, and adjustment variables for the most serious offense of conviction. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:05:26",
-            "accessLevel": "restricted public",
-            "identifier": "953",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 2000 [United States]"
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
-                "administration",
-                "court cases",
-                "criminal law",
-                "defendants",
-                "federal courts",
-                "judicial decisions",
-                "legal systems",
-                "sentencing guidelines",
-                "trial courts"
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
-            "issued": "2009-02-11T11:24:09",
-            "language": [
-                "eng"
-            ],
+            "description": "These data contain records of criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2001. It is estimated that over 90 percent of felony defendants in the federal criminal justice system are sentenced pursuant to the SRA of 1984. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. The Standardized Research Data File consists of variables from the Monitoring Department's database, which is limited to those defendants whose records have been furnished to the USSC by United States district courts and United States magistrates, as well as variables created by the OPA specifically for research purposes. The data include variables from the Judgement and Conviction (J and C) order submitted by the court, background and guideline information collected from the Presentencing Report (PSR), and the report on sentencing hearing in the Statement of Reasons (SOR). These data contain detailed information such as the guideline base offense level, offense level adjustments, criminal history, departure status, statement of reasons given for departure, and basic demographic information. These data are the primary analysis file and include only statute, guideline computation, and adjustment variables for the most serious offense of conviction. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://doi.org/10.3886/ICPSR24127.v2",
                     "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 2001 [United States]"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 2002 [United States]",
-            "description": "These data contain records of criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2002. It is estimated that over 90 percent of felony defendants in the federal criminal justice system are sentenced pursuant to the SRA of 1984. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. The Standardized Research Data File consists of variables from the Monitoring Department's database, which is limited to those defendants whose records have been furnished to the USSC by United States district courts and United States magistrates, as well as variables created by the OPA specifically for research purposes. The data include variables from the Judgement and Conviction (J and C) order submitted by the court, background and guideline information collected from the Presentencing Report (PSR), and the report on sentencing hearing in the Statement of Reasons (SOR). These data contain detailed information such as the guideline base offense level, offense level adjustments, criminal history, departure status, statement of reasons given for departure, and basic demographic information. These data are the primary analysis file and include only statute, guideline computation, and adjustment variables for the most serious offense of conviction. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:16:14",
-            "accessLevel": "restricted public",
-            "identifier": "954",
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
+            "identifier": "953",
+            "isPartOf": "2174",
+            "issued": "2009-02-11T11:24:09",
             "keyword": [
                 "administration",
                 "court cases",
@@ -27531,55 +27465,55 @@
                 "sentencing guidelines",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:05:26",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-11T11:27:04",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24146.v2",
-                    "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 2002 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 2003 [United States]",
-            "description": "These data contain records of criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2003. It is estimated that over 90 percent of felony defendants in the federal criminal justice system are sentenced pursuant to the SRA of 1984. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. The Standardized Research Data File consists of variables from the Monitoring Department's database, which is limited to those defendants whose records have been furnished to the USSC by United States district courts and United States magistrates, as well as variables created by the OPA specifically for research purposes. The data include variables from the Judgement and Conviction (J and C) order submitted by the court, background and guideline information collected from the Presentencing Report (PSR), and the report on sentencing hearing in the Statement of Reasons (SOR). These data contain detailed information such as the guideline base offense level, offense level adjustments, criminal history, departure status, statement of reasons given for departure, and basic demographic information. These data are the primary analysis file and include only statute, guideline computation, and adjustment variables for the most serious offense of conviction. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:26:57",
-            "accessLevel": "restricted public",
-            "identifier": "955",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 2001 [United States]"
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
+            "description": "These data contain records of criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2002. It is estimated that over 90 percent of felony defendants in the federal criminal justice system are sentenced pursuant to the SRA of 1984. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. The Standardized Research Data File consists of variables from the Monitoring Department's database, which is limited to those defendants whose records have been furnished to the USSC by United States district courts and United States magistrates, as well as variables created by the OPA specifically for research purposes. The data include variables from the Judgement and Conviction (J and C) order submitted by the court, background and guideline information collected from the Presentencing Report (PSR), and the report on sentencing hearing in the Statement of Reasons (SOR). These data contain detailed information such as the guideline base offense level, offense level adjustments, criminal history, departure status, statement of reasons given for departure, and basic demographic information. These data are the primary analysis file and include only statute, guideline computation, and adjustment variables for the most serious offense of conviction. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24146.v2",
+                    "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 2002 [United States]"
+                }
+            ],
+            "identifier": "954",
+            "isPartOf": "2174",
+            "issued": "2009-02-11T11:27:04",
             "keyword": [
                 "administration",
                 "court cases",
@@ -27591,55 +27525,55 @@
                 "sentencing guidelines",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:16:14",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-11T11:31:14",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24165.v2",
-                    "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 2003 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 2004 [United States]",
-            "description": "These data contain records of criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2004. It is estimated that over 90 percent of felony defendants in the federal criminal justice system are sentenced pursuant to the SRA of 1984. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. The Standardized Research Data File consists of variables from the Monitoring Department's database, which is limited to those defendants whose records have been furnished to the USSC by United States district courts and United States magistrates, as well as variables created by the OPA specifically for research purposes. The data include variables from the Judgement and Conviction (J and C) order submitted by the court, background and guideline information collected from the Presentencing Report (PSR), and the report on sentencing hearing in the Statement of Reasons (SOR). These data contain detailed information such as the guideline base offense level, offense level adjustments, criminal history, departure status, statement of reasons given for departure, and basic demographic information. These data are the primary analysis file and include only statute, guideline computation, and adjustment variables for the most serious offense of conviction. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:36:31",
-            "accessLevel": "restricted public",
-            "identifier": "956",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 2002 [United States]"
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
+            "description": "These data contain records of criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2003. It is estimated that over 90 percent of felony defendants in the federal criminal justice system are sentenced pursuant to the SRA of 1984. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. The Standardized Research Data File consists of variables from the Monitoring Department's database, which is limited to those defendants whose records have been furnished to the USSC by United States district courts and United States magistrates, as well as variables created by the OPA specifically for research purposes. The data include variables from the Judgement and Conviction (J and C) order submitted by the court, background and guideline information collected from the Presentencing Report (PSR), and the report on sentencing hearing in the Statement of Reasons (SOR). These data contain detailed information such as the guideline base offense level, offense level adjustments, criminal history, departure status, statement of reasons given for departure, and basic demographic information. These data are the primary analysis file and include only statute, guideline computation, and adjustment variables for the most serious offense of conviction. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24165.v2",
+                    "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 2003 [United States]"
+                }
+            ],
+            "identifier": "955",
+            "isPartOf": "2174",
+            "issued": "2009-02-11T11:31:14",
             "keyword": [
                 "administration",
                 "court cases",
@@ -27651,55 +27585,55 @@
                 "sentencing guidelines",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:26:57",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-11T11:36:02",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24182.v3",
-                    "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 2004 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 2005 [United States]",
-            "description": "These data contain records of criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2005. It is estimated that over 90 percent of felony defendants in the federal criminal justice system are sentenced pursuant to the SRA of 1984. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. The Standardized Research Data File consists of variables from the Monitoring Department's database, which is limited to those defendants whose records have been furnished to the USSC by United States district courts and United States magistrates, as well as variables created by the OPA specifically for research purposes. The data include variables from the Judgement and Conviction (J and C) order submitted by the court, background and guideline information collected from the Presentencing Report (PSR), and the report on sentencing hearing in the Statement of Reasons (SOR). These data contain detailed information such as the guideline base offense level, offense level adjustments, criminal history, departure status, statement of reasons given for departure, and basic demographic information. These data are the primary analysis file and include only statute, guideline computation, and adjustment variables for the most serious offense of conviction. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:46:06",
-            "accessLevel": "restricted public",
-            "identifier": "957",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 2003 [United States]"
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
+            "description": "These data contain records of criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2004. It is estimated that over 90 percent of felony defendants in the federal criminal justice system are sentenced pursuant to the SRA of 1984. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. The Standardized Research Data File consists of variables from the Monitoring Department's database, which is limited to those defendants whose records have been furnished to the USSC by United States district courts and United States magistrates, as well as variables created by the OPA specifically for research purposes. The data include variables from the Judgement and Conviction (J and C) order submitted by the court, background and guideline information collected from the Presentencing Report (PSR), and the report on sentencing hearing in the Statement of Reasons (SOR). These data contain detailed information such as the guideline base offense level, offense level adjustments, criminal history, departure status, statement of reasons given for departure, and basic demographic information. These data are the primary analysis file and include only statute, guideline computation, and adjustment variables for the most serious offense of conviction. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24182.v3",
+                    "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 2004 [United States]"
+                }
+            ],
+            "identifier": "956",
+            "isPartOf": "2174",
+            "issued": "2009-02-11T11:36:02",
             "keyword": [
                 "administration",
                 "court cases",
@@ -27711,55 +27645,55 @@
                 "sentencing guidelines",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:36:31",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-11T11:39:30",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24200.v3",
-                    "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 2005 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 2006 [United States]",
-            "description": "These data contain records of criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2006. It is estimated that over 90 percent of felony defendants in the federal criminal justice system are sentenced pursuant to the SRA of 1984. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. The Standardized Research Data File consists of variables from the Monitoring Department's database, which is limited to those defendants whose records have been furnished to the USSC by United States district courts and United States magistrates, as well as variables created by the OPA specifically for research purposes. The data include variables from the Judgement and Conviction (J and C) order submitted by the court, background and guideline information collected from the Presentencing Report (PSR), and the report on sentencing hearing in the Statement of Reasons (SOR). These data contain detailed information such as the guideline base offense level, offense level adjustments, criminal history, departure status, statement of reasons given for departure, and basic demographic information. These data are the primary analysis file and include only statute, guideline computation, and adjustment variables for the most serious offense of conviction. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:54:39",
-            "accessLevel": "restricted public",
-            "identifier": "958",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 2004 [United States]"
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
+            "description": "These data contain records of criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2005. It is estimated that over 90 percent of felony defendants in the federal criminal justice system are sentenced pursuant to the SRA of 1984. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. The Standardized Research Data File consists of variables from the Monitoring Department's database, which is limited to those defendants whose records have been furnished to the USSC by United States district courts and United States magistrates, as well as variables created by the OPA specifically for research purposes. The data include variables from the Judgement and Conviction (J and C) order submitted by the court, background and guideline information collected from the Presentencing Report (PSR), and the report on sentencing hearing in the Statement of Reasons (SOR). These data contain detailed information such as the guideline base offense level, offense level adjustments, criminal history, departure status, statement of reasons given for departure, and basic demographic information. These data are the primary analysis file and include only statute, guideline computation, and adjustment variables for the most serious offense of conviction. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24200.v3",
+                    "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 2005 [United States]"
+                }
+            ],
+            "identifier": "957",
+            "isPartOf": "2174",
+            "issued": "2009-02-11T11:39:30",
             "keyword": [
                 "administration",
                 "court cases",
@@ -27771,55 +27705,55 @@
                 "sentencing guidelines",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:46:06",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-11T11:43:35",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24217.v3",
-                    "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 2006 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 2007 [United States]",
-            "description": "These data contain records of criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2007. It is estimated that over 90 percent of felony defendants in the federal criminal justice system are sentenced pursuant to the SRA of 1984. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. The Standardized Research Data File consists of variables from the Monitoring Department's database, which is limited to those defendants whose records have been furnished to the USSC by United States district courts and United States magistrates, as well as variables created by the OPA specifically for research purposes. The data include variables from the Judgement and Conviction (J and C) order submitted by the court, background and guideline information collected from the Presentencing Report (PSR), and the report on sentencing hearing in the Statement of Reasons (SOR). These data contain detailed information such as the guideline base offense level, offense level adjustments, criminal history, departure status, statement of reasons given for departure, and basic demographic information. These data are the primary analysis file and include only statute, guideline computation, and adjustment variables for the most serious offense of conviction. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T12:03:13",
-            "accessLevel": "restricted public",
-            "identifier": "959",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 2005 [United States]"
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
+            "description": "These data contain records of criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2006. It is estimated that over 90 percent of felony defendants in the federal criminal justice system are sentenced pursuant to the SRA of 1984. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. The Standardized Research Data File consists of variables from the Monitoring Department's database, which is limited to those defendants whose records have been furnished to the USSC by United States district courts and United States magistrates, as well as variables created by the OPA specifically for research purposes. The data include variables from the Judgement and Conviction (J and C) order submitted by the court, background and guideline information collected from the Presentencing Report (PSR), and the report on sentencing hearing in the Statement of Reasons (SOR). These data contain detailed information such as the guideline base offense level, offense level adjustments, criminal history, departure status, statement of reasons given for departure, and basic demographic information. These data are the primary analysis file and include only statute, guideline computation, and adjustment variables for the most serious offense of conviction. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24217.v3",
+                    "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 2006 [United States]"
+                }
+            ],
+            "identifier": "958",
+            "isPartOf": "2174",
+            "issued": "2009-02-11T11:43:35",
             "keyword": [
                 "administration",
                 "court cases",
@@ -27831,55 +27765,55 @@
                 "sentencing guidelines",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:54:39",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-23T14:35:57",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24232.v2",
-                    "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 2007 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 2008 [United States]",
-            "description": "These data contain records of criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2008. It is estimated that over 90 percent of felony defendants in the federal criminal justice system are sentenced pursuant to the SRA of 1984. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. The Standardized Research Data File consists of variables from the Monitoring Department's database, which is limited to those defendants whose records have been furnished to the USSC by United States district courts and United States magistrates, as well as variables created by the OPA specifically for research purposes. The data include variables from the Judgement and Conviction (J and C) order submitted by the court, background and guideline information collected from the Presentencing Report (PSR), and the report on sentencing hearing in the Statement of Reasons (SOR). These data contain detailed information such as the guideline base offense level, offense level adjustments, criminal history, departure status, statement of reasons given for departure, and basic demographic information. These data are the primary analysis file and include only statute, guideline computation, and adjustment variables for the most serious offense of conviction. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T12:08:58",
-            "accessLevel": "restricted public",
-            "identifier": "960",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 2006 [United States]"
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
+            "description": "These data contain records of criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2007. It is estimated that over 90 percent of felony defendants in the federal criminal justice system are sentenced pursuant to the SRA of 1984. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. The Standardized Research Data File consists of variables from the Monitoring Department's database, which is limited to those defendants whose records have been furnished to the USSC by United States district courts and United States magistrates, as well as variables created by the OPA specifically for research purposes. The data include variables from the Judgement and Conviction (J and C) order submitted by the court, background and guideline information collected from the Presentencing Report (PSR), and the report on sentencing hearing in the Statement of Reasons (SOR). These data contain detailed information such as the guideline base offense level, offense level adjustments, criminal history, departure status, statement of reasons given for departure, and basic demographic information. These data are the primary analysis file and include only statute, guideline computation, and adjustment variables for the most serious offense of conviction. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24232.v2",
+                    "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 2007 [United States]"
+                }
+            ],
+            "identifier": "959",
+            "isPartOf": "2174",
+            "issued": "2009-02-23T14:35:57",
             "keyword": [
                 "administration",
                 "court cases",
@@ -27891,55 +27825,55 @@
                 "sentencing guidelines",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T12:03:13",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2011-02-07T15:10:31",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR29381.v2",
-                    "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 2008 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 2009",
-            "description": "These data contain records of criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2009. It is estimated that over 90 percent of felony defendants in the federal criminal justice system are sentenced pursuant to the SRA of 1984. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. The Standardized Research Data File consists of variables from the Monitoring Department's database, which is limited to those defendants whose records have been furnished to the USSC by United States district courts and United States magistrates, as well as variables created by the OPA specifically for research purposes. The data include variables from the Judgement and Conviction (J and C) order submitted by the court, background and guideline information collected from the Presentencing Report (PSR), and the report on sentencing hearing in the Statement of Reasons (SOR). These data contain detailed information such as the guideline base offense level, offense level adjustments, criminal history, departure status, statement of reasons given for departure, and basic demographic information. These data are the primary analysis file and include only statute, guideline computation, and adjustment variables for the most serious offense of conviction. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-06-06T09:16:02",
-            "accessLevel": "restricted public",
-            "identifier": "961",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 2007 [United States]"
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
+            "description": "These data contain records of criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2008. It is estimated that over 90 percent of felony defendants in the federal criminal justice system are sentenced pursuant to the SRA of 1984. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. The Standardized Research Data File consists of variables from the Monitoring Department's database, which is limited to those defendants whose records have been furnished to the USSC by United States district courts and United States magistrates, as well as variables created by the OPA specifically for research purposes. The data include variables from the Judgement and Conviction (J and C) order submitted by the court, background and guideline information collected from the Presentencing Report (PSR), and the report on sentencing hearing in the Statement of Reasons (SOR). These data contain detailed information such as the guideline base offense level, offense level adjustments, criminal history, departure status, statement of reasons given for departure, and basic demographic information. These data are the primary analysis file and include only statute, guideline computation, and adjustment variables for the most serious offense of conviction. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR29381.v2",
+                    "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 2008 [United States]"
+                }
+            ],
+            "identifier": "960",
+            "isPartOf": "2174",
+            "issued": "2011-02-07T15:10:31",
             "keyword": [
                 "administration",
                 "court cases",
@@ -27951,55 +27885,55 @@
                 "sentencing guidelines",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T12:08:58",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2011-06-06T09:14:24",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR30795.v1",
-                    "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 2009"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Guideline Computations for Defendants Sentenced Under the Sentencing Reform Act, 1999 [United States]",
-            "description": "These data contain records of guideline computations and adjustments for each count of conviction for criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 1999. The data are one of two supplementary files that should be used in conjunction with the primary analysis file, which contains records for all defendants sentenced under the guidelines. These data can be linked to the primary analysis file using the unique identifier variable USSCIDN. The number of records for a defendant in the current data corresponds to the total number of guideline computations, which may or may not equal the total counts of conviction for that defendant, dependent upon the grouping rules of the particular guideline in question (see Section 3D1.2 of the guidelines manual). As an example, a defendant with five counts of drug trafficking will only have one guideline computation because each of the drug weights for each count are simply added together and only one calculation is necessary. However, if a defendant has five counts of bank robbery, he or she will have five separate guideline computations because bank robbery is considered to be a nongroupable offense. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T09:50:27",
-            "accessLevel": "restricted public",
-            "identifier": "962",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 2008 [United States]"
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
+            "description": "These data contain records of criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2009. It is estimated that over 90 percent of felony defendants in the federal criminal justice system are sentenced pursuant to the SRA of 1984. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. The Standardized Research Data File consists of variables from the Monitoring Department's database, which is limited to those defendants whose records have been furnished to the USSC by United States district courts and United States magistrates, as well as variables created by the OPA specifically for research purposes. The data include variables from the Judgement and Conviction (J and C) order submitted by the court, background and guideline information collected from the Presentencing Report (PSR), and the report on sentencing hearing in the Statement of Reasons (SOR). These data contain detailed information such as the guideline base offense level, offense level adjustments, criminal history, departure status, statement of reasons given for departure, and basic demographic information. These data are the primary analysis file and include only statute, guideline computation, and adjustment variables for the most serious offense of conviction. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR30795.v1",
+                    "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 2009"
+                }
+            ],
+            "identifier": "961",
+            "isPartOf": "2174",
+            "issued": "2011-06-06T09:14:24",
             "keyword": [
                 "administration",
                 "court cases",
@@ -28011,55 +27945,55 @@
                 "sentencing guidelines",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-06-06T09:16:02",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-04T09:41:02",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR23764.v2",
-                    "title": "Federal Justice Statistics Program: Guideline Computations for Defendants Sentenced Under the Sentencing Reform Act, 1999 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Guideline Computations for Defendants Sentenced Under the Sentencing Reform Act, 2000",
-            "description": "These data contain records of guideline computations and adjustments for each count of conviction for criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2000. The data are one of two supplementary files that should be used in conjunction with the primary analysis file, which contains records for all defendants sentenced under the guidelines. These data can be linked to the primary analysis file using the unique identifier variable USSCIDN. The number of records for a defendant in the current data corresponds to the total number of guideline computations, which may or may not equal the total counts of conviction for that defendant, dependent upon the grouping rules of the particular guideline in question (see Section 3D1.2 of the guidelines manual). As an example, a defendant with five counts of drug trafficking will only have one guideline computation because each of the drug weights for each count are simply added together and only one calculation is necessary. However, if a defendant has five counts of bank robbery, he or she will have five separate guideline computations because bank robbery is considered to be a nongroupable offense. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:02:07",
-            "accessLevel": "restricted public",
-            "identifier": "963",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Defendants Sentenced Under the Sentencing Reform Act, 2009"
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
+            "description": "These data contain records of guideline computations and adjustments for each count of conviction for criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 1999. The data are one of two supplementary files that should be used in conjunction with the primary analysis file, which contains records for all defendants sentenced under the guidelines. These data can be linked to the primary analysis file using the unique identifier variable USSCIDN. The number of records for a defendant in the current data corresponds to the total number of guideline computations, which may or may not equal the total counts of conviction for that defendant, dependent upon the grouping rules of the particular guideline in question (see Section 3D1.2 of the guidelines manual). As an example, a defendant with five counts of drug trafficking will only have one guideline computation because each of the drug weights for each count are simply added together and only one calculation is necessary. However, if a defendant has five counts of bank robbery, he or she will have five separate guideline computations because bank robbery is considered to be a nongroupable offense. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR23764.v2",
+                    "title": "Federal Justice Statistics Program: Guideline Computations for Defendants Sentenced Under the Sentencing Reform Act, 1999 [United States]"
+                }
+            ],
+            "identifier": "962",
+            "isPartOf": "2174",
+            "issued": "2009-02-04T09:41:02",
             "keyword": [
                 "administration",
                 "court cases",
@@ -28071,55 +28005,55 @@
                 "sentencing guidelines",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T09:50:27",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-04T09:45:40",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24015.v2",
-                    "title": "Federal Justice Statistics Program: Guideline Computations for Defendants Sentenced Under the Sentencing Reform Act, 2000"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Guideline Computations for Defendants Sentenced Under the Sentencing Reform Act, 2001",
-            "description": "These data contain records of guideline computations and adjustments for each count of conviction for criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2001. The data are one of two supplementary files that should be used in conjunction with the primary analysis file, which contains records for all defendants sentenced under the guidelines. These data can be linked to the primary analysis file using the unique identifier variable USSCIDN. The number of records for a defendant in the current data corresponds to the total number of guideline computations, which may or may not equal the total counts of conviction for that defendant, dependent upon the grouping rules of the particular guideline in question (see Section 3D1.2 of the guidelines manual). As an example, a defendant with five counts of drug trafficking will only have one guideline computation because each of the drug weights for each count are simply added together and only one calculation is necessary. However, if a defendant has five counts of bank robbery, he or she will have five separate guideline computations because bank robbery is considered to be a nongroupable offense. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:12:20",
-            "accessLevel": "restricted public",
-            "identifier": "964",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Guideline Computations for Defendants Sentenced Under the Sentencing Reform Act, 1999 [United States]"
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
+            "description": "These data contain records of guideline computations and adjustments for each count of conviction for criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2000. The data are one of two supplementary files that should be used in conjunction with the primary analysis file, which contains records for all defendants sentenced under the guidelines. These data can be linked to the primary analysis file using the unique identifier variable USSCIDN. The number of records for a defendant in the current data corresponds to the total number of guideline computations, which may or may not equal the total counts of conviction for that defendant, dependent upon the grouping rules of the particular guideline in question (see Section 3D1.2 of the guidelines manual). As an example, a defendant with five counts of drug trafficking will only have one guideline computation because each of the drug weights for each count are simply added together and only one calculation is necessary. However, if a defendant has five counts of bank robbery, he or she will have five separate guideline computations because bank robbery is considered to be a nongroupable offense. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24015.v2",
+                    "title": "Federal Justice Statistics Program: Guideline Computations for Defendants Sentenced Under the Sentencing Reform Act, 2000"
+                }
+            ],
+            "identifier": "963",
+            "isPartOf": "2174",
+            "issued": "2009-02-04T09:45:40",
             "keyword": [
                 "administration",
                 "court cases",
@@ -28131,55 +28065,55 @@
                 "sentencing guidelines",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:02:07",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-04T09:50:55",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24034.v2",
-                    "title": "Federal Justice Statistics Program: Guideline Computations for Defendants Sentenced Under the Sentencing Reform Act, 2001"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Guideline Computations for Defendants Sentenced Under the Sentencing Reform Act, 2002",
-            "description": "These data contain records of guideline computations and adjustments for each count of conviction for criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2002. The data are one of two supplementary files that should be used in conjunction with the primary analysis file, which contains records for all defendants sentenced under the guidelines. These data can be linked to the primary analysis file using the unique identifier variable USSCIDN. The number of records for a defendant in the current data corresponds to the total number of guideline computations, which may or may not equal the total counts of conviction for that defendant, dependent upon the grouping rules of the particular guideline in question (see Section 3D1.2 of the guidelines manual). As an example, a defendant with five counts of drug trafficking will only have one guideline computation because each of the drug weights for each count are simply added together and only one calculation is necessary. However, if a defendant has five counts of bank robbery, he or she will have five separate guideline computations because bank robbery is considered to be a nongroupable offense. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:23:12",
-            "accessLevel": "restricted public",
-            "identifier": "965",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Guideline Computations for Defendants Sentenced Under the Sentencing Reform Act, 2000"
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
+            "description": "These data contain records of guideline computations and adjustments for each count of conviction for criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2001. The data are one of two supplementary files that should be used in conjunction with the primary analysis file, which contains records for all defendants sentenced under the guidelines. These data can be linked to the primary analysis file using the unique identifier variable USSCIDN. The number of records for a defendant in the current data corresponds to the total number of guideline computations, which may or may not equal the total counts of conviction for that defendant, dependent upon the grouping rules of the particular guideline in question (see Section 3D1.2 of the guidelines manual). As an example, a defendant with five counts of drug trafficking will only have one guideline computation because each of the drug weights for each count are simply added together and only one calculation is necessary. However, if a defendant has five counts of bank robbery, he or she will have five separate guideline computations because bank robbery is considered to be a nongroupable offense. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24034.v2",
+                    "title": "Federal Justice Statistics Program: Guideline Computations for Defendants Sentenced Under the Sentencing Reform Act, 2001"
+                }
+            ],
+            "identifier": "964",
+            "isPartOf": "2174",
+            "issued": "2009-02-04T09:50:55",
             "keyword": [
                 "administration",
                 "court cases",
@@ -28191,55 +28125,55 @@
                 "sentencing guidelines",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:12:20",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-04T09:56:38",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24053.v2",
-                    "title": "Federal Justice Statistics Program: Guideline Computations for Defendants Sentenced Under the Sentencing Reform Act, 2002"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Guideline Computations for Defendants Sentenced Under the Sentencing Reform Act, 2003",
-            "description": "These data contain records of guideline computations and adjustments for each count of conviction for criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2003. The data are one of two supplementary files that should be used in conjunction with the primary analysis file, which contains records for all defendants sentenced under the guidelines. These data can be linked to the primary analysis file using the unique identifier variable USSCIDN. The number of records for a defendant in the current data corresponds to the total number of guideline computations, which may or may not equal the total counts of conviction for that defendant, dependent upon the grouping rules of the particular guideline in question (see Section 3D1.2 of the guidelines manual). As an example, a defendant with five counts of drug trafficking will only have one guideline computation because each of the drug weights for each count are simply added together and only one calculation is necessary. However, if a defendant has five counts of bank robbery, he or she will have five separate guideline computations because bank robbery is considered to be a nongroupable offense. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:33:52",
-            "accessLevel": "restricted public",
-            "identifier": "966",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Guideline Computations for Defendants Sentenced Under the Sentencing Reform Act, 2001"
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
+            "description": "These data contain records of guideline computations and adjustments for each count of conviction for criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2002. The data are one of two supplementary files that should be used in conjunction with the primary analysis file, which contains records for all defendants sentenced under the guidelines. These data can be linked to the primary analysis file using the unique identifier variable USSCIDN. The number of records for a defendant in the current data corresponds to the total number of guideline computations, which may or may not equal the total counts of conviction for that defendant, dependent upon the grouping rules of the particular guideline in question (see Section 3D1.2 of the guidelines manual). As an example, a defendant with five counts of drug trafficking will only have one guideline computation because each of the drug weights for each count are simply added together and only one calculation is necessary. However, if a defendant has five counts of bank robbery, he or she will have five separate guideline computations because bank robbery is considered to be a nongroupable offense. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24053.v2",
+                    "title": "Federal Justice Statistics Program: Guideline Computations for Defendants Sentenced Under the Sentencing Reform Act, 2002"
+                }
+            ],
+            "identifier": "965",
+            "isPartOf": "2174",
+            "issued": "2009-02-04T09:56:38",
             "keyword": [
                 "administration",
                 "court cases",
@@ -28251,55 +28185,55 @@
                 "sentencing guidelines",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:23:12",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-04T10:00:24",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24072.v2",
-                    "title": "Federal Justice Statistics Program: Guideline Computations for Defendants Sentenced Under the Sentencing Reform Act, 2003"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Guideline Computations for Defendants Sentenced Under the Sentencing Reform Act, 2004",
-            "description": "These data contain records of guideline computations and adjustments for each count of conviction for criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2004. The data are one of two supplementary files that should be used in conjunction with the primary analysis file, which contains records for all defendants sentenced under the guidelines. These data can be linked to the primary analysis file using the unique identifier variable USSCIDN. The number of records for a defendant in the current data corresponds to the total number of guideline computations, which may or may not equal the total counts of conviction for that defendant, dependent upon the grouping rules of the particular guideline in question (see Section 3D1.2 of the guidelines manual). As an example, a defendant with five counts of drug trafficking will only have one guideline computation because each of the drug weights for each count are simply added together and only one calculation is necessary. However, if a defendant has five counts of bank robbery, he or she will have five separate guideline computations because bank robbery is considered to be a nongroupable offense. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:44:48",
-            "accessLevel": "restricted public",
-            "identifier": "967",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Guideline Computations for Defendants Sentenced Under the Sentencing Reform Act, 2002"
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
+            "description": "These data contain records of guideline computations and adjustments for each count of conviction for criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2003. The data are one of two supplementary files that should be used in conjunction with the primary analysis file, which contains records for all defendants sentenced under the guidelines. These data can be linked to the primary analysis file using the unique identifier variable USSCIDN. The number of records for a defendant in the current data corresponds to the total number of guideline computations, which may or may not equal the total counts of conviction for that defendant, dependent upon the grouping rules of the particular guideline in question (see Section 3D1.2 of the guidelines manual). As an example, a defendant with five counts of drug trafficking will only have one guideline computation because each of the drug weights for each count are simply added together and only one calculation is necessary. However, if a defendant has five counts of bank robbery, he or she will have five separate guideline computations because bank robbery is considered to be a nongroupable offense. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24072.v2",
+                    "title": "Federal Justice Statistics Program: Guideline Computations for Defendants Sentenced Under the Sentencing Reform Act, 2003"
+                }
+            ],
+            "identifier": "966",
+            "isPartOf": "2174",
+            "issued": "2009-02-04T10:00:24",
             "keyword": [
                 "administration",
                 "court cases",
@@ -28311,55 +28245,55 @@
                 "sentencing guidelines",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:33:52",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-03T13:53:16",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24091.v2",
-                    "title": "Federal Justice Statistics Program: Guideline Computations for Defendants Sentenced Under the Sentencing Reform Act, 2004"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Guideline Computations for Defendants Sentenced Under the Sentencing Reform Act, 2005",
-            "description": "These data contain records of guideline computations and adjustments for each count of conviction for criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2005. The data are one of two supplementary files that should be used in conjunction with the primary analysis file, which contains records for all defendants sentenced under the guidelines. These data can be linked to the primary analysis file using the unique identifier variable USSCIDN. The number of records for a defendant in the current data corresponds to the total number of guideline computations, which may or may not equal the total counts of conviction for that defendant, dependent upon the grouping rules of the particular guideline in question (see Section 3D1.2 of the guidelines manual). As an example, a defendant with five counts of drug trafficking will only have one guideline computation because each of the drug weights for each count are simply added together and only one calculation is necessary. However, if a defendant has five counts of bank robbery, he or she will have five separate guideline computations because bank robbery is considered to be a nongroupable offense. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:55:39",
-            "accessLevel": "restricted public",
-            "identifier": "968",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Guideline Computations for Defendants Sentenced Under the Sentencing Reform Act, 2003"
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
+            "description": "These data contain records of guideline computations and adjustments for each count of conviction for criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2004. The data are one of two supplementary files that should be used in conjunction with the primary analysis file, which contains records for all defendants sentenced under the guidelines. These data can be linked to the primary analysis file using the unique identifier variable USSCIDN. The number of records for a defendant in the current data corresponds to the total number of guideline computations, which may or may not equal the total counts of conviction for that defendant, dependent upon the grouping rules of the particular guideline in question (see Section 3D1.2 of the guidelines manual). As an example, a defendant with five counts of drug trafficking will only have one guideline computation because each of the drug weights for each count are simply added together and only one calculation is necessary. However, if a defendant has five counts of bank robbery, he or she will have five separate guideline computations because bank robbery is considered to be a nongroupable offense. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24091.v2",
+                    "title": "Federal Justice Statistics Program: Guideline Computations for Defendants Sentenced Under the Sentencing Reform Act, 2004"
+                }
+            ],
+            "identifier": "967",
+            "isPartOf": "2174",
+            "issued": "2009-02-03T13:53:16",
             "keyword": [
                 "administration",
                 "court cases",
@@ -28371,55 +28305,55 @@
                 "sentencing guidelines",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:44:48",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-03T13:58:20",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24110.v2",
-                    "title": "Federal Justice Statistics Program: Guideline Computations for Defendants Sentenced Under the Sentencing Reform Act, 2005"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Guideline Computations for Defendants Sentenced Under the Sentencing Reform Act, 2006",
-            "description": "These data contain records of guideline computations and adjustments for each count of conviction for criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2006. The data are one of two supplementary files that should be used in conjunction with the primary analysis file, which contains records for all defendants sentenced under the guidelines. These data can be linked to the primary analysis file using the unique identifier variable USSCIDN. The number of records for a defendant in the current data corresponds to the total number of guideline computations, which may or may not equal the total counts of conviction for that defendant, dependent upon the grouping rules of the particular guideline in question (see Section 3D1.2 of the guidelines manual). As an example, a defendant with five counts of drug trafficking will only have one guideline computation because each of the drug weights for each count are simply added together and only one calculation is necessary. However, if a defendant has five counts of bank robbery, he or she will have five separate guideline computations because bank robbery is considered to be a nongroupable offense. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:06:33",
-            "accessLevel": "restricted public",
-            "identifier": "969",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Guideline Computations for Defendants Sentenced Under the Sentencing Reform Act, 2004"
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
+            "description": "These data contain records of guideline computations and adjustments for each count of conviction for criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2005. The data are one of two supplementary files that should be used in conjunction with the primary analysis file, which contains records for all defendants sentenced under the guidelines. These data can be linked to the primary analysis file using the unique identifier variable USSCIDN. The number of records for a defendant in the current data corresponds to the total number of guideline computations, which may or may not equal the total counts of conviction for that defendant, dependent upon the grouping rules of the particular guideline in question (see Section 3D1.2 of the guidelines manual). As an example, a defendant with five counts of drug trafficking will only have one guideline computation because each of the drug weights for each count are simply added together and only one calculation is necessary. However, if a defendant has five counts of bank robbery, he or she will have five separate guideline computations because bank robbery is considered to be a nongroupable offense. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24110.v2",
+                    "title": "Federal Justice Statistics Program: Guideline Computations for Defendants Sentenced Under the Sentencing Reform Act, 2005"
+                }
+            ],
+            "identifier": "968",
+            "isPartOf": "2174",
+            "issued": "2009-02-03T13:58:20",
             "keyword": [
                 "administration",
                 "court cases",
@@ -28431,55 +28365,55 @@
                 "sentencing guidelines",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:55:39",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-03T14:10:45",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24129.v2",
-                    "title": "Federal Justice Statistics Program: Guideline Computations for Defendants Sentenced Under the Sentencing Reform Act, 2006"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Guideline Computations for Defendants Sentenced Under the Sentencing Reform Act, 2007",
-            "description": "These data contain records of guideline computations and adjustments for each count of conviction for criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2007. The data are one of two supplementary files that should be used in conjunction with the primary analysis file, which contains records for all defendants sentenced under the guidelines. These data can be linked to the primary analysis file using the unique identifier variable USSCIDN. The number of records for a defendant in the current data corresponds to the total number of guideline computations, which may or may not equal the total counts of conviction for that defendant, dependent upon the grouping rules of the particular guideline in question (see Section 3D1.2 of the guidelines manual). As an example, a defendant with five counts of drug trafficking will only have one guideline computation because each of the drug weights for each count are simply added together and only one calculation is necessary. However, if a defendant has five counts of bank robbery, he or she will have five separate guideline computations because bank robbery is considered to be a nongroupable offense. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:17:28",
-            "accessLevel": "restricted public",
-            "identifier": "970",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Guideline Computations for Defendants Sentenced Under the Sentencing Reform Act, 2005"
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
+            "description": "These data contain records of guideline computations and adjustments for each count of conviction for criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2006. The data are one of two supplementary files that should be used in conjunction with the primary analysis file, which contains records for all defendants sentenced under the guidelines. These data can be linked to the primary analysis file using the unique identifier variable USSCIDN. The number of records for a defendant in the current data corresponds to the total number of guideline computations, which may or may not equal the total counts of conviction for that defendant, dependent upon the grouping rules of the particular guideline in question (see Section 3D1.2 of the guidelines manual). As an example, a defendant with five counts of drug trafficking will only have one guideline computation because each of the drug weights for each count are simply added together and only one calculation is necessary. However, if a defendant has five counts of bank robbery, he or she will have five separate guideline computations because bank robbery is considered to be a nongroupable offense. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24129.v2",
+                    "title": "Federal Justice Statistics Program: Guideline Computations for Defendants Sentenced Under the Sentencing Reform Act, 2006"
+                }
+            ],
+            "identifier": "969",
+            "isPartOf": "2174",
+            "issued": "2009-02-03T14:10:45",
             "keyword": [
                 "administration",
                 "court cases",
@@ -28491,55 +28425,55 @@
                 "sentencing guidelines",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:06:33",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-23T14:32:01",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24148.v2",
-                    "title": "Federal Justice Statistics Program: Guideline Computations for Defendants Sentenced Under the Sentencing Reform Act, 2007"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Guideline Computations for Defendants Sentenced Under the Sentencing Reform Act, 2008",
-            "description": "These data contain records of guideline computations and adjustments for each count of conviction for criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2008. The data are one of two supplementary files that should be used in conjunction with the primary analysis file, which contains records for all defendants sentenced under the guidelines. These data can be linked to the primary analysis file using the unique identifier variable USSCIDN. The number of records for a defendant in the current data corresponds to the total number of guideline computations, which may or may not equal the total counts of conviction for that defendant, dependent upon the grouping rules of the particular guideline in question (see Section 3D1.2 of the guidelines manual). As an example, a defendant with five counts of drug trafficking will only have one guideline computation because each of the drug weights for each count are simply added together and only one calculation is necessary. However, if a defendant has five counts of bank robbery, he or she will have five separate guideline computations because bank robbery is considered to be a nongroupable offense. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T12:28:03",
-            "accessLevel": "restricted public",
-            "identifier": "971",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Guideline Computations for Defendants Sentenced Under the Sentencing Reform Act, 2006"
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
+            "description": "These data contain records of guideline computations and adjustments for each count of conviction for criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2007. The data are one of two supplementary files that should be used in conjunction with the primary analysis file, which contains records for all defendants sentenced under the guidelines. These data can be linked to the primary analysis file using the unique identifier variable USSCIDN. The number of records for a defendant in the current data corresponds to the total number of guideline computations, which may or may not equal the total counts of conviction for that defendant, dependent upon the grouping rules of the particular guideline in question (see Section 3D1.2 of the guidelines manual). As an example, a defendant with five counts of drug trafficking will only have one guideline computation because each of the drug weights for each count are simply added together and only one calculation is necessary. However, if a defendant has five counts of bank robbery, he or she will have five separate guideline computations because bank robbery is considered to be a nongroupable offense. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24148.v2",
+                    "title": "Federal Justice Statistics Program: Guideline Computations for Defendants Sentenced Under the Sentencing Reform Act, 2007"
+                }
+            ],
+            "identifier": "970",
+            "isPartOf": "2174",
+            "issued": "2009-02-23T14:32:01",
             "keyword": [
                 "administration",
                 "court cases",
@@ -28551,55 +28485,55 @@
                 "sentencing guidelines",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:17:28",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2011-02-08T10:12:27",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR29431.v2",
-                    "title": "Federal Justice Statistics Program: Guideline Computations for Defendants Sentenced Under the Sentencing Reform Act, 2008"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Guideline Computations for Defendants Sentenced Under the Sentencing Reform Act, 2009",
-            "description": "These data contain records of guideline computations and adjustments for each count of conviction for criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2009. The data are one of two supplementary files that should be used in conjunction with the primary analysis file, which contains records for all defendants sentenced under the guidelines. These data can be linked to the primary analysis file using the unique identifier variable USSCIDN. The number of records for a defendant in the current data corresponds to the total number of guideline computations, which may or may not equal the total counts of conviction for that defendant, dependent upon the grouping rules of the particular guideline in question (see Section 3D1.2 of the guidelines manual). As an example, a defendant with five counts of drug trafficking will only have one guideline computation because each of the drug weights for each count are simply added together and only one calculation is necessary. However, if a defendant has five counts of bank robbery, he or she will have five separate guideline computations because bank robbery is considered to be a nongroupable offense. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-06-06T09:22:08",
-            "accessLevel": "restricted public",
-            "identifier": "972",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Guideline Computations for Defendants Sentenced Under the Sentencing Reform Act, 2007"
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
+            "description": "These data contain records of guideline computations and adjustments for each count of conviction for criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2008. The data are one of two supplementary files that should be used in conjunction with the primary analysis file, which contains records for all defendants sentenced under the guidelines. These data can be linked to the primary analysis file using the unique identifier variable USSCIDN. The number of records for a defendant in the current data corresponds to the total number of guideline computations, which may or may not equal the total counts of conviction for that defendant, dependent upon the grouping rules of the particular guideline in question (see Section 3D1.2 of the guidelines manual). As an example, a defendant with five counts of drug trafficking will only have one guideline computation because each of the drug weights for each count are simply added together and only one calculation is necessary. However, if a defendant has five counts of bank robbery, he or she will have five separate guideline computations because bank robbery is considered to be a nongroupable offense. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR29431.v2",
+                    "title": "Federal Justice Statistics Program: Guideline Computations for Defendants Sentenced Under the Sentencing Reform Act, 2008"
+                }
+            ],
+            "identifier": "971",
+            "isPartOf": "2174",
+            "issued": "2011-02-08T10:12:27",
             "keyword": [
                 "administration",
                 "court cases",
@@ -28611,2108 +28545,2168 @@
                 "sentencing guidelines",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T12:28:03",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
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
-            "issued": "2011-06-06T09:21:08",
-            "language": [
-                "eng"
+            "title": "Federal Justice Statistics Program: Guideline Computations for Defendants Sentenced Under the Sentencing Reform Act, 2008"
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
+            "description": "These data contain records of guideline computations and adjustments for each count of conviction for criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2009. The data are one of two supplementary files that should be used in conjunction with the primary analysis file, which contains records for all defendants sentenced under the guidelines. These data can be linked to the primary analysis file using the unique identifier variable USSCIDN. The number of records for a defendant in the current data corresponds to the total number of guideline computations, which may or may not equal the total counts of conviction for that defendant, dependent upon the grouping rules of the particular guideline in question (see Section 3D1.2 of the guidelines manual). As an example, a defendant with five counts of drug trafficking will only have one guideline computation because each of the drug weights for each count are simply added together and only one calculation is necessary. However, if a defendant has five counts of bank robbery, he or she will have five separate guideline computations because bank robbery is considered to be a nongroupable offense. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://doi.org/10.3886/ICPSR30796.v1",
                     "title": "Federal Justice Statistics Program: Guideline Computations for Defendants Sentenced Under the Sentencing Reform Act, 2009"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Linking Data file, 1994 - 2005 [United States]",
-            "description": "The linking file relates the sequential record numbers (i.e. SEQ_NUM) included in the standard analysis files (SAFs) within an agency's SAFs over time and across different agencies' SAFs. The linking file includes sequential record numbers from the United States Marshals Service (arrests), Executive Office for United States Attorneys (matters and cases), Administrative Office of the United States Courts (cases), United States Sentencing Commission (sentencing events), and Bureau of Prisons (prisoners). By joining the sequential record numbers from the linking file with the sequential record numbers in the appropriate SAFs, it is possible to track the course of individual defendant-cases from arrest to prosecution, adjudication, sentencing, and corrections. Note: The Federal Justice Statistics Resource Center (FJSRC) only recently received data from the Bureau of Prisons (BOP) for fiscal years 2004 and 2005 and has not updated the linking file to include these newly acquired data. Consequently, the linking data file does not support linking records from other agencies to BOP records from those two fiscal years.",
-            "modified": "2011-03-08T12:05:32",
-            "accessLevel": "restricted public",
-            "identifier": "973",
+            ],
+            "identifier": "972",
+            "isPartOf": "2174",
+            "issued": "2011-06-06T09:21:08",
+            "keyword": [
+                "administration",
+                "court cases",
+                "criminal law",
+                "defendants",
+                "federal courts",
+                "judicial decisions",
+                "legal systems",
+                "sentencing guidelines",
+                "trial courts"
+            ],
+            "language": [
+                "eng"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-06-06T09:22:08",
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
+            "title": "Federal Justice Statistics Program: Guideline Computations for Defendants Sentenced Under the Sentencing Reform Act, 2009"
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
+            "description": "The linking file relates the sequential record numbers (i.e. SEQ_NUM) included in the standard analysis files (SAFs) within an agency's SAFs over time and across different agencies' SAFs. The linking file includes sequential record numbers from the United States Marshals Service (arrests), Executive Office for United States Attorneys (matters and cases), Administrative Office of the United States Courts (cases), United States Sentencing Commission (sentencing events), and Bureau of Prisons (prisoners). By joining the sequential record numbers from the linking file with the sequential record numbers in the appropriate SAFs, it is possible to track the course of individual defendant-cases from arrest to prosecution, adjudication, sentencing, and corrections. Note: The Federal Justice Statistics Resource Center (FJSRC) only recently received data from the Bureau of Prisons (BOP) for fiscal years 2004 and 2005 and has not updated the linking file to include these newly acquired data. Consequently, the linking data file does not support linking records from other agencies to BOP records from those two fiscal years.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24821.v2",
+                    "title": "Federal Justice Statistics Program: Linking Data file, 1994 - 2005 [United States]"
+                }
+            ],
+            "identifier": "973",
+            "isPartOf": "2174",
+            "issued": "2009-02-20T16:12:11",
             "keyword": [
                 "arrests",
                 "court cases",
                 "defendants",
                 "offenders"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T12:05:32",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-20T16:12:11",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24821.v2",
-                    "title": "Federal Justice Statistics Program: Linking Data file, 1994 - 2005 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 1994 [United States]",
-            "description": "The data contain records of sentenced offenders committed to the custody of the Bureau of Prisons (BOP) during fiscal year 1994. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T09:51:00",
-            "accessLevel": "restricted public",
-            "identifier": "974",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Linking Data file, 1994 - 2005 [United States]"
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
+            "description": "The data contain records of sentenced offenders committed to the custody of the Bureau of Prisons (BOP) during fiscal year 1994. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR23765.v2",
+                    "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 1994 [United States]"
+                }
+            ],
+            "identifier": "974",
+            "isPartOf": "2174",
+            "issued": "2009-02-05T09:51:25",
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
+            "modified": "2011-03-08T09:51:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-05T09:51:25",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR23765.v2",
-                    "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 1994 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 1995",
-            "description": "The data contain records of sentenced offenders committed to the custody of the Bureau of Prisons (BOP) during fiscal year 1995. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:02:40",
-            "accessLevel": "restricted public",
-            "identifier": "975",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 1994 [United States]"
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
+            "description": "The data contain records of sentenced offenders committed to the custody of the Bureau of Prisons (BOP) during fiscal year 1995. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24016.v2",
+                    "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 1995"
+                }
+            ],
+            "identifier": "975",
+            "isPartOf": "2174",
+            "issued": "2009-02-05T10:32:56",
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
+            "modified": "2011-03-08T10:02:40",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-05T10:32:56",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24016.v2",
-                    "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 1995"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 1996",
-            "description": "The data contain records of sentenced offenders committed to the custody of the Bureau of Prisons (BOP) during fiscal year 1996. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:12:58",
-            "accessLevel": "restricted public",
-            "identifier": "976",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 1995"
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
+            "description": "The data contain records of sentenced offenders committed to the custody of the Bureau of Prisons (BOP) during fiscal year 1996. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24035.v2",
+                    "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 1996"
+                }
+            ],
+            "identifier": "976",
+            "isPartOf": "2174",
+            "issued": "2009-02-05T10:35:38",
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
+            "modified": "2011-03-08T10:12:58",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-05T10:35:38",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24035.v2",
-                    "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 1996"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 1997",
-            "description": "The data contain records of sentenced offenders committed to the custody of the Bureau of Prisons (BOP) during fiscal year 1997. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:23:45",
-            "accessLevel": "restricted public",
-            "identifier": "977",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 1996"
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
+            "description": "The data contain records of sentenced offenders committed to the custody of the Bureau of Prisons (BOP) during fiscal year 1997. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24054.v2",
+                    "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 1997"
+                }
+            ],
+            "identifier": "977",
+            "isPartOf": "2174",
+            "issued": "2009-02-05T10:42:51",
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
+            "modified": "2011-03-08T10:23:45",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-05T10:42:51",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24054.v2",
-                    "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 1997"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 1998",
-            "description": "The data contain records of sentenced offenders committed to the custody of the Bureau of Prisons (BOP) during fiscal year 1998. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:34:26",
-            "accessLevel": "restricted public",
-            "identifier": "978",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 1997"
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
+            "description": "The data contain records of sentenced offenders committed to the custody of the Bureau of Prisons (BOP) during fiscal year 1998. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24073.v2",
+                    "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 1998"
+                }
+            ],
+            "identifier": "978",
+            "isPartOf": "2174",
+            "issued": "2009-02-05T10:46:43",
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
+            "modified": "2011-03-08T10:34:26",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-05T10:46:43",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24073.v2",
-                    "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 1998"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 1999",
-            "description": "The data contain records of sentenced offenders committed to the custody of the Bureau of Prisons (BOP) during fiscal year 1999. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:45:22",
-            "accessLevel": "restricted public",
-            "identifier": "979",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 1998"
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
+            "description": "The data contain records of sentenced offenders committed to the custody of the Bureau of Prisons (BOP) during fiscal year 1999. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24092.v2",
+                    "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 1999"
+                }
+            ],
+            "identifier": "979",
+            "isPartOf": "2174",
+            "issued": "2009-02-05T10:49:27",
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
+            "modified": "2011-03-08T10:45:22",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-05T10:49:27",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24092.v2",
-                    "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 1999"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2000",
-            "description": "The data contain records of sentenced offenders committed to the custody of the Bureau of Prisons (BOP) during fiscal year 2000. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:56:15",
-            "accessLevel": "restricted public",
-            "identifier": "980",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 1999"
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
+            "description": "The data contain records of sentenced offenders committed to the custody of the Bureau of Prisons (BOP) during fiscal year 2000. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24111.v2",
+                    "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2000"
+                }
+            ],
+            "identifier": "980",
+            "isPartOf": "2174",
+            "issued": "2009-02-05T10:52:13",
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
+            "modified": "2011-03-08T10:56:15",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-05T10:52:13",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24111.v2",
-                    "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2000"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2001",
-            "description": "The data contain records of sentenced offenders committed to the custody of the Bureau of Prisons (BOP) during fiscal year 2001. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:07:07",
-            "accessLevel": "restricted public",
-            "identifier": "981",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2000"
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
+            "description": "The data contain records of sentenced offenders committed to the custody of the Bureau of Prisons (BOP) during fiscal year 2001. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24130.v2",
+                    "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2001"
+                }
+            ],
+            "identifier": "981",
+            "isPartOf": "2174",
+            "issued": "2009-02-05T10:59:30",
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
+            "modified": "2011-03-08T11:07:07",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-05T10:59:30",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24130.v2",
-                    "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2001"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2002",
-            "description": "The data contain records of sentenced offenders committed to the custody of the Bureau of Prisons (BOP) during fiscal year 2002. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:18:06",
-            "accessLevel": "restricted public",
-            "identifier": "982",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2001"
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
+            "description": "The data contain records of sentenced offenders committed to the custody of the Bureau of Prisons (BOP) during fiscal year 2002. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24149.v2",
+                    "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2002"
+                }
+            ],
+            "identifier": "982",
+            "isPartOf": "2174",
+            "issued": "2009-02-05T11:03:34",
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
+            "modified": "2011-03-08T11:18:06",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-05T11:03:34",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24149.v2",
-                    "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2002"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2003",
-            "description": "The data contain records of sentenced offenders committed to the custody of the Bureau of Prisons (BOP) during fiscal year 2003. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:27:30",
-            "accessLevel": "restricted public",
-            "identifier": "983",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2002"
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
+            "description": "The data contain records of sentenced offenders committed to the custody of the Bureau of Prisons (BOP) during fiscal year 2003. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24166.v2",
+                    "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2003"
+                }
+            ],
+            "identifier": "983",
+            "isPartOf": "2174",
+            "issued": "2009-02-05T11:06:57",
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
+            "modified": "2011-03-08T11:27:30",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-05T11:06:57",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24166.v2",
-                    "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2003"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2004",
-            "description": "The data contain records of sentenced offenders committed to the custody of the Bureau of Prisons (BOP) during fiscal year 2004. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:37:05",
-            "accessLevel": "restricted public",
-            "identifier": "984",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2003"
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
+            "description": "The data contain records of sentenced offenders committed to the custody of the Bureau of Prisons (BOP) during fiscal year 2004. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24183.v2",
+                    "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2004"
+                }
+            ],
+            "identifier": "984",
+            "isPartOf": "2174",
+            "issued": "2009-02-05T11:09:21",
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
+            "modified": "2011-03-08T11:37:05",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-05T11:09:21",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24183.v2",
-                    "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2004"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2005",
-            "description": "The data contain records of sentenced offenders committed to the custody of the Bureau of Prisons (BOP) during fiscal year 2005. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:46:40",
-            "accessLevel": "restricted public",
-            "identifier": "985",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2004"
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
+            "description": "The data contain records of sentenced offenders committed to the custody of the Bureau of Prisons (BOP) during fiscal year 2005. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24201.v2",
+                    "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2005"
+                }
+            ],
+            "identifier": "985",
+            "isPartOf": "2174",
+            "issued": "2009-02-05T11:14:16",
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
+            "modified": "2011-03-08T11:46:40",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-05T11:14:16",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24201.v2",
-                    "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2005"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2006",
-            "description": "The data contain records of sentenced offenders committed to the custody of the Bureau of Prisons (BOP) during fiscal year 2006. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:55:15",
-            "accessLevel": "restricted public",
-            "identifier": "986",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2005"
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
+            "description": "The data contain records of sentenced offenders committed to the custody of the Bureau of Prisons (BOP) during fiscal year 2006. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24218.v2",
+                    "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2006"
+                }
+            ],
+            "identifier": "986",
+            "isPartOf": "2174",
+            "issued": "2009-02-05T11:16:41",
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
+            "modified": "2011-03-08T11:55:15",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-05T11:16:41",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24218.v2",
-                    "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2006"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2007",
-            "description": "The data contain records of sentenced offenders committed to the custody of the Bureau of Prisons (BOP) during fiscal year 2007. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T12:03:48",
-            "accessLevel": "restricted public",
-            "identifier": "987",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2006"
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
+            "description": "The data contain records of sentenced offenders committed to the custody of the Bureau of Prisons (BOP) during fiscal year 2007. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24233.v2",
+                    "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2007"
+                }
+            ],
+            "identifier": "987",
+            "isPartOf": "2174",
+            "issued": "2009-02-05T11:19:06",
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
+            "modified": "2011-03-08T12:03:48",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-05T11:19:06",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24233.v2",
-                    "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2007"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2008",
-            "description": "The data contain records of sentenced offenders committed to the custody of the Bureau of Prisons (BOP) during fiscal year 2008. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T12:10:41",
-            "accessLevel": "restricted public",
-            "identifier": "988",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2007"
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
+            "description": "The data contain records of sentenced offenders committed to the custody of the Bureau of Prisons (BOP) during fiscal year 2008. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR29404.v2",
+                    "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2008"
+                }
+            ],
+            "identifier": "988",
+            "isPartOf": "2174",
+            "issued": "2011-02-04T10:42:35",
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
+            "modified": "2011-03-08T12:10:41",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2011-02-04T10:42:35",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR29404.v2",
-                    "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2008"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2009",
-            "description": "The data contain records of sentenced offenders committed to the custody of the Bureau of Prisons (BOP) during fiscal year 2009. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-06-03T15:45:11",
-            "accessLevel": "restricted public",
-            "identifier": "989",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2008"
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
+            "description": "The data contain records of sentenced offenders committed to the custody of the Bureau of Prisons (BOP) during fiscal year 2009. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR30785.v1",
+                    "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2009"
+                }
+            ],
+            "identifier": "989",
+            "isPartOf": "2174",
+            "issued": "2011-06-03T15:43:02",
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
+            "modified": "2011-06-03T15:45:11",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2011-06-03T15:43:02",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR30785.v1",
-                    "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2009"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2010",
-            "description": "The data contain records of sentenced offenders committed to the custody of the Bureau of Prisons (BOP) during fiscal year 2010. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2013-01-07T10:16:04",
-            "accessLevel": "restricted public",
-            "identifier": "990",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2009"
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
+            "description": "The data contain records of sentenced offenders committed to the custody of the Bureau of Prisons (BOP) during fiscal year 2010. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR34327.v1",
+                    "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2010"
+                }
+            ],
+            "identifier": "990",
+            "isPartOf": "2174",
+            "issued": "2013-01-07T10:11:09",
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
+            "modified": "2013-01-07T10:16:04",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2013-01-07T10:11:09",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR34327.v1",
-                    "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2010"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 1994 [United States]",
-            "description": "The data contain records of sentenced offenders in the custody of the Bureau of Prisons (BOP) at year-end of fiscal year 1994. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T09:52:09",
-            "accessLevel": "restricted public",
-            "identifier": "991",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Offenders Admitted to Prison, 2010"
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
+            "description": "The data contain records of sentenced offenders in the custody of the Bureau of Prisons (BOP) at year-end of fiscal year 1994. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR23767.v2",
+                    "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 1994 [United States]"
+                }
+            ],
+            "identifier": "991",
+            "isPartOf": "2174",
+            "issued": "2009-02-06T08:56:17",
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
+            "modified": "2011-03-08T09:52:09",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-06T08:56:17",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR23767.v2",
-                    "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 1994 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 1995 [United States]",
-            "description": "The data contain records of sentenced offenders in the custody of the Bureau of Prisons (BOP) at year-end of fiscal year 1995. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:03:43",
-            "accessLevel": "restricted public",
-            "identifier": "992",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 1994 [United States]"
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
+            "description": "The data contain records of sentenced offenders in the custody of the Bureau of Prisons (BOP) at year-end of fiscal year 1995. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24018.v2",
+                    "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 1995 [United States]"
+                }
+            ],
+            "identifier": "992",
+            "isPartOf": "2174",
+            "issued": "2009-02-06T09:05:33",
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
+            "modified": "2011-03-08T10:03:43",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-06T09:05:33",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24018.v2",
-                    "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 1995 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 1996 [United States]",
-            "description": "The data contain records of sentenced offenders in the custody of the Bureau of Prisons (BOP) at year-end of fiscal year 1996. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:14:10",
-            "accessLevel": "restricted public",
-            "identifier": "993",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 1995 [United States]"
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
+            "description": "The data contain records of sentenced offenders in the custody of the Bureau of Prisons (BOP) at year-end of fiscal year 1996. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24037.v2",
+                    "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 1996 [United States]"
+                }
+            ],
+            "identifier": "993",
+            "isPartOf": "2174",
+            "issued": "2009-02-06T09:10:08",
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
+            "modified": "2011-03-08T10:14:10",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-06T09:10:08",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24037.v2",
-                    "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 1996 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 1997 [United States]",
-            "description": "The data contain records of sentenced offenders in the custody of the Bureau of Prisons (BOP) at year-end of fiscal year 1997. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:27:31",
-            "accessLevel": "restricted public",
-            "identifier": "994",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 1996 [United States]"
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
+            "description": "The data contain records of sentenced offenders in the custody of the Bureau of Prisons (BOP) at year-end of fiscal year 1997. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24056.v2",
+                    "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 1997 [United States]"
+                }
+            ],
+            "identifier": "994",
+            "isPartOf": "2174",
+            "issued": "2009-02-10T09:05:45",
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
+            "modified": "2011-03-08T10:27:31",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-10T09:05:45",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24056.v2",
-                    "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 1997 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 1998",
```

