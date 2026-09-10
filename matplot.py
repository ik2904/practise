import matplotlib.pyplot as plt
import numpy as np
xaxis=np.array([1,2,4,6,8,10,12,14,15])
yaxis=np.array([2,5,2,5,2,5,2,5,2])

# plt.plot(yaxis)
plt.plot(xaxis,yaxis,marker='D',ls="dotted")


font1 = {'color':'purple','size':15}



plt.xlabel("distance")
plt.ylabel("time")
plt.title("showing distance and time",fontdict=font1,loc='right')
plt.grid(color="red",ls=":",linewidth=1)
plt.show()