import numpy as np
a=np.array([[[[1,2],[3,4],[5,6],[7,8]]]])
print(a.ndim)
a1=a.transpose()
print(a1)
print(a+a1)
print(a-a1)
print(a*a1)
print(a/a1)