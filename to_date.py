import pandas as pd
df=pd.read_csv('data.csv')
df['Date']=pd.to_datetime(df['Date'],format='mixed')
print(df.to_string())
# this code will give error because we dont have date column in our csv data
