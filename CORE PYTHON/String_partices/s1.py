str = str(input("Enter the sentences"))
n = len(str)
print("**************     Orginal String    ************** ")
for i in range(n):
    print(str[i],end=" \t")
print()
print()
print("**************  After Reverse String  *************   ")
for j in range(i,-1,-1):
    print(str[j],end="\t")

