# Change History for justice.json (Part 4)

### Changes from acf49f0 to dd2190f (Part 4/22)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
-            "description": "The data contain records of sentenced offenders in the custody of the Bureau of Prisons (BOP) at year-end of fiscal year 1998. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2014-03-10T21:49:15",
-            "accessLevel": "restricted public",
-            "identifier": "995",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 1997 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of sentenced offenders in the custody of the Bureau of Prisons (BOP) at year-end of fiscal year 1998. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24075.v3",
+                    "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 1998"
+                }
+            ],
+            "identifier": "995",
+            "isPartOf": "2174",
+            "issued": "2009-02-06T09:15:18",
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
+            "modified": "2014-03-10T21:49:15",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-06T09:15:18",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24075.v3",
-                    "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 1998"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 1999",
-            "description": "The data contain records of sentenced offenders in the custody of the Bureau of Prisons (BOP) at year-end of fiscal year 1999. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2014-03-10T21:47:05",
-            "accessLevel": "restricted public",
-            "identifier": "996",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 1998"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of sentenced offenders in the custody of the Bureau of Prisons (BOP) at year-end of fiscal year 1999. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24094.v3",
+                    "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 1999"
+                }
+            ],
+            "identifier": "996",
+            "isPartOf": "2174",
+            "issued": "2009-02-10T09:09:30",
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
+            "modified": "2014-03-10T21:47:05",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-10T09:09:30",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24094.v3",
-                    "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 1999"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 2000",
-            "description": "The data contain records of sentenced offenders in the custody of the Bureau of Prisons (BOP) at year-end of fiscal year 2000. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2014-03-10T21:45:04",
-            "accessLevel": "restricted public",
-            "identifier": "997",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 1999"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of sentenced offenders in the custody of the Bureau of Prisons (BOP) at year-end of fiscal year 2000. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24113.v3",
+                    "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 2000"
+                }
+            ],
+            "identifier": "997",
+            "isPartOf": "2174",
+            "issued": "2009-02-06T09:20:24",
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
+            "modified": "2014-03-10T21:45:04",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-06T09:20:24",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24113.v3",
-                    "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 2000"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 2001",
-            "description": "The data contain records of sentenced offenders in the custody of the Bureau of Prisons (BOP) at year-end of fiscal year 2001. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2014-03-10T21:43:06",
-            "accessLevel": "restricted public",
-            "identifier": "998",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 2000"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of sentenced offenders in the custody of the Bureau of Prisons (BOP) at year-end of fiscal year 2001. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24132.v3",
+                    "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 2001"
+                }
+            ],
+            "identifier": "998",
+            "isPartOf": "2174",
+            "issued": "2009-02-06T09:24:10",
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
+            "modified": "2014-03-10T21:43:06",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-06T09:24:10",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24132.v3",
-                    "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 2001"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 2002",
-            "description": "The data contain records of sentenced offenders in the custody of the Bureau of Prisons (BOP) at year-end of fiscal year 2002. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2014-03-10T21:40:49",
-            "accessLevel": "restricted public",
-            "identifier": "999",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 2001"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of sentenced offenders in the custody of the Bureau of Prisons (BOP) at year-end of fiscal year 2002. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24151.v3",
+                    "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 2002"
+                }
+            ],
+            "identifier": "999",
+            "isPartOf": "2174",
+            "issued": "2009-02-06T09:30:01",
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
+            "modified": "2014-03-10T21:40:49",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-06T09:30:01",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24151.v3",
-                    "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 2002"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 2003",
-            "description": "The data contain records of sentenced offenders in the custody of the Bureau of Prisons (BOP) at year-end of fiscal year 2003. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2014-03-10T21:36:37",
-            "accessLevel": "restricted public",
-            "identifier": "1000",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 2002"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of sentenced offenders in the custody of the Bureau of Prisons (BOP) at year-end of fiscal year 2003. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24168.v3",
+                    "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 2003"
+                }
+            ],
+            "identifier": "1000",
+            "isPartOf": "2174",
+            "issued": "2009-02-06T09:35:49",
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
+            "modified": "2014-03-10T21:36:37",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-06T09:35:49",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24168.v3",
-                    "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 2003"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 2004",
-            "description": "The data contain records of sentenced offenders in the custody of the Bureau of Prisons (BOP) at year-end of fiscal year 2004. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2014-03-10T21:31:37",
-            "accessLevel": "restricted public",
-            "identifier": "1001",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 2003"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of sentenced offenders in the custody of the Bureau of Prisons (BOP) at year-end of fiscal year 2004. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24185.v3",
+                    "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 2004"
+                }
+            ],
+            "identifier": "1001",
+            "isPartOf": "2174",
+            "issued": "2009-02-06T09:39:46",
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
+            "modified": "2014-03-10T21:31:37",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-06T09:39:46",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24185.v3",
-                    "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 2004"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 2005",
-            "description": "The data contain records of sentenced offenders in the custody of the Bureau of Prisons (BOP) at year-end of fiscal year 2005. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2014-03-10T21:27:45",
-            "accessLevel": "restricted public",
-            "identifier": "1002",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 2004"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of sentenced offenders in the custody of the Bureau of Prisons (BOP) at year-end of fiscal year 2005. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24203.v3",
+                    "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 2005"
+                }
+            ],
+            "identifier": "1002",
+            "isPartOf": "2174",
+            "issued": "2009-02-06T09:43:03",
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
+            "modified": "2014-03-10T21:27:45",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-06T09:43:03",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24203.v3",
-                    "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 2005"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 2006",
-            "description": "The data contain records of sentenced offenders in the custody of the Bureau of Prisons (BOP) at year-end of fiscal year 2006. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2014-03-10T21:25:27",
-            "accessLevel": "restricted public",
-            "identifier": "1003",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 2005"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of sentenced offenders in the custody of the Bureau of Prisons (BOP) at year-end of fiscal year 2006. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24220.v3",
+                    "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 2006"
+                }
+            ],
+            "identifier": "1003",
+            "isPartOf": "2174",
+            "issued": "2009-02-06T09:47:07",
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
+            "modified": "2014-03-10T21:25:27",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-06T09:47:07",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24220.v3",
-                    "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 2006"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 2007",
-            "description": "The data contain records of sentenced offenders in the custody of the Bureau of Prisons (BOP) at year-end of fiscal year 2007. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2014-03-10T21:22:49",
-            "accessLevel": "restricted public",
-            "identifier": "1004",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 2006"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of sentenced offenders in the custody of the Bureau of Prisons (BOP) at year-end of fiscal year 2007. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24235.v3",
+                    "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 2007"
+                }
+            ],
+            "identifier": "1004",
+            "isPartOf": "2174",
+            "issued": "2009-02-06T14:29:00",
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
+            "modified": "2014-03-10T21:22:49",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-06T14:29:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24235.v3",
-                    "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 2007"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 2008",
-            "description": "The data contain records of sentenced offenders in the custody of the Bureau of Prisons (BOP) at year-end of fiscal year 2008. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2014-03-11T12:09:41",
-            "accessLevel": "restricted public",
-            "identifier": "1005",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 2007"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of sentenced offenders in the custody of the Bureau of Prisons (BOP) at year-end of fiscal year 2008. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR29406.v3",
+                    "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 2008"
+                }
+            ],
+            "identifier": "1005",
+            "isPartOf": "2174",
+            "issued": "2011-02-04T09:20:30",
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
+            "modified": "2014-03-11T12:09:41",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2011-02-04T09:20:30",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR29406.v3",
-                    "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 2008"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Offenders Released From Prison, 1994 [United States]",
-            "description": "The data contain records of sentenced offenders released from the custody of the Bureau of Prisons (BOP) during fiscal year 1994. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. Records of offenders who exit federal prison temporarily, such as for transit to another location, to serve a weekend sentence, or for health care, are not included in the exiting cohort. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T09:51:35",
-            "accessLevel": "restricted public",
-            "identifier": "1006",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 2008"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of sentenced offenders released from the custody of the Bureau of Prisons (BOP) during fiscal year 1994. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. Records of offenders who exit federal prison temporarily, such as for transit to another location, to serve a weekend sentence, or for health care, are not included in the exiting cohort. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR23766.v2",
+                    "title": "Federal Justice Statistics Program: Offenders Released From Prison, 1994 [United States]"
+                }
+            ],
+            "identifier": "1006",
+            "isPartOf": "2174",
+            "issued": "2009-02-05T11:21:55",
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
+            "modified": "2011-03-08T09:51:35",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-05T11:21:55",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR23766.v2",
-                    "title": "Federal Justice Statistics Program: Offenders Released From Prison, 1994 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Offenders Released From Prison, 1995",
-            "description": "The data contain records of sentenced offenders released from the custody of the Bureau of Prisons (BOP) during fiscal year 1995. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. Records of offenders who exit federal prison temporarily, such as for transit to another location, to serve a weekend sentence, or for health care, are not included in the exiting cohort. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:03:11",
-            "accessLevel": "restricted public",
-            "identifier": "1007",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Federal Justice Statistics Program: Offenders Released From Prison, 1994 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of sentenced offenders released from the custody of the Bureau of Prisons (BOP) during fiscal year 1995. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. Records of offenders who exit federal prison temporarily, such as for transit to another location, to serve a weekend sentence, or for health care, are not included in the exiting cohort. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24017.v2",
+                    "title": "Federal Justice Statistics Program: Offenders Released From Prison, 1995"
+                }
+            ],
+            "identifier": "1007",
+            "isPartOf": "2174",
+            "issued": "2009-02-05T11:28:29",
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
+            "modified": "2011-03-08T10:03:11",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-05T11:28:29",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24017.v2",
-                    "title": "Federal Justice Statistics Program: Offenders Released From Prison, 1995"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Offenders Released From Prison, 1996",
-            "description": "The data contain records of sentenced offenders released from the custody of the Bureau of Prisons (BOP) during fiscal year 1996. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. Records of offenders who exit federal prison temporarily, such as for transit to another location, to serve a weekend sentence, or for health care, are not included in the exiting cohort. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:13:36",
-            "accessLevel": "restricted public",
-            "identifier": "1008",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Federal Justice Statistics Program: Offenders Released From Prison, 1995"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of sentenced offenders released from the custody of the Bureau of Prisons (BOP) during fiscal year 1996. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. Records of offenders who exit federal prison temporarily, such as for transit to another location, to serve a weekend sentence, or for health care, are not included in the exiting cohort. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24036.v2",
+                    "title": "Federal Justice Statistics Program: Offenders Released From Prison, 1996"
+                }
+            ],
+            "identifier": "1008",
+            "isPartOf": "2174",
+            "issued": "2009-02-05T11:32:15",
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
+            "modified": "2011-03-08T10:13:36",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-05T11:32:15",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24036.v2",
-                    "title": "Federal Justice Statistics Program: Offenders Released From Prison, 1996"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Offenders Released From Prison, 1997",
-            "description": "The data contain records of sentenced offenders released from the custody of the Bureau of Prisons (BOP) during fiscal year 1997. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. Records of offenders who exit federal prison temporarily, such as for transit to another location, to serve a weekend sentence, or for health care, are not included in the exiting cohort. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:24:19",
-            "accessLevel": "restricted public",
-            "identifier": "1009",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Federal Justice Statistics Program: Offenders Released From Prison, 1996"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of sentenced offenders released from the custody of the Bureau of Prisons (BOP) during fiscal year 1997. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. Records of offenders who exit federal prison temporarily, such as for transit to another location, to serve a weekend sentence, or for health care, are not included in the exiting cohort. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24055.v2",
+                    "title": "Federal Justice Statistics Program: Offenders Released From Prison, 1997"
+                }
+            ],
+            "identifier": "1009",
+            "isPartOf": "2174",
+            "issued": "2009-02-05T11:34:28",
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
+            "modified": "2011-03-08T10:24:19",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-05T11:34:28",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24055.v2",
-                    "title": "Federal Justice Statistics Program: Offenders Released From Prison, 1997"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Paired-Agency Linked Files, 1994-2018",
-            "description": "The new FJSRC linking system, implemented with the 2008\r\nFJSRC data, includes sets of agency dyad linked files\r\ncreated by improved methods of algorithmic matching.  There\r\nare both inter-agency linked files and intra-agency dyad\r\nlinked files.\r\nThe inter-agency matched pair files (or \"dyads\") permit\r\nthe linking of records from two different source agencies\r\nfor adjacent stages of federal case processing by providing\r\na crosswalk of the agency-specific key ID variables for the\r\ntwo agency data files in the pair.  These agency ID\r\nvariables (sequential ID numbers) may be used to link\r\nrecords from one agency's standard analysis file (SAF) to\r\nthe next. The system enables users to track individual\r\ndefendant-cases through stages of the federal criminal\r\njustice system (from arrest to prosecution, adjudication,\r\nsentencing, and corrections) sequentially, one agency dyad\r\npair at a time.  Each inter-agency paired linked file\r\nrelates the sequential record numbers (i.e. SEQ_NUM)\r\nincluded in the SAFs from one agency/stage to another.\r\nThe intra-agency matched pair files (also dyads) permit\r\nthe same type of linking as described above except that the\r\nlinkages are within the same federal agency. The linkages\r\nare to different stages of case processing withing a\r\nparticular agency.\r\nThe system covers all data years from 1994-2018.\r\nThese data are part of a series designed by the Urban\r\nInstitute (Washington, D.C.)  and the Bureau of Justice\r\nStatistics. Data and documentation were prepared by the\r\nUrban Institute through 2012. Data from 2013 and on were prepared by Abt Associates.",
-            "modified": "2022-06-23T14:35:52",
-            "accessLevel": "restricted public",
-            "identifier": "1010",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Federal Justice Statistics Program: Offenders Released From Prison, 1997"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The new FJSRC linking system, implemented with the 2008\r\nFJSRC data, includes sets of agency dyad linked files\r\ncreated by improved methods of algorithmic matching.  There\r\nare both inter-agency linked files and intra-agency dyad\r\nlinked files.\r\nThe inter-agency matched pair files (or \"dyads\") permit\r\nthe linking of records from two different source agencies\r\nfor adjacent stages of federal case processing by providing\r\na crosswalk of the agency-specific key ID variables for the\r\ntwo agency data files in the pair.  These agency ID\r\nvariables (sequential ID numbers) may be used to link\r\nrecords from one agency's standard analysis file (SAF) to\r\nthe next. The system enables users to track individual\r\ndefendant-cases through stages of the federal criminal\r\njustice system (from arrest to prosecution, adjudication,\r\nsentencing, and corrections) sequentially, one agency dyad\r\npair at a time.  Each inter-agency paired linked file\r\nrelates the sequential record numbers (i.e. SEQ_NUM)\r\nincluded in the SAFs from one agency/stage to another.\r\nThe intra-agency matched pair files (also dyads) permit\r\nthe same type of linking as described above except that the\r\nlinkages are within the same federal agency. The linkages\r\nare to different stages of case processing withing a\r\nparticular agency.\r\nThe system covers all data years from 1994-2018.\r\nThese data are part of a series designed by the Urban\r\nInstitute (Washington, D.C.)  and the Bureau of Justice\r\nStatistics. Data and documentation were prepared by the\r\nUrban Institute through 2012. Data from 2013 and on were prepared by Abt Associates.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR30701.v10",
+                    "title": "Federal Justice Statistics Program: Paired-Agency Linked Files, 1994-2018"
+                }
+            ],
+            "identifier": "1010",
+            "isPartOf": "2174",
+            "issued": "2011-06-14T17:11:28",
             "keyword": [
                 "case processing",
                 "federal courts",
                 "federal offenses"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2022-06-23T14:35:52",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2011-06-14T17:11:28",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR30701.v10",
-                    "title": "Federal Justice Statistics Program: Paired-Agency Linked Files, 1994-2018"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Statutes for Counts of Conviction for Defendants Sentenced Under the Sentencing Reform Act, 1999 [United States]",
-            "description": "These data contain records of statutes for each count of conviction for criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 1999. The data are one of two supplementary files that should be used in conjunction with the primary analysis file, which contains records for all defendants sentenced under the guidelines. These data can be linked to the primary analysis file using the unique identifier variable USSCIDN. The number of records for a defendant in the current data corresponds to the total number of counts of conviction for that defendant, and that total is recorded in the NOCOUNT variable. As an example, if a defendant has five counts of conviction (NOCOUNT=5), he or she will have five records in the current data. As it is possible for defendants to have multiple statutes applying to a single count of conviction, up to three statutes (STA1 - STA3) are recorded for each count of conviction. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T09:49:53",
-            "accessLevel": "restricted public",
-            "identifier": "1011",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Federal Justice Statistics Program: Paired-Agency Linked Files, 1994-2018"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "These data contain records of statutes for each count of conviction for criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 1999. The data are one of two supplementary files that should be used in conjunction with the primary analysis file, which contains records for all defendants sentenced under the guidelines. These data can be linked to the primary analysis file using the unique identifier variable USSCIDN. The number of records for a defendant in the current data corresponds to the total number of counts of conviction for that defendant, and that total is recorded in the NOCOUNT variable. As an example, if a defendant has five counts of conviction (NOCOUNT=5), he or she will have five records in the current data. As it is possible for defendants to have multiple statutes applying to a single count of conviction, up to three statutes (STA1 - STA3) are recorded for each count of conviction. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR23763.v2",
+                    "title": "Federal Justice Statistics Program: Statutes for Counts of Conviction for Defendants Sentenced Under the Sentencing Reform Act, 1999 [United States]"
+                }
+            ],
+            "identifier": "1011",
+            "isPartOf": "2174",
+            "issued": "2009-02-03T14:34:41",
             "keyword": [
                 "administration",
                 "court cases",
@@ -30724,55 +30718,55 @@
                 "sentencing guidelines",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T09:49:53",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-03T14:34:41",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR23763.v2",
-                    "title": "Federal Justice Statistics Program: Statutes for Counts of Conviction for Defendants Sentenced Under the Sentencing Reform Act, 1999 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Statutes for Counts of Conviction for Defendants Sentenced Under the Sentencing Reform Act, 2000 [United States]",
-            "description": "These data contain records of statutes for each count of conviction for criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2000. The data are one of two supplementary files that should be used in conjunction with the primary analysis file, which contains records for all defendants sentenced under the guidelines. These data can be linked to the primary analysis file using the unique identifier variable USSCIDN. The number of records for a defendant in the current data corresponds to the total number of counts of conviction for that defendant, and that total is recorded in the NOCOUNT variable. As an example, if a defendant has five counts of conviction (NOCOUNT=5), he or she will have five records in the current data. As it is possible for defendants to have multiple statutes applying to a single count of conviction, up to three statutes (STA1 - STA3) are recorded for each count of conviction. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:01:34",
-            "accessLevel": "restricted public",
-            "identifier": "1012",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Federal Justice Statistics Program: Statutes for Counts of Conviction for Defendants Sentenced Under the Sentencing Reform Act, 1999 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "These data contain records of statutes for each count of conviction for criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2000. The data are one of two supplementary files that should be used in conjunction with the primary analysis file, which contains records for all defendants sentenced under the guidelines. These data can be linked to the primary analysis file using the unique identifier variable USSCIDN. The number of records for a defendant in the current data corresponds to the total number of counts of conviction for that defendant, and that total is recorded in the NOCOUNT variable. As an example, if a defendant has five counts of conviction (NOCOUNT=5), he or she will have five records in the current data. As it is possible for defendants to have multiple statutes applying to a single count of conviction, up to three statutes (STA1 - STA3) are recorded for each count of conviction. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24014.v2",
+                    "title": "Federal Justice Statistics Program: Statutes for Counts of Conviction for Defendants Sentenced Under the Sentencing Reform Act, 2000 [United States]"
+                }
+            ],
+            "identifier": "1012",
+            "isPartOf": "2174",
+            "issued": "2009-02-03T14:37:46",
             "keyword": [
                 "administration",
                 "court cases",
@@ -30784,55 +30778,55 @@
                 "sentencing guidelines",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:01:34",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-03T14:37:46",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24014.v2",
-                    "title": "Federal Justice Statistics Program: Statutes for Counts of Conviction for Defendants Sentenced Under the Sentencing Reform Act, 2000 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Statutes for Counts of Conviction for Defendants Sentenced Under the Sentencing Reform Act, 2001 [United States]",
-            "description": "These data contain records of statutes for each count of conviction for criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2001. The data are one of two supplementary files that should be used in conjunction with the primary analysis file, which contains records for all defendants sentenced under the guidelines. These data can be linked to the primary analysis file using the unique identifier variable USSCIDN. The number of records for a defendant in the current data corresponds to the total number of counts of conviction for that defendant, and that total is recorded in the NOCOUNT variable. As an example, if a defendant has five counts of conviction (NOCOUNT=5), he or she will have five records in the current data. As it is possible for defendants to have multiple statutes applying to a single count of conviction, up to three statutes (STA1 - STA3) are recorded for each count of conviction. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:11:46",
-            "accessLevel": "restricted public",
-            "identifier": "1013",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Federal Justice Statistics Program: Statutes for Counts of Conviction for Defendants Sentenced Under the Sentencing Reform Act, 2000 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "These data contain records of statutes for each count of conviction for criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2001. The data are one of two supplementary files that should be used in conjunction with the primary analysis file, which contains records for all defendants sentenced under the guidelines. These data can be linked to the primary analysis file using the unique identifier variable USSCIDN. The number of records for a defendant in the current data corresponds to the total number of counts of conviction for that defendant, and that total is recorded in the NOCOUNT variable. As an example, if a defendant has five counts of conviction (NOCOUNT=5), he or she will have five records in the current data. As it is possible for defendants to have multiple statutes applying to a single count of conviction, up to three statutes (STA1 - STA3) are recorded for each count of conviction. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24033.v2",
+                    "title": "Federal Justice Statistics Program: Statutes for Counts of Conviction for Defendants Sentenced Under the Sentencing Reform Act, 2001 [United States]"
+                }
+            ],
+            "identifier": "1013",
+            "isPartOf": "2174",
+            "issued": "2009-02-03T14:41:21",
             "keyword": [
                 "administration",
                 "court cases",
@@ -30844,55 +30838,55 @@
                 "sentencing guidelines",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:11:46",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-03T14:41:21",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24033.v2",
-                    "title": "Federal Justice Statistics Program: Statutes for Counts of Conviction for Defendants Sentenced Under the Sentencing Reform Act, 2001 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Statutes for Counts of Conviction for Defendants Sentenced Under the Sentencing Reform Act, 2002 [United States]",
-            "description": "These data contain records of statutes for each count of conviction for criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2002. The data are one of two supplementary files that should be used in conjunction with the primary analysis file, which contains records for all defendants sentenced under the guidelines. These data can be linked to the primary analysis file using the unique identifier variable USSCIDN. The number of records for a defendant in the current data corresponds to the total number of counts of conviction for that defendant, and that total is recorded in the NOCOUNT variable. As an example, if a defendant has five counts of conviction (NOCOUNT=5), he or she will have five records in the current data. As it is possible for defendants to have multiple statutes applying to a single count of conviction, up to three statutes (STA1 - STA3) are recorded for each count of conviction. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:22:37",
-            "accessLevel": "restricted public",
-            "identifier": "1014",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Federal Justice Statistics Program: Statutes for Counts of Conviction for Defendants Sentenced Under the Sentencing Reform Act, 2001 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "These data contain records of statutes for each count of conviction for criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2002. The data are one of two supplementary files that should be used in conjunction with the primary analysis file, which contains records for all defendants sentenced under the guidelines. These data can be linked to the primary analysis file using the unique identifier variable USSCIDN. The number of records for a defendant in the current data corresponds to the total number of counts of conviction for that defendant, and that total is recorded in the NOCOUNT variable. As an example, if a defendant has five counts of conviction (NOCOUNT=5), he or she will have five records in the current data. As it is possible for defendants to have multiple statutes applying to a single count of conviction, up to three statutes (STA1 - STA3) are recorded for each count of conviction. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24052.v2",
+                    "title": "Federal Justice Statistics Program: Statutes for Counts of Conviction for Defendants Sentenced Under the Sentencing Reform Act, 2002 [United States]"
+                }
+            ],
+            "identifier": "1014",
+            "isPartOf": "2174",
+            "issued": "2009-02-03T14:44:37",
             "keyword": [
                 "administration",
                 "court cases",
@@ -30904,55 +30898,55 @@
                 "sentencing guidelines",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:22:37",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-03T14:44:37",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24052.v2",
-                    "title": "Federal Justice Statistics Program: Statutes for Counts of Conviction for Defendants Sentenced Under the Sentencing Reform Act, 2002 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Statutes for Counts of Conviction for Defendants Sentenced Under the Sentencing Reform Act, 2003 [United States]",
-            "description": "These data contain records of statutes for each count of conviction for criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2003. The data are one of two supplementary files that should be used in conjunction with the primary analysis file, which contains records for all defendants sentenced under the guidelines. These data can be linked to the primary analysis file using the unique identifier variable USSCIDN. The number of records for a defendant in the current data corresponds to the total number of counts of conviction for that defendant, and that total is recorded in the NOCOUNT variable. As an example, if a defendant has five counts of conviction (NOCOUNT=5), he or she will have five records in the current data. As it is possible for defendants to have multiple statutes applying to a single count of conviction, up to three statutes (STA1 - STA3) are recorded for each count of conviction. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:33:18",
-            "accessLevel": "restricted public",
-            "identifier": "1015",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Federal Justice Statistics Program: Statutes for Counts of Conviction for Defendants Sentenced Under the Sentencing Reform Act, 2002 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "These data contain records of statutes for each count of conviction for criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2003. The data are one of two supplementary files that should be used in conjunction with the primary analysis file, which contains records for all defendants sentenced under the guidelines. These data can be linked to the primary analysis file using the unique identifier variable USSCIDN. The number of records for a defendant in the current data corresponds to the total number of counts of conviction for that defendant, and that total is recorded in the NOCOUNT variable. As an example, if a defendant has five counts of conviction (NOCOUNT=5), he or she will have five records in the current data. As it is possible for defendants to have multiple statutes applying to a single count of conviction, up to three statutes (STA1 - STA3) are recorded for each count of conviction. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24071.v2",
+                    "title": "Federal Justice Statistics Program: Statutes for Counts of Conviction for Defendants Sentenced Under the Sentencing Reform Act, 2003 [United States]"
+                }
+            ],
+            "identifier": "1015",
+            "isPartOf": "2174",
+            "issued": "2009-02-03T14:47:08",
             "keyword": [
                 "administration",
                 "court cases",
@@ -30964,55 +30958,55 @@
                 "sentencing guidelines",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:33:18",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-03T14:47:08",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24071.v2",
-                    "title": "Federal Justice Statistics Program: Statutes for Counts of Conviction for Defendants Sentenced Under the Sentencing Reform Act, 2003 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Statutes for Counts of Convictions for Defendants Sentenced Under the Sentencing Reform Act, 2004",
-            "description": "These data contain records of statutes for each count of conviction for criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2004. The data are one of two supplementary files that should be used in conjunction with the primary analysis file, which contains records for all defendants sentenced under the guidelines. These data can be linked to the primary analysis file using the unique identifier variable USSCIDN. The number of records for a defendant in the current data corresponds to the total number of counts of conviction for that defendant, and that total is recorded in the NOCOUNT variable. As an example, if a defendant has five counts of conviction (NOCOUNT=5), he or she will have five records in the current data. As it is possible for defendants to have multiple statutes applying to a single count of conviction, up to three statutes (STA1 - STA3) are recorded for each count of conviction. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:44:15",
-            "accessLevel": "restricted public",
-            "identifier": "1016",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Federal Justice Statistics Program: Statutes for Counts of Conviction for Defendants Sentenced Under the Sentencing Reform Act, 2003 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "These data contain records of statutes for each count of conviction for criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2004. The data are one of two supplementary files that should be used in conjunction with the primary analysis file, which contains records for all defendants sentenced under the guidelines. These data can be linked to the primary analysis file using the unique identifier variable USSCIDN. The number of records for a defendant in the current data corresponds to the total number of counts of conviction for that defendant, and that total is recorded in the NOCOUNT variable. As an example, if a defendant has five counts of conviction (NOCOUNT=5), he or she will have five records in the current data. As it is possible for defendants to have multiple statutes applying to a single count of conviction, up to three statutes (STA1 - STA3) are recorded for each count of conviction. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24090.v2",
+                    "title": "Federal Justice Statistics Program: Statutes for Counts of Convictions for Defendants Sentenced Under the Sentencing Reform Act, 2004"
+                }
+            ],
+            "identifier": "1016",
+            "isPartOf": "2174",
+            "issued": "2009-02-03T14:52:20",
             "keyword": [
                 "administration",
                 "court cases",
@@ -31024,55 +31018,55 @@
                 "sentencing guidelines",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:44:15",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-03T14:52:20",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24090.v2",
-                    "title": "Federal Justice Statistics Program: Statutes for Counts of Convictions for Defendants Sentenced Under the Sentencing Reform Act, 2004"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Statutes for Counts of Convictions for Defendants Sentenced Under the Sentencing Reform Act, 2005",
-            "description": "These data contain records of statutes for each count of conviction for criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2005. The data are one of two supplementary files that should be used in conjunction with the primary analysis file, which contains records for all defendants sentenced under the guidelines. These data can be linked to the primary analysis file using the unique identifier variable USSCIDN. The number of records for a defendant in the current data corresponds to the total number of counts of conviction for that defendant, and that total is recorded in the NOCOUNT variable. As an example, if a defendant has five counts of conviction (NOCOUNT=5), he or she will have five records in the current data. As it is possible for defendants to have multiple statutes applying to a single count of conviction, up to three statutes (STA1 - STA3) are recorded for each count of conviction. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:55:02",
-            "accessLevel": "restricted public",
-            "identifier": "1017",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Federal Justice Statistics Program: Statutes for Counts of Convictions for Defendants Sentenced Under the Sentencing Reform Act, 2004"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "These data contain records of statutes for each count of conviction for criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2005. The data are one of two supplementary files that should be used in conjunction with the primary analysis file, which contains records for all defendants sentenced under the guidelines. These data can be linked to the primary analysis file using the unique identifier variable USSCIDN. The number of records for a defendant in the current data corresponds to the total number of counts of conviction for that defendant, and that total is recorded in the NOCOUNT variable. As an example, if a defendant has five counts of conviction (NOCOUNT=5), he or she will have five records in the current data. As it is possible for defendants to have multiple statutes applying to a single count of conviction, up to three statutes (STA1 - STA3) are recorded for each count of conviction. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24109.v2",
+                    "title": "Federal Justice Statistics Program: Statutes for Counts of Convictions for Defendants Sentenced Under the Sentencing Reform Act, 2005"
+                }
+            ],
+            "identifier": "1017",
+            "isPartOf": "2174",
+            "issued": "2009-02-03T14:56:14",
             "keyword": [
                 "administration",
                 "court cases",
@@ -31084,55 +31078,55 @@
                 "sentencing guidelines",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:55:02",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-03T14:56:14",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24109.v2",
-                    "title": "Federal Justice Statistics Program: Statutes for Counts of Convictions for Defendants Sentenced Under the Sentencing Reform Act, 2005"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Statutes for Counts of Convictions for Defendants Sentenced Under the Sentencing Reform Act, 2006",
-            "description": "These data contain records of statutes for each count of conviction for criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2006. The data are one of two supplementary files that should be used in conjunction with the primary analysis file, which contains records for all defendants sentenced under the guidelines. These data can be linked to the primary analysis file using the unique identifier variable USSCIDN. The number of records for a defendant in the current data corresponds to the total number of counts of conviction for that defendant, and that total is recorded in the NOCOUNT variable. As an example, if a defendant has five counts of conviction (NOCOUNT=5), he or she will have five records in the current data. As it is possible for defendants to have multiple statutes applying to a single count of conviction, up to three statutes (STA1 - STA3) are recorded for each count of conviction. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:06:00",
-            "accessLevel": "restricted public",
-            "identifier": "1018",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Federal Justice Statistics Program: Statutes for Counts of Convictions for Defendants Sentenced Under the Sentencing Reform Act, 2005"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "These data contain records of statutes for each count of conviction for criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2006. The data are one of two supplementary files that should be used in conjunction with the primary analysis file, which contains records for all defendants sentenced under the guidelines. These data can be linked to the primary analysis file using the unique identifier variable USSCIDN. The number of records for a defendant in the current data corresponds to the total number of counts of conviction for that defendant, and that total is recorded in the NOCOUNT variable. As an example, if a defendant has five counts of conviction (NOCOUNT=5), he or she will have five records in the current data. As it is possible for defendants to have multiple statutes applying to a single count of conviction, up to three statutes (STA1 - STA3) are recorded for each count of conviction. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24128.v2",
+                    "title": "Federal Justice Statistics Program: Statutes for Counts of Convictions for Defendants Sentenced Under the Sentencing Reform Act, 2006"
+                }
+            ],
+            "identifier": "1018",
+            "isPartOf": "2174",
+            "issued": "2009-02-03T15:01:36",
             "keyword": [
                 "administration",
                 "court cases",
@@ -31144,55 +31138,55 @@
                 "sentencing guidelines",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:06:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-03T15:01:36",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24128.v2",
-                    "title": "Federal Justice Statistics Program: Statutes for Counts of Convictions for Defendants Sentenced Under the Sentencing Reform Act, 2006"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Statutes for Counts of Convictions for Defendants Sentenced Under the Sentencing Reform Act, 2007",
-            "description": "These data contain records of statutes for each count of conviction for criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2007. The data are one of two supplementary files that should be used in conjunction with the primary analysis file, which contains records for all defendants sentenced under the guidelines. These data can be linked to the primary analysis file using the unique identifier variable USSCIDN. The number of records for a defendant in the current data corresponds to the total number of counts of conviction for that defendant, and that total is recorded in the NOCOUNT variable. As an example, if a defendant has five counts of conviction (NOCOUNT=5), he or she will have five records in the current data. As it is possible for defendants to have multiple statutes applying to a single count of conviction, up to three statutes (STA1 - STA3) are recorded for each count of conviction. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:16:48",
-            "accessLevel": "restricted public",
-            "identifier": "1019",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Federal Justice Statistics Program: Statutes for Counts of Convictions for Defendants Sentenced Under the Sentencing Reform Act, 2006"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "These data contain records of statutes for each count of conviction for criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2007. The data are one of two supplementary files that should be used in conjunction with the primary analysis file, which contains records for all defendants sentenced under the guidelines. These data can be linked to the primary analysis file using the unique identifier variable USSCIDN. The number of records for a defendant in the current data corresponds to the total number of counts of conviction for that defendant, and that total is recorded in the NOCOUNT variable. As an example, if a defendant has five counts of conviction (NOCOUNT=5), he or she will have five records in the current data. As it is possible for defendants to have multiple statutes applying to a single count of conviction, up to three statutes (STA1 - STA3) are recorded for each count of conviction. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24147.v2",
+                    "title": "Federal Justice Statistics Program: Statutes for Counts of Convictions for Defendants Sentenced Under the Sentencing Reform Act, 2007"
+                }
+            ],
+            "identifier": "1019",
+            "isPartOf": "2174",
+            "issued": "2009-02-23T14:38:49",
             "keyword": [
                 "administration",
                 "court cases",
@@ -31204,55 +31198,55 @@
                 "sentencing guidelines",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:16:48",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-23T14:38:49",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24147.v2",
-                    "title": "Federal Justice Statistics Program: Statutes for Counts of Convictions for Defendants Sentenced Under the Sentencing Reform Act, 2007"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Statutes for Counts of Convictions for Defendants Sentenced Under the Sentencing Reform Act, 2008",
-            "description": "These data contain records of statutes for each count of conviction for criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2008. The data are one of two supplementary files that should be used in conjunction with the primary analysis file, which contains records for all defendants sentenced under the guidelines. These data can be linked to the primary analysis file using the unique identifier variable USSCIDN. The number of records for a defendant in the current data corresponds to the total number of counts of conviction for that defendant, and that total is recorded in the NOCOUNT variable. As an example, if a defendant has five counts of conviction (NOCOUNT=5), he or she will have five records in the current data. As it is possible for defendants to have multiple statutes applying to a single count of conviction, up to three statutes (STA1-STA3) are recorded for each count of conviction. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T12:15:36",
-            "accessLevel": "restricted public",
-            "identifier": "1020",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Federal Justice Statistics Program: Statutes for Counts of Convictions for Defendants Sentenced Under the Sentencing Reform Act, 2007"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "These data contain records of statutes for each count of conviction for criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2008. The data are one of two supplementary files that should be used in conjunction with the primary analysis file, which contains records for all defendants sentenced under the guidelines. These data can be linked to the primary analysis file using the unique identifier variable USSCIDN. The number of records for a defendant in the current data corresponds to the total number of counts of conviction for that defendant, and that total is recorded in the NOCOUNT variable. As an example, if a defendant has five counts of conviction (NOCOUNT=5), he or she will have five records in the current data. As it is possible for defendants to have multiple statutes applying to a single count of conviction, up to three statutes (STA1-STA3) are recorded for each count of conviction. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR29432.v2",
+                    "title": "Federal Justice Statistics Program: Statutes for Counts of Convictions for Defendants Sentenced Under the Sentencing Reform Act, 2008"
+                }
+            ],
+            "identifier": "1020",
+            "isPartOf": "2174",
+            "issued": "2011-02-08T10:22:07",
             "keyword": [
                 "administration",
                 "court cases",
@@ -31264,55 +31258,55 @@
                 "sentencing guidelines",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T12:15:36",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2011-02-08T10:22:07",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR29432.v2",
-                    "title": "Federal Justice Statistics Program: Statutes for Counts of Convictions for Defendants Sentenced Under the Sentencing Reform Act, 2008"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Statutes for Counts of Convictions for Defendants Sentenced Under the Sentencing Reform Act, 2009",
-            "description": "These data contain records of statutes for each count of conviction for criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2009. The data are one of two supplementary files that should be used in conjunction with the primary analysis file, which contains records for all defendants sentenced under the guidelines. These data can be linked to the primary analysis file using the unique identifier variable USSCIDN. The number of records for a defendant in the current data corresponds to the total number of counts of conviction for that defendant, and that total is recorded in the NOCOUNT variable. As an example, if a defendant has five counts of conviction (NOCOUNT=5), he or she will have five records in the current data. As it is possible for defendants to have multiple statutes applying to a single count of conviction, up to three statutes (STA1-STA3) are recorded for each count of conviction. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-06-06T09:28:27",
-            "accessLevel": "restricted public",
-            "identifier": "1021",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Federal Justice Statistics Program: Statutes for Counts of Convictions for Defendants Sentenced Under the Sentencing Reform Act, 2008"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "These data contain records of statutes for each count of conviction for criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2009. The data are one of two supplementary files that should be used in conjunction with the primary analysis file, which contains records for all defendants sentenced under the guidelines. These data can be linked to the primary analysis file using the unique identifier variable USSCIDN. The number of records for a defendant in the current data corresponds to the total number of counts of conviction for that defendant, and that total is recorded in the NOCOUNT variable. As an example, if a defendant has five counts of conviction (NOCOUNT=5), he or she will have five records in the current data. As it is possible for defendants to have multiple statutes applying to a single count of conviction, up to three statutes (STA1-STA3) are recorded for each count of conviction. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR30797.v1",
+                    "title": "Federal Justice Statistics Program: Statutes for Counts of Convictions for Defendants Sentenced Under the Sentencing Reform Act, 2009"
+                }
+            ],
+            "identifier": "1021",
+            "isPartOf": "2174",
+            "issued": "2011-06-06T09:27:44",
             "keyword": [
                 "administration",
                 "court cases",
@@ -31324,55 +31318,55 @@
                 "sentencing guidelines",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-06-06T09:28:27",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2011-06-06T09:27:44",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR30797.v1",
-                    "title": "Federal Justice Statistics Program: Statutes for Counts of Convictions for Defendants Sentenced Under the Sentencing Reform Act, 2009"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Statutes for Counts of Convictions for Defendants Sentenced Under the Sentencing Reform Act, 2010",
-            "description": "These data contain records of statutes for each count of conviction for criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2010. The data are one of two supplementary files that should be used in conjunction with the primary analysis file, which contains records for all defendants sentenced under the guidelines. These data can be linked to the primary analysis file using the unique identifier variable USSCIDN. The number of records for a defendant in the current data corresponds to the total number of counts of conviction for that defendant, and that total is recorded in the NOCOUNT variable. As an example, if a defendant has five counts of conviction (NOCOUNT=5), he or she will have five records in the current data. As it is possible for defendants to have multiple statutes applying to a single count of conviction, up to three statutes (STA1-STA3) are recorded for each count of conviction. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2013-01-08T12:05:14",
-            "accessLevel": "restricted public",
-            "identifier": "1022",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Federal Justice Statistics Program: Statutes for Counts of Convictions for Defendants Sentenced Under the Sentencing Reform Act, 2009"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "These data contain records of statutes for each count of conviction for criminal defendants who were sentenced pursuant to provisions of the Sentencing Reform Act (SRA) of 1984 and reported to the United States Sentencing Commission (USSC) during fiscal year 2010. The data are one of two supplementary files that should be used in conjunction with the primary analysis file, which contains records for all defendants sentenced under the guidelines. These data can be linked to the primary analysis file using the unique identifier variable USSCIDN. The number of records for a defendant in the current data corresponds to the total number of counts of conviction for that defendant, and that total is recorded in the NOCOUNT variable. As an example, if a defendant has five counts of conviction (NOCOUNT=5), he or she will have five records in the current data. As it is possible for defendants to have multiple statutes applying to a single count of conviction, up to three statutes (STA1-STA3) are recorded for each count of conviction. The data were obtained from the United States Sentencing Commission's Office of Policy Analysis' (OPA) Standardized Research Data File. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR34339.v1",
+                    "title": "Federal Justice Statistics Program: Statutes for Counts of Convictions for Defendants Sentenced Under the Sentencing Reform Act, 2010"
+                }
+            ],
+            "identifier": "1022",
+            "isPartOf": "2174",
+            "issued": "2013-01-08T12:00:22",
             "keyword": [
                 "administration",
                 "court cases",
@@ -31384,55 +31378,55 @@
                 "sentencing guidelines",
                 "trial courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-01-08T12:05:14",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2013-01-08T12:00:22",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR34339.v1",
-                    "title": "Federal Justice Statistics Program: Statutes for Counts of Convictions for Defendants Sentenced Under the Sentencing Reform Act, 2010"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 1994 [United States]",
-            "description": "The data contain records of suspects in federal criminal matters concluded by United States attorneys or United States magistrates during fiscal year 1994. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.2-1.5. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T09:45:19",
-            "accessLevel": "restricted public",
-            "identifier": "1023",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Federal Justice Statistics Program: Statutes for Counts of Convictions for Defendants Sentenced Under the Sentencing Reform Act, 2010"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of suspects in federal criminal matters concluded by United States attorneys or United States magistrates during fiscal year 1994. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.2-1.5. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR23741.v2",
+                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 1994 [United States]"
+                }
+            ],
+            "identifier": "1023",
+            "isPartOf": "2174",
+            "issued": "2009-02-12T14:29:55",
             "keyword": [
                 "defendants",
                 "federal courts",
@@ -31440,55 +31434,55 @@
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T09:45:19",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-12T14:29:55",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR23741.v2",
-                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 1994 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 1995 [United States]",
-            "description": "The data contain records of suspects in federal criminal matters concluded by United States attorneys or United States magistrates during fiscal year 1995. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.2-1.5. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T09:57:11",
-            "accessLevel": "restricted public",
-            "identifier": "1024",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 1994 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of suspects in federal criminal matters concluded by United States attorneys or United States magistrates during fiscal year 1995. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.2-1.5. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24006.v2",
+                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 1995 [United States]"
+                }
+            ],
+            "identifier": "1024",
+            "isPartOf": "2174",
+            "issued": "2009-02-12T14:32:21",
             "keyword": [
                 "defendants",
                 "federal courts",
@@ -31496,55 +31490,55 @@
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T09:57:11",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-12T14:32:21",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24006.v2",
-                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 1995 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 1996 [United States]",
-            "description": "The data contain records of suspects in federal criminal matters concluded by United States attorneys or United States magistrates during fiscal year 1996. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.2-1.5. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:07:26",
-            "accessLevel": "restricted public",
-            "identifier": "1025",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 1995 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of suspects in federal criminal matters concluded by United States attorneys or United States magistrates during fiscal year 1996. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.2-1.5. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24025.v2",
+                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 1996 [United States]"
+                }
+            ],
+            "identifier": "1025",
+            "isPartOf": "2174",
+            "issued": "2009-02-12T15:24:21",
             "keyword": [
                 "defendants",
                 "federal courts",
@@ -31552,55 +31546,55 @@
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:07:26",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-12T15:24:21",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24025.v2",
-                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 1996 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 1997 [United States]",
-            "description": "The data contain records of suspects in federal criminal matters concluded by United States attorneys or United States magistrates during fiscal year 1997. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.2-1.5. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:18:08",
-            "accessLevel": "restricted public",
-            "identifier": "1026",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 1996 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of suspects in federal criminal matters concluded by United States attorneys or United States magistrates during fiscal year 1997. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.2-1.5. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24044.v2",
+                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 1997 [United States]"
+                }
+            ],
+            "identifier": "1026",
+            "isPartOf": "2174",
+            "issued": "2009-02-12T14:36:00",
             "keyword": [
                 "defendants",
                 "federal courts",
@@ -31608,55 +31602,55 @@
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:18:08",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-12T14:36:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24044.v2",
-                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 1997 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 1998 [United States]",
-            "description": "The data contain records of suspects in federal criminal matters concluded by United States attorneys or United States magistrates during fiscal year 1998. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.2-1.5. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:28:42",
-            "accessLevel": "restricted public",
-            "identifier": "1027",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 1997 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of suspects in federal criminal matters concluded by United States attorneys or United States magistrates during fiscal year 1998. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.2-1.5. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24063.v2",
+                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 1998 [United States]"
+                }
+            ],
+            "identifier": "1027",
+            "isPartOf": "2174",
+            "issued": "2009-02-12T14:38:53",
             "keyword": [
                 "defendants",
                 "federal courts",
@@ -31664,55 +31658,55 @@
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:28:42",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-12T14:38:53",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24063.v2",
-                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 1998 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 1999 [United States]",
-            "description": "The data contain records of suspects in federal criminal matters concluded by United States attorneys or United States magistrates during fiscal year 1999. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.2-1.5. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:39:33",
-            "accessLevel": "restricted public",
-            "identifier": "1028",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 1998 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of suspects in federal criminal matters concluded by United States attorneys or United States magistrates during fiscal year 1999. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.2-1.5. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24082.v2",
+                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 1999 [United States]"
+                }
+            ],
+            "identifier": "1028",
+            "isPartOf": "2174",
+            "issued": "2009-02-12T15:17:43",
             "keyword": [
                 "defendants",
                 "federal courts",
@@ -31720,55 +31714,55 @@
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:39:33",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-12T15:17:43",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24082.v2",
-                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 1999 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2000 [United States]",
-            "description": "The data contain records of suspects in federal criminal matters concluded by United States attorneys or United States magistrates during fiscal year 2000. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.2-1.5. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:50:29",
-            "accessLevel": "restricted public",
-            "identifier": "1029",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 1999 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of suspects in federal criminal matters concluded by United States attorneys or United States magistrates during fiscal year 2000. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.2-1.5. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24101.v2",
+                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2000 [United States]"
+                }
+            ],
+            "identifier": "1029",
+            "isPartOf": "2174",
+            "issued": "2009-02-12T14:43:39",
             "keyword": [
                 "defendants",
                 "federal courts",
@@ -31776,55 +31770,55 @@
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:50:29",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-12T14:43:39",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24101.v2",
-                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2000 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2001 [United States]",
-            "description": "The data contain records of suspects in federal criminal matters concluded by United States attorneys or United States magistrates during fiscal year 2001. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.2-1.5. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:01:25",
-            "accessLevel": "restricted public",
-            "identifier": "1030",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2000 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of suspects in federal criminal matters concluded by United States attorneys or United States magistrates during fiscal year 2001. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.2-1.5. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24120.v2",
+                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2001 [United States]"
+                }
+            ],
+            "identifier": "1030",
+            "isPartOf": "2174",
+            "issued": "2009-02-12T14:46:40",
             "keyword": [
                 "defendants",
                 "federal courts",
@@ -31832,55 +31826,55 @@
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:01:25",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-12T14:46:40",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24120.v2",
-                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2001 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2002 [United States]",
-            "description": "The data contain records of suspects in federal criminal matters concluded by United States attorneys or United States magistrates during fiscal year 2002. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.2-1.5. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:12:11",
-            "accessLevel": "restricted public",
-            "identifier": "1031",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2001 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of suspects in federal criminal matters concluded by United States attorneys or United States magistrates during fiscal year 2002. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.2-1.5. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24139.v2",
+                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2002 [United States]"
+                }
+            ],
+            "identifier": "1031",
+            "isPartOf": "2174",
+            "issued": "2009-02-12T14:49:14",
             "keyword": [
                 "defendants",
                 "federal courts",
@@ -31888,55 +31882,55 @@
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:12:11",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-12T14:49:14",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24139.v2",
-                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2002 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2003 [United States]",
-            "description": "The data contain records of suspects in federal criminal matters concluded by United States attorneys or United States magistrates during fiscal year 2003. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.2-1.5. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:23:11",
-            "accessLevel": "restricted public",
-            "identifier": "1032",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2002 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of suspects in federal criminal matters concluded by United States attorneys or United States magistrates during fiscal year 2003. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.2-1.5. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24158.v2",
+                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2003 [United States]"
+                }
+            ],
+            "identifier": "1032",
+            "isPartOf": "2174",
+            "issued": "2009-02-12T14:52:00",
             "keyword": [
                 "defendants",
                 "federal courts",
@@ -31944,55 +31938,55 @@
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:23:11",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-12T14:52:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24158.v2",
-                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2003 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2004 [United States]",
-            "description": "The data contain records of suspects in federal criminal matters concluded by United States attorneys or United States magistrates during fiscal year 2004. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.2-1.5. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:32:36",
-            "accessLevel": "restricted public",
-            "identifier": "1033",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2003 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of suspects in federal criminal matters concluded by United States attorneys or United States magistrates during fiscal year 2004. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.2-1.5. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24175.v2",
+                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2004 [United States]"
+                }
+            ],
+            "identifier": "1033",
+            "isPartOf": "2174",
+            "issued": "2009-02-12T14:54:35",
             "keyword": [
                 "defendants",
                 "federal courts",
@@ -32000,55 +31994,55 @@
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:32:36",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-12T14:54:35",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24175.v2",
-                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2004 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2005 [United States]",
-            "description": "The data contain records of suspects in federal criminal matters concluded by United States attorneys or United States magistrates during fiscal year 2005. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.2-1.5. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:42:11",
-            "accessLevel": "restricted public",
-            "identifier": "1034",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2004 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of suspects in federal criminal matters concluded by United States attorneys or United States magistrates during fiscal year 2005. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.2-1.5. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24193.v2",
+                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2005 [United States]"
+                }
+            ],
+            "identifier": "1034",
+            "isPartOf": "2174",
+            "issued": "2009-02-12T14:58:59",
             "keyword": [
                 "defendants",
                 "federal courts",
@@ -32056,55 +32050,55 @@
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:42:11",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-12T14:58:59",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24193.v2",
-                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2005 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2006 [United States]",
-            "description": "The data contain records of suspects in federal criminal matters concluded by United States attorneys or United States magistrates during fiscal year 2006. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.2-1.5. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:50:36",
-            "accessLevel": "restricted public",
-            "identifier": "1035",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2005 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of suspects in federal criminal matters concluded by United States attorneys or United States magistrates during fiscal year 2006. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.2-1.5. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24210.v2",
+                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2006 [United States]"
+                }
+            ],
+            "identifier": "1035",
+            "isPartOf": "2174",
+            "issued": "2009-02-12T15:05:28",
             "keyword": [
                 "defendants",
                 "federal courts",
@@ -32112,55 +32106,55 @@
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:50:36",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-12T15:05:28",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24210.v2",
-                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2006 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2007 [United States]",
-            "description": "The data contain records of suspects in federal criminal matters concluded by United States attorneys or United States magistrates during fiscal year 2007. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.2-1.5. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:59:21",
-            "accessLevel": "restricted public",
-            "identifier": "1036",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2006 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of suspects in federal criminal matters concluded by United States attorneys or United States magistrates during fiscal year 2007. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.2-1.5. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24225.v2",
+                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2007 [United States]"
+                }
+            ],
+            "identifier": "1036",
+            "isPartOf": "2174",
+            "issued": "2009-02-19T10:50:36",
             "keyword": [
                 "defendants",
                 "federal courts",
@@ -32168,55 +32162,55 @@
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:59:21",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-19T10:50:36",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24225.v2",
-                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2007 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2008 [United States]",
-            "description": "The data contain records of suspects in federal criminal matters concluded by United States attorneys or United States magistrates during fiscal year 2008. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.2-1.5. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T12:12:56",
-            "accessLevel": "restricted public",
-            "identifier": "1037",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2007 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of suspects in federal criminal matters concluded by United States attorneys or United States magistrates during fiscal year 2008. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.2-1.5. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR29424.v2",
+                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2008 [United States]"
+                }
+            ],
+            "identifier": "1037",
+            "isPartOf": "2174",
+            "issued": "2011-02-07T14:25:23",
             "keyword": [
                 "defendants",
                 "federal courts",
@@ -32224,55 +32218,55 @@
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T12:12:56",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2011-02-07T14:25:23",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR29424.v2",
-                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2008 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2009",
-            "description": "The data contain records of suspects in federal criminal matters concluded by United States attorneys or United States magistrates during fiscal year 2009. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.2-1.5. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-06-03T17:46:10",
-            "accessLevel": "restricted public",
-            "identifier": "1038",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2008 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of suspects in federal criminal matters concluded by United States attorneys or United States magistrates during fiscal year 2009. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.2-1.5. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR30790.v1",
+                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2009"
+                }
+            ],
+            "identifier": "1038",
+            "isPartOf": "2174",
+            "issued": "2011-06-03T17:45:07",
             "keyword": [
                 "defendants",
                 "federal courts",
@@ -32280,55 +32274,55 @@
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-06-03T17:46:10",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2011-06-03T17:45:07",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR30790.v1",
-                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2009"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2010",
-            "description": "The data contain records of suspects in federal criminal matters concluded by United States attorneys or United States magistrates during fiscal year 2010. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.2-1.5. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2013-01-08T09:26:58",
-            "accessLevel": "restricted public",
-            "identifier": "1039",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2009"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of suspects in federal criminal matters concluded by United States attorneys or United States magistrates during fiscal year 2010. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 1.2-1.5. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR34332.v1",
+                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2010"
+                }
+            ],
+            "identifier": "1039",
+            "isPartOf": "2174",
+            "issued": "2013-01-08T09:17:28",
             "keyword": [
                 "defendants",
                 "federal courts",
@@ -32336,990 +32330,990 @@
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-01-08T09:26:58",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2013-01-08T09:17:28",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR34332.v1",
-                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2010"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters in the United States, 1995",
-            "description": "The data contain records of suspects in federal criminal matters received by United States attorneys or filed before the United States magistrates during fiscal year 1995. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Table 1.1. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T09:56:37",
-            "accessLevel": "restricted public",
-            "identifier": "1040",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters Concluded, 2010"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of suspects in federal criminal matters received by United States attorneys or filed before the United States magistrates during fiscal year 1995. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Table 1.1. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24005.v2",
+                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters in the United States, 1995"
+                }
+            ],
+            "identifier": "1040",
+            "isPartOf": "2174",
+            "issued": "2009-02-12T13:57:00",
             "keyword": [
                 "federal courts",
                 "offenders",
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T09:56:37",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-12T13:57:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24005.v2",
-                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters in the United States, 1995"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters in the United States, 1996",
-            "description": "The data contain records of suspects in federal criminal matters received by United States attorneys or filed before the United States magistrates during fiscal year 1996. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Table 1.1. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:06:54",
-            "accessLevel": "restricted public",
-            "identifier": "1041",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters in the United States, 1995"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of suspects in federal criminal matters received by United States attorneys or filed before the United States magistrates during fiscal year 1996. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Table 1.1. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24024.v2",
+                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters in the United States, 1996"
+                }
+            ],
+            "identifier": "1041",
+            "isPartOf": "2174",
+            "issued": "2009-02-12T13:59:36",
             "keyword": [
                 "federal courts",
                 "offenders",
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:06:54",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-12T13:59:36",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24024.v2",
-                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters in the United States, 1996"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters in the United States, 1997",
-            "description": "The data contain records of suspects in federal criminal matters received by United States attorneys or filed before the United States magistrates during fiscal year 1997. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Table 1.1. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:17:35",
-            "accessLevel": "restricted public",
-            "identifier": "1042",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters in the United States, 1996"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of suspects in federal criminal matters received by United States attorneys or filed before the United States magistrates during fiscal year 1997. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Table 1.1. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24043.v2",
+                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters in the United States, 1997"
+                }
+            ],
+            "identifier": "1042",
+            "isPartOf": "2174",
+            "issued": "2009-02-12T14:01:57",
             "keyword": [
                 "federal courts",
                 "offenders",
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:17:35",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-12T14:01:57",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24043.v2",
-                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters in the United States, 1997"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 1994 [United States]",
-            "description": "The data contain records of suspects in federal criminal matters received by United States attorneys or filed before the United States magistrates during fiscal year 1994. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Table 1.1. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T09:44:47",
-            "accessLevel": "restricted public",
-            "identifier": "1043",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters in the United States, 1997"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of suspects in federal criminal matters received by United States attorneys or filed before the United States magistrates during fiscal year 1994. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Table 1.1. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR23740.v2",
+                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 1994 [United States]"
+                }
+            ],
+            "identifier": "1043",
+            "isPartOf": "2174",
+            "issued": "2009-02-12T13:53:17",
             "keyword": [
                 "federal courts",
                 "offenders",
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T09:44:47",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-12T13:53:17",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR23740.v2",
-                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 1994 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 1998 [United States]",
-            "description": "The data contain records of suspects in federal criminal matters received by United States attorneys or filed before the United States magistrates during fiscal year 1998. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Table 1.1. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:28:08",
-            "accessLevel": "restricted public",
-            "identifier": "1044",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 1994 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
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
-                "federal courts",
-                "offenders",
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
-            "issued": "2009-02-12T14:04:28",
-            "language": [
-                "eng"
-            ],
+            "description": "The data contain records of suspects in federal criminal matters received by United States attorneys or filed before the United States magistrates during fiscal year 1998. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Table 1.1. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://doi.org/10.3886/ICPSR24062.v2",
                     "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 1998 [United States]"
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 1999 [United States]",
-            "description": "The data contain records of suspects in federal criminal matters received by United States attorneys or filed before the United States magistrates during fiscal year 1999. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Table 1.1. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:38:59",
-            "accessLevel": "restricted public",
-            "identifier": "1045",
+            ],
+            "identifier": "1044",
+            "isPartOf": "2174",
+            "issued": "2009-02-12T14:04:28",
+            "keyword": [
+                "federal courts",
+                "offenders",
+                "offenses",
+                "prosecution"
+            ],
+            "language": [
+                "eng"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:28:08",
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
+            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 1998 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of suspects in federal criminal matters received by United States attorneys or filed before the United States magistrates during fiscal year 1999. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Table 1.1. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24081.v2",
+                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 1999 [United States]"
+                }
+            ],
+            "identifier": "1045",
+            "isPartOf": "2174",
+            "issued": "2009-02-12T14:07:05",
             "keyword": [
                 "federal courts",
                 "offenders",
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:38:59",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-12T14:07:05",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24081.v2",
-                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 1999 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 2000 [United States]",
-            "description": "The data contain records of suspects in federal criminal matters received by United States attorneys or filed before the United States magistrates during fiscal year 2000. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Table 1.1. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T10:49:54",
-            "accessLevel": "restricted public",
-            "identifier": "1046",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 1999 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of suspects in federal criminal matters received by United States attorneys or filed before the United States magistrates during fiscal year 2000. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Table 1.1. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24100.v2",
+                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 2000 [United States]"
+                }
+            ],
+            "identifier": "1046",
+            "isPartOf": "2174",
+            "issued": "2009-02-12T14:09:17",
             "keyword": [
                 "federal courts",
                 "offenders",
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T10:49:54",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-12T14:09:17",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24100.v2",
-                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 2000 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 2001 [United States]",
-            "description": "The data contain records of suspects in federal criminal matters received by United States attorneys or filed before the United States magistrates during fiscal year 2001. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Table 1.1. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:00:51",
-            "accessLevel": "restricted public",
-            "identifier": "1047",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 2000 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of suspects in federal criminal matters received by United States attorneys or filed before the United States magistrates during fiscal year 2001. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Table 1.1. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24119.v2",
+                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 2001 [United States]"
+                }
+            ],
+            "identifier": "1047",
+            "isPartOf": "2174",
+            "issued": "2009-02-12T14:11:57",
             "keyword": [
                 "federal courts",
                 "offenders",
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:00:51",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-12T14:11:57",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24119.v2",
-                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 2001 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 2002 [United States]",
-            "description": "The data contain records of suspects in federal criminal matters received by United States attorneys or filed before the United States magistrates during fiscal year 2002. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Table 1.1. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:11:38",
-            "accessLevel": "restricted public",
-            "identifier": "1048",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 2001 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of suspects in federal criminal matters received by United States attorneys or filed before the United States magistrates during fiscal year 2002. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Table 1.1. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24138.v2",
+                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 2002 [United States]"
+                }
+            ],
+            "identifier": "1048",
+            "isPartOf": "2174",
+            "issued": "2009-02-12T14:14:03",
             "keyword": [
                 "federal courts",
                 "offenders",
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:11:38",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-12T14:14:03",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24138.v2",
-                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 2002 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 2003 [United States]",
-            "description": "The data contain records of suspects in federal criminal matters received by United States attorneys or filed before the United States magistrates during fiscal year 2003. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Table 1.1. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:22:37",
-            "accessLevel": "restricted public",
-            "identifier": "1049",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 2002 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of suspects in federal criminal matters received by United States attorneys or filed before the United States magistrates during fiscal year 2003. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Table 1.1. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24157.v2",
+                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 2003 [United States]"
+                }
+            ],
+            "identifier": "1049",
+            "isPartOf": "2174",
+            "issued": "2009-02-12T14:16:15",
             "keyword": [
                 "federal courts",
                 "offenders",
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:22:37",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-12T14:16:15",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24157.v2",
-                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 2003 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 2004 [United States]",
-            "description": "The data contain records of suspects in federal criminal matters received by United States attorneys or filed before the United States magistrates during fiscal year 2004. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Table 1.1. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:32:02",
-            "accessLevel": "restricted public",
-            "identifier": "1050",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 2003 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of suspects in federal criminal matters received by United States attorneys or filed before the United States magistrates during fiscal year 2004. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Table 1.1. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24174.v2",
+                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 2004 [United States]"
+                }
+            ],
+            "identifier": "1050",
+            "isPartOf": "2174",
+            "issued": "2009-02-12T14:18:38",
             "keyword": [
                 "federal courts",
                 "offenders",
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:32:02",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-12T14:18:38",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24174.v2",
-                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 2004 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 2005 [United States]",
-            "description": "The data contain records of suspects in federal criminal matters received by United States attorneys or filed before the United States magistrates during fiscal year 2005. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Table 1.1. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:41:38",
-            "accessLevel": "restricted public",
-            "identifier": "1051",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 2004 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of suspects in federal criminal matters received by United States attorneys or filed before the United States magistrates during fiscal year 2005. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Table 1.1. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24192.v2",
+                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 2005 [United States]"
+                }
+            ],
+            "identifier": "1051",
+            "isPartOf": "2174",
+            "issued": "2009-02-12T14:21:48",
             "keyword": [
                 "federal courts",
                 "offenders",
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:41:38",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-12T14:21:48",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24192.v2",
-                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 2005 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 2006 [United States]",
-            "description": "The data contain records of suspects in federal criminal matters received by United States attorneys or filed before the United States magistrates during fiscal year 2006. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Table 1.1. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:50:02",
-            "accessLevel": "restricted public",
-            "identifier": "1052",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 2005 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of suspects in federal criminal matters received by United States attorneys or filed before the United States magistrates during fiscal year 2006. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Table 1.1. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24209.v2",
+                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 2006 [United States]"
+                }
+            ],
+            "identifier": "1052",
+            "isPartOf": "2174",
+            "issued": "2009-02-12T14:25:38",
             "keyword": [
                 "federal courts",
                 "offenders",
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:50:02",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-12T14:25:38",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24209.v2",
-                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 2006 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 2007 [United States]",
-            "description": "The data contain records of suspects in federal criminal matters received by United States attorneys or filed before the United States magistrates during fiscal year 2007. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Table 1.1. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T11:58:47",
-            "accessLevel": "restricted public",
-            "identifier": "1053",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 2006 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of suspects in federal criminal matters received by United States attorneys or filed before the United States magistrates during fiscal year 2007. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Table 1.1. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24224.v2",
+                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 2007 [United States]"
+                }
+            ],
+            "identifier": "1053",
+            "isPartOf": "2174",
+            "issued": "2009-02-19T10:47:49",
             "keyword": [
                 "federal courts",
                 "offenders",
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T11:58:47",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-19T10:47:49",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24224.v2",
-                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 2007 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 2008 [United States]",
-            "description": "The data contain records of suspects in federal criminal matters received by United States attorneys or filed before the United States magistrates during fiscal year 2008. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Table 1.1. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-03-08T12:14:04",
-            "accessLevel": "restricted public",
-            "identifier": "1054",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 2007 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of suspects in federal criminal matters received by United States attorneys or filed before the United States magistrates during fiscal year 2008. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Table 1.1. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR29427.v2",
+                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 2008 [United States]"
+                }
+            ],
+            "identifier": "1054",
+            "isPartOf": "2174",
+            "issued": "2011-02-07T15:45:10",
             "keyword": [
                 "federal courts",
                 "offenders",
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T12:14:04",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2011-02-07T15:45:10",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR29427.v2",
-                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 2008 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 2009",
-            "description": "The data contain records of suspects in federal criminal matters received by United States attorneys or filed before the United States magistrates during fiscal year 2009. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Table 1.1. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2011-06-06T09:35:37",
-            "accessLevel": "restricted public",
-            "identifier": "1055",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 2008 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of suspects in federal criminal matters received by United States attorneys or filed before the United States magistrates during fiscal year 2009. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Table 1.1. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR30793.v1",
+                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 2009"
+                }
+            ],
+            "identifier": "1055",
+            "isPartOf": "2174",
+            "issued": "2011-06-06T09:34:39",
             "keyword": [
                 "federal courts",
                 "offenders",
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-06-06T09:35:37",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2011-06-06T09:34:39",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR30793.v1",
-                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 2009"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 2010",
-            "description": "The data contain records of suspects in federal criminal matters received by United States attorneys or filed before the United States magistrates during fiscal year 2010. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Table 1.1. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2013-01-08T11:18:42",
-            "accessLevel": "restricted public",
-            "identifier": "1056",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 2009"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of suspects in federal criminal matters received by United States attorneys or filed before the United States magistrates during fiscal year 2010. The data were constructed from the Executive Office for United States Attorneys (EOUSA) Central System file. Records include suspects in criminal matters, and are limited to suspects whose matters were not declined immediately by the United States attorneys. According to the EOUSA, the United States attorneys conduct approximately 95 percent of the prosecutions handled by the Department of Justice. The Central System data contain variables from the original EOUSA files as well as additional analysis variables, or \"SAF\" variables, that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Table 1.1. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR34335.v1",
+                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 2010"
+                }
+            ],
+            "identifier": "1056",
+            "isPartOf": "2174",
+            "issued": "2013-01-08T10:37:11",
             "keyword": [
                 "federal courts",
                 "offenders",
                 "offenses",
                 "prosecution"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-01-08T11:18:42",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2013-01-08T10:37:11",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR34335.v1",
-                    "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 2010"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "State Court Processing Statistics, 2002: Felony and Domestic Violence Defendants in Large Urban Counties",
-            "description": "This study provides incident-based, case processing, and criminal history data on defendants charged in state courts during May 2002. The State Court Processing Statistics Program tracked the processing of about 15,000 felony defendants charged in 40 of the 75 largest counties during May 2002. The BJS study entitled Processing of Domestic Violence Cases in State Courts collected additional incident-based and case processing data on more than 5,000 felony and misdemeanor domestic violence defendants in 16 of the 40 counties.",
-            "modified": "2019-03-28T09:36:18",
-            "accessLevel": "restricted public",
-            "identifier": "1057",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Suspects in Federal Criminal Matters, 2010"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This study provides incident-based, case processing, and criminal history data on defendants charged in state courts during May 2002. The State Court Processing Statistics Program tracked the processing of about 15,000 felony defendants charged in 40 of the 75 largest counties during May 2002. The BJS study entitled Processing of Domestic Violence Cases in State Courts collected additional incident-based and case processing data on more than 5,000 felony and misdemeanor domestic violence defendants in 16 of the 40 counties.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR34892.v3",
+                    "title": "State Court Processing Statistics, 2002: Felony and Domestic Violence Defendants in Large Urban Counties"
+                }
+            ],
+            "identifier": "1057",
+            "isPartOf": "2178",
+            "issued": "2013-12-11T13:20:22",
             "keyword": [
                 "arrest records",
                 "case processing",
@@ -33336,55 +33330,55 @@
                 "state courts",
                 "statistical data"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2019-03-28T09:36:18",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2178",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2013-12-11T13:20:22",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR34892.v3",
-                    "title": "State Court Processing Statistics, 2002: Felony and Domestic Violence Defendants in Large Urban Counties"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Corrections Reporting Program, 1983",
-            "description": "This study was conducted to provide a consistent and\r\ncomprehensive description of convicted persons' entrance into and departure\r\nfrom correctional custody and correctional supervision. To accomplish\r\nthis goal, data were gathered from official state prison records on\r\ntopics such as race, sex, and age of inmates, length of time in jail,\r\nlength of time in prison, and type of offense committed. The data were\r\ncollected from the state prison systems of 32 states.",
-            "modified": "2010-04-23T08:44:42",
-            "accessLevel": "restricted public",
-            "identifier": "1058",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "State Court Processing Statistics, 2002: Felony and Domestic Violence Defendants in Large Urban Counties"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This study was conducted to provide a consistent and\r\ncomprehensive description of convicted persons' entrance into and departure\r\nfrom correctional custody and correctional supervision. To accomplish\r\nthis goal, data were gathered from official state prison records on\r\ntopics such as race, sex, and age of inmates, length of time in jail,\r\nlength of time in prison, and type of offense committed. The data were\r\ncollected from the state prison systems of 32 states.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR08363.v2",
+                    "title": "National Corrections Reporting Program, 1983"
+                }
+            ],
+            "identifier": "1058",
+            "isPartOf": "2589",
+            "issued": "1986-06-06T00:00:00",
             "keyword": [
                 "correctional facilities",
                 "correctional system",
@@ -33398,55 +33392,55 @@
                 "probation",
                 "state correctional facilities"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2010-04-23T08:44:42",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2589",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "1986-06-06T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR08363.v2",
-                    "title": "National Corrections Reporting Program, 1983"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Corrections Reporting Program, 1984",
-            "description": "This study was conducted to provide a consistent and\r\ncomprehensive description of convicted persons' entrance into and departure\r\nfrom correctional custody and correctional supervision. To accomplish\r\nthis goal, data were gathered from official state prison records on\r\ntopics such as race, sex, and age of inmates, length of time in jail,\r\nlength of time in prison, and type of offense committed. The data were\r\ncollected from the state prison systems of 36 states and the Federal\r\nPrison System.",
-            "modified": "2010-04-23T08:50:11",
-            "accessLevel": "restricted public",
-            "identifier": "1059",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "National Corrections Reporting Program, 1983"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This study was conducted to provide a consistent and\r\ncomprehensive description of convicted persons' entrance into and departure\r\nfrom correctional custody and correctional supervision. To accomplish\r\nthis goal, data were gathered from official state prison records on\r\ntopics such as race, sex, and age of inmates, length of time in jail,\r\nlength of time in prison, and type of offense committed. The data were\r\ncollected from the state prison systems of 36 states and the Federal\r\nPrison System.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR08497.v3",
+                    "title": "National Corrections Reporting Program, 1984"
+                }
+            ],
+            "identifier": "1059",
+            "isPartOf": "2589",
+            "issued": "1988-06-01T00:00:00",
             "keyword": [
                 "correctional facilities",
                 "correctional facilities (juveniles)",
@@ -33463,55 +33457,55 @@
                 "probation",
                 "state correctional facilities"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2010-04-23T08:50:11",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2589",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "1988-06-01T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR08497.v3",
-                    "title": "National Corrections Reporting Program, 1984"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Corrections Reporting Program, 1985",
-            "description": "This study was conducted to provide a consistent and\r\ncomprehensive description of convicted persons' entrance into and departure\r\nfrom correctional custody and correctional supervision. To accomplish\r\nthis goal, data were gathered from official state prison records on\r\ntopics such as race, sex, and age of inmates, length of time in jail,\r\nlength of time in prison, and type of offense committed. The data were\r\ncollected from the state prison systems of 40 states, the Federal\r\nPrison System, and the California Youth Authority.",
-            "modified": "2010-04-26T09:36:27",
-            "accessLevel": "restricted public",
-            "identifier": "1060",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "National Corrections Reporting Program, 1984"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This study was conducted to provide a consistent and\r\ncomprehensive description of convicted persons' entrance into and departure\r\nfrom correctional custody and correctional supervision. To accomplish\r\nthis goal, data were gathered from official state prison records on\r\ntopics such as race, sex, and age of inmates, length of time in jail,\r\nlength of time in prison, and type of offense committed. The data were\r\ncollected from the state prison systems of 40 states, the Federal\r\nPrison System, and the California Youth Authority.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR08918.v1",
+                    "title": "National Corrections Reporting Program, 1985"
+                }
+            ],
+            "identifier": "1060",
+            "isPartOf": "2589",
+            "issued": "1990-03-02T00:00:00",
             "keyword": [
                 "correctional facilities",
                 "correctional facilities (juveniles)",
@@ -33528,55 +33522,55 @@
                 "probation",
                 "state correctional facilities"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2010-04-26T09:36:27",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2589",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "1990-03-02T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR08918.v1",
-                    "title": "National Corrections Reporting Program, 1985"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Corrections Reporting Program, 1986",
-            "description": "This study was conducted to provide a consistent and\r\ncomprehensive description of convicted persons' entrance into and\r\ndeparture from correctional custody and correctional supervision. To\r\naccomplish this goal, data were gathered from official state prison\r\nrecords on topics such as race, sex, and age of inmates, length of\r\ntime in jail, length of time in prison, and type of offense committed.\r\nThe data were collected from the state prison systems of 36 states, as\r\nwell as the Federal Prison System, the California Youth Authority, and\r\nthe District of Columbia.",
-            "modified": "2010-11-17T14:22:01",
-            "accessLevel": "restricted public",
-            "identifier": "1061",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "National Corrections Reporting Program, 1985"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This study was conducted to provide a consistent and\r\ncomprehensive description of convicted persons' entrance into and\r\ndeparture from correctional custody and correctional supervision. To\r\naccomplish this goal, data were gathered from official state prison\r\nrecords on topics such as race, sex, and age of inmates, length of\r\ntime in jail, length of time in prison, and type of offense committed.\r\nThe data were collected from the state prison systems of 36 states, as\r\nwell as the Federal Prison System, the California Youth Authority, and\r\nthe District of Columbia.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR09276.v1",
+                    "title": "National Corrections Reporting Program, 1986"
+                }
+            ],
+            "identifier": "1061",
+            "isPartOf": "2589",
+            "issued": "1991-10-22T00:00:00",
             "keyword": [
                 "correctional facilities",
                 "correctional facilities (juveniles)",
@@ -33593,55 +33587,55 @@
                 "probation",
                 "state correctional facilities"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2010-11-17T14:22:01",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2589",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "1991-10-22T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR09276.v1",
-                    "title": "National Corrections Reporting Program, 1986"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Corrections Reporting Program, 1987",
-            "description": "This study was conducted to provide a consistent and\r\ncomprehensive description of convicted persons' entrance into and departure\r\nfrom correctional custody and correctional supervision. To accomplish\r\nthis goal, data were gathered from official state prison records on\r\ntopics such as race, sex, and age of inmates, length of time in jail,\r\nlength of time in prison, and type of offense committed. The data were\r\ncollected from the state prison systems of 35 states, as well\r\nas the Federal Prison System and the California Youth Authority, and the\r\nDistrict of Columbia.",
-            "modified": "2010-04-23T09:29:23",
-            "accessLevel": "restricted public",
-            "identifier": "1062",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "National Corrections Reporting Program, 1986"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This study was conducted to provide a consistent and\r\ncomprehensive description of convicted persons' entrance into and departure\r\nfrom correctional custody and correctional supervision. To accomplish\r\nthis goal, data were gathered from official state prison records on\r\ntopics such as race, sex, and age of inmates, length of time in jail,\r\nlength of time in prison, and type of offense committed. The data were\r\ncollected from the state prison systems of 35 states, as well\r\nas the Federal Prison System and the California Youth Authority, and the\r\nDistrict of Columbia.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR09402.v3",
+                    "title": "National Corrections Reporting Program, 1987"
+                }
+            ],
+            "identifier": "1062",
+            "isPartOf": "2589",
+            "issued": "1991-10-23T00:00:00",
             "keyword": [
                 "correctional facilities",
                 "correctional facilities (juveniles)",
@@ -33658,55 +33652,55 @@
                 "probation",
                 "state correctional facilities"
             ],
