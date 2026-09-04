import numpy as np
from statistics import mode
# dice=np.random.choice([1,2,3,4,5,6],size=2)
# even=np.sum((dice==2)|(dice==4)|(dice==6))
# probability=even/2
# print(probability)
data = np.array([1,2,3,4,5,6,6,4,4,4,4,])

median = np.median(data)

print(median)
mode1=mode(data)
print(mode1)
st=np.std(data)
print(st)