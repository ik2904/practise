import pandas as pf
week={
    "weeday":["M","T","W"],
    "weekend":["F","SA","SUN"]


}
DF=pf.Series(week)
print(DF)