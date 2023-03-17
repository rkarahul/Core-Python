num = int(input("Enter the number"))
p = 1
while(num>0):
    p = p*(num % 10)
    num = num //10
print("Product of the digits number is :",p)
