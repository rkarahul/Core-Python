#copy array in first to second
from array import *
array_num = array("i",[])
n = int(input("Enter the total number"))
for i in range(n):
    array_num.append(int(input("Enter the number")))

print("original array ",end=" ")
for i in range(len(array_num)):
    print(array_num[i], end=" ")

print("\n new array",end=" ")
copy_array = array("i",[])
for j in range(len(array_num)):
   copy_array.append(array_num[j])
   print(copy_array[j],end=" ")