-            "bureauCode": [
-                "011:21"
-            ],
-            "programCode": [
-                "011:061"
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2589",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "1991-10-23T00:00:00",
             "language": [
                 "eng"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR09402.v3",
-                    "title": "National Corrections Reporting Program, 1987"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Corrections Reporting Program, 1988",
-            "description": "This study was conducted to provide a consistent and\r\ncomprehensive description of convicted persons' entrance into and departure\r\nfrom correctional custody and correctional supervision. To accomplish\r\nthis goal, data were gathered from official state prison records on\r\ntopics such as race, sex, and age of inmates, length of time in jail,\r\nlength of time in prison, and type of offense committed. The data were\r\ncollected from the state prison systems of 36 states, as well\r\nas the Federal Prison System, the California Youth Authority, and the\r\nDistrict of Columbia.",
-            "modified": "2010-04-23T09:48:33",
-            "accessLevel": "restricted public",
-            "identifier": "1063",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2010-04-23T09:29:23",
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
+            "title": "National Corrections Reporting Program, 1987"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This study was conducted to provide a consistent and\r\ncomprehensive description of convicted persons' entrance into and departure\r\nfrom correctional custody and correctional supervision. To accomplish\r\nthis goal, data were gathered from official state prison records on\r\ntopics such as race, sex, and age of inmates, length of time in jail,\r\nlength of time in prison, and type of offense committed. The data were\r\ncollected from the state prison systems of 36 states, as well\r\nas the Federal Prison System, the California Youth Authority, and the\r\nDistrict of Columbia.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR09450.v3",
+                    "title": "National Corrections Reporting Program, 1988"
+                }
+            ],
+            "identifier": "1063",
+            "isPartOf": "2589",
+            "issued": "1991-10-23T00:00:00",
             "keyword": [
                 "correctional facilities",
                 "correctional facilities (juveniles)",
@@ -33723,55 +33717,55 @@
                 "probation",
                 "state correctional facilities"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2010-04-23T09:48:33",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2589",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "1991-10-23T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR09450.v3",
-                    "title": "National Corrections Reporting Program, 1988"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Corrections Reporting Program, 1989",
-            "description": "This study was conducted to provide a consistent and\r\ncomprehensive description of convicted persons' entrance into and departure\r\nfrom correctional custody and correctional supervision. To accomplish\r\nthis goal, data were gathered from official state prison records on\r\ntopics such as race, sex, and age of inmates, length of time in jail,\r\nlength of time in prison, and type of offense committed. The data were\r\ncollected from the state prison systems of 36 states, as well\r\nas the Federal Prison System, the California Youth Authority, and the\r\nDistrict of Columbia.",
-            "modified": "2010-04-23T11:25:08",
-            "accessLevel": "restricted public",
-            "identifier": "1064",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "National Corrections Reporting Program, 1988"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This study was conducted to provide a consistent and\r\ncomprehensive description of convicted persons' entrance into and departure\r\nfrom correctional custody and correctional supervision. To accomplish\r\nthis goal, data were gathered from official state prison records on\r\ntopics such as race, sex, and age of inmates, length of time in jail,\r\nlength of time in prison, and type of offense committed. The data were\r\ncollected from the state prison systems of 36 states, as well\r\nas the Federal Prison System, the California Youth Authority, and the\r\nDistrict of Columbia.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR09849.v1",
+                    "title": "National Corrections Reporting Program, 1989"
+                }
+            ],
+            "identifier": "1064",
+            "isPartOf": "2589",
+            "issued": "1993-12-18T00:00:00",
             "keyword": [
                 "correctional facilities",
                 "correctional facilities (juveniles)",
@@ -33788,55 +33782,55 @@
                 "probation",
                 "state correctional facilities"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2010-04-23T11:25:08",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2589",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "1993-12-18T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR09849.v1",
-                    "title": "National Corrections Reporting Program, 1989"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Corrections Reporting Program, 1990",
-            "description": "This study was conducted to provide a consistent and\r\ncomprehensive description of convicted persons' entrance into and departure\r\nfrom correctional custody and correctional supervision. To accomplish\r\nthis goal, data were gathered from official state prison records on\r\ntopics such as race, sex, and age of inmates, length of time in jail,\r\nlength of time in prison, and type of offense committed. The data were\r\ncollected from the state prison systems of 35 states, as well\r\nas the Federal Prison System, the California Youth Authority, and the\r\nDistrict of Columbia.",
-            "modified": "2010-04-23T16:31:24",
-            "accessLevel": "restricted public",
-            "identifier": "1065",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "National Corrections Reporting Program, 1989"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This study was conducted to provide a consistent and\r\ncomprehensive description of convicted persons' entrance into and departure\r\nfrom correctional custody and correctional supervision. To accomplish\r\nthis goal, data were gathered from official state prison records on\r\ntopics such as race, sex, and age of inmates, length of time in jail,\r\nlength of time in prison, and type of offense committed. The data were\r\ncollected from the state prison systems of 35 states, as well\r\nas the Federal Prison System, the California Youth Authority, and the\r\nDistrict of Columbia.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR06141.v1",
+                    "title": "National Corrections Reporting Program, 1990"
+                }
+            ],
+            "identifier": "1065",
+            "isPartOf": "2589",
+            "issued": "1993-12-18T00:00:00",
             "keyword": [
                 "correctional facilities",
                 "correctional facilities (juveniles)",
@@ -33853,55 +33847,55 @@
                 "probation",
                 "state correctional facilities"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2010-04-23T16:31:24",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2589",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "1993-12-18T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR06141.v1",
-                    "title": "National Corrections Reporting Program, 1990"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Corrections Reporting Program, 1991",
-            "description": "This study was conducted to provide a consistent and\r\ncomprehensive description of convicted persons' entrance into and departure\r\nfrom correctional custody and correctional supervision. To accomplish\r\nthis goal, data were gathered from official state prison records on\r\ntopics such as race, sex, and age of inmates, length of time in jail,\r\nlength of time in prison, and type of offense committed. The data were\r\ncollected from the state prison systems of 35 states, as well\r\nas the Federal Prison System, the California Youth Authority, and the\r\nDistrict of Columbia.",
-            "modified": "2010-04-23T16:38:50",
-            "accessLevel": "restricted public",
-            "identifier": "1066",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "National Corrections Reporting Program, 1990"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This study was conducted to provide a consistent and\r\ncomprehensive description of convicted persons' entrance into and departure\r\nfrom correctional custody and correctional supervision. To accomplish\r\nthis goal, data were gathered from official state prison records on\r\ntopics such as race, sex, and age of inmates, length of time in jail,\r\nlength of time in prison, and type of offense committed. The data were\r\ncollected from the state prison systems of 35 states, as well\r\nas the Federal Prison System, the California Youth Authority, and the\r\nDistrict of Columbia.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR06272.v1",
+                    "title": "National Corrections Reporting Program, 1991"
+                }
+            ],
+            "identifier": "1066",
+            "isPartOf": "2589",
+            "issued": "1994-10-19T00:00:00",
             "keyword": [
                 "correctional facilities",
                 "correctional facilities (juveniles)",
@@ -33918,55 +33912,55 @@
                 "probation",
                 "state correctional facilities"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2010-04-23T16:38:50",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2589",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "1994-10-19T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR06272.v1",
-                    "title": "National Corrections Reporting Program, 1991"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Corrections Reporting Program, 1992",
-            "description": "This study was conducted to provide a consistent and\r\ncomprehensive description of convicted persons' entrance into and departure\r\nfrom correctional custody and correctional supervision. To accomplish\r\nthis goal, data were gathered from official state prison records on\r\ntopics such as race, sex, and age of inmates, length of time in jail,\r\nlength of time in prison, and type of offense committed. The data were\r\ncollected from the state prison systems of 38 states, as well\r\nas the Federal Prison System, the California Youth Authority, and the\r\nDistrict of Columbia.",
-            "modified": "2010-04-23T16:45:42",
-            "accessLevel": "restricted public",
-            "identifier": "1067",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "National Corrections Reporting Program, 1991"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This study was conducted to provide a consistent and\r\ncomprehensive description of convicted persons' entrance into and departure\r\nfrom correctional custody and correctional supervision. To accomplish\r\nthis goal, data were gathered from official state prison records on\r\ntopics such as race, sex, and age of inmates, length of time in jail,\r\nlength of time in prison, and type of offense committed. The data were\r\ncollected from the state prison systems of 38 states, as well\r\nas the Federal Prison System, the California Youth Authority, and the\r\nDistrict of Columbia.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR06400.v1",
+                    "title": "National Corrections Reporting Program, 1992"
+                }
+            ],
+            "identifier": "1067",
+            "isPartOf": "2589",
+            "issued": "1995-01-11T00:00:00",
             "keyword": [
                 "correctional facilities",
                 "correctional facilities (juveniles)",
@@ -33983,55 +33977,55 @@
                 "probation",
                 "state correctional facilities"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2010-04-23T16:45:42",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2589",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "1995-01-11T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR06400.v1",
-                    "title": "National Corrections Reporting Program, 1992"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Corrections Reporting Program, 1993",
-            "description": "This study was conducted to provide a consistent and\r\ncomprehensive description of convicted persons' entrance into and departure\r\nfrom correctional custody and correctional supervision. To accomplish\r\nthis goal, data were gathered from official state prison records on\r\ntopics such as race, sex, and age of inmates, length of time in jail,\r\nlength of time in prison, and type of offense committed. The data were\r\ncollected from the state prison systems of 38 states, as well\r\nas the Federal Prison System, the California Youth Authority, and the\r\nDistrict of Columbia.",
-            "modified": "2010-04-23T17:02:03",
-            "accessLevel": "restricted public",
-            "identifier": "1068",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "National Corrections Reporting Program, 1992"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This study was conducted to provide a consistent and\r\ncomprehensive description of convicted persons' entrance into and departure\r\nfrom correctional custody and correctional supervision. To accomplish\r\nthis goal, data were gathered from official state prison records on\r\ntopics such as race, sex, and age of inmates, length of time in jail,\r\nlength of time in prison, and type of offense committed. The data were\r\ncollected from the state prison systems of 38 states, as well\r\nas the Federal Prison System, the California Youth Authority, and the\r\nDistrict of Columbia.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR06823.v1",
+                    "title": "National Corrections Reporting Program, 1993"
+                }
+            ],
+            "identifier": "1068",
+            "isPartOf": "2589",
+            "issued": "1997-04-14T00:00:00",
             "keyword": [
                 "correctional facilities",
                 "correctional facilities (juveniles)",
@@ -34048,55 +34042,55 @@
                 "probation",
                 "state correctional facilities"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2010-04-23T17:02:03",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2589",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "1997-04-14T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR06823.v1",
-                    "title": "National Corrections Reporting Program, 1993"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Corrections Reporting Program, 1994",
-            "description": "The purpose of this study was to gather data on prisoners\r\nentering and leaving the custody or supervision of state and federal\r\nauthorities. Data refer to prisoners who were admitted to prison,\r\nreleased from prison, or released from parole in 1994. Variables\r\ninclude incarceration history, current offenses, and total time\r\nserved. Background information on individuals includes year of birth,\r\nsex, age, race, Hispanic origin, and educational attainment.",
-            "modified": "2010-04-23T17:19:36",
-            "accessLevel": "restricted public",
-            "identifier": "1069",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "National Corrections Reporting Program, 1993"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The purpose of this study was to gather data on prisoners\r\nentering and leaving the custody or supervision of state and federal\r\nauthorities. Data refer to prisoners who were admitted to prison,\r\nreleased from prison, or released from parole in 1994. Variables\r\ninclude incarceration history, current offenses, and total time\r\nserved. Background information on individuals includes year of birth,\r\nsex, age, race, Hispanic origin, and educational attainment.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR06881.v1",
+                    "title": "National Corrections Reporting Program, 1994"
+                }
+            ],
+            "identifier": "1069",
+            "isPartOf": "2589",
+            "issued": "1998-01-13T00:00:00",
             "keyword": [
                 "correctional facilities",
                 "correctional facilities (juveniles)",
@@ -34113,55 +34107,55 @@
                 "probation",
                 "state correctional facilities"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2010-04-23T17:19:36",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2589",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "1998-01-13T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR06881.v1",
-                    "title": "National Corrections Reporting Program, 1994"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Corrections Reporting Program, 1995",
-            "description": "The purpose of this study was to gather data on prisoners\r\nentering and leaving the custody or supervision of state and federal\r\nauthorities. Data refer to prisoners who were admitted to prison,\r\nreleased from prison, or released from parole in 1995. Variables\r\ninclude incarceration history, current offenses, and total time\r\nserved. Background information on individuals includes year of birth,\r\nsex, age, race, Hispanic origin, and educational attainment.",
-            "modified": "2010-04-23T18:00:38",
-            "accessLevel": "restricted public",
-            "identifier": "1070",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "National Corrections Reporting Program, 1994"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The purpose of this study was to gather data on prisoners\r\nentering and leaving the custody or supervision of state and federal\r\nauthorities. Data refer to prisoners who were admitted to prison,\r\nreleased from prison, or released from parole in 1995. Variables\r\ninclude incarceration history, current offenses, and total time\r\nserved. Background information on individuals includes year of birth,\r\nsex, age, race, Hispanic origin, and educational attainment.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR02194.v1",
+                    "title": "National Corrections Reporting Program, 1995"
+                }
+            ],
+            "identifier": "1070",
+            "isPartOf": "2589",
+            "issued": "1998-07-28T00:00:00",
             "keyword": [
                 "correctional facilities",
                 "correctional facilities (juveniles)",
@@ -34178,55 +34172,55 @@
                 "probation",
                 "state correctional facilities"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2010-04-23T18:00:38",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2589",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "1998-07-28T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR02194.v1",
-                    "title": "National Corrections Reporting Program, 1995"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Corrections Reporting Program, 1996",
-            "description": "The purpose of this study was to gather data on prisoners\r\nentering and leaving the custody or supervision of state and federal\r\nauthorities. Data refer to prisoners who were admitted to prison,\r\nreleased from prison, or released from parole in 1996. Variables\r\ninclude incarceration history, current offenses, and total time\r\nserved. Background information on individuals includes year of birth,\r\nsex, age, race, Hispanic origin, and educational attainment.",
-            "modified": "2010-04-23T18:56:31",
-            "accessLevel": "restricted public",
-            "identifier": "1071",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "National Corrections Reporting Program, 1995"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The purpose of this study was to gather data on prisoners\r\nentering and leaving the custody or supervision of state and federal\r\nauthorities. Data refer to prisoners who were admitted to prison,\r\nreleased from prison, or released from parole in 1996. Variables\r\ninclude incarceration history, current offenses, and total time\r\nserved. Background information on individuals includes year of birth,\r\nsex, age, race, Hispanic origin, and educational attainment.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR02448.v1",
+                    "title": "National Corrections Reporting Program, 1996"
+                }
+            ],
+            "identifier": "1071",
+            "isPartOf": "2589",
+            "issued": "1998-12-23T00:00:00",
             "keyword": [
                 "correctional facilities",
                 "correctional facilities (juveniles)",
@@ -34243,55 +34237,55 @@
                 "probation",
                 "state correctional facilities"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2010-04-23T18:56:31",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2589",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "1998-12-23T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR02448.v1",
-                    "title": "National Corrections Reporting Program, 1996"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Corrections Reporting Program, 1997",
-            "description": "The purpose of this study was to gather data on prisoners\r\nentering and leaving the custody or supervision of state and federal\r\nauthorities. Data refer to prisoners who were admitted to prison,\r\nreleased from prison, or released from parole in 1997. Variables\r\ninclude incarceration history, current offenses, and total time\r\nserved. Background information on individuals includes year of birth,\r\nsex, age, race, Hispanic origin, and educational attainment.",
-            "modified": "2010-04-23T19:17:33",
-            "accessLevel": "restricted public",
-            "identifier": "1072",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "National Corrections Reporting Program, 1996"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The purpose of this study was to gather data on prisoners\r\nentering and leaving the custody or supervision of state and federal\r\nauthorities. Data refer to prisoners who were admitted to prison,\r\nreleased from prison, or released from parole in 1997. Variables\r\ninclude incarceration history, current offenses, and total time\r\nserved. Background information on individuals includes year of birth,\r\nsex, age, race, Hispanic origin, and educational attainment.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR02613.v2",
+                    "title": "National Corrections Reporting Program, 1997"
+                }
+            ],
+            "identifier": "1072",
+            "isPartOf": "2589",
+            "issued": "2000-02-01T00:00:00",
             "keyword": [
                 "correctional facilities",
                 "correctional facilities (juveniles)",
@@ -34308,55 +34302,55 @@
                 "probation",
                 "state correctional facilities"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2010-04-23T19:17:33",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2589",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2000-02-01T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR02613.v2",
-                    "title": "National Corrections Reporting Program, 1997"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Corrections Reporting Program, 1998",
-            "description": "The purpose of this study was to gather data on prisoners\r\nentering and leaving the custody or supervision of state and federal\r\nauthorities. Data refer to prisoners who were admitted to prison,\r\nreleased from prison, or released from parole in 1998. Variables\r\ninclude incarceration history, current offenses, and total time\r\nserved. Background information on individuals includes year of birth,\r\nsex, age, race, Hispanic origin, and educational attainment.",
-            "modified": "2010-04-23T19:36:00",
-            "accessLevel": "restricted public",
-            "identifier": "1073",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "National Corrections Reporting Program, 1997"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The purpose of this study was to gather data on prisoners\r\nentering and leaving the custody or supervision of state and federal\r\nauthorities. Data refer to prisoners who were admitted to prison,\r\nreleased from prison, or released from parole in 1998. Variables\r\ninclude incarceration history, current offenses, and total time\r\nserved. Background information on individuals includes year of birth,\r\nsex, age, race, Hispanic origin, and educational attainment.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR03029.v1",
+                    "title": "National Corrections Reporting Program, 1998"
+                }
+            ],
+            "identifier": "1073",
+            "isPartOf": "2589",
+            "issued": "2001-02-23T00:00:00",
             "keyword": [
                 "correctional facilities",
                 "correctional facilities (juveniles)",
@@ -34373,55 +34367,55 @@
                 "probation",
                 "state correctional facilities"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2010-04-23T19:36:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2589",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2001-02-23T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR03029.v1",
-                    "title": "National Corrections Reporting Program, 1998"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Corrections Reporting Program, 1999: [United States]",
-            "description": "The purpose of this study was to gather data on prisoners\r\nentering and leaving the custody or supervision of state and federal\r\nauthorities. Data refer to prisoners who were admitted to prison (Part\r\n1), released from prison (Part 2), or released from parole (Part 3) in\r\n1999. Variables include incarceration history, current offenses, and\r\ntotal time served. Background information on individuals includes year\r\nof birth, sex, age, race, Hispanic origin, and educational attainment.",
-            "modified": "2010-04-23T20:07:07",
-            "accessLevel": "restricted public",
-            "identifier": "1074",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "National Corrections Reporting Program, 1998"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The purpose of this study was to gather data on prisoners\r\nentering and leaving the custody or supervision of state and federal\r\nauthorities. Data refer to prisoners who were admitted to prison (Part\r\n1), released from prison (Part 2), or released from parole (Part 3) in\r\n1999. Variables include incarceration history, current offenses, and\r\ntotal time served. Background information on individuals includes year\r\nof birth, sex, age, race, Hispanic origin, and educational attainment.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR03339.v1",
+                    "title": "National Corrections Reporting Program, 1999: [United States]"
+                }
+            ],
+            "identifier": "1074",
+            "isPartOf": "2589",
+            "issued": "2002-03-29T00:00:00",
             "keyword": [
                 "correctional facilities",
                 "correctional facilities (juveniles)",
@@ -34438,55 +34432,55 @@
                 "probation",
                 "state correctional facilities"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2010-04-23T20:07:07",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2589",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2002-03-29T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR03339.v1",
-                    "title": "National Corrections Reporting Program, 1999: [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Corrections Reporting Program, 2000:  [United States]",
-            "description": "The purpose of this study was to gather data on prisoners\r\nentering and leaving the custody or supervision of state and federal\r\nauthorities. Data refer to prisoners who were admitted to prison (Part\r\n1), released from prison (Part 2), or released from parole (Part 3) in\r\n2000. Variables include incarceration history, current offenses, and\r\ntotal time served. Background information on individuals includes year\r\nof birth, sex, age, race, Hispanic origin, and educational\r\nattainment.",
-            "modified": "2010-04-26T07:44:41",
-            "accessLevel": "restricted public",
-            "identifier": "1075",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "National Corrections Reporting Program, 1999: [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The purpose of this study was to gather data on prisoners\r\nentering and leaving the custody or supervision of state and federal\r\nauthorities. Data refer to prisoners who were admitted to prison (Part\r\n1), released from prison (Part 2), or released from parole (Part 3) in\r\n2000. Variables include incarceration history, current offenses, and\r\ntotal time served. Background information on individuals includes year\r\nof birth, sex, age, race, Hispanic origin, and educational\r\nattainment.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR03761.v1",
+                    "title": "National Corrections Reporting Program, 2000:  [United States]"
+                }
+            ],
+            "identifier": "1075",
+            "isPartOf": "2589",
+            "issued": "2003-07-30T00:00:00",
             "keyword": [
                 "correctional facilities",
                 "correctional facilities (juveniles)",
@@ -34503,55 +34497,55 @@
                 "probation",
                 "state correctional facilities"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2010-04-26T07:44:41",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2589",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2003-07-30T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR03761.v1",
-                    "title": "National Corrections Reporting Program, 2000:  [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Corrections Reporting Program, 2000-2011",
-            "description": "The National Corrections Reporting Program (NCRP) compiles offender-level data on admissions and releases from state and federal prisons and post-confinement community supervision. The data are used to monitor the nation's correctional population and address specific policy questions related to recidivism, prisoner reentry, and trends in demographic characteristics of the incarcerated and community supervision populations. The Bureau of Justice Statistics (BJS) has administered the NCRP since 1983. The United States Bureau of the Census served as data collection agent for BJS until October 2010, when Abt Associates assumed this position.\r\nFrom 2000 to 2009, NCRP data were archived each year in four, year-specific files that corresponded to the four files that states were asked to submit to the Census Bureau. The four files are: Prison Admissions (Part A), Prison Releases (Part B), Parole Exits (Part C), and Prison Custody (Part D). For example, the 2009 NCRP archive consists of prison admissions occurring in 2009, prison releases occurring in 2009, parole exits occurring in 2009, and prisoners in custody on December 31, 2009.\r\nStarting in 2011, NCRP data will be archived in a single, multi-year Term Record file. A Term Record represents a single period of incarceration for an individual offender. Each year, the archived Term Record file will be replaced by a new Term Record file that incorporates new NCRP data collected and processed during the previous year, as well as updates to previously collected data. The Term Records were created from the Prison Admissions (Part A), Prison Releases (Part B), and Prison Custody (Part D) records submitted by states since 2000. With a few lines of computing code (included with the archive), an analyst can create a prison admission, release, or custody file from the Term Record file.\r\nIn addition to the Term Record file, two additional files are being archived: (1) Prison Admissions (Part A), Prison Releases (Part B), and Prison Custody (Part D) records that were not used in building the Term Record file and (2) Part C (Parole Exit) records collected from January 1, 2011 to October 31, 2012.",
-            "modified": "2013-09-23T11:52:04",
-            "accessLevel": "restricted public",
-            "identifier": "1076",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "National Corrections Reporting Program, 2000:  [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Corrections Reporting Program (NCRP) compiles offender-level data on admissions and releases from state and federal prisons and post-confinement community supervision. The data are used to monitor the nation's correctional population and address specific policy questions related to recidivism, prisoner reentry, and trends in demographic characteristics of the incarcerated and community supervision populations. The Bureau of Justice Statistics (BJS) has administered the NCRP since 1983. The United States Bureau of the Census served as data collection agent for BJS until October 2010, when Abt Associates assumed this position.\r\nFrom 2000 to 2009, NCRP data were archived each year in four, year-specific files that corresponded to the four files that states were asked to submit to the Census Bureau. The four files are: Prison Admissions (Part A), Prison Releases (Part B), Parole Exits (Part C), and Prison Custody (Part D). For example, the 2009 NCRP archive consists of prison admissions occurring in 2009, prison releases occurring in 2009, parole exits occurring in 2009, and prisoners in custody on December 31, 2009.\r\nStarting in 2011, NCRP data will be archived in a single, multi-year Term Record file. A Term Record represents a single period of incarceration for an individual offender. Each year, the archived Term Record file will be replaced by a new Term Record file that incorporates new NCRP data collected and processed during the previous year, as well as updates to previously collected data. The Term Records were created from the Prison Admissions (Part A), Prison Releases (Part B), and Prison Custody (Part D) records submitted by states since 2000. With a few lines of computing code (included with the archive), an analyst can create a prison admission, release, or custody file from the Term Record file.\r\nIn addition to the Term Record file, two additional files are being archived: (1) Prison Admissions (Part A), Prison Releases (Part B), and Prison Custody (Part D) records that were not used in building the Term Record file and (2) Part C (Parole Exit) records collected from January 1, 2011 to October 31, 2012.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR34555.v1",
+                    "title": "National Corrections Reporting Program, 2000-2011"
+                }
+            ],
+            "identifier": "1076",
+            "isPartOf": "2589",
+            "issued": "2013-09-23T10:36:19",
             "keyword": [
                 "correctional facilities",
                 "correctional facilities (juveniles)",
@@ -34568,55 +34562,55 @@
                 "probation",
                 "state correctional facilities"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-09-23T11:52:04",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2589",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2013-09-23T10:36:19",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR34555.v1",
-                    "title": "National Corrections Reporting Program, 2000-2011"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Corrections Reporting Program, 2001:  [United States]",
-            "description": "The purpose of this study was to gather data on prisoners\r\nentering and leaving the custody or supervision of state and federal\r\nauthorities. Data refer to prisoners who were admitted to prison (Part\r\n1), released from prison (Part 2), or released from parole (Part 3) in\r\n2001. Variables include incarceration history, current offenses, and\r\ntotal time served. Background information on individuals includes year\r\nof birth, sex, age, race, Hispanic origin, and educational\r\nattainment.",
-            "modified": "2010-04-26T08:07:15",
-            "accessLevel": "restricted public",
-            "identifier": "1077",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "National Corrections Reporting Program, 2000-2011"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The purpose of this study was to gather data on prisoners\r\nentering and leaving the custody or supervision of state and federal\r\nauthorities. Data refer to prisoners who were admitted to prison (Part\r\n1), released from prison (Part 2), or released from parole (Part 3) in\r\n2001. Variables include incarceration history, current offenses, and\r\ntotal time served. Background information on individuals includes year\r\nof birth, sex, age, race, Hispanic origin, and educational\r\nattainment.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR04052.v1",
+                    "title": "National Corrections Reporting Program, 2001:  [United States]"
+                }
+            ],
+            "identifier": "1077",
+            "isPartOf": "2589",
+            "issued": "2004-08-20T00:00:00",
             "keyword": [
                 "correctional facilities",
                 "correctional facilities (juveniles)",
@@ -34633,55 +34627,55 @@
                 "probation",
                 "state correctional facilities"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2010-04-26T08:07:15",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2589",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2004-08-20T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR04052.v1",
-                    "title": "National Corrections Reporting Program, 2001:  [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Corrections Reporting Program, 2002: [United States]",
-            "description": "The purpose of this study was to gather data on prisoners\r\nentering and leaving the custody or supervision of state and federal\r\nauthorities. Data refer to prisoners who were admitted to prison (Part\r\n1), released from prison (Part 2), or released from parole (Part 3)\r\nin 2002. Variables include incarceration history, current offenses,\r\nand total time served. Background information on individuals includes\r\nyear of birth, sex, age, race, Hispanic origin, and educational\r\nattainment.",
-            "modified": "2010-04-26T08:35:04",
-            "accessLevel": "restricted public",
-            "identifier": "1078",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "National Corrections Reporting Program, 2001:  [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The purpose of this study was to gather data on prisoners\r\nentering and leaving the custody or supervision of state and federal\r\nauthorities. Data refer to prisoners who were admitted to prison (Part\r\n1), released from prison (Part 2), or released from parole (Part 3)\r\nin 2002. Variables include incarceration history, current offenses,\r\nand total time served. Background information on individuals includes\r\nyear of birth, sex, age, race, Hispanic origin, and educational\r\nattainment.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR04345.v1",
+                    "title": "National Corrections Reporting Program, 2002: [United States]"
+                }
+            ],
+            "identifier": "1078",
+            "isPartOf": "2589",
+            "issued": "2006-04-05T00:00:00",
             "keyword": [
                 "correctional facilities",
                 "correctional facilities (juveniles)",
@@ -34698,55 +34692,55 @@
                 "probation",
                 "state correctional facilities"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2010-04-26T08:35:04",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2589",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2006-04-05T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR04345.v1",
-                    "title": "National Corrections Reporting Program, 2002: [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Corrections Reporting Program, 2003 [United States]",
-            "description": "The purpose of this study was to gather data on prisoners\r\nentering and leaving the custody or supervision of state and federal\r\nauthorities. Data refer to prisoners who were admitted to prison (Part\r\n1), released from prison (Part 2), or released from parole (Part 3)\r\nin 2003. Variables include incarceration history, current offenses,\r\nand total time served. Background information on individuals includes\r\nyear of birth, sex, age, race, Hispanic origin, and educational\r\nattainment.",
-            "modified": "2010-04-26T08:58:23",
-            "accessLevel": "restricted public",
-            "identifier": "1079",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "National Corrections Reporting Program, 2002: [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The purpose of this study was to gather data on prisoners\r\nentering and leaving the custody or supervision of state and federal\r\nauthorities. Data refer to prisoners who were admitted to prison (Part\r\n1), released from prison (Part 2), or released from parole (Part 3)\r\nin 2003. Variables include incarceration history, current offenses,\r\nand total time served. Background information on individuals includes\r\nyear of birth, sex, age, race, Hispanic origin, and educational\r\nattainment.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR20741.v1",
+                    "title": "National Corrections Reporting Program, 2003 [United States]"
+                }
+            ],
+            "identifier": "1079",
+            "isPartOf": "2589",
+            "issued": "2007-08-30T00:00:00",
             "keyword": [
                 "correctional facilities",
                 "correctional facilities (juveniles)",
@@ -34763,55 +34757,55 @@
                 "probation",
                 "state correctional facilities"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2010-04-26T08:58:23",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2589",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2007-08-30T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR20741.v1",
-                    "title": "National Corrections Reporting Program, 2003 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Corrections Reporting Program, 2004",
-            "description": "The National Corrections Reporting Program gathers data on prisoners entering and leaving the custody or supervision of state and federal authorities. The dataset is comprised of four types of data: prisoners who were admitted to prison (Part 1), released from prison (Part 2), released from parole (Part 3), or in prison at year end (Part 4).\r\nThe National Prison Statistics (NPS) program was established in 1926 by the Bureau of the Census in response to a congressional mandate to compile national information on the populations confined in correctional institutions. This program described the characteristics and counts of prison inmates during each calendar year. Since its initiation, responsibility for this program has shifted among several agencies -- in 1950 it was transferred to the Federal Bureau of Prisons and to the Law Enforcement Assistance Administration in 1971. Since 1972, the Bureau of Census, under agreement with the Department of Justice, has had responsibility for compiling the statistical data. Census staff negotiates directly with each state, assembles and edits the data, and prepares the data for analysis and publication.",
-            "modified": "2013-01-17T10:17:13",
-            "accessLevel": "restricted public",
-            "identifier": "1080",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "National Corrections Reporting Program, 2003 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Corrections Reporting Program gathers data on prisoners entering and leaving the custody or supervision of state and federal authorities. The dataset is comprised of four types of data: prisoners who were admitted to prison (Part 1), released from prison (Part 2), released from parole (Part 3), or in prison at year end (Part 4).\r\nThe National Prison Statistics (NPS) program was established in 1926 by the Bureau of the Census in response to a congressional mandate to compile national information on the populations confined in correctional institutions. This program described the characteristics and counts of prison inmates during each calendar year. Since its initiation, responsibility for this program has shifted among several agencies -- in 1950 it was transferred to the Federal Bureau of Prisons and to the Law Enforcement Assistance Administration in 1971. Since 1972, the Bureau of Census, under agreement with the Department of Justice, has had responsibility for compiling the statistical data. Census staff negotiates directly with each state, assembles and edits the data, and prepares the data for analysis and publication.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR26521.v2",
+                    "title": "National Corrections Reporting Program, 2004"
+                }
+            ],
+            "identifier": "1080",
+            "isPartOf": "2589",
+            "issued": "2010-01-27T08:15:16",
             "keyword": [
                 "correctional facilities",
                 "correctional facilities (juveniles)",
@@ -34828,55 +34822,55 @@
                 "probation",
                 "state correctional facilities"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-01-17T10:17:13",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2589",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2010-01-27T08:15:16",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR26521.v2",
-                    "title": "National Corrections Reporting Program, 2004"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Corrections Reporting Program, 2005",
-            "description": "The National Corrections Reporting Program gathers data on prisoners entering and leaving the custody or supervision of state and federal authorities. The dataset is comprised of four types of data: prisoners who were admitted to prison (Part 1), released from prison (Part 2), released from parole (Part 3), or in prison at year end (Part 4).\r\nThe National Prison Statistics (NPS) program was established in 1926 by the Bureau of the Census in response to a congressional mandate to compile national information on the populations confined in correctional institutions. This program described the characteristics and counts of prison inmates during each calendar year. Since its initiation, responsibility for this program has shifted among several agencies -- in 1950 it was transferred to the Federal Bureau of Prisons and to the Law Enforcement Assistance Administration in 1971. Since 1972, the Bureau of Census, under agreement with the Department of Justice, has had responsibility for compiling the statistical data. Census staff negotiates directly with each state, assembles and edits the data, and prepares the data for analysis and publication.",
-            "modified": "2013-01-18T09:29:03",
-            "accessLevel": "restricted public",
-            "identifier": "1081",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "National Corrections Reporting Program, 2004"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Corrections Reporting Program gathers data on prisoners entering and leaving the custody or supervision of state and federal authorities. The dataset is comprised of four types of data: prisoners who were admitted to prison (Part 1), released from prison (Part 2), released from parole (Part 3), or in prison at year end (Part 4).\r\nThe National Prison Statistics (NPS) program was established in 1926 by the Bureau of the Census in response to a congressional mandate to compile national information on the populations confined in correctional institutions. This program described the characteristics and counts of prison inmates during each calendar year. Since its initiation, responsibility for this program has shifted among several agencies -- in 1950 it was transferred to the Federal Bureau of Prisons and to the Law Enforcement Assistance Administration in 1971. Since 1972, the Bureau of Census, under agreement with the Department of Justice, has had responsibility for compiling the statistical data. Census staff negotiates directly with each state, assembles and edits the data, and prepares the data for analysis and publication.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR27742.v2",
+                    "title": "National Corrections Reporting Program, 2005"
+                }
+            ],
+            "identifier": "1081",
+            "isPartOf": "2589",
+            "issued": "2011-03-23T14:38:49",
             "keyword": [
                 "correctional facilities",
                 "correctional facilities (juveniles)",
@@ -34893,55 +34887,55 @@
                 "probation",
                 "state correctional facilities"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-01-18T09:29:03",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2589",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2011-03-23T14:38:49",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR27742.v2",
-                    "title": "National Corrections Reporting Program, 2005"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Corrections Reporting Program, 2006",
-            "description": "The National Corrections Reporting Program gathers data on prisoners entering and leaving the custody or supervision of state and federal authorities. The dataset is comprised of four types of data: prisoners who were admitted to prison (Part 1), released from prison (Part 2), released from parole (Part 3), or in prison at year end (Part 4).\r\nThe National Prison Statistics (NPS) program was established in 1926 by the Bureau of the Census in response to a congressional mandate to compile national information on the populations confined in correctional institutions. This program described the characteristics and counts of prison inmates during each calendar year. Since its initiation, responsibility for this program has shifted among several agencies -- in 1950 it was transferred to the Federal Bureau of Prisons and to the Law Enforcement Assistance Administration in 1971. Since 1972, the Bureau of Census, under agreement with the Department of Justice, has had responsibility for compiling the statistical data. Census staff negotiates directly with each state, assembles and edits the data, and prepares the data for analysis and publication.",
-            "modified": "2012-03-01T10:17:47",
-            "accessLevel": "restricted public",
-            "identifier": "1082",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "National Corrections Reporting Program, 2005"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Corrections Reporting Program gathers data on prisoners entering and leaving the custody or supervision of state and federal authorities. The dataset is comprised of four types of data: prisoners who were admitted to prison (Part 1), released from prison (Part 2), released from parole (Part 3), or in prison at year end (Part 4).\r\nThe National Prison Statistics (NPS) program was established in 1926 by the Bureau of the Census in response to a congressional mandate to compile national information on the populations confined in correctional institutions. This program described the characteristics and counts of prison inmates during each calendar year. Since its initiation, responsibility for this program has shifted among several agencies -- in 1950 it was transferred to the Federal Bureau of Prisons and to the Law Enforcement Assistance Administration in 1971. Since 1972, the Bureau of Census, under agreement with the Department of Justice, has had responsibility for compiling the statistical data. Census staff negotiates directly with each state, assembles and edits the data, and prepares the data for analysis and publication.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR30641.v1",
+                    "title": "National Corrections Reporting Program, 2006"
+                }
+            ],
+            "identifier": "1082",
+            "isPartOf": "2589",
+            "issued": "2012-03-01T10:14:44",
             "keyword": [
                 "correctional facilities",
                 "correctional facilities (juveniles)",
@@ -34958,55 +34952,55 @@
                 "probation",
                 "state correctional facilities"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2012-03-01T10:17:47",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2589",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2012-03-01T10:14:44",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR30641.v1",
-                    "title": "National Corrections Reporting Program, 2006"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Corrections Reporting Program, 2007",
-            "description": "The National Corrections Reporting Program gathers data on prisoners entering and leaving the custody or supervision of state and federal authorities. The dataset is comprised of four types of data: prisoners who were admitted to prison (Part 1), released from prison (Part 2), released from parole (Part 3), or in prison at year end (Part 4).\r\nThe National Prison Statistics (NPS) program was established in 1926 by the Bureau of the Census in response to a congressional mandate to compile national information on the populations confined in correctional institutions. This program described the characteristics and counts of prison inmates during each calendar year. Since its initiation, responsibility for this program has shifted among several agencies -- in 1950 it was transferred to the Federal Bureau of Prisons and to the Law Enforcement Assistance Administration in 1971. Since 1972, the Bureau of Census, under agreement with the Department of Justice, has had responsibility for compiling the statistical data. Census staff negotiates directly with each state, assembles and edits the data, and prepares the data for analysis and publication.",
-            "modified": "2012-02-29T16:50:34",
-            "accessLevel": "restricted public",
-            "identifier": "1083",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "National Corrections Reporting Program, 2006"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Corrections Reporting Program gathers data on prisoners entering and leaving the custody or supervision of state and federal authorities. The dataset is comprised of four types of data: prisoners who were admitted to prison (Part 1), released from prison (Part 2), released from parole (Part 3), or in prison at year end (Part 4).\r\nThe National Prison Statistics (NPS) program was established in 1926 by the Bureau of the Census in response to a congressional mandate to compile national information on the populations confined in correctional institutions. This program described the characteristics and counts of prison inmates during each calendar year. Since its initiation, responsibility for this program has shifted among several agencies -- in 1950 it was transferred to the Federal Bureau of Prisons and to the Law Enforcement Assistance Administration in 1971. Since 1972, the Bureau of Census, under agreement with the Department of Justice, has had responsibility for compiling the statistical data. Census staff negotiates directly with each state, assembles and edits the data, and prepares the data for analysis and publication.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR30081.v1",
+                    "title": "National Corrections Reporting Program, 2007"
+                }
+            ],
+            "identifier": "1083",
+            "isPartOf": "2589",
+            "issued": "2012-02-28T16:02:22",
             "keyword": [
                 "correctional facilities",
                 "correctional facilities (juveniles)",
@@ -35023,55 +35017,55 @@
                 "probation",
                 "state correctional facilities"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2012-02-29T16:50:34",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2589",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2012-02-28T16:02:22",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR30081.v1",
-                    "title": "National Corrections Reporting Program, 2007"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Corrections Reporting Program, 2008",
-            "description": "The National Corrections Reporting Program gathers data on prisoners entering and leaving the custody or supervision of state and federal authorities. The dataset is comprised of four types of data: prisoners who were admitted to prison (Part 1), released from prison (Part 2), released from parole (Part 3), or in prison at year end (Part 4).\r\nThe National Prison Statistics (NPS) program was established in 1926 by the Bureau of the Census in response to a congressional mandate to compile national information on the populations confined in correctional institutions. This program described the characteristics and counts of prison inmates during each calendar year. Since its initiation, responsibility for this program has shifted among several agencies -- in 1950 it was transferred to the Federal Bureau of Prisons and to the Law Enforcement Assistance Administration in 1971. Since 1972, the Bureau of Census, under agreement with the Department of Justice, has had responsibility for compiling the statistical data. Census staff negotiates directly with each state, assembles and edits the data, and prepares the data for analysis and publication.",
-            "modified": "2012-01-31T11:47:52",
-            "accessLevel": "restricted public",
-            "identifier": "1084",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "National Corrections Reporting Program, 2007"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Corrections Reporting Program gathers data on prisoners entering and leaving the custody or supervision of state and federal authorities. The dataset is comprised of four types of data: prisoners who were admitted to prison (Part 1), released from prison (Part 2), released from parole (Part 3), or in prison at year end (Part 4).\r\nThe National Prison Statistics (NPS) program was established in 1926 by the Bureau of the Census in response to a congressional mandate to compile national information on the populations confined in correctional institutions. This program described the characteristics and counts of prison inmates during each calendar year. Since its initiation, responsibility for this program has shifted among several agencies -- in 1950 it was transferred to the Federal Bureau of Prisons and to the Law Enforcement Assistance Administration in 1971. Since 1972, the Bureau of Census, under agreement with the Department of Justice, has had responsibility for compiling the statistical data. Census staff negotiates directly with each state, assembles and edits the data, and prepares the data for analysis and publication.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR30082.v1",
+                    "title": "National Corrections Reporting Program, 2008"
+                }
+            ],
+            "identifier": "1084",
+            "isPartOf": "2589",
+            "issued": "2012-01-31T11:38:28",
             "keyword": [
                 "correctional facilities",
                 "correctional facilities (juveniles)",
@@ -35088,55 +35082,55 @@
                 "probation",
                 "state correctional facilities"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2012-01-31T11:47:52",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2589",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2012-01-31T11:38:28",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR30082.v1",
-                    "title": "National Corrections Reporting Program, 2008"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Corrections Reporting Program, 2009",
-            "description": "The National Corrections Reporting Program gathers data on prisoners entering and leaving the custody or supervision of state and federal authorities. The dataset is comprised of four types of data: prisoners who were admitted to prison (Part 1), released from prison (Part 2), released from parole (Part 3), or in prison at year end (Part 4).\r\nThe National Prison Statistics (NPS) program was established in 1926 by the Bureau of the Census in response to a congressional mandate to compile national information on the populations confined in correctional institutions. This program described the characteristics and counts of prison inmates during each calendar year. Since its initiation, responsibility for this program has shifted among several agencies -- in 1950 it was transferred to the Federal Bureau of Prisons and to the Law Enforcement Assistance Administration in 1971. Since 1972, the Bureau of Census, under agreement with the Department of Justice, has had responsibility for compiling the statistical data. Census staff negotiates directly with each state, assembles and edits the data, and prepares the data for analysis and publication.",
-            "modified": "2013-02-11T17:41:27",
-            "accessLevel": "restricted public",
-            "identifier": "1085",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "National Corrections Reporting Program, 2008"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Corrections Reporting Program gathers data on prisoners entering and leaving the custody or supervision of state and federal authorities. The dataset is comprised of four types of data: prisoners who were admitted to prison (Part 1), released from prison (Part 2), released from parole (Part 3), or in prison at year end (Part 4).\r\nThe National Prison Statistics (NPS) program was established in 1926 by the Bureau of the Census in response to a congressional mandate to compile national information on the populations confined in correctional institutions. This program described the characteristics and counts of prison inmates during each calendar year. Since its initiation, responsibility for this program has shifted among several agencies -- in 1950 it was transferred to the Federal Bureau of Prisons and to the Law Enforcement Assistance Administration in 1971. Since 1972, the Bureau of Census, under agreement with the Department of Justice, has had responsibility for compiling the statistical data. Census staff negotiates directly with each state, assembles and edits the data, and prepares the data for analysis and publication.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR30799.v2",
+                    "title": "National Corrections Reporting Program, 2009"
+                }
+            ],
+            "identifier": "1085",
+            "isPartOf": "2589",
+            "issued": "2011-05-06T12:14:38",
             "keyword": [
                 "correctional facilities",
                 "correctional facilities (juveniles)",
@@ -35153,55 +35147,55 @@
                 "probation",
                 "state correctional facilities"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-02-11T17:41:27",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2589",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2011-05-06T12:14:38",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR30799.v2",
-                    "title": "National Corrections Reporting Program, 2009"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Former Prisoner Survey, 2008",
-            "description": "Under the Prison Rape Elimination Act of 2003, Congress mandated that the United States Department of Justice, Bureau of Justice Statistics (BJS) investigate former prisoners' experiences in prison to assist in understanding the incidence and prevalence of sexual victimization within the prison setting. BJS and its subcontractor, NORC at the University of Chicago, led a national data collection effort focusing on prison sexual assault as reported by former state prisoners.\r\nThe focus of the National Former Prisoner Survey (NFPS) was sexual victimization among former state prisoners. The survey was divided into 6 sections. The first two sections were administered using a computer-assisted personal interviewing (CAPI) method and focused on demographic and criminal history information. The remaining sections, covering more sensitive information, were administered using a touch-screen-audio-assisted-computer-self-interviewing (TACASI) method.\r\nSections A and B of the instrument collected demographic and criminal history information, as well as information on placements during the last continuous incarceration. Sections C and D captured detailed inmate-on-inmate sexual victimization during the last continuous incarceration, including the type of sexual activity, identification of facilities at which such incidents occurred, frequency of occurrences, and other specifics regarding sexual victimization. Section E addressed staff-on-inmate sexual victimization and misconduct, whether considered willing or unwilling, and gathered specifics of activity indicated. The last section, F, focused on the impacts of sexual assault on victimized respondents, as well as parole supervision characteristics for all respondents.\r\nThe National Former Prisoner Survey (NFPS) began in January 2008 and concluded in October 2008, and involved the random selection of approximately 250 parole offices across the country using probability proportional-to-size (PPS) sampling procedures.  Completed interviews were obtained for 17,738 respondents; supplemental data was collected on all former prisoners sampled in order to develop weights for national estimations.",
-            "modified": "2012-08-03T14:33:15",
-            "accessLevel": "restricted public",
-            "identifier": "1086",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "National Corrections Reporting Program, 2009"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "Under the Prison Rape Elimination Act of 2003, Congress mandated that the United States Department of Justice, Bureau of Justice Statistics (BJS) investigate former prisoners' experiences in prison to assist in understanding the incidence and prevalence of sexual victimization within the prison setting. BJS and its subcontractor, NORC at the University of Chicago, led a national data collection effort focusing on prison sexual assault as reported by former state prisoners.\r\nThe focus of the National Former Prisoner Survey (NFPS) was sexual victimization among former state prisoners. The survey was divided into 6 sections. The first two sections were administered using a computer-assisted personal interviewing (CAPI) method and focused on demographic and criminal history information. The remaining sections, covering more sensitive information, were administered using a touch-screen-audio-assisted-computer-self-interviewing (TACASI) method.\r\nSections A and B of the instrument collected demographic and criminal history information, as well as information on placements during the last continuous incarceration. Sections C and D captured detailed inmate-on-inmate sexual victimization during the last continuous incarceration, including the type of sexual activity, identification of facilities at which such incidents occurred, frequency of occurrences, and other specifics regarding sexual victimization. Section E addressed staff-on-inmate sexual victimization and misconduct, whether considered willing or unwilling, and gathered specifics of activity indicated. The last section, F, focused on the impacts of sexual assault on victimized respondents, as well as parole supervision characteristics for all respondents.\r\nThe National Former Prisoner Survey (NFPS) began in January 2008 and concluded in October 2008, and involved the random selection of approximately 250 parole offices across the country using probability proportional-to-size (PPS) sampling procedures.  Completed interviews were obtained for 17,738 respondents; supplemental data was collected on all former prisoners sampled in order to develop weights for national estimations.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR31441.v1",
+                    "title": "National Former Prisoner Survey, 2008"
+                }
+            ],
+            "identifier": "1086",
+            "isPartOf": "2442",
+            "issued": "2012-08-03T14:30:56",
             "keyword": [
                 "correctional facilities",
                 "correctional guards",
@@ -35216,55 +35210,55 @@
                 "sexual assault",
                 "sexual behavior"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2012-08-03T14:33:15",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2442",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2012-08-03T14:30:56",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR31441.v1",
-                    "title": "National Former Prisoner Survey, 2008"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Inmate Survey, 2007",
-            "description": "Data for this study were collected as part of the 2007 National Inmate Survey (NIS), which is comprised of two questionnaires -- a survey of sexual victimization and a survey of past drug and alcohol use and abuse. The survey of sexual victimization resulted in data from 23,398 inmates held in 146 sampled prisons and 40,419 inmates in 282 local jails in the NIS.\r\nRespondents were asked if they had been forced or otherwise coerced into any sexual contact with other inmates or facility staff while incarcerated.  The respondents were asked about the type of sexual contact, the frequency, when it occurred, and where it occurred.  The survey also sought information on any injuries received and treatment obtained for those injuries. Other questions pertained to the reporting of sexual contact -- if it was reported, to whom it was reported, and any results from reporting sexual contact.  Respondents were also asked for reasons why they had not reported the sexual contact if no report was made.\r\nBackground and demographic information collected included reasons for incarceration, sexual history, sexual orientation, marital status, gender, ethnicity, and physical characteristics such as height and weight.",
-            "modified": "2012-05-25T10:26:37",
-            "accessLevel": "restricted public",
-            "identifier": "1087",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "National Former Prisoner Survey, 2008"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "Data for this study were collected as part of the 2007 National Inmate Survey (NIS), which is comprised of two questionnaires -- a survey of sexual victimization and a survey of past drug and alcohol use and abuse. The survey of sexual victimization resulted in data from 23,398 inmates held in 146 sampled prisons and 40,419 inmates in 282 local jails in the NIS.\r\nRespondents were asked if they had been forced or otherwise coerced into any sexual contact with other inmates or facility staff while incarcerated.  The respondents were asked about the type of sexual contact, the frequency, when it occurred, and where it occurred.  The survey also sought information on any injuries received and treatment obtained for those injuries. Other questions pertained to the reporting of sexual contact -- if it was reported, to whom it was reported, and any results from reporting sexual contact.  Respondents were also asked for reasons why they had not reported the sexual contact if no report was made.\r\nBackground and demographic information collected included reasons for incarceration, sexual history, sexual orientation, marital status, gender, ethnicity, and physical characteristics such as height and weight.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR26361.v1",
+                    "title": "National Inmate Survey, 2007"
+                }
+            ],
+            "identifier": "1087",
+            "isPartOf": "2442",
+            "issued": "2011-11-11T14:34:54",
             "keyword": [
                 "correctional facilities",
                 "correctional guards",
@@ -35278,55 +35272,55 @@
                 "sexual assault",
                 "sexual behavior"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2012-05-25T10:26:37",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2442",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2011-11-11T14:34:54",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR26361.v1",
-                    "title": "National Inmate Survey, 2007"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Inmate Survey, 2008-2009",
-            "description": "The National Inmate Survey, 2008-2009 (NIS-2) was conducted in 167 state and federal prisons between October 13, 2008, and March 11, 2009; 286 jails between January 20, 2009, and August 13, 2009; and 10 special (military, Indian country, and Immigration and Customs Enforcement (ICE)) facilities between May 11, 2009, and December 17, 2009. The data were collected by RTI International under a cooperative agreement with the Bureau of Justice Statistics (BJS). The NIS-2 comprised two questionnaires -- a survey of sexual victimization and a\r\nsurvey of past drug and alcohol use and treatment. Inmates were randomly assigned to receive one of the questionnaires so that at the time of the interview the content of the survey remained unknown to facility staff and the interviewers. A total of 81,566 inmates participated in the survey, including 32,029 inmates in state and federal prisons, 48,066 inmates in jails, 399 inmates in military facilities, 115 inmates in Indian country jails, and 957 inmates in facilities operated by ICE.\r\nThe respondents were asked about the type of sexual contact, the frequency, when it occurred, and where it occurred. The survey also sought information on any injuries received and the treatment obtained for those injuries. Other questions pertained to the reporting of sexual contact -- if it was reported, to whom it was reported, and any results from reporting sexual contact. Respondents were also asked for reasons why they had not reported the sexual contact if no report was made. Background and demographic information collected includes reasons for incarceration, sexual history, sexual orientation, marital status, gender, ethnicity, and physical characteristics such as height and weight.",
-            "modified": "2014-01-15T15:51:29",
-            "accessLevel": "restricted public",
-            "identifier": "1088",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "National Inmate Survey, 2007"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Inmate Survey, 2008-2009 (NIS-2) was conducted in 167 state and federal prisons between October 13, 2008, and March 11, 2009; 286 jails between January 20, 2009, and August 13, 2009; and 10 special (military, Indian country, and Immigration and Customs Enforcement (ICE)) facilities between May 11, 2009, and December 17, 2009. The data were collected by RTI International under a cooperative agreement with the Bureau of Justice Statistics (BJS). The NIS-2 comprised two questionnaires -- a survey of sexual victimization and a\r\nsurvey of past drug and alcohol use and treatment. Inmates were randomly assigned to receive one of the questionnaires so that at the time of the interview the content of the survey remained unknown to facility staff and the interviewers. A total of 81,566 inmates participated in the survey, including 32,029 inmates in state and federal prisons, 48,066 inmates in jails, 399 inmates in military facilities, 115 inmates in Indian country jails, and 957 inmates in facilities operated by ICE.\r\nThe respondents were asked about the type of sexual contact, the frequency, when it occurred, and where it occurred. The survey also sought information on any injuries received and the treatment obtained for those injuries. Other questions pertained to the reporting of sexual contact -- if it was reported, to whom it was reported, and any results from reporting sexual contact. Respondents were also asked for reasons why they had not reported the sexual contact if no report was made. Background and demographic information collected includes reasons for incarceration, sexual history, sexual orientation, marital status, gender, ethnicity, and physical characteristics such as height and weight.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR34510.v1",
+                    "title": "National Inmate Survey, 2008-2009"
+                }
+            ],
+            "identifier": "1088",
+            "isPartOf": "2442",
+            "issued": "2014-01-15T15:45:59",
             "keyword": [
                 "correctional facilities (adults)",
                 "correctional guards",
@@ -35340,55 +35334,55 @@
                 "sexual assault",
                 "sexual behavior"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2014-01-15T15:51:29",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2442",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2014-01-15T15:45:59",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR34510.v1",
-                    "title": "National Inmate Survey, 2008-2009"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Jail Census, 1999",
-            "description": "The 1999 Census of Jails is the seventh in a series of data\r\ncollection efforts aimed at studying the nation's locally administered\r\njails. Previous censuses were conducted in 1970, 1972, 1978, 1983,\r\n1988, and 1993. The 1999 census enumerated 3,365 locally administered\r\nconfinement facilities that held inmates beyond arraignment and were\r\nstaffed by municipal or county employees. Among these were 47\r\nprivately operated jails under contract for local governments and 42\r\nregional jails that were operated for two or more jail authorities. In\r\naddition, the census identified 11 facilities maintained by the\r\nFederal Bureau of Prisons that functioned as jails. The nationwide\r\ntotal of the number of jails in operation on June 30, 1999, was 3,376.\r\nFor purposes of this data collection, a local jail was defined as a\r\nlocally operated adult detention facility that receives individuals\r\npending arraignment and holds them awaiting trial, conviction, or\r\nsentencing, readmits probation, parole, and bail-bond violators and\r\nabsconders, temporarily detains juveniles pending transfer to juvenile\r\nauthorities, holds mentally ill persons pending their movement to\r\nappropriate health facilities, holds individuals for the military, for\r\nprotective custody, for contempt, and for the courts as witnesses,\r\nreleases convicted inmates to the community upon completion of\r\nsentence, transfers inmates to federal, state, or other authorities,\r\nhouses inmates for federal, state, or other authorities because of\r\ncrowding of their facilities, relinquishes custody of temporary\r\ndetainees to juvenile and medical authorities, operates\r\ncommunity-based programs with day-reporting, home detention,\r\nelectronic monitoring, or other types of supervision, and holds\r\ninmates sentenced to short terms. Variables include information on\r\njail population by legal status, age and sex of prisoners, maximum\r\nsentence, admissions and releases, available services and programs,\r\nstructure and capacity, facility age and use of space, expenditure,\r\nemployment, staff information, and health issues, which include\r\nstatistics on drugs, AIDS, and tuberculosis.",
-            "modified": "2009-07-09T10:27:21",
-            "accessLevel": "restricted public",
-            "identifier": "1089",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "National Inmate Survey, 2008-2009"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The 1999 Census of Jails is the seventh in a series of data\r\ncollection efforts aimed at studying the nation's locally administered\r\njails. Previous censuses were conducted in 1970, 1972, 1978, 1983,\r\n1988, and 1993. The 1999 census enumerated 3,365 locally administered\r\nconfinement facilities that held inmates beyond arraignment and were\r\nstaffed by municipal or county employees. Among these were 47\r\nprivately operated jails under contract for local governments and 42\r\nregional jails that were operated for two or more jail authorities. In\r\naddition, the census identified 11 facilities maintained by the\r\nFederal Bureau of Prisons that functioned as jails. The nationwide\r\ntotal of the number of jails in operation on June 30, 1999, was 3,376.\r\nFor purposes of this data collection, a local jail was defined as a\r\nlocally operated adult detention facility that receives individuals\r\npending arraignment and holds them awaiting trial, conviction, or\r\nsentencing, readmits probation, parole, and bail-bond violators and\r\nabsconders, temporarily detains juveniles pending transfer to juvenile\r\nauthorities, holds mentally ill persons pending their movement to\r\nappropriate health facilities, holds individuals for the military, for\r\nprotective custody, for contempt, and for the courts as witnesses,\r\nreleases convicted inmates to the community upon completion of\r\nsentence, transfers inmates to federal, state, or other authorities,\r\nhouses inmates for federal, state, or other authorities because of\r\ncrowding of their facilities, relinquishes custody of temporary\r\ndetainees to juvenile and medical authorities, operates\r\ncommunity-based programs with day-reporting, home detention,\r\nelectronic monitoring, or other types of supervision, and holds\r\ninmates sentenced to short terms. Variables include information on\r\njail population by legal status, age and sex of prisoners, maximum\r\nsentence, admissions and releases, available services and programs,\r\nstructure and capacity, facility age and use of space, expenditure,\r\nemployment, staff information, and health issues, which include\r\nstatistics on drugs, AIDS, and tuberculosis.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR03318.v3",
+                    "title": "National Jail Census, 1999"
+                }
+            ],
+            "identifier": "1089",
+            "isPartOf": "2169",
+            "issued": "2002-06-07T00:00:00",
             "keyword": [
                 "census data",
                 "correctional facilities",
@@ -35401,55 +35395,55 @@
                 "jail inmates",
                 "jails"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2009-07-09T10:27:21",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2169",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2002-06-07T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR03318.v3",
-                    "title": "National Jail Census, 1999"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Judicial Reporting Program, 1986",
-            "description": "This data collection tabulates the number of persons\r\nconvicted of felonies in state courts and describes the sentences\r\nthese individuals received. Data were collected from state courts and\r\nstate prosecutors in 100 counties of the United States.\r\nSociodemographic information includes age, race, and sex of\r\nfelon. Types of offenses committed include homicide, rape, and\r\nrobbery. Adjudication variables referring to the process between\r\narrest and sentencing are also a part of this dataset. Data can be\r\nanalyzed on a national level or by the individual counties.",
-            "modified": "2011-03-08T09:36:58",
-            "accessLevel": "restricted public",
-            "identifier": "1090",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "National Jail Census, 1999"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This data collection tabulates the number of persons\r\nconvicted of felonies in state courts and describes the sentences\r\nthese individuals received. Data were collected from state courts and\r\nstate prosecutors in 100 counties of the United States.\r\nSociodemographic information includes age, race, and sex of\r\nfelon. Types of offenses committed include homicide, rape, and\r\nrobbery. Adjudication variables referring to the process between\r\narrest and sentencing are also a part of this dataset. Data can be\r\nanalyzed on a national level or by the individual counties.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR09073.v2",
+                    "title": "National Judicial Reporting Program, 1986"
+                }
+            ],
+            "identifier": "1090",
+            "isPartOf": "2176",
+            "issued": "1989-08-02T00:00:00",
             "keyword": [
                 "arrests",
                 "assault",
@@ -35471,55 +35465,55 @@
                 "sentencing",
                 "state courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T09:36:58",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2176",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "1989-08-02T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR09073.v2",
-                    "title": "National Judicial Reporting Program, 1986"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Judicial Reporting Program, 1988",
-            "description": "This data collection tabulates the number of persons\r\nconvicted of felonies in state courts and describes the sentences\r\nthese individuals received. Data were collected from state courts and\r\nstate prosecutors in 100 counties of the United States. The collection\r\ncontains sociodemographic information such as age, race, and sex of\r\nthe felon. Types of offenses committed include homicide, rape, and\r\nrobbery. Adjudication variables referring to the process between\r\narrest and sentencing are also a part of this dataset. Data can be\r\nanalyzed on a national level or by the individual counties.",
-            "modified": "2012-12-07T10:28:18",
-            "accessLevel": "restricted public",
-            "identifier": "1091",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "National Judicial Reporting Program, 1986"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This data collection tabulates the number of persons\r\nconvicted of felonies in state courts and describes the sentences\r\nthese individuals received. Data were collected from state courts and\r\nstate prosecutors in 100 counties of the United States. The collection\r\ncontains sociodemographic information such as age, race, and sex of\r\nthe felon. Types of offenses committed include homicide, rape, and\r\nrobbery. Adjudication variables referring to the process between\r\narrest and sentencing are also a part of this dataset. Data can be\r\nanalyzed on a national level or by the individual counties.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR09449.v2",
+                    "title": "National Judicial Reporting Program, 1988"
+                }
+            ],
+            "identifier": "1091",
+            "isPartOf": "2176",
+            "issued": "1991-05-03T00:00:00",
             "keyword": [
                 "arrests",
                 "assault",
@@ -35541,55 +35535,55 @@
                 "sentencing",
                 "state courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2012-12-07T10:28:18",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2176",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "1991-05-03T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR09449.v2",
-                    "title": "National Judicial Reporting Program, 1988"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Judicial Reporting Program, 1990",
-            "description": "This data collection tabulates the number of persons\r\nconvicted of felonies in state courts and describes their\r\nsentences. Data were collected from state courts and state prosecutors\r\nin 100 counties of the United States. The collection contains\r\nsociodemographic information such as age, race, and sex of the\r\nfelon. Types of offenses committed include homicide, rape, and\r\nrobbery. Adjudication variables referring to the process between\r\narrest and sentencing are also a part of this dataset. Data can be\r\nanalyzed at the national level or by the individual counties.",
-            "modified": "2011-04-14T09:06:59",
-            "accessLevel": "restricted public",
-            "identifier": "1092",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "National Judicial Reporting Program, 1988"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This data collection tabulates the number of persons\r\nconvicted of felonies in state courts and describes their\r\nsentences. Data were collected from state courts and state prosecutors\r\nin 100 counties of the United States. The collection contains\r\nsociodemographic information such as age, race, and sex of the\r\nfelon. Types of offenses committed include homicide, rape, and\r\nrobbery. Adjudication variables referring to the process between\r\narrest and sentencing are also a part of this dataset. Data can be\r\nanalyzed at the national level or by the individual counties.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR06038.v2",
+                    "title": "National Judicial Reporting Program, 1990"
+                }
+            ],
+            "identifier": "1092",
+            "isPartOf": "2176",
+            "issued": "1993-10-02T00:00:00",
             "keyword": [
                 "arrests",
                 "assault",
@@ -35611,55 +35605,55 @@
                 "sentencing",
                 "state courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-04-14T09:06:59",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2176",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "1993-10-02T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR06038.v2",
-                    "title": "National Judicial Reporting Program, 1990"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Judicial Reporting Program, 1992",
-            "description": "This data collection tabulates the number of persons\r\nconvicted of felonies in state courts and describes their\r\nsentences. Data were collected from state courts and state prosecutors\r\nin 100 counties of the United States. The collection contains\r\nsociodemographic information such as age, race, and sex of the\r\nfelon. Types of offenses committed include homicide, rape, and\r\nrobbery. Adjudication variables referring to the process between\r\narrest and sentencing are also a part of this dataset. Data can be\r\nanalyzed at the national level or by the individual counties.",
-            "modified": "2011-04-14T10:19:22",
-            "accessLevel": "restricted public",
-            "identifier": "1093",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "National Judicial Reporting Program, 1990"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This data collection tabulates the number of persons\r\nconvicted of felonies in state courts and describes their\r\nsentences. Data were collected from state courts and state prosecutors\r\nin 100 counties of the United States. The collection contains\r\nsociodemographic information such as age, race, and sex of the\r\nfelon. Types of offenses committed include homicide, rape, and\r\nrobbery. Adjudication variables referring to the process between\r\narrest and sentencing are also a part of this dataset. Data can be\r\nanalyzed at the national level or by the individual counties.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR06509.v2",
+                    "title": "National Judicial Reporting Program, 1992"
+                }
+            ],
+            "identifier": "1093",
+            "isPartOf": "2176",
+            "issued": "1995-10-30T00:00:00",
             "keyword": [
                 "arrests",
                 "assault",
@@ -35681,55 +35675,55 @@
                 "sentencing",
                 "state courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-04-14T10:19:22",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2176",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "1995-10-30T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR06509.v2",
-                    "title": "National Judicial Reporting Program, 1992"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Judicial Reporting Program, 1994",
-            "description": "This data collection tabulates the number of persons\r\nconvicted of felonies in state courts and describes their\r\nsentences. Data were collected from state courts and state prosecutors\r\nin 100 counties of the United States. The collection contains\r\nsociodemographic information such as age, race, and sex of the\r\nfelon. Types of offenses committed include homicide, rape, and\r\nrobbery. Adjudication variables referring to the process between\r\narrest and sentencing are also a part of this dataset. Data can be\r\nanalyzed at the national level or by individual counties.",
-            "modified": "2012-11-06T08:59:36",
-            "accessLevel": "restricted public",
-            "identifier": "1094",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "National Judicial Reporting Program, 1992"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This data collection tabulates the number of persons\r\nconvicted of felonies in state courts and describes their\r\nsentences. Data were collected from state courts and state prosecutors\r\nin 100 counties of the United States. The collection contains\r\nsociodemographic information such as age, race, and sex of the\r\nfelon. Types of offenses committed include homicide, rape, and\r\nrobbery. Adjudication variables referring to the process between\r\narrest and sentencing are also a part of this dataset. Data can be\r\nanalyzed at the national level or by individual counties.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR06855.v2",
+                    "title": "National Judicial Reporting Program, 1994"
+                }
+            ],
+            "identifier": "1094",
+            "isPartOf": "2176",
+            "issued": "1997-07-18T00:00:00",
             "keyword": [
                 "arrests",
                 "assault",
@@ -35751,55 +35745,55 @@
                 "sentencing",
                 "state courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2012-11-06T08:59:36",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2176",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "1997-07-18T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR06855.v2",
-                    "title": "National Judicial Reporting Program, 1994"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Judicial Reporting Program, 1996",
-            "description": "This data collection tabulates the number of persons\r\nconvicted of felonies in state courts and describes their\r\nsentences. Data were collected from state courts and state prosecutors\r\nin 344 counties of the United States. The collection contains\r\nsociodemographic information such as age, race, and sex of the\r\nfelon. Types of offenses committed include homicide, rape, and\r\nrobbery. Adjudication variables referring to the process between\r\narrest and sentencing are also a part of this dataset. Data can be\r\nanalyzed at the national level or by individual counties.",
-            "modified": "2011-04-08T10:00:11",
-            "accessLevel": "restricted public",
-            "identifier": "1095",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "National Judicial Reporting Program, 1994"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This data collection tabulates the number of persons\r\nconvicted of felonies in state courts and describes their\r\nsentences. Data were collected from state courts and state prosecutors\r\nin 344 counties of the United States. The collection contains\r\nsociodemographic information such as age, race, and sex of the\r\nfelon. Types of offenses committed include homicide, rape, and\r\nrobbery. Adjudication variables referring to the process between\r\narrest and sentencing are also a part of this dataset. Data can be\r\nanalyzed at the national level or by individual counties.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR02660.v3",
+                    "title": "National Judicial Reporting Program, 1996"
+                }
+            ],
+            "identifier": "1095",
+            "isPartOf": "2176",
+            "issued": "1999-05-12T00:00:00",
             "keyword": [
                 "arrests",
                 "assault",
@@ -35821,55 +35815,55 @@
                 "sentencing",
                 "state courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-04-08T10:00:11",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2176",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "1999-05-12T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR02660.v3",
-                    "title": "National Judicial Reporting Program, 1996"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Judicial Reporting Program, 1998",
-            "description": "This data collection tabulates the number of persons\r\nconvicted of felonies in state courts and describes their sentences.\r\nData were collected from state courts and state prosecutors in 344\r\ncounties of the United States. The collection contains\r\nsociodemographic information such as age, race, and sex of the felon.\r\nTypes of offenses committed include homicide, rape, and robbery.\r\nAdjudication variables referring to the process between arrest and\r\nsentencing are also a part of this dataset. Data can be analyzed at\r\nthe national level or by individual counties.",
-            "modified": "2011-04-11T12:14:52",
-            "accessLevel": "restricted public",
-            "identifier": "1096",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "National Judicial Reporting Program, 1996"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This data collection tabulates the number of persons\r\nconvicted of felonies in state courts and describes their sentences.\r\nData were collected from state courts and state prosecutors in 344\r\ncounties of the United States. The collection contains\r\nsociodemographic information such as age, race, and sex of the felon.\r\nTypes of offenses committed include homicide, rape, and robbery.\r\nAdjudication variables referring to the process between arrest and\r\nsentencing are also a part of this dataset. Data can be analyzed at\r\nthe national level or by individual counties.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR03316.v2",
+                    "title": "National Judicial Reporting Program, 1998"
+                }
+            ],
+            "identifier": "1096",
+            "isPartOf": "2176",
+            "issued": "2002-02-15T00:00:00",
             "keyword": [
                 "arrests",
                 "assault",
@@ -35891,55 +35885,55 @@
                 "sentencing",
                 "state courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-04-11T12:14:52",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2176",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2002-02-15T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR03316.v2",
-                    "title": "National Judicial Reporting Program, 1998"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Judicial Reporting Program, 2000",
-            "description": "This data collection provides detailed information on the\r\nsentences and characteristics of convicted felons based on data\r\ncollected from state courts. The 2000 survey was based on a sample of\r\n344 counties selected to be nationally representative. The collection\r\ncontains sociodemographic information such as age, race, and sex of\r\nthe felon. Types of offenses committed include homicide, rape, and\r\nrobbery. Adjudication variables referring to the process between\r\narrest and sentencing are also a part of this dataset. Data can be\r\nanalyzed at the national level or by individual counties.",
-            "modified": "2011-04-11T14:47:08",
-            "accessLevel": "restricted public",
-            "identifier": "1097",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "National Judicial Reporting Program, 1998"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This data collection provides detailed information on the\r\nsentences and characteristics of convicted felons based on data\r\ncollected from state courts. The 2000 survey was based on a sample of\r\n344 counties selected to be nationally representative. The collection\r\ncontains sociodemographic information such as age, race, and sex of\r\nthe felon. Types of offenses committed include homicide, rape, and\r\nrobbery. Adjudication variables referring to the process between\r\narrest and sentencing are also a part of this dataset. Data can be\r\nanalyzed at the national level or by individual counties.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR03802.v1",
+                    "title": "National Judicial Reporting Program, 2000"
+                }
+            ],
+            "identifier": "1097",
+            "isPartOf": "2176",
+            "issued": "2003-09-10T00:00:00",
             "keyword": [
                 "arrests",
                 "assault",
@@ -35961,55 +35955,55 @@
                 "sentencing",
                 "state courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-04-11T14:47:08",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2176",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2003-09-10T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR03802.v1",
-                    "title": "National Judicial Reporting Program, 2000"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Judicial Reporting Program, 2002: [United States]",
-            "description": "This data collection provides detailed information on the\r\nsentences and characteristics of convicted felons based on data\r\ncollected from state courts. The 2002 survey was based on a sample of\r\n300 counties selected to be nationally representative. The collection\r\ncontains sociodemographic information such as age, race, and sex of\r\nthe felon. Types of offenses committed include homicide, rape, and\r\nrobbery. Data can be analyzed at the national level or by individual\r\ncounties.",
-            "modified": "2011-03-08T09:30:33",
-            "accessLevel": "restricted public",
-            "identifier": "1098",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "National Judicial Reporting Program, 2000"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This data collection provides detailed information on the\r\nsentences and characteristics of convicted felons based on data\r\ncollected from state courts. The 2002 survey was based on a sample of\r\n300 counties selected to be nationally representative. The collection\r\ncontains sociodemographic information such as age, race, and sex of\r\nthe felon. Types of offenses committed include homicide, rape, and\r\nrobbery. Data can be analyzed at the national level or by individual\r\ncounties.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR04203.v3",
+                    "title": "National Judicial Reporting Program, 2002: [United States]"
+                }
+            ],
+            "identifier": "1098",
+            "isPartOf": "2176",
+            "issued": "2005-04-01T00:00:00",
             "keyword": [
                 "assault",
                 "auto theft",
@@ -36030,55 +36024,55 @@
                 "sentencing",
                 "state courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T09:30:33",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2176",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2005-04-01T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR04203.v3",
-                    "title": "National Judicial Reporting Program, 2002: [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Judicial Reporting Program, 2004",
-            "description": "This data collection provides detailed information on the\r\nsentences and characteristics of convicted felons based on data\r\ncollected from state courts. The 2004 survey was based on a sample of\r\n300 counties selected to be nationally representative. The collection\r\ncontains sociodemographic information such as age, race, and sex of\r\nthe felon. Types of offenses committed include homicide, rape, and\r\nrobbery. Data can be analyzed at the national level or by individual\r\ncounties.",
-            "modified": "2011-03-08T09:39:03",
-            "accessLevel": "restricted public",
-            "identifier": "1099",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "National Judicial Reporting Program, 2002: [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This data collection provides detailed information on the\r\nsentences and characteristics of convicted felons based on data\r\ncollected from state courts. The 2004 survey was based on a sample of\r\n300 counties selected to be nationally representative. The collection\r\ncontains sociodemographic information such as age, race, and sex of\r\nthe felon. Types of offenses committed include homicide, rape, and\r\nrobbery. Data can be analyzed at the national level or by individual\r\ncounties.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR20760.v2",
+                    "title": "National Judicial Reporting Program, 2004"
+                }
+            ],
+            "identifier": "1099",
+            "isPartOf": "2176",
+            "issued": "2007-10-29T00:00:00",
             "keyword": [
                 "assault",
                 "auto theft",
@@ -36099,55 +36093,55 @@
                 "sentencing",
                 "state courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T09:39:03",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2176",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2007-10-29T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR20760.v2",
-                    "title": "National Judicial Reporting Program, 2004"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Judicial Reporting Program, 2006",
-            "description": "This data collection provides detailed information on the\r\nsentences and characteristics of convicted felons based on data\r\ncollected from state courts. The 2006 survey was based on a sample of\r\n300 counties selected to be nationally representative. The collection\r\ncontains sociodemographic information such as age, race, and sex of\r\nthe felon. Types of offenses committed include murder, rape, and\r\nrobbery. Data can be analyzed at the national level or by individual\r\ncounties.",
-            "modified": "2011-03-08T12:07:49",
-            "accessLevel": "restricted public",
-            "identifier": "1100",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "National Judicial Reporting Program, 2004"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This data collection provides detailed information on the\r\nsentences and characteristics of convicted felons based on data\r\ncollected from state courts. The 2006 survey was based on a sample of\r\n300 counties selected to be nationally representative. The collection\r\ncontains sociodemographic information such as age, race, and sex of\r\nthe felon. Types of offenses committed include murder, rape, and\r\nrobbery. Data can be analyzed at the national level or by individual\r\ncounties.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR27701.v2",
+                    "title": "National Judicial Reporting Program, 2006"
+                }
+            ],
+            "identifier": "1100",
+            "isPartOf": "2176",
+            "issued": "2010-11-12T14:34:40",
             "keyword": [
                 "assault",
                 "auto theft",
@@ -36168,55 +36162,55 @@
                 "sentencing",
                 "state courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T12:07:49",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2176",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2010-11-12T14:34:40",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR27701.v2",
-                    "title": "National Judicial Reporting Program, 2006"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Prosecutors Survey, 1990",
-            "description": "This survey queried chief prosecuting attorneys of state\r\nprosecutorial districts (district attorneys, commonwealth attorneys,\r\netc.) about the prosecution of felony cases within their jurisdictions\r\nduring 1989-1990. Questions regarding the prefiling, filing, and\r\npretrial stages of felony prosecution asked about policies limiting\r\nthe time for plea negotiations, the role of the grand jury, how felony\r\ncases were screened, and the amount of time that usually elapsed\r\nbefore the prosecutor was notified of persons arrested for a felony.\r\nProsecutors were also asked to report the percentage of court case\r\nfilings by grand jury indictment, by information following a\r\npreliminary hearing, or by other means, and the percentage of felony\r\ncases processed by a court of general jurisdiction, a felony court, or\r\nother court(s). The trial stage of felony prosecution was covered by\r\nquestions about the conduct of voir dire examination of prospective\r\njurors, limits on time allowed to commence trial, the number of\r\npermitted peremptory challenges, who was responsible for notifying\r\ngovernment witnesses to appear in court, whether the prosecution had\r\nthe right to request a jury trial, whether the jurisdiction's felony\r\ncourt discouraged motions on trial date that would delay trial, and\r\nwhether the felony court normally granted a continuance on trial date\r\nto permit additional time for plea negotiations. Questions on felony\r\nsentencing and appeals asked whether the prosecutor was usually\r\npresent at felony sentence proceedings, whether the judge usually\r\nordered a presentence report, whether victim information was requested\r\nor provided by the court, whether the prosecutor normally recommended\r\na type or duration of sentence to be imposed, whether police, victims,\r\nor witnesses were notified of the disposition of felony cases, whether\r\nthe prosecutor was involved in various types of appellate work, and\r\nwhether the prosecutor had any right of appeal from rulings on\r\nmotions, from sentences, and from determination of guilt or\r\ninnocence. General information gathered by the survey includes the\r\nnumber of jurisdictions contained in the prosecutorial district, the\r\nnumber of attorneys and investigators employed in the sampled\r\njurisdiction and in the prosecutorial district as a whole, the length\r\nof the prosecutor's term of office, the number of law enforcement\r\nagencies that brought arrests into the jurisdiction's court, how much\r\nof the prosecutor's felony caseload was assigned on a vertical basis,\r\nthe kinds of nonfelony matters the prosecutor had responsibility for\r\nor jurisdiction over (e.g., family and domestic relations, mental\r\ncommitments, environmental protection, traffic, etc.), whether the\r\noffice of prosecutor was an elective position, and whether it was a\r\nfull- or part-time position. Other general items include whether any\r\nfelony defendants were provided an attorney on the grounds of\r\nindigency, whether, in criminal cases involving both state and federal\r\njurisdiction, the prosecutor would ordinarily be cross-designated to\r\nrepresent the prosecutor in both courts, whether the prosecutor's\r\noffice contained a \"career criminal\" unit, whether the state's\r\nattorney general was entitled to try cases in the jurisdiction's\r\nfelony court, which types of criminal history data normally were of\r\npractical value in felony prosecution, and who supervised the\r\nprobationer in most cases of adult felons sentenced to probation.",
-            "modified": "2005-11-04T00:00:00",
-            "accessLevel": "restricted public",
-            "identifier": "1101",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "National Judicial Reporting Program, 2006"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This survey queried chief prosecuting attorneys of state\r\nprosecutorial districts (district attorneys, commonwealth attorneys,\r\netc.) about the prosecution of felony cases within their jurisdictions\r\nduring 1989-1990. Questions regarding the prefiling, filing, and\r\npretrial stages of felony prosecution asked about policies limiting\r\nthe time for plea negotiations, the role of the grand jury, how felony\r\ncases were screened, and the amount of time that usually elapsed\r\nbefore the prosecutor was notified of persons arrested for a felony.\r\nProsecutors were also asked to report the percentage of court case\r\nfilings by grand jury indictment, by information following a\r\npreliminary hearing, or by other means, and the percentage of felony\r\ncases processed by a court of general jurisdiction, a felony court, or\r\nother court(s). The trial stage of felony prosecution was covered by\r\nquestions about the conduct of voir dire examination of prospective\r\njurors, limits on time allowed to commence trial, the number of\r\npermitted peremptory challenges, who was responsible for notifying\r\ngovernment witnesses to appear in court, whether the prosecution had\r\nthe right to request a jury trial, whether the jurisdiction's felony\r\ncourt discouraged motions on trial date that would delay trial, and\r\nwhether the felony court normally granted a continuance on trial date\r\nto permit additional time for plea negotiations. Questions on felony\r\nsentencing and appeals asked whether the prosecutor was usually\r\npresent at felony sentence proceedings, whether the judge usually\r\nordered a presentence report, whether victim information was requested\r\nor provided by the court, whether the prosecutor normally recommended\r\na type or duration of sentence to be imposed, whether police, victims,\r\nor witnesses were notified of the disposition of felony cases, whether\r\nthe prosecutor was involved in various types of appellate work, and\r\nwhether the prosecutor had any right of appeal from rulings on\r\nmotions, from sentences, and from determination of guilt or\r\ninnocence. General information gathered by the survey includes the\r\nnumber of jurisdictions contained in the prosecutorial district, the\r\nnumber of attorneys and investigators employed in the sampled\r\njurisdiction and in the prosecutorial district as a whole, the length\r\nof the prosecutor's term of office, the number of law enforcement\r\nagencies that brought arrests into the jurisdiction's court, how much\r\nof the prosecutor's felony caseload was assigned on a vertical basis,\r\nthe kinds of nonfelony matters the prosecutor had responsibility for\r\nor jurisdiction over (e.g., family and domestic relations, mental\r\ncommitments, environmental protection, traffic, etc.), whether the\r\noffice of prosecutor was an elective position, and whether it was a\r\nfull- or part-time position. Other general items include whether any\r\nfelony defendants were provided an attorney on the grounds of\r\nindigency, whether, in criminal cases involving both state and federal\r\njurisdiction, the prosecutor would ordinarily be cross-designated to\r\nrepresent the prosecutor in both courts, whether the prosecutor's\r\noffice contained a \"career criminal\" unit, whether the state's\r\nattorney general was entitled to try cases in the jurisdiction's\r\nfelony court, which types of criminal history data normally were of\r\npractical value in felony prosecution, and who supervised the\r\nprobationer in most cases of adult felons sentenced to probation.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR09579.v1",
+                    "title": "National Prosecutors Survey, 1990"
+                }
+            ],
+            "identifier": "1101",
+            "isPartOf": "2181",
+            "issued": "1992-03-04T00:00:00",
             "keyword": [
                 "attorneys",
                 "case processing",
@@ -36232,55 +36226,55 @@
                 "state courts",
                 "trial procedures"
             ],
