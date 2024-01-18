import pandas as pd
df = pd.read_json('replay.json')
#print(df.to_string())
#print(type(df.loc[0]['list']))  #this returns a dictionary from the list outputted in the first row of dataframe
#dictFromList = print(type(df.loc[0]['list']))  #ensure that this is a dictionary 
dictFromList = df.loc[0]['list']
#print(dictFromList)

#we want to explode the dictionary*****

#dictKeys = dictFromList.keys()
#print(dictKeys)

#print(type(dictFromList['blue']['players']))

#print(df.count())

#new_df = df.dropna()
#print(new_df.count())

df.info()
df.describe  #returns a little from each row
df.dtypes #returns the columns and their data types
df.memory_usage()
df.shape  #returns (50, 3)
df.values
df.keys
