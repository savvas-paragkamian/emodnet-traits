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
import json
import csv        
import os
import sys
import re

def flatten_json(nested_json, separator='|'):
    flat_dict = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + separator)
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + separator)
                i += 1
        else:
            flat_dict[name[:-1]] = x

    flatten(nested_json)
    return flat_dict

# Example usage:

#js = 'worms_traits/traits_360492.json'
#with open(js) as json_file:
#	data = json.load(json_file)


directory_path = 'worms_traits/'
print(f'loading all json files from the {directory_path}')

# Define the output TSV file path
output_file = 'output.tsv'
output_directory = 'worms_traits_df/'

# start loading the files
#data_list = []

with open('output.tsv', 'w', newline='') as f_output:
    tsv_output = csv.writer(f_output, delimiter='\t')

    for filename in os.listdir(directory_path):
        if filename.endswith('.json'):
            file_path = os.path.join(directory_path, filename)
    
            # Open and read the JSON file
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
                
                # make the json a flat long list
                flat_dict = flatten_json(data)
                
                for i in flat_dict:
                    name = re.sub("|children|0|","",i)
                    #namea = re.sub("|{2,}", "|",name)
                    name_s = name.replace("|", '', name.count("|") - 1)
                    d = name_s.split("|")
    
                    d.append(flat_dict[i])
                    d.append(filename)
                    tsv_output.writerow(d)
            # Append the data to the list
            #data_list.append(my_list)

print("done")
