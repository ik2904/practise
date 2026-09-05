import numpy as np
mat=np.array([[1,2,3],[4,5,6],[8,9,2]])
mat1=np.array([[1,2,3],[4,5,6],[8,9,2]])

val,vec=np.linalg.eig(mat)
# print(val,vec)
# print(vec)
# print(val)
# pr=np.kron(mat,mat1)
# print(pr)
z=3+4j
print(z.real+z.imag)
print(z.imag)