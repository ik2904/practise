import scipy.optimize as s
import numpy as n

# def eqn(x):
#     return x+n.cos(x)

# myroot=s.root(eqn,0)
# print(myroot.x)


# def eqn(x):
#     return 3*x+x**2+x+2

# mymin = s.minimize(eqn,0,method='BFGS')
#print(mymin)

# compressed sparese column
# import scipy.sparse as ss
# arr=n.array([1,0,0,0,0,2,0,0,0,0,3,4,5])
# print(ss.csr_matrix(arr))
# print(ss.csr_matrix(arr).data)
# print(ss.csr_matrix(arr).count_nonzero())
# mat=ss.csr_matrix(arr)
# print(mat.eliminate_zeros())
# print(mat)
# # csr to csc 
# cscc=ss.csr_matrix(arr).tocsc()
# print(cscc)


# SCIPY GRAPHS
import scipy.sparse.csgraph as g
import numpy as n
import scipy.sparse as gg


arr=n.array([


[0,  1,  0,  0],
[1, 0, 0, 0],
[0, 0, 0, 1],
[0, 0, 1, 0]

    ])
gr=gg.csr_matrix(arr)
# gh=g.connected_components(gr)
# print(gh)

# DIJKSTRA ALGO 
print(g.dijkstra(gr, return_predecessors=True, indices=0))