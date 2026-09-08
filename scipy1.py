import scipy.optimize as s
import numpy as n

def eqn(x):
    return x+n.cos(x)

myroot=s.root(eqn,0)
print(myroot.x)
