import scipy.optimize as s
import numpy as n

# def eqn(x):
#     return x+n.cos(x)

# myroot=s.root(eqn,0)
# print(myroot.x)

def eqn(x):
    return 3*x+x**2+x+2

mymin = s.minimize(eqn,0,method='BFGS')
print(mymin)