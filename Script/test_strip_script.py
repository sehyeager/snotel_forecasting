import os
import pandas as pd

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

# Saving sorted dataframe
df.to_csv('output/merged.csv', index = False)