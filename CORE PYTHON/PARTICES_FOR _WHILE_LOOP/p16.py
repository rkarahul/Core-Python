f = int(input("Enter the First Number"))
l = int(input("Enter the last number"))
for num in range(f,l+1):
    count =0
    for i in range(1,num+1):
        if(num%i)==0:
            count = count+1
    if count==2:
        print(num)