-            "bureauCode": [
-                "011:21"
-            ],
-            "programCode": [
-                "011:061"
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2181",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "1992-03-04T00:00:00",
             "language": [
                 "eng"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR09579.v1",
-                    "title": "National Prosecutors Survey, 1990"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Prosecutors Survey, 1992",
-            "description": "This survey queried chief prosecuting attorneys of state\r\nprosecutorial districts (district attorneys, commonwealth attorneys,\r\netc.) about the prosecution of felony cases within their jurisdictions\r\nduring 1991 and 1992. Some items included in an earlier survey,\r\nNATIONAL PROSECUTORS SURVEY, 1990 (ICPSR 9579), were repeated,\r\ncovering topics such as new methods of prosecution, new kinds of\r\nevidence, use of criminal history data, general workload statistics,\r\nfunding, plea negotiations, sentencing of intermediate sanctions,\r\nrelationships with victims and other persons aiding prosecution,\r\ncriminal defense of indigents, and the use of lower courts and grand\r\njuries. New areas of concern in 1992 included staffing, turnover,\r\nrecruitment, new kinds of felonies, problem cases, scientific\r\nevidence, computerization, staff training, drug testing, and the\r\npersonal risks associated with the role of prosecutor. Demographic\r\ndata include sex, race, and ethnic composition of current staff\r\nmembers.",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "modified": "2005-11-04T00:00:00",
-            "accessLevel": "restricted public",
-            "identifier": "1102",
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
+            "title": "National Prosecutors Survey, 1990"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This survey queried chief prosecuting attorneys of state\r\nprosecutorial districts (district attorneys, commonwealth attorneys,\r\netc.) about the prosecution of felony cases within their jurisdictions\r\nduring 1991 and 1992. Some items included in an earlier survey,\r\nNATIONAL PROSECUTORS SURVEY, 1990 (ICPSR 9579), were repeated,\r\ncovering topics such as new methods of prosecution, new kinds of\r\nevidence, use of criminal history data, general workload statistics,\r\nfunding, plea negotiations, sentencing of intermediate sanctions,\r\nrelationships with victims and other persons aiding prosecution,\r\ncriminal defense of indigents, and the use of lower courts and grand\r\njuries. New areas of concern in 1992 included staffing, turnover,\r\nrecruitment, new kinds of felonies, problem cases, scientific\r\nevidence, computerization, staff training, drug testing, and the\r\npersonal risks associated with the role of prosecutor. Demographic\r\ndata include sex, race, and ethnic composition of current staff\r\nmembers.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR06273.v1",
+                    "title": "National Prosecutors Survey, 1992"
+                }
+            ],
+            "identifier": "1102",
+            "isPartOf": "2181",
+            "issued": "1994-05-20T00:00:00",
             "keyword": [
                 "attorneys",
                 "case processing",
@@ -36299,55 +36293,55 @@
                 "trial procedures",
                 "victim services"
             ],
