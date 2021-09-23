# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 09:44:39 2021

@author: Lenovo
"""

# =============================================================================
#   C
#   https://randomuser.me/documentation
# =============================================================================
import requests

URL = 'https://randomuser.me/api'
PARAMS = {'results': 2}
HEADERS = {'content-type': 'application/json'}

RES = requests.get(URL, headers=HEADERS, params=PARAMS)
MYDATA = RES.json()
# print(mydata['results'])

print(RES.status_code)

for user in MYDATA['results']:
    print(user["name"])
    print(user["gender"])
    print(user["email"])

for k, v in MYDATA['info'].items():
    print(k, v)

print(MYDATA['info'].get('seed'))
