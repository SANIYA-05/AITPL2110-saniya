import numpy as np
a=np.array([[[[1,2],[3,4],[5,6],[7,8]]]])
print(a.ndim)
b=np.array([[1,2,7,8],[3,4,5,6]])
print(b.ndim)
c=np.array([[1,2],[5,6]])
d=np.dot(a,b)
print(d)
print(np.dot(d,c)) #col of 1st matrix not equal to row of 2nd matrix
print(np.dot(b,c))