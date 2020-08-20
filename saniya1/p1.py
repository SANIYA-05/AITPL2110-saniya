import pandas as pd
student1=[('saniya','001','bca'),('ali','002','mca'),('meena','004','b.tech')]
df=pd.DataFrame(student1,columns=['name','regno','degree'])
print(df)