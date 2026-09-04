import numpy as np
x=np.array([1,2,3,4,5])
y=x**2
re=np.gradient(y,x)
print(re)
inte=np.trapezoid(y,x)
print(inte)