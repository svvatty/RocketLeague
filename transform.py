import pandas as pd
import json_normalize

df = pd.read_json('replay.json')

#df was instantiated in load.py
#renumber 'count' column so that each row has unique 'count'
rows = df[df.columns[0]].count()  #number of rows in the dataframe since count() returns a dataframe with count of each columns (series)
#df.iloc[0, 1] = 'yer' #for example this will change the value of the zero row, first column to 'yer'
for i in range(rows):
    df.iloc[i, 0] = i


#drop last column 'next' as there is only one unique value in all 50 rows
df_dropped_last_col = df.drop('next', axis = 1)
print(df_dropped_last_col)
df = df_dropped_last_col

#rename count column to 'id'
df.columns = ['id', 'list']

#now, we want to start exploding/unnesting the columns
normalized_df = pd.json_normalize(df['list'])
normalized_df.iloc[0]