-            "bureauCode": [
-                "011:21"
-            ],
-            "programCode": [
-                "011:061"
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2181",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "1994-05-20T00:00:00",
             "language": [
                 "eng"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR06273.v1",
-                    "title": "National Prosecutors Survey, 1992"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Prosecutors Survey, 1994",
-            "description": "The National Survey of Prosecutors is a biennial survey of\r\nchief prosecutors in state court systems. A chief prosecutor is an\r\nofficial, usually locally elected and typically with the title of\r\ndistrict attorney or county attorney, who is in charge of a\r\nprosecutorial district made up of one or more counties, and who\r\nconducts or supervises the prosecution of felony cases in a state\r\ncourt system. Prosecutors in courts of limited jurisdiction, such as\r\nmunicipal prosecutors, were not included in the survey. The survey's\r\npurpose was to obtain detailed descriptive information on prosecutors'\r\noffices, as well as information on their policies and practices. The\r\ndata collection instrument was based on questions that were included\r\nin the NATIONAL PROSECUTORS SURVEY, 1992 (ICPSR 6273), and also added\r\nqueries on topics of current concern, including: cross-designation of\r\nstate prosecutors to try cases in federal court, juvenile transfers to\r\ncriminal court, personal liability insurance for prosecutors, and\r\ninvolvement with community-based drug abuse programs. Variables\r\ninclude whether certain categories of felony prosecution, such as\r\ngangs, hate crimes, domestic violence, stalking, fraud, or child abuse\r\nor abduction were handled, whether DNA evidence, videotape, expert or\r\nchild witnesses, polygraph tests, or wiretap evidence were used in\r\ntrials, types of intermediate sanctions used, including house arrest,\r\nelectronic monitoring, work release, substance abuse rehabilitation or\r\ntherapy, community service, and fines or restitution, information on\r\nproblem cases, personal risks associated with the role of the\r\nprosecutor, civil actions against prosecutors, criminal defense of\r\nindigent offenders, staffing, workload, funding, whether the\r\ndefendant's criminal history was used in trials, juvenile matters,\r\nrelationships with victims and other persons aiding prosecution,\r\ncomputerization, and community leadership. The unit of analysis is the\r\ndistrict office.",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "modified": "2005-11-04T00:00:00",
-            "accessLevel": "restricted public",
-            "identifier": "1103",
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
+            "title": "National Prosecutors Survey, 1992"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Survey of Prosecutors is a biennial survey of\r\nchief prosecutors in state court systems. A chief prosecutor is an\r\nofficial, usually locally elected and typically with the title of\r\ndistrict attorney or county attorney, who is in charge of a\r\nprosecutorial district made up of one or more counties, and who\r\nconducts or supervises the prosecution of felony cases in a state\r\ncourt system. Prosecutors in courts of limited jurisdiction, such as\r\nmunicipal prosecutors, were not included in the survey. The survey's\r\npurpose was to obtain detailed descriptive information on prosecutors'\r\noffices, as well as information on their policies and practices. The\r\ndata collection instrument was based on questions that were included\r\nin the NATIONAL PROSECUTORS SURVEY, 1992 (ICPSR 6273), and also added\r\nqueries on topics of current concern, including: cross-designation of\r\nstate prosecutors to try cases in federal court, juvenile transfers to\r\ncriminal court, personal liability insurance for prosecutors, and\r\ninvolvement with community-based drug abuse programs. Variables\r\ninclude whether certain categories of felony prosecution, such as\r\ngangs, hate crimes, domestic violence, stalking, fraud, or child abuse\r\nor abduction were handled, whether DNA evidence, videotape, expert or\r\nchild witnesses, polygraph tests, or wiretap evidence were used in\r\ntrials, types of intermediate sanctions used, including house arrest,\r\nelectronic monitoring, work release, substance abuse rehabilitation or\r\ntherapy, community service, and fines or restitution, information on\r\nproblem cases, personal risks associated with the role of the\r\nprosecutor, civil actions against prosecutors, criminal defense of\r\nindigent offenders, staffing, workload, funding, whether the\r\ndefendant's criminal history was used in trials, juvenile matters,\r\nrelationships with victims and other persons aiding prosecution,\r\ncomputerization, and community leadership. The unit of analysis is the\r\ndistrict office.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR06785.v1",
+                    "title": "National Prosecutors Survey, 1994"
+                }
+            ],
+            "identifier": "1103",
+            "isPartOf": "2181",
+            "issued": "1997-02-13T00:00:00",
             "keyword": [
                 "attorneys",
                 "case processing",
@@ -36365,55 +36359,55 @@
                 "treatment programs",
                 "trial procedures"
             ],
