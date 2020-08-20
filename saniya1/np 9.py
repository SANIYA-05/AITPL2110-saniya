import numpy as np
x=np.array([1,2,3,4,5],dtype='int64')
print(x)
print(x.dtype)
print(x.itemsize)#each item size
print(x.size)# no of elements in list
print(x.size * x.itemsize)
print(x.nbytes) #list size

