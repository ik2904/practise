import pandas as pf
import matplotlib.pyplot as plt

df=pf.read_json('data.json')
# df.plot()
df.plot(kind = 'scatter', x = 'Calories', y = 'Duration')

plt.show()