-            "bureauCode": [
-                "011:21"
-            ],
-            "programCode": [
-                "011:061"
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2181",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "1997-02-13T00:00:00",
             "language": [
                 "eng"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR06785.v1",
-                    "title": "National Prosecutors Survey, 1994"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Prosecutors Survey, 1996",
-            "description": "The National Survey of Prosecutors is a biennial survey of\r\nchief prosecutors in state court systems. A chief prosecutor is an\r\nofficial, usually locally elected and typically with the title of\r\ndistrict attorney or county attorney, who is in charge of a\r\nprosecutorial district made up of one or more counties, and who\r\nconducts or supervises the prosecution of felony cases in a state\r\ncourt system. Prosecutors in courts of limited jurisdiction, such as\r\nmunicipal prosecutors, were not included in the survey. The survey's\r\npurpose was to obtain detailed descriptive information on prosecutors'\r\noffices, as well as information on their policies and practices. The\r\ndata collection instrument was based on questions that were included\r\nin the NATIONAL PROSECUTORS SURVEY, 1994 (ICPSR 6785), and also added\r\nqueries on topics of current concern. Variables cover staffing,\r\nworkload, funding, what type of computer access the office had,\r\nwhether the office was part of an integrated computerized system with\r\nother specific criminal agencies, the use of DNA evidence in plea\r\nnegotiations of felony trials, which laboratories performed these DNA\r\nanalyses, juvenile matters, and risks associated with the role of the\r\nprosecutor, such as threatening letters or calls, face-to-face\r\nassaults, or batter/assaults. The unit of analysis is the district\r\noffice.",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "modified": "2005-11-04T00:00:00",
-            "accessLevel": "restricted public",
-            "identifier": "1104",
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
+            "title": "National Prosecutors Survey, 1994"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Survey of Prosecutors is a biennial survey of\r\nchief prosecutors in state court systems. A chief prosecutor is an\r\nofficial, usually locally elected and typically with the title of\r\ndistrict attorney or county attorney, who is in charge of a\r\nprosecutorial district made up of one or more counties, and who\r\nconducts or supervises the prosecution of felony cases in a state\r\ncourt system. Prosecutors in courts of limited jurisdiction, such as\r\nmunicipal prosecutors, were not included in the survey. The survey's\r\npurpose was to obtain detailed descriptive information on prosecutors'\r\noffices, as well as information on their policies and practices. The\r\ndata collection instrument was based on questions that were included\r\nin the NATIONAL PROSECUTORS SURVEY, 1994 (ICPSR 6785), and also added\r\nqueries on topics of current concern. Variables cover staffing,\r\nworkload, funding, what type of computer access the office had,\r\nwhether the office was part of an integrated computerized system with\r\nother specific criminal agencies, the use of DNA evidence in plea\r\nnegotiations of felony trials, which laboratories performed these DNA\r\nanalyses, juvenile matters, and risks associated with the role of the\r\nprosecutor, such as threatening letters or calls, face-to-face\r\nassaults, or batter/assaults. The unit of analysis is the district\r\noffice.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR02433.v1",
+                    "title": "National Prosecutors Survey, 1996"
+                }
+            ],
+            "identifier": "1104",
+            "isPartOf": "2181",
+            "issued": "1998-11-16T00:00:00",
             "keyword": [
                 "DNA fingerprinting",
                 "attorneys",
@@ -36436,55 +36430,55 @@
                 "trial procedures",
                 "victim services"
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
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "1998-11-16T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR02433.v1",
-                    "title": "National Prosecutors Survey, 1996"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Survey of Youth in Custody, 2008-2009",
-            "description": "The National Survey of Youth in Custody (NSYC) is part of the BJS National Prison Rape Statistics Program to gather mandated data on the incidence of prevalence of sexual assault in juvenile facilities under the Prison Rape Elimination Act of 2003 (PREA; P.L. 108-79). The Act requires a 10 percent sample of juvenile facilities to be listed by incidence of sexual assault. Data are collected directly from youth in a private setting using audio computer-assisted self interview (ACASI) technology with a touch-screen laptop and an audio feed to maximize inmate confidentiality and minimize literacy issues. The first year of collection includes nearly 200 juvenile facilities, with an estimated 10,000 completed interviews with youth. \r\nThe NSYC utilized two questionnaires, based on the age of the respondent.  The Older Youth questionnaire was administered to youths ages 15 and older, and the Younger Youth questionnaire was administered to those 14 and younger.  The survey was divided into five sections.  Section A collected background information, such as details of admission to facility and demographics including education, height, weight, race, ethnicity, gender, sexual orientation, and history of any forced sexual contact.  Section B, Facility Perceptions and Victimization, included respondents' opinions of the facility and staff, any incidence of gang activity, and any injuries that had occurred.  Section C, Sexual Activity Within Facility, captured the types of sexual contact that occurred and the circumstances of sexual contact.  Section D, Description of Events with Youth, and Section E, Description of Events with Staff Member, focused on when and where the contact occurred, the race and gender of the other youths or staff members, if threats or coersion were involved, and outcomes, included whether or not the sexual contact was reported.\r\nOther variables include debriefing questions about respondents' experiences completing the survey, interviewer observations, created variables to summarize victimization reports (due to the complicated routing in Section C), weight and stratification data, and administrative data about the facilities.",
-            "modified": "2013-04-04T10:55:15",
-            "accessLevel": "restricted public",
-            "identifier": "1105",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "National Prosecutors Survey, 1996"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Survey of Youth in Custody (NSYC) is part of the BJS National Prison Rape Statistics Program to gather mandated data on the incidence of prevalence of sexual assault in juvenile facilities under the Prison Rape Elimination Act of 2003 (PREA; P.L. 108-79). The Act requires a 10 percent sample of juvenile facilities to be listed by incidence of sexual assault. Data are collected directly from youth in a private setting using audio computer-assisted self interview (ACASI) technology with a touch-screen laptop and an audio feed to maximize inmate confidentiality and minimize literacy issues. The first year of collection includes nearly 200 juvenile facilities, with an estimated 10,000 completed interviews with youth. \r\nThe NSYC utilized two questionnaires, based on the age of the respondent.  The Older Youth questionnaire was administered to youths ages 15 and older, and the Younger Youth questionnaire was administered to those 14 and younger.  The survey was divided into five sections.  Section A collected background information, such as details of admission to facility and demographics including education, height, weight, race, ethnicity, gender, sexual orientation, and history of any forced sexual contact.  Section B, Facility Perceptions and Victimization, included respondents' opinions of the facility and staff, any incidence of gang activity, and any injuries that had occurred.  Section C, Sexual Activity Within Facility, captured the types of sexual contact that occurred and the circumstances of sexual contact.  Section D, Description of Events with Youth, and Section E, Description of Events with Staff Member, focused on when and where the contact occurred, the race and gender of the other youths or staff members, if threats or coersion were involved, and outcomes, included whether or not the sexual contact was reported.\r\nOther variables include debriefing questions about respondents' experiences completing the survey, interviewer observations, created variables to summarize victimization reports (due to the complicated routing in Section C), weight and stratification data, and administrative data about the facilities.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR33942.v1",
+                    "title": "National Survey of Youth in Custody, 2008-2009"
+                }
+            ],
+            "identifier": "1105",
+            "isPartOf": "2442",
+            "issued": "2013-04-04T10:53:25",
             "keyword": [
                 "correctional facilities (juveniles)",
                 "correctional guards",
@@ -36501,55 +36495,55 @@
                 "sexual assault",
                 "sexual behavior"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2013-04-04T10:55:15",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2442",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2013-04-04T10:53:25",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR33942.v1",
-                    "title": "National Survey of Youth in Custody, 2008-2009"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Offender Based Transaction Statistics (OBTS), 1979:  Hawaii",
-            "description": "The purpose of the Offender Based Transaction Statistics\r\n (OBTS), 1979: Hawaii was to compile, collate, analyze, publish, and\r\n disseminate statistical information concerning the operation of the\r\n criminal justice system at the federal, state, and local levels. This\r\n collection includes facts on an arrested offender showing actions by\r\n the police, prosecutor, and court. The individual offender is the unit\r\n of analysis, and felony arrests and other related dispositions are\r\nincluded.",
-            "modified": "2005-08-08T00:00:00",
-            "accessLevel": "restricted public",
-            "identifier": "1106",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "National Survey of Youth in Custody, 2008-2009"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The purpose of the Offender Based Transaction Statistics\r\n (OBTS), 1979: Hawaii was to compile, collate, analyze, publish, and\r\n disseminate statistical information concerning the operation of the\r\n criminal justice system at the federal, state, and local levels. This\r\n collection includes facts on an arrested offender showing actions by\r\n the police, prosecutor, and court. The individual offender is the unit\r\n of analysis, and felony arrests and other related dispositions are\r\nincluded.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR08042.v2",
+                    "title": "Offender Based Transaction Statistics (OBTS), 1979:  Hawaii"
+                }
+            ],
+            "identifier": "1106",
+            "isPartOf": "2177",
+            "issued": "1986-04-28T00:00:00",
             "keyword": [
                 "adult offenders",
                 "arrests",
@@ -36560,55 +36554,55 @@
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
-            "isPartOf": "2177",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "1986-04-28T00:00:00",
             "language": [
                 "eng"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR08042.v2",
-                    "title": "Offender Based Transaction Statistics (OBTS), 1979:  Hawaii"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Offender Based Transaction Statistics (OBTS), 1980: California, Ohio, New York, Pennsylvania, and Utah",
-            "description": "Offender Based Transaction Statistics (OBTS) studies are\r\n designed to collect information by tracking adult offenders from the\r\n point of entry into the criminal justice system (typically by arrest)\r\n through final disposition, regardless of whether the offender is\r\n convicted or acquitted. Information is provided on arrest, police\r\n action, prosecutor action, level of charges, charges filed by the\r\n prosecutor, type of counsel, pretrial status, type of trial, sentence\r\n type, and sentence length. This allows researchers to examine how the\r\n criminal justice system processes offenders, to measure the changing\r\n volume of offenders moving through the different segments of the\r\n criminal justice system, to calculate processing time intervals\r\n between major decision-making events, and to assess the changing\r\nstructure of the offender population.",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "modified": "2005-08-08T00:00:00",
-            "accessLevel": "restricted public",
-            "identifier": "1107",
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
+            "title": "Offender Based Transaction Statistics (OBTS), 1979:  Hawaii"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
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
+                    "accessURL": "https://doi.org/10.3886/ICPSR08248.v6",
+                    "title": "Offender Based Transaction Statistics (OBTS), 1980: California, Ohio, New York, Pennsylvania, and Utah"
+                }
+            ],
+            "identifier": "1107",
+            "isPartOf": "2177",
+            "issued": "1984-07-12T00:00:00",
             "keyword": [
                 "adult offenders",
                 "arrests",
@@ -36619,55 +36613,55 @@
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
-            "isPartOf": "2177",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "1984-07-12T00:00:00",
             "language": [
                 "eng"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR08248.v6",
-                    "title": "Offender Based Transaction Statistics (OBTS), 1980: California, Ohio, New York, Pennsylvania, and Utah"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Offender Based Transaction Statistics (OBTS), 1981: California, Ohio, Pennsylvania, Utah, Minnesota, New York, and Virginia",
-            "description": "Offender Based Transaction Statistics (OBTS) studies are\r\n designed to collect information by tracking adult offenders from the\r\n point of entry into the criminal justice system (typically by arrest)\r\n through final disposition, regardless of whether the offender is\r\n convicted or acquitted. Information is provided on arrest, police\r\n action, prosecutor action, level of charges, charges filed by the\r\n prosecutor, type of counsel, pretrial status, type of trial, sentence\r\n type, and sentence length. This allows researchers to examine how the\r\n criminal justice system processes offenders, to measure the changing\r\n volume of offenders moving through the different segments of the\r\n criminal justice system, to calculate processing time intervals\r\n between major decision-making events, and to assess the changing\r\nstructure of the offender population.",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "modified": "2005-08-08T00:00:00",
-            "accessLevel": "restricted public",
-            "identifier": "1108",
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
+            "title": "Offender Based Transaction Statistics (OBTS), 1980: California, Ohio, New York, Pennsylvania, and Utah"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
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
+                    "accessURL": "https://doi.org/10.3886/ICPSR08277.v5",
+                    "title": "Offender Based Transaction Statistics (OBTS), 1981: California, Ohio, Pennsylvania, Utah, Minnesota, New York, and Virginia"
+                }
+            ],
+            "identifier": "1108",
+            "isPartOf": "2177",
+            "issued": "1984-11-14T00:00:00",
             "keyword": [
                 "adult offenders",
                 "arrests",
@@ -36678,55 +36672,55 @@
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
-            "isPartOf": "2177",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "1984-11-14T00:00:00",
             "language": [
                 "eng"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR08277.v5",
-                    "title": "Offender Based Transaction Statistics (OBTS), 1981: California, Ohio, Pennsylvania, Utah, Minnesota, New York, and Virginia"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Offender Based Transaction Statistics (OBTS), 1982: California, Ohio, Pennsylvania, Utah, Minnesota, New York, Virgin Islands, and Virginia",
-            "description": "Offender Based Transaction Statistics (OBTS) studies are\r\n designed to collect information by tracking adult offenders from the\r\n point of entry into the criminal justice system (typically by arrest)\r\n through final disposition, regardless of whether the offender is\r\n convicted or acquitted. Information is provided on arrest, police\r\n action, prosecutor action, level of charges, charges filed by the\r\n prosecutor, type of counsel, pretrial status, type of trial, sentence\r\n type, and sentence length. This allows researchers to examine how the\r\n criminal justice system processes offenders, to measure the changing\r\n volume of offenders moving through the different segments of the\r\n criminal justice system, to calculate processing time intervals\r\n between major decision-making events, and to assess the changing\r\nstructure of the offender population.",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "modified": "2005-08-08T00:00:00",
-            "accessLevel": "restricted public",
-            "identifier": "1109",
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
+            "title": "Offender Based Transaction Statistics (OBTS), 1981: California, Ohio, Pennsylvania, Utah, Minnesota, New York, and Virginia"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
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
+                    "accessURL": "https://doi.org/10.3886/ICPSR08408.v6",
+                    "title": "Offender Based Transaction Statistics (OBTS), 1982: California, Ohio, Pennsylvania, Utah, Minnesota, New York, Virgin Islands, and Virginia"
+                }
+            ],
+            "identifier": "1109",
+            "isPartOf": "2177",
+            "issued": "1985-12-20T00:00:00",
             "keyword": [
                 "adult offenders",
                 "arrests",
@@ -36737,55 +36731,55 @@
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
-            "isPartOf": "2177",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "1985-12-20T00:00:00",
             "language": [
                 "eng"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR08408.v6",
-                    "title": "Offender Based Transaction Statistics (OBTS), 1982: California, Ohio, Pennsylvania, Utah, Minnesota, New York, Virgin Islands, and Virginia"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Offender Based Transaction Statistics (OBTS), 1983:  California, Minnesota, Nebraska, New York, Ohio, Pennsylvania, Utah, Virgin Islands, and Virginia",
-            "description": "Offender Based Transaction Statistics (OBTS) studies are\r\n designed to collect information by tracking adult offenders from the\r\n point of entry into the criminal justice system (typically by arrest)\r\n through final disposition, regardless of whether the offender is\r\n convicted or acquitted. Information is provided on arrest, police\r\n action, prosecutor action, level of charges, charges filed by the\r\n prosecutor, type of counsel, pretrial status, type of trial, sentence\r\n type, and sentence length. This allows researchers to examine how the\r\n criminal justice system processes offenders, to measure the changing\r\n volume of offenders moving through the different segments of the\r\n criminal justice system, to calculate processing time intervals\r\n between major decision-making events, and to assess the changing\r\nstructure of the offender population.",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "modified": "2005-08-08T00:00:00",
-            "accessLevel": "restricted public",
-            "identifier": "1110",
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
+            "title": "Offender Based Transaction Statistics (OBTS), 1982: California, Ohio, Pennsylvania, Utah, Minnesota, New York, Virgin Islands, and Virginia"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
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
+                    "accessURL": "https://doi.org/10.3886/ICPSR08449.v7",
+                    "title": "Offender Based Transaction Statistics (OBTS), 1983:  California, Minnesota, Nebraska, New York, Ohio, Pennsylvania, Utah, Virgin Islands, and Virginia"
+                }
+            ],
+            "identifier": "1110",
+            "isPartOf": "2177",
+            "issued": "1986-03-28T00:00:00",
             "keyword": [
                 "adult offenders",
                 "arrests",
@@ -36796,55 +36790,55 @@
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
-            "isPartOf": "2177",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "1986-03-28T00:00:00",
             "language": [
                 "eng"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR08449.v7",
-                    "title": "Offender Based Transaction Statistics (OBTS), 1983:  California, Minnesota, Nebraska, New York, Ohio, Pennsylvania, Utah, Virgin Islands, and Virginia"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Offender Based Transaction Statistics (OBTS), 1984: Alaska, California, Delaware, Georgia, Minnesota, Missouri, Nebraska, New York, Ohio, Pennsylvania, and Virginia",
-            "description": "Offender Based Transaction Statistics (OBTS) studies are\r\n designed to collect information by tracking adult offenders from the\r\n point of entry into the criminal justice system (typically by arrest)\r\n through final disposition, regardless of whether the offender is\r\n convicted or acquitted. Information is provided on arrest, police\r\n action, prosecutor action, level of charges, charges filed by the\r\n prosecutor, type of counsel, pretrial status, type of trial, sentence\r\n type, and sentence length. This allows researchers to examine how the\r\n criminal justice system processes offenders, to measure the changing\r\n volume of offenders moving through the different segments of the\r\n criminal justice system, to calculate processing time intervals\r\n between major decision-making events, and to assess the changing\r\nstructure of the offender population.",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "modified": "2005-08-08T00:00:00",
-            "accessLevel": "restricted public",
-            "identifier": "1111",
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
+            "title": "Offender Based Transaction Statistics (OBTS), 1983:  California, Minnesota, Nebraska, New York, Ohio, Pennsylvania, Utah, Virgin Islands, and Virginia"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
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
+                    "accessURL": "https://doi.org/10.3886/ICPSR08675.v4",
+                    "title": "Offender Based Transaction Statistics (OBTS), 1984: Alaska, California, Delaware, Georgia, Minnesota, Missouri, Nebraska, New York, Ohio, Pennsylvania, and Virginia"
+                }
+            ],
+            "identifier": "1111",
+            "isPartOf": "2177",
+            "issued": "1987-10-12T00:00:00",
             "keyword": [
                 "adult offenders",
                 "arrests",
@@ -36855,55 +36849,55 @@
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
-            "isPartOf": "2177",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "1987-10-12T00:00:00",
             "language": [
                 "eng"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR08675.v4",
-                    "title": "Offender Based Transaction Statistics (OBTS), 1984: Alaska, California, Delaware, Georgia, Minnesota, Missouri, Nebraska, New York, Ohio, Pennsylvania, and Virginia"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Offender Based Transaction Statistics (OBTS), 1985: Alaska, California, Delaware, Georgia, Minnesota, Missouri, Nebraska, New York, Pennsylvania, and Virginia",
-            "description": "Offender Based Transaction Statistics (OBTS) studies are\r\n designed to collect information by tracking adult offenders from the\r\n point of entry into the criminal justice system (typically by arrest)\r\n through final disposition, regardless of whether the offender is\r\n convicted or acquitted. Information is provided on arrest, police\r\n action, prosecutor action, level of charges, charges filed by the\r\n prosecutor, type of counsel, pretrial status, type of trial, sentence\r\n type, and sentence length. This allows researchers to examine how the\r\n criminal justice system processes offenders, to measure the changing\r\n volume of offenders moving through the different segments of the\r\n criminal justice system, to calculate processing time intervals\r\n between major decision-making events, and to assess the changing\r\nstructure of the offender population.",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "modified": "2005-08-08T00:00:00",
-            "accessLevel": "restricted public",
-            "identifier": "1112",
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
+            "title": "Offender Based Transaction Statistics (OBTS), 1984: Alaska, California, Delaware, Georgia, Minnesota, Missouri, Nebraska, New York, Ohio, Pennsylvania, and Virginia"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
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
+                    "accessURL": "https://doi.org/10.3886/ICPSR08911.v2",
+                    "title": "Offender Based Transaction Statistics (OBTS), 1985: Alaska, California, Delaware, Georgia, Minnesota, Missouri, Nebraska, New York, Pennsylvania, and Virginia"
+                }
+            ],
+            "identifier": "1112",
+            "isPartOf": "2177",
+            "issued": "1988-10-25T00:00:00",
             "keyword": [
                 "adult offenders",
                 "arrests",
@@ -36914,55 +36908,55 @@
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
-            "isPartOf": "2177",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "1988-10-25T00:00:00",
             "language": [
                 "eng"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR08911.v2",
-                    "title": "Offender Based Transaction Statistics (OBTS), 1985: Alaska, California, Delaware, Georgia, Minnesota, Missouri, Nebraska, New York, Pennsylvania, and Virginia"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Offender Based Transaction Statistics (OBTS), 1986: Alabama, Alaska, California, Delaware, Georgia, Minnesota, Missouri, Nebraska, New York, Pennsylvania, and Virginia",
-            "description": "Offender Based Transaction Statistics (OBTS) studies are\r\n designed to collect information by tracking adult offenders from the\r\n point of entry into the criminal justice system (typically by arrest)\r\n through final disposition, regardless of whether the offender is\r\n convicted or acquitted. Information is provided on arrest, police\r\n action, prosecutor action, level of charges, charges filed by the\r\n prosecutor, type of counsel, pretrial status, type of trial, sentence\r\n type, and sentence length. This allows researchers to examine how the\r\n criminal justice system processes offenders, to measure the changing\r\n volume of offenders moving through the different segments of the\r\n criminal justice system, to calculate processing time intervals\r\n between major decision-making events, and to assess the changing\r\nstructure of the offender population.",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "modified": "2005-08-08T00:00:00",
-            "accessLevel": "restricted public",
-            "identifier": "1113",
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
+            "title": "Offender Based Transaction Statistics (OBTS), 1985: Alaska, California, Delaware, Georgia, Minnesota, Missouri, Nebraska, New York, Pennsylvania, and Virginia"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
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
+                    "accessURL": "https://doi.org/10.3886/ICPSR09130.v2",
+                    "title": "Offender Based Transaction Statistics (OBTS), 1986: Alabama, Alaska, California, Delaware, Georgia, Minnesota, Missouri, Nebraska, New York, Pennsylvania, and Virginia"
+                }
+            ],
+            "identifier": "1113",
+            "isPartOf": "2177",
+            "issued": "1989-09-26T00:00:00",
             "keyword": [
                 "adult offenders",
                 "arrests",
@@ -36973,55 +36967,55 @@
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
-            "isPartOf": "2177",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "1989-09-26T00:00:00",
             "language": [
                 "eng"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR09130.v2",
-                    "title": "Offender Based Transaction Statistics (OBTS), 1986: Alabama, Alaska, California, Delaware, Georgia, Minnesota, Missouri, Nebraska, New York, Pennsylvania, and Virginia"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Offender Based Transaction Statistics (OBTS), 1987: Alabama, Alaska, California, Delaware, Georgia, Minnesota, Missouri, Nebraska, New Jersey, New York, Pennsylvania, Utah, Vermont, and Virginia",
-            "description": "Offender Based Transaction Statistics (OBTS) studies are\r\n designed to collect information by tracking adult offenders from the\r\n point of entry into the criminal justice system (typically by arrest)\r\n through final disposition, regardless of whether the offender is\r\n convicted or acquitted. Information is provided on arrest, police\r\n action, prosecutor action, level of charges, charges filed by the\r\n prosecutor, type of counsel, pretrial status, type of trial, sentence\r\n type, and sentence length. This allows researchers to examine how the\r\n criminal justice system processes offenders, to measure the changing\r\n volume of offenders moving through the different segments of the\r\n criminal justice system, to calculate processing time intervals\r\n between major decision-making events, and to assess the changing\r\nstructure of the offender population.",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "modified": "2005-08-08T00:00:00",
-            "accessLevel": "restricted public",
-            "identifier": "1114",
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
+            "title": "Offender Based Transaction Statistics (OBTS), 1986: Alabama, Alaska, California, Delaware, Georgia, Minnesota, Missouri, Nebraska, New York, Pennsylvania, and Virginia"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
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
+                    "accessURL": "https://doi.org/10.3886/ICPSR09287.v3",
+                    "title": "Offender Based Transaction Statistics (OBTS), 1987: Alabama, Alaska, California, Delaware, Georgia, Minnesota, Missouri, Nebraska, New Jersey, New York, Pennsylvania, Utah, Vermont, and Virginia"
+                }
+            ],
+            "identifier": "1114",
+            "isPartOf": "2177",
+            "issued": "1990-03-06T00:00:00",
             "keyword": [
                 "adult offenders",
                 "arrests",
@@ -37032,55 +37026,55 @@
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
-            "isPartOf": "2177",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "1990-03-06T00:00:00",
             "language": [
                 "eng"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR09287.v3",
-                    "title": "Offender Based Transaction Statistics (OBTS), 1987: Alabama, Alaska, California, Delaware, Georgia, Minnesota, Missouri, Nebraska, New Jersey, New York, Pennsylvania, Utah, Vermont, and Virginia"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Offender Based Transaction Statistics (OBTS), 1988: Alabama, Alaska, California, Delaware, Idaho, Kentucky, Minnesota, Missouri, Nebraska, New Jersey, New York, Oregon, Pennsylvania, Utah, Vermont, and Virginia",
-            "description": "Offender Based Transaction Statistics (OBTS) studies are\r\n designed to collect information by tracking adult offenders from the\r\n point of entry into the criminal justice system (typically by arrest)\r\n through final disposition, regardless of whether the offender is\r\n convicted or acquitted. Information is provided on arrest, police\r\n action, prosecutor action, level of charges, charges filed by the\r\n prosecutor, type of counsel, pretrial status, type of trial, sentence\r\n type, and sentence length. This allows researchers to examine how the\r\n criminal justice system processes offenders, to measure the changing\r\n volume of offenders moving through the different segments of the\r\n criminal justice system, to calculate processing time intervals\r\n between major decision-making events, and to assess the changing\r\nstructure of the offender population.",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "modified": "2005-08-08T00:00:00",
-            "accessLevel": "restricted public",
-            "identifier": "1115",
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
+            "title": "Offender Based Transaction Statistics (OBTS), 1987: Alabama, Alaska, California, Delaware, Georgia, Minnesota, Missouri, Nebraska, New Jersey, New York, Pennsylvania, Utah, Vermont, and Virginia"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
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
+                    "accessURL": "https://doi.org/10.3886/ICPSR09523.v5",
+                    "title": "Offender Based Transaction Statistics (OBTS), 1988: Alabama, Alaska, California, Delaware, Idaho, Kentucky, Minnesota, Missouri, Nebraska, New Jersey, New York, Oregon, Pennsylvania, Utah, Vermont, and Virginia"
+                }
+            ],
+            "identifier": "1115",
+            "isPartOf": "2177",
+            "issued": "1992-02-03T00:00:00",
             "keyword": [
                 "adult offenders",
                 "arrests",
@@ -37091,55 +37085,55 @@
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
-            "isPartOf": "2177",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "1992-02-03T00:00:00",
             "language": [
                 "eng"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR09523.v5",
-                    "title": "Offender Based Transaction Statistics (OBTS), 1988: Alabama, Alaska, California, Delaware, Idaho, Kentucky, Minnesota, Missouri, Nebraska, New Jersey, New York, Oregon, Pennsylvania, Utah, Vermont, and Virginia"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Offender Based Transaction Statistics (OBTS), 1989: Alabama, Alaska, California, Idaho, Kentucky, Minnesota, Missouri, Nebraska, New Jersey, New York, Pennsylvania, Vermont, and Virginia",
-            "description": "Offender Based Transaction Statistics (OBTS) studies are\r\n designed to collect information by tracking adult offenders from the\r\n point of entry into the criminal justice system (typically by arrest)\r\n through final disposition, regardless of whether the offender is\r\n convicted or acquitted. Information is provided on arrest, police\r\n action, prosecutor action, level of charges, charges filed by the\r\n prosecutor, type of counsel, pretrial status, type of trial, sentence\r\n type, and sentence length. This allows researchers to examine how the\r\n criminal justice system processes offenders, to measure the changing\r\n volume of offenders moving through the different segments of the\r\n criminal justice system, to calculate processing time intervals\r\n between major decision-making events, and to assess the changing\r\nstructure of the offender population.",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "modified": "2005-08-08T00:00:00",
-            "accessLevel": "restricted public",
-            "identifier": "1116",
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
+            "title": "Offender Based Transaction Statistics (OBTS), 1988: Alabama, Alaska, California, Delaware, Idaho, Kentucky, Minnesota, Missouri, Nebraska, New Jersey, New York, Oregon, Pennsylvania, Utah, Vermont, and Virginia"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
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
+                    "accessURL": "https://doi.org/10.3886/ICPSR06190.v2",
+                    "title": "Offender Based Transaction Statistics (OBTS), 1989: Alabama, Alaska, California, Idaho, Kentucky, Minnesota, Missouri, Nebraska, New Jersey, New York, Pennsylvania, Vermont, and Virginia"
+                }
+            ],
+            "identifier": "1116",
+            "isPartOf": "2177",
+            "issued": "1994-03-10T00:00:00",
             "keyword": [
                 "adult offenders",
                 "arrests",
@@ -37150,110 +37144,109 @@
                 "prosecution",
                 "sentencing"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2005-08-08T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2177",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "1994-03-10T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR06190.v2",
-                    "title": "Offender Based Transaction Statistics (OBTS), 1989: Alabama, Alaska, California, Idaho, Kentucky, Minnesota, Missouri, Nebraska, New Jersey, New York, Pennsylvania, Vermont, and Virginia"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Recidivism Among Released Prisoners, 1983:  [United States]  ",
-            "description": "This data collection provides comprehensive criminal history\r\ndata on prisoners released from custody in 1983. Precise estimates are\r\nsupplied on recidivism among prisoners of all ages with all types of\r\npostrelease supervision. Data cover recidivism both within and outside\r\nthe states in which the prisoners were released. Variables include\r\nsociodemographic indices, type of sentence, length of sentence, offense,\r\ncourt action, and date of court action.",
-            "modified": "2011-03-08T09:36:25",
-            "accessLevel": "restricted public",
-            "identifier": "1117",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Offender Based Transaction Statistics (OBTS), 1989: Alabama, Alaska, California, Idaho, Kentucky, Minnesota, Missouri, Nebraska, New Jersey, New York, Pennsylvania, Vermont, and Virginia"
+        },
+        {
+            "@type": "dcat:Dataset",
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
-                "criminal histories",
-                "ex-offenders",
-                "offenders",
-                "postrelease programs",
-                "recidivism"
-            ],
-            "bureauCode": [
-                "011:21"
-            ],
-            "programCode": [
-                "011:061"
-            ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
             "dataQuality": false,
-            "issued": "1989-09-26T00:00:00",
-            "language": [
-                "eng"
-            ],
+            "description": "This data collection provides comprehensive criminal history\r\ndata on prisoners released from custody in 1983. Precise estimates are\r\nsupplied on recidivism among prisoners of all ages with all types of\r\npostrelease supervision. Data cover recidivism both within and outside\r\nthe states in which the prisoners were released. Variables include\r\nsociodemographic indices, type of sentence, length of sentence, offense,\r\ncourt action, and date of court action.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://doi.org/10.3886/ICPSR08875.v3",
                     "title": "Recidivism Among Released Prisoners, 1983:  [United States]  "
                 }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Recidivism of Prisoners Released in 1994",
