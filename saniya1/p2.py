
import pandas as pd
df=pd.read_csv('test.csv')
#print(df.shape)
#print(df.head())
#print(df.tail())
#print(df[3:6])
#print(df.name)
#print(df['name'])
#print(df.columns)
#print(df[['name','degree']])
#print(df['totalmarks'].max())
#print(df['totalmarks'].min())
#print(df['totalmarks'].describe())# it does all the basic fuctionalities
#print(df['totalmarks'].max())
print(df[df.totalmarks == df.totalmarks.min()])

