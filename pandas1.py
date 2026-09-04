import pandas as p

# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }

# myvar = p.DataFrame(mydataset)

# # print(myvar)
# print(p.__version__)
#

# series__--------------------------------------------------->
# series is like a column in a table 
# a = [1, 7, 2]

# myvar = p.Series(a,index=[10,9,8])

# print(myvar)
# print(myvar[10])

# key value pair as series
# days={"day1":"monday","day2":"tuesday","day3":"wednesday"}
# day=p.Series(days)
# print(day)
# print(day["day2"])

# DATA  FRAME-------------------------->>>>>>>>
week={
"weekday":["monday","tuesday","wednesday","thursday"],

"weekend":["friday","saturday","sunday","monady"]

}
# w1=p.DataFrame(week)
# # print(w1)
# print(w1.loc[[1,2]])
# # print(w1.loc[1])



# "saturday","sunday"

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = p.DataFrame(data, index = ["day1", "day2", "day3"])

print(df.loc["day2"])
