# Making a Python request
import requests
import json

# Sample query for device 2004 and trip 12 
url = "https://ipacdev.hondaresearch.com:8443/hackathon/hondadsrc/evtwarn?device=2004"
#url = "https://ipacdev.hondaresearch.com:8443/hackathon/hondadsrc/summary"

headers = {
    'key' : "AC85FK223FNP90AK72",
    'cache-control' : "no-cache"
}

response = requests.request("GET", url, headers=headers)

json_obj = json.loads(response.text)

#print(json.dumps(json_obj, indent=4))

#with open('dev_2004_evtwarn.json', 'w') as outfile:
#    json.dump(json_obj, outfile)

print(json_obj['data'][0]['hvSpeed'])