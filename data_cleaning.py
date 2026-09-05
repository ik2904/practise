import pandas as pd
df=pd.read_csv('data.csv')
ndf=df.dropna()
print(ndf.to_string())
