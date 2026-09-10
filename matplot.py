import matplotlib.pyplot as plt
import numpy as np
# xaxis=np.array([1,2,4,6,8,10,12,14,15])
# yaxis=np.array([2,5,2,5,2,5,2,5,2])

# plt.plot(yaxis)
# plt.plot(xaxis,yaxis,marker='D',ls="dotted")


font1 = {'color':'purple','size':15}



# plt.xlabel("distance")
# plt.ylabel("time")

# x=np.array([1,2,4,6,8,10,12,14,15])
# y=np.array([2,5,2,5,2,5,2,5,2])
# plt.subplot(2,1,1)
# plt.plot(x,y)
# plt.title("this is plot 1 ")
# x1=np.array([1,3,1,6,9,10,12,14,15])
# y1=np.array([2,5,2,5,2,5,2,5,2])
# plt.subplot(2,1,2)
# plt.plot(x,y)
# plt.title("this is plot 2",loc='right')
plt.suptitle("this is two plot")



# plt.title("showing distance and time",fontdict=font1,loc='right')
# plt.grid(color="red",ls=":",linewidth=1)

# THIS IS EXAMPLES OF SCATTER PLOT

# x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
# y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
# plt.scatter(x, y,color="hotpink")

# #day two, the age and speed of 15 cars:
# x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
# y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
# plt.scatter(x,y,c='#FFBF00')



# THIS IS NOW EXAMPLE OF BAR GRAPGH
# x=np.array(["student 1","student2","student3","student4","student5"])
# y=np.array([3,1,2,1,10])
# # plt.bar(x,y)
# # plt.bar(x,y,color="hotpink", width=0.5)




# THIS IS THE EXAMPLE OF HISTOGRAM
# x = [10, 12, 12, 15, 16, 17, 17, 18, 20, 22]
# plt.hist(x)

x=np.array([30,15,22,11,50])
y=["maths","science","social science","hindi","english"]
mexplode=[0.1,0.1,0.1,0.1,0.1]
plt.pie(x,labels=y ,explode=mexplode)



plt.show()



