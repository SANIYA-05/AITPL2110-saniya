import numpy as np
a=np.array([[1,2,3,4],[6,7,8,9]])
print(a)
print(a.shape)
print(a.nbytes)
print(a.dtype)
print(np.full_like(a,7))#replacing all values with 7
b=np.random.randint(1,8,size=(4,2))
print(b)
c=np.random.randint(-4,4,size=(4,2))
print(c)