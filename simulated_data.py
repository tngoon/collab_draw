##script to create random dataset with given variables

#load packages
import pandas as pd 
import numpy as np 

###PARAMETERS###
#how many participants
pids = list(range(40))
#list IVs
conditions = ['G','B']
#list DVs
columns = ['condition', 'r1_orig1', 'r1_util1', 'r2_orig1', 'r2_util1', 'avg_orig1', 'avg_util1','r1_orig2', 'r1_util2', 'r2_orig2', 'r2_util2', 'avg_orig2', 'avg_util2']
measures = ['r1_orig1','r1_orig1', 'r1_util1', 'r2_orig1', 'r2_util1','r1_orig2', 'r1_util2', 'r2_orig2', 'r2_util2']

###MAKE THE RANDOM SAMPLE###

#make the empty dataframe w/ participants and DVs as columns
df = pd.DataFrame(index=pids, columns=columns)

#randomize DVs into condition
df['condition'] = np.random.choice(conditions, size=len(df), p=[.50,.50])

#add random numeric values for each DV
for measure in measures:
	df[measure] = np.random.randint(1,4, size=(40,1))

# df['originality1'] = np.random.randint(1,4, size=(40,1))
# df['elaboration'] = np.random.randint(1,4, size=(40,1))
# df['feasibility'] = np.random.randint(1,4, size=(40,1))

print(df)

#export dataframe to csv
df.to_csv('order_sim_data.csv')

