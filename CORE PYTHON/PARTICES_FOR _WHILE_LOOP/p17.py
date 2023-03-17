sum1 = 0
sum2 = 0
f = int(input("Enter the number"))
l = int(input("enter the number "))
for i in range(f,l+1):
    if(i % 2 == 0):

        sum1 = sum1 +i
    else:
        sum2 = sum2 +i
print(sum1)
print(sum2)
        