#!/usr/bin/env python3

import requests, sys, json, time
from datetime import date

worms_url = "https://www.marinespecies.org/rest/AphiaAttributesByAphiaID/"

taxa = []

with open("../WoRMS_2022-04-01/taxon.txt") as file:
    for line in file:
        
        columns = []
        l=line.split('\t')
        
        aphia_url=l[26].split('=')
        
        if (len(aphia_url)>1):
            aphia_id=aphia_url[2]
        else:
            aphia_id=l[26]

        columns = [l[5], l[19], aphia_id]
        taxa.append(columns)

l = taxa[222]
aphia_id = l[2]
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
