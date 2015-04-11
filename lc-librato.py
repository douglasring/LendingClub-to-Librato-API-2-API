# 4/11/2015 Douglas Ring http://www.douglasring.com
# Simple pull of account data from LendingClub.com API and push to Librato.com to graph data
# ZERO Error Checking

import time
import json
import requests # pip install requests
import urllib3.contrib.pyopenssl   #pip install pyopenssl ndg-httpsclient pyasn1 
import librato # pip install librato-metrics

REQUESTS_CA_BUNDLE = '/usr/share/ca-certificates/mozilla/Go_Daddy_Root_Certificate_Authority_-_G2.crt'   # Today - LC uses Godaddy

librato_key='<librato api key>'
librato_api=librato.connect('email@example.com', librato_key)


urllib3.contrib.pyopenssl.inject_into_urllib3()   #avoid urllib3 security issues  https://urllib3.readthedocs.org/en/latest/security.html
headers = {'Authorization':'<LendingClub API Key>','Accept':'application/json','Content-type':'application/json'}

# If you use this - throw in a Try/Except routine at pull and push
print "Grabbing data from LendingClub"
r = requests.get("https://api.lendingclub.com/api/investor/v1/accounts/<investor account id>/summary", headers=headers, verify=True) 
all_lc_data = r.json()
print "Got data from LendingClub"
time.sleep(10)

for data in all_lc_data:
	print("Posting to Librato: ")+data,all_lc_data[data]
	librato_api.submit(data, all_lc_data[data], description=data)


