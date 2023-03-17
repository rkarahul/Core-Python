import pandas as pd

s = pd.Series(12,index=[1,2,3,4,5,6,7])
s1 = pd.Series(12, index=[1, 2, 3, 4, 5])
print(s+s1)
print(type(s))