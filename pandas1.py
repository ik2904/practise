import pandas as p

# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }

# myvar = p.DataFrame(mydataset)

# # print(myvar)
# print(p.__version__)



a = [1, 7, 2]

myvar = p.Series(a,index=["10","9","8"])

print(myvar)