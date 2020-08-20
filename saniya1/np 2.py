import numpy as np
x=np.array([1,2,3,4,5],ndmin=5) #min dimension
#print(x)
y=np.arange(24)

print(y)
z=y.reshape(2,4,3)# 2 matrices with 4 rows and 3 col
#print(z)
a=y.reshape(1,4,6)
print(a)
#