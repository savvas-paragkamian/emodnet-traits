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
import pandas as pd
import json
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

js = 'worms_traits/traits_360492.json'
with open(js) as json_file:
	data = json.load(json_file)

flat_dict = flatten_json(data)

df = pd.json_normalize(flat_dict)

for i in flat_dict:
    name = re.sub("children|0|","",i)
    d = name.split("|")
    print(d)
    print(name,"\t",flat_dict[i])

#print(flat_dict)
directory_path = 'worms_traits/'
print(f'loading all json files from the {directory_path}')

sys.exit()
# Define the output TSV file path
output_file = 'output.tsv'
output_directory = 'worms_traits_df/'

# start loading the files
data_list = []

for filename in os.listdir(directory_path):
    if filename.endswith('.json'):
        file_path = os.path.join(directory_path, filename)

        # Open and read the JSON file
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)

        # Append the data to the list
        data_list.append(data)

print(f'the number of files read are : {len(data_list)}')
dataframes = []

for json_obj in data_list:
    df = pd.json_normalize(json_obj, record_path=['children'], meta=['AphiaID', 'AphiaID_Inherited', 'reference', 'qualitystatus', 'measurementType', 'CategoryID', 'source_id', 'measurementValue', 'measurementTypeID'], record_prefix='children.', meta_prefix='meta.')
    dataframes.append(df)

# Concatenate the list of DataFrames into a single DataFrame
combined_df = pd.concat(dataframes, ignore_index=True)

# Write the combined DataFrame to a TSV file

combined_df.to_csv(output_file, sep='\t', index=False)
print(f'Data from the list of DataFrames has been written to {output_file}')

# Write each DataFrame to a separate TSV file


for i, df in enumerate(dataframes):
    output_file = f"{output_directory}output_{i}.tsv"
    df.to_csv(output_file, sep='\t', index=False)
    print(f'DataFrame {i} has been written to {output_file}')



