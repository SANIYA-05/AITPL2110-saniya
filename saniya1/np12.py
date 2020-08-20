import numpy as np
a=np.array([[1,2,3,4,5,6,7,8],[10,20,30,40,50,60,70,80]])
print(a)
print("shape of a:",a.shape)
print("data type of a ",a.dtype)
print("no of bytes:",a.nbytes)
print(a[1,1])
print(a[1,3])
print(a[0,3])
print(a[0,:])
print(a[1,:])
print(a[:,-2])
print(a[:,4])
print(a[0:6,4])
print(a[1,1:6:2])
a[:,3]=[100,200]
a[:,-1]=[100,200]
print(a)

