import scipy as sp
import numpy as np

arr=np.arange(10)

sp.io.savemat('arr.mat',{'vec':arr})
matlabdata=sp.io.loadmat('arr.mat')
print(matlabdata)