-            "description": "RECIDIVISM OF PRISONERS RELEASED IN 1994\r\nis a database containing information on each of 38,624 sampled\r\nprisoners released from prisons in 15 states in 1994 and tracked for\r\nthree years following their release. The majority of the database\r\nconsists of information on each released prisoner's entire officially\r\nrecorded criminal history (before and after the 1994 release). Sources\r\nfor criminal history information are state and FBI automated RAP\r\n(\"Records of Arrests and Prosecutions\") sheets, which contain records\r\nof arrests, adjudications, and sentences. The study is the second\r\nmajor recidivism study conducted by the Bureau of Justice Statistics.\r\nThe first study, RECIDIVISM AMONG RELEASED PRISONERS, 1983: [UNITED\r\nSTATES] (ICPSR 8875), tracked over 16,000 prisoners released in 11\r\nstates in 1983 for three years. These two studies are the\r\nclosest approximation to \"national\" recidivism studies in the United\r\nStates. They are distinguished by their large sample size (over 16,000\r\nreleased prisoners in the first study, 38,624 in the second),\r\ngeographic breadth of coverage (11 states in the first study, 15 in\r\nthe second), length of prospective tracking (three years from date of\r\nrelease in both studies), ability to track the movement of released\r\nprisoners across state boundaries (both studies), and multiple\r\nmeasures of recidivism (both studies). Demographic data include race,\r\nethnicity, sex, and date of birth.",
-            "modified": "2014-12-05T14:51:37",
-            "accessLevel": "restricted public",
-            "identifier": "1118",
+            ],
+            "identifier": "1117",
+            "issued": "1989-09-26T00:00:00",
+            "keyword": [
+                "criminal histories",
+                "ex-offenders",
+                "offenders",
+                "postrelease programs",
+                "recidivism"
+            ],
+            "language": [
+                "eng"
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-03-08T09:36:25",
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
+            "title": "Recidivism Among Released Prisoners, 1983:  [United States]  "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "RECIDIVISM OF PRISONERS RELEASED IN 1994\r\nis a database containing information on each of 38,624 sampled\r\nprisoners released from prisons in 15 states in 1994 and tracked for\r\nthree years following their release. The majority of the database\r\nconsists of information on each released prisoner's entire officially\r\nrecorded criminal history (before and after the 1994 release). Sources\r\nfor criminal history information are state and FBI automated RAP\r\n(\"Records of Arrests and Prosecutions\") sheets, which contain records\r\nof arrests, adjudications, and sentences. The study is the second\r\nmajor recidivism study conducted by the Bureau of Justice Statistics.\r\nThe first study, RECIDIVISM AMONG RELEASED PRISONERS, 1983: [UNITED\r\nSTATES] (ICPSR 8875), tracked over 16,000 prisoners released in 11\r\nstates in 1983 for three years. These two studies are the\r\nclosest approximation to \"national\" recidivism studies in the United\r\nStates. They are distinguished by their large sample size (over 16,000\r\nreleased prisoners in the first study, 38,624 in the second),\r\ngeographic breadth of coverage (11 states in the first study, 15 in\r\nthe second), length of prospective tracking (three years from date of\r\nrelease in both studies), ability to track the movement of released\r\nprisoners across state boundaries (both studies), and multiple\r\nmeasures of recidivism (both studies). Demographic data include race,\r\nethnicity, sex, and date of birth.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR03355.v8",
+                    "title": "Recidivism of Prisoners Released in 1994"
+                }
+            ],
+            "identifier": "1118",
+            "issued": "2002-09-25T00:00:00",
             "keyword": [
                 "arrest records",
                 "conviction records",
@@ -37261,54 +37254,55 @@
                 "offenses",
                 "recidivism"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2014-12-05T14:51:37",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2002-09-25T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR03355.v8",
-                    "title": "Recidivism of Prisoners Released in 1994"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Supplemental Survey of Civil Appeals, 2001",
-            "description": "The 2001 Supplemental Survey of Civil Appeals is a\r\nfollow-up to the CIVIL JUSTICE SURVEY OF STATE COURTS, 2001 (ICPSR 3957) which examined 8,311 general civil cases (e.g.,\r\ntort, contract, and real property) concluded by bench or jury trial in\r\na sample of 46 of the nation's 75 most populous counties in 2001.\r\nThese cases were then weighted to represent the 11,908 general civil\r\ntrials concluded in the nation's 75 most populous counties. Data from\r\nthe 2001 Civil Trial Survey were used to produce several Bureau of\r\nJustice Statistics (BJS) reports describing the characteristics of\r\ncivil litigation in state courts. The 2001 Supplemental Survey of\r\nCivil Appeals tracks every general civil case concluded by bench or\r\njury trial in 2001 in the 46 surveyed counties that were subsequently\r\nappealed to an intermediate appellate court or court of last resort.\r\nIn the 2001 Civil Justice Survey of State Courts information was\r\ncollected for every general civil trial concluded in 43 of the 46\r\nselected counties. In these counties, the 2001 Supplemental Survey of\r\nCivil Appeals collected information on all general trials that\r\nproduced an appeal. In the three remaining counties, (Cook County,\r\nPhiladelphia County, and Bergen County), the appeals survey obtained\r\ninformation for both those general civil trials concluded in 2001 that\r\nwere subsequently appealed and, in addition, collected information for\r\nthose general civil appeals that were not captured at the trial court\r\nlevel. The 2001 Supplemental Survey of Civil Appeals tracks data on\r\ngeneral civil appeals that originated from 46 of the nation's 75 most\r\npopulous counties. Unlike the 2001 Civil Justice Survey of State\r\nCourts, cases were not weighted to represent appeals in the nation's\r\n75 most populous counties. The appeals were followed until they were\r\nwithdrawn, dismissed, or decided on the merits in the appellate\r\ncourts. All appeals were tracked until April 30, 2005. Appeals not\r\ndisposed on that date are identified as pending. Overall four\r\nappellate datasets were produced from this survey.",
-            "modified": "2011-11-02T16:21:19",
-            "accessLevel": "restricted public",
-            "identifier": "1119",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Recidivism of Prisoners Released in 1994"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The 2001 Supplemental Survey of Civil Appeals is a\r\nfollow-up to the CIVIL JUSTICE SURVEY OF STATE COURTS, 2001 (ICPSR 3957) which examined 8,311 general civil cases (e.g.,\r\ntort, contract, and real property) concluded by bench or jury trial in\r\na sample of 46 of the nation's 75 most populous counties in 2001.\r\nThese cases were then weighted to represent the 11,908 general civil\r\ntrials concluded in the nation's 75 most populous counties. Data from\r\nthe 2001 Civil Trial Survey were used to produce several Bureau of\r\nJustice Statistics (BJS) reports describing the characteristics of\r\ncivil litigation in state courts. The 2001 Supplemental Survey of\r\nCivil Appeals tracks every general civil case concluded by bench or\r\njury trial in 2001 in the 46 surveyed counties that were subsequently\r\nappealed to an intermediate appellate court or court of last resort.\r\nIn the 2001 Civil Justice Survey of State Courts information was\r\ncollected for every general civil trial concluded in 43 of the 46\r\nselected counties. In these counties, the 2001 Supplemental Survey of\r\nCivil Appeals collected information on all general trials that\r\nproduced an appeal. In the three remaining counties, (Cook County,\r\nPhiladelphia County, and Bergen County), the appeals survey obtained\r\ninformation for both those general civil trials concluded in 2001 that\r\nwere subsequently appealed and, in addition, collected information for\r\nthose general civil appeals that were not captured at the trial court\r\nlevel. The 2001 Supplemental Survey of Civil Appeals tracks data on\r\ngeneral civil appeals that originated from 46 of the nation's 75 most\r\npopulous counties. Unlike the 2001 Civil Justice Survey of State\r\nCourts, cases were not weighted to represent appeals in the nation's\r\n75 most populous counties. The appeals were followed until they were\r\nwithdrawn, dismissed, or decided on the merits in the appellate\r\ncourts. All appeals were tracked until April 30, 2005. Appeals not\r\ndisposed on that date are identified as pending. Overall four\r\nappellate datasets were produced from this survey.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR04539.v2",
+                    "title": "Supplemental Survey of Civil Appeals, 2001"
+                }
+            ],
+            "identifier": "1119",
+            "isPartOf": "2172",
+            "issued": "2006-08-21T00:00:00",
             "keyword": [
                 "case processing",
                 "civil courts",
@@ -37319,55 +37313,55 @@
                 "lawsuits",
                 "state courts"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2011-11-02T16:21:19",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2172",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2006-08-21T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR04539.v2",
-                    "title": "Supplemental Survey of Civil Appeals, 2001"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Survey of Inmates in Local Jails, 2002 [United States]",
-            "description": "This collection provides nationally representative data on\r\n persons held prior to trial and on convicted offenders serving\r\n sentences in local jails or awaiting transfer to state prisons. Data\r\n cover individual characteristics of jail inmates, current offenses,\r\n sentences and time served, criminal histories, jail activities,\r\n conditions and programs, prior drug and alcohol use and treatment, and\r\n health care services provided while in jail. Part 1, Numeric Data,\r\n contains numeric data for all questions in the survey, while Part 2,\r\n Alphanumeric Data, consists of non-numeric answers to the \"Other,\r\nSpecify\" selection available for some of the questions.",
-            "modified": "2012-08-22T09:09:32",
-            "accessLevel": "restricted public",
-            "identifier": "1120",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Supplemental Survey of Civil Appeals, 2001"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This collection provides nationally representative data on\r\n persons held prior to trial and on convicted offenders serving\r\n sentences in local jails or awaiting transfer to state prisons. Data\r\n cover individual characteristics of jail inmates, current offenses,\r\n sentences and time served, criminal histories, jail activities,\r\n conditions and programs, prior drug and alcohol use and treatment, and\r\n health care services provided while in jail. Part 1, Numeric Data,\r\n contains numeric data for all questions in the survey, while Part 2,\r\n Alphanumeric Data, consists of non-numeric answers to the \"Other,\r\nSpecify\" selection available for some of the questions.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR04359.v2",
+                    "title": "Survey of Inmates in Local Jails, 2002 [United States]"
+                }
+            ],
+            "identifier": "1120",
+            "isPartOf": "2170",
+            "issued": "2006-03-17T00:00:00",
             "keyword": [
                 "correctional facilities",
                 "criminal histories",
@@ -37380,55 +37374,55 @@
                 "offenses",
                 "sentencing"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2012-08-22T09:09:32",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2170",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2006-03-17T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR04359.v2",
-                    "title": "Survey of Inmates in Local Jails, 2002 [United States]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Survey of Inmates in State and Federal Correctional Facilities, 1997",
-            "description": "Conducted by the Bureau of the Census, this survey provides\r\nnationally representative data on state prison inmates and sentenced\r\nfederal inmates held in federally owned and operated facilities.\r\nThrough personal interviews from June-October 1997, inmates in both\r\nstate and federal prisons provided information about their current\r\noffense and sentence, criminal history, family background and personal\r\ncharacteristics, prior drug and alcohol use and treatment programs,\r\ngun possession and use, gang membership, and prison activities,\r\nprograms, and services. Prior surveys of state prison inmates, called\r\nSURVEY OF INMATES OF STATE CORRECTIONAL FACILITIES, were conducted in\r\n1974, 1979, 1986, and 1991 (see ICPSR 7811, 7856, 8711, and 6086).\r\nSentenced federal prison inmates were first interviewed in 1991 (see\r\nSURVEY OF INMATES OF FEDERAL CORRECTIONAL FACILITIES, 1991 [ICPSR\r\n6037]). The federal data are combined with the state data in this\r\ncollection. Part 1, Numeric Data, consists of numerically-coded\r\nresponses, while Part 2, Alphanumeric Data, contains free-field\r\nresponses to \"Specify, Other\" questions in ASCII text form.",
-            "modified": "2006-03-30T00:00:00",
-            "accessLevel": "restricted public",
-            "identifier": "1121",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Survey of Inmates in Local Jails, 2002 [United States]"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "Conducted by the Bureau of the Census, this survey provides\r\nnationally representative data on state prison inmates and sentenced\r\nfederal inmates held in federally owned and operated facilities.\r\nThrough personal interviews from June-October 1997, inmates in both\r\nstate and federal prisons provided information about their current\r\noffense and sentence, criminal history, family background and personal\r\ncharacteristics, prior drug and alcohol use and treatment programs,\r\ngun possession and use, gang membership, and prison activities,\r\nprograms, and services. Prior surveys of state prison inmates, called\r\nSURVEY OF INMATES OF STATE CORRECTIONAL FACILITIES, were conducted in\r\n1974, 1979, 1986, and 1991 (see ICPSR 7811, 7856, 8711, and 6086).\r\nSentenced federal prison inmates were first interviewed in 1991 (see\r\nSURVEY OF INMATES OF FEDERAL CORRECTIONAL FACILITIES, 1991 [ICPSR\r\n6037]). The federal data are combined with the state data in this\r\ncollection. Part 1, Numeric Data, consists of numerically-coded\r\nresponses, while Part 2, Alphanumeric Data, contains free-field\r\nresponses to \"Specify, Other\" questions in ASCII text form.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR02598.v1",
+                    "title": "Survey of Inmates in State and Federal Correctional Facilities, 1997"
+                }
+            ],
+            "identifier": "1121",
+            "isPartOf": "2171",
+            "issued": "2000-06-01T00:00:00",
             "keyword": [
                 "HIV",
                 "correctional facilities",
@@ -37446,55 +37440,55 @@
                 "substance abuse",
                 "treatment programs"
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
-            "isPartOf": "2171",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2000-06-01T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR02598.v1",
-                    "title": "Survey of Inmates in State and Federal Correctional Facilities, 1997"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Survey of Inmates in State and Federal Correctional Facilities, [United States], 2004",
-            "description": "This survey provides nationally representative data on inmates\r\nheld in state prisons and federally-owned and operated prisons.\r\nThrough personal interviews conducted from October 2003 through May\r\n2004, inmates in both state and federal prisons provided information\r\nabout their current offense and sentence, criminal history, family\r\nbackground and personal characteristics, prior drug and alcohol use\r\nand treatment programs, gun possession and use, and prison activities,\r\nprograms, and services. Prior surveys of State prison inmates were\r\nconducted in 1974, 1979, 1986, 1991, and 1997. Sentenced federal\r\nprison inmates were interviewed in the 1991 and 1997 surveys.",
-            "modified": "2019-12-12T08:49:49",
-            "accessLevel": "restricted public",
-            "identifier": "1122",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Survey of Inmates in State and Federal Correctional Facilities, 1997"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "This survey provides nationally representative data on inmates\r\nheld in state prisons and federally-owned and operated prisons.\r\nThrough personal interviews conducted from October 2003 through May\r\n2004, inmates in both state and federal prisons provided information\r\nabout their current offense and sentence, criminal history, family\r\nbackground and personal characteristics, prior drug and alcohol use\r\nand treatment programs, gun possession and use, and prison activities,\r\nprograms, and services. Prior surveys of State prison inmates were\r\nconducted in 1974, 1979, 1986, 1991, and 1997. Sentenced federal\r\nprison inmates were interviewed in the 1991 and 1997 surveys.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR04572.v6",
+                    "title": "Survey of Inmates in State and Federal Correctional Facilities, [United States], 2004"
+                }
+            ],
+            "identifier": "1122",
+            "isPartOf": "2171",
+            "issued": "2007-02-28T00:00:00",
             "keyword": [
                 "HIV",
                 "correctional facilities",
@@ -37512,55 +37506,55 @@
                 "substance abuse",
                 "treatment programs"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2019-12-12T08:49:49",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2171",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2007-02-28T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR04572.v6",
-                    "title": "Survey of Inmates in State and Federal Correctional Facilities, [United States], 2004"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Protective Behaviors of Student Victims of Bullying: A Rare Events Analysis of the 2009 School Crime Supplement to the National Crime Victimization Survey",
-            "description": "This study explored whether bullied students (ages 12 through 18, in grades 6 through 12, enrolled during the current school year, and not homeschooled) engage in specific protective behaviors that inhibit learning, put other students' safety at risk, or foster a negative school climate. It also explored whether bullied students' behaviors varied by the type of bullying (direct, verbal, indirect, or cyber) endured. The researchers conducted secondary analyses of the NATIONAL CRIME VICTIMIZATION SURVEY: SCHOOL CRIME SUPPLEMENT, 2009 (ICPSR 28201), using rare events logistic regression, a technique that enables examination of the effects of several independent variables on a dichotomous dependent variable. The dataset produced contains a total of 65 variables, including 18 variables describing direct, verbal, indirect, and cyber bullying behaviors, 4 variables describing response behaviors by those bullied, and 28 variables describing student and school characteristics.",
-            "modified": "2015-02-25T15:25:38",
-            "accessLevel": "public",
-            "identifier": "1143",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Survey of Inmates in State and Federal Correctional Facilities, [United States], 2004"
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
+            "description": "This study explored whether bullied students (ages 12 through 18, in grades 6 through 12, enrolled during the current school year, and not homeschooled) engage in specific protective behaviors that inhibit learning, put other students' safety at risk, or foster a negative school climate. It also explored whether bullied students' behaviors varied by the type of bullying (direct, verbal, indirect, or cyber) endured. The researchers conducted secondary analyses of the NATIONAL CRIME VICTIMIZATION SURVEY: SCHOOL CRIME SUPPLEMENT, 2009 (ICPSR 28201), using rare events logistic regression, a technique that enables examination of the effects of several independent variables on a dichotomous dependent variable. The dataset produced contains a total of 65 variables, including 18 variables describing direct, verbal, indirect, and cyber bullying behaviors, 4 variables describing response behaviors by those bullied, and 28 variables describing student and school characteristics.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR32741.v1",
+                    "title": "Protective Behaviors of Student Victims of Bullying: A Rare Events Analysis of the 2009 School Crime Supplement to the National Crime Victimization Survey"
+                }
+            ],
+            "identifier": "1143",
+            "isPartOf": "2432",
+            "issued": "2015-02-25T15:25:38",
             "keyword": [
                 "abuse",
                 "abused children",
@@ -37577,54 +37571,54 @@
                 "victims",
                 "youths"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2015-02-25T15:25:38",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2015-02-25T15:25:38",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR32741.v1",
-                    "title": "Protective Behaviors of Student Victims of Bullying: A Rare Events Analysis of the 2009 School Crime Supplement to the National Crime Victimization Survey"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data [United States]: Offenses Known and Clearances by Arrest, 2004 ",
-            "description": "Since 1930, the Federal Bureau of Investigation has\r\n compiled the Uniform Crime Reports (UCR) to serve as periodic\r\n nationwide assessments of reported crimes not available elsewhere in\r\n the criminal justice system. Law enforcement agencies contribute\r\n reports either directly or through their state reporting programs.\r\n Each year, summary data are reported in four types of files: (1)\r\n Offenses Known and Clearances by Arrest, (2) Property Stolen and\r\n Recovered, (3) Supplementary Homicide Reports (SHR), and (4) Police\r\n Employee (LEOKA) Data. The Offenses Known and Clearances by Arrest\r\n data files include monthly data on the number of Crime Index offenses\r\n reported and the number of offenses cleared by arrest or other means.\r\n The counts include all reports of Index crimes (excluding arson)\r\n received from victims, officers who discovered infractions, or other\r\nsources.",
-            "modified": "2006-08-18T00:00:00",
-            "accessLevel": "public",
-            "identifier": "1990",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Protective Behaviors of Student Victims of Bullying: A Rare Events Analysis of the 2009 School Crime Supplement to the National Crime Victimization Survey"
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
+            "description": "Since 1930, the Federal Bureau of Investigation has\r\n compiled the Uniform Crime Reports (UCR) to serve as periodic\r\n nationwide assessments of reported crimes not available elsewhere in\r\n the criminal justice system. Law enforcement agencies contribute\r\n reports either directly or through their state reporting programs.\r\n Each year, summary data are reported in four types of files: (1)\r\n Offenses Known and Clearances by Arrest, (2) Property Stolen and\r\n Recovered, (3) Supplementary Homicide Reports (SHR), and (4) Police\r\n Employee (LEOKA) Data. The Offenses Known and Clearances by Arrest\r\n data files include monthly data on the number of Crime Index offenses\r\n reported and the number of offenses cleared by arrest or other means.\r\n The counts include all reports of Index crimes (excluding arson)\r\n received from victims, officers who discovered infractions, or other\r\nsources.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR04459.v1",
+                    "title": "Uniform Crime Reporting Program Data [United States]: Offenses Known and Clearances by Arrest, 2004 "
+                }
+            ],
+            "identifier": "1990",
+            "isPartOf": "2167",
+            "issued": "2006-08-18T00:00:00",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -37634,54 +37628,54 @@
                 "law enforcement",
                 "offenses"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2006-08-18T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2006-08-18T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR04459.v1",
-                    "title": "Uniform Crime Reporting Program Data [United States]: Offenses Known and Clearances by Arrest, 2004 "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, 2004",
-            "description": "These data provide information on the number of arrests\r\n reported to the Federal Bureau of Investigation's Uniform Crime\r\n Reporting (UCR) Program each year by police agencies in the United\r\n States. These arrest reports provide data on 43 offenses including\r\n violent crime, drug use, gambling, and larceny. The data received by\r\n ICPSR were structured as a hierarchical file containing (per reporting\r\n police agency) an agency header record, 1 to 12 monthly header\r\n records, and 1 to 43 detail offense records containing the counts of\r\n arrests by age, sex, and race for a particular offense. ICPSR\r\nrestructured the original data to a rectangular format.",
-            "modified": "2007-02-23T00:00:00",
-            "accessLevel": "public",
-            "identifier": "1991",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Uniform Crime Reporting Program Data [United States]: Offenses Known and Clearances by Arrest, 2004 "
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
+            "description": "These data provide information on the number of arrests\r\n reported to the Federal Bureau of Investigation's Uniform Crime\r\n Reporting (UCR) Program each year by police agencies in the United\r\n States. These arrest reports provide data on 43 offenses including\r\n violent crime, drug use, gambling, and larceny. The data received by\r\n ICPSR were structured as a hierarchical file containing (per reporting\r\n police agency) an agency header record, 1 to 12 monthly header\r\n records, and 1 to 43 detail offense records containing the counts of\r\n arrests by age, sex, and race for a particular offense. ICPSR\r\nrestructured the original data to a rectangular format.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR04460.v2",
+                    "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, 2004"
+                }
+            ],
+            "identifier": "1991",
+            "isPartOf": "2167",
+            "issued": "2006-09-13T00:00:00",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -37706,54 +37700,54 @@
                 "vandalism",
                 "weapons"
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
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2006-09-13T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR04460.v2",
-                    "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, 2004"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, Summarized Yearly, 2004",
-            "description": "These data provide information on the number of arrests\r\nreported to the Federal Bureau of Investigation's Uniform Crime\r\nReporting (UCR) Program each year by police agencies in the United\r\nStates. These arrest reports provide data on 43 offenses including\r\nviolent crime, drug use, gambling, and larceny. The data received by\r\nICPSR were structured as a hierarchical file containing, per reporting\r\npolice agency: an agency header record, and 1 to 43 detail offense\r\nrecords containing the counts of arrests by age, sex, and race for a\r\nparticular offense. ICPSR restructured the original data to logical\r\nrecord length format with the agency header record variables copied\r\nonto the detail records. Consequently, each record contains arrest\r\ncounts for a particular agency-offense.",
-            "modified": "2009-09-28T18:58:25",
-            "accessLevel": "public",
-            "identifier": "1992",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, 2004"
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
+                    "accessURL": "https://doi.org/10.3886/ICPSR04461.v2",
+                    "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, Summarized Yearly, 2004"
+                }
+            ],
+            "identifier": "1992",
+            "isPartOf": "2167",
+            "issued": "2006-09-13T00:00:00",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrest records",
@@ -37769,54 +37763,54 @@
                 "offenses",
                 "violent crime"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2009-09-28T18:58:25",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2006-09-13T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR04461.v2",
-                    "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, Summarized Yearly, 2004"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data [United States]: Police Employee (LEOKA) Data, 2004 ",
-            "description": "Since 1930, the Federal Bureau of Investigation has\r\n compiled the Uniform Crime Reports (UCR) to serve as a periodic\r\n nationwide assessment of reported crimes not available elsewhere in\r\n the criminal justice system. Each year, this information is reported\r\n in four types of files: (1) Offenses Known and Clearances by Arrest,\r\n (2) Property Stolen and Recovered, (3) Supplementary Homicide Reports\r\n (SHR), and (4) Police Employee (LEOKA) Data. The Police Employee\r\n (LEOKA) Data provide information about law enforcement officers killed\r\n or assaulted (hence the acronym, LEOKA) in the line of duty. The\r\n variables created from the LEOKA forms provide in-depth information on\r\n the circumstances surrounding killings or assaults, including type of\r\n call answered, type of weapon used, and type of patrol the officers\r\nwere on.",
-            "modified": "2006-08-18T00:00:00",
-            "accessLevel": "public",
-            "identifier": "1993",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Uniform Crime Reporting Program Data [United States]: Arrests by Age, Sex, and Race, Summarized Yearly, 2004"
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
+                    "accessURL": "https://doi.org/10.3886/ICPSR04462.v1",
+                    "title": "Uniform Crime Reporting Program Data [United States]: Police Employee (LEOKA) Data, 2004 "
+                }
+            ],
+            "identifier": "1993",
+            "isPartOf": "2167",
+            "issued": "2006-08-18T00:00:00",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -37829,54 +37823,54 @@
                 "police deaths",
                 "police officers"
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
-            "issued": "2006-08-18T00:00:00",
             "language": [
                 "eng"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR04462.v1",
-                    "title": "Uniform Crime Reporting Program Data [United States]: Police Employee (LEOKA) Data, 2004 "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data [United States]: Property Stolen and Recovered, 2004 ",
-            "description": "Since 1930, the Federal Bureau of Investigation has\r\n compiled the Uniform Crime Reports (UCR) to serve as periodic\r\n nationwide assessments of reported crimes not available elsewhere in\r\n the criminal justice system. Law enforcement agencies contribute\r\n reports either directly or through their state reporting programs.\r\n Each year, this information is reported in four types of files: (1)\r\n Offenses Known and Clearances by Arrest, (2) Property Stolen and\r\n Recovered, (3) Supplementary Homicide Reports (SHR), and (4) Police\r\n Employee (LEOKA) Data. The Property Stolen and Recovered data are\r\n collected on a monthly basis by all UCR contributing agencies. These\r\n data, aggregated at the agency level, report on the nature of the\r\n crime, the monetary value of the property stolen, and the type of\r\n property stolen. Similar information regarding recovered property is\r\nalso included in the data.",
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
             "modified": "2006-08-18T00:00:00",
-            "accessLevel": "public",
-            "identifier": "1994",
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
+            "title": "Uniform Crime Reporting Program Data [United States]: Police Employee (LEOKA) Data, 2004 "
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
+                    "accessURL": "https://doi.org/10.3886/ICPSR04463.v1",
+                    "title": "Uniform Crime Reporting Program Data [United States]: Property Stolen and Recovered, 2004 "
+                }
+            ],
+            "identifier": "1994",
+            "isPartOf": "2167",
+            "issued": "2006-08-18T00:00:00",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -37891,54 +37885,54 @@
                 "stolen property",
                 "stolen property recovery"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2006-08-18T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2006-08-18T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR04463.v1",
