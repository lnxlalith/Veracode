#!/usr/bin/env python
# to inspect dynamic report data from Veracode
# author : Malika

from __future__ import print_function
from requests.auth import HTTPBasicAuth
import requests
import json
import xmltodict
from copy import copy
# from bs4 import BeautifulSoup
# from itertools import chain
# from html.parser import HTMLParser

s = requests.Session()
s.proxies = {"http": "proxy.pfshq.com:3128"}
url = 'https://analysiscenter.veracode.com/api/5.0/detailedreport.do?build_id=2581484'

r = s.get(url, auth=HTTPBasicAuth('malika.mohammed@primerica.com', 'password'))
data = r.content
# print(data)
xml_data = xmltodict.parse(data)
rawdata = (json.dumps(xml_data))
json_obj = json.loads(rawdata)


with open('/Users/a6748/Documents/scandata.json','w') as f:
    f.write(json.dumps(json_obj))
    
# result = []
# path = []


# def get_keys(d, target):
#     for k, v in d.iteritems():
#         path.append(k)
#         if isinstance(v, dict):
#             get_keys(v, target)
#         if v == target:
#             result.append(copy(path))
#             path.pop()


# for key, value in json_obj.items():
#     print(key)
