# Sum of array number
from array import *
sum = 0
array_num =array("i",[])
n = int(input("Enter the total number"))
for i in range(n):
    array_num.append(int(input("Enter the number")))
for j in range(len(array_num)):
    sum = sum + array_num[j]
print("sum of the array number",sum)
