#!/usr/bin/env python3

###############################################################################
# script name: get_worms_traits.py
# developed by: Savvas Paragkamian
# framework: EMODnet Biology Phase IV
###############################################################################
# GOAL:
# Aim of this script is to retrieve all available attributes from 
# Aphia database (WoRMS) assigned to taxa.
###############################################################################
# usage:./get_worms_traits.py
###############################################################################

import requests, sys, json, time
from random import uniform
from datetime import date


def aphiaid_attr_request(aphia_id):

    worms_url = "https://www.marinespecies.org/rest/AphiaAttributesByAphiaID/"
    url = worms_url + aphia_id
    aphia_attr = requests.get(url = url)
    code = aphia_attr.status_code

    if code == 204:
        print(str(aphia_id) + "\t" + str(code))

    if code == 400:
        print(str(aphia_id) + "\t" + str(code))

    if code == 200:
        print(str(aphia_id) + "\t" + str(code))
        data = aphia_attr.json()
        return(data)

    time.sleep(uniform(2,4))

def write_json_attr(attributes):
    
    # load to json
    newjson = "../worms_traits/" + "traits_" + str(aphia_id) + ".json"
    jsonFile = open(newjson, "w")
    jsonString = json.dumps(attributes)
    jsonFile.write(jsonString)
    jsonFile.close()

### main part of code
taxa = []

with open("../worms/2022-04-01-aphia_ids.tsv") as file:
    for line in file:
        
        l=line.split('\t')
        taxa.append(l)

print("there are " + str(len(taxa)) + " aphia IDS")

## Iterate and make the GET requests to server

for a in taxa:
    aphia_id = a[1]
    
    attributes = aphiaid_attr_request(aphia_id)
    if attributes != None:
        write_json_attr(attributes)

    else:
        continue

