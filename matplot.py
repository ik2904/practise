import matplotlib.pyplot as plt
import numpy as np
# xaxis=np.array([1,2,4,6,8,10,12,14,15])
# yaxis=np.array([2,5,2,5,2,5,2,5,2])

# plt.plot(yaxis)
# plt.plot(xaxis,yaxis,marker='D',ls="dotted")


font1 = {'color':'purple','size':15}



# plt.xlabel("distance")
# plt.ylabel("time")

x=np.array([1,2,4,6,8,10,12,14,15])
y=np.array([2,5,2,5,2,5,2,5,2])
plt.subplot(2,1,1)
plt.plot(x,y)
plt.title("this is plot 1 ")
x=np.array([1,2,4,6,8,10,12,14,15])
y=np.array([2,5,2,5,2,5,2,5,2])
plt.subplot(2,1,2)
plt.plot(x,y)
plt.title("this is plot 2",loc='right')
plt.suptitle("this is two plot")



# plt.title("showing distance and time",fontdict=font1,loc='right')
# plt.grid(color="red",ls=":",linewidth=1)
plt.show()