import pandas as p
csv_data=p.read_csv("data.csv")
print(csv_data)   #it show data but from start and  middle data is hide and then show last data  
# Pandas will only return the first 5 rows, and the last 5 rows
print(csv_data.to_string()) #it shows all data  