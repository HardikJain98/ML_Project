# combine-data.py
# Kartik Sastry
# 3/1/2022

# Description:
# Python script to loop through data files in ../dataset/
# and create a master data file, a list of features, a
# matrix characterizing missing data, and a histogram

# Usage:
# python combine-data.py

# Inputs:
# None, but note relative paths to data files

# Outputs:
# - ../dataset/all-trips.csv: containing data from all trips
# - feature-names.txt: containing the names of all features
# - missing-data.csv: indicates
# - histogram.pdf: a nicely styled histogram

################################################
#                 Libraries
################################################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

################################################
#                Concatenate Data
################################################
# Collection of dataframes from each file
dfs = []

# Iterate over all files
filenames = ['../dataset/TripA{:02d}.csv'.format(i) for i in range(1, 32+1)] + ['../dataset/TripB{:02d}.csv'.format(i) for i in range(1, 38+1)]
for filename in filenames:
    # encoding='utf-8', errors='ignore' skips over non-standard characters, e.g. the degree symbol
    with open(filename, encoding='utf-8', errors='ignore') as f:
        df = pd.read_csv(f, delimiter=';')

    # add a feature to each datapoint to indicate which file it came from
    df['trip_id'] = filename.split('/')[-1].split('/')[-1].split('.')[0]

    # add to collection
    dfs.append(df)

# Concatenate all dataframes into one large dataframe
df_concatenated = pd.concat(dfs, axis=0, ignore_index=True)

################################################
#          Save Concatenated Data to CSV
################################################
df_concatenated.to_csv('../dataset/all-trips.csv', index=False)

################################################
#      Generate Text File w/ Feature Names
################################################
# Write the column names to a text file, one per line
with open('feature-names.txt', 'w') as f:
    for col in df_concatenated.columns:
        f.write(col + '\n')

################################################
#   Generate Table to Indicate Missing Data
################################################
# Initialize the results table
results = pd.DataFrame(columns=(['file'] + df_concatenated.columns.to_list()))

# Append the results for each dataframe
filenames = ['TripA{:02d}.csv'.format(i) for i in range(1, 32+1)] + ['TripB{:02d}.csv'.format(i) for i in range(1, 38+1)]
for filename, df in zip(filenames, dfs):
    row = {'file': filename}
    for col in results.columns[1:]:
        if col in df.columns:
            row[col] = 1
        else:
            row[col] = 0
    results = results.append(row, ignore_index=True)
results.to_csv('missing-data.csv', index=False)

################################################
#             Make a Histogram
################################################
# Set Up Plot
plt.rc('text', usetex=True);
plt.rc('font', family='serif');
fig, ax = plt.subplots(1, 1, figsize=(12, 6));

# Plot a histogram of the 'Speed' column for all trips
ax.hist(df_concatenated['Velocity [km/h]'], density=True)
ax.set_xlabel('Velocity [km/h]')
ax.set_ylabel('Density')
ax.set_title('Histogram of Velocity over All Trips')
plt.yscale('linear')

# Show the plot (blocks execution)
plt.show()

# # Save image for LaTeX
fig.savefig('histogram.pdf', format='pdf', bbox_inches='tight');
