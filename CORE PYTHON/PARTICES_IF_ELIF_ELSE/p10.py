# write a program to check leap year or not
y = int(input("Enter the Year"))
if(y % 400 == 0 ):
    print("This is leap year")
elif(y % 4 == 0 and y % 100 != 0):
    print("this is leap Year")
else:
    print("this is not leap year")