-                    "title": "Uniform Crime Reporting Program Data [United States]: Property Stolen and Recovered, 2004 "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data [United States]: Arson, 2004 ",
-            "description": "Since 1930, the Federal Bureau of Investigation has\r\n compiled the Uniform Crime Reports (UCR) to serve as periodic\r\n nationwide assessments of reported crimes not available elsewhere in\r\n the criminal justice system. Seven main classifications of crime were\r\n chosen to gauge fluctuations in the overall volume and rate of\r\n crime. These seven classifications that eventually became known as the\r\n Crime Index included the violent crimes of murder and non-negligent\r\n manslaughter, forcible rape, robbery, and aggravated assault, and the\r\n property crimes of burglary, larceny-theft, and motor vehicle theft.\r\n By congressional mandate, arson was added as the eighth Index offense\r\n in 1979. Arson is defined as any willful or malicious burning or\r\n attempt to burn, with or without intent to defraud, a dwelling house,\r\n public building, motor vehicle or aircraft, personal property of\r\n another, etc. The arson data files include monthly data on the number\r\n of arson offenses reported and the number of offenses cleared by\r\n arrest or other means. The counts include all reports of arson\r\n received from victims, officers who discovered infractions, or other\r\nsources.",
-            "modified": "2006-07-07T00:00:00",
-            "accessLevel": "public",
-            "identifier": "1995",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Uniform Crime Reporting Program Data [United States]: Property Stolen and Recovered, 2004 "
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
+            "description": "Since 1930, the Federal Bureau of Investigation has\r\n compiled the Uniform Crime Reports (UCR) to serve as periodic\r\n nationwide assessments of reported crimes not available elsewhere in\r\n the criminal justice system. Seven main classifications of crime were\r\n chosen to gauge fluctuations in the overall volume and rate of\r\n crime. These seven classifications that eventually became known as the\r\n Crime Index included the violent crimes of murder and non-negligent\r\n manslaughter, forcible rape, robbery, and aggravated assault, and the\r\n property crimes of burglary, larceny-theft, and motor vehicle theft.\r\n By congressional mandate, arson was added as the eighth Index offense\r\n in 1979. Arson is defined as any willful or malicious burning or\r\n attempt to burn, with or without intent to defraud, a dwelling house,\r\n public building, motor vehicle or aircraft, personal property of\r\n another, etc. The arson data files include monthly data on the number\r\n of arson offenses reported and the number of offenses cleared by\r\n arrest or other means. The counts include all reports of arson\r\n received from victims, officers who discovered infractions, or other\r\nsources.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR04464.v1",
+                    "title": "Uniform Crime Reporting Program Data [United States]: Arson, 2004 "
+                }
+            ],
+            "identifier": "1995",
+            "isPartOf": "2167",
+            "issued": "2006-07-07T00:00:00",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -37949,54 +37943,54 @@
                 "law enforcement",
                 "offenses"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2006-07-07T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2006-07-07T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR04464.v1",
-                    "title": "Uniform Crime Reporting Program Data [United States]: Arson, 2004 "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data [United States]: Supplementary Homicide Reports, 2004 ",
-            "description": "Since 1930, the Federal Bureau of Investigation has\r\ncompiled the Uniform Crime Reports (UCR) to serve as a periodic\r\nnationwide assessment of reported crimes not available elsewhere in\r\nthe criminal justice system. Each year, this information is reported\r\nin four types of files: (1) Offenses Known and Clearances by Arrest,\r\n(2) Property Stolen and Recovered, (3) Supplementary Homicide Reports\r\n(SHR), and (4) Police Employee (LEOKA) Data. The Supplementary\r\nHomicide Reports provide incident-based information on criminal\r\nhomicides reported to the police. These homicides consist of murders,\r\nnon-negligent manslaughter, and justifiable homicides. The data,\r\nprovided monthly by UCR agencies, contain information describing the\r\nvictim of the homicide, the offender, and the relationship between\r\nvictim and offender.",
-            "modified": "2006-08-18T00:00:00",
-            "accessLevel": "public",
-            "identifier": "1996",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Uniform Crime Reporting Program Data [United States]: Arson, 2004 "
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
+            "description": "Since 1930, the Federal Bureau of Investigation has\r\ncompiled the Uniform Crime Reports (UCR) to serve as a periodic\r\nnationwide assessment of reported crimes not available elsewhere in\r\nthe criminal justice system. Each year, this information is reported\r\nin four types of files: (1) Offenses Known and Clearances by Arrest,\r\n(2) Property Stolen and Recovered, (3) Supplementary Homicide Reports\r\n(SHR), and (4) Police Employee (LEOKA) Data. The Supplementary\r\nHomicide Reports provide incident-based information on criminal\r\nhomicides reported to the police. These homicides consist of murders,\r\nnon-negligent manslaughter, and justifiable homicides. The data,\r\nprovided monthly by UCR agencies, contain information describing the\r\nvictim of the homicide, the offender, and the relationship between\r\nvictim and offender.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR04465.v1",
+                    "title": "Uniform Crime Reporting Program Data [United States]: Supplementary Homicide Reports, 2004 "
+                }
+            ],
+            "identifier": "1996",
+            "isPartOf": "2167",
+            "issued": "2006-08-18T00:00:00",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -38010,54 +38004,54 @@
                 "offenses",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2006-08-18T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2006-08-18T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR04465.v1",
-                    "title": "Uniform Crime Reporting Program Data [United States]: Supplementary Homicide Reports, 2004 "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data [United States]: County-Level Detailed Arrest and Offense Data, 2004",
-            "description": "This data collection contains county-level counts of\r\narrests and offenses for Part I offenses (murder, rape, robbery,\r\naggravated assault, burglary, larceny, auto theft, and arson) and\r\ncounts of arrests for Part II offenses (forgery, fraud, embezzlement,\r\nvandalism, weapons violations, sex offenses, drug and alcohol abuse\r\nviolations, gambling, vagrancy, curfew violations, and runaways).",
-            "modified": "2006-07-26T00:00:00",
-            "accessLevel": "public",
-            "identifier": "1997",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Uniform Crime Reporting Program Data [United States]: Supplementary Homicide Reports, 2004 "
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
+                    "accessURL": "https://doi.org/10.3886/ICPSR04466.v1",
+                    "title": "Uniform Crime Reporting Program Data [United States]: County-Level Detailed Arrest and Offense Data, 2004"
+                }
+            ],
+            "identifier": "1997",
+            "isPartOf": "2167",
+            "issued": "2006-07-26T00:00:00",
             "keyword": [
                 "Uniform Crime Reports",
                 "aggravated assault",
@@ -38086,216 +38080,216 @@
                 "vandalism",
                 "weapons offenses"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2006-07-26T00:00:00",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2006-07-26T00:00:00",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR04466.v1",
-                    "title": "Uniform Crime Reporting Program Data [United States]: County-Level Detailed Arrest and Offense Data, 2004"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Offenders Released From Prison, 2005",
-            "description": "The data contain records of sentenced offenders released from the custody of the Bureau of Prisons (BOP) during fiscal year 2005. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. Records of offenders who exit federal prison temporarily, such as for transit to another location, to serve a weekend sentence, or for health care, are not included in the exiting cohort. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2014-03-10T21:55:59",
-            "accessLevel": "restricted public",
-            "identifier": "1998",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Uniform Crime Reporting Program Data [United States]: County-Level Detailed Arrest and Offense Data, 2004"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of sentenced offenders released from the custody of the Bureau of Prisons (BOP) during fiscal year 2005. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. Records of offenders who exit federal prison temporarily, such as for transit to another location, to serve a weekend sentence, or for health care, are not included in the exiting cohort. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR24202.v3",
+                    "title": "Federal Justice Statistics Program: Offenders Released From Prison, 2005"
+                }
+            ],
+            "identifier": "1998",
+            "isPartOf": "2174",
+            "issued": "2009-02-05T12:13:42",
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
+            "modified": "2014-03-10T21:55:59",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2009-02-05T12:13:42",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR24202.v3",
-                    "title": "Federal Justice Statistics Program: Offenders Released From Prison, 2005"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Offenders Released From Prison, 2009",
-            "description": "The data contain records of sentenced offenders released from the custody of the Bureau of Prisons (BOP) during fiscal year 2009. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. Records of offenders who exit federal prison temporarily, such as for transit to another location, to serve a weekend sentence, or for health care, are not included in the exiting cohort. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2014-03-11T12:05:17",
-            "accessLevel": "restricted public",
-            "identifier": "1999",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Offenders Released From Prison, 2005"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of sentenced offenders released from the custody of the Bureau of Prisons (BOP) during fiscal year 2009. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. Records of offenders who exit federal prison temporarily, such as for transit to another location, to serve a weekend sentence, or for health care, are not included in the exiting cohort. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR30786.v2",
+                    "title": "Federal Justice Statistics Program: Offenders Released From Prison, 2009"
+                }
+            ],
+            "identifier": "1999",
+            "isPartOf": "2174",
+            "issued": "2011-06-03T17:21:57",
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
+            "modified": "2014-03-11T12:05:17",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2011-06-03T17:21:57",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR30786.v2",
-                    "title": "Federal Justice Statistics Program: Offenders Released From Prison, 2009"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 2009",
-            "description": "The data contain records of sentenced offenders in the custody of the Bureau of Prisons (BOP) at year-end of fiscal year 2009. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
-            "modified": "2014-03-11T12:10:44",
-            "accessLevel": "restricted public",
-            "identifier": "2000",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Offenders Released From Prison, 2009"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The data contain records of sentenced offenders in the custody of the Bureau of Prisons (BOP) at year-end of fiscal year 2009. The data include commitments of United States District Court, violators of conditions of release (e.g., parole, probation, or supervised release violators), offenders convicted in other courts (e.g., military or District of Columbia courts), and persons admitted to prison as material witnesses or for purposes of treatment, examination, or transfer to another authority. These data include variables that describe the offender, such as age, race, citizenship, as well as variables that describe the sentences and expected prison terms. The data file contains original variables from the Bureau of Prisons' SENTRY database, as well as \"SAF\" variables that denote subsets of the data. These SAF variables are related to statistics reported in the Compendium of Federal Justice Statistics, Tables 7.9-7.16. Variables containing identifying information (e.g., name, Social Security Number) were replaced with blanks, and the day portions of date fields were also sanitized in order to protect the identities of individuals. These data are part of a series designed by the Urban Institute (Washington, DC) and the Bureau of Justice Statistics. Data and documentation were prepared by the Urban Institute.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR30787.v2",
+                    "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 2009"
+                }
+            ],
+            "identifier": "2000",
+            "isPartOf": "2174",
+            "issued": "2011-06-03T17:27:04",
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
+            "modified": "2014-03-11T12:10:44",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2174",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2011-06-03T17:27:04",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR30787.v2",
-                    "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 2009"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data: Arrests by Age, Sex, and Race, United States, 2013",
-            "description": "These data provide information on the number of arrests reported to the Federal Bureau of Investigation's (FBI) Uniform Crime Reporting (UCR) Program each month by police agencies in the United States. Although not as well known as the \"Crimes Known to the Police\" data drawn from the Uniform Crime Report's Return A form, the arrest reports by age, sex, and race provide valuable data on 43 offenses including violent, drug, gambling, and larceny crimes. The data received by ICPSR were structured as a hierarchical file containing (per reporting police agency) an agency header record, and 1 to 12 monthly header reports, and 1 to 43 detail offense records containing the counts of arrests by age, sex, and race for a particular offense. ICPSR restructured the original data to a rectangular format.",
-            "modified": "2015-10-07T14:52:27",
-            "accessLevel": "public",
-            "identifier": "2001",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
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
+            "title": "Federal Justice Statistics Program: Offenders in Prison at Year-End, 2009"
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
+            "description": "These data provide information on the number of arrests reported to the Federal Bureau of Investigation's (FBI) Uniform Crime Reporting (UCR) Program each month by police agencies in the United States. Although not as well known as the \"Crimes Known to the Police\" data drawn from the Uniform Crime Report's Return A form, the arrest reports by age, sex, and race provide valuable data on 43 offenses including violent, drug, gambling, and larceny crimes. The data received by ICPSR were structured as a hierarchical file containing (per reporting police agency) an agency header record, and 1 to 12 monthly header reports, and 1 to 43 detail offense records containing the counts of arrests by age, sex, and race for a particular offense. ICPSR restructured the original data to a rectangular format.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR36115.v1",
+                    "title": "Uniform Crime Reporting Program Data: Arrests by Age, Sex, and Race, United States, 2013"
+                }
+            ],
+            "identifier": "2001",
+            "isPartOf": "2167",
+            "issued": "2015-10-07T14:52:27",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -38320,54 +38314,54 @@
                 "vandalism",
                 "weapons"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2015-10-07T14:52:27",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2015-10-07T14:52:27",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR36115.v1",
-                    "title": "Uniform Crime Reporting Program Data: Arrests by Age, Sex, and Race, United States, 2013"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data: Arrests by Age, Sex, and Race, Summarized Yearly, United States, 2013",
-            "description": "These data provide information on the number of arrests\r\nreported to the Federal Bureau of Investigation's Uniform Crime\r\nReporting (UCR) Program each year by police agencies in the United\r\nStates. These arrest reports provide data on 43 offenses including\r\nviolent crime, drug use, gambling, and larceny. The data received by\r\nICPSR were structured as a hierarchical file containing, per reporting\r\npolice agency: an agency header record, and 1 to 43 detail offense\r\nrecords containing the counts of arrests by age, sex, and race for a\r\nparticular offense. ICPSR restructured the original data to logical\r\nrecord length format with the agency header record variables copied\r\nonto the detail records. Consequently, each record contains arrest\r\ncounts for a particular agency-offense.",
-            "modified": "2015-04-30T11:18:25",
-            "accessLevel": "public",
-            "identifier": "2002",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Uniform Crime Reporting Program Data: Arrests by Age, Sex, and Race, United States, 2013"
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
+                    "accessURL": "https://doi.org/10.3886/ICPSR36116.v1",
+                    "title": "Uniform Crime Reporting Program Data: Arrests by Age, Sex, and Race, Summarized Yearly, United States, 2013"
+                }
+            ],
+            "identifier": "2002",
+            "isPartOf": "2167",
+            "issued": "2015-04-30T11:18:25",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrest records",
@@ -38383,54 +38377,54 @@
                 "offenses",
                 "violent crime"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2015-04-30T11:18:25",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2015-04-30T11:18:25",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR36116.v1",
-                    "title": "Uniform Crime Reporting Program Data: Arrests by Age, Sex, and Race, Summarized Yearly, United States, 2013"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data: County-Level Detailed Arrest and Offense Data, United States, 2013",
-            "description": "This data collection contains county-level counts of\r\narrests and offenses for Part I offenses (murder, rape, robbery,\r\naggravated assault, burglary, larceny, auto theft, and arson) and\r\ncounts of arrests for Part II offenses (forgery, fraud, embezzlement,\r\nvandalism, weapons violations, sex offenses, drug and alcohol abuse\r\nviolations, gambling, vagrancy, curfew violations, and runaways).",
-            "modified": "2017-09-12T10:32:25",
-            "accessLevel": "public",
-            "identifier": "2003",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Uniform Crime Reporting Program Data: Arrests by Age, Sex, and Race, Summarized Yearly, United States, 2013"
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
+                    "accessURL": "https://doi.org/10.3886/ICPSR36117.v2",
+                    "title": "Uniform Crime Reporting Program Data: County-Level Detailed Arrest and Offense Data, United States, 2013"
+                }
+            ],
+            "identifier": "2003",
+            "isPartOf": "2167",
+            "issued": "2016-08-22T10:16:09",
             "keyword": [
                 "Uniform Crime Reports",
                 "aggravated assault",
@@ -38458,54 +38452,54 @@
                 "vandalism",
                 "weapons offenses"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2017-09-12T10:32:25",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2016-08-22T10:16:09",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR36117.v2",
-                    "title": "Uniform Crime Reporting Program Data: County-Level Detailed Arrest and Offense Data, United States, 2013"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data: Hate Crime Data, 2013 [Record-Type Files]",
-            "description": "In response to a growing concern about hate crimes, the\r\nUnited States Congress enacted the Hate Crime Statistics Act of\r\n1990. The Act requires the attorney general to establish guidelines\r\nand collect, as part of the Uniform Crime Reporting (UCR) Program,\r\ndata \"about crimes that manifest evidence of prejudice based on race,\r\nreligion, sexual orientation, or ethnicity, including where\r\nappropriate the crimes of murder and non-negligent manslaughter,\r\nforcible rape, aggravated assault, simple assault, intimidation,\r\narson, and destruction, damage or vandalism of property.\" Hate crime\r\ndata collection was required by the Act to begin in calendar year 1990\r\nand to continue for four successive years. In September 1994, the\r\nViolent Crime Control and Law Enforcement Act amended the Hate Crime\r\nStatistics Act to add disabilities, both physical and mental, as\r\nfactors that could be considered a basis for hate crimes. Although the\r\nAct originally mandated data collection for five years, the Church\r\nArson Prevention Act of 1996 amended the collection duration \"for each\r\ncalendar year,\" making hate crime statistics a permanent addition to\r\nthe UCR program. As with the other UCR data, law enforcement agencies\r\ncontribute reports either directly or through their state reporting\r\nprograms. Information contained in the data includes number of victims\r\nand offenders involved in each hate crime incident, type of victims,\r\nbias motivation, offense type, and location type.",
-            "modified": "2015-11-13T12:07:26",
-            "accessLevel": "public",
-            "identifier": "2004",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Uniform Crime Reporting Program Data: County-Level Detailed Arrest and Offense Data, United States, 2013"
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
+                    "accessURL": "https://doi.org/10.3886/ICPSR36118.v1",
+                    "title": "Uniform Crime Reporting Program Data: Hate Crime Data, 2013 [Record-Type Files]"
+                }
+            ],
+            "identifier": "2004",
+            "isPartOf": "2167",
+            "issued": "2015-11-13T12:07:26",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -38524,54 +38518,54 @@
                 "religion",
                 "violence"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2015-11-13T12:07:26",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2015-11-13T12:07:26",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR36118.v1",
-                    "title": "Uniform Crime Reporting Program Data: Hate Crime Data, 2013 [Record-Type Files]"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data: Police Employee (LEOKA) Data, 2013",
-            "description": "The Uniform Crime Reporting Program Data, Police Employee Data, 2013 file contains monthly data on felonious or accidental killings and assaults upon United States law enforcement officers acting in the line of duty. The Federal Bureau of Investigation (FBI) assembled the data and processed them from UCR Master Police Employee (LEOKA) data tapes.\r\nEach agency record in the file includes the following summary variables: state code, population group code, geographic division, Metropolitan Statistical Area code, and agency name. These variables afford considerable flexibility in creating subsets or aggregations of the data.\r\nSince 1930, the Federal Bureau of Investigation has compiled the Uniform Crime Reports (UCR) to serve as a periodic nationwide assessment of reported crimes not available elsewhere in the criminal justice system. Each year, this information is reported in four types of files: (1) Offenses Known and Clearances by Arrest, (2) Property Stolen and Recovered, (3) Supplementary Homicide Reports (SHR), and (4) Police Employee (LEOKA) Data. The Police Employee (LEOKA) Data provide information about law enforcement officers killed or assaulted (hence the acronym, LEOKA) in the line of duty. The variables created from the LEOKA forms provide in-depth information on the circumstances surrounding killings or assaults, including type of call answered, type of weapon used, and type of patrol the officers were on.",
-            "modified": "2015-05-07T08:54:43",
-            "accessLevel": "public",
-            "identifier": "2005",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Uniform Crime Reporting Program Data: Hate Crime Data, 2013 [Record-Type Files]"
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
+            "description": "The Uniform Crime Reporting Program Data, Police Employee Data, 2013 file contains monthly data on felonious or accidental killings and assaults upon United States law enforcement officers acting in the line of duty. The Federal Bureau of Investigation (FBI) assembled the data and processed them from UCR Master Police Employee (LEOKA) data tapes.\r\nEach agency record in the file includes the following summary variables: state code, population group code, geographic division, Metropolitan Statistical Area code, and agency name. These variables afford considerable flexibility in creating subsets or aggregations of the data.\r\nSince 1930, the Federal Bureau of Investigation has compiled the Uniform Crime Reports (UCR) to serve as a periodic nationwide assessment of reported crimes not available elsewhere in the criminal justice system. Each year, this information is reported in four types of files: (1) Offenses Known and Clearances by Arrest, (2) Property Stolen and Recovered, (3) Supplementary Homicide Reports (SHR), and (4) Police Employee (LEOKA) Data. The Police Employee (LEOKA) Data provide information about law enforcement officers killed or assaulted (hence the acronym, LEOKA) in the line of duty. The variables created from the LEOKA forms provide in-depth information on the circumstances surrounding killings or assaults, including type of call answered, type of weapon used, and type of patrol the officers were on.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR36119.v1",
+                    "title": "Uniform Crime Reporting Program Data: Police Employee (LEOKA) Data, 2013"
+                }
+            ],
+            "identifier": "2005",
+            "isPartOf": "2167",
+            "issued": "2015-05-07T08:54:43",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -38584,54 +38578,54 @@
                 "police deaths",
                 "police officers"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2015-05-07T08:54:43",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2015-05-07T08:54:43",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR36119.v1",
-                    "title": "Uniform Crime Reporting Program Data: Police Employee (LEOKA) Data, 2013"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data: National Incident-Based Reporting System, 2013",
-            "description": "The National Incident-Based Reporting System (NIBRS) is a\r\npart of the Uniform Crime Reporting Program (UCR), administered by the\r\nFederal Bureau of Investigation (FBI). In the late 1970s, the law\r\nenforcement community called for a thorough evaluative study of the\r\nUCR with the objective of recommending an expanded and enhanced UCR\r\nprogram to meet law enforcement needs into the 21st century. The FBI\r\nfully concurred with the need for an updated program to meet\r\ncontemporary needs and provided its support, formulating a\r\ncomprehensive redesign effort. Following a multiyear study, a\r\n\"Blueprint for the Future of the Uniform Crime Reporting Program\" was\r\ndeveloped. Using the \"Blueprint,\" and in consultation with local and\r\nstate law enforcement executives, the FBI formulated new guidelines\r\nfor the Uniform Crime Reports. The National Incident-Based Reporting\r\nSystem (NIBRS) was implemented to meet these guidelines. NIBRS data\r\nare archived at ICPSR as 11 separate data files per year, which may be\r\nmerged by using linkage variables. Prior to 2013 the data were archived and distributed as 13 separate data files, including three separate batch header record files. In 2013 the FBI combined the three batch header files into one file. Consequently, ICPSR instituted new file numbering for the 2013 data. NIBRS data focus on a variety of\r\naspects of a crime incident. Part 2 (formerly Part 4), Administrative Segment, offers\r\ndata on the incident itself (date and time). Each crime incident is\r\ndelineated by one administrative segment record. Also provided are\r\nPart 3 (formerly Part 5), Offense Segment (offense type, location, weapon use, and bias\r\nmotivation), Part 4 (formerly Part 6), Property Segment (type of property loss, property\r\ndescription, property value, drug type and quantity), Part 5 (formerly Part 7), Victim\r\nSegment (age, sex, race, ethnicity, and injuries), Part 6 (formerly Part 8), Offender\r\nSegment (age, sex, and race), and Part 7 (formerly Part 9), Arrestee Segment (arrest\r\ndate, age, sex, race, and weapon use). The Batch Header Segment (Part 1, formerly Parts\r\n1-3) separates and identifies individual police agencies by\r\nOriginating Agency Identifier (ORI). Batch Header information, which\r\nis contained on three records for each ORI, includes agency name,\r\ngeographic location, and population of the area. Part 8 (formerly Part 10), Group B\r\nArrest Report Segment, includes arrestee data for Group B crimes.\r\nWindow Segments files (Parts 9-11, formerly Parts 11-13) pertain to incidents for which the\r\ncomplete Group A Incident Report was not submitted to the FBI. In\r\ngeneral, a Window Segment record will be generated if the incident\r\noccurred prior to January 1 of the previous year or if the incident\r\noccurred prior to when the agency started NIBRS reporting. As with the\r\nUCR, participation in NIBRS is voluntary on the part of law\r\nenforcement agencies. The data are not a representative sample of\r\ncrime in the United States.",
-            "modified": "2015-06-29T10:29:56",
-            "accessLevel": "public",
-            "identifier": "2006",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Uniform Crime Reporting Program Data: Police Employee (LEOKA) Data, 2013"
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
+            "description": "The National Incident-Based Reporting System (NIBRS) is a\r\npart of the Uniform Crime Reporting Program (UCR), administered by the\r\nFederal Bureau of Investigation (FBI). In the late 1970s, the law\r\nenforcement community called for a thorough evaluative study of the\r\nUCR with the objective of recommending an expanded and enhanced UCR\r\nprogram to meet law enforcement needs into the 21st century. The FBI\r\nfully concurred with the need for an updated program to meet\r\ncontemporary needs and provided its support, formulating a\r\ncomprehensive redesign effort. Following a multiyear study, a\r\n\"Blueprint for the Future of the Uniform Crime Reporting Program\" was\r\ndeveloped. Using the \"Blueprint,\" and in consultation with local and\r\nstate law enforcement executives, the FBI formulated new guidelines\r\nfor the Uniform Crime Reports. The National Incident-Based Reporting\r\nSystem (NIBRS) was implemented to meet these guidelines. NIBRS data\r\nare archived at ICPSR as 11 separate data files per year, which may be\r\nmerged by using linkage variables. Prior to 2013 the data were archived and distributed as 13 separate data files, including three separate batch header record files. In 2013 the FBI combined the three batch header files into one file. Consequently, ICPSR instituted new file numbering for the 2013 data. NIBRS data focus on a variety of\r\naspects of a crime incident. Part 2 (formerly Part 4), Administrative Segment, offers\r\ndata on the incident itself (date and time). Each crime incident is\r\ndelineated by one administrative segment record. Also provided are\r\nPart 3 (formerly Part 5), Offense Segment (offense type, location, weapon use, and bias\r\nmotivation), Part 4 (formerly Part 6), Property Segment (type of property loss, property\r\ndescription, property value, drug type and quantity), Part 5 (formerly Part 7), Victim\r\nSegment (age, sex, race, ethnicity, and injuries), Part 6 (formerly Part 8), Offender\r\nSegment (age, sex, and race), and Part 7 (formerly Part 9), Arrestee Segment (arrest\r\ndate, age, sex, race, and weapon use). The Batch Header Segment (Part 1, formerly Parts\r\n1-3) separates and identifies individual police agencies by\r\nOriginating Agency Identifier (ORI). Batch Header information, which\r\nis contained on three records for each ORI, includes agency name,\r\ngeographic location, and population of the area. Part 8 (formerly Part 10), Group B\r\nArrest Report Segment, includes arrestee data for Group B crimes.\r\nWindow Segments files (Parts 9-11, formerly Parts 11-13) pertain to incidents for which the\r\ncomplete Group A Incident Report was not submitted to the FBI. In\r\ngeneral, a Window Segment record will be generated if the incident\r\noccurred prior to January 1 of the previous year or if the incident\r\noccurred prior to when the agency started NIBRS reporting. As with the\r\nUCR, participation in NIBRS is voluntary on the part of law\r\nenforcement agencies. The data are not a representative sample of\r\ncrime in the United States.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR36120.v2",
+                    "title": "Uniform Crime Reporting Program Data: National Incident-Based Reporting System, 2013"
+                }
+            ],
+            "identifier": "2006",
+            "isPartOf": "2433",
+            "issued": "2015-05-27T18:10:07",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -38645,54 +38639,54 @@
                 "victims",
                 "violent crime"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2015-06-29T10:29:56",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2433",
-            "dataQuality": false,
-            "issued": "2015-05-27T18:10:07",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR36120.v2",
-                    "title": "Uniform Crime Reporting Program Data: National Incident-Based Reporting System, 2013"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Incident-Based Reporting System, 2013: Extract Files",
-            "description": "The National Incident-Based Reporting System (NIBRS) is a\r\npart of the Uniform Crime Reporting Program (UCR), administered by the\r\nFederal Bureau of Investigation (FBI). The extract files version of\r\nNIBRS was created to simplify working with NIBRS data. Data management\r\nissues with NIBRS are significant, especially when two or more segment\r\nlevels are being merged. These issues require skills separate from\r\ndata analysis. NIBRS data as formatted by the FBI are stored in a\r\nsingle file. These data are organized by various segment levels\r\n(record types). There are six main segment levels: administrative,\r\noffense, property, victim, offender, and arrestee. Each segment level\r\nhas a different length and layout. There are other segment levels that\r\noccur with less frequency than the six main levels. Significant\r\ncomputing resources are necessary to work with the data in its\r\nsingle-file format. In addition, the user must be sophisticated in\r\nworking with data in complex file types. For these reasons and the\r\ndesire to facilitate the use of NIBRS data, ICPSR created the extract\r\nfiles. The data are not a representative sample of crime in the United\r\nStates.",
-            "modified": "2018-10-02T13:12:26",
-            "accessLevel": "public",
-            "identifier": "2007",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Uniform Crime Reporting Program Data: National Incident-Based Reporting System, 2013"
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
+                    "accessURL": "https://doi.org/10.3886/ICPSR36121.v2",
+                    "title": "National Incident-Based Reporting System, 2013: Extract Files"
+                }
+            ],
+            "identifier": "2007",
+            "isPartOf": "2433",
+            "issued": "2015-08-04T20:09:31",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -38707,54 +38701,54 @@
                 "victims",
                 "violent crime"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2018-10-02T13:12:26",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2433",
-            "dataQuality": false,
-            "issued": "2015-08-04T20:09:31",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR36121.v2",
-                    "title": "National Incident-Based Reporting System, 2013: Extract Files"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data: Offenses Known and Clearances by Arrest, 2013",
-            "description": "The UNIFORM CRIME REPORTING PROGRAM DATA: OFFENSES KNOWN AND CLEARANCES BY ARREST, 2013 dataset is a compilation of offenses reported to law enforcement agencies in the United States. Due to the vast number of categories of crime committed in the United States, the FBI has limited the type of crimes included in this compilation to those crimes which people are most likely to report to police and those crimes which occur frequently enough to be analyzed across time. Crimes included are criminal homicide, forcible rape, robbery, aggravated assault, burglary, larceny-theft, and motor vehicle theft.\r\nMuch information about these crimes is provided in this dataset. The number of times an offense has been reported, the number of reported offenses that have been cleared by arrests, and the number of cleared offenses which involved offenders under the age of 18 are the major items of information collected.",
-            "modified": "2015-04-24T15:52:21",
-            "accessLevel": "public",
-            "identifier": "2008",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Incident-Based Reporting System, 2013: Extract Files"
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
+            "description": "The UNIFORM CRIME REPORTING PROGRAM DATA: OFFENSES KNOWN AND CLEARANCES BY ARREST, 2013 dataset is a compilation of offenses reported to law enforcement agencies in the United States. Due to the vast number of categories of crime committed in the United States, the FBI has limited the type of crimes included in this compilation to those crimes which people are most likely to report to police and those crimes which occur frequently enough to be analyzed across time. Crimes included are criminal homicide, forcible rape, robbery, aggravated assault, burglary, larceny-theft, and motor vehicle theft.\r\nMuch information about these crimes is provided in this dataset. The number of times an offense has been reported, the number of reported offenses that have been cleared by arrests, and the number of cleared offenses which involved offenders under the age of 18 are the major items of information collected.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR36122.v1",
+                    "title": "Uniform Crime Reporting Program Data: Offenses Known and Clearances by Arrest, 2013"
+                }
+            ],
+            "identifier": "2008",
+            "isPartOf": "2167",
+            "issued": "2015-04-24T15:52:21",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -38764,54 +38758,54 @@
                 "law enforcement",
                 "offenses"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2015-04-24T15:52:21",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2015-04-24T15:52:21",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR36122.v1",
-                    "title": "Uniform Crime Reporting Program Data: Offenses Known and Clearances by Arrest, 2013"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data: Property Stolen and Recovered, 2013",
-            "description": "The UNIFORM CRIME REPORTING PROGRAM DATA: PROPERTY STOLEN AND RECOVERED,\r\n2013 file (also known as the Supplement to Return A) is collected at the agency level and includes detailed monthly data on the nature of crime and the value and type of property stolen and recovered incident to each crime. The Return A Supplement requires that a value be established for property stolen and recovered in each Crime Index category except aggravated assault. It is designed to record the value of property stolen and recovered in the following eleven classifications: Currency/notes, Jewelry and Precious Metals, Clothing and Furs, Locally Stolen Motor Vehicles, Office Equipment, Televisions/Radios, Firearms, Household Goods, Consumable Goods, Livestock, and Miscellaneous. The determination of the value of property stolen is an obligation of the investigating officer, and such information is essential to assure the completeness of a law enforcement investigative report on stolen property. The data were originally assembled by the Federal Bureau of Investigation (FBI) from reports submitted by agencies participating in the UCR. The ICPSR file was processed from Return A Supplement files provided by the FBI.",
-            "modified": "2015-08-04T11:17:02",
-            "accessLevel": "public",
-            "identifier": "2009",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Uniform Crime Reporting Program Data: Offenses Known and Clearances by Arrest, 2013"
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
+            "description": "The UNIFORM CRIME REPORTING PROGRAM DATA: PROPERTY STOLEN AND RECOVERED,\r\n2013 file (also known as the Supplement to Return A) is collected at the agency level and includes detailed monthly data on the nature of crime and the value and type of property stolen and recovered incident to each crime. The Return A Supplement requires that a value be established for property stolen and recovered in each Crime Index category except aggravated assault. It is designed to record the value of property stolen and recovered in the following eleven classifications: Currency/notes, Jewelry and Precious Metals, Clothing and Furs, Locally Stolen Motor Vehicles, Office Equipment, Televisions/Radios, Firearms, Household Goods, Consumable Goods, Livestock, and Miscellaneous. The determination of the value of property stolen is an obligation of the investigating officer, and such information is essential to assure the completeness of a law enforcement investigative report on stolen property. The data were originally assembled by the Federal Bureau of Investigation (FBI) from reports submitted by agencies participating in the UCR. The ICPSR file was processed from Return A Supplement files provided by the FBI.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR36123.v1",
+                    "title": "Uniform Crime Reporting Program Data: Property Stolen and Recovered, 2013"
+                }
+            ],
+            "identifier": "2009",
+            "isPartOf": "2167",
+            "issued": "2015-08-04T11:17:02",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -38826,54 +38820,54 @@
                 "stolen property",
                 "stolen property recovery"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2015-08-04T11:17:02",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2015-08-04T11:17:02",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR36123.v1",
