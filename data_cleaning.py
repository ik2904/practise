import pandas as pd
df=pd.read_csv('data.csv')
# ndf=df.dropna()
# print(ndf.to_string())
# df.dropna(inplace=True)
# print(df.to_string())
# df.fillna(2004,inplace =True)

ndf=df.fillna(2004)
print(ndf.to_string())