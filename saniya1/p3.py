import pandas as pd
df=pd.read_csv("test1.csv")
#print(df)
grp=df.groupby('empsal')
for i in grp:
 print(i)
#print(grp.get_group('mech'))
print(grp.max())


