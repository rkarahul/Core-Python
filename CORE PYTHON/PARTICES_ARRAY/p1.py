from array import *
stu_roll = array("i",[])
n = int(input("how many element"))
for i in range(n):
    stu_roll.append(int(input("Enter the element")))
for j in range(len(stu_roll)):
    print(stu_roll[j])