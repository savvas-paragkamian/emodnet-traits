#!/usr/bin/env python3

###############################################################################
# script name: parse_worms_traits.py
# developed by: Savvas Paragkamian
# framework: EMODnet Biology Phase IV
###############################################################################
# GOAL:
# Aim of this script is parse the json files retrieved from worms traits and 
# create a tsv file with fields : "i", "name","value","depth","filename"
###############################################################################
# usage:./parse_worms_traits.py
###############################################################################
import json
import csv
import os
import sys
import re

# Recurcive Function to flatten the nested json
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

directory_path = 'worms_traits/'
print(f'loading all json files from the {directory_path}')

# Define the output TSV file path
output_directory = 'worms_traits_df/'

# start loading the files
#data_list = []

with open('worms_traits_long.tsv', 'w', newline='') as f_output:
    tsv_output = csv.writer(f_output, delimiter='\t')
    header = ["i", "name","value","depth","filename"]
    tsv_output.writerow(header)

    for filename in os.listdir(directory_path):
        if filename.endswith('.json'):
            file_path = os.path.join(directory_path, filename)
    
            # Open and read the JSON file
            with open(file_path, 'r') as json_file:
                data = json.load(json_file)
                
                # make the json a flat long list
                flat_dict = flatten_json(data)
                
                for i in flat_dict:
                    # count the clildren depth of each entry
                    depth = i.count("children")
                    # remove the children mention
                    name = re.sub("|children|0|","",i)
                    #namea = re.sub("|{2,}", "|",name)
                    name_s = name.replace("|", '', name.count("|") - 1)
                    #make a list of the line
                    d = name_s.split("|")
                    # append the data to the list
                    d.append(flat_dict[i])
                    d.append(depth)
                    d.append(filename)
                    #write the line to the file
                    tsv_output.writerow(d)

print("done")
