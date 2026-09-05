import pandas as p
df=p.read_csv('data.csv')
x=df['Calories'].mean()
df.fillna(x,inplace= True)
print(x)
print(df)