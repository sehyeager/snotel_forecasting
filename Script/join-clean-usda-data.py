# This will take all data stored year by year in a folder labeled 'data' and then merge that 
# data into one master dataframe and clean up missing data. The result will be an 'output'
# folder existing of the data from each year with the data dictionary at the top removed so that
# it is easy to import to a dataframe. The folder will also include a complete dataframe of all 
# years included in the 'data' folder that has been cleaned with any missing values addressed.

import os
import pandas as pd
import numpy as np

# Create output folder
try:
    os.mkdir('output')
except:
    pass

# Checks for files in data folder
files = os.listdir('data')
output = os.listdir('output')

# Strips header from NRCS data, outputs the new CSVs into the output folder
for file_name in files:
	with open('data/' + str(file_name), 'r') as file_in:
		data = file_in.read().splitlines(True)
	with open('output/' + str(file_name), 'w') as file_out:
		file_out.writelines(data[77:])

# Adding cleaned year CSVs to list
df_list = []

for i in os.listdir('./output'):
    path = os.path.join("./output", i)
    temp = pd.read_csv(path, index_col=None, header=0) 
    df_list.append(temp)

# Making one large datafram	
df = pd.concat(df_list, axis=0, ignore_index=True)

# Checking for blank columns to drop
if ' ' in df.columns:
	df.drop(columns = ' ', inplace = True)

# The 'YYYMMDD' column needs to be set to a datetime
df['YYYYMMDD'] = pd.to_datetime(df['YYYYMMDD'], format='%Y%m%d')

# Dropping values with no time to work with
df = df.loc[df['YYYYMMDD'].notnull()]

# Changing the names of the columns to be easier to work with
lower_cols = [column.lower() for column in df.columns]
df.columns = lower_cols

# Some data is entered as negative numbers when they should be null values.
# -997 : Data may not provide valid measure of contitions
# -998 : No normal available
# -999 : Missing data

# Replacing the negative values with null values
df.replace(-997.0, np.nan, inplace = True)
df.replace(-998.0, np.nan, inplace = True)
df.replace(-999.0, np.nan, inplace = True)

# Dropping columns full of null values (flag columns) as even the values not already nulled represent an invalid
# measure of contitions according to the data dictionary.
df.drop(columns = ['wteq_amt_pct_med_flag', 'prec_wytd_pct_avg_flag'], inplace = True)

#list of all my features with nulls after dropping those two flag columns and changing all the codes to nulls as well
features_to_fill = ['wteq_amt', 'wteq_med', 'wteq_amt_pct_med', 'prec_wytd_amt', 'prec_wytd_avg', 'prec_wytd_pctavg']

#groups by year, and then fills the nulls with the year's median value
def null_filler(feature):
	"""Fills null values in the dataframe with the yearly median value.

	:param feature: The feature to replace nulls with median.

	:return: The main dataframe with null values replaced by the yearly median for that feature.
	"""
	return df.groupby(by = df.index)[feature].transform(lambda x: x.fillna(x.median()))

#fills the nulls of every feature in my above list
for feature in features_to_fill:
    df[feature] = null_filler(feature)

# Saving final cleaned dataframe as a new csv
df.to_csv('output/data_full.csv', index = False)