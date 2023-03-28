# combine_data.py
# Kartik Sastry
# 3/1/2022

# Description:
# Python script to loop through data files in ../dataset/
# and create a master data file, a list of features, a
# matrix characterizing missing data, and a histogram

# Usage:
# python combine_data.py

# Inputs:
# - ../dataset/TripA01.csv ... TripA32.csv, TripB01.csv ... TripB38.csv

# Outputs:
# - ../dataset/all_trips.csv: containing data from all trips
# - ../dataset/original_feature_names.txt: containing the names of all features
# - ../dataset/missing_data.csv: characterizes which features are missing in which file

################################################
#                 Libraries
################################################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

################################################
#     Relative Paths to Inputs/Outputs
################################################
paths_to_trip_files = ['../dataset/TripA{:02d}.csv'.format(i) for i in range(1, 32+1)] + ['../dataset/TripB{:02d}.csv'.format(i) for i in range(1, 38+1)]
path_to_all_data = '../dataset/all_trips.csv'
path_to_feature_list = '../dataset/original_feature_names.txt'
path_to_missing_data_matrix = '../dataset/missing_data.csv'

################################################
#         Concatenate Trips Together
################################################
# Collection of dataframes from each trip data file
dfs = []

# Iterate over all files
print('Reading in trip data...')
for filename in paths_to_trip_files:
    # encoding='utf-8', errors='ignore' skips over non-standard characters, e.g. the degree symbol
    with open(filename, encoding='utf-8', errors='ignore') as f:
        df = pd.read_csv(f, delimiter=';')

    # add a feature to each datapoint to indicate which file it came from
    # this feature is a string of the form TripXYY where X = {A, B} and YY is two digits
    df['trip_id'] = filename.split('/')[-1].split('/')[-1].split('.')[0]

    # add to collection
    dfs.append(df)
print('Done reading in data. Concatenating...')

# Concatenate all dataframes into one large dataframe
# rows correspond to observations, columns correspond to features
df_concatenated = pd.concat(dfs, axis=0, ignore_index=True)
print('Concatenated dataset has', df_concatenated.shape[0], 'observations and', df_concatenated.shape[1], 'features.')

################################################
#          Save Concatenated Data to CSV
################################################
print('Saving concatenated dataset to:', path_to_all_data)
df_concatenated.to_csv(path_to_all_data, index=False)

################################################
#      Generate Text File w/ Feature Names
################################################
# Write the column names to a text file, one per line
print('Saving a list of feature names in:', path_to_feature_list)
with open(path_to_feature_list, 'w') as f:
    for col in df_concatenated.columns:
        f.write(col + '\n')

################################################
#   Generate Matrix to Indicate Missing Data
################################################
# The purpose of this table is to show which of the trip data files
# (i.e. TripA01.csv, ..., Trip A32.csv, TripB01.csv, ..., TripB3.csv)
# are missing data. The file contains a matrix, where rows correspond
# to trip data files, and columns correspond to features
# (there are some 50 features, listed in original_feature_names.txt).
# Entry (i, j) = 1 if file i contains feature j, and 0 otherwise.

# Initialize the results matrix
results = pd.DataFrame(columns=(['file'] + df_concatenated.columns.to_list()))

# Concatenate the results for each dataframe
row_labels = ['TripA{:02d}.csv'.format(i) for i in range(1, 32+1)] + ['TripB{:02d}.csv'.format(i) for i in range(1, 38+1)]
dfs_list = []
for filename, df in zip(row_labels, dfs):
    row = {'file': filename}
    for col in results.columns[1:]:
        if col in df.columns:
            row[col] = 1
        else:
            row[col] = 0
    dfs_list.append(pd.DataFrame(row, index=[0]))
results = pd.concat(dfs_list, ignore_index=True)

# Save to file
print('Saving a matrix characterizing missing data in:', path_to_missing_data_matrix)
results.to_csv(path_to_missing_data_matrix, index=False)
