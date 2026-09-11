import scipy.spatial as ss
import numpy as np
import matplotlib.pyplot as mp

points=np.array([[2,3],[4,5],[7,8],[6,1]])
simp=ss.Delaunay(points).simplices

mp.triplot(points[:,0],points[:,1],simp)
mp.scatter(points[:,0],points[:,1],color="red")
mp.show()