-                    "title": "Uniform Crime Reporting Program Data: Property Stolen and Recovered, 2013"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Uniform Crime Reporting Program Data: Supplementary Homicide Reports, 2013",
-            "description": "The UNIFORM CRIME REPORTING PROGRAM DATA: SUPPLEMENTARY HOMICIDE REPORTS, 2013 (SHR) provide detailed information on criminal homicides reported to the police. These homicides consist of murders; non-negligent killings also called non-negligent manslaughter; and justifiable homicides. UCR Program contributors compile and submit their crime data by one of two means: either directly to the FBI or through their State UCR Programs. State UCR Programs frequently impose mandatory reporting requirements which have been effective in increasing both the number of reporting agencies as well as the number and accuracy of each participating agency's reports. Each agency may be identified by its numeric state code, alpha-numeric agency (\"ORI\") code, jurisdiction population, and population group. In addition, each homicide incident is identified by month of occurrence and situation type, allowing flexibility in creating aggregations and subsets.",
-            "modified": "2015-04-24T15:45:10",
-            "accessLevel": "public",
-            "identifier": "2010",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Uniform Crime Reporting Program Data: Property Stolen and Recovered, 2013"
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
+            "description": "The UNIFORM CRIME REPORTING PROGRAM DATA: SUPPLEMENTARY HOMICIDE REPORTS, 2013 (SHR) provide detailed information on criminal homicides reported to the police. These homicides consist of murders; non-negligent killings also called non-negligent manslaughter; and justifiable homicides. UCR Program contributors compile and submit their crime data by one of two means: either directly to the FBI or through their State UCR Programs. State UCR Programs frequently impose mandatory reporting requirements which have been effective in increasing both the number of reporting agencies as well as the number and accuracy of each participating agency's reports. Each agency may be identified by its numeric state code, alpha-numeric agency (\"ORI\") code, jurisdiction population, and population group. In addition, each homicide incident is identified by month of occurrence and situation type, allowing flexibility in creating aggregations and subsets.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR36124.v1",
+                    "title": "Uniform Crime Reporting Program Data: Supplementary Homicide Reports, 2013"
+                }
+            ],
+            "identifier": "2010",
+            "isPartOf": "2167",
+            "issued": "2015-04-24T15:45:10",
             "keyword": [
                 "Uniform Crime Reports",
                 "arrests",
@@ -38886,54 +38880,54 @@
                 "offenses",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2015-04-24T15:45:10",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2167",
-            "dataQuality": false,
-            "issued": "2015-04-24T15:45:10",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR36124.v1",
-                    "title": "Uniform Crime Reporting Program Data: Supplementary Homicide Reports, 2013"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Census of Jails, 2013",
-            "description": "To reduce respondent burden for the 2013 collection, the Census of Jails was combined with the Deaths in Custody Reporting Program (DCRP). The census provides the sampling frame for the nationwide Survey of Inmates in Local Jails (SILJ) and the Annual Survey of Jails (ASJ). Previous jail enumerations were conducted in 1970 (ICPSR 7641), 1972 (ICPSR 7638), 1978 (ICPSR 7737), 1983 (ICPSR 8203), 1988 (ICPSR 9256), 1993 (ICPSR 6648), 1999 (ICPSR 3318), 2005 (ICPSR 20367), and 2006 (ICPSR 26602). The RTI International collected the data for the Bureau of Justice Statistics in 2013. The United States Census Bureau was the collection agent from 1970-2006.\r\nThe 2013 Census of Jails gathered data from all jail detention facilities holding inmates beyond arraignment, a period normally exceeding 72 hours. Jail facilities were operated by cities and counties, by private entities under contract to correctional authorities, and by the Federal Bureau of Prisons (BOP).\r\nExcluded from the census were physically separate temporary holding facilities such as drunk tanks and police lockups that do not hold persons after being formally charged in court. Also excluded were state-operated facilities in Connecticut, Delaware, Hawaii, Rhode Island, Vermont, and Alaska, which have combined jail-prison systems. Fifteen independently operated jails in Alaska were included in the Census.\r\nThe 2013 census collected facility-level information on the number of confined and nonconfined inmates, number of inmates participating in weekend programs, number of confined non-U.S. citizens, number of confined inmates by sex and adult or juvenile status, number of juveniles held as adults, conviction and sentencing status, offense type, number of inmates held by race or Hispanic origin, number of inmates held for other jurisdictions or authorities, average daily population, rated capacity, number of admissions and releases, program participation for nonconfined inmates, operating expenditures, and staff by occupational category. ",
-            "modified": "2018-04-25T12:15:10",
-            "accessLevel": "public",
-            "identifier": "2011",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Uniform Crime Reporting Program Data: Supplementary Homicide Reports, 2013"
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
+            "description": "To reduce respondent burden for the 2013 collection, the Census of Jails was combined with the Deaths in Custody Reporting Program (DCRP). The census provides the sampling frame for the nationwide Survey of Inmates in Local Jails (SILJ) and the Annual Survey of Jails (ASJ). Previous jail enumerations were conducted in 1970 (ICPSR 7641), 1972 (ICPSR 7638), 1978 (ICPSR 7737), 1983 (ICPSR 8203), 1988 (ICPSR 9256), 1993 (ICPSR 6648), 1999 (ICPSR 3318), 2005 (ICPSR 20367), and 2006 (ICPSR 26602). The RTI International collected the data for the Bureau of Justice Statistics in 2013. The United States Census Bureau was the collection agent from 1970-2006.\r\nThe 2013 Census of Jails gathered data from all jail detention facilities holding inmates beyond arraignment, a period normally exceeding 72 hours. Jail facilities were operated by cities and counties, by private entities under contract to correctional authorities, and by the Federal Bureau of Prisons (BOP).\r\nExcluded from the census were physically separate temporary holding facilities such as drunk tanks and police lockups that do not hold persons after being formally charged in court. Also excluded were state-operated facilities in Connecticut, Delaware, Hawaii, Rhode Island, Vermont, and Alaska, which have combined jail-prison systems. Fifteen independently operated jails in Alaska were included in the Census.\r\nThe 2013 census collected facility-level information on the number of confined and nonconfined inmates, number of inmates participating in weekend programs, number of confined non-U.S. citizens, number of confined inmates by sex and adult or juvenile status, number of juveniles held as adults, conviction and sentencing status, offense type, number of inmates held by race or Hispanic origin, number of inmates held for other jurisdictions or authorities, average daily population, rated capacity, number of admissions and releases, program participation for nonconfined inmates, operating expenditures, and staff by occupational category. ",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR36128.v4",
+                    "title": "Census of Jails, 2013"
+                }
+            ],
+            "identifier": "2011",
+            "isPartOf": "2169",
+            "issued": "2015-12-08T12:17:20",
             "keyword": [
                 "census data",
                 "correctional facilities",
@@ -38948,54 +38942,54 @@
                 "jails",
                 "personnel"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2018-04-25T12:15:10",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2169",
-            "dataQuality": false,
-            "issued": "2015-12-08T12:17:20",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR36128.v4",
-                    "title": "Census of Jails, 2013"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Capital Punishment in the United States, 1973-2013",
-            "description": "CAPITAL PUNISHMENT IN THE UNITED STATES, 1973-2013 provides annual data on prisoners under a sentence of death, as well as those who had their sentences commuted or vacated and prisoners who were executed. This study examines basic sociodemographic classifications including age, sex, race and ethnicity, marital status at time of imprisonment, level of education, and state and region of incarceration. Criminal history information includes prior felony convictions and prior convictions for criminal homicide and the legal status at the time of the capital offense. Additional information is provided on those inmates removed from death row by yearend 2013.\r\nThe dataset consists of one part which contains 9,058 cases. The file provides information on inmates whose death sentences were removed in addition to information on those inmates who were executed. The file also gives information about inmates who received a second death sentence by yearend 2013 as well as inmates who were already on death row.",
-            "modified": "2020-12-17T09:48:48",
-            "accessLevel": "restricted public",
-            "identifier": "2012",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Census of Jails, 2013"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "CAPITAL PUNISHMENT IN THE UNITED STATES, 1973-2013 provides annual data on prisoners under a sentence of death, as well as those who had their sentences commuted or vacated and prisoners who were executed. This study examines basic sociodemographic classifications including age, sex, race and ethnicity, marital status at time of imprisonment, level of education, and state and region of incarceration. Criminal history information includes prior felony convictions and prior convictions for criminal homicide and the legal status at the time of the capital offense. Additional information is provided on those inmates removed from death row by yearend 2013.\r\nThe dataset consists of one part which contains 9,058 cases. The file provides information on inmates whose death sentences were removed in addition to information on those inmates who were executed. The file also gives information about inmates who received a second death sentence by yearend 2013 as well as inmates who were already on death row.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR36139.v2",
+                    "title": "Capital Punishment in the United States, 1973-2013"
+                }
+            ],
+            "identifier": "2012",
+            "isPartOf": "2587",
+            "issued": "2015-05-07T14:20:26",
             "keyword": [
                 "capital punishment",
                 "commuted sentences",
@@ -39008,55 +39002,55 @@
                 "sentencing",
                 "states (USA)"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2020-12-17T09:48:48",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2587",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2015-05-07T14:20:26",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR36139.v2",
-                    "title": "Capital Punishment in the United States, 1973-2013"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Victimization Survey, [United States], 2014",
-            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a nationally-representative sample of residential addresses since 1973. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, motor vehicle theft, and vandalism. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations. This version of the NCVS, referred to as the collection year, contains records from interviews conducted in the 12 months of the given year.",
-            "modified": "2020-07-23T18:18:45",
-            "accessLevel": "public",
-            "identifier": "2013",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Capital Punishment in the United States, 1973-2013"
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
+                    "accessURL": "https://doi.org/10.3886/ICPSR36142.v2",
+                    "title": "National Crime Victimization Survey, [United States], 2014"
+                }
+            ],
+            "identifier": "2013",
+            "isPartOf": "2432",
+            "issued": "2015-08-27T10:01:36",
             "keyword": [
                 "assault",
                 "auto theft",
@@ -39077,54 +39071,54 @@
                 "victimization",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2020-07-23T18:18:45",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2015-08-27T10:01:36",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR36142.v2",
-                    "title": "National Crime Victimization Survey, [United States], 2014"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Victimization Survey, Concatenated File, 1992-2014",
-            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a nationally-representative sample of residential addresses since 1973. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, motor vehicle theft, and vandalism. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations. \r\nThis dataset represents the concatenated version of the NCVS on a collection year basis for 1992-2014.  A collection year contains records from interviews conducted in the 12 months of the given year.  Under the collection year format, victimizations are counted in the year the interview is conducted, regardless of the year when the crime incident occurred.\r\nFor additional information, please see the documentation for the data from the most current year of the NCVS, ICPSR Study 36142.",
-            "modified": "2016-03-01T18:34:56",
-            "accessLevel": "public",
-            "identifier": "2014",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Victimization Survey, [United States], 2014"
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
+            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a nationally-representative sample of residential addresses since 1973. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, motor vehicle theft, and vandalism. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations. \r\nThis dataset represents the concatenated version of the NCVS on a collection year basis for 1992-2014.  A collection year contains records from interviews conducted in the 12 months of the given year.  Under the collection year format, victimizations are counted in the year the interview is conducted, regardless of the year when the crime incident occurred.\r\nFor additional information, please see the documentation for the data from the most current year of the NCVS, ICPSR Study 36142.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR36143.v1",
+                    "title": "National Crime Victimization Survey, Concatenated File, 1992-2014"
+                }
+            ],
+            "identifier": "2014",
+            "isPartOf": "2432",
+            "issued": "2015-08-27T10:17:20",
             "keyword": [
                 "assault",
                 "auto theft",
@@ -39145,54 +39139,54 @@
                 "victimization",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2016-03-01T18:34:56",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2015-08-27T10:17:20",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR36143.v1",
-                    "title": "National Crime Victimization Survey, Concatenated File, 1992-2014"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Organizations Convicted in Federal Criminal Courts, 2016 ",
-            "description": "These data, collected to assist in the development of sentencing guidelines, describe offense and sentencing characteristics for organizations sentenced in federal district courts in 2016. The United States Sentencing Commission's primary function is to inform federal courts of sentencing policies and practices that include guidelines prescribing the appropriate form and severity of punishment for offenders convicted of federal crimes. Court-related variables include primary offense type, pecuniary offense loss and gain, dates of disposition and sentencing, method of determination of guilt, number of counts pled and charged, and dates and types of sentencing and restitution. Defendant organization variables include ownership structure, number of owners and employees, highest level of corporate knowledge of the criminal offense, highest level of corporate indictment and conviction for participation in the criminal offense, annual revenue, equity and financial status, whether it was a criminal organization, duration of criminal activity, and risk to national security. Organizational defendants data, 2016, covers fiscal year October 1, 2015, through September 30, 2016.",
-            "modified": "2018-06-06T08:43:26",
-            "accessLevel": "public",
-            "identifier": "2015",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Victimization Survey, Concatenated File, 1992-2014"
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
+            "description": "These data, collected to assist in the development of sentencing guidelines, describe offense and sentencing characteristics for organizations sentenced in federal district courts in 2016. The United States Sentencing Commission's primary function is to inform federal courts of sentencing policies and practices that include guidelines prescribing the appropriate form and severity of punishment for offenders convicted of federal crimes. Court-related variables include primary offense type, pecuniary offense loss and gain, dates of disposition and sentencing, method of determination of guilt, number of counts pled and charged, and dates and types of sentencing and restitution. Defendant organization variables include ownership structure, number of owners and employees, highest level of corporate knowledge of the criminal offense, highest level of corporate indictment and conviction for participation in the criminal offense, annual revenue, equity and financial status, whether it was a criminal organization, duration of criminal activity, and risk to national security. Organizational defendants data, 2016, covers fiscal year October 1, 2015, through September 30, 2016.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR36980.v1",
+                    "title": "Organizations Convicted in Federal Criminal Courts, 2016 "
+                }
+            ],
+            "identifier": "2015",
+            "isPartOf": "2427",
+            "issued": "2018-06-06T08:43:26",
             "keyword": [
                 "convictions (law)",
                 "corporate crime",
@@ -39208,54 +39202,54 @@
                 "sentencing",
                 "sentencing guidelines"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2018-06-06T08:43:26",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2427",
-            "dataQuality": false,
-            "issued": "2018-06-06T08:43:26",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR36980.v1",
-                    "title": "Organizations Convicted in Federal Criminal Courts, 2016 "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Victimization Survey, [United States], 2017",
-            "description": "The National Crime Victimization Survey (NCVS) Series, previously called the National Crime Surveys (NCS), has been collecting data on personal and household victimization through an ongoing survey of a nationally-representative sample of residential addresses since 1973. The NCVS was designed with four primary objectives: (1) to develop detailed information about the victims and consequences of crime, (2) to estimate the number and types of crimes not reported to the police, (3) to provide uniform measures of selected types of crimes, and (4) to permit comparisons over time and types of areas. The survey categorizes crimes as \"personal\" or \"property.\" Personal crimes include rape and sexual attack, robbery, aggravated and simple assault, and purse-snatching/pocket-picking, while property crimes include burglary, theft, motor vehicle theft, and vandalism. Each respondent is asked a series of screen questions designed to determine whether she or he was victimized during the six-month period preceding the first day of the month of the interview. A \"household respondent\" is also asked to report on crimes against the household as a whole (e.g., burglary, motor vehicle theft). The data include type of crime, month, time, and location of the crime, relationship between victim and offender, characteristics of the offender, self-protective actions taken by the victim during the incident and results of those actions, consequences of the victimization, type of property lost, whether the crime was reported to police and reasons for reporting or not reporting, and offender use of weapons, drugs, and alcohol. Basic demographic information such as age, race, gender, and income is also collected, to enable analysis of crime by various subpopulations. This version of the NCVS, referred to as the collection year, contains records from interviews conducted in the 12 months of the given year.",
-            "modified": "2020-03-23T15:10:33",
-            "accessLevel": "public",
-            "identifier": "2016",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "Organizations Convicted in Federal Criminal Courts, 2016 "
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
+                    "accessURL": "https://doi.org/10.3886/ICPSR36981.v2",
+                    "title": "National Crime Victimization Survey, [United States], 2017"
+                }
+            ],
+            "identifier": "2016",
+            "isPartOf": "2432",
+            "issued": "2019-11-11T08:25:23",
             "keyword": [
                 "assault",
                 "auto theft",
@@ -39274,54 +39268,54 @@
                 "vandalism",
                 "victimization"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2020-03-23T15:10:33",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2019-11-11T08:25:23",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR36981.v2",
-                    "title": "National Crime Victimization Survey, [United States], 2017"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Crime Victimization Survey: School Crime Supplement, [United States], 2017",
-            "description": "The primary purpose of the School Crime Supplement (SCS) is to obtain additional information about school-related victimizations so that policymakers; academic researchers; practitioners at the federal, state, and local levels; and special interest groups who are concerned with crime in schools can make informed decisions concerning policies and programs. The SCS asks questions related to students' experiences with, and perceptions of crime and safety at school, including preventive measures employed by schools; students' participation in after school activities; students' perception of school rules and enforcement of these rules; the presence of weapons, drugs, alcohol, and gangs in school; student bullying; hate-related incidents; and attitudinal questions relating to the fear of victimization at school. These responses are linked to the National Crime Victimization Survey (NCVS) survey instrument responses for a more complete understanding of the individual student's circumstances.",
-            "modified": "2020-02-27T10:17:40",
-            "accessLevel": "public",
-            "identifier": "2017",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Victimization Survey, [United States], 2017"
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
+            "description": "The primary purpose of the School Crime Supplement (SCS) is to obtain additional information about school-related victimizations so that policymakers; academic researchers; practitioners at the federal, state, and local levels; and special interest groups who are concerned with crime in schools can make informed decisions concerning policies and programs. The SCS asks questions related to students' experiences with, and perceptions of crime and safety at school, including preventive measures employed by schools; students' participation in after school activities; students' perception of school rules and enforcement of these rules; the presence of weapons, drugs, alcohol, and gangs in school; student bullying; hate-related incidents; and attitudinal questions relating to the fear of victimization at school. These responses are linked to the National Crime Victimization Survey (NCVS) survey instrument responses for a more complete understanding of the individual student's circumstances.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR36982.v1",
+                    "title": "National Crime Victimization Survey: School Crime Supplement, [United States], 2017"
+                }
+            ],
+            "identifier": "2017",
+            "isPartOf": "2432",
+            "issued": "2020-02-27T10:17:40",
             "keyword": [
                 "crime",
                 "crime in schools",
@@ -39345,54 +39339,54 @@
                 "victimization",
                 "victims"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2020-02-27T10:17:40",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2432",
-            "dataQuality": false,
-            "issued": "2020-02-27T10:17:40",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR36982.v1",
-                    "title": "National Crime Victimization Survey: School Crime Supplement, [United States], 2017"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Prisoner Statistics, 1978-2016",
-            "description": "The National Prisoner Statistics (NPS) data collection began in 1926 in response to a congressional mandate to gather information on persons incarcerated in state and federal prisons. Originally under the auspices of the United States Census Bureau, the collection moved to the Bureau of Prisons in 1950, and then in 1971 to the National Criminal Justice Information and Statistics Service, the precursor to the Bureau of Justice Statistics (BJS) which was established in 1979. Since 1979, the Census Bureau has been the NPS data collection agent. The NPS is administered to 51 respondents. Before 2001, the District of Columbia was also a respondent, but responsibility for housing the District of Columbia's sentenced prisoners was transferred to the federal Bureau of Prisons, and by yearend 2001 the District of Columbia no longer operated a prison system. The NPS provides an enumeration of persons in state and federal prisons and collects data on key characteristics of the nation's prison population. NPS has been adapted over time to keep pace with the changing information needs of the public, researchers, and federal, state, and local governments.",
-            "modified": "2018-09-14T09:37:29",
-            "accessLevel": "public",
-            "identifier": "2018",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Crime Victimization Survey: School Crime Supplement, [United States], 2017"
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
+            "description": "The National Prisoner Statistics (NPS) data collection began in 1926 in response to a congressional mandate to gather information on persons incarcerated in state and federal prisons. Originally under the auspices of the United States Census Bureau, the collection moved to the Bureau of Prisons in 1950, and then in 1971 to the National Criminal Justice Information and Statistics Service, the precursor to the Bureau of Justice Statistics (BJS) which was established in 1979. Since 1979, the Census Bureau has been the NPS data collection agent. The NPS is administered to 51 respondents. Before 2001, the District of Columbia was also a respondent, but responsibility for housing the District of Columbia's sentenced prisoners was transferred to the federal Bureau of Prisons, and by yearend 2001 the District of Columbia no longer operated a prison system. The NPS provides an enumeration of persons in state and federal prisons and collects data on key characteristics of the nation's prison population. NPS has been adapted over time to keep pace with the changing information needs of the public, researchers, and federal, state, and local governments.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR37003.v1",
+                    "title": "National Prisoner Statistics, 1978-2016"
+                }
+            ],
+            "identifier": "2018",
+            "isPartOf": "2633",
+            "issued": "2018-09-14T09:37:29",
             "keyword": [
                 "HIV",
                 "correctional system",
@@ -39402,54 +39396,54 @@
                 "prison inmates",
                 "state correctional facilities"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2018-09-14T09:37:29",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2633",
-            "dataQuality": false,
-            "issued": "2018-09-14T09:37:29",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR37003.v1",
-                    "title": "National Prisoner Statistics, 1978-2016"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Survey of Jails in Indian Country, 2015",
-            "description": "The purpose of the Survey of Jails in Indian Country is an enumeration of all known adult and juvenile facilities -- jails, confinement facilities, detention centers, and other correctional facilities operated by tribal authorities or the Bureau of Indian Affairs (BIA), United States Department of the Interior. For the purpose of this collection, Indian country includes reservations, pueblos, rancherias, and other Native American and Alaska Native communities throughout the United States. The survey collects data on the number of adults and juveniles held on the last weekday in June 2015, type of offense, average daily population in June, most crowded day in June, admissions and releases in June, number of inmate deaths and suicide attempts, rated capacity, and jail staffing.",
-            "modified": "2021-11-22T17:16:44",
-            "accessLevel": "restricted public",
-            "identifier": "2019",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
-                        "id": 10,
                         "acronym": "DOJ",
+                        "id": 10,
                         "name": "Department of Justice"
+                    },
+                    "parentOrganizationID": 10
                 }
-                }
             },
+            "title": "National Prisoner Statistics, 1978-2016"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The purpose of the Survey of Jails in Indian Country is an enumeration of all known adult and juvenile facilities -- jails, confinement facilities, detention centers, and other correctional facilities operated by tribal authorities or the Bureau of Indian Affairs (BIA), United States Department of the Interior. For the purpose of this collection, Indian country includes reservations, pueblos, rancherias, and other Native American and Alaska Native communities throughout the United States. The survey collects data on the number of adults and juveniles held on the last weekday in June 2015, type of offense, average daily population in June, most crowded day in June, admissions and releases in June, number of inmate deaths and suicide attempts, rated capacity, and jail staffing.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR37005.v2",
+                    "title": "Annual Survey of Jails in Indian Country, 2015"
+                }
+            ],
+            "identifier": "2019",
+            "isPartOf": "2435",
+            "issued": "2018-05-23T11:04:12",
             "keyword": [
                 "Alaskan Natives",
                 "Native Americans",
@@ -39460,55 +39454,55 @@
                 "jails",
                 "population characteristics"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-11-22T17:16:44",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2435",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2018-05-23T11:04:12",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR37005.v2",
-                    "title": "Annual Survey of Jails in Indian Country, 2015"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Survey of Jails in Indian Country, 2016",
-            "description": "The purpose of the Survey of Jails in Indian Country is an enumeration of all known adult and juvenile facilities -- jails, confinement facilities,\r\ndetention centers, and other correctional facilities operated by tribal authorities or the Bureau of Indian Affairs (BIA), U.S. Department of\r\nthe Interior. For the purpose of this collection, Indian country includes reservations, pueblos, rancherias, and other Native American and\r\nAlaska Native communities throughout the United States. The survey collects data on the number of adults and juveniles held on the last\r\nweekday in June 2016, type of offense, average daily population in June, most crowded day in June, admissions and releases in June,\r\nnumber of inmate deaths and suicide attempts, rated capacity, and jail staffing.",
-            "modified": "2021-11-22T17:06:49",
-            "accessLevel": "restricted public",
-            "identifier": "2020",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Annual Survey of Jails in Indian Country, 2015"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The purpose of the Survey of Jails in Indian Country is an enumeration of all known adult and juvenile facilities -- jails, confinement facilities,\r\ndetention centers, and other correctional facilities operated by tribal authorities or the Bureau of Indian Affairs (BIA), U.S. Department of\r\nthe Interior. For the purpose of this collection, Indian country includes reservations, pueblos, rancherias, and other Native American and\r\nAlaska Native communities throughout the United States. The survey collects data on the number of adults and juveniles held on the last\r\nweekday in June 2016, type of offense, average daily population in June, most crowded day in June, admissions and releases in June,\r\nnumber of inmate deaths and suicide attempts, rated capacity, and jail staffing.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR37006.v2",
+                    "title": "Annual Survey of Jails in Indian Country, 2016"
+                }
+            ],
+            "identifier": "2020",
+            "isPartOf": "2435",
+            "issued": "2018-05-23T12:32:47",
             "keyword": [
                 "Alaskan Natives",
                 "Native Americans",
@@ -39519,55 +39513,55 @@
                 "jails",
                 "population characteristics"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2021-11-22T17:06:49",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2435",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2018-05-23T12:32:47",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR37006.v2",
-                    "title": "Annual Survey of Jails in Indian Country, 2016"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Corrections Reporting Program, [United States], 2000-2016",
-            "description": "The National Corrections Reporting Program (NCRP) compiles offender-level data on admissions and releases from state and federal prisons and post-confinement community supervision. The data are used to monitor the nation's correctional population and address specific policy questions related to recidivism, prisoner reentry, and trends in demographic characteristics of the incarcerated and community supervision populations. The Bureau of Justice Statistics (BJS) has administered the NCRP since 1983. Abt Associates has served as the NCRP data collection agent since October 2010.",
-            "modified": "2019-03-21T14:52:25",
-            "accessLevel": "restricted public",
-            "identifier": "2021",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "Annual Survey of Jails in Indian Country, 2016"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Corrections Reporting Program (NCRP) compiles offender-level data on admissions and releases from state and federal prisons and post-confinement community supervision. The data are used to monitor the nation's correctional population and address specific policy questions related to recidivism, prisoner reentry, and trends in demographic characteristics of the incarcerated and community supervision populations. The Bureau of Justice Statistics (BJS) has administered the NCRP since 1983. Abt Associates has served as the NCRP data collection agent since October 2010.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR37007.v1",
+                    "title": "National Corrections Reporting Program, [United States], 2000-2016"
+                }
+            ],
+            "identifier": "2021",
+            "isPartOf": "2589",
+            "issued": "2019-03-21T14:48:35",
             "keyword": [
                 "correctional facilities",
                 "correctional facilities (juveniles)",
@@ -39584,55 +39578,55 @@
                 "probation",
                 "state correctional facilities"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2019-03-21T14:52:25",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2589",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2019-03-21T14:48:35",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR37007.v1",
-                    "title": "National Corrections Reporting Program, [United States], 2000-2016"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Inmate Survey (NIS) - Jails: Full Survey Respondents, [United States], 2007",
-            "description": "The National Inmate Survey (NIS) is part of the Bureau of Justice Statistics' (BJS) National Prison Rape Statistics Program, which gathers mandated data on the incidence and prevalence of sexual assault in correctional facilities under the Prison Rape Elimination Act of 2003 (PREA; P.L. 108- 79). Inmates are randomly assigned to receive either a survey of sexual victimization or a survey of mental and physical health, past drug and alcohol use, and treatment for substance abuse. About 88 percent of the respondents completed modules through the survey of sexual victimization while the other 12 percent completed modules through the alternative survey. However, the data in this study focuses solely upon substance use and treatment. No respondent answered questions about sexual victimization.\r\nThe same 37,0888 respondents who are in this data are also part of the 79,973 respondents from the study National Inmate Survey (NIS) - Jails: Full Survey Respondents, [United States], 2007-2009 (ICPSR 37011).",
-            "modified": "2018-09-10T10:30:31",
-            "accessLevel": "restricted public",
-            "identifier": "2022",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "National Corrections Reporting Program, [United States], 2000-2016"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Inmate Survey (NIS) is part of the Bureau of Justice Statistics' (BJS) National Prison Rape Statistics Program, which gathers mandated data on the incidence and prevalence of sexual assault in correctional facilities under the Prison Rape Elimination Act of 2003 (PREA; P.L. 108- 79). Inmates are randomly assigned to receive either a survey of sexual victimization or a survey of mental and physical health, past drug and alcohol use, and treatment for substance abuse. About 88 percent of the respondents completed modules through the survey of sexual victimization while the other 12 percent completed modules through the alternative survey. However, the data in this study focuses solely upon substance use and treatment. No respondent answered questions about sexual victimization.\r\nThe same 37,0888 respondents who are in this data are also part of the 79,973 respondents from the study National Inmate Survey (NIS) - Jails: Full Survey Respondents, [United States], 2007-2009 (ICPSR 37011).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR37009.v1",
+                    "title": "National Inmate Survey (NIS) - Jails: Full Survey Respondents, [United States], 2007"
+                }
+            ],
+            "identifier": "2022",
+            "isPartOf": "2442",
+            "issued": "2018-09-10T10:28:29",
             "keyword": [
                 "alcohol abuse",
                 "correctional facilities",
@@ -39646,55 +39640,55 @@
                 "sexual preference",
                 "substance abuse treatment"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2018-09-10T10:30:31",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2442",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2018-09-10T10:28:29",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR37009.v1",
-                    "title": "National Inmate Survey (NIS) - Jails: Full Survey Respondents, [United States], 2007"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Inmate Survey (NIS) - Jails: Alternative Survey Respondents Only, [United States], 2007-2009 ",
-            "description": "The National Inmate Survey (NIS) is part of the Bureau of Justice Statistics' (BJS) National Prison Rape Statistics Program, which gathers mandated data on the incidence and prevalence of sexual assault in correctional facilities under the Prison Rape Elimination Act of 2003 (PREA; P.L. 108- 79). Inmates are randomly assigned to receive either a survey of sexual victimization or a survey of mental and physical health, past drug and alcohol use, and treatment for substance abuse. The data in this study focuses solely upon substance use and treatment from the \"alternative\" version of the survey.\r\nThese 6,577 respondents contained in this file who completed the \"alternative\" survey are the same 6,577 alternative respondents from the study National Inmate Survey (NIS) - Jails: Full Survey Respondents, [United States], 2007-2009 (ICPSR 37011).",
-            "modified": "2019-12-19T12:11:15",
-            "accessLevel": "restricted public",
-            "identifier": "2023",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "National Inmate Survey (NIS) - Jails: Full Survey Respondents, [United States], 2007"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Inmate Survey (NIS) is part of the Bureau of Justice Statistics' (BJS) National Prison Rape Statistics Program, which gathers mandated data on the incidence and prevalence of sexual assault in correctional facilities under the Prison Rape Elimination Act of 2003 (PREA; P.L. 108- 79). Inmates are randomly assigned to receive either a survey of sexual victimization or a survey of mental and physical health, past drug and alcohol use, and treatment for substance abuse. The data in this study focuses solely upon substance use and treatment from the \"alternative\" version of the survey.\r\nThese 6,577 respondents contained in this file who completed the \"alternative\" survey are the same 6,577 alternative respondents from the study National Inmate Survey (NIS) - Jails: Full Survey Respondents, [United States], 2007-2009 (ICPSR 37011).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR37010.v1",
+                    "title": "National Inmate Survey (NIS) - Jails: Alternative Survey Respondents Only, [United States], 2007-2009 "
+                }
+            ],
+            "identifier": "2023",
+            "isPartOf": "2442",
+            "issued": "2019-12-19T12:06:56",
             "keyword": [
                 "alcohol abuse",
                 "correctional facilities",
@@ -39708,55 +39702,55 @@
                 "sexual preference",
                 "substance abuse treatment"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2019-12-19T12:11:15",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2442",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2019-12-19T12:06:56",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR37010.v1",
-                    "title": "National Inmate Survey (NIS) - Jails: Alternative Survey Respondents Only, [United States], 2007-2009 "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Inmate Survey (NIS) - Jails: Full Survey Respondents, [United States], 2007-2009 ",
-            "description": "The National Inmate Survey (NIS) is part of the Bureau of Justice Statistics' (BJS) National Prison Rape Statistics Program, which gathers mandated data on the incidence and prevalence of sexual assault in correctional facilities under the Prison Rape Elimination Act of 2003 (PREA; P.L. 108- 79). Inmates are randomly assigned to receive either a survey of sexual victimization or a survey of mental and physical health, past drug and alcohol use, and treatment for substance abuse. About 92 percent of the respondents completed modules through the survey of sexual victimization while the other eight percent completed modules through the alternative survey. However, the data in this study focuses solely upon substance use and treatment. No respondent answered questions about sexual victimization.\r\nThe same eight percent of respondents (n=6,577) who completed the alternative survey are the same 6,577 respondents from the study National Inmate Survey (NIS) - Jails: Alternative Survey Respondents Only, [United States], 2007-2009 (ICPSR 37010).",
-            "modified": "2018-09-10T10:35:33",
-            "accessLevel": "restricted public",
-            "identifier": "2024",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "National Inmate Survey (NIS) - Jails: Alternative Survey Respondents Only, [United States], 2007-2009 "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Inmate Survey (NIS) is part of the Bureau of Justice Statistics' (BJS) National Prison Rape Statistics Program, which gathers mandated data on the incidence and prevalence of sexual assault in correctional facilities under the Prison Rape Elimination Act of 2003 (PREA; P.L. 108- 79). Inmates are randomly assigned to receive either a survey of sexual victimization or a survey of mental and physical health, past drug and alcohol use, and treatment for substance abuse. About 92 percent of the respondents completed modules through the survey of sexual victimization while the other eight percent completed modules through the alternative survey. However, the data in this study focuses solely upon substance use and treatment. No respondent answered questions about sexual victimization.\r\nThe same eight percent of respondents (n=6,577) who completed the alternative survey are the same 6,577 respondents from the study National Inmate Survey (NIS) - Jails: Alternative Survey Respondents Only, [United States], 2007-2009 (ICPSR 37010).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR37011.v1",
+                    "title": "National Inmate Survey (NIS) - Jails: Full Survey Respondents, [United States], 2007-2009 "
+                }
+            ],
+            "identifier": "2024",
+            "isPartOf": "2442",
+            "issued": "2018-09-10T10:33:38",
             "keyword": [
                 "alcohol abuse",
                 "correctional facilities",
@@ -39770,55 +39764,55 @@
                 "sexual preference",
                 "substance abuse treatment"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2018-09-10T10:35:33",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2442",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2018-09-10T10:33:38",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR37011.v1",
-                    "title": "National Inmate Survey (NIS) - Jails: Full Survey Respondents, [United States], 2007-2009 "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Inmate Survey (NIS) - Jails: Full Survey Respondents, [United States], 2008-2009 ",
-            "description": "The National Inmate Survey (NIS) is part of the Bureau of Justice Statistics' (BJS) National Prison Rape Statistics Program, which gathers mandated data on the incidence and prevalence of sexual assault in correctional facilities under the Prison Rape Elimination Act of 2003 (PREA; P.L. 108- 79). Inmates are randomly assigned to receive either a survey of sexual victimization or a survey of mental and physical health, past drug and alcohol use, and treatment for substance abuse. About 95 percent of the respondents completed modules through the survey of sexual victimization while the other five percent completed modules through the alternative survey. However, the data in this study focuses solely upon substance use and treatment. No respondent answered questions about sexual victimization.\r\nThe same 42,885 respondents who are in this data are also part of the 79,973 respondents from the study National Inmate Survey (NIS) - Jails: Full Survey Respondents, [United States], 2007-2009 (ICPSR 37011).",
-            "modified": "2018-09-10T10:40:55",
-            "accessLevel": "restricted public",
-            "identifier": "2025",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "National Inmate Survey (NIS) - Jails: Full Survey Respondents, [United States], 2007-2009 "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Inmate Survey (NIS) is part of the Bureau of Justice Statistics' (BJS) National Prison Rape Statistics Program, which gathers mandated data on the incidence and prevalence of sexual assault in correctional facilities under the Prison Rape Elimination Act of 2003 (PREA; P.L. 108- 79). Inmates are randomly assigned to receive either a survey of sexual victimization or a survey of mental and physical health, past drug and alcohol use, and treatment for substance abuse. About 95 percent of the respondents completed modules through the survey of sexual victimization while the other five percent completed modules through the alternative survey. However, the data in this study focuses solely upon substance use and treatment. No respondent answered questions about sexual victimization.\r\nThe same 42,885 respondents who are in this data are also part of the 79,973 respondents from the study National Inmate Survey (NIS) - Jails: Full Survey Respondents, [United States], 2007-2009 (ICPSR 37011).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR37012.v1",
+                    "title": "National Inmate Survey (NIS) - Jails: Full Survey Respondents, [United States], 2008-2009 "
+                }
+            ],
+            "identifier": "2025",
+            "isPartOf": "2442",
+            "issued": "2018-09-10T10:39:23",
             "keyword": [
                 "alcohol abuse",
                 "correctional facilities",
@@ -39832,55 +39826,55 @@
                 "sexual preference",
                 "substance abuse treatment"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2018-09-10T10:40:55",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2442",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2018-09-10T10:39:23",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR37012.v1",
-                    "title": "National Inmate Survey (NIS) - Jails: Full Survey Respondents, [United States], 2008-2009 "
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Inmate Survey (NIS) - Jails: Alternative Survey Respondents Only, [United States], 2011-2012",
-            "description": "The National Inmate Survey (NIS) is part of the Bureau of Justice Statistics' (BJS) National Prison Rape Statistics Program, which gathers mandated data on the incidence and prevalence of sexual assault in correctional facilities under the Prison Rape Elimination Act of 2003 (PREA; P.L. 108- 79). Inmates are randomly assigned to receive either a survey of sexual victimization or a survey of criminal history, facility climate, and mental health. About 90 percent of the respondents completed modules through the survey of sexual victimization while the other 10 percent completed modules through the alternative survey. However, the data in this study focuses primarily upon criminal history, facility climate, and mental health. No respondent answered questions about sexual victimization.",
-            "modified": "2019-12-19T12:00:27",
-            "accessLevel": "restricted public",
-            "identifier": "2026",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "National Inmate Survey (NIS) - Jails: Full Survey Respondents, [United States], 2008-2009 "
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "011:21"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ask BJS Bureau of Justice Statistics (USDOJ)",
                 "hasEmail": "mailto:askbjs@usdoj.gov"
             },
+            "dataQuality": false,
+            "description": "The National Inmate Survey (NIS) is part of the Bureau of Justice Statistics' (BJS) National Prison Rape Statistics Program, which gathers mandated data on the incidence and prevalence of sexual assault in correctional facilities under the Prison Rape Elimination Act of 2003 (PREA; P.L. 108- 79). Inmates are randomly assigned to receive either a survey of sexual victimization or a survey of criminal history, facility climate, and mental health. About 90 percent of the respondents completed modules through the survey of sexual victimization while the other 10 percent completed modules through the alternative survey. However, the data in this study focuses primarily upon criminal history, facility climate, and mental health. No respondent answered questions about sexual victimization.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://doi.org/10.3886/ICPSR37013.v1",
+                    "title": "National Inmate Survey (NIS) - Jails: Alternative Survey Respondents Only, [United States], 2011-2012"
+                }
+            ],
+            "identifier": "2026",
+            "isPartOf": "2442",
+            "issued": "2019-12-19T11:54:38",
             "keyword": [
                 "correctional facilities",
                 "criminal histories",
@@ -39894,55 +39888,55 @@
                 "prescription drugs",
                 "sexual preference"
             ],
-            "bureauCode": [
-                "011:21"
+            "language": [
+                "eng"
             ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "modified": "2019-12-19T12:00:27",
             "programCode": [
                 "011:061"
             ],
-            "license": "http://www.usa.gov/publicdomain/label/1.0/",
-            "isPartOf": "2442",
-            "rights": "These data are restricted due to the increased risk of violation of confidentiality of respondent and subject data.",
-            "dataQuality": false,
-            "issued": "2019-12-19T11:54:38",
-            "language": [
-                "eng"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://doi.org/10.3886/ICPSR37013.v1",
-                    "title": "National Inmate Survey (NIS) - Jails: Alternative Survey Respondents Only, [United States], 2011-2012"
-                }
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Inmate Survey (NIS) - Jails: Full Survey Respondents, [United States], 2011-2012 ",
-            "description": "The National Inmate Survey (NIS) is part of the Bureau of Justice Statistics' (BJS) National Prison Rape Statistics Program, which gathers mandated data on the incidence and prevalence of sexual assault in correctional facilities under the Prison Rape Elimination Act of 2003 (PREA; P.L. 108- 79). Inmates are randomly assigned to receive either a survey of sexual victimization or a survey of criminal history, facility climate, and mental health. About 90 percent of the respondents completed modules through the survey of sexual victimization while the other 10 percent completed modules through the alternative survey. However, the data in this study focuses primarily upon criminal history, facility climate, and mental health. No respondent answered questions about sexual victimization.",
-            "modified": "2018-09-10T10:54:35",
-            "accessLevel": "restricted public",
-            "identifier": "2027",
             "publisher": {
-                "name": "Bureau of Justice Statistics",
                 "@type": "org:Organization",
+                "name": "Bureau of Justice Statistics",
                 "subOrganizationOf": {
-                    "id": 22,
                     "acronym": "OJP",
+                    "id": 22,
                     "name": "Office of Justice Programs",
-                    "parentOrganizationID": 10,
                     "parentOrganization": {
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
+            "title": "National Inmate Survey (NIS) - Jails: Alternative Survey Respondents Only, [United States], 2011-2012"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
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

