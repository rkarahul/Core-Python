num = int(input("Enter the number"))
sum = 0
while(num>0):
    r = num % 10
    sum = sum + r
    num = num // 10
print(sum)