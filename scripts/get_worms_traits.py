#!/usr/bin/env python3

import requests, sys, json, time
from datetime import date

worms_url = "https://www.marinespecies.org/rest/AphiaAttributesByAphiaID/"

taxa = []

with open("../worms/2022-04-01-aphia_ids.tsv") as file:
    for line in file:
        
        l=line.split('\t')
        taxa.append(l)

print("there are " + str(len(taxa)) + " aphia IDS")

for a in taxa:
    aphia_id = a[1]
    url = worms_url + aphia_id
    aphia_attr = requests.get(url = url)
    code = aphia_attr.status_code
    
    time.sleep(3)

    if code == 204:
        print(str(a[0]) + " " + str(aphia_id) + " return code = " + str(code))

    if code == 400:
        print(str(aphia_id) + " return code = " + str(code))

    if code == 200:
        print(str(aphia_id) + " return code = " + str(code))
        data = aphia_attr.json()
        data_j = data #json.loads(data)
        print(type(data_j))
        print(type(data_j[0]))
        print(len(data_j))
        
        # load to json
        newjson = "../worms_traits/" + "traits_" + str(aphia_id) + ".json"
        jsonFile = open(newjson, "w")
        jsonString = json.dumps(data_j)
        jsonFile.write(jsonString)
        jsonFile.close()


