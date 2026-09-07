import pandas as pd
df= pd.read_csv('data.csv')
# for x in df.index:
#     if df.loc[x, "Pulse"] <100:
#         # df.loc[x,"Pulse"] =2000
#         df.drop(x,inplace= True)

# print(df.to_string())
print(df.duplicated())
df.drop_duplicates(inplace=True)
print(df.to_string())
