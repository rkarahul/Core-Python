from array import *
count = 0
array_num = array("i",[])
frq = array("i",[])
n = int(input("Enter the Total Number of array"))
for i in range(n):
    array_num.append(int(input("Enter the element")))


print("Fist Array ", end=" ")
for j in range(len(array_num)):
    # print(array_num[j],end=' ')
    for k in range(len(array_num)):
        if(array_num[j] == array_num[k]):
            count = count+1
            frq.append(count)

    print()
for l in range(len(frq)):
    print(frq[l],end=" ")


