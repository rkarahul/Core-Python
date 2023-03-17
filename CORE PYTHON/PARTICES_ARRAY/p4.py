# resverse the array 
from array import *
num = array("i",[1,3,4,5,3,9,1])
print("orginal array",num)
num.reverse()
print("resverse array",num)

print ("*************************** OR **************************")
array_num = array("i",[1,3,5,6,8,9,1,2])
print("This is orginal array")
print(array_num)

print("this is reverse array")
for i in range(len(array_num)-1,-1,-1):
    print(array_num[i],end=" ")

