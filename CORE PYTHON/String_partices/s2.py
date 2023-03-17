str = """ hello guys i am rahul"""
n = len(str)
for i in range(n):
    print(str[i],end=" ")

print()
for j in range(i,-1,-1):
    print(str[j],end=" ")
print()
for k in range (j,0,-1):
    print(str[k])