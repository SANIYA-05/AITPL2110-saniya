import numpy as np # we cannot perform multiplication as shapes are not equal
a= np.diag([[1,2,3],[1,6,3],[1,2,8]])
print(a)
print(a.ndim)
b=np.array([[[[1,2],[3,4],[4,5],[6,7]]]])
print(b.ndim)
print(np.dot(a,b))