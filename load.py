import pandas as p
csv_data=p.read_csv("data.csv")
#it show data but from start and  middle data is hide and then show last data  
# Pandas will only return the first 5 rows, and the last 5 rows
print(csv_data)   
 #it shows all data  
# print(csv_data.to_string())
print(p.options.display.max_rows)
# use to increase the rows in system 
p.options.display.max_rows = 9999

df = p.read_csv('data.csv')

print(df) 
