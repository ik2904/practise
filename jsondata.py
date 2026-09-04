import pandas as pd
show=pd.read_json("data.json")
# print(show)
# print(show.to_string())
print(show.head(20))
print(show.tail(2))
print(show.info())