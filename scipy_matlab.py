import scipy as sp
import numpy as np

arr=np.arange(10)

sp.io.savemat('arr.mat',{'vec':arr})
matlabdata=sp.io.loadmat('arr.mat')
print(matlabdata)



# INTERPOLATION 1D=
# EXAMPLE=1
import numpy as np
from scipy.interpolate import interp1d

xs = np.array([1, 2, 3, 4])
ys = np.array([10, 20, 30, 40])

interp_func = interp1d(xs, ys)

print(interp_func(2.5))


# EXAMPLE 2-

from scipy.interpolate import interp1d
import numpy as np

xs = np.arange(10)
ys = 2*xs + 1

interp_func = interp1d(xs, ys)

newarr = interp_func(np.arange(2.1, 3, 0.1))

print(newarr)