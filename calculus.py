import numpy as np
x=np.array([1,2,3])
y=x**2
dy=np.gradient(y,x)
print(dy)