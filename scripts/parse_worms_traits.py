#!/usr/bin/env python3

###############################################################################
# script name: parse_worms_traits.py
# developed by: Savvas Paragkamian
# framework: EMODnet Biology Phase IV
###############################################################################
# GOAL:
# Aim of this script is parse the json files retrieved from worms traits and 
# create a tsv file
###############################################################################
# usage:./parse_worms_traits.py
###############################################################################

import sys, json, csv
from pandas import json_normalize

filename = "../worms_traits/traits_999827.json"

with open(filename, "r") as json_file:
    trait = json.load(json_file)


with open("output.tsv", "w") as output_file:
    dw = csv.DictWriter(output_file, trait[0].keys(), delimiter='\t')
    dw.writeheader()
    dw.writerows(trait)


df = pd.json_normalize(trait, record_path="children")
df.head()
print(trait[0].get("children"))
print(trait[0].keys())
