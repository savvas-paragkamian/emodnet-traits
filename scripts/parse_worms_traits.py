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

directory_path = 'worms_traits/'
print(f'loading all json files from the {directory_path}')

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
    df = pd.json_normalize(data,
                           record_path=['children'],
                           meta=['AphiaID',
                                 'AphiaID_Inherited',
                                 'reference',
                                 'qualitystatus',
                                 'measurementType',
                                 'CategoryID',
                                 'source_id',
                                 'measurementValue',
                                 'measurementTypeID'])

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



