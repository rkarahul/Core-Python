num = int(input("Enter the number"))
count = 0
if (num==1 or num==0):
    count = 1
for i in range(2,num):
    if(num%i==0):
        count = 1
if (count==1):
    print("This is not prime number")
else:
    print("this is prime number")