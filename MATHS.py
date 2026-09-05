import numpy as np
mat=np.array([[1,2,3],[4,5,6],[8,9,2]])

val,vec=np.linalg.eig(mat)
# print(val,vec)
print(vec)
print(val)
