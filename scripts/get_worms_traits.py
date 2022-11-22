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

l = taxa[222]
aphia_id = l[1]
print(aphia_id)
url = worms_url + aphia_id
aphia_attr = requests.get(url = url)
time.sleep(3)
print(aphia_attr.status_code)
data = aphia_attr.json()
data_j = data #json.loads(data)
print(type(data_j))
print(type(data_j[0]))
print(len(data_j))

jsonFile = open("data.json", "w")
jsonString = json.dumps(data_j)
jsonFile.write(jsonString)
jsonFile.close()
