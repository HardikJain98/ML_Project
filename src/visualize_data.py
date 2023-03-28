# visualize_data.py
# Kartik Sastry
# 3/10/2022

# Description:
# Python script to perform some basic visualization of the reduced dataset

# Usage:
# python combine_data.py
# python preprocess_data.py
# python visualize_data.py

# Inputs:
# - ../dataset/all_trips_reduced.csv: generated by preprocess_data.py

# Outputs:
# - Trip Data Visualizations
#   - ../figs/TripB01.pdf
#   - ../figs/TripB02.pdf
# - Correlation Visualizations
#   - ../figs/feature-correlation-matrix.pdf
#   - ../figs/feature-correlation-with-temp.pdf
#   - ../figs/pairplot.pdf

################################################
#                 Libraries
################################################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

################################################
#     Relative Paths to Inputs/Outputs
################################################
path_to_all_data_reduced = '../dataset/all_trips_reduced.csv'
path_to_figs_dir = '../figs/'

################################################
#         Read In Reduced Data Record
################################################
# encoding='utf-8', errors='ignore' skips over non-standard characters, e.g. the degree symbol
with open(path_to_all_data_reduced, encoding='utf-8', errors='ignore') as f:
    df = pd.read_csv(f, delimiter=',')

################################################
#         Visualize Trip Data
################################################
# one normal trip, one outlier
for trip in ['TripB01', 'TripB02']:
    df_trip = df[df['trip_id']==trip]

    # create figure and axes objects
    fig, axs = plt.subplots(nrows=2, ncols=1, figsize=(8, 8))

    # plot battery current and SoC on shared axis
    axs[0].plot(df_trip['Time [s]'], df_trip['Battery Current [A]'], color='blue')
    axs0_2 = axs[0].twinx()
    axs0_2.plot(df_trip['Time [s]'], df_trip['SoC [%]'], color='red')
    axs[0].set_xlabel('Time [s]')
    axs[0].set_ylabel('Battery Current [A]', color='blue')
    axs0_2.set_ylabel('SoC [%]', color='red')

    # plot ambient and battery temperature on shared axis
    axs[1].plot(df_trip['Time [s]'], df_trip['Ambient Temperature [C]'], color='blue')
    axs1_2 = axs[1].twinx()
    axs1_2.plot(df_trip['Time [s]'], df_trip['Battery Temperature [C]'], color='red')
    axs[1].set_xlabel('Time [s]')
    axs[1].set_ylabel('Ambient Temperature [C]', color='blue')
    axs1_2.set_ylabel('Battery Temperature [C]', color='red')

    fig.suptitle('Selected Features vs. Time for ' + trip + '.csv', fontsize=16)
    plt.savefig(path_to_figs_dir + trip + '.pdf' , format='pdf', bbox_inches='tight')

################################################
#         Correlation Visualizations
################################################
# Pearson correlation between features (including target)
print('Computing feature correlation matrix...')
plt.figure(figsize=(8, 8))
mask = np.triu(np.ones_like(df.corr(method='pearson', numeric_only=True), dtype=bool))
sns_plot1 = sns.heatmap(df.corr(method='pearson', numeric_only=True), mask=mask, vmin=-1, vmax=1, annot=False, cmap='BrBG', cbar_kws={'label': 'Pearson correlation'})
sns_plot1.set_title('Pairwise Pearson Correlation Matrix', fontdict={'fontsize':12}, pad=16);
# plt.show() # blocks execution
sns_plot1.figure.savefig(path_to_figs_dir + 'feature-correlation-matrix.pdf', format='pdf', bbox_inches='tight')

# Pearson correlation between features and target, sorted
print('Computing correlation of features with battery temperature...')
df.corr(method='pearson', numeric_only=True)[['Battery Temperature [C]']].sort_values(by='Battery Temperature [C]', ascending=False)
plt.figure(figsize=(8, 8))
sns_plot2 = sns.heatmap(df.corr(method='pearson', numeric_only=True)[['Battery Temperature [C]']].sort_values(by='Battery Temperature [C]', ascending=False), vmin=-1, vmax=1, annot=True, cmap='BrBG', cbar_kws={'label': 'Pearson correlation'})
sns_plot2.set_title('Pearson Correlation of Features with Battery Temperature', fontdict={'fontsize':12}, pad=16);
# plt.show() # blocks execution
sns_plot2.figure.savefig(path_to_figs_dir + 'feature-correlation-with-temp.pdf', format='pdf', bbox_inches='tight')

# Pair plot to reveal nonlinear relationships
# Sample a subset to keep the plotting tractable
print('Creating a pair plot ...')
df2 = df.sample(200000).drop(columns=['trip_id'], inplace=False)
sns_plot3 = sns.pairplot(df2, diag_kind='kde')
# plt.show() # blocks execution
sns_plot3.figure.savefig(path_to_figs_dir + 'pairplot.png', format='png', bbox_inches='tight')

